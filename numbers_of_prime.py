num, prime = int(input("Till where prime number you want : ")), []

print("Prime number : ")

for i in range(1,num+1):
    count = 0
    for j in range(1,num+1):
        if i%j==0:
            count+=1
    if count==2:
        prime.append(i)
        #print(f'{i}\t')
print(prime)