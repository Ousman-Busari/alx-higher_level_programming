#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list = MyList([5, 7, None, "type"])
print(my_list)
my_list.print_sorted()
print(my_list)
