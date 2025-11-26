class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # brute force approach
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # check whether the first [i] and second [j] equals to target
                if nums[i] + nums[j] == target:
                    return [i , j]

                    # time complexity O(n^2)

        # hash map approach

        # # create an empty hash map
        # seen_values = {}
        
        # # loop through each number in array with its index
        # for current_index, current_number in enumerate(nums):

        #     # calculate what number we need to reach the target
        #     required_number = target - current_number

        #     # check if we've already seen the number, we need
        #     if required_number in seen_values:

        #         # return both indices
        #         required_index = seen_values[required_number]
        #         return [required_index, current_index]

        #     # haven't found the pair, yet
        #     # store this number and its index for future reference
        #     seen_values[current_number] = current_index 

