#!/usr/bin/python3
""" A singly-linked list"""


class Node:

    def __init__(self, data, next_node=None):
        """ Initiliazes an instance of the square

        Args:
             data(int): data of the new instance of the clas
             next_node(Node): the next node on the singly linked list

        Return:
               None
        """

        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        """ Retrieves the value of data

        Return:
               None
        """

        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the value of the data attributes

        Args:
             value(int): new data of the Node Object

        Return:
               None
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrieves the value of next_noded

        Return:
               None
        """

        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Sets the value of the data attributes

        Args:
             value(Node): new data of the Node Object

        Return:
               None
        """

        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


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
