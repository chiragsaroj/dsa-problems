class Solution:
    """
    TC - O(n)
    SC - O(n)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()

        for s in strs:
            char_count = [0]*26

            for c in s:
                char_count[ord(c) - ord('a')] += 1

            key = tuple(char_count)

            if key not in map:
                map[key] = []
            
            map[key].append(s)

        return list(map.values())