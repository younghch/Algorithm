package adventofcode.day4

import adventofcode.util.InputUtil

fun main() {
    val rawPassportLines = InputUtil.getListFromStdin { it }
    val numOfValid1 = PassportProcessing.countNumOfValid(rawPassportLines, '1')
    val numOfValid2 = PassportProcessing.countNumOfValid(rawPassportLines, '2')
    println(numOfValid1)
    println(numOfValid2)
}