package adventofcode

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class ReportRepairTest {
    val solution = ReportRepair()
    val stringInput = "1721\n" +
            "979\n" +
            "366\n" +
            "299\n" +
            "675\n" +
            "1456"

    @Test
    fun listFromString() {
        val list = solution.getListFromString(stringInput)
        assertArrayEquals(intArrayOf(1721, 979, 366, 299, 675, 1456), list.toIntArray())
    }

    @Test
    fun listFromFile() {
        val list =
            solution.getListFromFile("/Users/choyounghoun/Algorithm/Kotlin/src/test/resources/adventofcode/day1.txt")
        assertEquals(2008, list[0])
    }

    @Test
    fun getMultipleFromSumPair() {
        val list = solution.getListFromString(stringInput)
        assertEquals(1721 * 299, solution.getMultipleOfSum2020Pair(list))
    }

    @Test
    fun preventHalfCountedTwice() {
        val list = listOf<Int>(1010, 1000, 1)
        assertNull(solution.getMultipleOfSum2020Pair(list))
    }

    @Test
    fun getMultipleFromSumTripler() {
        val list = solution.getListFromString(stringInput)
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