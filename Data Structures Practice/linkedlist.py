class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=node()

    def length(self):
        length = 0
        current = self.head
        while current.next != None:
            length += 1
            current = current.next
        return length

    def append(self,data):
        new_node = node(data)

        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_node

    def print(self):
        print("Start of the list")
        current = self.head

        while current.next != None:
            current = current.next
            print(current.data)
        
        print("End of the list")

    def delete(self, index):
        
        if index >= self.length():
            return "Index out of bound"
        current_index = 0
        current_node = self.head
        while True:
            previous_node = current_node
            current_node = current_node.next
            if current_index == index:
                previous_node.next = current_node.next
                return
            current_index += 1
            


l = linkedlist()

l.append("10")
l.append(5)
l.append(7)

l.print()

l.delete(1)

l.print()
