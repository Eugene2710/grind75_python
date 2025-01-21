class Solution:
    def myAtoi(s: str) -> int:
        """
        approach:

        """
        INT_MAX = -2**31
        INT_MAX = 2**31 -1

        n: int = len(s)
        i = 0
        #step 1: skip leading whitespaces
        while i < n and s[i] == ' ':
            i+=1
        
        #step 2: determine if positive and negative signs are present - if nagative sign exists, sign=-1 else sign=1
        sign: int = 1
        if  i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # step 3: convert digits until non-digit or end
        res: int = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # check for overflow/underflow before updating res
            # // : floor division
            if res > (INT_MAX // 10) or (res == INT_MAX//10 and digit > INT_MAX%10):
                return INT_MAX if sign==1 else INT_MIN

            res = res*10+digit
            i+=1

    return sign*result

        

