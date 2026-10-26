class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nums = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.nums:
            return -1

        self.nums.move_to_end(key)
        return self.nums[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.nums:
            self.nums.move_to_end(key)

        self.nums[key] = value

        if len(self.nums) > self.capacity:
            self.nums.popitem(last = False)
