#Find and Replace

words = "It's thanksgiving day. It's my birthday, too!"

print words.find("day")
print words.replace("day", "month")

#Min and Max
x = [2,-50,-2,7,125,98]

print min(x)
print max(x)

#First and Last
x = ["peanut",2,54,-2,7,12,98,"planet"]
newlist= []

print x[len(x)-1]
print x[0]

newlist.append(x[0])
newlist.append(x[len(x)-1])

print newlist


#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
y = []
z = []
i = 0

x.sort()
print x

for  count in range(len(x) /2):
    y.append(x[count])
    print count
print y 

for i in range(len(x) /2 -1, len(x)):
    z.append(x[i])
print z

z[0] = y

print z

