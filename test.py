#task1
"""
string = "Welcome Mahmoud"
vowels = "aeiou"
vowel_count=0
for i in string:
    if i in vowels:
        vowel_count+=1
    
print(f"The Number Of Vowel in {string} is: {vowel_count}")
"""
#task2
"""
def generat_array(length,start):
    array=[start+i for i in range(length)]
    return array

len=4
st=10
result= generat_array(len,st)
print("Generated Array Is : ",result)
"""
#task3
"""
user_input = [int(input(f"Enter the Element {i+1}: ")) for i in range(5)]

ascending = sorted(user_input)
descending = sorted(user_input, reverse=True)

print(f"\nOriginal array: {user_input}")
print(f"\nAscending array: {ascending}")
print(f"\nDescending array: {descending}")
"""
#task4
"""
def cheack(num):
    if num%3==0:
        return "FIZZ"
    elif num%5==0:
        return "buzz"
    elif num%3==0  and num%5==0:
        return "FizzBuzz"
    else:
        return  num

n=16
print ("the Output ",cheack(n))
    """
#task5
"""
def revers_string(string):
    return  string[::-1]

s="Hello World!"
print (revers_string(s))
"""

#Task6
"""
radius = input("Enter The radius :")
area=radius*radius*3.14
circumference=3.14*2*radius
print(f"The Area = {area} and circumference = {circumference}")
"""
#task7
"""
def get_user_data():
    name = input("Enter your name: ")
    
    while not name or name.isdigit():
        print("Invalid input. Please enter a valid name.")
        name = input("Enter your name: ")

    email = input("Enter your email: ")

    return name, email
    
    """
#task 8
"""
def count_occurrences(input_text, target_substring):
    count = input_text.lower().count(target_substring.lower())
    return count


input_text = "itida is a great place to learn, itida is awesome, ItiDa"
target_substring = "itida"

occurrences = count_occurrences(input_text, target_substring)
print(f"The substring '{target_substring}' occurs {occurrences} times in the given text.")

"""
#task 9

def alphabetical_substring(input_string):
    current_substring = input_string[0]
    longest_substring = input_string[0]

    for char in input_string[1:]:
        if char >= current_substring[-1]:
            current_substring += char
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        else:
            current_substring = char

    print(f"Longest substring in alphabetical order is: {longest_substring}")


input_string = "abcdkabdhefg"
alphabetical_substring(input_string)


