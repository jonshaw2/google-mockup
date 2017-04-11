from pythonds.basic.queue import Queue



class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False
    def enqueue(self, item):
        self.item.append(item)

    def dequeue(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)

x = Queue()
print x.isEmpty()
x.enqueue(5)
print x.item
x.dequeue()
print x.item
print x.size()
