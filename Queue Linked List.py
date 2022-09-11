from Linked_List import Linked_List


class Queue:
    def __init__(self):
        self.list = Linked_List()

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        x = self.list.return_front()
        self.list.remove_first()
        return x

    def is_empty(self):
        return self.list.size == 0

    def front(self):
        return self.list.return_front()

    def __len__(self):
        return self.list.size


quetype = Queue()
quetype.enqueue(10)
quetype.enqueue(20)
quetype.enqueue(30)
quetype.enqueue(40)

quetype.dequeue()
quetype.front()
