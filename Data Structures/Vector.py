class Vector:
    def __init__(self):
        array = [None] * 16 
        size = 0

    def size():
        return size

    def capacity():
        return len(array) 

    def is_empty():
        return size == 0

    def at(index):
        if index >= size:
            raise Exception("IndexOutofBounds")
        return array[index]

    def push(item):
        if size == len(array):
            resize(len(array)*2)
        array[size] = item
        size+=1

    def insert(index, item):
        if size == len(array):
            resize(len(array)*2)
        for i in range(size, index, -1):
            array[i] = array[i-1]
        array[index] = item
        size += 1

    def prepend(item):
        if size == len(array):
            resize(len(array)*2)
        for i in range(size, 0, -1):
            array[i-1] = array[i]
        array[0] = item
        size+=1

    def pop():
        delete(size-1)

    def delete(index):
        for i in range(index,size-1):
            array[i] = array[i+1]
        array[size] = None
        size-=1
        if size <= len(array)/4:
            resize(len(array)/2)
            
    def remove(item):
        for i in range(0, size):
            if array[i] == item:
                delete(i)

    def find(item):
        for i in range(0, size):
            if array[i] == item:
                return i
        return -1

    def __resize(new_capacity):
        tempArray = [None]*new_capacity
        for i in range(0, size):
            tempArray[i] = array[i]
        array = tempArray
    
