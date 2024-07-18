

# get help
# help()

# string, tuple, list, dict

my_string = 'Daniel'
age = 30
# age = age + 1
age += 1

# print("age:", age)
# print(type(my_string))


# print(dir())

# n = 5
# while n < 0: 
#     if n % 2 == 0: 
#         print("it is even number")
#         break 
#     else: 
#         print("it is even number")
#         continue


# number = 15
# if number % 3 & number % 5 == 0:
#     print('Number is divisible by 3 and 5')
# elif number % 2 == 0:
#     print("Number is even")
# elif number % 3 == 0:
#     print("Number is divisible by 3")
# elif number % 5 == 0:
#     print("Number is divisible by 5")
# else:
#     print("Number is neither even nor divisible by 3 or 5")


name = 'Daniel' # global scope
def Sum(number1, number2):
    print("Sum = ", number1 + number2) #local scope
    
print('Hello,', name) #global scope   
Sum(2,3)

from manage import dog

myList = ['John', 'Daniel', 'Andrews', 'Damons']

myList.insert(2, 'Dan')
myList.append('Danny')
myList.pop()
print(myList)


myTuple = ('John', 'Daniel', 'Andrews', 'Damons')

print(myTuple.count('John'))
print(myTuple.index('Andrews'))
