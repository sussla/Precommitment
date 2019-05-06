###### Basic Data Analysis Option ######
library(ggplot2)
install.packages("psych")
library(psych)

#Working directory
path <- "~/Documents/Github/Precommitment/data/"
#Set working diretory 
setwd(path)

#Open the data
Precomm_1 <- read.csv("~/Documents/Github/Precommitment/data/PreComm_Task_01_01052019.csv")
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
ggplot(Precomm_1, aes(Best_changes, difference)) + geom_bar(stat="identity", color="purple") + 
  theme(axis.text.x= element_text(angle= 70, vjust = 0.5, color="black")) + ggtitle("difference vs change") + 
  theme_bw()

Precommitment = 0
### setting up some graphs 
# proportion of times that decide to precommit 
if (Precomm_1['Choice_Play'] == True) {
  Precommitment = 1
} else if (Precomm_1['Choice_Play'] == False) {
  Precommitment = 2
}
if (Precomm_1['Choice_Pick'] == True) {
  Precommitment = 2
} else if (Precomm_1['Choice_Pick'] == False) {
  Precommitment = 1
}
print(Precommitment)

plot(Precommitment ~ Change, data = Precomm_1)