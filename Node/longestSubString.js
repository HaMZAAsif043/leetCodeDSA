/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let freq ={}; let result = "";
    for(let i =0; i < s.length ; i++){
        if(!freq[s[i]]){
            freq[s[i]] =true;
result += s[i]
        }
        else{
          result = result.length -2
        }
    }
    return result.length
};
console.log(lengthOfLongestSubstring("pwwkew"))