import emoji as emoji

name = "sateesh ganta"
name_split = name.split(" ")
print(name_split)
for n in name_split:
    print(n[::-1], end="")

#
# class Vehicle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def show(self):
#         print(self.a)
#
#
# v = Vehicle(10, 20)
# v.show()


students = {"name": "satish", "id": "1234"}
# for stu in students:
keys_li = list(students.keys())
val_li = list(students.values())
print(keys_li, val_li)


n = 7
for i in range(1, 11):
    # result = n * i
    print(n, "X", i, "=", n*i)

given_string = "rotatorr"
rev_string = given_string[::-1]
if given_string == rev_string:
    print(given_string, " is palindrome")
else:
    print(given_string, " is not a palindrome")


n = 5
fact = 1
for i in range(1, n+1):
    fact = fact * i
    print("factorial of ", n, " is:", fact)


num_list = [10, 50, 0, 120, 3]
l_num = num_list[0]
for num in num_list:
    if num > l_num:
        l_num = num
print("Largest number is: ", l_num)


random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = {}
for i in random_list:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1
print("Frequency: ", frequency)

list1 = ['s', 'a', 't', 'i', 's', 'h']
list2 = ['s', 'a', 't', 't', 'i', 'k', 'a']
common_list = []
for item in list1:
    if item in list2:
        common_list.append(item)
print("The common list is:", common_list)

n = 5
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, " :is not a prime")
            break
    else:
        print(n, ": is a prime")


string = "Hello, World!"
print("String is: ", string[0:7])

exp_text = "Hello, Your Coupon Code Copied. 😃" \
           "Please select your preferred bus routes and avail this discount offer on your bus ticket booking now!"
print("Strip text: ", exp_text.split())