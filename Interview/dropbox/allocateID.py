class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.maxNumbers = maxNumbers
        self.next = [(i+1) % maxNumbers for i in range(maxNumbers)]
        self.pos = 0 # the current available phone number
        
    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.next[self.pos] == -1: return -1
        
        res = self.pos
        self.pos = self.next[res]
        self.next[res] = -1
        return res
    

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return self.next[number] != -1
        

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if self.next[number] != -1: return
        
        self.next[number] = self.pos
        self.pos = number


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)