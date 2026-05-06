var isPalindrome = function(x) {
    let target= x.toString()
   let left =0 ; let right =target.length -1 
     while(left<right){
        if(target[left] !== target[right]){
            console.log("not",target[left] , target[right])
            return false;
        }
        console.log("is",target[left] , target[right])
        left +=1
        right -=1
     }
    return true;
}

     const palindrome = isPalindrome(121)

     console.log(palindrome)
     /**
      * Two pointers
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let isNegative = x < 0;
    let num = Math.abs(x);
    let reverseNum = 0;
    while (num > 0) {
        let lastDigit = num % 10;
        reverseNum = reverseNum * 10 + lastDigit;
        num = Math.floor(num/10);
    }

    reverseNum = isNegative ? reverseNum +'-' : reverseNum;

    return x == reverseNum;
};