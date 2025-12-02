

class Jar():
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if (self.size+n) > self.capacity:
            raise ValueError()
        self.size += n

    def withdraw(self, n):
        if (self.size-n) < 0:
            raise ValueError()
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if (not isinstance(capacity, int)):
            raise ValueError()
        if capacity < 0:
            raise ValueError()
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if (not isinstance(size, int)):
            raise ValueError()
        if size < 0 or size > self.capacity:
            raise ValueError()
        self._size = size

def main():

    j = Jar()
    j.deposit(10)
    print(j)
    print(f"Capacity is {j.capacity} and there are {j.size} cookies inside")

if __name__ == "__main__":
    main()

