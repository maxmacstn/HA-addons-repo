#!/bin/bash

echo "Content-Type: multipart/x-mixed-replace;boundary=ffmpeg"
echo "Cache-Control: no-cache"
echo ""
ffmpeg -i "rtsp://admin:xxxxxxx@192.168.1.xx/cam/realmonitor?channel=1&subtype=00" -c:v mjpeg -q:v 1 -f mpjpeg -an -
