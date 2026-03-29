class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        header = ''
        body = ''
        counter = 0
        for s in strs:
            counter += len(s)
            header += str(counter) + ','
            body += s
        return header + '|' + body
    
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        header, body = s.split(',|', maxsplit=1)
        lst = []
        i = 0
        indicies = header.split(',')
        for j in indicies:
            j = int(j)
            lst += [body[i: j]]
            i = j
        return lst
