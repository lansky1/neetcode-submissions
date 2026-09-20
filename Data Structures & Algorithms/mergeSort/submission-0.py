# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.merge_sort(pairs, 0, len(pairs) - 1)
        return pairs

    def merge_sort(self, pairs, start, end):
        if (end - start + 1) <= 1:
            return

        mid = (end + start) // 2
        self.merge_sort(pairs, start, mid)
        self.merge_sort(pairs, mid + 1, end)

        self.merge(pairs, start, mid, end)

    def merge(self, pairs, start, mid, end):
        temp = []

        i = start
        j = mid + 1

        while i <= mid and j <= end:
            if pairs[i].key <= pairs[j].key:
                temp.append(pairs[i])
                i += 1
            else:
                temp.append(pairs[j])
                j += 1

        while i <= mid:
            temp.append(pairs[i])
            i += 1

        while j <= end:
            temp.append(pairs[j])
            j += 1

        for k in range(len(temp)):
            pairs[start + k] = temp[k]
