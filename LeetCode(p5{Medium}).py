
class Solution(object):

    def longestPalindrome(self, s):
        if not s:
            return "invalid input"
        best_start = 0  # its start from 0 because the index always start from first
        best_length = 0 # length start from 1 because even single word is a palindrome

        def expanding(left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1

            return left+1, right - left- 1
        for i in range(len(s)):
            #odd
            odd_start, odd_length = expanding(i,i) #this mean we are looking aroung one box
            if odd_length > best_length:
                best_length = odd_length
                best_start = odd_start
            #even
            even_start, even_length = expanding(i,i+1) #this mean we are looking the box and the next box after it
            if even_length > best_length:
                best_length = even_length
                best_start = even_start
        return s[best_start:best_start+best_length]

if __name__ == "__main__":
    sol = Solution()
    s="babad"
    print(sol.longestPalindrome(s))