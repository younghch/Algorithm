package adventofcode

import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class ReportRepairTest {
    val solution = ReportRepair()

    @Test
    fun example() {
        val in_ = "1721\n" +
                "979\n" +
                "366\n" +
                "299\n" +
                "675\n" +
                "1456"
        Assertions.assertEquals(1721 * 299, solution.getAns(in_))
    }
}