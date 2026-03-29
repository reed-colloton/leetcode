class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):

            # if strs[i].startswith(prefix):
            #     continue

            if len(prefix) > len(strs[i]):
                prefix = prefix[:len(strs[i])]
            
            new_prefix = ''
            for j, c in enumerate(prefix):
                if c == strs[i][j]:
                    new_prefix += c
                else:
                    prefix = new_prefix
                    
            if prefix == "":
                return prefix

        return prefix