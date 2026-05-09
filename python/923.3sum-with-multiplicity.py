class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        1. Count frequencies of numbers and et uniq sorted numbers
        2. Iterate all keys, calculating T = target - key and perform "Two Sum" algorithm for every T
        3. Two sum algo (two pointers):
            * two pointers - left and right (j, k)
            * case: sum of two pointers less than T: move left pointer
            * case: sum of two pointers greater than T: move right pointer
            * case: else: calculate result and append to answer: move both pointers
        
        result calculation:
        
        case i < j < k: multiply their frequesncies
        case i == j < k: multiply frequency of i, frequnecy of i minus 1 and divide by 2 and frequency of k
        case i == j == k: multiply frequency of i, frequnecy of i minus 1, frequnecy of i minus 2 and divide all by 6
        
        Time: O(n * 2)
        Space: O(n)
        
        """
        MOD = 10**9 + 7
        freq = collections.Counter(arr)
        keys = sorted(freq)
        
        # i, j, k - indexes
        # x, y, z - numbers
        # freq[x], freq[y], freq[z] - frequencies
        # ans - final answer
        
        ans = 0
        
        for i, x in enumerate(keys):
            T = target - x
            
            j, k = i, len(keys) - 1
            
            while j <= k:
                y, z = keys[j], keys[k]            
                
                if y + z < T:
                    # move left pointer
                    j += 1
                elif y + z > T:
                    # move right pointer
                    k -= 1
                else:
                    # calculate result
                    if i < j < k:
                        ans += freq[x] * freq[y] * freq[z]
                    elif i == j < k:
                        ans += freq[x] * (freq[x] - 1) // 2 * freq[z]
                    elif i < j == k:
                        ans += freq[x] * freq[y] * (freq[y] - 1) // 2
                    else: # i == j == k
                        ans += freq[x] * (freq[x] - 1) * (freq[x] - 2) // 6
                    
                    j += 1
                    k -= 1
                    
        return ans % MOD