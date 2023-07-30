class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Function for appending a node to the end
    def add_the_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length = self.length + 1
        return True

    # Function that pops the last node from the list

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length = self.length - 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    # Add nodes at the beginning of the list

    def add_at_the_begining(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length = self.length + 1
        return True

    # Pop the  first node from the list
    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

    # Get a node
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    # Set a value
    def set_value(self, index, value):
        temp = self.get(index)

        if temp is not None:
            temp.value = value
            return True
        return False

    # Insert value at a specific node
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.add_at_the_begining(value)
        if index == self.length:
            return self.add_the_end(value)

        new_node = Node(value)

        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # Remove node from the list at a particular index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    # Reverse a link
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.add_the_end(1)
my_linked_list.add_the_end(24)
my_linked_list.add_at_the_begining(7)
my_linked_list.reverse()
my_linked_list.print_list()
