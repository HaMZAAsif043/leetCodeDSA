function getConcatenation(nums) {
    let ans= nums;
    let n = nums.length

    for (let i=0 ; i< n ; i++){
        console.log(i)
        ans[i+n] = nums[i];
    }
    return ans
};
// function getConcatenation(nums) {
//     return nums.concat(nums)
// };
console.log(getConcatenation([1,2,1]))