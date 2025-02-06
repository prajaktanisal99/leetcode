class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        unique1 = {}
        unique2 = {}
        swaps = 0
        i = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                swaps += 1
                unique1[s1[i]] = unique1.get(s1[i], 0) + 1
                unique2[s2[i]] = unique2.get(s2[i], 0) + 1
            i += 1

        print(f'{swaps} : {unique1} : {unique2}')
        if swaps == 0:
            return True
        return (swaps == 2) and unique1 == unique2