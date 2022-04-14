class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
        
        

def searchBST(root, val):
    if root is None: 
            return 
        
    elif root.val == val: 
        return root

    elif root.val > val:
        return searchBST(root.left, val)

    elif root.val < val: 
        return searchBST(root.right, val)

    
        