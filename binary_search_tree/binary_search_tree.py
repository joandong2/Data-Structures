"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode = None  # either BSTNode or None
        self.right: BSTNode = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare target value to node.value
        # If value > node.value:
        if value >= self.value:
            # Go right
            # If node.right is None:
            if self.right is None:
                # Create the new node there
                self.right = BSTNode(value)
            else:  # self.right is a BSTNode
                # Do the same thing (aka recurse)
                # Insert value into node.right
                # right_child is a BSTNode, so we can call insert on it
                right_child = self.right
                right_child.insert(value)
        # Else if value < node.value
        if value < self.value:
            # Go Left
            # If node.left is None:
            if self.left is None:
                # Create node
                self.left = BSTNode(value)
            else:
                # Do the same thing
                # (compare, go left or right)
                # Insert value into node.left
                left_child = self.left
                left_child.insert(value)

    def contains(self, target):
        # if target == node.value
        # return True
        if target == self.value:
            return True

        # If target > node.value:
        # Go right
        if target >= self.value:
            # If node.right is None:
            # We've traversed the tree and haven't found it
            # return False
            if self.right is None:
                return False
            # Else:
            # Do the same thing
            # return node.right.contains(target)
            else:
                return self.right.contains(target)

        # Else if target < node.value
        elif target < self.value:
            # Go Left
            # If node.left is None:
            if self.right is None:
                # return False
                return False
            # Else:
            else:
                # Do the same thing
                # (compare, go left or right)
                # return node.left.contains(target)
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            current_node = self  # top of the tree as current node
            while current_node.right is not None:
                current_node = current_node.right
            return current_node.value

    # set the fn to every  value, if self.left === for_each
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value
        # start at root, call the fn on it
        fn(self.value)

        # go left, call for_each on the left tree, children
        if self.left is not None:
            self.left.for_each(fn)
        # go right call for_each on the right tree, children
        if self.right is not None:
            self.right.for_each(fn)

    # Stack
    def for_each_iterative(self, fn):
        # start at root
        # cur_node = self
        # # push it on to the stack, use stack made in last module
        # stack = Stack()
        # stack.push(cur_node)

        # # while stack is not empty:
        # while len(stack) > 0:
        #     cur_node = stack.pop()
        #     # push right
        #     if cur_node.right is not None:
        #         stack.push(cur_node.right)
        #     # push left
        #     if cur_node.left is not None:
        #         stack.push(cur_node.left)
        #     # call the fn
        #     fn(cur_node.value)
        pass

    def breadth_first_traversal(self, fn):
        pass
        # start at teh root
        # push it on the queue

        # while queue is not empty
        # cur_node = remove from teh queue
        # add cur_node children to the queue
        # process queue

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # create a queue for nodes
        # add the first node from the queue
        # print the removed node
        # add all chidren in the queue
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
