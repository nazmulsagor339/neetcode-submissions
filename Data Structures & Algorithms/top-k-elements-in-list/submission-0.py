class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        frequency_list = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        for element, frequency in frequency_dict.items():
            frequency_list[frequency].append(element)
        result = []
        for i in range(len(frequency_list)-1,0,-1):
            for res in frequency_list[i]:
                result.append(res)
                if len(result) == k:
                    return result
        return result