sample_string = "This is a String"

# length of a string
print("Length: ", len(sample_string))

# print first index of string
print(sample_string[0])

# slicing
print(sample_string[-1])
print(sample_string[0:4])
print(sample_string[8:])
print(sample_string[:5])
print(sample_string[0::2])

# Reverse a String
print(sample_string[::-1])

# for char in sample_string:
#     print(char)


# Get unicode characters
print("A = ", ord("A"))
print("65 = ", chr(65))

# Program to convert a string to secret string

# message = input("Enter a string to hide: ")
# message = message.upper()
# secret = ""
#
# for char in message:
#     secret += str(ord(char))
# print("Secret message: ", secret)
#
# original_message = ""
# for i in range(0, len(secret)-1, 2):
#     char_code = secret[i] + secret[i+1]
#     original_message += chr(int(char_code))
# print("Original message: ", original_message)


# Program to Create an Acronym
# user_input = input("Enter a string to convert into the acronym: ")
# words = user_input.split(' ')
# acronym = ""
# for word in words:
#     acronym += word[0]
# print("Acronym: ", acronym.upper())

