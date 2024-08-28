class Node:
    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None

#function to perform preorder traversal
def preorderTraversal(root):

    #Base case
    if root is None:
        return
    
    #visit the current node
    print(root.data,end=" ")

    #recur on the left subtree
    preorderTraversal(root.left)

    #recur on the right subtree
    preorderTraversal(root.right)

if __name__ == "__main__":
    root =  Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    preorderTraversal(root)