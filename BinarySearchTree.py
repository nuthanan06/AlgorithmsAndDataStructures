class BinarySearchTreeNode: 
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

    def add_child(self, data): 
        if data == self.data:
            return

        if data < self.data:
             if self.left: 
                 self.left.add_child(data)
             else: 
                 self.left = BinarySearchTreeNode(data)
        else: 
            if self.right: 
                 self.right.add_child(data)
            else: 
                 self.right = BinarySearchTreeNode(data)
    
    def inOrderTraversal(self): 
        elements = [] 
        
        if self.left: 
            elements += self.left.inOrderTraversal()
        
        elements.append(self.data)

        if self.right: 
            elements += self.right.inOrderTraversal()

        return elements
    
    def search(self, val):
        if self.data == val: 
            return True
        
        if val < self.data: 
            if self.left: 
                return self.left.search(val)
            else:
                return False
        
        if val > self.data: 
            if self.right: 
                return self.right.search(val)
            else: 
                return False 
    
    def find_max(self):
        if self.right is None: 
            return self.data
        return self.right.find_max() 
    
    def find_min(self): 
        if self.left is None: 
            return self.data
        return self.left.find_min()
        
    def remove(self, val): 
        if val < self.data:
            if self.left: 
                self.left = self.left.remove(val) 
        elif val > self.data:
            if self.right: 
                self.right = self.right.remove(val)
        else: 
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.remove(min_val)
        return self

            

        
            
def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
number_tree = buildTree(numbers)

print(number_tree.inOrderTraversal())
print(number_tree.remove(34))
print(number_tree.inOrderTraversal())
