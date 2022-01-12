def prime_checker(number):
        a=number-1
        while 1<a<number:
                if number ==2 or number==1:
                        print("It's a prime number.")
                        break
                if number%a == 0:
                        print("It's not a prime number.")
                        break
                if number%a != 0 and a==2 and number!=2:
                        print("It's a prime number.")
                        break
                else:
                        a=a-1





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



