# Gotta Think of new question
import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as sq
import pandas as pd

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



plt.scatter(player_height, player_finishing)
# ax.set_xticklabels(n_neighbors)
plt.xlabel("Player Score")
plt.ylabel("Player Height")
plt.title("Player Heights")
plt.show()


