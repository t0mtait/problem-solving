function getCommon(nums1, nums2) {
    // convert to sets to get rid of dupes in each array
    let set1 = new Set(nums1);
    let set2 = new Set(nums2);
    let commonNums = [...set1].filter(num => set2.has(num));
    if (commonNums.length === 0)
        return -1;
    else
        return Math.min(...commonNums);
}

const nums1 = [3,4,5,10,12,15,16,16,25,48,51,69,74,74,78,78,78,82,82,88];
const nums2 = [3,8,9,10,13,16,24,25,27,29,34,39,55,62,70,80,83,87,92,94];

console.log(getCommon(nums1,nums2));  //Returns 3