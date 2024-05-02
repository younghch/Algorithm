package leetcode;

class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length;

        while (start < end) {
            int cur = (start + end) / 2;
            int toCompare = nums[cur];
            if (toCompare == target) return cur;
            else if (toCompare < target) start = cur+1;
            else end = cur;
        }
        return start;
    }

    public int searchInsertWithLibrary(int[] nums, int target) {
        int binarySearch = Arrays.binarySearch(nums, target);
        if (binarySearch < 0) return -binarySearch - 1;
        else return binarySearch;
    }
}