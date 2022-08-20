    # basic



# def main():
#     print(55)
#     print("Sameer")
#     print('Gupta')
#     age = input('What is your age?\n')
#     print(age)
# if __name__ == "__main__":
#     main()

    # variables



myint = 5
myfloat = 54.9
mybool = True
mystr = "This shit is string"
mylist = [3,2,'Nani',88,54,56,99]               # sequence type             (0,1,2,3,4.......)
mytuple = (5 , 9 , 56)                 # this can not be changed   (0,1,2,3,4.......)
mydict = {"One" : 1, "Two" : 2}        # Provide unique values

# print(mylist[0])
# print(mytuple[1])

        # slice the list



# print(mylist[0:2])
# print(mylist[0:6:2])
# print(mylist[::-1]) # reverse the sequence)
# print(mydict["One"])

# print("YOYO " + "hONEYsINGH " + str(12345))  #concationation of strings

        # funtion



# def func1() :
#     print("This is Function")

# func1()
# print(func1())  #Two results , print value and None

# def maths1(x) :                  Some error here 
#     return x*x

# x = input("Enter First value\n")
# # y = input("Enter second value\n")
# maths1(x)                             To here

# def multi_add(*values):
#     result = 0
#     for i in values:
#         result = result + i
#     return result

# print(multi_add(1,21,3,5,6))

    # Conditionals



# def cond():
#     x = input("Input X\n")
#     y = input("Input Y\n")

    # if x > y:
    #     result = "x is greater than y"
    # elif x < y:
    #     result = "x is less then y"
    # else :
    #     result = "x equal y"

    # print(result)

#     result = "x is greater than y" if x > y else "x is smaller or equal to y"
#     print(result)
# cond()

# def match():
#     check = "two"
#     match check:
#         case "one":
#             result = 1
#         case "two":
#             result = 2
#         case "three" | "four":
#             result = (3,4)
#         case _:
#             return -1
#     print(result)

# match()

        #LOOPS


# def whileloop():
#     x = 0
#     while(x <= 5):
#         print(x)
#         x = x + 1
# whileloop()

def forloop():
    for x in range(5,10):   #looping in range
        print(x)
    
    days = ["mon","tue","wed","thus","fri","sat","sun"]   #looping over content of list
    for d in days:
        print(d)

    for x in range(11,21):          # break statment break through loop
        # if x == 19:
        #     break
        if x % 2 == 0:                 #continue means skip the print value and increment the value and go in start of loop again
            continue
        print(x)

    for i,d in enumerate(days):             # i praint index of the item 
        print(i,d)
forloop()
