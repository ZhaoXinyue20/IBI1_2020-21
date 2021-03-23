import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/zhaoxinyue/Desktop/IBI1/Practical7")
# os.getcwd()=pwd, os.listdir()=ls

covid_data = pd.read_csv("full_data.csv")
# every sevcond row between 0 ~ 10
covid_data.iloc[0:10:2,:]

# method 1
covid_data.loc[covid_data['location'].str.contains('Afghanistan'),"total_cases"]
# method 2, use boolean
my_loc=[]
for i in range (0,7996):
	if covid_data.iloc[i,1]=="Afghanistan":
		my_loc.append(True)
	else:
		my_loc.append(False)

covid_data.loc[my_loc,"total_cases"]

L= []
for i in range (0,7996):
     if covid_data.iloc[i,1]=="World":
             L.append(True)
     else:
             L.append(False)
world_new_cases=covid_data.loc[L,"new_cases"]
world_dates=covid_data.loc[L,"date"]
world_new_deaths=covid_data.loc[L,"new_deaths"]

np.mean(world_new_cases)
np.median(world_new_cases)

score = world_new_cases
plt.boxplot(score,
             vert = True,
             whis = 1.5,
             patch_artist = True,
             meanline = False,
             showbox = True,
             showcaps = True,
             showfliers = True,
             notch = False
             )
plt.xlabel('world_dates')
plt.ylabel('world_new_cases')
plt.show()

plt.plot(world_dates, world_new_cases, 'b+')

Loc=[]
for i in range (0,7996):
	if covid_data.iloc[i,1]=="China":
		Loc.append(True)
	else:
		Loc.append(False)

#my questions
China_new_cases=covid_data.loc[Loc,"new_cases"]
China_total_cases=covid_data.loc[Loc,"total_cases"]
China_dates=covid_data.loc[Loc,"date"]
plt.plot(China_dates, China_new_cases, 'bo')
plt.plot(China_dates, China_total_cases, 'r+')
plt.xticks(China_dates.iloc[0:len(China_dates):4],rotation=-90)
plt.xlabel('dates')
plt.ylabel('population')
plt.legend()
plt.show()
