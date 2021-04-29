class Node:
	def __init__(self,num):
		self.data = num
		self.left = None
		self.right = None
def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print(root.data,end=" ")
	inorder(root.right)

#Complete Wrong 
#def createTree():
# 	n=int(input('Enter root data'))
# 	root = Node(n)
# 	temp = root
# 	x = 'R'
# 	while x=='R' or x=='L':
# 		x=input('Enter L or R or anything')
# 		if x=='R' or x=='L':
# 			n=int(input('Enter number'))
# 			if x=='R':
# 				temp.right = Node(n)
# 				temp = temp.right
# 			else:
# 				temp.left = Node(n)
# 				temp = temp.left
# 	print('Tree created',root.data)
# 	return root


if __name__ == '__main__':
	#root = createTree()
	print(root.data)
	inorder(root)

