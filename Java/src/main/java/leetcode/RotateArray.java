package leetcode;

// https://leetcode.com/problems/rotate-array
public class RotateArray {

    public void rotate(int[] nums, int k) {
        int rotate = k % nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, rotate - 1);
        reverse(nums, rotate, nums.length - 1);
    }

    void reverse(int[] nums, int startIdx, int endIdx) {
        while (startIdx < endIdx) {
            int temp = nums[startIdx];
            nums[startIdx] = nums[endIdx];
            nums[endIdx] = temp;
            startIdx++;
            endIdx--;
        }
    }

    public void rotateCheckMoved(int[] nums, int k) {
        boolean[] moved = new boolean[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int curIdx = i;
            int curValue = nums[i];
            while (!moved[curIdx]) {
                moved[curIdx] = true;
                int rotatedIdx = (curIdx + k) % nums.length;
                int rotatedValue = nums[rotatedIdx];
                nums[rotatedIdx] = curValue;
                curIdx = rotatedIdx;
                curValue = rotatedValue;
            }
        }
    }

    public void rotateCopy(int[] nums, int k) {
        int rotate = k % nums.length;
        int[] rotatedNums = new int[nums.length];
        int j = 0;
        for (int i = nums.length - rotate; i < nums.length; i++) {
            rotatedNums[j] = nums[i];
            j++;
        }
        for (int i = 0; i < nums.length - rotate; i++) {
            rotatedNums[j] = nums[i];
            j++;
        }
        for (int l = 0; l < nums.length; l++) {
            nums[l] = rotatedNums[l];
        }
    }
}
