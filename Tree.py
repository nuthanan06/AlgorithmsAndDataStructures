class TreeNode: 
    def __init__(self, data): 
        self.data = data
        self.child = []
        self.parent = None 
    
    def add_child(self, child): 

        child.parent = self
        self.child.append(child)

    def get_level(self): 
        level = 0 
        p = self.parent 
        while p: 
            level += 1
            p = p.parent
        
        return level

    def print_tree(self): 
        prefix = "  "
        print(prefix*self.get_level() + self.data)
        if len(self.child) > 0: 
            for child in self.child: 
                child.print_tree() 

def build_product_tree(): 
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("ThinkPad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("IPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    root.add_child(laptop)
    root.add_child(cellphone)
    return root

root = build_product_tree()
root.print_tree()