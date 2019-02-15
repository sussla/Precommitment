
# expected value of max(x1, x2), where:
# x1 is drawn uniformly from a lower range, unif(a1, b1)
# x2 is drawn uniformly from a higher range, unif(a2, b2)
# x1 and x2 are independent
# the ranges are the same size: b1 - a1 == b2 - a2
# the range for x2 is higher: a2 > a1
# the ranges overlap: a2 <= b1

# free params
a1 = 10 # lower bound of the lower range
a2 = 20 # lower bound of the higher range
w = 40  # width of each range

lambda = 0.3 #proportion of random choice being made for you 

# derived params
b1 = a1 + w # upper bound of lower range
b2 = a2 + w # upper bound of higher range
pOverlap = max(0, (b1-a2)/w) # proportion overlap

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

#picking value 
x_1 = sample(a1:b1,1)
x_1
x_2 = sample(a2:b2,1)
x_2

#when adding in the random component towards the later waiting concept (?)
with_random = (lambda * total_ev) + ((1-lambda)*(p1*ev1) + (1-lambda)*(p2*ev2) + (1-lambda)*(p3*ev3))
with_random

# print results
cat(a1, '< x1 <', b1 ,'\n')
cat(a2, '< x2 <', b2, '\n')
cat('Expected max value =', total_ev, '\n')
cat('Total p =', total_p, '\n')

# verify through sampling
n = 1000000 # number of random samples
x1 = runif(n, min=a1, max=b1)
x2 = runif(n, min=a2, max=b2)
total_ev_samp = mean(pmax(x1, x2))
cat('Average max value from sampling =', total_ev_samp, '\n')



