# Gotta Think of new question
import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as sq
import pandas as pd
import random
from operator import itemgetter

def get_overall_rating(x, data):
    all_rating = data.execute("""SELECT overall_rating FROM Player_Stats WHERE player_api_id = '%d' """ % (x)).fetchall()
    all_rating = np.array(all_rating,dtype=np.float)[:,0]
    mean_rating = np.nanmean(all_rating)
    return mean_rating
def get_player_height(x, data):
    all_rating = data.execute("""SELECT height FROM Player WHERE player_api_id = '%d' """ % (x)).fetchall()
    all_rating = np.array(all_rating,dtype=np.float)[:,0]
    mean_rating = np.nanmean(all_rating)
    return mean_rating
def get_overall_finishing(x, data):
    all_rating = data.execute("""SELECT finishing FROM Player_Stats WHERE player_api_id = '%d' """ % (x)).fetchall()
    all_rating = np.array(all_rating,dtype=np.float)[:,0]
    mean_rating = np.nanmean(all_rating)
    return mean_rating

# Globals 
data = sq.connect('./database.sqlite/database.sqlite')
player_stats = data.execute("SELECT * FROM Player_Stats")
player_info = data.execute("SELECT * FROM Player")
player_api_id = []
player_height = []
player_fifaScore = []
player_finishing =[]
for row in player_info:
    player_api_id.append(row[1])
for api_id in player_api_id:
    player_fifaScore.append(get_overall_rating(api_id, data))
    player_finishing.append(get_overall_finishing(api_id, data))
    player_height.append(get_player_height(api_id, data))
player_height_ints = []
for thing in player_height:
    player_height_ints.append(int(round(thing)))
print("min: ", min(player_height))
print("max: ", max(player_height))
random_indices = np.random.randint(50,size=len(player_api_id))
player_height_subSample = np.array(player_height)
player_finishing_subSample = np.array(player_finishing)
player_height_subSample = player_height_subSample[random_indices]
player_finishing_subSample = player_finishing_subSample[random_indices]
plt.scatter(player_height_subSample, player_finishing_subSample)
plt.xlabel("Player Height (cm)")
plt.ylabel("Player Finishing (0-100)")
plt.title("Player Finishing vs. Height")
plt.show()
table_data = zip(player_height_subSample, player_finishing_subSample)
table_data = sorted(table_data, key=itemgetter(0))




