//Intuition
//I just started my leetcode journey so I used beginner friendly methon to solve this question which is using sliding window approach.

//Complexity
//Time complexity: 22ms

//which is not the best but I have a clear understanding of the topic.

//Space complexity: 12.07 MB

//Code
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> seen;
        int left =0;
        int maxLength =0;

        for(int right =0; right <s.length(); right++){

            while(seen.count(s[right])){
                seen.erase(s[left]);
                left = left +1;

            }

            seen.insert(s[right]);
            int winLength = right - left +1;

            if(winLength > maxLength){
                maxLength = winLength;
            }

        }
        return maxLength;

    }
};
