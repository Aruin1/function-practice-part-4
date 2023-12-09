#first function finds the max of a set of numbers

def max_num(list):
    list.sort(reverse=True)
    return list[0]

numbers = [5, 10, 18, 6, 3, 23, 9, 14]

print(max_num(numbers))

#second function multiplies a set of numbers

def multi_list(list):
    product = 1
    for x in list:
        product = product * x
    return product

print(multi_list(numbers))

#third function reverses a string

def rev_string(string):
    return string[::-1]

print(rev_string("hello"))

#fourth function checks if a number is between two numbers (inclusive)

def num_within(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False
    
print(num_within(5, 10, 15))
print(num_within(12, 10, 15))

#fith function prints n rows of Pascal's triangle

def pascal(n):
    list = []
    for i in range(n):
       temp_list = []
       for j in range(i+1):
           if j == 0 or j == i:
               temp_list.append(1)
           else:
               temp_list.append(list[i-1][j-1] + list[i-1][j])
       list.append(temp_list)
    #printing the created triangle
    printed_list = ""
    for i in range (n):
        for j in range(i+1):
            printed_list = printed_list + str(list[i][j]) + " "
        printed_list = printed_list + "\n"

    return printed_list

print(pascal(5))