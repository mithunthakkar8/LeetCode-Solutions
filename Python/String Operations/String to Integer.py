class Solution:
    def myAtoi(self, s: str) -> int:
        # Handle Whitespace
        s=s.strip()

        # check boundary case where there is no string provided
        if s=='':
            return 0

        # Check positive or negative
        negative_flag = False
        if s[0]=='-':
            s = s[1:]
            negative_flag = True
        elif s[0]=='+':
            s = s[1:]
        
        #remove leading 0s
        i = 0
        while i<len(s):
            if s[i]=='0':
                pass
            else:
                s=s[i:]
                break
            i += 1
        
        # read only digits untill a non-digit is encountered
        i = 0
        result = ''
        while i<len(s):
            if s[i].isdigit():
                result += s[i]
            else:
                break
            i += 1
              
        # if number was initially negative, assign negative sign
        if negative_flag == True:
            result = '-' + result
        
        # convert result into integer wherever possible
        if result == '':
            result = 0
        else:
            try:
                result = int(result)
            except Exception as e:
                print("Error Code: ", e)
                result = 0
        
        # ensure the integer remains in the range of 32-bit signed integer
        if result > 2**31-1:
            result = 2**31-1
        elif result < -2**31:
            result = -2**31
        
        return result


        
        
