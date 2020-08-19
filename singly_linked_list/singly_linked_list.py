class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # The next node in the list


class LinkedList:
    def __init__(self):
        self.head: Node = None  # points to the first node in the list
        self.tail: Node = None  # Points to the last node in the list
        self.length = 0

    def __str__(self):
        pass

    def add_to_tail(self, value):
        # If there is no tail (empty list)
        if self.tail is None:
            # Create a new node
            new_tail = Node(value, None)
            # Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail (general case):
        else:
            # Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
            # Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
            # Set self.tail to the new node
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        # If not head (empty list)
        if self.head is None:  # if self.head is None
            return None
        # List with one element:
        if self.head == self.tail:
            # Set self.head to current_head.next / None
            current_head = self.head
            self.head = None
            # Set self.tail to None
            self.tail = None
            # Decrement length by 1
            self.length = self.length - 1
            return current_head.value
        # If head (General case):
        else:
            # 	Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            #  Return current_head.value
            self.length = self.length - 1
            return current_head.value

    def remove_tail(self):
        # Check if it's theres a list
        if self.tail is not None:
            # Start at head and iterate to the next-to-last node
            current_head = self.head
            current_tail = self.tail
            temp_node = None  # for looping current_head
            # Stop when current_node.next == self.tail
            while current_head != current_tail:
                temp_node = current_head
                current_head = current_head.next

            # Set self.tail to current_node
            self.tail = temp_node

            # Set current_node.next to None
            if temp_node is not None:
                temp_node.next = None

            if self.head == current_tail:
                self.head = None

            return current_tail.value
