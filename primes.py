# Python program to print all  
# prime numbers in a given interval.
# Start should be greater than 1.  
start = 1
end = 25
  
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 