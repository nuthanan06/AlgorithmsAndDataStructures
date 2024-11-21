class Node: 
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

class LinkedList: 
    def __init__(self): 
        self.head = None 
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
            
        itr = self.head 
        while itr.next: 
            itr = itr.next 
        
        itr.next = Node(data, None)

    def print(self): 
        if self.head is None: 
            print("Linked list is empty")
            return 
        
        itr = self.head 
        llstr = ' '

        while itr: 
            print(itr)
            llstr += str(itr.data) + " "
            itr = itr.next

        print(llstr)
    
    def insert_values(self, data_list): 
        for i in data_list: 
            self.insert_at_end(i)

        
    def get_length(self):
        counter = 0 

        itr = self.head
        while itr: 
            counter += 1
            itr = itr.next

        return counter
    
    def insert_after_value(self, data_after, data_to_insert): 
        
        itr = self.head
        while itr: 
            if itr.data == data_after: 
                node = Node(data_to_insert, itr.next)
                itr.next = node 
                return
            itr = itr.next 
        
        print("Invalid Value")
        return
    
    def remove_by_value(self, data): 
        itr = self.head
        counter = 0
        while itr and itr.next and counter < self.get_length(): 
            if (itr.next).data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
            counter += 1
        



        
        

        
ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()