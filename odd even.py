def odd_even(n):
    if n % 2:
        return "FALSE"
    else:
        return "TRUE"
    
try:
    for i in range(1,1001):
        print(i, ":",  odd_even(i)) 
except ValueError:
    print("Error")        

    
  