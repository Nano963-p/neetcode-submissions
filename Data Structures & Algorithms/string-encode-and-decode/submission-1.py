class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for t in strs:
            r = f"{len(t)}#{t}"
            s+= r
        return s

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while(i<len(s)):
            j = s.find("#",i)
            l = int(s[i:j])
            r = s[j+1:j+l+1]
            res.append(r)
            i=j+l+1
        return res
                
       