---
title: "R Notebook"
output: html_notebook
---

# Importing
rottom <- read.csv("test_2018-04-23_19-52-54.txt", sep = "\t", stringsAsFactors = FALSE)

library(stringr)

# Extracting year
rottom$Yr <- str_sub(rottom$In_Theaters_date, -2, -1)

rt <- rottom[rottom$Yr != "ne", ]

rt$Year <- ifelse(as.integer(rt$Yr) <= 18, paste0("20",rt$Yr), paste0("19", rt$Yr))

rt$ReleaseDate <- paste(str_sub(rt$In_Theaters_date, 1, -4), rt$Year, sep = "-")


rt$ReleaseDate <- strptime(rt$ReleaseDate, format = "%d-%b-%Y")




#Creating copies of the main dataset

cast_pop <- rt[, c(1, 15, 2, 3, 21, 22)] # FIRST CHANGE HERE: 15 to Directers, Writters
cast_pop$ReleaseDate <- as.character(cast_pop$ReleaseDate)


#Reshape the dataframe

library(splitstackshape)
library(reshape2)

temp1 <- cSplit(cast_pop, 'Cast', sep=",", type.convert=FALSE)
temp2 <- melt(temp1, variable.name = "Cast", id.vars = c("Movie_name", "Critics_Score", "Audience_Score", "Year", "ReleaseDate")) # CHANGE Cast to D, W, add BO
temp3 <- temp2[!is.na(temp2$value), ]

castmem <- temp3[, -6]
castmem$Year <- as.integer(castmem$Year)
castmem$Audience_Score <- as.integer(castmem$Audience_Score)
castmem$Critics_Score <- as.integer(castmem$Critics_Score)

names(castmem) <- c("Movie", "Critics_Score", "Audience_Score", "Year", "ReleaseDate", "Actor")



#Calculations


library(sqldf)
library(dplyr)

a <- sqldf("select Actor, Year, avg(Audience_Score) from castmem group by Actor, Year")

b <- castmem[castmem$Actor == "JohnAbraham", ]

c <- b %>% group_by(Actor, Year) %>% summarise(Avg = mean(Audience_Score))

d <- castmem %>% arrange(Actor, Year) %>% mutate(Avg = cummean(Audience_Score, na.rm = TRUE)) %>% select(Actor, Year, Avg) %>% group_by(Actor, Year) %>% summarise(AvgValue = last(Avg))
