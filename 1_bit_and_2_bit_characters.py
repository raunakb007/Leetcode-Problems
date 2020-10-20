class Solution:

    def isOneBitCharacter(self, bits):
        if len(bits) == 1:
            return True
        else:
            count = 0
            bits.reverse()
            for i in bits:
                if bits[i] == 0:
                    while bits[i] != 0:
                        count += 1
                        i += 1
                    return count % 2 == 0