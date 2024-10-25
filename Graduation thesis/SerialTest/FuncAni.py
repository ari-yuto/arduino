import json
import serial
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ser = serial.Serial('/dev/tty.usbmodem1301', 9600)

# リアルタイムでプロットするためのリスト
x_data = []
y_data = []

# 図の設定
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

#　初期化関数
def init():
    ax.set_xlim(0, 100)  # x軸の範囲
    ax.set_ylim(0, 1024)  # y軸の範囲（アナログ値の場合）
    return line,

def update(frame):
    # data = ser.readline().decode().strip()  # Arduinoからデータを読み込む
    val_arduino = ser.readline()
    data = pd.json_normalize(eval(val_arduino.decode()))
    # print(data)
    y_data.append(float(data['DO']))
    x_data.append(len(y_data))  # 自動的にx軸のデータを更新
    line.set_data(x_data, y_data)
    ax.set_xlim(0, len(y_data))  # x軸を更新
    return line,

# while True:
#     val_arduino = ser.readline()
#     # text = json.loads(val_arduino.decode())
#     # print(text)
#     data = pd.json_normalize(eval(val_arduino.decode()))
#     Time = data['time']
#     press = data['DO']
#     CapSen= data['D1']
    
#     if len(x_data) > 0:
#         x_data.pop(0)
#         y_data.pop(0)
#         ani = FuncAnimation(fig, update, init_func=init, blit=True)
#         plt.show()

    # print(Time, press)


    # plt.plot(Time, press)
    # plt.pause()

ani = FuncAnimation(fig, update, init_func=init, blit=True , interval=50)
plt.show()




