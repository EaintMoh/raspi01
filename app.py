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

application = Flask(__name__, static_folder='./images/')
random.seed()  # Initialize the random number generator
raspi_data = '0 0 0'
raspi_data1 = '0 0 0'
sensordata = 0

# # conn = sqlite3.connect('sensor.db')
# conn1 = sqlite3.connect('sensor4.db')
# # cur = conn.cursor()
# cur1 = conn1.cursor()
# # cur.execute('INSERT INTO sensor (day, temperature, humidity, pressure) VALUES (?,?,?,?)', (11,raspi_data,raspi_data,raspi_data))
# cur1.execute('INSERT INTO sensor (temperature, humidity, pressure) VALUES (?,?,?)', (raspi_data,raspi_data,raspi_data))
# cur1.execute('select * from sensor')
# # sensordata1 = cur.fetchall()
# sensordata2 = cur1.fetchall()
# # print("chenchenchen123212",cur.fetchall())
# # print("chenchen",sensordata1[100])
# print("chenchay123",sensordata2)
# conn1.commit()
# conn1.close()
def timer():
    t = time.time()  # UNIX時間（1970/01/01 00:00:00からの経過時刻）を取得
    local_time = time.localtime(t)  # ローカル時刻をtime.struct_time型として取得
    asc_time = time.asctime(local_time)  # 上のlocal_timeを文字列表現に変換
    dt = datetime.now().strptime(asc_time, '%a %b %d %H:%M:%S %Y')
    # dt = datetime.now().strptime(asc_time, '%a %b %d %H:%M:%S %Y')
    return dt

nowtime = timer()
conn1 = sqlite3.connect('sensor4.db')
# cur = conn.cursor()
cur1 = conn1.cursor()
# cur.execute('INSERT INTO sensor (day, temperature, humidity, pressure) VALUES (?,?,?,?)', (11,raspi_data,raspi_data,raspi_data))
# cur1.execute('INSERT INTO sensor (date, temperature, humidity, pressure) VALUES (?,?,?,?)', ("2024-07-11 24:00:00",27.69,77.99,1013.89))
# cur1.execute('select * from sensor where date = "2024-07-12 19:15:21" AND date = "2024-07-12 19:47:55"')
# cur1.execute('DELETE from sensor WHERE id = "1030"')
cur1.execute('select * from sensor where date = "2024-07-11 00:00:00" OR date = "2024-07-11 01:00:00" ')
# cur1.execute('select * from sensor where date = "2024-07-11 01:00:00" OR date = "2024-07-12 20:03:45"')
# sensordata1 = cur.fetchall()
sensordata2 = cur1.fetchall()
a1 = sensordata2[0][2]
a2 = sensordata2[0][3]
a3 = sensordata2[0][4]
a4 = sensordata2[1][2]
a5 = sensordata2[1][3]
a6 = sensordata2[1][4]
print("sensor", sensordata2)
print("chenchay1",a1)
print("chenchay2",a2)
print("chenchay3",a3)
cur1.execute('select * from sensor where date = "2024-07-11 20:00:00" OR date = "2024-07-11 03:00:00" ')
sensordata3 = cur1.fetchall()
b1 = sensordata3[0][2]
b2 = sensordata3[0][3]
b3 = sensordata3[0][4]
b4 = sensordata3[1][2]
b5 = sensordata3[1][3]
b6 = sensordata3[1][4]
print("sensor", sensordata3)
print("chenchay1",b1)
print("chenchay2",b2)
print("chenchay3",b3)
cur1.execute('select * from sensor where date = "2024-07-11 04:00:00" OR date = "2024-07-11 05:00:00" ')
sensordata4 = cur1.fetchall()
c1 = sensordata4[0][2]
c2 = sensordata4[0][3]
c3 = sensordata4[0][4]
c4 = sensordata4[1][2]
c5 = sensordata4[1][3]
c6 = sensordata4[1][4]
print("sensor", sensordata4)
cur1.execute('select * from sensor where date = "2024-07-11 06:00:00" OR date = "2024-07-11 07:00:00" ')
sensordata5 = cur1.fetchall()
d1 = sensordata5[0][2]
d2 = sensordata5[0][3]
d3 = sensordata5[0][4]
d4 = sensordata5[1][2]
d5 = sensordata5[1][3]
d6 = sensordata5[1][4]
print("sensor", sensordata5)
cur1.execute('select * from sensor where date = "2024-07-11 08:00:00" OR date = "2024-07-11 09:00:00" ')
sensordata6 = cur1.fetchall()
e1 = sensordata6[0][2]
e2 = sensordata6[0][3]
e3 = sensordata6[0][4]
e4 = sensordata6[1][2]
e5 = sensordata6[1][3]
e6 = sensordata6[1][4]
print("sensor", sensordata6)
cur1.execute('select * from sensor where date = "2024-07-11 10:00:00" OR date = "2024-07-11 11:00:00" ')
sensordata7 = cur1.fetchall()
f1 = sensordata7[0][2]
f2 = sensordata7[0][3]
f3 = sensordata7[0][4]
f4 = sensordata7[1][2]
f5 = sensordata7[1][3]
f6 = sensordata7[1][4]
print("sensor", sensordata7)
cur1.execute('select * from sensor where date = "2024-07-11 12:00:00" OR date = "2024-07-11 13:00:00" ')
sensordata8 = cur1.fetchall()
g1 = sensordata8[0][2]
g2 = sensordata8[0][3]
g3 = sensordata8[0][4]
g4 = sensordata8[1][2]
g5 = sensordata8[1][3]
g6 = sensordata8[1][4]
print("sensor", sensordata8)
cur1.execute('select * from sensor where date = "2024-07-11 14:00:00" OR date = "2024-07-11 15:00:00" ')
sensordata9 = cur1.fetchall()
h1 = sensordata9[0][2]
h2 = sensordata9[0][3]
h3 = sensordata9[0][4]
h4 = sensordata9[1][2]
h5 = sensordata9[1][3]
h6 = sensordata9[1][4]
print("sensor", sensordata9)
cur1.execute('select * from sensor where date = "2024-07-11 16:00:00" OR date = "2024-07-11 17:00:00" ')
sensordata10 = cur1.fetchall()
i1 = sensordata10[0][2]
i2 = sensordata10[0][3]
i3 = sensordata10[0][4]
i4 = sensordata10[1][2]
i5 = sensordata10[1][3]
i6 = sensordata10[1][4]
print("sensor", sensordata10)
cur1.execute('select * from sensor where date = "2024-07-11 18:00:00" OR date = "2024-07-11 19:00:00" ')
sensordata11 = cur1.fetchall()
j1 = sensordata11[0][2]
j2 = sensordata11[0][3]
j3 = sensordata11[0][4]
j4 = sensordata11[1][2]
j5 = sensordata11[1][3]
j6 = sensordata11[1][4]
print("sensor", sensordata11)
cur1.execute('select * from sensor where date = "2024-07-11 20:00:00" OR date = "2024-07-11 21:00:00" ')
sensordata12 = cur1.fetchall()
k1 = sensordata12[0][2]
k2 = sensordata12[0][3]
k3 = sensordata12[0][4]
k4 = sensordata12[1][2]
k5 = sensordata12[1][3]
k6 = sensordata12[1][4]
print("sensor", sensordata12)
cur1.execute('select * from sensor where date = "2024-07-11 22:00:00" OR date = "2024-07-11 23:00:00" ')
sensordata13 = cur1.fetchall()
l1 = sensordata13[0][2]
l2 = sensordata13[0][3]
l3 = sensordata13[0][4]
l4 = sensordata13[1][2]
l5 = sensordata13[1][3]
l6 = sensordata13[1][4]
print("sensor", sensordata13)
# plt.rcParams["font.size"] = 14
# fig, ax = plt.subplots(facecolor='white')
# ax.plot(['月', '火' , '水'], [a1, a2, a3], label='気温', marker='o')
# ax.plot(['月', '火' , '水'], [12, 10, 13], label='湿', marker = 'o')
# ax.set_xlabel('曜日')
# ax.set_ylabel('気温', rotation='horizontal')
# ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
# ax.grid()
# ax.legend()




aaa = sensordata2
# split = re.split('\s+', aaa)
# print("chenchenchen123212",cur.fetchall())
# print("chenchen",sensordata1[100])
conn1.commit()
conn1.close()


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
    time.sleep(1)
    nowtime = timer()
    split = re.split('\s+', data)
    # print("split", split)
    temperature = float(split[0])
    humidity = float(split[1])
    pressure = float(split[2])
    sensor = [
        {
            "temperature": temperature,
            "huminity": humidity,
            "pressure": pressure
        }
    ]
    global raspi_data
    raspi_data = data
    # conn = sqlite3.connect('sensor.db')
    # conn1 = sqlite3.connect('sensor4.db')
    # # cur = conn.cursor()
    # cur1 = conn1.cursor()
    # # cur.execute('INSERT INTO sensor (day, temperature, humidity, pressure) VALUES (?,?,?,?)', (11,raspi_data,raspi_data,raspi_data))
    # cur1.execute('INSERT INTO sensor (date, temperature, humidity, pressure) VALUES (?,?,?,?)', (nowtime,11,11,11))
    # cur1.execute('select * from sensor where date = "2024-07-12 19:15:21"')
    # # sensordata1 = cur.fetchall()
    # sensordata2 = cur1.fetchall()
    # aaa = sensordata2[0]
    # # print("chenchenchen123212",cur.fetchall())
    # # print("chenchen",sensordata1[100])
    # print("chenchay123",aaa)
    # conn1.commit()
    # conn1.close()
    # split = re.split('\s+', sensordata2)
    # print("split", split)
    # temperature = float(split[0])
    # humidity = float(split[1])
    # pressure = float(split[2])
    # sensor = [
    #     {
    #         "temperature": temperature,
    #         "huminity": humidity,
    #         "pressure": pressure
    #     }
    # ]
    # print("sensor", sensor)
    
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
    global raspi_data1
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


# def generate_data1():
#     raspberrypiData = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     raspberrypiData.connect(('192.168.11.75', 6000))
#     data_decode = (raspberrypiData.recv(1024).decode('utf-8'))
#     return data_decode

@application.route('/')
def index():
    split = re.split('\s+', raspi_data)
    split1 = re.split('\s+', raspi_data1)
    # print("split", split)
    # print("split1", split1) 
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
    plt.rcParams["font.size"] = 10
    fig, ax = plt.subplots(facecolor='white')
    xs = ['00:00', '01:00', '02:00' , '03:00','04:00','05:00','06:00','07:00','08:00','09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    ax.plot(xs, [a1, a4, b1, b4, c1, c4, d1, d4, e1, e4, f1, f4, g1, g4, h1, h4, i1, i4, j1, j4, k1, k4, l1, l4], label='開発ルーム', marker='o')
    ax.plot(xs, [a1, 28, 26,27,24,26,28,26,27,24,25,26,25,24,24,25,26,25,26,24,24,23,25,24], label='小会議室', marker = 'o')
    ax.set_title('温度',fontsize=25)
    ax.set_xticklabels(xs, rotation=60)
    # ax.set_ylabel(rotation='horizontal')
    ax.set_yticks([10, 15, 20, 25, 30, 35, 40])
    ax.grid()
    ax.legend()
    dirname = "images/"
    filename = dirname + "img.png"
    fig.savefig(filename)
    fig1, ax1 = plt.subplots(facecolor='white')
    ax1.plot(xs, [a2,a5,b2,b5,c2,c5,d2,d5,e2,e5,f2,f5,g2,g5,h2,h5,i2,i5,j2,j5,k2,k5,l2,l5], label='開発ルーム', marker='o')
    ax1.plot(xs, [a2,a5,b2,73,72,72,73,73,72,75,72,71,73,71,76,74,75,74,73,72,79,73,71,73], label='小会議室', marker = 'o')
    ax1.set_title('湿度',fontsize=25)
    ax1.set_xticklabels(xs, rotation=60)
    # ax.set_ylabel(rotation='horizontal')
    ax1.set_yticks([60, 65, 70, 75, 80, 85, 90])
    ax1.grid()
    ax1.legend()
    dirname1 = "images/"
    filename1 = dirname1 + "img1.png"
    fig1.savefig(filename1)
    fig2, ax2 = plt.subplots(facecolor='white')
    xs4 = ['00:00', '01:00', '02:00' , '03:00','04:00','05:00','06:00','07:00','08:00','09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    xs5 = ['00:00', '01:00', '02:00' , '03:00','04:00','05:00','06:00','07:00','08:00','09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    ax2.plot(xs, [a3,a6,b3,b6,c3,c6,d3,d6,e3,e6,f3,f6,g3,g6,h3,h6,i3,i6,j3,j6,k3,k6,l3,l6], label='開発ルーム', marker='o')
    ax2.plot(xs, [d3,c6,f3,1013.2,1014.2,1014,1014.6,1014,1014.5,1014.5,1013.2,1014.5,1013.8,1014.4,1013.5,1013,1013.5,1013.3,1013.1,1014.2,1014.3,1013.2,1013.6,1013.2], label='小会議室', marker = 'o')
    ax2.set_title('気圧', fontsize=25)
    ax2.set_xticklabels(xs, rotation=60)
    # ax.set_ylabel(rotation='horizontal')
    ax2.set_yticks([1010,1011,1012, 1013, 1014, 1015, 1016])
    ax2.grid()
    ax2.legend()
    dirname2 = "images/"
    filename2 = dirname2 + "img2.png"
    fig2.savefig(filename2)
    return render_template('index.html', text=sensor, text1=sensor1)

@application.route('/data')
def data():
        split = re.split('\s+', raspi_data)
        # print("split", split)
        temperature = float(split[0])
        if (temperature == 0):
            return
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
        split1 = re.split('\s+', raspi_data1)
        # print("split", split1)
        temperature = float(split1[0])
        if (temperature == 0):
            return
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

# @application.route('/chart-data')
# def chart_data():
#     def generate_random_data():
#             data = []
#         # while raspi_data != '0 0 0':
#             nowtime = timer()
#             split = re.split('\s+', raspi_data)
#             split1 = re.split('\s+', raspi_data1)
#             # print("split", split)
#             # print("split1", split1) 
#             temperature = float(split[0])
#             humidity = float(split[1])
#             pressure = float(split[2])
#             temperature1 = float(split1[0])
#             data.append([nowtime, temperature, humidity, pressure])
#             suujirandom = random.randrange(25, 27)
#             # print("suujirandom", suujirandom)
#             with open('sample.csv', 'w', newline="") as f:
#                 writer = csv.writer(f)
#                 writer.writerows(data)
#             json_data = json.dumps(
#                 {'time': datetime.now().strftime('%H:%M:%S'), 'value': temperature, 'value1': humidity, 'value2': temperature1})
#             yield f"data:{json_data}\n\n"
#             # time.sleep(10)
#     response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
#     response.headers["Cache-Control"] = "no-cache"
#     response.headers["X-Accel-Buffering"] = "no"
#     return response

# @application.route('/chart-data1')
# def chart_data1(): 
#     def generate_random_data():
#         # while raspi_data != '0 0 0':
#             split = re.split('\s+', raspi_data)
#             split1 = re.split('\s+', raspi_data1)
#             # print("split", split)
#             # print("split1", split1) 
#             humidity = float(split[1])
#             humidity1 = float(split1[1])
#             json_data = json.dumps({'time': datetime.now().strftime('%H:%M:%S'), 'value': humidity, 'value1': humidity1})
#             yield f"data:{json_data}\n\n"
#             # time.sleep(10)
#     response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
#     response.headers["Cache-Control"] = "no-cache"
#     response.headers["X-Accel-Buffering"] = "no"
#     return response

# @application.route('/chart-data2')
# def chart_data2():
#     def generate_random_data():
#         # while raspi_data != '0 0 0':
#             split = re.split('\s+', raspi_data)
#             split1 = re.split('\s+', raspi_data1)
#             # print("split", split)
#             # print("split1", split1) 
#             pressure = float(split[2])
#             pressure1 = float(split1[2])
#             json_data = json.dumps(
#                 {'time': datetime.now().strftime('%H:%M:%S'), 'value': pressure, 'value1': pressure1})
#             yield f"data:{json_data}\n\n"
#             # time.sleep(10)
#     response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
#     response.headers["Cache-Control"] = "no-cache"
#     response.headers["X-Accel-Buffering"] = "no"
#     return response


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=8000)