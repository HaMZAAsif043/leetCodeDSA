/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let number =[...nums1,...nums2].sort((a, b) => a - b)
            // console.log(number)
    if(number.length %2 ===0){
      const  newNumber = (number[number.length/2]+number[number.length/2 -1])/2
        console.log(number,number.length/2)
      return newNumber
    }
   return  number[Math.floor(number.length/2)]
};


const num1 =[1,2,3,4,5]
const num2 =[6,7,8,9,10,11,12,13,14,15,16,17]

function benchmark(fn, nums1, nums2, iterations = 1_000_000) {
  let start = performance.now();
  for (let i = 0; i < iterations; i++) {
    fn(nums1, nums2);
  }
  let end = performance.now();
  return (end - start).toFixed(4);
}

console.log("Benchmark:", benchmark(findMedianSortedArrays, num1, num2), "ms");
