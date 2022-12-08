package adventofcode.day4

import adventofcode.util.InputUtil

fun main() {
    val numOfValid = PassportProcessing.countNumOfValid(InputUtil.getListFromStdin { it })
    println(numOfValid)
}