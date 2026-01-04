class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def sum_if4_divs(num):
            divs = set()
            for i in range(1, int(num**(1/2))+1):
                if num%i == 0:
                    divs.add(i)
                    divs.add(num/i)
            # print(num, divs)
            if len(divs)==4:
                return sum(divs)
            return 0

        result = [sum_if4_divs(num) for num in nums]
        return int(sum(result))
