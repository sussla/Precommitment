# free params
a1 = 20 # lower bound of the lower range
a2 = 28 # lower bound of the higher range
w = 80  # width of each range
l = 0.5 # lambda = the amount of times a random choice will be granted 

# derived params
b1 = a1 + w # upper bound of lower range
b2 = a2 + w # upper bound of higher range
pOverlap = max(0, (b1-a2)/w) # proportion overlap

#picking first values 
First_x1 = sample(a1:b1,1)
First_x2 = sample(a2:b2,1)
First_choice = max(First_x1:First_x2)

#picking second values v
Second_x1 = sample(a1:b1,1)
Second_x2 = sample(a2:b2,1)
Second_choice = max(Second_x1:Second_x2)

#difference between first an second values 
Difference_x1 = First_x1 - Second_x1
Difference_x2 = First_x2 - Second_x2

#best and worst options
Best_Choice = max(First_choice:Second_choice)
if(Best_Choice == First_choice) print("Best Option in Initial Choice") else print("Best Option in Final Choice")
Worst_option = min(Second_x1:Second_x2)

#are the greater option in the same domain of either 1 or 2
if(First_x1>=First_x2 & Second_x1>=Second_x2) print("x1 always better option")
if(First_x1<=First_x2 & Second_x1<=Second_x2) print("x2 always better option")
if(First_x1>=First_x2 & Second_x1<=Second_x2 | First_x1<=First_x2 & Second_x1>=Second_x2) print("better option changes")

# 1st scenario: x2 > b1
# x2 lands above the overlap range
# x2 is greater, and ranges from b1 to b2
p1 = 1 - pOverlap # probability of this occurring
ev1 = (b1+b2)/2 # expected value if this occurs

# 2nd scenario: x2 < b1 and x1 < a2
# x2 lands in the overlap range and x1 lands below the overlap range
# x2 is greater, and ranges from a2 to b1
p2 = pOverlap * (1 - pOverlap) # probability of this occurring
ev2 = (a2+b1)/2 # expected value if this occurs

# 3rd scenario: 
# x1 and x2 both land in the overlap range
# both range from a2 to b1
# the expected value of the max will be 2/3 of the range. 
p3 = pOverlap^2 # probability of this occurring
ev3 = a2 + (2/3)*(b1-a2)

# tally it up
total_p = p1 + p2 + p3 # confirm this equals 1
total_ev = p1*ev1 + p2*ev2 + p3*ev3

#expected value
value_ev = ((l/3)*(p1*ev1 + p2*ev2 + p3*ev3)) + (1-l)*(p1*ev1 + p2*ev2 + p3*ev3)

# print results
#cat(a1, '< x1 <', b1 ,'\n')
#cat(a2, '< x2 <', b2, '\n')
#cat('Best option presented =',Best_Choice, '\n')
#cat('Worst option presented =',Worst_option, '\n')
#cat('Expected value simulation =', value_ev, '\n')
#cat('Expected max value Joe =', total_ev, '\n')
#cat('Total p =', total_p, '\n')
cat('First x1 =', First_x1, '\n')
cat('Second x1 =', Second_x1, '\n')
cat('First x2 =', First_x2, '\n')
cat('Second x2 =', Second_x2, '\n')