// var longestPalindrome = function(s) {
//     let target= s.toString()
//    let left =0 ; let right =target.length -1 
//    result =""
//      while(left<right){
//         if(target[left] !== target[right]){
//             console.log("not",target[left] , target[right])
//         right < target.length -1 ? left +=1 : right -=1
//         }
//         console.log("is",target[left] , target[right])
//         result += target.slice(left,right)
//         left +=1
//         right -=1
//      }
//     return result;
// }
var longestPalindrome = function(s) {
    if (s.length < 2) return s;

    let start = 0, maxLen = 1;

    function expandAroundCenter(left, right) {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            console.log("left", s[left], "right", s[right])
            if (right - left + 1 > maxLen) {
                start = left;
                console.log("start", start)
                console.log("maxLen", maxLen)
                maxLen = right - left + 1;
                console.log("maxLen", maxLen)
            }
            left--;
            right++;
            console.log("left", left,"right",right)
        }
    }

    for (let i = 0; i < s.length; i++) {
        expandAroundCenter(i, i);     
        expandAroundCenter(i, i + 1); 
    }

    return s.slice(start, start + maxLen);
};

 s = "cbbd"
 console.log(longestPalindrome(s))