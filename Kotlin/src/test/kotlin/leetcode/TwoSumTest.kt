package leetcode

import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*

internal class TwoSumTest {
    val solution = TwoSum()

    @Test
    fun twoSum1() {
        Assertions.assertArrayEquals(intArrayOf(0,1), solution.twoSum(intArrayOf(2,7,11,15), 9))
    }

    @Test
    fun twoSum2() {
        Assertions.assertArrayEquals(intArrayOf(1,2), solution.twoSum(intArrayOf(3,2,4), 6))
    }

    @Test
    fun twoSum3() {
        Assertions.assertArrayEquals(intArrayOf(0,1), solution.twoSum(intArrayOf(3,3), 6))
    }



}