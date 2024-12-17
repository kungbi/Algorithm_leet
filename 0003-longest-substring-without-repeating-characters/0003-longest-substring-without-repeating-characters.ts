function lengthOfLongestSubstring(s: string): number {
    let left = 0;
    let right = 0;

    const dict = {};
    const n = s.length;
    let result = 0;
    while (left < n && right < n) {
        const c = s[right];
        if (dict[c] === 0 || dict[c] === undefined) {
            dict[c] = 1;
            right += 1;
            result = Math.max(result, right - left);
        } else {
            dict[s[left]] = 0;
            left += 1;
        }
    }
    return result;
};