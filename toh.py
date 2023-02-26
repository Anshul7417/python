# def toh(n,a,b,c):
#     if(n>0):
#         toh(n-1,a,c,b)
#         print("move from "+a+" to "+c)
#         toh(n-1,b,a,c)

# A="a"
# B="b"
# C="c"
# toh(3,A,B,C)



# x=0
# y=2
# z=3
# a=z or y
# print(a)


# def factors(n):
#     list=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             list.append(i)
#     return list

# print(factors(6))


# from ast import Try


# def aver(l):
#     try:
#         length=len(l)
#         summ=sum(l)
#         average=summ/length
#         return average
#     except:
#         x=0.0
#         return x

# list=[]
# print(aver(list))

# def mergelist(l1,l2):
#     length=len(l1)
#     list=[]
#     for i in range(length):
#         list.append((l1[i],l2[i]))
#     return list

# a=[]
# b=[]
# print(mergelist(a,b))


# def searchmany(s,x,k):
#     count=0
#     for element in s:
#         if element==x:
#             count=count+1
#     if count>k:
#         return False
#     elif count==0:
#         return True
#     else:
#         return True

# print(searchmany([10,12,12,12],12,2))


# def alternate(lst):
#     for count,item in enumerate(lst):
#         if count%2==0 and item%2!=0:
#             return False
#         elif  count%2!=0 and item%2==0:
#             return False
#     return True    


# print(alternate([15,10,9]))

# import math

# def countsquares(n):
#     count=0
#     for i in range(1,n+1):
#         x=int(math.sqrt(i))
#         if x*x==i:
#             count=count+1
#     return count


# print(countsquares(5))


# n=25
# prime=[]
# for i in range(n+1):
#     prime.append(i)
# prime[0]=0
# prime[1]=0
# p=2
# while p*p<=25:
#     if p!=0:
#         for i in range(p*2,n+1,p):
#             prime[i]=0
#         p+=1
# print()
# for i in range(len(prime)):
#     if(prime[i]!=0):
#         print(prime[i],end=" ")


# file = open("Employees.txt", "w")

# for i in range(3):
#     name = input("Enter the name of the employee: ")
#     file.write(name)
#     file.write("\n")
	
# file.close()

# print("Data is written into the file.")


# file1 = open("Employees.txt", "w")
# lst = []
# for i in range(3):
# 	name = input("Enter the name of the employee: ")
# 	lst.append(name + '\n')
	
# file1.writelines(lst)
# file1.close()
# print("Data is written into the file.")
















       