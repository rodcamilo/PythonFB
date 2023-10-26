import tkinter as tk
class TreeNode:
    def __init__(self,key,left=None,right=None):
        self.key=key
        self.left=left
        self.right=right
def display_tree(node,canvas,x,y,horizontal_spacing):
       if node:
           canvas.create_oval(x-20,y-20,x+20,y+20)
           canvas.create_text(x,y,text=str(node.key))
           if node.left:
               x_left=x-horizontal_spacing
               y_left=y+60
               canvas.create_line(x,y,x_left,y_left)
               display_tree(node.left,canvas,x_left,y_left,horizontal_spacing/2)
           if node.right:
               x_right=x+horizontal_spacing
               y_right=y+60
               canvas.create_line(x,y,x_right,y_right)
               display_tree(node.right,canvas,x_right,y_right,horizontal_spacing/2)
root=tk.Tk()
root.title("Visualização de Árvore Balanceada (AVL)")
canvas=tk.Canvas(root,width=400,height=400)
canvas.pack()

tree=TreeNode(1)
tree.left=TreeNode(2)
tree.right=TreeNode(3)
tree.left.left=TreeNode(4)
tree.left.right=TreeNode(5)
tree.right.left=TreeNode(6)
tree.right.right=TreeNode(7)
tree.right.left.left=TreeNode(8)
tree.right.left.right=TreeNode(9)
tree.right.right.left=TreeNode(10)
tree.right.right.right=TreeNode(11)
tree.left.left.left=TreeNode(12)
tree.left.left.right=TreeNode(13)
tree.left.right.left=TreeNode(14)
tree.left.right.right=TreeNode(15)

display_tree(tree,canvas,200,50,100)
root.mainloop()
