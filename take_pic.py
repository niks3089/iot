#!/usr/bin/python
import cgitb
import subprocess

cgitb.enable()
print "Content-Type: text/plain\r\n\r\n"
subprocess.Popen(["fswebcam", "-r 1280x720", "-S 20", "/tmp/image.jpg"],
        stderr=subprocess.STDOUT)
