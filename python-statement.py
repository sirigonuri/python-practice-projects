# Python Statements Assessment

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
def test_func():
    st = 'Print only the words that start with s in this sentence'
    test = st.split()
    print(test)
    for x in test:
        if x[0] == 's':
            print(x)            
test_func()

# Use range() to print all the even numbers from 0 to 10.
for x in range(0,11):
    if x % 2 == 0:
        print(x)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
print("Below given are the numbers that are divisible by 3")
for x in range(51):
    if x % 3 == 0:
        print(x)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
test = st.split()
for word in test:
    l = len(word)
    if l % 2 == 0:
        print("Length of the word '" + word + "' is " + "even!")

# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1,101):
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
test = st.split()
lst = [letter[0] for letter in test]
print(lst)
