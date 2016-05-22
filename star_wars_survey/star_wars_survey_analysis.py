# star wars survey analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import data
star_wars = pd.read_csv("star_wars_survey.csv", encoding="ISO-8859-1")

# rename column names that contain answers to which episode has been seen
episodes_seen_list = ["Episode I_seen", "Episode II_seen", "Episode III_seen",
                      "Episode IV_seen", "Episode V_seen", "Episode VI_seen"] 
old_column_names = star_wars.columns[3:9].tolist()
new_column_names = episodes_seen_list

rename_seen_movie_columns = dict(zip(old_column_names, new_column_names))
star_wars = star_wars.rename(columns=rename_seen_movie_columns)

# rename ranking column names for each episode
episodes_ranking_list = ["Episode I_ranking", "Episode II_ranking", "Episode III_ranking",
                      "Episode IV_ranking", "Episode V_ranking", "Episode VI_ranking"] 
old_column_names = star_wars.columns[9:15].tolist()
new_column_names = episodes_ranking_list

rename_ranking_columns = dict(zip(old_column_names, new_column_names))
star_wars = star_wars.rename(columns=rename_ranking_columns)

# add character names of favorite ranking from row 0 to column names, 
old_column_names = star_wars.columns[15:29].tolist()
new_column_names = star_wars[star_wars.columns[15:29]].iloc[0].values.tolist()

rename_character_ranking_columns = dict(zip(old_column_names,
                                                      new_column_names))
star_wars = star_wars.rename(columns=rename_character_ranking_columns)

# remove respondents without ID (second header row)
star_wars = star_wars[pd.notnull(star_wars["RespondentID"])]

# rename yes/no/nan answers if the participants have seen any of the Star Wars
# movies or consider themselves star wars fans to True/False 
yes_no_rename = dict(zip(["Yes", "No", np.nan], [True, False, False]))

any_episode_seen = "Have you seen any of the 6 films in the Star Wars franchise?"
consider_fan = "Do you consider yourself to be a fan of the Star Wars film franchise?"
star_wars[any_episode_seen] = star_wars[any_episode_seen].replace(yes_no_rename)
star_wars[consider_fan] = star_wars[consider_fan].replace(yes_no_rename)

# change column entries from movie name that has been seen to True or False
old_row_values = pd.unique(star_wars[
    star_wars.columns[3:9]].values.ravel()).tolist() # find unique values in survey columns
new_row_values = [True for i in range(6)]
new_row_values.append(False)

seen_or_not_rename = dict(zip(old_row_values, new_row_values))

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].replace(seen_or_not_rename)

# convert values in ranking columns to floats
star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)

# calculate the mean ranking for each star wars film
mean_rankings = star_wars[star_wars.columns[9:15]].mean()

# plot mean rankings in a bar plot for each episode
fig1 = plt.figure()
ax = fig1.add_subplot(1, 1, 1)

ax.set(title="Rankings for each Episode",
       ylabel="Mean Ranking",
       xticks=(np.arange(6) + 0.5), xticklabels=["Episode I", "Episode II",
                                                 "Episode III", "Episode IV",
                                                 "Episode V", "Episode VI"])
ax.bar(range(6), mean_rankings)
plt.show()

# calculate how many people have seen each movie
sum_seens = star_wars[star_wars.columns[3:9]].sum()

# plot the viewer numbers for each episode in a bar chart
fig2 = plt.figure()
ax = fig2.add_subplot(1, 1, 1)

ax.set(title="Viewer Number for each Episode",
       ylabel="Viewer Number",
       xticks=(np.arange(6) + 0.5), xticklabels=["Episode I", "Episode II",
                                                 "Episode III", "Episode IV",
                                                 "Episode V", "Episode VI"])
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

ax1.set(ylabel="Viewer Number",
        xticks=(np.arange(6) + 0.5), xticklabels=["E I", "E II",
                                                  "E III", "E IV",
                                                  "E V", "E VI"])
ax2.set(xticks=(np.arange(6) + 0.5), xticklabels=["E I", "E II",
                                                  "E III", "E IV",
                                                  "E V", "E VI"])
ax3.set(ylabel="Mean Ranking",
        xticks=(np.arange(6) + 0.5), xticklabels=["E I", "E II",
                                                  "E III", "E IV",
                                                  "E V", "E VI"])
ax4.set(xticks=(np.arange(6) + 0.5), xticklabels=["E I", "E II",
                                                  "E III", "E IV",
                                                  "E V", "E VI"])
ax1.bar(range(6), sum_seens_sw_fans)
ax2.bar(range(6), sum_seens_not_sw_fans)
ax3.bar(range(6), mean_rankings_sw_fans)
ax4.bar(range(6), mean_rankings_not_sw_fans)
plt.show()
