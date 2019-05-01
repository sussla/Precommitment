###### Basic Data Analysis Option ######
library(ggplot2)

#Working directory
path <- "~/Documents/Github/Precommitment/data/"
#Set working diretory 
setwd(path)

#Open the data
Precomm_1 <- read.csv("~/Documents/Github/Precommitment/data/")
View(Precomm_1)

##### Checking on Components of the data #####

#check dimensions (number of rows & columns) in data set 
dim(Precomm_1)

#check the variables and their types
str(Precomm_1)

#check to see if the data has any missing values 
table(is.na(Precomm_1))
#look closer into the missing data 
colSums(is.na(Precomm_1))

#To get fully summary information 
summary(Precomm_1)

#### Plotting Components of the data ####

#scatter plot graph 
ggplot(Precomm_1, aes(x= difference, y= change)) + geom_point(size = 2.5, color='navy') +
  xlab("difference") + ylab("change") + ggtitle('difference vs change')

#bar graph
ggplot(Precomm_1, aes(difference, change)) + geom_bar(stat="identity", color="purple") + 
  theme(axis.text.x= element_text(angle= 70, vjust = 0.5, color="black")) + ggtitle("difference vs change") + 
  theme_bw()