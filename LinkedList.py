from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        else:
            current_node = self.head
            while current_node.right:
                current_node = current_node.right
            current_node.right = node

    def insert_node(self, target, value):
        new_node = Node(value)
        if self.head:
            for node in self:
                if node.value == target:
                    right_node = node.right
                    node.right = new_node
                    new_node.right = right_node
        else:
            print("Empty List")

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right

    def __repr__(self):
        return ' -> '.join(node.value for node in self)

        
linked_list = LinkedList()

linked_list.add_node('Sunday')
linked_list.add_node('Monday')
linked_list.add_node('Wednesday')
linked_list.add_node('Thursday')
linked_list.add_node('Friday')
linked_list.add_node('Saturday')

print(linked_list.head.right.value)
print(linked_list.head.right.right.value)
print(linked_list.head.right.right.right.value)
print(linked_list.head.right.right.right.right.value)

linked_list.insert_node('Monday', 'Tuesday')

print(linked_list)