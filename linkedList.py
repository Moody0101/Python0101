"""
-----------------------------------------------------------------------------------------------------------------
=> author: Moody0101
=> date: 16 October 2021
=> description:
    - a linked list that supports getting items by index, length property
    and also you can dump all the data into a json database
    --> the linked list implements alot of methods:
    * dunder methods => [__str__, __repre__,__len__, __iter__, __list__, __getitem__]
    plus, others that are provided with dataclasses lib.
    * other methods:
    => pushLeft
    => pushRight
    => insert
    => remove
    => find
    => store: stores everything in a json database, but you can you a csv file tho.
Note: the prop property in the node class represents a property but you can costumize it whatever you want.
for instance another constructor for a database that stroes usernames and passwrds would be:

    self.data => self.userName
    self.prop  => self.password
I wish you understand.
-----------------------------------------------------------------------------------------------------------------
"""

from dataclasses import dataclass
from json import dumps
class invalidIndex(Exception):
    pass

@dataclass
class node:
    def __init__(self, data, Next=None,prop="Property"):
        self.data = data
        self.Next = Next
        self.prop = prop
        
    def __str__(self):
        return f"({self.data})"
    def __dict__(self):
        return {
        "data": self.data,
        "prop": self.prop,
        "next": self.Next.data
        }


@dataclass
class linkedlist:
    root = None
    size = 0
    
    def __iter__(self):
        current = self.root
        while current:
            yield current
            current = current.Next
    def __str__(self):
        self.nodes = [str(i) for i in self.__iter__()]
        return "=>".join(self.nodes)
    def __len__(self):
        return self.size
    def __list__(self):
        return self.nodes 
    def __getitem__(self, index):
        self.__str__()
        return self.nodes[index]

    def addLeft(self, data):
        if isinstance(data, str) or isinstance(data, int):
            new = node(data, self.root)
            self.root = new
        elif isinstance(data, node):
            new = data
            self.root = new
        elif isinstance(data, list):
            for _ in data:
                self.addLeft(_)
        self.size += 1
    def addRight(self, data):
        self.insert(data, self.size)
    def find(self, data):
        prev = None
        current = self.root
        while current:
            if current.data == data:
                return current, prev
            else:
                prev = current
                current = current.Next
                index += 1
        return None, None

    def remove(self, data):
        removing, prevremoving = self.find(data)[0], self.find(data)[1] 
        if not removing and not prevremoving: print("The data was not found to be removed")
        else:
            if prevremoving is not None:
                prevremoving.Next = removing.Next
            else:
                self.root = removing.Next
            self.size -= 1
            return True
        return False
    def insert(self, data,index):
        if index == 0:
            self.addLeft(data)
        if index < 0:
            raise invalidIndex("Invalid index less than 0!")
        if index > self.size:
            print(f"index {index} is out of range")
        elif not isinstance(index, int):
            raise invalidIndex(f"index = {index}a str or list can not be an index!! ")
        else:
            current = self.root
            position = index
            while position >= 1:
                prev = current
                current = current.Next
                position -= 1
            if not isinstance(data, node):
                new = node(data)
            else:
                new = data
            prev.Next = new
            new.Next = current
            self.size += 1
    def store(self, file: str = "Data.json"):
        current = self.root
        if current == None:
            return False
        table = {}
        while current:
            table[current.data] = current.prop
            current = current.Next
        open(file, "w").write(dumps(table, indent=4))
        print("data dumped")
        return True

def main():
    l = linkedlist()
    # adding values to the left
    l.addLeft(1)
    l.addLeft(2)
    l.addLeft(3)
    l.addLeft(4)
    # inserting values in index
    l.insert("EXX", 3)  
    # adding values to the end of the list using addRight
    l.addRight(3)
    # note: The linked list is dynamic, you can add nodes or values whatever you want.
    print(l)
    l.store()

if __name__ == '__main__':
    main()

