#https://www.studytonight.com/data-structures/bubble-sort
#https://www.bigocheatsheet.com
#https://www.quora.com/What%E2%80%99s-the-simple-explanation-for-O-n-log-n
#https://www.studytonight.com/data-structures/merge-sort
#Bubble Sort
z = [6,5,4,3,2,1]
#z = [1,2,3,4,5]
n = len(z)

print("Unsorted Array:",z)

for i in range(n):
    print("i",i)
    for j in range(n-1-i):
        if z[j] > z[j+1]:
            z[j],z[j+1]=z[j+1],z[j]
            print(z)
print("Bubble Sort:",z)
