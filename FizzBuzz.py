##FIZZBUZZ PROGRAM

#First Approach
i=1
while(i<=100):
    if ((i % 5 == 0) and (i % 3 == 0)):
        print('fizzbuzz')
    elif(i%3==0):
        print('fizz')
    elif(i%5==0):
        print('buzz')
    else:
        print(i)
    i+=1

# Second Approach

for i in range(1, 101):
    if ((i % 5 == 0) and (i % 3 == 0)):
        print('fizzbuzz')
    elif(i%3==0):
        print('fizz')
    elif(i%5==0):
        print('buzz')
    else:
        print(i)

# Third  Approach

#Function
def mod(x,y):
    if(x % y == 0):
        return (1)
    else:
        return (0)


for i in range(1, 101):
    if ((mod(i,5) ==1 )  and (mod(i,3) ==1)): #Calling Function & Reusability
        print('fizzbuzz')
    elif(mod(i,3) ==1):
        print('fizz')
    elif(mod(i,5) ==1):
        print('buzz')
    else:
        print(i)



# Fourth  Approach

#Mod Function
def mod(x,y):
    if(x % y == 0):
        return (1)
    else:
        return (0)

#Equal Function
def equal(z):
    if (z ==1):
        return True
    else:
        return False

for i in range(1, 101):
    if (equal(mod(i,5))  and equal(mod(i,3))): #Calling Function & Reusability
        print('fizzbuzz')
    elif(equal(mod(i,3))):
        print('fizz')
    elif(equal(mod(i,5))):
        print('buzz')
    else:
        print(i)


