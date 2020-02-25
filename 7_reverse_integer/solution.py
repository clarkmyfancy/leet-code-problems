class Solution:

    def __init__(self):
        pass

    def reverse(self, x):
        isNegative = True if x < 0 else False 
        x = abs(x)
        if (x > pow(2, 31)):
            return 0
        
        x_str = str(x)
        x_str = x_str[::-1]
        if isNegative:
            x_str = "-" + x_str
        return int(x_str)

