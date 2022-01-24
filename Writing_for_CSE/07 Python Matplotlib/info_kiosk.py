import matplotlib.pyplot as plot
import numpy as np
from matplotlib import font_manager, rc

x = ['전체', '은행 환전', '민원/안내', '공항/터미널/철도', '백화점/쇼핑몰/마트', '종합병원/약국', 
'도서관/서점', '음식점', '주유소/주차장', '대학', '공연장', '영화관', '체육관']
y = [64.5,82.0,70.3,68.3,63.8,61.6,61.6,61.2,61.0,60.7,59.3,57.9,59.6]
num = np.arange(13)

font_path = "C:/Windows/Fonts/BATANG.TTC"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

plot.title('2020 키오스크 정보접근성 현황 조사')
plot.bar(num, y)
plot.xticks(num, x, rotation=45)
plot.ylim(30, 90)
plot.grid(True)
plot.show()