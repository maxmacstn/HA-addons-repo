import json, os

mjpeg_template = """#!/bin/bash
echo "Content-Type: multipart/x-mixed-replace;boundary=ffmpeg"
echo "Cache-Control: no-cache"
echo ""
ffmpeg -rtsp_transport tcp -i "<url>" -c:v mjpeg -q:v 1 -f mpjpeg -an - -hide_banner -loglevel error"""

image_template = """#!/bin/bash
echo "Content-Type: image/jpeg"
echo "Cache-Control: no-cache"
echo ""
ffmpeg -rtsp_transport tcp -i "<url>" -vframes 1 -f image2pipe -an - -hide_banner -loglevel error"""

#check if path exists
web_path = "/var/www/localhost/cgi-bin/"


# Opening JSON file
f = open('/data/options.json')

# returns JSON object as
# a dictionary
data = json.load(f)

for camera in data['cameras']:
    mjpeg_path = web_path+camera['name'].replace(" ","-") +"/mjpeg.cgi"
    os.makedirs(os.path.dirname(mjpeg_path), exist_ok=True)
    cgi_mjpeg = open(mjpeg_path, "w")
    content = mjpeg_template.replace("<url>", camera['url'])
    cgi_mjpeg.write(content)
    cgi_mjpeg.close
    os.chmod(mjpeg_path, 0o775)

    image_path = web_path+camera['name'].replace(" ","-") +"/image.cgi"
    cgi_image = open(image_path, "w")
    content = image_template.replace("<url>", camera['url'])
    cgi_image.write(content)
    cgi_image.close
    os.chmod(image_path, 0o775)

    print("Created MJPEG cgi for "+camera['name']+": http://<host-ip-address>:9090/cgi-bin/"+camera['name'].replace(" ","-") +"/mjpeg.cgi")
    print("Created IMAGE cgi for "+camera['name']+": http://<host-ip-address>:9090/cgi-bin/"+camera['name'].replace(" ","-") +"/image.cgi")

# Closing file
f.close()