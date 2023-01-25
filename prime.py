num = int(input('Enter number to check prime or not : '))
count =0

for i in range(1,num+1):

    if num%i==0:
        count+=1

if count==2:
    print(f'{num} is prime number')
else:
    print(f'{num} is not prime number')