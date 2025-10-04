@echo off
echo بدء بث الشاشة عبر FFmpeg...
cd /d "C:\Users\Dark Rove\Documents\ffmpeg-8.0-essentials_build\ffmpeg-8.0-essentials_build\bin"

ffmpeg -f gdigrab -framerate 30 -offset_x 0 -offset_y 0 -video_size 1920x1080 -i desktop -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -r 30 -g 60 -keyint_min 60 -b:v 2M -maxrate 2M -bufsize 1M -f flv "rtmp://127.0.0.1:1935/desktop"

pause