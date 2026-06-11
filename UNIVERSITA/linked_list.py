class Node:
    """
    Represents a single node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Return the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

def add(self, data):
    """
    add new node containing data at head of the list
    Takes o(1) time
    """
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node
