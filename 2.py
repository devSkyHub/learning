n=5
for x in range (0,4):
  n=n-1 
  for y in range (0,4):
   if(y<n-1):	
    print (" ", end = "\t ")
   elif( y>=n-1):
    print(" \t  x")
print("\n")

