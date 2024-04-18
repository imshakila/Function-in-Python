def my_function (fname ,lname):
    print(fname + " " +lname)


my_function("shakila","gholipour")  

#---------------------------------------

def my_function(*kid):
    print("the youngest child is " + kid[2])

my_function("shakila","parya","hanita")
#----------------------------------------
def my_function(**kid):
    print("his last name is" + kid["lname"])

my_function(fname = "shakila", lname ="gholipour")
#---------------------------------------------------
def my_function(country = "Spain"):
    print("I am from" + country)

my_function("Sweden")
my_function("Iran")
my_function()
#---------------------------------------------------
fruits = ['apple','cherry','orange']
for i in fruits :
    print (i)
#-------------------------------------------------------
def my_function(food):
    for i in food :
        print(i)
fruits = ["apple","cherry","orange"]
my_function(fruits)
#-----------------------------------------------------------
def my_function(x):
    return 4*x
print(my_function(3))
print(my_function(7))
#-------------------------------------------------------
x = lambda a:a+10
print(x(5))
#=========================================================
x = lambda a,b:a*b
print(x(4,5))
#---------------------------------------------------------
x = lambda a,b,c : a+ b + c
print(x(3,4,5))
#------------------------------------------------------
def myfunc(n):
    return lambda a: a*n

mytripler = myfunc(3)
mydoubler = myfunc (2)
print(mytripler(11))
print(mydoubler(11))
#===================================== use lambda function when an anonymouse function is required for a short period of time
