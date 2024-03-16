#16-03-2024
# 1) pyhton program to capitalize the first and last charecter of each word in a string 
'''
s1 = "hello world"
fst = s1[0].upper()
lst = s1[-1].upper()

print(fst+s1[1:len(s1)-1]+lst)
'''
# 2) input:128
#output : Yes
#128% 1 ==0,128% 2 ==0,and 128 % 8 ==0
'''
n= 128
temp = n
f1 = 0
while n!=0:
    rem = n%10
    check = temp % rem
    if check !=0:
        f1 = 1
        
    n = n//10

if f1==0:
    print("yes")
else:
    print("no")
'''



# 3)
#l1 = [1,2,3,4], 12= [5,6,7,8]
#add both l1 and l2,ArithmeticError ans = [6,8,10,12]
'''
l1= [8,9,0,7]
l2= [7,6,5,4]
l3=[]

'''
'''
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)
'''

'''

# ! ----> set


# charecterstic of set
'''
'''
1) set can be created using {}
2) the elements inside set are not indexd
3) does not allow duplicate values
4) it unordered
5)heterogenous   ----> acceot only unmutable datatypes
6)mutable or changable
'''

# eg : 1
#s1= {9,89,7.76,8+7j,(8,7,5), "truck" , 'e'}
#print(s1)


  # eg :2
'''
s2 = {5,6,98,[9,0]}
print(s2)  ----> error 
'''

# eg :3

#min(),max(), len()
# eg :4
# to add element inside set
'''
s1 = {8,78,67,'u'}
#add()
s1.add(43)
print(s1)
'''
#update()
#s1.update([9,0])
#print(s1)


 #To delete the element inside the set
'''
 s1 = {8,78,67,'u'}
 # pop() # to delete one element randomly
 s1.pop()
 print(s1)
'''


#remove()
#s1.remove(78)
#print(s1)


# discard()
#s1.discard(67)
#print(s1) 


# clear()
#l1 = {}
#print(type(l1))  ----> data type is dict


#s1 = set() # to create empty set
# print(type(s1))


'''
s1 = {8,9,0}
s1.clear()
print(s1)
'''
# del s1
#print(s1)



## joining the sets
#s1 = { 9,0,8}
#s2 = {5,6,8,"caed",'t',56}
# union()---> to Combine 2 sets
#s3 = S1.union(s2)
#print(s3)

'''

S1 = {4,5,6}
S2 = {5,6,7,8}
print(s1.intersection(s2))
'''

'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
'''


#isdidjoin(),issubset(),issuperset()


'''
s1 = {2,4,6,7,8}
s2 = {4,7,5,8,4,0,}

'''
'''
print(s1.issubset(s2))
print(s2.issuperset(s1))
'''

# problem : 1
'''
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,9,9}
'''

#for val in s1:
 #   if val in s2:
  #      str1 = "its joint set"
#print(str1)



# !-----> dictionary
  # eg :

'''
d1 = {1:100, 'a':200,4.5:"hello"}
print(d1)
print(len(d1))
'''
'''
  #---->char of dictionary.
'''  
#1) have to be surounded by {}
#2) it have to be in the form of key, value pair
#3)it is mutable
#4) duplicate keys are not allowed ,duplicates values are allowed
#5) it is unindexd
#6) it is ordered
#7)key does not allow mutable datatypes,values allow mutable datatype

#d1 = {1:100,2:200,3:300,4:400}

 #to acces the element in dictionary

'''
#print(d1)
#or
#To acces the values, have to use key 
#print(d1[1])# o/p --> 100


'''
# some common functions
# len(),min,max()
#print(max(d1))



# To find min, max based on values 
'''
print(min(d1.values()))
print(max(d1.values()))
'''

# dictoinary based function
# to add element (key and value pair)in dict
'''
d1 = {1:100,2:200,3:300,4:400}
d1[5}= 500
print(d1)
'''

# to replace a value in dictionary
'''
d1 = {1:100,2:200,3:300,4:400}
d1[2]="mango"
print(d1)
'''


# delete element from dictionary
'''
d1 = {1:100,2:200,3:300,4:400}
popitem()  # -----> to delete last key value pair in dict.
d1.popitem()
print(d1)    
'''




# pop()
#d1.pop(2) # 2is the key in dectionary
#print(d1)

#clear(),del


# join 2 dictionary
'''
d1 = {1:100,2:200,3:300,4:400}
d2 = {"a","apple,"b":"boy',"g":"game"}
d1.update(d2)
print(d1)
'''

#get()----> uesd to get the value from a key
'''
d1 = {1:100,2:200,3:300,4:400}
print(d1[90])
print(d1.get(90))
'''


# to print all the keys
'''
print(d1.keys())
prin(type(d1.keys()))
'''


# to print sll the values
# print(d1.values())




# *** Iterating dictionary
'''
d1 = {1:100,2:200,3:300,4:400}
for val in d1:
    print(val)

 for val in d1.values():# to iterate values alone
   print(val)

to get both key and values
for key,val in d1.item():
    print(key,val)

'''


# problem : 1

'''
n= int(input("enter num of times:")
integer=[]
float_value=[]
string=[]

for val in range(n):
    value =eval(input("enter the value:"))
    if type(value)==int:
       integer.append(value)
    elif type(value)==float:
        foat=value,append(value)
    elif type(value)== str:
        string.append(value)
    else:
        print("pls provide data in int,float,string")
print(integer)
print(float_value)
print(string)
'''

# problem : 2

#REturn a set of elements present in set A or B,but not both
#set1 = {10,20,30,40,50}
#set2 = {30,40,50,60,70}
#S#{20,70,10,60}
'''
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

set3 = set()
for val in set1:
    if val not in set2:
       set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)

'''

       

# --- > problem :3

#l1 = [1,2,3,4]
#l2 = ["a","b","c","d"]
'''
d1={}
d1[l1[0]]=l2[0]    ### it is the small example only one element dictionary .
print(d1)
'''
'''      or
d1 = {}
for val in range (len(l1)):
    d1[l1[val]]=l2[val]
print(d1)

'''  

















