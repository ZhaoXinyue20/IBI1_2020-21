import matplotlib.pyplot as plt
# make freqeucy directionary
My_dict={}
Countries = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}
# making pie chart
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
# emphasize the UK part
explode = (0,0,0,0,0.1)
colors = ['red', 'yellow', 'green', 'lightskyblue', 'pink']
pathes,text1,text2 = plt.pie(sizes, #text1 outside, text2 inside
                             explode=explode,
                             labels=labels,
                             colors=colors,
                             autopct='%1.1f%%', #Values are kept in fixed decimal places
                             shadow=False, #No shadow setting
                             startangle=90, #Set counterclockwise starting Angle
                             pctdistance = 0.6 #distance multiple from the center of the circle
                             )
# x,y axis:The scale is set uniformly to ensure that the pie is round
plt.axis('equal')
plt.title('Covid-19 cases in 5 countires')
plt.show()
