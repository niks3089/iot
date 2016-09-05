#!/bin/bash
sudo chmod 666 /dev/video0
sudo touch /tmp/image.jpg
sudo chmod 777 /tmp/image.jpg
fswebcam -r 1280x720 -S 20 /tmp/image.jpg
if  [ $? -eq 0 ]; then
    echo "Content-type: text/html"
    echo ""
    echo "<html><head><title>IoT Wifi Photo capture</title></head><body>"
    echo "Successfully took photo<br>"
    echo "Shell Script name is $0"
    echo "</body></html>"
else
    echo "Content-type: text/html"
    echo ""
    echo "<html><head><title>IoT Wifi Photo capture</title></head><body>"
    echo "Failed to take photo<br>"
    echo "Shell Script name is $0"
    echo "</body></html>"
fi
