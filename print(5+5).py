# class Fibonacci :
#     def fib(self,n) :
#         if n <= 0 :
#             return 0
#         if n ==1 :
#             return 1
#         else :
#             return self.fib(n-1) + self.fib(n-2)
        
#     def fibtill(self,num) :
#         result = []
#         for i in range(num) :
#             result.append(self.fib(i))
#         return result
        
#     pass

# f = Fibonacci()
# x = int(input("Enter till which number : "))
# print(f.fibtill(x))

# class Node :
    # def __init__(self,data):
#         self.data = data
#         self.right = None
#         self.left = None

#     def BinarySearchtreeNode(root,key) :
#         if root == None :
#             return False
#bubble sort     
# a = [4,5,7,1,2]
# n = len(a)
# for i in range(n - 1) :
#     for j in range(n - i - 1) :
#         if a[j] > a[j+1] :
#             #swap
#             a[j],a[j+1] = a[j+1],a[j]
            
            
# print(a)

#insertion sort

#swap with minimum element
def selection(a) :
    for i in range(len(a)-1) :
        min = i
        for j in range(i+1,len(a)) :
            if a[j] < a[min] :
                min = j
        if min != i :
            a[i],a[min] = a[min],a[i]

    return a

a = [50,60,40,10,20,100]
print(selection(a))

        















    
       
