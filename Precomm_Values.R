twenty = 20

for (x in c(1:10))
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
  {  
    Max_end <- (Max_start + twenty)
    Min_end <- (Min_start - twenty) }

  #what to do when the difference is less than 20
  if (difference < 20)
  {  
    Max_end <- (Max_start - twenty)
    Min_end <- (Min_start + twenty) }
  
  # naming the max and min values in alignment with A and B 
  if (Max_end == (A + 20))
    A2 <- Max_end else A2 <- Min_end 
  if (Max_end == (B + 20))
    B2 = Max_end else B2 = Min_end 
  
  print(Max_end)
  print(Min_end)
  
  
  #if the values are the same or different 
  if ((Max_start == A_start) & (Max_end == A_end)) {
    option <- ("A_always_best") 
    } else if  ((Max_start == B_start) & (Max_end == B_end)) {
      option <- ("B_always_best")
    } else if  ((Max_start == A_start) & (Max_end == B_end)) {
      option <- ("changes") 
    } else if ((Max_start == B_start) & (Max_end == A_end)) {
      option <- ("changes")
    }
      
  data = c(A_start, B_start, A_end, B_end, difference, option)
  print(data)
  print 
}
  #view = matrix(c(data), nrow = 6, ncol = 10, byrow = TRUE)
  #colnames(view) <- c('A_start', 'B_start', 'A_end', 'B_end', 'difference', 'option')
  #rownames(view) <- c(1:10)
  #view.table <- as.table(view)