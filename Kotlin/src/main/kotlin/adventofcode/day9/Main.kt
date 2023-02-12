package adventofcode.day9

import adventofcode.util.InputUtil

fun main() {
    val numbers = InputUtil.getListFromStdin { it.toLong() }
    val invalidNumber = EncodingError.findFirstInvalidNumber(numbers)
    val contiguousList = EncodingError.findContiguousList(numbers, invalidNumber)
    println(invalidNumber)
    println(contiguousList.max() + contiguousList.min())
}