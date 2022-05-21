# Live stream vision ML from Raspberry Pi

This is a basic app that streams image results from a vision ML
model (face detection) to a web page, using aiymakerkit for
ML inferencing and Flask for the web server.

## Requirements

+ Raspberry Pi with a camera (Pi Camera or USB camera)
+ Coral USB Accelerator
+ [Flask](https://pypi.org/project/Flask/) and
    [aiymakerkit](https://github.com/google-coral/aiy-maker-kit)
    (simple solution: flash the [AIY Maker Kit system
    image](https://aiyprojects.withgoogle.com/maker/#setup--1-flash-the-sd-card))

## Setup

Run the following commands on your Raspberry Pi (assuming you already
have Flask and aiymakerkit).

1. Clone this repo and navigate into it:

        git clone https://github.com/scottamain/makerkit-video-stream && cd makerkit-video-stream

2. Download the face detection model:

        bash download_model.sh

3. Start the server:

        python3 app.py

4. From another computer on the same network, open a browser and enter
the Raspberry Pi IP address (run `hostname -I` on the Raspberry Pi to find it), plus
port 8000. So it might be something like http://192.168.86.42:8000.

    You can also see it from on the Raspberry Pi at http://localhost:8000.