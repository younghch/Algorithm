// https://adventofcode.com/2020/day/5

package adventofcode.day5

class BinaryBoarding {
    companion object {

        fun getRowNum(s: String): Int {
            return Integer.parseInt(s.replace('F', '0').replace('B', '1'), 2)
        }

        fun getColNum(s: String): Int {
            return Integer.parseInt(s.replace('L', '0').replace('R', '1'), 2)
        }

        fun getSeatId(row: Int, col: Int): Int {
            return row * 8 + col
        }

        fun lineToSeatId(line: String): Int {
            if (line.isEmpty()) return -1

            val row = getRowNum(line.take(7))
            val col = getColNum(line.takeLast(3))
            return getSeatId(row, col)
        }

        fun findMissingBoardingPass(notAvailSeat: List<Int>): Int {
            val seats = 0..1023
            val availableSeats = seats.filter {
                !notAvailSeat.contains(it)
                        && it > notAvailSeat.min() + 2
                        && it < notAvailSeat.max() - 2
            }
            return availableSeats[0]
        }
    }
}