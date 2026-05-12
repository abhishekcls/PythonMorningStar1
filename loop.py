#loop -> to repeat
print("for")
for i in range(5):
    print(i)

print("odd")
c=0
for i in range(1,100,2):
    print(i)
    c=c+1
    if c==5:
        break

print("while")
i=0
while i<5:
    print(i)
    i=i+1