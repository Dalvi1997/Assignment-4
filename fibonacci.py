n1=1
n2=1
count=1
for count in range(1,11):
    print(n1,end=",")
    nth=n1+n2
    n1 = n2
    n2 = nth
    count += 1

