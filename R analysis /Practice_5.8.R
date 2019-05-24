###### Basic Data Analysis Option ######
library(ggplot2)
library(psych)

#Working directory
path <- "~/Documents/Github/Precommitment/data/"
#Set working diretory 
setwd(path)

#Open the data
mydata <- read.csv("~/Documents/Github/Precommitment/data/PreComm_Task_01_01052019.csv")
View(mydata)


#See the amount of times we have each difference, each change and the combination of them 
differences <- table(mydata$difference)
ggplot(mydata, aes(factor(difference))) + geom_bar(fill="royalblue") + 
  labs(title = "Differences Count", x = "difference values", y = "occurrences") + 
  theme_classic()
barplot(differences, col="royalblue", main="Differences", las=1)
changes <- table(mydata$change)
barplot(changes)
ggplot(mydata, aes(factor(change))) + geom_bar(fill="mediumturquoise") + 
  labs(title = "Changes Count", x = "change values", y = "occurrences") + 
  theme_classic()
differences_changes <- table(mydata$difference, mydata$change)
differences_changes
#ggplot(mydata, aes(factor(differences_changes))) + geom_bar(fill="mediumturquoise") + 
  #labs(title = "Changes Count", x = "change values", y = "occurrences") + 
  #theme_classic()
barplot(differences_changes, col=rainbow(16))

#Scatterplot of differnces and changes 
qplot(change, difference, data=mydata)


