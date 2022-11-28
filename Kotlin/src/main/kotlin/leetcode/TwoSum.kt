// https://leetcode.com/problems/two-sum/

package leetcode

class TwoSum {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var left = 0
        var right = nums.size - 1
        var sum: Int

        var sortedNums = nums.sorted()

        sum = sortedNums[left] + sortedNums[right]
        while (sum != target) {
            if (sum < target) left += 1
            else right -= 1
            sum = sortedNums[left] + sortedNums[right]
        }

        return intArrayOf(nums.indexOf(sortedNums[left]), nums.lastIndexOf(sortedNums[right]))
    }

    fun twoSumHash(nums: IntArray, target: Int): IntArray {
        val map = mutableMapOf<Int, Int>()

        for (i in nums.indices) {
            val v = nums[i]
            if (map.containsKey(target - v))
                return intArrayOf(map.get(target - v)!!, i)
            map.put(v, i)
        }

        return intArrayOf()
    }
}