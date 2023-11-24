def factorial(n): 
    bing = 1
    for i in range(2, n+1): 
        bing *= i 
    return bing
   
number = 4; 
print("Factorial skaitlim", number, "ir", 
factorial(number)) 