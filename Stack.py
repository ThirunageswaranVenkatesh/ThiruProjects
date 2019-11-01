#https://www.tutorialspoint.com/python/python_lists.htm
#https://www.tutorialspoint.com/python/python_basic_operators.htm

# Stack Operation
#Push Operation
def push(x,y,z):
    x.append(y)
    maxpush(y,z)
    print("Stack after Push Operation:\n",x)

#Pushing data into Max value stack
def maxpush(x,y):
    if(len(y)==0):
        maxval=0
    else:
        maxval=y[len(y)-1]
    if (int(x) >= int(maxval)):
        maxval=x
        y.append(x)

#Pop Operation
def pop(z,m):
    c = len(z)
    if (c == 0):
        print("Stack is empty.\n")
    else:
        top_v =z[c-1]
        z.pop()
        print("Stack after Pop Operation:\n", z)
        temp = m[len(m)-1]
        if( int(top_v) == int(temp)):
            m.pop()

#Topmost element
def top(z):
    c=len(z)
    if(c==0):
        print("Stack is empty.\n")
    else:
        print("Top most element of stack:\n",z[c-1])
'''
#Find Maximum value - Alternative method
def maxval(z):
    c=len(z)
    if (c==0):
        print("Stack is empty.\n")
    else:
        maxv = z[0]
        for i in range(1,c):
            if z[i] > maxv:
                maxv = z[i]
    print("Max value in the stack is:\n", maxv)
'''

#Using List datatype for stack operation
stack = []
maxvalst =[]
operation =(1,2,3,4,5)
var = 1
while var == 1 :  # This constructs an infinite loop
    num = int(input("Enter a number to perform Stack Operation:\n1.Push\n2.Pop\n3.Top Element\n4.Max Value in Stack\n5.Exit\n"))
    if(num in operation):
        if(num==1):
            zz=input("Enter the value to push into stack:")
            push(stack,zz,maxvalst)
            print("Max Value Stack:\n", maxvalst)
        elif(num==2):
            pop(stack,maxvalst)
            print("Max Value Stack:\n", maxvalst)
        elif(num==3):
            top(stack)
        elif(num==4):
            if (len(maxvalst)==0):
                print("Stack is empty.\n")
            else:
                print("Max Value in the stack is:\n",maxvalst[len(maxvalst)-1])
        else:
            break
    else:
        print("Enter a valid Stack operation.\n")