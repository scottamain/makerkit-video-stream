# Live stream vision ML from Raspberry Pi

This is a basic app showing how to stream results from a vision ML
(face detection) model, using flask as the server and aiymakerkit for
the ML inferencing.

## Dependencies

+ Raspberry Pi with a camera (Pi Camera or USB camera)
+ Coral USB Accelerator
+ [Flask](https://pypi.org/project/Flask/) and
    [aiymakerkit](https://github.com/google-coral/aiy-maker-kit)
    (simple solution: flash the [AIY Maker Kit system
    image](https://aiyprojects.withgoogle.com/maker/#setup--1-flash-the-sd-card))

## Setup

Run the following commands on your Raspberry Pi (assuming you already
have Flask and aiymakerkit).

First clone this repo:

        git clone https://github.com/scottamain/makerkit-video-stream

Chand dirs into the repo and start the server:

        cd makerkit-video-stream

        python3 app.py

Then, from another computer on the same network, open a browser and enter
the Raspberry Pi IP address (run `hostname -I` on the Raspberry Pi to find it).
It might be something like http://192.168.86.42.