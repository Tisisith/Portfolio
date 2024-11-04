#products = ['phone', 'tablet', 'laptop', 'journal']
#
#item = input('Enter product to search: ').lower()
#
#print(item in products)

#items = ['phone', 'tablet', 'map', 'glass']
#
#add_item = input('Enter product to add: ')
#
#add_after = input(f"After which item would you like to add {add_item} ")
#
#index = items.index(add_after)
#
#items.insert(index+1, add_item)
#
#print(items)

# products = {'phone':100, 'tablet':200, 'laptop':400, 'journal':40}
#
# print(products)
# new_product = input("Enter a product you want to add: ")
# new_product_price = input("What is the price? ")
# products[new_product] = new_product_price
# print(f'The new products list is {products}')

#for x in range(5):
#    print("I love you, Camille!")

#fruits = ['apple','banana','orange']
#for x in fruits:
#    print(x)

#people = {"Camille":30, "Nelson":33,"Donna":32}
#for man in people.items():
#    print(man)

#counter = 1
#while counter<=10:
#    print(counter)
#    counter +=1

#counter =0
#while counter<=10:
#    print(counter)
#    if counter==5:
#        break
#    counter=counter+1
#print("Line after the loop")


#counter = 0
#while counter <=9:
#    counter += 1
#    if counter ==5:
#        continue
#   print(counter)

#cart=[]
#numbers = int(input('How many items do you want to include in the cart? '))
#items = 1
#while items<=numbers:
#    item = input('Enter an item into the cart ')
#    items += 1
#    cart.append(item)
#print(cart)

#cart=[]
#n = int(input('How many items? '))
#
#for x in range(n):
#    item= input("What item do you want to add into the cart: ")
#    cart.append(item)
#
#for y in cart:
#    print(y)

'''MY VERSION OF THE WHILE LOOP'''
# cart=[]
# y = input("Do you want to add an item in the cart? ")
# while y=='y'.lower():
#     item=input("What item do you want to add in the cart? ")
#     cart.append(item)
#     y1 = input("Do you want to add an item in the cart? ")
#     print(cart)
#     if y1=='n'.lower():
#         break
# print(f"Here are your items {cart}")

'''OTHER VERSION'''
#cart=[]
#while True:
#    choice = input("Do you want to add item to the cart? ")
#    if choice =='n'.lower():
#        break
#    item = input("What item do you want to add into the cart: ")
#    cart.append(item)
#print(f"Here are your items! {cart}")


products = [
    {'name':'iPhone','price':500000,'description':'a very expensive product'},
    {'name':'iPad','price':49879,'description':'a very nice tablet'},
    {'name':'travel','price':30000,'description':'stupid ideal'}
]
#ADDING ITEMS TO CART
#cart= []
#while True:
#    choice = input('Do you want to continue shopping?')
#    if choice=='y'.lower():
#        print("Here is the list of the products:\n")
#        for index, product in enumerate(products):
#            print(f"{index}: {product['name']}: {product['description']} : ${product['price']}\n")
#        product_id = int(input("What product ID would you like to purchase? "))
#        if products[product_id] in cart:
#            products[product_id]['quantity']+=1
#        else:
#            products[product_id]['quantity']=1
#            cart.append(products[product_id])
#        total = 0
#        print('Current contents are: ')
#        for product in cart:
#            print(f"{product['name']}: {product['price']}: QTY: {product['quantity']}")
#            total = total+ product['price']*product['quantity']
#            print(f'Your current total is {total}')
#    else:
#        break
#print(f"Thank you! Your total cart value is {total}")


#CODING CHALLENGES
#for x in range(5):
#    print('I am a programmer')
#
#def square():
#    for x in range(1,10):
#        print(x**2)
#square()

#def add(a,b):
#    print(a+b)
#
#add(4,5)


#def speed(distance, time):
#    print(distance/time)
#
#speed(distance=500,time=100)



#def area(radius, pi=3.14):
#    print(pi*radius*radius)
#
#area(50)

#def area(radius, pi=3.14):
#    print(pi*radius*radius)
#
#area(10,3.15)


#def area(radius,pi=3.14):
#    result = pi*radius*radius
#    return result
#
#def cost(circle_area,cost_per_sq_m):
#    tc = circle_area*cost_per_sq_m
#    return tc
#
#calculated_area = area(100)
#total_cost = cost(calculated_area, 10)
#
#print(total_cost)

#def area(r):
#    area = 3.14*r*r
#    circumference = 2 *3.14*r
#    return area, circumference
#
#a,c = area(100)
#print(f"Area is {a}, circumference is {c}")


#REMOVING DUPLICATES VERSION 1
#def remove_duplicates(numbers):
#    new_list=[]
#    for x in numbers:
#        if x not in new_list:
#            new_list.append(x)
#    return new_list
#
#ids = [1,2,3,4,5,6,7,1,3,4]
#a = remove_duplicates(ids)
#print(a)

#REMOVING DUPLICATES(SHORT VERSION)
#def remove_duplicates(numbers):
#    return list(set(numbers))
#
#ids = [1,2,3,4,1,2,4,5,6]
#result=remove_duplicates(ids)
#print(result)

# LOCAL VS GLOBAL VARIABLE

#CHECK IF A PALINDROME
#word = ('noon')
#l = len(word)
#
#palindrome_flag = True
#
#for x in range(l):
#    if word[x] != word[l-x-1]:
#        palindrome_flag=False
#        break
#    else:
#        palindrome_flag=True
#
#if palindrome_flag==True:
#    print('The word is a palindrome!')
#else:
#    print('The word is not a palindrome!')


#CHECK IF PALINDROME(FUNCTION VERSION)
#def check_palindrome(word):
#    l = len(word)
#    for x in range(l):
#        if word[x]!=word[l-x-1]:
#            return False
#    return True
#
#print(check_palindrome('racecar'))


#EMI Calculator
#def emi_calculator(principal, rate, time):
#    r = rate/12/100
#    emi = (principal * r*(1+r)**time)/ ((1+r)**time-1)
#    return emi
#
#print(emi_calculator(50000000,8.75,240))


#RECURSION
#def hello():
#    print("Hello")
#    hello()
#
#hello()

#FACTORIALS IN RECURSION
#def factorial(number):
#    if number ==1:
#        return 1
#    else:
#        return number * factorial(number-1)
#print(factorial(4))
#EXPLANATION
# factorial(4) => return 4 * factorial(3)
# factorial(3) => return 3 * factorial(2)
# factorial(2) => return 2 * factorial(1)

#MULTIPLE VARIABLES
#def add(*args):
#    sum=0
#    for n in args:
#        sum = sum+n
#    return sum
#print(add(1,2,3,4,5,9,23.56,20))

#MULTIPLE VARIABLES WITH KEYWORD ARGUMENTS
#def product(**kwargs):
#    for key,value in kwargs.items():
#        print(f"{key}:{value}")
#
#product(name='iphone',product="700")
#product(name='iphone',price="400",description="an stupid idea")


#DECORATORS
#def chocolate():
#    print("Chocolate")
#
#def decorator(a):
#    def wrapper():
#        print('Wrapper inside up')
#        a()
#        print("Wrapper outside up")
#    return wrapper
#
#chocolate= (decorator(chocolate))
#chocolate()

#DECORATORS OTHER VERSION
#def decorator(a):
#    def wrapper():
#        print('Wrapper inside up')
#        a()
#        print("Wrapper outside up")
#    return wrapper
#@decorator
#def chocolate():
#    print("Chocolate")
#@decorator
#def cake():
#    print("Cake")
#chocolate()
#cake()

#DECORATORS WITH MULTIPLE ARGUMENTS
#def decorator(a):
#    def wrapper(*args,**kwargs):
#        print('Wrapper inside up')
#        a(*args,*kwargs)
#        print("Wrapper outside up")
#    return wrapper
#@decorator
#def chocolate():
#    print("Chocolate")
#@decorator
#def cake(name):
#    print(f"Cake "+ name)
#chocolate()
#cake('apple')


#DECORATOR THAT RETURNS A VALUE (MY VERSION)
#def summer_discount(func):
#    def wrapper(price):
#        b= func(price*0.20)
#        print(f"Our summer discount for your price is {b}")
#    return wrapper
#@summer_discount
#def total(price):
#    return price
#total(500)


#def summer_discount_decorator(func):
#    def wrapper(price):
#        func(price)
#        return func(price/2)
#    return wrapper
#
#@summer_discount_decorator
#def total(price):
#    return price
#
#print(total(1000))

#def bmi_calc(weight,height):
#    bmi = weight/(height**2)
#    return bmi
#
#weight = float(input("Enter your weight in kg "))
#height = float(input("Enter your height in meters "))
#
#print(bmi_calc(weight,height))

#MODULES
#import greet
#
#greet.hello()
#greet.bye()

#MODULES USING FROM
#from greet import hello, bye
#bye()

#RANDOM MODULE
#import random
#
#print(random.randint(1,10))

#DATETIME MODULE
#from datetime import date,datetime
#print(datetime.now())
#print(date.today())

#ERRORS & EXCEPTIONS
#SYNTAX ERROR - programming language error
#LOGICAL ERROR - program works but your program doesn't make sense/ output is not expected
#RUNTIME ERROR - error that happens when your program is actually running (Division by Zero, Undefined Variable errors)
#EXCEPTION HANDLING

#TRY/EXCEPT BLOCK

#n = int(input("Enter numerator: "))
#m = int(input("Enter denominator: "))
#result=0
#try:
#    result = n/m
#except ZeroDivisionError:
#    print("Cannot divide by zero!")
#print(result)

#ELSE BLOCK - happens when the exception didn't occur
#n = int(input("Enter numerator: "))
#m = int(input("Enter denominator: "))
#try:
#    result = n/m
#except ZeroDivisionError:
#    print("Cannot divide by zero!")
#else:
#    print(result)

#FINALLY BLOCK - happens no matter what
#n = int(input("Enter numerator: "))
#m = int(input("Enter denominator: "))
#try:
#    result = n/m
#except ZeroDivisionError:
#    print('cannot divide by zero!')
#else:
#    print(result)
#finally:
#    print("I love you!")

#CODING CHALLENGE:
#def divide(n,m):
#    result=n/m
#    return result
#try:
#    a= divide(56,56)
#except ZeroDivisionError:
#    print("cannot divide by zero!")
#else:
#    print(a)

#OPENING A FILE
#file = open('data.txt','r')
#content = file.readline()
#print(content)
#file.close()

#WRITING AND APPENDING FILE
#file = open('data.txt','a')
#content = "This is a third line"
#file.write(f"\n{content}")
#file.close()

#USING WITH IN OPENING FILES
#with open('data.txt','r') as file:
#    contents = file.read()
#    print(contents)


#with open('data.txt','r') as file:
#    line1 = file.readline()
#    print(line1)

#STRIP, LSTRIP, RSTRIP
#text = "    Hello World!   "
#stripped_text = text.strip()
#print(stripped_text)

#READLINE VS READLINES
#with open('data.txt','r') as file:
#    content = file.readlines()
#for line in content:
#    print(line.strip())


#READING AND WRITING FILES + Capitalize
#while True:
#    with open('write.txt','a') as file:
#        name = input("Enter a name: ")
#        file.write(name+"\n")
#        choice = input('Do you want to add another name: (y/n')
#        if choice == 'n':
#            break
#
#with open('write.txt','r') as file:
#    nelson = file.readlines()
#
#for x in nelson:
#    print(x.strip().capitalize()

#SAVING COMPLEX DATA
#def save_user_data():
#    with open('write.txt','a') as file:
#        name= input('Enter name: ')
#        email = input("Enter email: ")
#        contact = input('Enter contact: ')
#        user_data = f"Name: {name}\n Email: {email} \n Contact: {contact}\n"
#        file.write(user_data)
#
#def open_data():
#    with open('write.txt','r') as file:
#        print(file.read())
#
#save_user_data()
#open_data()

#SERIALIZING DATA USING JSON
#import json
#data = {
#    "name:":"Nelson",
#    "age:":30,
#    "city":"New York"
#}
#json_data = json.dumps(data)
#print(type(json_data))

#DESERIALIZATION
#import json
#json_data = '{"name":"John Doe","age":30,"city":"Philippines"}'
#data = json.loads(json_data)
#print(data['age'])

#LOADING AND ADDING NEW DATA (1 out of 4)
import json
import os
def save_user_data():
    user_list=[]
    while True:
        name = input("Enter name or type 'quit' ")
        if name == 'quit':
            break
        age = input("Enter age : ")
        location = input("Enter location: ")
        user_dict = {
            "name": name,
            "age": age,
            "location": location
        }
        user_list.append(user_dict)

    if os.path.exists('new.json'):
        with open('new.json','r') as file:
            data = json.load(file)
        user_list.extend(data)

    with open('new.json','w') as file:
        json.dump(user_list,file)

#READING EXISTING DATA + CRUD - CREATE READ UPDATE DELETE (2 out of 4)
def read_user_data():

    if not os.path.exists('new.json'):
        print("No user data found")
        return

    with open('new.json','r') as file:
        user_list = json.load(file)
        for person in user_list:
            print(f'Name:{person["name"]}')
            print(f'Email:{person["age"]}')
            print(f'location:{person["location"]}')
            print('\n')


#UPDATING USER DATA (3 out of 4)
def update_user_data(edit_name):

    if not os.path.exists('new.json'):
        print("No user data found")
        return

    with open('new.json','r') as file:
        user_list = json.load(file)

    user_found = False
    for person in user_list:
        if person['name'] == edit_name:
            print('Data found for this person')
            age = input('Input new age: ')
            location = input('Input new location')
            person["age"] = age
            person["location"] = location
            user_found = True
            break


    if not user_found:
        print('Person does not exist')

    with open('new.json','w') as file:
        json.dump(user_list,file)
    print("User data updated!")

#DELETING USER DATA
def delete_user_data(delete_name):

    if not os.path.exists('new.json'):
        print("No user data found")
        return

    with open('new.json','r') as file:
        user_list = json.load(file)

    user_found = False
    for person in user_list:
        if person['name'] == delete_name:
            user_list.remove(person)
            user_found = True
            break


    if not user_found:
        print('Person does not exist')

    with open('new.json','w') as file:
        json.dump(user_list,file)
    print("User data updated!")

delete_name = input("Whose data do you want to delete data for: ")
delete_user_data(delete_name)





