from pythonds.basic.queue import Queue



class Node:
    def __init__(self, value, previous_node, next_node):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node


class QueueLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def queue(self,new_node):
        if self.head_node is None and self.tail_node is None:
            self.head_node = new_node;
            self.tail_node = new_node;
        else:
            old_tail = self.tail_node
            self.tail_node = new_node
            new_node.previous_node = old_tail
            old_tail.next_node = new_node

    def dequeue(self):
        temp =self.head
        self.head = temp.next_node
ll = QueueLinkedList()
