class Solution:

    def maximum69Number (self, num):
        str_num = str(num)
        return int(str_num.replace('6', '9', 1))
