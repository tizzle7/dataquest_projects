# customizing data visualizations
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import data
recent_grads = pd.read_csv("recent-grads.csv")

# print out the first five rows of the dataset and generate summary statistics for each
# column
print(recent_grads.head())
print(recent_grads.describe())

# get rid of rows containing empty values, display how many rows were removed
row_number = recent_grads.shape[0]
recent_grads = recent_grads.dropna()
print("Number of rows containing NaN values dropped: {}".format(
        row_number - recent_grads.shape[0]))

# create a customized scatter matrix plot, can also be obtained using the scatter_matrix
# function from pandas.tools.plotting
fig1 = plt.figure(figsize=(8, 8))
ax_topleft = fig1.add_subplot(2, 2, 1)
ax_topright = fig1.add_subplot(2, 2, 2)
ax_bottomleft = fig1.add_subplot(2, 2, 3)
ax_bottomright = fig1.add_subplot(2, 2, 4)

# histogram of the "ShareWomen" column in the top-left plot
ax_topleft.hist(recent_grads["ShareWomen"])
ax_topleft.get_xaxis().set_visible(False) # hide x-axis ticks
ax_topleft.set_ylabel("ShareWomen") # assign y-axis label
ax_topleft.set_ylim(0, 30) # set y-axis data limits
ax_topleft.set_yticklabels([0, 5, 10, 15, 20, 25, 30]) # set y-axis tick labels

# scatter plot using the "Unemployment_rate" as x-axis and "ShareWomen" as y-axis in the
# top-right plot
ax_topright.scatter(recent_grads["Unemployment_rate"], recent_grads["ShareWomen"])
ax_topright.get_xaxis().set_visible(False)
ax_topright.get_yaxis().set_visible(False) # hide y-axis ticks
ax_topright.set_xlim(0.0, 0.20) # set x-axis data limits

# scatter plot using the "ShareWomen" as x-axis and "Unemployment_rate" as y-axis in the
# bottom-left plot
ax_bottomleft.scatter(recent_grads["ShareWomen"], recent_grads["Unemployment_rate"])
ax_bottomleft.set_xlabel("ShareWomen") # assign x-axis label
ax_bottomleft.set_ylabel("Unemployment_rate")
ax_bottomleft.set_xlim(0.0, 1.0)
ax_bottomleft.set_xticklabels([0.0, 0.2, 0.4, 0.6, 0.8], rotation=90) # set and rotate x-axis tick labels
ax_bottomleft.set_ylim(0.0, 0.20) # set y-axis data limits
ax_bottomleft.set_yticklabels([0.00, 0.05, 0.10, 0.15])

# histogram of the "Unemployment_rate" column in the bottom-right plot
ax_bottomright.hist(recent_grads["Unemployment_rate"])
ax_bottomright.set_xlabel("Unemployment_rate")
ax_bottomright.get_yaxis().set_visible(False)
ax_bottomright.set_xlim(0.0, 0.20)
ax_bottomright.set_xticklabels([0.00, 0.05, 0.10, 0.15], rotation=90)

# remove vertical and horizontal spacing between subplots
fig1.subplots_adjust(wspace=0, hspace=0)

# create a new ShareMen column in the dataframe
recent_grads["ShareMen"] = recent_grads["Men"] / recent_grads["Total"]

# extract only the art majors from the complete dataframe
arts_grads = recent_grads[recent_grads["Major_category"] == "Arts"]

# create a grouped bar plot to compare the gender ratios in the arts majors
fig2 = plt.figure(figsize=(8, 8))
ax = fig2.add_subplot(1, 1, 1)

locs = np.arange(0, arts_grads.shape[0]) # list used for the placement of the first bar group
offset_locs = locs + 0.35 # placement of the second bar group

bar_1 = ax.bar(locs, arts_grads["ShareMen"].tolist(), width=0.35) # "ShareMen" bars
bar_2 = ax.bar(offset_locs, arts_grads["ShareWomen"].tolist(), width=0.35, color="green") # "ShareWomen" bars

ax.set_xticks(offset_locs) # align the x-axis labels between the two bars
ax.set_xticklabels(arts_grads["Major"].tolist(), rotation=90) # set x-axis tick labels
ax.legend((bar_1, bar_2), ("ShareMen", "ShareWomen"), loc="upper left") # create legend
ax.grid() # turn on background grid

plt.show()
