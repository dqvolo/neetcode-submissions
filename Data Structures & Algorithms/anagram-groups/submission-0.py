class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}

        for ch in strs:
            key="".join(sorted(ch))
            if key not in groups:
                groups[key]=[]
            groups[key].append(ch)
        return list(groups.values())