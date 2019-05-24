### parameters ###

#difference options
d1 = 4 
d2 = 12 
d3 = 20 
d4 = 28 
d01 = -4 
d02 = -12 
d03 = -20 
d04 = -28
diff_options = c(d1, d2, d3, d4, d01, d02, d03, d04)

#value changing options 
c1 = 3 
c2 = 9 
c3 = 13 
change_options = c(c1, c2, c3)

print("d, A_start, B_start, First_start, Second_start, c, direction, random, A_end, B_end, Best")

# simulation loop 
for (x in c(1:30))
{
  #Pick the first value
  First_start = sample(42:89,1)
  #Decide on a difference option 
  d = sample(c(diff_options), 1)
  #Pick the second value 
  Second_start = First_start + d
  
  #Determine the random options 
  direction = sample(c(0, 1), 1)
  random = sample(c(0, 1), 1)
  
  #Determine which value (first or second) is A and which value is B
  if (random == 1) {
    A_start = First_start
    B_start = Second_start
  } else if (random == 0){
    A_start = Second_start
    B_start = First_start
  }
  
  #Pick the value you want to change by 
  c = sample(c(change_options), 1)

  #Different ending options depending on the two different directions
  if (direction == 1) {
    A_end = A_start + c
    B_end = B_start - c
  } else if (direction == 0) {
    A_end = A_start - c 
    B_end = B_start + c
  }
  
  #determine larger values
  max_start = max(A_start:B_start)
  min_start = min(A_start:B_start)
  max_end = max(A_end:B_end)
  min_end = min(A_end:B_end)
  
  if (max_start == A_start & max_end == A_end) {
    best = str('A_both')
  } else if (max_start == B_start & max_end == B_end) {
    best = str('B_both')
  } else best = str('changes')
  
  
  #cat('d=', d, '\n')
  #cat('A_start=', A_start, '\n')
  #cat('B_start=', B_start, '\n')
  #cat('First_start=', First_start, '\n')
  #cat('Second_start=', Second_start, '\n')
  #cat('c=', c, '\n')
  #cat('direction=', direction, '\n')
  #cat('random=', random, '\n')
  #cat('A_end=', A_end, '\n')
  #cat('B_end=', B_end, '\n')
  
  data = (c(d, A_start, B_start, First_start, Second_start, c, direction, random, A_end, B_end, best))
  print(data)
}