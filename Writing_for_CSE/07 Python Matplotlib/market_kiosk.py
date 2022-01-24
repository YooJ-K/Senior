import matplotlib.pyplot as plot
import numpy as np
from matplotlib import font_manager, rc
import matplotlib.patches as patches

x = ['1999', '2006', '2009', '2013', '2014', '2017', '2018']
y = [100, 600, 1000, 1800, 2000, 2500, 3000]
num = np.arange(7)
num_x = [1999, 2006, 2009, 2013, 2014, 2017, 2018]

font_path = "C:/Windows/Fonts/BATANG.TTC"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

plot.plot(num_x, y, 'ko-')
plot.title('국내 키오스크 시장 규모')
plot.xlabel('Year', loc='right')
plot.ylabel('Cost(단위 : 억원)', loc='top')
plot.xticks(num_x, x, rotation=30)
plot.grid(True)

plot.show()