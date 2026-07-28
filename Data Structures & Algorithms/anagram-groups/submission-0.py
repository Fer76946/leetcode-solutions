class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            groups = defaultdict(list)

            for n in strs:
                count = [0] * 26
                for m in n:
                    count[ord(m) - ord('a')] += 1
                groups[tuple(count)].append(n)
            return list(groups.values())        
