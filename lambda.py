# lambda arguments: expression

s1 = 'GeeksforGeeks'

s2 = lambda func: func.upper()
print(s2(s1))

# A lambda function that adds 10 to the input
add_ten = lambda a: a + 10
print(add_ten(5)) # Output: 15

# A lambda function that multiplies two arguments
multiply = lambda a, b: a * b
print(multiply(5, 6)) # Output: 30