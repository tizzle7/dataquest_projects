# pixar movies analysis
import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns

# import datafile
pixar_movies = pd.read_csv("pixar_movies.csv")

# determine dimensions of the dataset
row_number = pixar_movies.shape[0]
column_number = pixar_movies.shape[1]

# print out the entire table, the datatypes of all the columns and the results
# of the describe method to get a first insight into the dataset
print(80 * "-")
print(pixar_movies.head(row_number))
print(80 * "-")
print(pixar_movies.dtypes)
print(80 * "-")
print(pixar_movies.describe())
print(80 * "-")

# get rid of the %-sign in the "Domestic %" and "International %" columns and convert
# their datatypes to float, use the series attribute str to apply the rstrip function to
# each row and strip the %-sign
pixar_movies["Domestic %"] = pixar_movies["Domestic %"].str.rstrip("%").astype(float)
pixar_movies["International %"] = pixar_movies["International %"].str.rstrip("%").astype(float)

# convert the "IMDB Score" column from a 10 point scale to a 100 point scale
pixar_movies["IMDB Score"] = pixar_movies["IMDB Score"] * 10

# get rid of the rows containing NaN values
filtered_pixar = pixar_movies.dropna()

# set the "Movie" column containing the respective movie names as the index 
# for the dataframes
pixar_movies.set_index("Movie", inplace=True)
filtered_pixar.set_index("Movie", inplace=True)

# dataframe containing only the different critics scores from all three providers
critics_reviews = filtered_pixar[["RT Score", "IMDB Score", "Metacritic Score"]]
print(critics_reviews)

# plot all the reviews in a single line plot
critics_reviews.plot()
plt.show()

# plot the distribution of the reviews in a box plot
critics_reviews.boxplot(figsize=(10, 6))
plt.show()

# create new dataframe containing only the percentage numbers of the total revenue made
# in the US and internationally
revenue_proportions = filtered_pixar[["Domestic %", "International %"]]

# plot the numbers in a stacked bar plot
revenue_proportions.plot(kind="bar", stacked=True, figsize=(10, 6))
plt.show()
