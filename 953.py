class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ddd={c: i for i, c in enumerate(order)}

        for a,b in zip(words,words[1:]):
            if len(a)>len(b) and a[:len(b)]==b:
                return False
            for c1,c2 in zip(a,b):
                if ddd[c1]<ddd[c2]:
                    break
                elif ddd[c1]>ddd[c2]:
                    return False
        return True


