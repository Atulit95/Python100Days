# Our goal is to count squirrels based on their Primary fur color from squirrel_data.csv.
# Also store data into new csv file named as squirrel_count.csv.

import pandas

squirrel_data = pandas.read_csv("squirrel_data.csv")
fur_color = squirrel_data["Primary Fur Color"].to_list()

data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [
        fur_color.count("Gray"),
        fur_color.count("Cinnamon"),
        fur_color.count("Black"),
    ],
}

squirrel_count = pandas.DataFrame(data)
squirrel_count.to_csv("Squirrel_count.csv")
