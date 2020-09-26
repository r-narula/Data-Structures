class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class List:
    def __init__(self):
        self.head = None
    
    def reverse(self,head,k):
        current = self.head
        next = None
        prev = None
        count = 0
        print(current,current.data)
        while current is not None and count<k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None: 
            head.next = self.reverse(next, k) 
  
        # prev is new head of the input list 
        return prev 

    def push(self,new_data):
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    def printList(self): 
        print(self.head.data)
        temp = self.head 
        while(temp): 
            print (temp.data,end =" ") 
            temp = temp.next
        print()

llist = List() 
llist.push(9) 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
  
print ("Given linked list")
llist.printList() 
llist.head = llist.reverse(llist.head, 3) 

print ("\nReversed Linked list")
llist.printList() 