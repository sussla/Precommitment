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

# simulation loop 
for (x in c(1:2))
{
  #Pick the first value
  A_start = sample(14:86,1)
  print (A_start)
  #Decide on a difference option 
  d = sample(c(diff_options), 1)
  print(d)
  #Pick the second value 
  B_start = A_start + d
  print(B_start)
  #Pick the value you want to change by 
  c = sample(c(change_options), 1)
  print(c)
  
  direction = sample(c(1, -1), 1)
  print(direction)
  
  if (direction == 1) {
    A_end = A_start + c
    B_end = B_start - c
  } else if (direction == -1){
    A_end = A_start - c 
    B_end = B_start + c
  }
  
  print(A_end)
  print(B_end)
}