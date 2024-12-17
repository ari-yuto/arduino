import numpy as np
import matplotlib.pyplot as plt
import FuncAni
import openpyxl
import datetime

time = datetime.datetime.now().strftime('%m-%d-%H-%M-%S')

excel_path = rf"/Users/ariyoshiyuto/GitHub/arduino/Graduation thesis/SerialTest/excel/{time}.xlsx"

# フーリエ変換
fft_data_x = np.abs(np.fft.rfft(FuncAni.X_data_accel)).tolist()  # 絶対値
fft_data_y = np.abs(np.fft.rfft(FuncAni.Y_data_accel)).tolist()  # 絶対値
fft_data_z = np.abs(np.fft.rfft(FuncAni.Z_data_accel)).tolist()  # 絶対値
freqList = np.fft.rfftfreq(len(FuncAni.X_data_accel), 1.0 / 67).tolist()  # 横軸



fft_datas = [fft_data_x, fft_data_y, fft_data_z, FuncAni.y_data_press[-200:-1]]

wb = openpyxl.Workbook()
sheet = wb.worksheets[0]

for row in fft_datas :
    sheet.append(row)

wb.save(excel_path)
wb.close()

plt.subplot(3, 1, 1)
plt.plot(freqList, fft_data_x, color='blue')
plt.legend(['X'])

plt.subplot(3, 1, 2)
plt.plot(freqList, fft_data_y, color='orange')
plt.legend(['Y'])

plt.subplot(3, 1, 3)
plt.plot(freqList, fft_data_z, color='green')
plt.legend(['Z'])

plt.xlabel('Frequency')
plt.ylabel('Power')

plt.tight_layout()

plt.show()

