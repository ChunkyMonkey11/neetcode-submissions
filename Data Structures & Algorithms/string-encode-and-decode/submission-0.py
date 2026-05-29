class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "" 
        for string in strs:
            encoded += str(len(string))
            encoded += "|"
            encoded += string
        return encoded
    
    def decode(self, s: str) -> List[str]:
        """ 
        How do we decode a string like:
        5|Hello5|World
        bar = 1
        sp = 0
        lens = 5
        we read 2:7
        
        now bar = 

        
        """ 
        decoded = []
        sp = 0 #Starting point variable for where we are starting our search for the bar

        def get_bar(s: str, sp: int) -> int:
            idx = s.find("|",sp)
            return idx

        bar = get_bar(s,sp)

        while bar != -1:
            lenS = int(s[sp:bar])
            decoded.append(s[(bar+1):lenS+bar+1])
            sp = bar + 1 + lenS
            bar = get_bar(s,sp)

        return decoded
            

