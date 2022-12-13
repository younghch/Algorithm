package adventofcode.day5

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

//BFFFBBFRRR: row 70, column 7, seat ID 567.
//FFFBBBFRRR: row 14, column 7, seat ID 119.
//BBFFBBFRLL: row 102, column 4, seat ID 820.
internal class BinaryBoardingTest {

    @Test
    fun getRowNum() {

        Assertions.assertThat(BinaryBoarding.getRowNum("BFFFBBF")).isEqualTo(70)
        Assertions.assertThat(BinaryBoarding.getRowNum("FFFBBBF")).isEqualTo(14)
        Assertions.assertThat(BinaryBoarding.getRowNum("BBFFBBF")).isEqualTo(102)
    }

    @Test
    fun getColNum() {
        Assertions.assertThat(BinaryBoarding.getColNum("RRR")).isEqualTo(7)
        Assertions.assertThat(BinaryBoarding.getColNum("RRR")).isEqualTo(7)
        Assertions.assertThat(BinaryBoarding.getColNum("RLL")).isEqualTo(4)
    }

    @Test
    fun getSeatId() {
        Assertions.assertThat(BinaryBoarding.getSeatId(70, 7)).isEqualTo(567)
        Assertions.assertThat(BinaryBoarding.getSeatId(14, 7)).isEqualTo(119)
        Assertions.assertThat(BinaryBoarding.getSeatId(102, 4)).isEqualTo(820)
    }

    @Test
    fun lineToSeatId() {
        Assertions.assertThat(BinaryBoarding.lineToSeatId("BFFFBBFRRR")).isEqualTo(567)
        Assertions.assertThat(BinaryBoarding.lineToSeatId("FFFBBBFRRR")).isEqualTo(119)
        Assertions.assertThat(BinaryBoarding.lineToSeatId("BBFFBBFRLL")).isEqualTo(820)

    }


}