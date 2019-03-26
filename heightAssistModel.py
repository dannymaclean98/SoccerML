# Gotta Think of new question
import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as sq
import pandas as pd

data = sq.connect('./database.sqlite/database.sqlite')
player_stats = data.execute("SELECT * FROM Player_Stats")
player_info = data.execute("SELECT * FROM Player")
player_height = []
player_fifaScore = []
for row in player_info:
    player_height.append(row[6])
for row in player_stats:
    player_fifaScore.append(row[4])


plt.scatter(player_fifaScore, player_height)
# ax.set_xticklabels(n_neighbors)
plt.xlabel("Player Score")
plt.ylabel("Player Height")
plt.title("Player Heights")
plt.show()


