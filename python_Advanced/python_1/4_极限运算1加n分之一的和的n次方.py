print("enter a big number !\n")
n = int(input("Enter n:"))        
t = 1.0
e = 1.0                    
for i in range(1, n+1):         
        t = t*i
        e = e+1.0/t       

print(" %f" %e)
