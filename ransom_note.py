class Solution:

    def canConstruct(self, ransomNote, magazine):
        mag = {}
        for ch in magazine:
            if mag.get(ch, None) is None:
                mag[ch] = 1
            else:
                mag[ch] +=1
        for ch in ransomNote:
            ch_num = mag.get(ch, None)
            if ch_num is None or ch_num == 0:
                return False
            else:
                mag[ch] -= 1
        return True
