import Flask as flask

#Import necessary libraries
from flask import Flask, render_template, Response
import cv2
#Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"
