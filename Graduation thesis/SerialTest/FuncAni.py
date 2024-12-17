import json
import serial
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

start = time.time()

ser = serial.Serial('/dev/tty.usbmodem11301', 9600)  # シリアル通信の設定

# リアルタイムでプロットするためのリスト

x_data_press = []
y_data_press = []

x_data_time_accel = []
X_data_accel = []
Y_data_accel = []
Z_data_accel = []

# 図の設定
plt.figure(figsize=(8, 3), dpi=100)
fig_press, ax_press = plt.subplots()
line_press, = ax_press.plot([], [], lw=2)

fig_accel, ax_accel = plt.subplots()
line_accel_X, = ax_accel.plot([], [], lw=2, label='X')
line_accel_Y, = ax_accel.plot([], [], lw=2, label='Y')
line_accel_Z, = ax_accel.plot([], [], lw=2, label='Z')

#　初期化関数
def init():
    ax_press.set_xlim(0, 200)  # x軸の範囲
    ax_press.set_ylim(0, 1024)  # y軸の範囲（アナログ値の場合）

    ax_accel.set_xlim(0, 100)  # x軸の範囲
    ax_accel.set_ylim(-1.5, 1.5)  # y軸の範囲（アナログ値の場合）

    return line_press, line_accel_X, line_accel_Y, line_accel_Z

def update_press(frame):
    val_arduino = ser.readline()
    data = pd.json_normalize(eval(val_arduino.decode()))
    y_data_press.append(float(data['DO']))
    x_data_press.append(int(data['time']))  
    line_press.set_data(x_data_press, y_data_press)
    if int(data['time']) > 200:
        ax_press.set_xlim(int(data['time'])-300,int(data['time']) )  # x軸を更新  
    else:
        ax_press.set_xlim(0, int(data['time']))  # x軸を更新

    return line_press

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
    if int(data['time']) > 200:
        ax_accel.set_xlim(int(data['time'])-200,int(data['time']) )  # x軸を更新  
    else:
        ax_accel.set_xlim(0, int(data['time']))  # x軸を更新

    return line_accel_X, line_accel_Y, line_accel_Z

# 保存用の終了関数
def stop_animation(*args):
    ser.close()  # シリアルポートを閉じる
    ani_press.event_source.stop()  # アニメーションを停止
    ani_accel.event_source.stop()  # アニメーションを停止

    # グラフを保存
    fig_press.savefig('press.png')
    fig_accel.savefig('accel.png')
    plt.close('all')  # すべてのプロットを閉じる

ani_press = FuncAnimation(fig_press, update_press, init_func=init, blit=True , interval=16,cache_frame_data=False)
ani_accel = FuncAnimation(fig_accel, update_accel, init_func=init, blit=True , interval=16,cache_frame_data=False)

# 自動停止するタイミングを設定
def stop_animation_after_time():
    if time.time() - start > 10:  # 10秒経過後
        stop_animation()

# 一定時間ごとにチェック
timer = fig_press.canvas.new_timer(interval=100)  # 100msごとに実行
timer.add_callback(stop_animation_after_time)
timer.start()

plt.legend()

plt.show()




