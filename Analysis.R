###### Basic Data Analysis Option ######
library(ggplot2)
library(dplyr)

#Working directory
path <- "~/Documents/Github/Precommitment/data/"
#Set working diretory 
setwd(path)

#Open the data
Precomm <- read.csv("Test_values.csv")
View(Precomm)

##### Checking on Components of the data #####

#check dimensions (number of rows & columns) in data set 
dim(Precomm)

#check the variables and their types
str(Precomm)

#check to see if the data has any missing values 
table(is.na(Precomm))
#look closer into the missing data 
colSums(is.na(Precomm))

#To get fully summary information 
summary(Precomm)

#### Plotting Components of the data ####

## Amount of times each of the differences appears in the data ##
difference_counts <-table(Precomm$difference)
View(difference_counts)
ggplot(Precomm, aes(x=factor(difference)), ylim=0) + geom_bar(fill="plum3") + theme_classic() + 
  labs(x="difference values", y="freq", title="Frequency of Difference Values")

## Amount of times each of the changes appears in the data ##
change_counts <-table(Precomm$change)
View(change_counts)
ggplot(Precomm, aes(x=factor(change)), ylim=0) + geom_bar(fill="darkturquoise") + theme_classic() + 
  labs(x="change values", y="freq", title="Frequency of Change Values")

## Table on Changes and Differences ## 
differences <- Precomm$difference
changes <- Precomm$change
changeXdifference <-table(differences, changes)
View(changeXdifference)
ChangesXDifferences <- matrix(c(differences, changes), nrow=40)
View(ChangesXDifferences)


## What is best ##
A_best <- table(Precomm$A_alwaysBest)
B_best <- table(Precomm$B_alwaysBest)
Best_changes <- table(Precomm$Best_changes)
Best <- c(A_best, B_best, Best_changes)
nrow(Precomm[Precomm$A_alwaysBest=TRUE])

Best_A <- as.numeric(Precomm$A_alwaysBest)>1
Best_A
Precomm$A_alwaysBest>1
A_best <- table(Precomm$A_alwaysBest>1)

table(Precomm$A_alwaysBest == "True")

ggplot(Precomm, aes(x=Best_A), ylim=0) + geom_bar(fill="plum3") + theme_classic() + 
  labs(x="difference values", y="freq", title="Frequency of Difference Values")
