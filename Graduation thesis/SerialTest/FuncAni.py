import json
import serial
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ser = serial.Serial('/dev/tty.usbmodem11301', 9600)

# リアルタイムでプロットするためのリスト

x_data_press = []
y_data_press = []

x_data_CapSen = []
y_data_CapSen = []

x_data_time_accel = []
X_data_accel = []
Y_data_accel = []
Z_data_accel = []

x_data_time_gyro = []
X_data_gyro = []
Y_data_gyro = []
Z_data_gyro = []

# 図の設定
fig_press, ax_press = plt.subplots()
line_press, = ax_press.plot([], [], lw=2)

fig_CapSen, ax_CapSen = plt.subplots()
line_CapSen, = ax_CapSen.plot([], [], lw=2)

fig_accel, ax_accel = plt.subplots()
line_accel_X, = ax_accel.plot([], [], lw=2, label='X')
line_accel_Y, = ax_accel.plot([], [], lw=2, label='Y')
line_accel_Z, = ax_accel.plot([], [], lw=2, label='Z')

fig_gyro, ax_gyro = plt.subplots()
line_gyro_X, = ax_gyro.plot([], [], lw=2, label='X')
line_gyro_Y, = ax_gyro.plot([], [], lw=2, label='Y')
line_gyro_Z, = ax_gyro.plot([], [], lw=2, label='Z')


#　初期化関数
def init():
    ax_press.set_xlim(0, 100)  # x軸の範囲
    ax_press.set_ylim(0, 1024)  # y軸の範囲（アナログ値の場合）

    ax_CapSen.set_xlim(0, 100)  # x軸の範囲
    ax_CapSen.set_ylim(0, 100)  # y軸の範囲（アナログ値の場合）

    ax_accel.set_xlim(0, 100)  # x軸の範囲
    ax_accel.set_ylim(-1.5, 1.5)  # y軸の範囲（アナログ値の場合）

    ax_gyro.set_xlim(0, 100)  # x軸の範囲
    ax_gyro.set_ylim(-10, 10)  # y軸の範囲（アナログ値の場合）

    return line_press, line_CapSen, line_accel_X, line_accel_Y, line_accel_Z, line_gyro_X, line_gyro_Y, line_gyro_Z

def update_press(frame):
    # data = ser.readline().decode().strip()  # Arduinoからデータを読み込む
    val_arduino = ser.readline()
    data = pd.json_normalize(eval(val_arduino.decode()))
    y_data_press.append(float(data['DO']))
    x_data_press.append(int(data['time']))  # 自動的にx軸のデータを更新
    line_press.set_data(x_data_press, y_data_press)
    if int(data['time']) > 100:
        ax_press.set_xlim(int(data['time'])-100,int(data['time']) )  # x軸を更新  
    else:
        ax_press.set_xlim(0, int(data['time']))  # x軸を更新

    return line_press,

def update_CapSen(frame):
    val_arduino = ser.readline()
    data = pd.json_normalize(eval(val_arduino.decode()))
    y_data_CapSen.append(float(data['D1']))
    x_data_CapSen.append(int(data['time']))  # 自動的にx軸のデータを更新
    line_CapSen.set_data(x_data_CapSen, y_data_CapSen)
    print(data['D1'])
    if int(data['time']) > 100:
        ax_CapSen.set_xlim(int(data['time'])-100,int(data['time']) )  # x軸を更新  
    else:
        ax_CapSen.set_xlim(0, int(data['time']))  # x軸を更新
    
    return line_CapSen,

def update_accel(frame):
    val_arduino = ser.readline()
    data = pd.json_normalize(eval(val_arduino.decode()))
    X_data_accel.append(float(data['X_accel']))
    Y_data_accel.append(float(data['Y_accel']))
    Z_data_accel.append(float(data['Z_accel']))
    x_data_time_accel.append(int(data['time']))  # 自動的にx軸のデータを更新
    line_accel_X.set_data(x_data_time_accel, X_data_accel)
    line_accel_Y.set_data(x_data_time_accel, Y_data_accel)
    line_accel_Z.set_data(x_data_time_accel, Z_data_accel)
    if int(data['time']) > 100:
        ax_accel.set_xlim(int(data['time'])-100,int(data['time']) )  # x軸を更新  
    else:
        ax_accel.set_xlim(0, int(data['time']))  # x軸を更新
    
    return line_accel_X, line_accel_Y, line_accel_Z

def update_gyro(frame):
    val_arduino = ser.readline()
    data = pd.json_normalize(eval(val_arduino.decode()))
    X_data_gyro.append(float(data['X_gyro']))
    Y_data_gyro.append(float(data['Y_gyro']))
    Z_data_gyro.append(float(data['Z_gyro']))
    x_data_time_gyro.append(int(data['time']))  # 自動的にx軸のデータを更新
    line_gyro_X.set_data(x_data_time_gyro, X_data_gyro)
    line_gyro_Y.set_data(x_data_time_gyro, Y_data_gyro) 
    line_gyro_Z.set_data(x_data_time_gyro, Z_data_gyro)
    if int(data['time']) > 100:
        ax_gyro.set_xlim(int(data['time'])-100,int(data['time']) )  # x軸を更新  
    else:
        ax_gyro.set_xlim(0, int(data['time']))  # x軸を更新
    
    return line_gyro_X, line_gyro_Y, line_gyro_Z


ani_press = FuncAnimation(fig_press, update_press, init_func=init, blit=True , interval=53)
ani_CapSen = FuncAnimation(fig_CapSen, update_CapSen, init_func=init, blit=True , interval=100)
ani_accel = FuncAnimation(fig_accel, update_accel, init_func=init, blit=True , interval=53)
ani_gyro = FuncAnimation(fig_gyro, update_gyro, init_func=init, blit=True , interval=53)

plt.legend()

plt.show()




