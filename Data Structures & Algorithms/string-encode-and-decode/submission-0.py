class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            length_s = len(s)
            encoded_str += f"{length_s}#{s}"

        return encoded_str        

    def decode(self, s: str) -> List[str]:

        strs = []
        def delimit(strr: str | None) -> Tuple[str, str]:
            if strr is None:
                return
            split_result = strr.split("#", maxsplit=1)
            if len(split_result) == 1:
                return
            a, b = split_result
            strs.append(b[:int(a)])
            return b[int(a):]

        og_str = s
        while True:
            og_str = delimit(og_str)
            if not og_str:
                break
        return strs

