# Question 1: Basic Function Definition and Calling
def greet():
   print("Hello, World!")

greet()

# Question 2: Function with Parameters
def personalized_greeting(name):
   print("Hello,", name)

personalized_greeting("Azaxole")

# Question 3: Function with return value  
def square(number):
   return number **2

result = square(5)
print(result)

# Question 4: Function with Multiple Parameters And Return Value

def rectangle_area(lenth, width):
   return lenth * width

result = rectangle_area(4, 5)
print(result)

# Question 5: Using A Function As A Argument

def apply_operation(function, number):
   return function(number)

def double(number):
   return number * 2

print(apply_operation(double, 7))
print(apply_operation(square, 3))

   
