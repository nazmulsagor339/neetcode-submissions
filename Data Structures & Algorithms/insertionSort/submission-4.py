# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        for i in range(len(pairs)):
            j = i
            # Move the element left until it is in the right spot
            while j > 0 and pairs[j-1].key > pairs[j].key:
                pairs[j], pairs[j-1] = pairs[j-1], pairs[j]
                j -= 1
            
            # Capture the state after the i-th insertion
            # Use list() or [:] to create a copy of the current state
            states.append(list(pairs))
        return states