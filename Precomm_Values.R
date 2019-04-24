for (x in c(1:10))
{ 
  {
  difference = 0 
  option = 0
  #Pick the first values 
  A_start = sample(20:80,1)
  B_start = sample(20:80,1)
  
  #max is the higher start value 
  #min is the smaller start value 
  Max_start = max(A_start:B_start)
  Min_start = min(A_start:B_start)
  
  #Difference between the two values and the absolute value of that 
  difference_start = A_start - B_start 
  difference = abs(difference_start)
  
  #define the actual values of A and B
  if (Max_start == A_start) 
    A = Max_start else A = Min_start 
  if (Max_start == B_start)
    B = Max_start else B = Min_start
  
  #what to do when the differnce is greater than 20
  if (difference >= 20)
    Max_end = Max_start + 30
    Min_end = Min_start - 30
    if (A == Max_start & B == Min_start)
      A_end = Max_end
      B_end = Min_end
      if (B == Max_start & A == Min_start)
      A_end = Min_end
      B_end = Max_end

  #what to do when the difference is less than 20
  if (difference <= 20)
    Max_end = Max_start - 30
    Min_end = Min_start + 30
    if (A == Max_start & B == Min_start)
      A_end = Max_end
      B_end = Min_end
    if (B == Max_start & A == Min_start)
      A_end = Min_end
      B_end = Max_end
    
  #if the values are the same or different 
  if (Max_start == A_start & Max_end == A_end) 
    option <- ("A_always_best")
  if (Max_start == B_start & Max_end == B_end) 
    option <- ("B_always_best")
  if (Max_start == A_start & Max_end == B_end | Max_start == B_start & Max_end == A_end)
    option <- ("changes") 
  
data = c(A_start, B_start, A_end, B_end, difference, option)
print(data)
}
}
write.table(data)
colnames(view) <- c('A_start', 'B_start', 'A_end', 'B_end', 'difference', 'option')
rownames(view) <- c(1:10)
view.table <- as.table(view)