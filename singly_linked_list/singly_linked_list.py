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
            self.length -= 1
            return current_head.value
        # If head (General case):
        else:
            # 	Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            #  Return current_head.value
            self.length -= 1
            return current_head.value

    def remove_tail(self):
        # Remove Tail:
        # Check if it's there
        if self.tail is None:
            return None

        # List of 1 element:
        # Save the current_tail.value
        # Set self.tail to None
        # Set self.head to None
        elif self.head == self.tail:
            current_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return current_tail.value

        else:
            # General case:
            # Start at head and iterate to the next-to-last node
            # Stop when current_node.next == self.tail
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            # Save the current_tail value,
            current_tail = current_node.next
            # Set self.tail to current_node
            self.tail = current_node
            # Set current_node.next to None
            current_node.next = None
            self.length -= 1
            return current_tail.value  # assertEqual to tail value

    def add_to_head(self, value):
        pass
        # check if theres a head
        # if no head/empty list:
        if self.head is None:
            # create new node
            # set with next to None
            new_node = Node(value, None)
            self.head = new_node
            # set self.tail = new NOde
            self.tail = new_node
            self.length += 1
        # if theres a head
        else:
            # create a new node
            # set new node.next to current_head/self.head
            new_node = Node(value, self.head)
            # set self.head = new_node
            self.head = new_node
            # length
            self.length += 1

    def remove_at_index(self, index):
        # remove at index i:
        # check length > i, if not return None
        if index >= self.length:
            return None
        if self.length == 1 and index == 0:
            target = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return target.value
        #     self.remove_tail()
        # iterate through the loop i times
        prev_node = self.head
        for i in range(index - 1):
            # this will get us to prev_node points to the node before the target node
            prev_node = prev_node.next

        target = prev_node.next
        prev_node.next = target.next
        target.next = None

        self.length -= 1

        return target.value
