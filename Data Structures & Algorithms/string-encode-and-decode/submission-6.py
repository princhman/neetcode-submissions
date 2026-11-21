class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            if s == "":
                encoded += "0,"
            else:
                for c in s:
                    encoded += f"{ord(c)},"
            encoded += "-1,"
        return encoded

        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        splitted = s.split(",")[:-1]
        current = ""
        for s in splitted:
            if s == "0":
                pass
            elif s == "-1":
                result.append(current)
                current = ""
            else:
                current += chr(int(s))
        return result
