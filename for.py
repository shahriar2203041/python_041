#1

for x in range(1,9):
	print(x)
	print(x*10)
for letter in "shah":
	print(letter)
print("hello shah"*10)
for word in "kamal": 
	print(word)
#2



for shah in range(4,10,1):
    print(shah)


#3

temp=0
for shah in range(11,20,2):
    temp=temp+shah
    
print(temp)



#4
times = input("How many times do I have to tell you? ")
times = int(times)

# Simplest Version
for time in range(times):
	print("CLEAN UP YOUR ROOM")

# Version 2
for time in range(times):
	print(f"time {time+1}:CLEAN UP YOUR ROOM")




#5
for num in range(1,21):
    if num==4 or num==13:
        print(f"the {num} number is unlucky")
    elif num%2==0 :
        print(f"{num}number is even")
    else:
        print(f"{num}number is odd")
