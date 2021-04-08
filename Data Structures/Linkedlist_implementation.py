class Node:
    def __init__(self,data):
        self.__data = data
        self.__link = None
    def __init__(self, data, link):
        self.__data = data
        self.__link = link

    def get_link(self):
        return self.__link
    def get_data(self):
        return self.__data
    def set_data(self,data):
        self.__data = data
    def set_link(self,link):
        self.__link = link

class Linkedlist:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def size(self):
        return self.__size

    def empty(self):
        return self.__size == 0

    def value_at(self,index):
        if index >= self.__size:
            raise Exception("Index_out_of_bounds")

        temp = self.__head
        for i in range(0, index):
            temp = temp.get_link()
        return temp.get_data()

    def push_front(self,value):
        temp = Node(value, self.__head)
        self.__head = temp
        size+=1

    def pop_front(self):
        temp = self.__head.get_data()
        self.__head = self.__head.get_link()
        size-=1
        return temp.get_data()

    def push_back(self,value):
        temp = __head
        while temp.get_link() != None:
            temp = temp.get_link()
        temp.set_link(Node(value))
        size+=1
``  
    def pop_back(self):
        temp = self.__head
        while temp.get_link().get_link() != None:
            temp = temp.get_link()
        temp_value = temp.get_link().get_data()
        temp.set_link(None)
        size-=1
        return temp_value
    
    def front(self):
        return self.__head.get_data()
    
    def back(self):
        temp = self.__head
        while temp.get_link() != None:
            temp = temp.get_link()
        return temp.get_data

    def insert(self, index, value):
        if index >= self.__size:
            raise Exception("Index_out_of_bounds")
        if index == 0:
            self.push_front(value)
        else:
            temp = self.__head
            for i in range(0, index-1):
                temp = temp.get_link()
            temp_node = Node(value , temp.get_link())
            temp.set_link(temp_node)
            size+=1
    
    def erase(self, index):
        if index >= self.__size:
            raise Exception("Index_out_of_bounds")
        if index == 0:
            self.pop_back()
        else:
            for i in range(0, index-1):
                temp = temp.get_link()
            temp.set_link(temp.get_link().get_link())
            size-=1
    
    def value_n_from_end(self, n):
        if n >= self.__size:
            raise Exception("Index_out_of_bounds")
        index = size-n
        return self.value_at(index)

    def reverse(self):
        temp = self.__head
        self.__head = None
        while temp != None:
            self.push_front(temp.get_data())
            temp = temp.get_link()

    def remove_value(self, value):
        temp = self.__head
        index = None
        for i in range(0 , size):
            if temp.get_data() == value:
                index = i
                break
            temp = temp.get_link()
        if index == None:
            return
        else:
            self.erase(index)
