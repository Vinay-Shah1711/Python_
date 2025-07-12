# Break and continue

# for i in range(12):
#     if(i==10):
#         break
#     print("5 * " , i , "=", 5*i)

# print("LOOP ko drop kro by if condition")


# for i in range(12):
#     if(i==10):
#         print("Skip the iteration")
#         continue
#     print("5 * " , i , "=", 5*i)

# This is like do while loop first execute if condition is true it again execute
i=0
while True:
    print(i)
    i=i+1
    if(i%50==0):
        break

for i in range(1,101,1):
    print(i ,end=" ")
    if(i==10):
        break
    else:
        print("Mississippi")
print("Thank you")