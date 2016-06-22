# analyzing movie reviews
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress
from scipy.stats import pearsonr

# import data
movies = pd.read_csv("fandango_score_comparison.csv")

# print out first five lines of the dataframe
print(movies.head())

# create a histogram of the Fandango ratings
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.hist(movies["Fandango_Stars"])
ax1.set(xlabel="Fandango_Stars", ylabel="Frequency",
        title="Histogram Fandango_Stars", xlim=(0, 5))

# plot a histogram of the normalized Metacritic scores
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.hist(movies["Metacritic_norm_round"])
ax2.set(xlabel="Metacritic_norm_round", ylabel="Frequency", 
        title="Histogram Metacritic_norm_round", xlim=(0, 5))

# calculate the mean, median and std for both rating columns and compare
# the results
fan_star_mean = movies["Fandango_Stars"].mean()
fan_star_med = movies["Fandango_Stars"].median()
fan_star_std = np.std(movies["Fandango_Stars"])

met_norm_round_mean = movies["Metacritic_norm_round"].mean()
met_norm_round_med = movies["Metacritic_norm_round"].median()
met_norm_round_std = np.std(movies["Metacritic_norm_round"])

print("\t\t\t Mean\t\t\t Median\t std")
print("Fandango_Stars \t\t {0} \t {1} \t {2}".format(fan_star_mean,
                                                     fan_star_med, fan_star_std))
print("Metacritic_norm_round \t {0} \t {1} \t {2}".format(met_norm_round_mean,
                                                          met_norm_round_med, 
                                                          met_norm_round_std))
# scatter plot to compare the two rating columns
fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)
ax3.scatter(movies["Fandango_Stars"], movies["Metacritic_norm_round"])
ax3.set(xlabel="Fandango_Stars", ylabel="Metacritic_norm_round", xlim=(0, 5),
        ylim=(0, 5))

# find movies that have very different scores on the two critics sites
movies["fm_diff"] = np.abs(movies["Fandango_Stars"] -
                           movies["Metacritic_norm_round"])
print(movies.sort_values("fm_diff", ascending=False).head())

# find the r-value describing the correlation between the Fandango stars
# and the normalized Metacritic scores
r_value, p_value = pearsonr(movies["Fandango_Stars"],
                            movies["Metacritic_norm_round"])
print("r-value: {0}, p-value: {1}".format(r_value, p_value))

# create a linear regression line using the normalized Metacritic scores as
# x-values and the Fandango stars as y-values
slope, intercept, rvalue, pvalue, stderr = linregress(
    movies["Metacritic_norm_round"], movies["Fandango_Stars"])

# plot the regression line
fig4 = plt.figure()
ax4 = fig4.add_subplot(1, 1, 1)

x = np.arange(0, 6)
y = slope * x + intercept
ax4.scatter(movies["Metacritic_norm_round"], movies["Fandango_Stars"])
ax4.plot(x, y)
ax4.set(xlabel="Metacritic_norm_round", ylabel="Fandango_Stars", xlim=(0, 5),
        ylim=(0, 5))

# predict the Fandango score a movie with a Metacritic rating of 3.0 would
# get using the regression line
fandango_predicted1 = 3.0 * slope + intercept
print("Fandango_Stars predicted for Metacritic_norm_round of 3.0: {0}".format(
    fandango_predicted1))

fandango_predicted2 = 4.0 * slope + intercept
print("Fandango_Stars predicted for Metacritic_norm_round of 4.0: {0}".format(
    fandango_predicted2))

plt.show()
