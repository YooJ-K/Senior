import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/BATANG.TTC"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

f = open('부산코로나.csv', 'rt', encoding='UTF8')
rdr = csv.reader(f)
date = list()
num = list()
for line in rdr:
    if line != []:
        date.append(line[0].split('일일')[0].strip())
        num.append(int(line[0].split('확진자')[1].strip().split('명')[0]))
f.close()

plt.title("영업 제한 조치 해제 후, 부산 코로나 확진자 수")
plt.scatter(date, num, label="original")
plt.xticks([d for i, d in enumerate(date) if d.split('-')[2]=='01' or i == 0 ], rotation=90)

def func(x, a, b, c, d):
    return a*pow(x,3) + b*pow(x, 2) + c * x + d

x = np.array([i for i in range(0, len(date))])
result_x, result_y = curve_fit(func, x, num)
plt.plot(x, func(x, *result_x), color="r", label="fitting")
plt.legend()

#print(func(164, *result_x)) 2021-12-01 확진자 수의 예상

plt.show()