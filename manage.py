# import random;

# condition = random.randint(0, 1)

# print(condition);

# if condition == 0:
#     print("Condition is false");
# elif condition == 1:
#     print("Condition is true");


# condition = False 
# if condition: 
# 	print("Python is the best!")


# condition = False 
# if condition: 
# 	print("Python is the best!") 
# else: print("Python is my favorite language!")


# condition = False 
# other_condition = True 
# if condition: 
# 	print("Python is the best!") 
# elif other_condition: 
# 	print("The other condition is", other_condition) 
# else: print("Python is my favorite language!")



# fizzbuzz

# define  a variable for the number being checked
# number = 15
# # if the number is divisible by 3 and 5 print 'fizzbuzz'
# if number % 3 == 0 and number % 5 == 0:
#     print('fizzbuzz')
# # if the number is divisible by 3 print 'fizz'
# elif number % 3 == 0:
# 	print('fizz')
# # if the number is divisible by 5 print 'buzz'
# elif number % 5 == 0:
#     print('buzz')

# # if the number is not divisible by 3 or 5 print 'nothing'
# else:
#     print('nothing')


# condition = ( 5 % 2 != 0) 
# if condition: 
# 	print("Python is the best!") 
# else: 
#     print("Python is my favorite language!")


# n = 5 
# while n < 0: 
#     if n % 2 == 0: 
#         break 
#     else: continue


# function
# def hello(a, b):
# 	print(a+b)
	


# hello(4,6)

# global_var = "global"
# def func():
# local_var = "local"
# print(global_var)
# func()


mylist = [1,2,3,4,5,6, [1,2,3,], 'spam', True]
myTuple = (1,2,3,4,5,6, [1,2,3,], 'spam', True)

# print(mylist)

mylist.append('Eggs');
# print(mylist)


# print(mylist[-1]) #last element
# print(mylist[0:2]) #slice(0,2)

################################################################
####LIST IN PYTHON #################################

# loop over numbers between 1 and 100 and make a lisr of even numbers
evens = []

count = 0

while count <= 100:
    if count % 2 == 0:
        evens.append(count)
    count += 1

print(evens)


my_numbers = [1,2,3,4,5,6]
print("+++++++:",my_numbers[::-1])

######## TUPLES #################################
print(" ")
print("############# TUPPLES #################################")
print(" ")

me = (25, "Daniel", True, ['Coding', 'Reading'])
print(me)
#  tuple unpacking
age, name, employed, hobbies = me;

hobbies.append('Teaching')
print(hobbies);


a = 21
b = 42


print("Original A: ",a)
print(b)
temp = a
a = b
b = temp
print(a)
print(b)



######## RANGES AND FOR #################################
print(" ")
print("############# RANGES #################################")
print(" ")

start = 0
stop   = 101
step = 2

my_range = range(start, stop, step)

total = []

for number in my_range:
    total.append(number ** 2)
print(total)

######## DICTIONARY #################################
print(" ")
print("############# DICTIONARY #################################")
print(" ")

me = {'name': 'Daniel', age: '25'}
print(me["name"])

me["hobbies"] = ['coding', 'problem solving']

print(me)

me["hobbies"].append('sleeping')

print(me)

my_string = 'I love coding with veroskills'
letter = {};

for char in my_string:
    # letter[char] = 'hi'
    if char not in letter.keys():
        letter[char] = 1
    else:
        letter[char] += 1
print(letter)


######## CLASSES #################################
print(" ")
print("############# CLASSES #################################")
print(" ")


class Account:
    def __init__(self, accountType, balance):
        self.accountType = accountType
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount

checking = Account('checking', 5000)

checking.deposit(3000)

print(checking.accountType, 'account type')
print(checking.balance, 'balance')