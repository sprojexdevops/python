###########
# Integer #
###########
a = 10
b = 20
# result = a + b
#result = 10 + 20
# print("total sum:", result)
# print("memory address:", id(result))
# print("data type:", type(result))
# print("total sum:", result, "\nmemory address:", id(result), "\ndata type:", type(result) )
print(a + b)
print( a - b)
print(a * b)
print(a / b)

# modulo division --> returns the remainder
print(b % a)    
print(a % b)

# Integer division --> gives the quotient as integer without decimals
print(a // b)
print(b // a)

# exponential --> a^b 
print(a ** b)


##########
# string #
##########
# sample_str = "this is a string"
# sample_str2 = "This Is A String"
# sample_str3 = "THIS IS A STRING"

# print(sample_str, "\n",type(sample_str))

# dir() --> show the methods available for a specific data type
#print(dir(sample_str))

# capitalize() --> change the starting letter to uppercase
# print(sample_str.capitalize())

# change the entire string to uppercase
# print(sample_str.upper())   

# converts the entire string to lower case
# print(sample_str3.lower()) 

# casefold() --> change the starting letter or entire string to lower case
# print(sample_str2.casefold())   
# print(sample_str3.casefold())
 
# swapcase() --> change the case of a given string
# print(sample_str.swapcase())

# split() --> split the sentence into a list of words
# print(sample_str.split(' '))

# find() --> find a word or a letter in a string, gives the index value of it
# print(sample_str.find('a'))

# index() --> gives the index value of a letter
# sample_str = "this is a string"
# print(sample_str.index('i'))
# print(sample_str.index('string'))


# sample_str4 = "Hello"
# print(sample_str4.index('H'))
# print(sample_str4.index('o'))

# special_char = sample_str4[4]
# special_char2 = sample_str4[-1]
# print(special_char, special_char2)

# len() --> length of a string
# print(len(sample_str4))


###########
# boolean #
###########
# a = True
# b = False

# print(a and b)
# print(a or b)