player_data <- read.csv(file="player_output/federer.csv", header=TRUE, sep=",")
plot_rank <- ggplot(data = player_data, mapping = aes(x = player_age, y = player_rank)) + geom_point(color = "blue") + ggtitle("Federer's ATP Ranking Since Turning Pro")
gamelength_boxplot <- ggplot(data = player_data) + geom_boxplot(mapping = aes(x = "", y = minutes)) + coord_flip() + ggtitle("Boxplot of Length of Federer's Games (Minutes)")
rank_lineplot <- ggplot(data = player_data) + geom_line(mapping = aes(x = player_age, y = player_rank)) + ggtitle("Federer's Ranking (Line Plot)")
numberofaces_boxplot <- ggplot(data = player_data) + geom_boxplot(mapping = aes(x = "", y = player_ace)) + coord_flip() + ggtitle("The number of aces Federer has in a game")
firstservepointswonperyear_histogram <- ggplot(player_data, aes(x = player_1stWon)) + geom_histogram(position = "stack") + ggtitle("1st Points Histogram")

print(gamelength_boxplot)
print(rank_lineplot)
print(numberofaces_boxplot)
print(firstservepointswonperyear_histogram)




