package leetcode;

import java.util.Arrays;

// https://leetcode.com/problems/product-of-array-except-self
public class ProductOfArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int[] prefixProducts = new int[nums.length];
        int[] suffixProducts = new int[nums.length];

        prefixProducts[0] = 1;
        suffixProducts[nums.length - 1] = 1;

        for (int i = 1; i < nums.length; i++) {
            prefixProducts[i] = prefixProducts[i - 1] * nums[i - 1];
            suffixProducts[nums.length - 1 - i] = suffixProducts[nums.length - i] * nums[nums.length - i];
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = prefixProducts[i] * suffixProducts[i];
        }
        return nums;
    }

    public int[] productExceptSelfMinimumSpace(int[] nums) {
        int[] answer = new int[nums.length];
        Arrays.fill(answer, 1);

        int cur = 1;
        for (int i = 0; i < nums.length; i++) {
            answer[i] *= cur;
            cur *= nums[i];
        }
        cur = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            answer[i] *= cur;
            cur *= nums[i];
        }
        return answer;
    }
}
