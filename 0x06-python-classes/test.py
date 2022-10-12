#!/usr/bin/python3
''' A singly linked list module '''


class Node:
    ''' A class that defines a node of a singly linked list '''

    def __init__(self, data, next_node=None):
        ''' Initialization function '''

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' Gets the value of data '''

        return self.__data

    @data.setter
    def data(self, value):
        ''' Sets the value of data '''

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
