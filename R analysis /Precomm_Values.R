#parameters
addition = 20

for (x in c(1:30))
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
  if (difference >= 20) { 
    One_end = (Max_start + addition)
    Two_end = (Min_start - addition) }
    #what to do when the difference is less than 20
  if (difference < 20) {
    One_end = (Max_start - addition)
    Two_end = (Min_start + addition) 
  }
  

  # naming the max and min values in alignment with A and B 
  if (One_end == (A + addition))
    A_end <- One_end else A_end <- Two_end 
  if (One_end == (B + addition))
    B_end <- Two_end else B_end <- One_end
  
  #max is the higher end value 
  #min is the smaller end value 
  Max_end = max(One_end:Two_end)
  Min_end = min(One_end:Two_end)
  
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
}
