############
list=[1,2,3,4,4,5,6,7,7,9]
len(list)

###########
my_stuff=['shahriar',5,10.4,44]
print(my_stuff)
r=range(1,99)
my_list = list(r) 
print(my_list)

###############
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
people[0]="Hannah"
people[4]="Jeffrey"
people[5]="Aparna"

print(people)




##########
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
for human in people:
  print(human)




#####
people = [1,2,3,4,5,6,7]
i=0
while i<len(people):
  print(people[i])
  i=i+1



###
people = [1,2,3,4,5,6,7]
i=0
while i<len(people):
  print(f"{i}:{people[i]}")
  i=i+1

####
I've given you a list called sounds .  It looks like this:

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"] 

Write code that loops over the list and adds all the strings together to form one large combined string (don't add any spaces between them) 
The combined string should be in all UPPERCASE as well 
Save the result in a variable called result  


solution:

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result =''

for s in sounds:
    result += s
result = result.upper()
print(result)

###
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
sounds.append(5)
print(sounds)

###

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
sounds.extend([5,6,7,8,9,0,10,11])
print(sounds)

####
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
sounds.extend([5,6,7,8,9,0,10,11])
print(sounds)
sounds.insert(2,66)
print(sounds)

