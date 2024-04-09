class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_full(self):
        return len(self.queue) == self.size

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return "Empty"
        else:
            return self.queue.pop(0)

    def print(self):
        return self.queue[0]