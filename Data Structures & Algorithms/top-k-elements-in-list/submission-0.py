class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num]=1
            else:
                freqs[num]+=1
        sorted_freqs=dict(sorted(freqs.items(),key=lambda item:item[1],reverse= True))
        liste = list(sorted_freqs.keys())[:k]
        return liste
            
