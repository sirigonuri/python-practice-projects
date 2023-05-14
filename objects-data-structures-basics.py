a = 1/4 + 25*2+100-50
print(a)

def practice_function():
    a = 4 * (6 + 5)
    b = 4 * 6 + 5
    c = 4 + 6 * 5
    d = 100 ** 0.5
    e = 10**2
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(type(3 + 1.5 + 4))
    s = "hello"
    print(s[1])
    #Reverse a string using slicing
    print(s[::-1])
    #First method to print o
    print(s[-1])
    #Second method to print o
    print(s[4])
practice_function()

def build_lists():
    a = [0,0,0]
    print(a)
    b = (0,0,0)
    c = list(b)
    print(c)
    list3 = [1,2,[3,4,'hello']]
    list3[2][2]='goodbye'
    print(list3)
    list4 = [5,3,4,6,1]
    list4.sort()
    print(list4)
build_lists()

def build_dictionaries():
    d = {'simple_key':'hello'}
    print(d['simple_key'])
    d = {'k1':{'k2':'hello'}}
    print(d['k1']['k2'])
    d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
    print(d['k1'][0]['nest_key'][1][0])
    d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
    print(d['k1'][2]['k2'][1]['tough'][2][0])
build_dictionaries()

def build_sets():
    list5 = [1,2,2,33,4,4,11,22,3,3,2]
    print(set(list5))
build_sets()

def boolean_test():
    # two nested lists
    l_one = [1,2,[3,4]]
    l_two = [1,2,{'k1':4}]

    # True or False?
    print(l_one[2][0] >= l_two[2]['k1'])
boolean_test()
