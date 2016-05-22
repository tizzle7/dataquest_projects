# star wars survey analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import data
star_wars = pd.read_csv("star_wars_survey.csv", encoding="ISO-8859-1")

# remove respondents without ID
star_wars = star_wars[pd.notnull(star_wars["RespondentID"])]

# rename yes/no answers if they have seen any of the Star Wars movies
# to True/False 
yes_no ={
    "Yes": True,
    "No": False
}

any_6 = "Have you seen any of the 6 films in the Star Wars franchise?"
consider_fan = "Do you consider yourself to be a fan of the Star Wars film franchise?"
star_wars[any_6] = star_wars[any_6].map(yes_no)
star_wars[consider_fan] = star_wars[consider_fan].replace(yes_no)

# change column entries from movie name that has been seen to True or False
seen_or_not = {
    np.nan: False,
    "Star Wars: Episode I  The Phantom Menace" : True,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True
}

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].replace(seen_or_not)

# rename column names that contain answers to which movie has been seen
rename_seen_or_not_columns = {
    "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
    "Unnamed: 4": "seen_2",
    "Unnamed: 5": "seen_3",
    "Unnamed: 6": "seen_4",
    "Unnamed: 7": "seen_5",
    "Unnamed: 8": "seen_6"
    }
star_wars = star_wars.rename(columns=rename_seen_or_not_columns)

# convert ranking columns to floats
star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)

# rename ranking column names
rename_ranking_columns = {
    "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
    "Unnamed: 10": "ranking_2",
    "Unnamed: 11": "ranking_3",
    "Unnamed: 12": "ranking_4",
    "Unnamed: 13": "ranking_5",
    "Unnamed: 14": "ranking_6"
    }
star_wars = star_wars.rename(columns=rename_ranking_columns)

# calculate the mean ranking for each film
mean_rankings = star_wars[star_wars.columns[9:15]].mean()

# plot mean rankings in a bar plot
fig1 = plt.figure()
ax = fig1.add_subplot(1, 1, 1)

ax.set(xlabel="Episode Number", ylabel="Mean Ranking", xticks=(np.arange(6) + 0.5), xticklabels=mean_rankings.index.tolist())
ax.bar(range(6), mean_rankings)
plt.show()

# calculate how many people have seen each movie
sum_seens = star_wars[star_wars.columns[3:9]].sum()

# plot the viewer numbers for each episode in a bar chart
fig2 = plt.figure()
ax = fig2.add_subplot(1, 1, 1)

ax.set(xlabel="Episode Number", ylabel="#People Who Have Seen The Movie", xticks=(np.arange(6) + 0.5), xticklabels=sum_seens.index.tolist())
ax.bar(range(6), sum_seens)
plt.show()

# split dataframe into participants that consider themselves star wars fans
# or not
sw_fan_column = "Do you consider yourself to be a fan of the Star Wars film franchise?"
sw_fans = star_wars[star_wars[sw_fan_column] == True]
not_sw_fans = star_wars[star_wars[sw_fan_column] == False]

# number of viewers of each episode for star wars fans and not star wars fans
sum_seens_sw_fans = sw_fans[sw_fans.columns[3:9]].sum()
sum_seens_not_sw_fans = not_sw_fans[not_sw_fans.columns[3:9]].sum()

# mean rankings for each episode for star wars fans and not star wars fans
mean_rankings_sw_fans = sw_fans[sw_fans.columns[9:15]].mean()
mean_rankings_not_sw_fans = not_sw_fans[not_sw_fans.columns[9:15]].mean()

# plot number of viewers and mean rankings for both participant groups
# to compare the results
fig3 = plt.figure()
ax1 = fig3.add_subplot(2, 2, 1)
ax2 = fig3.add_subplot(2, 2, 2)
ax3 = fig3.add_subplot(2, 2, 3)
ax4 = fig3.add_subplot(2, 2, 4)

ax1.set(ylabel="# People")
ax3.set(ylabel="Mean Ranking")
ax1.bar(range(6), sum_seens_sw_fans)
ax2.bar(range(6), sum_seens_not_sw_fans)
ax3.bar(range(6), mean_rankings_sw_fans)
ax4.bar(range(6), mean_rankings_not_sw_fans)
plt.show()



