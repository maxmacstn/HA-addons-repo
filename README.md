# Config camera sources

To config camera sources, go to configuration tab and enter your cameras RTSP URL.

Example

```
cameras:
  - name: cam_1
    url: rtsp://admin:admin2@192.168.1.xxx/cam/realmonitor?channel=1&subtype=00
```

# Viewing

You can obtain MJPEG url and still image url (jpeg) using the following urls

MJPEG:

```
http://<host-ip-address>:9090/cgi-bin/<name>/mjpeg.cgi
```

IMAGE:

```
http://<host-ip-address>:9090/cgi-bin/<name>/image.cgi
```

# Casting to Google Cast device
To cast the video stream to Google Cast devices (Google Nest Hub or Android TV). Call service `media_player.play_media` in Home Assistant with the following data:
```
service: media_player.play_media
data:
  media_content_id: http://<host-ip-address>:9090/cgi-bin/<name>/mjpeg.cgi
  media_content_type: image/jpeg
target:
  entity_id: media_player.your_google_cast_entity

```

___Make sure to stop the streaming or call service `media_player.media_stop` after finished watching the stream, otherwise it will continuously processing the stream and consuming your system's resources.___

# Security warnings
This integration does not encrypt or having any authentication for the stream. Therefore, anyone in the network can access and view the camera's live feed using the url. Make sure to use this add-on only in your private network. 


# Acknowledgements

This Home Assistant add-on is based on

- https://stevethemoose.blogspot.com/2021/07/converting-rtsp-to-mjpeg-stream-on.html
- https://github.com/piersfinlayson/rtspmpeg


