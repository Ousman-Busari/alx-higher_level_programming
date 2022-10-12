#!/usr/bin/python3
"""singly-linked list"""


class Node:
    """defines the node of a singly-linked list

    Attributes:
              data(int): integer data of the node
              next_node: the next node Object
    """
    def __init__(self, data, next_node=None):
        """Initiliazes an instance of the square

        Args:
             data(int): the ineteger data at the node object
             next_node: the next node object on the list

        Return:
               None
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """retrieves the data attribute of a Node object

            Return:
                   the data of the object Node
            """
            return(self.__data)

        @data.setter
        def data(self, value):
            """retrieves the data attribute of a Node object

            Args:
                 value(int): the new data of the node object

            Return:
                   None
            """
            if type(value) is int:
                self.__data = value
            else:
                raise TypeError("data must be an integer")

        @property
        def next_node(self):
            """retrieves the next_node attribute of a Node object

            Return:
                   the next node of the object Node
            """
            return(self.__next_node)

        @data.setter
        def next_node(self, value):
            """retrieves the next_node attribute of a Node object

            Args:
                 next_node(Node): the new data of the node object

            Return:
                   None
            """
            if type(value) is Node:
                self.__next_node = value
            else:
                raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """initialise an instance of a SinglyLinkedList

        Return:
                None
        """
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted
           position in the list (increasing order)

        Args:
             Value(int): the data value of the new node to insert

        Return:
               None
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            new_node.next_node = None
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """defines string operation of a singlyLinkedList"""

        string = []
        temp = self.__head
        while temp is not None:
            string.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(string))
