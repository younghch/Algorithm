package adventofcode

import org.junit.jupiter.api.Assertions.assertArrayEquals
import org.junit.jupiter.api.Assertions.assertEquals
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
    fun streamFromString() {
        val stream = solution.getStreamFromString(stringInput)
        assertArrayEquals(arrayOf("1721", "979", "366", "299", "675", "1456"), stream.toArray())
    }

    @Test
    fun streamFromFile() {
        val stream =
            solution.getStreamFromFile("~/Algorithm/Kotlin/src/test/resources/adventofcode/day1.txt")
        assertEquals("2008", stream.findFirst().get())
    }

    @Test
    fun getMultipleFromString() {
        val stream = solution.getStreamFromString(stringInput)
        assertEquals(1721 * 299, solution.getMultipleOfSum2020Pair(stream))
    }
}