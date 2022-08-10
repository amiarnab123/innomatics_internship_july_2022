# Enter your code here. Read input from STDIN. Print output to STDOUT
c = 0
e = int(input())
eng = set(map(int,input().split()))
f = int(input())
french = set(map(int,input().split()))
for i in eng:
    if i not in french:
        c += 1
print(c)
