#1
while msg !=1234:
	print("wrong password")

print("correct")

#2
num=1
while num<11:
  print(num)
  num=num+1










# With a for loop
for x in range(3):
	for num in range(1,11): 
		print("\U0001f600" * num)

# With a while loop
times = 1
while times < 11:
	print("\U0001f600" * times)
	times += 1

# Without string multiplication - ugly solution
# for num in range(1,11): 
# 	count = 1
# 	smileys = ""
# 	while count <= num:
# 		smileys += "\U0001f600"
# 		count += 1
# 	print(smileys)

##3
msg = input("Say Something: ")


while msg != "stop copying me":
	print(msg)
	msg = input()
print("UGH FINE YOU WIN, BROTHER!")

# while msg != "stop copying me":
# 	msg = input(f"{msg}\n")
# print("UGH FINE YOU WIN, BROTHER!")
