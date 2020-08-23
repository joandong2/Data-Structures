"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # new node
        new_node = ListNode(value, None)
        # if length == 0 return self.head an self.tail
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # if length > 1
        else:
            old_head = self.head
            old_head.prev = new_node
            self.head = new_node
            self.head.next = old_head
            self.head.prev = None
        self.length += 1
        return self.head.value

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length == 0:
            return None
        if self.length == 1:
            old_head = self.head
            self.head = None
            self.tail = None
        else:
            old_head = self.head
            self.head = old_head.next
        self.length -= 1
        return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_tail = ListNode(value, None)
        # If there is no tail (empty list)
        if self.length == 0:
            # Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail (general case):
        else:
            # Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
            # Set self.tail to the new node
            self.tail = new_tail
            self.tail.prev = old_tail
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # Remove Tail:
        # Check if it's there
        if self.length == 0:
            return None

        # List of 1 element:
        # Save the current_tail.value
        # Set self.tail to None
        # Set self.head to None
        if self.length == 1:
            old_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return old_tail.value

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

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # check for empty pointers
        if self.length == 0:
            return None
        if self.length == 1:
            return node
        else:
            next_node = node.next
            prev_node = node.prev
            if next_node == None:  # node is tail
                self.tail = prev_node
                prev_node.next = None
            else:  # node in between
                prev_node.next = next_node
                next_node.prev = prev_node

            current_head = self.head  # assign self.head as current head
            current_head.prev = node  # self.head prev would be our node
            node.next = current_head  # assign self.head prev node to the current tail
            node.prev = None
            self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # check for empty pointers
        if self.length == 0:
            return None
        if self.length == 1:
            return node
        else:
            next_node = node.next
            prev_node = node.prev
            if prev_node == None:  # node is head
                self.head = next_node
                next_node.prev = None
            else:  # node in between
                prev_node.next = next_node
                next_node.prev = prev_node

            current_tail = self.tail  # assign self.tail to current tail
            current_tail.next = node  # self.tail next would be our node
            node.prev = current_tail  # assign self.tail prev node to the current tail
            node.next = None
            self.tail = node
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # check for empty pointers
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return node

        # get previous node = node.prev
        # set prev_node.next to node.next
        # next_node = node.next
        else:
            next_node = node.next
            prev_node = node.prev
            if prev_node == None:
                self.head = next_node
                next_node.prev = None
            elif next_node == None:
                self.tail = prev_node
                prev_node.next = None
            else:
                # set node_next.previous = previous_node
                prev_node.next = next_node
                next_node.prev = prev_node
        # set node.prev = None && node.next = None
        node.prev = None
        node.next = None
        # decrement length & return node.value
        self.length -= 1
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # if length == 0 return None
        if self.length == 0:
            return None
        # if length == 1 return self.head/self.tail
        if self.length == 1:
            current_max = self.head
            return current_max.value
        # current max variable starts in self.head
        current_max = self.head.value
        current_node = self.head
        # iterate through list, stop when current_node == self.tail
        while current_node is not None:
            # compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
            # current_max = max(current_max, current_node.value)
        # return current_max
        return current_max
