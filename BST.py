"""
Rohan is learning about trees and he want to test his knowledge on trees by constructing a BinarySearch Tree
from the list which contains the following:
a)the elements in the list are the pairs of numbers whose sum is equal to n in soreted order
b)the list do not contain duplicate numbers and negative numbers if exists then ignore

input format:
 first line contains list of numbers
 second line contains number n
output format:
 inorder traversal of BinarySearch Tree
example:
input:
3 4 5
9
output:
3
"""
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)

arr = list(map(int,input().split()))
n = int(input())
l = []
for i in range(len(arr)):
    if n - arr[i] in arr:
        if arr[i] not in l:
            l.append(arr[i])
        if n-arr[i] not in l:
            l.append(n-arr[i])
print(*l)
x=Node(l[0])
for i in range(1, len(l)):
    insert(x, Node(l[i]))
inorder(x)
