function findErrorNums(nums: number[]): number[] {
    let n = nums.length;
    let count = new Array(n + 1).fill(0);
    let duplicate = 0;
    let missing = 0;

    for (let num of nums) {
        count[num]++;
    }

    for (let i = 1; i <= n; i++) {
        if (count[i] === 2) duplicate = i;
        if (count[i] === 0) missing = i;
    }

    return [duplicate, missing];
}
