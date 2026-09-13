class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quick_sort_helper(pairs, 0, len(pairs) - 1)
        return pairs

    def _quick_sort_helper(self, pairs, start, end):
        if start >= end:
            return

        swap_index = start
        for i in range(start, end):
            if pairs[i].key < pairs[end].key:
                pairs[swap_index], pairs[i] = pairs[i], pairs[swap_index]
                swap_index += 1

        pairs[swap_index], pairs[end] = pairs[end], pairs[swap_index]

        self._quick_sort_helper(pairs, start, swap_index - 1)
        self._quick_sort_helper(pairs, swap_index + 1, end)
