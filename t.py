class pair_elements:
    def twosum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
value = int(input("Enter the sum for wich you want to find pairs: "))
print("index1=%d, index2=%d" % pair_elements().twosum((1, 2, 3, 4, 5), value))
