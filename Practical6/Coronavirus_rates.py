# make freqeucy directionary
My_dict={}
Countries = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924, 'Others':59959870}
# making pie chart
import matplotlib.pyplot as plt
labels = 'USA', 'Inddia', 'Brazil', 'Russia', 'UK', 'Others'
sizes = [29862124, 11285561, 11205972, 4360823, 4234924, 59959870]
explode = (0,0,0,0,0,0)
colors = ['red', 'yellow', 'green', 'lightskyblue', 'yellowgreen', 'pink']
# text1 outside, text2 inside, autopct数值保留固定小数位，shadowF无阴影设置，startangle逆时针其实角度设置，pctistance数值距圆心半径倍数距离
pathes,text1,text2 = plt.pie(sizes, explode=explode, labels=labels,colors=colors, autopct='%1.1f%%', shadow=False, startangle=90, pctdistance = 0.6)
# x,y轴刻度设置一致保证饼图为圆形
plt.axis('equal')
plt.title('Covid-19 patients in the world')
plt.show()
