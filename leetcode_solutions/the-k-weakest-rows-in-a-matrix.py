class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        # order by number of soldiers
        # handle tiebreakers
        # order the keys by the values
        # filter to top k
        # Beats 98.25% for memory and 94.8% for runtime
        # Using enumerate has better space and time complexity than using range(len(mat))
        # Using range(len(mat)) is 88.2, 47.64
        """
        hashmap = {}
        for i, list_ in enumerate(mat):
            hashmap[i] = len([j for j in list_ if j])
        return sorted(hashmap, key=hashmap.get)

sol = Solution()
sol.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3)