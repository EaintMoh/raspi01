import os
from flask import Flask, render_template
import pandas as pd
import socket
import matplotlib.pyplot as plt
import streamlit as st
# import plotly.express as px
# import cv2
import numpy as np
from PIL import Image
import json
import random
import time
from datetime import datetime
import re
import csv
# import socket
import sqlite3
import matplotlib.pyplot as plt
import japanize_matplotlib
import mpl_finance as mpf
from flask import Flask, Response, render_template, stream_with_context, jsonify, request

app = Flask(__name__, static_folder='./templates/')
@app.route('/', methods=['GET','POST'])
@app.route('/start', methods=['GET','POST'])

def index():

    text = "こちらFlaskスネーク。応答せよ。"  
    while True:
        a = 11, 44, 9
        print(a)
        df = pd.DataFrame([a])
        df.to_csv('output.csv')
        # fig, ax = plt.subplots(facecolor="white")
        # ax.plot(['月','火','水','木','金','土','日'],[3,1,2,4,5,6,5])
        # CSVデータの読み込み
        # df = pd.read_csv("output.csv")
        plt.rcParams["font.size"] = 14
        fig, ax = plt.subplots(facecolor='white')
        xs = ['2021-01-01', '2021-01-02', '2021-01-03' , '2021-01-04','2021-01-05','2021-01-06','2021-01-07','2021-01-08','2021-01-09']
        ax.plot(['2021-01-01', '2021-01-02', '2021-01-03' , '2021-01-04','2021-01-05','2021-01-06','2021-01-07','2021-01-08','2021-01-09','9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], [10,11,11,12,11,15,16,15,14,14,15,12,13,15,16,13,15,12,13,14,17,15,12,14], label='開発ルーム', marker='o')
        ax.plot(xs, [12, 10, 13,12,15,12,15,12,11], label='小会議室', marker = 'o')
        ax.set_xticklabels(xs, rotation=30)
        ax.set_xlabel('曜日')
        ax.set_ylabel('気温', rotation=45)
        # ax.set_xticklabels(rotation=30)
        ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
        ax.grid()
        ax.legend()
        dirname = "templates/"
        filename = dirname + "img.png"
        fig.savefig(filename)
        return render_template('index1.html', text=text)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)