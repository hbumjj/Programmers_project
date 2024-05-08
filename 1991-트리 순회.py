# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:34:02 2024

@author: user
"""

# 트리 구현

tree = {}
# tree['A'] = ['B', 'C']

# tree['B'] = ['D', '.']

# tree['C'] = ['E', 'F']

# tree['E'] = ['.', '.']

# tree['F'] = ['.', 'G']

# tree['D'] = ['.', '.']

# tree['G'] = ['.', '.']

# print(tree)

N = int(input())
for i in range(N):
    a,b,c = map(str, input().split())
    tree[a] = [b,c]


# 전위 순회
def first(root):
    if root != '.':
        print(root, end = "")
        first(tree[root][0])    
        first(tree[root][1])

def middle(root):
    if root != '.':
        middle(tree[root][0])
        print(root, end = "")
        middle(tree[root][1])



def end(root):
    if root != '.':
        end(tree[root][0])
        end(tree[root][1])
        print(root, end = "")


root = 'A'
first(root)
print()
root = 'A'
middle(root)
print()
root = 'A'
end(root)