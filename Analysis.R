###### Basic Data Analysis Option ######
library(ggplot2)

#Working directory
path <- "~/Documents/Github/Precommitment/data/"
#Set working diretory 
setwd(path)

#Open the data
Precomm <- read.csv("PreComm_Task_1_09052019.csv")
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