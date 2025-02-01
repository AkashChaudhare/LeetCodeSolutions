class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=""
        len1, len2 = len(word1), len(word2)
        index1, index2 = 0, 0

        while index1<len1 and index2<len2:
            word3 += word1[index1]
            word3 += word2[index2]

            index1, index2 = index1+1, index2+1


        if len2 < len1:
            return word3 + word1[index1:]
        
        return word3 + word2[index2:]
