#Write a function that uses while, if and continue statements 
#to print all the even numbers between 0 and 50. 
def even_numbers():
    num=1
    while num <=50:
        num+=1
        if num%2!=0:
         continue
        print(num)


#Write a function that takes an integer argument and prints "Prime" if the number is prime,
# and "Not prime" if the number is not prime.
def prime_numbers(lst):
    for num in range(10,100):
        if num >1:
            for i in range(2,num):
                if(num%i)==0:
                    print("Prime")
                else:
                    print("Not prime")

#Write a function that takes a list of integers as input and 
#prints the sum of all the even numbers in the list.
def sum_evennumbers(num):
    sums=0
    for i in num:
        if i%2==0:
            sums+=i
    print (sums)

#Write a function that takes any two integers as input, 
#and prints the sum of all the numbers between the two integers (inclusive)
# that are divisible by 3.
def Addition_nums(a,b):
    addition=0
    for num in range(a,b+1):
        if num%3==0:
            addition+=i
            print(addition)


