####-----------------------------#####
        #usefull packages#
#####-----------------------------#####
library("tidyr"); library("dplyr") # powerful tools for data manipulation 
library("ggplot2") # for making figures
library("ggpubr") # my recent favorite for t.test and t.test plotting

####-----------------------------#####
        #load all data files#
#####-----------------------------#####
# I duplicated the file you sent to me, assigned it a new file name, and changed the participant name in the file
# so that I can demonstrate how to deal with data from multiple subjects

## get filenames of all files in the data directory
dataDir = "Desktop/Precomm_data/Precommit/data"
allFileNames = list.files(path = dataDir)
nFile = length(allFileNames)
## it is good to ensure you don't miss or duplicate any file
if(any(duplicated(allFileNames))){
  print("duplicated files detected!")
}else{
  sprintf("load %d files!", nFile) # check whether nFile matches the num of participants
}
## load all files, each file as an element in the list
allData = list()
for(i in 1 : nFile){
  thisFileName = allFileNames[i]
  tempt = read.csv(sprintf("%s/%s", dataDir, thisFileName)) # tempt is a cache variable
  allData[[i]] = tempt # list is different from matrix and vector,and we use [[i]] instead of [i] as the index
}
## if you want to quickly check the data object, use the command: str
## you can see it is a "list of 1", and the only element in the list is a data.frame
## within the data.frame, there are "96 obs. of 37 variables",
## and you can see the data type of each variable below, like int, factor, logi
str(allData)
## after the check, I realize there seems to be an empty space in your data file
## and in this case, R can't recognize True/False as logical variables. 
## You can delete that empty space to solve the problem, or you can use the following code to load data
## load all files, the deBug version
allData = list()
TFCols = c("A_alwaysBest", "B_alwaysBest", "Best_changes", "Choice_Wait",
           "Choice_Commit", "Choice_Miss",  "Play_win_A",
           "Play_win_B", "Play_lost", "Play_lost_chosenA", "Play_lost_chosenB", "Precomm_B",
           "Precomm_A","Precomm_miss")
TFNACols = c("Press_hit", "Press_miss")
for(i in 1 : nFile){
  thisFileName = allFileNames[i]
  tempt = read.csv(sprintf("%s/%s", dataDir, thisFileName)) 
  # change True and False to 0 and 1, change 0 to NA
  # this part is tricky since I use the command lapply.
  # Temporarily you can just use it, and you can ask google, Claudio or me to know more about lapply!
  tempt[,TFCols] = lapply(1 : length(TFCols), function(i) as.numeric(tempt[,TFCols[i]]) - 1)
  tempt[,TFNACols] = lapply(1 : length(TFNACols), function(i) {
    junk = as.numeric(tempt[,TFNACols[i]]) - 2
    junk[junk == -1] = NA
  })

  allData[[i]] = tempt 
}



#####-----------------------------#####
      #single-subject analyses#
#####-----------------------------#####
# when you get more participants, you usually do group analyses
# however, it is good to start from single-subject analyse since most techniques are the same

## extract one subject data 
sIdx = 1
thisData = allData[[sIdx]]

## generate some variables useful for analyses, yet not recorded
thisData = within(thisData, {difference = abs(OptionB - OptionA); cumEarnings = cumsum(Earnings)})
## alternatively, you can use the following two lines, easier to understand yet less concise,
## especially when you have a lot variables to generate
thisData$difference = abs(thisData$OptionB - thisData$OptionA)
thisData$cumEarnings = cumsum(thisData$Earnings)

## before statistic tests, we usually just want to get a sense of the data 
## we use two commands, group_by and summarise to calcualte pCommit for 3 groups with different values on difference.
thisDataClean = thisData[thisData$Choice_Miss == F,] # we don't use the missed trials
summarise(group_by(thisDataClean, difference) , pCommit = mean(Choice_Commit)) 
## here I introduce you the pipe symbol, %>%, which sends the output of this command as the input of the next command,
## therefore making consective commands into a chain. 
## here is a more concise version using %>%
thisData %>% filter(Choice_Miss == F) %>% group_by(difference) %>% summarise(pCommit = mean(Choice_Commit))

## we conduct  a logistic regression here to test whether difference has a significant effect on the precommit choice
fit = glm(Choice_Commit ~ difference, data = thisData[thisData$Choice_Miss == F,],
          family = "binomial") 
## print out the regression results
## we mainly look at the part Coefficients, where we can get betas and p-values
summary(fit)


#####-----------------------------#####
           #group analyses#
#####-----------------------------#####
# there are a lot ways to conduct group analyses, and here we show the probably most straight-forward one
# we combine all subject data together, and analyse it as what we did in the single-subject analyses

## combine all subject data in the list into one data.frame
allDataCombined = do.call("rbind", allData)

## repeat analyses in the single-subject analyses
allDataCombined= within(allDataCombined, {difference = abs(OptionB - OptionA); cumEarnings = cumsum(Earnings)})
allDataCombined %>% filter(Choice_Miss == F) %>% group_by(difference) %>% summarise( pCommit = mean(Choice_Commit))
## in the regression results, we can see the beta values remain the same, since the two data file here are actually the same
## However, the Z scores and p-values change and the results are more significant, since we have more observations
fit = glm(Choice_Commit ~ difference, data = allDataCombined[allDataCombined$Choice_Miss == F, ],
          family = "binomial") 
summary(fit)
  

## in the group analyses, we can conduct a mixed-effect logistic regression
library(lme4)
## generate the clean data
allDataCombinedClean = allDataCombined[allDataCombined$Choice_Miss == F, ]

## the mixed effect model with random intercepts
## it generates a singular fit since we only have two duplicated datasets
## anyway I just want to demonstrate how to do it
fitMixed = lmer(Choice_Commit ~ difference + (1 | participant), data = allDataCombinedClean)
## we look at the part fixed effects.
summary(fitMixed)

## the mixed effect model with random slopes and intercepts
fitMixed = lmer(Choice_Commit ~ difference + (1 + difference | participant), data = allDataCombinedClean)
## we look at the part fixed effects.
summary(fitMixed)

