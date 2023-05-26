# '''
# Function Practice Exercises - Warmup Exercise

# '''
# a=0
# b=0
# def number(a,b):
#     '''
#     Write a function that returns the lesser of two given numbers if both numbers are even, 
#     but returns the greater if one or both numbers are odd
#     '''
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second number:"))

#     if a%2==0 and b%2==0:
#         if a<b:
#             return a
#         else:
#             return b
#     elif a%2 !=0 or b%2 !=0:
#         if a>b:
#             return a
#         else:
#             return b
# result = number(a,b)
# print(result)

# def animals(word):
#     '''
#     Write a function takes a two-word string and returns True if both words begin with same letter
#     '''
#     words = word.split()
#     if words[0][0] == words[1][0]:
#         return True
#     else:
#         return False
# result_one = animals("Levelheaded Llama")
# result_two = animals("Crazy Kangaroo")
# print(result_one)
# print(result_two)

# def makes_twenty(n1,n2):
#     '''
#     Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#     '''
#     if (n1+n2) == 20:
#         return True
#     elif n1 == 20 or n2 == 20:
#         return True
#     else:
#         return False

# print(makes_twenty(12,8))
# print(makes_twenty(20,10))
# print(makes_twenty(4,4))

# def upper_case_letter(word):
#     '''
#     Write a function that capitalizes the first and fourth letters of a name
#     '''
#     length = len(word)
#     result = word[0].upper() + word[1:3] + word[3].upper() + word[4:length]
#     print(result)
# # upper_case_letter("macdonald")

# def reverse_words(sentence):
#     '''
#     Given a sentence, return a sentence with the words reversed
#     '''
#     r = " ".join(sentence.split()[::-1])
#     print(r)
# reverse_words('Hi my name is Siri')
# reverse_words('We are ready')

# def almost_there():
#     '''
#     ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#     '''
#     n = int(input("Enter n:"))
#     n1=90
#     n2=110
#     n3=190
#     n4=210
#     if (abs(100-n)<=10 or abs(200-n)<=10): 
#         return True
#     else:
#         return False
# res = almost_there()
# print(res)

# def find_33(nums_list):
#     '''
#     Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#     '''
#     for i in range(0, len(nums_list)-1):
#         if nums_list[i] == 3 and nums_list[i+1] == 3:
#             return True
#         return False

# s = find_33([1,2,3])
# print(s)
# result = find_33([3,3,1])
# print(result)
# e = find_33([3,3,1,1])
# print(e)

# def paper_doll(name):
#     '''
#     PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#     '''
#     result=''
#     for i in name:
#         result += i*3
#     return result

# r = paper_doll("Hello")
# print(r)
# res = paper_doll("Mississippi")
# print(res)

# def blackjack(a,b,c):
#     '''
#     BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
#     If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
#     Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#     '''
#     if (a+b+c) <= 21:
#         return (a+b+c)
#     elif (a+b+c) > 21:
#         if a==11 or b==11 or c==11:
#             return (a+b+c)-10
#         else:
#             return "BUST"

# r = blackjack(5,6,7)
# print(r)
# e = blackjack(9,9,9)
# print(e)
# s = blackjack(9,9,11)
# print(s)

def summer_69(array):
    '''
    SUMMER OF '69: Return the sum of the numbers in the array,
    except ignore sections of numbers starting with a 6 and extending to the next 9
    (every 6 will be followed by at least one 9). Return 0 for no numbers.
    '''
