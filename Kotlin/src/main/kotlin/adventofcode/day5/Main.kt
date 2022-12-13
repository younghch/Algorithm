package adventofcode.day5

import adventofcode.util.InputUtil

fun main() {
    val list = InputUtil.getListFromStdin(BinaryBoarding::lineToSeatId).filter { it != -1 }
    println(list.max())
    println(BinaryBoarding.findMissingBoardingPass(list))
}