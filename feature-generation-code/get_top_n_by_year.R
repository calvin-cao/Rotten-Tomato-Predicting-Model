
#install.packages("data.table")
library(data.table)

#Change the value of n here
n <- 5

### This code is for the directors
dl <- read.csv("Director_csv.csv")
dl <- na.omit(dl)
dl2 <- data.table(dl)
new_dl <- dl2[, rank := frank(-AvgCS, ties.method = "dense"), by = Year]
d_top5 <- subset(new_dl, rank <= n)[, c(2, 1, 4)]
#write.csv(d_top5, "Top5DirectorsByYear.csv", row.names = FALSE)

### This code is for the directors
dl <- read.csv("Writer_csv.csv")

dl2 <- data.table(dl)
new_dl <- dl2[, rank := frank(-AvgCS, ties.method = "dense"), by = Year]
w_top5 <- subset(new_dl, rank <= n)[, c(2, 1, 4)]
#write.csv(dl_top5, "Top5WritersByYear.csv", row.names = FALSE)

### This code is for the directors
dl <- read.csv("Actor_csv.csv")

dl2 <- data.table(dl)
new_dl <- dl2[, rank := frank(-AvgCS, ties.method = "dense"), by = Year]
a_top5 <- subset(new_dl, rank <= n)[, c(2, 1, 4)]
#write.csv(dl_top5, "Top5ActorsByYear.csv", row.names = FALSE)
