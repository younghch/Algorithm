// https://leetcode.com/problems/two-sum/

package leetcode

class TwoSum {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var left = 0
        var right = nums.size - 1
        var sum:Int

        var sortedNums = nums.sorted()

        sum = sortedNums[left]+sortedNums[right]
        while(sum != target) {
            if (sum < target) left += 1
            else right -= 1
            sum = sortedNums[left]+sortedNums[right]
        }

        return intArrayOf(nums.indexOf(sortedNums[left]), nums.lastIndexOf(sortedNums[right]))
    }
}