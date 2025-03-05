class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBegin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def find(self, index):
        if index < 0 or index is None:
            raise IndexError("Index out of range!")
        current_node = self.head
        i = 0
        while current_node is not None:
            if i == index:
                return current_node
            i = i + 1
            current_node = current_node.next
        return None

    def insertAtIndex(self, data, index):
        if index < 0 or index is None:
            raise IndexError("Index out of range!")
        if index == 0:
            self.insertAtBegin(data)
            return
        if self.sizeOfDLL() == index:
            self.insertAtEnd(data)
            return
        if self.find(index):
            current_node = self.find(index)
        else:
            return
        new_node = Node(data)
        new_node.prev = current_node.prev
        new_node.prev.next = new_node
        new_node.next = current_node
        current_node.prev = new_node

        # Method to add a node at the end of LL

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def updateNode(self, val, index):
        current_node = self.find(index)

        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")

    def remove_first_node(self):

        if self.head is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

        # Method to remove last node of linked list

    def remove_last_node(self):
        if self.head is None:
            return

        # If there's only one node
        if self.head.next is None:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def remove_at_index(self, index):
        if index == 0:
            self.remove_first_node()
        elif index == self.sizeOfDLL():
            self.remove_last_node()
        else:
            node_to_remove = self.find(index)
            self.drop_node(node_to_remove)

    def drop_node(self, node_to_remove):
        if node_to_remove is not None:
            if node_to_remove.prev is not None:
                node_to_remove.prev.next = node_to_remove.next
            if node_to_remove.next is not None:
                node_to_remove.next.prev = node_to_remove.prev
        else:
            print("Index not present")

    def remove_node(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.remove_first_node()
            return
        if self.tail.data == data:
            self.remove_last_node()
            return
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                self.drop_node(current_node)
                return
            current_node = current_node.next

        print("Node with the given data not found")

    def sizeOfDLL(self):
        size = 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    # Print the linked list
    def printDLL(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def revPrintDLL(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev


# create a new linked list
dllist = DoublyLinkedList()

# add nodes to the linked list
dllist.insertAtEnd('a')
dllist.insertAtEnd('b')
dllist.insertAtBegin('c')
dllist.insertAtEnd('d')
dllist.insertAtIndex('g', 2)

# print the doubly linked list
print("Node Data:")
dllist.printDLL()

# print the doubly linked list in reverse
print("Reverse Node Data:")
dllist.revPrintDLL()

print("\nSize of linked list:", dllist.sizeOfDLL())

# remove nodes from the linked list
print("\nRemove First Node:")
dllist.remove_first_node()
dllist.printDLL()

print("\nRemove Last Node:")
dllist.remove_last_node()
dllist.printDLL()

print("\nRemove Node at Index 2:")
dllist.remove_at_index(2)
dllist.printDLL()

print("\nUpdate node Value at Index 0:")
dllist.updateNode('z', 0)
dllist.printDLL()

print("\nSize of linked list:", dllist.sizeOfDLL())

print("\nRemove Node with data 'g':")
dllist.remove_node('g')
dllist.printDLL()

#
