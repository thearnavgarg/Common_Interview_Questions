def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        import heapq
        
        if not nums:
            return 0
        
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        
        count = [(-value, key) for key, value in count.items()]
        heapq.heapify(count)
        output = []
        while k > 0:
            value = heapq.heappop(count)[1]
            print(value)
            output.append(value)
            k -= 1
        return output
