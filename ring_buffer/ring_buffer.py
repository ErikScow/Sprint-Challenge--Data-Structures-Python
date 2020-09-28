class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            
            self.storage.insert(self.index, item)
            self.storage.pop(self.index + 1)
            if (self.index + 1) == self.capacity:
                self.index = 0
            else:
                self.index += 1
            

    def get(self):
        return self.storage