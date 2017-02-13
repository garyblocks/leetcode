class TwoSum(object):
    def __init__(self):
        self.nums = {}
        """
        Initialize your data structure here.
        """
    def add(self, number):
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
    def find(self, value):
        for i in self.nums:
            if value == 2*i and self.nums[i] > 1:
                return True
            elif value != 2*i and value-i in self.nums:
                return True
        return False
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)