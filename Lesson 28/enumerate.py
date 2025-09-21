class twoPair():
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target - num], i)
            lookup[num] = i

value = int(input("What sum are you using for this search? "))
print("index 1 = %d     index 2 = %d" %twoPair().twoSum((10, 20, 30, 40, 50, 60, 70), value))