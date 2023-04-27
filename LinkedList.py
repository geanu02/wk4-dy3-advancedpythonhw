from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right

    def __repr__(self):
        return ' -> '.join(node.value for node in self)

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

    def insert_node_before(self, target, value):
        new_node = Node(value)
        if self.head:
            if self.head.value == target:
                old_self_head = self.head
                self.head = new_node
                new_node.right = old_self_head
                return
            for node in self:
                if node.value.right == target:
                    right_node = node.right
                    node.right = new_node
                    new_node.right = right_node
        else:
            print("Empty List")

    def remove_node(self, value):
        if value == self.head.value:
            self.head = self.head.right
        else:
            for node in self:
                if node.right:
                    if node.right.value == value:
                        node.right = node.right.right
                        return
                    
    def get_tail(self):
        node = self.head
        while node.right:
            node = node.right
        return node.value
    
    def remove_tail(self):
        node = self.head
        if node.right:
            while node.right.right:
                node = node.right
        node.right = None

# Exercise 1: Adding Elements to LinkedList

    def add_list_elements(self, alist):
        for elem in alist:
            self.add_node(elem)

linked_list = LinkedList()

linked_list.add_node('Sunday')

linked_list.add_list_elements(['Monday', 'Tuesday', 'Wednesday'])

print(linked_list)
print(linked_list.head.right.value)
print(linked_list.head.right.right.right.value)

# linked_list.add_node('Monday')
# linked_list.add_node('Wednesday')
# linked_list.add_node('Thursday')
# linked_list.add_node('Friday')
# linked_list.add_node('Saturday')

# print(linked_list.head.right.value)
# print(linked_list.head.right.right.value)
# print(linked_list.head.right.right.right.value)
# print(linked_list.head.right.right.right.right.value)

# linked_list.insert_node('Monday', 'Tuesday')

# print(linked_list)

# linked_list.insert_node_before('Monday', 'Pokemonday')

# print(linked_list)

# linked_list.remove_tail()

# print(linked_list)