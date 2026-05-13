class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"]
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        return encode

    def decode(self, s: str) -> List[str]:
        #       5#Hello5#World
        decode = []
        i = 0
        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            string_len = int(s[i:j])
            decode.append(s[j+1 : j+1+string_len])

            i = string_len + 1 + j

        return decode

