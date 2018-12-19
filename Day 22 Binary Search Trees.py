class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getWeight(self,root):
        #Write your code here
        count = 0
        value = 0
        if root == None:
            return count
        else:
            count+=1 + max(self.getWeight(root.left), self.getWeight(root.right))
            return count

    def getHeight(self,root):
        return self.getWeight(root)-1
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
