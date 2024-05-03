package leetcode;

// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

public class RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        boolean wasSame = false;
        int curIdx = 1;
        for (int i=1; i < nums.length; i++) {
            boolean isSame = nums[i] == nums[i-1];
            if (!(isSame & wasSame)) {
                nums[curIdx] = nums[i];
                curIdx++;
            }
            wasSame = isSame;
        }
        return curIdx;
    }
}
