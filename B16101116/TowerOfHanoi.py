def hanoi(n,source,destination,temp):
    if n>1:
        hanoi(n-1,source,temp,destination)
        hanoi(1,source,destination,temp)
        hanoi(n-1,temp,destination,source)
    else:
        Move(source, destination)
def Move(src,dest):
    print("moving from" +  src + "to" + dest)
n=3
source="A"
temp="B"
destination="C"
hanoi(n,source,destination,temp)