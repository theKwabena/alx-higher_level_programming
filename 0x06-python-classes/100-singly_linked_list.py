#!/usr/bin/python3
"""module fongly linked list"""


class Node:
    """"define node"""

    def __init__(self, data, next_node=None):
        """initializes with instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets databute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """sets dataibute"""

        if not isinstance(value, int):
            raise TypeError('data mue an integer')
        self.__data = value

    @property
    def next_node(self):
        """get neattribute
        Returns: next node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """set value ot node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """defines a siinked list"""

    def __init__(self):
        """Initializes ty linked list"""

        self.head = None

    def __str__(self):
        """make listtable"""

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insertted fashion
        Args:
            value: whatill be on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
