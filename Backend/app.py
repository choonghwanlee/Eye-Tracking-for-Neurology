import numpy as np
from flask import Flask, Response, request, jsonify
from io import BytesIO
import base64
from flask_cors import CORS, cross_origin
import skvideo.io
from GazeTracking.gaze_tracking import GazeTracking
import os
import sys

app = Flask(__name__)
cors = CORS(app)


def data_extractor(video_file):
    # convert video_file to list of numpy arrays (one for each frame)
    videogen = skvideo.io.vreader(video_file)
    # create an instance of GazeTracking
    gaze = GazeTracking()
    coords = []
    for frame in videogen:
        gaze.refresh(frame)
        if gaze.pupils_located():
            left_tuple = gaze.pupil_left_coords()
            right_tuple = gaze.pupil_right_coords()
        coords.append([left_tuple,right_tuple])
    return coords


@app.route("/video", methods=['GET', 'POST'])
def video():
    if(request.method == "POST"):
        bytesOfVideo = request.get_data()
        # y = np.frombuffer(bytesOfVideo, dtype=np.ndarray)
        with open('video.mp4', 'wb') as out:
            out.write(bytesOfVideo)
        coords = data_extractor('video.mp4')
        return jsonify(coords)

@app.route("/")
def hello_world():
    return 'Hello, World!'

