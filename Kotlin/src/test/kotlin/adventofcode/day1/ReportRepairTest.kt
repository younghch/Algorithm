package adventofcode.day1

import adventofcode.util.InputUtil
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class Day1Test {
    val solution = ReportRepair()
    val stringInput = "1721\n" +
            "979\n" +
            "366\n" +
            "299\n" +
            "675\n" +
            "1456"

    @Test
    fun listFromString() {
        val list = InputUtil.getListFromString(stringInput, String::toInt)
        assertArrayEquals(intArrayOf(1721, 979, 366, 299, 675, 1456), list.toIntArray())
    }

    @Test
    fun listFromFile() {
        val list =
            InputUtil.getListFromFile(
                "/Users/choyounghoun/Algorithm/Kotlin/src/test/resources/adventofcode/day1.txt",
                String::toInt
            )
        assertEquals(2008, list[0])
    }

    @Test
    fun getMultipleFromSumPair() {
        val list = InputUtil.getListFromString(stringInput, String::toInt)
        assertEquals(1721 * 299, solution.getMultipleOfSum2020Pair(list))
    }

    @Test
    fun preventHalfCountedTwice() {
        val list = listOf<Int>(1010, 1000, 1)
        assertNull(solution.getMultipleOfSum2020Pair(list))
    }

    @Test
    fun getMultipleFromSumTripler() {
        val list = InputUtil.getListFromString(stringInput, String::toInt)
        assertEquals(979 * 366 * 675, solution.getMultipleOfSum2020Triple(list))
    }

    @Test
    fun preventOneThirdDuplicateCounted() {
        val target = 9
        val list = listOf<Int>(3, 3, 4)
        val counter = solution.getCounter(list)
        assertNull(solution.getTripleOfSum(list, counter, target))
    }

}