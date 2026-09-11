class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for  i,j in freq.items():
            bucket[j].append(i)

        result = []


        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                result.append(j)

                if len(result) == k:
                    return result

        
        
                
            
        