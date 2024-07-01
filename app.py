import json
import random
import time
from datetime import datetime
import re
import csv
# import socket
from flask import Flask, Response, render_template, stream_with_context, jsonify, request

application = Flask(__name__)
random.seed()  # Initialize the random number generator

raspi_data = None
raspi_data1 = None

def generate_data():
    # raspberrypiData = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # raspberrypiData.connect(('192.168.11.90', 5000)) read/write
    # data_decode = (raspberrypiData.recv(1024).decode('utf-8'))
    # print("data_decode", data_decode)
    data_decode = "25.0 50.0 1013.25"
    return data_decode

@application.route('/post', methods=['POST', 'GET'])
def post_handler():
    # raspiがここにrequestを送る。。。。
    data = request.data.decode('utf-8')
    print("data",data)
    global raspi_data
    time.sleep(10)
    raspi_data = data
    # split = re.split('\s+', a)
    # print("asdasdasdas",split) # should display 'bar'
    # temperature = (split[0])
    # sensor = [
    #         {
    #             "temperature": temperature,
    #         }
    #     ]
    return "data receive"

@application.route('/post1', methods=['POST', 'GET'])
def post_handler1():
    # raspiがここにrequestを送る。。。。
    data1 = request.data.decode('utf-8')
    print("data1",data1)
    global raspi_data1
    time.sleep(10)
    raspi_data1 = data1
    # split = re.split('\s+', a)
    # print("asdasdasdas",split) # should display 'bar'
    # temperature = (split[0])
    # sensor = [
    #         {
    #             "temperature": temperature,
    #         }
    #     ]
    return "data receive"

def timer():
    t = time.time()  # UNIX時間（1970/01/01 00:00:00からの経過時刻）を取得
    local_time = time.localtime(t)  # ローカル時刻をtime.struct_time型として取得
    asc_time = time.asctime(local_time)  # 上のlocal_timeを文字列表現に変換
    dt = datetime.now().strptime(asc_time, '%a %b %d %H:%M:%S %Y')
    return dt

# def generate_data1():
#     raspberrypiData = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     raspberrypiData.connect(('192.168.11.75', 6000))
#     data_decode = (raspberrypiData.recv(1024).decode('utf-8'))
#     return data_decode

@application.route('/')
def index():
    split = re.split('\s+', raspi_data)
    split1 = re.split('\s+', raspi_data1)
    print("split", split)
    print("split1", split1) 
    temperature = float(split[0])
    humidity = float(split[1])
    pressure = float(split[2])
    temperature1 = float(split1[0])
    humidity1 = float(split1[1])
    pressure1 = float(split1[2])
    sensor = [
        {
            "temperature": temperature,
            "huminity": humidity,
            "pressure": pressure
        }
    ]
    sensor1 = [
        {
            "temperature": temperature1,
            "huminity": humidity1,
            "pressure": pressure1
        }
    ]
    return render_template('index.html', text=sensor, text1=sensor1)

@application.route('/data')
def data():
    while True:
        split = re.split('\s+', raspi_data)
        print("split", split)
        temperature = float(split[0])
        print("temperature", temperature)
        humidity = float(split[1])
        pressure = float(split[2])
        data = [
            {
                "temperature": temperature,
                "huminity": humidity,
                "pressure": pressure,
            }
        ]
        return jsonify(data)
    
@application.route('/data1')
def data1():
    while True:
        split1 = re.split('\s+', raspi_data1)
        print("split", split1)
        temperature = float(split1[0])
        print("temperature", temperature)
        humidity = float(split1[1])
        pressure = float(split1[2])
        data1 = [
            {
                "temperature": temperature,
                "huminity": humidity,
                "pressure": pressure,
            }
        ]
        return jsonify(data1)

@application.route('/chart-data')
def chart_data():
    def generate_random_data():
        data = []
        while True:
            nowtime = timer()
            split = re.split('\s+', raspi_data)
            split1 = re.split('\s+', raspi_data1)
            print("split", split)
            print("split1", split1) 
            temperature = float(split[0])
            humidity = float(split[1])
            pressure = float(split[2])
            temperature1 = float(split1[0])
            data.append([nowtime, temperature, humidity, pressure])
            suujirandom = random.randrange(25, 27)
            print("suujirandom", suujirandom)
            with open('sample.csv', 'w', newline="") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': temperature, 'value1': humidity, 'value2': temperature1})
            yield f"data:{json_data}\n\n"
            time.sleep(10)
    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

@application.route('/chart-data1')
def chart_data1(): 
    def generate_random_data():
        while True:
            split = re.split('\s+', raspi_data)
            split1 = re.split('\s+', raspi_data1)
            print("split", split)
            print("split1", split1) 
            humidity = float(split[1])
            humidity1 = float(split1[1])
            json_data = json.dumps({'time': datetime.now().strftime('%H:%M:%S'), 'value': humidity, 'value1': humidity1})
            yield f"data:{json_data}\n\n"
            time.sleep(10)
    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

@application.route('/chart-data2')
def chart_data2():
    def generate_random_data():
        while True:
            split = re.split('\s+', raspi_data)
            split1 = re.split('\s+', raspi_data1)
            print("split", split)
            print("split1", split1) 
            pressure = float(split[2])
            pressure1 = float(split1[2])
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': pressure, 'value1': pressure1})
            yield f"data:{json_data}\n\n"
            time.sleep(10)
    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=80)