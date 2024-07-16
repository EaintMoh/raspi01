import json
import random
import time
from datetime import datetime
import re
import csv
# import socket
import sqlite3
import matplotlib.pyplot as plt
# import japanize_matplotlib
from flask import Flask, Response, render_template, stream_with_context, jsonify, request

app = Flask(__name__)

plt.rcParams["font.size"] = 14
fig, ax = plt.subplots(facecolor='white')
ax.plot(['月', '火' , '水'], [11, 44, 9], label='気温', marker='o')
ax.plot(['月', '火' , '水'], [12, 10, 13], label='湿', marker = 'o')
ax.set_xlabel('曜日')
ax.set_ylabel('気温', rotation='horizontal')
ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
ax.grid()
ax.legend()

if __name__ == "__main__":
    app.run()