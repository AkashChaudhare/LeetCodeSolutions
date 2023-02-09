class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        cache=defaultdict(set)

        for idea in ideas:
            cache[idea[0]].add(idea[1:])
        print(cache)
        
        chars={c[0] for c in cache}
        print(chars)
        counter=0
        for i in chars:
            for j in chars:
                if i!=j:
                    left=cache[i].difference(cache[j])
                    right=cache[j].difference(cache[i])
                    counter+= len(left)*len(right)

        return counter
