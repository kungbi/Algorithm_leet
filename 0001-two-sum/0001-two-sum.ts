function twoSum(nums: number[], target: number): number[] {
    const map = Object.fromEntries(nums.map((num, index) => [num, index]));

    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i];
        if (map[diff] && i !== map[diff]) {
            return [i, map[diff]];
        }
    }
};