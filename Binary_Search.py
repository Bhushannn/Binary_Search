#python 3.7.1

def binary(lis,n,low,number):
    mid = (low+n)//2
    if lis[mid]==number:
      return number,mid
    if lis[mid]>number:
      return binary(lis,low,mid-1,number)
    if lis[mid]< number:
      return binary(lis,mid+1,n,number)
      
list =[]
num = int(input("Number of numbers u want to have in list : "))
for i in range(0,num):
  item = int(input())
  list.append(item)

list.sort()
#print(list)
n = len(list)
number = int(input("write the number u want to check in list: "))

try:
  print(binary(list,n,0,number))
  print("The number with its respective index is printed")
except IndexError:
  print("There is no such number in list")
  

