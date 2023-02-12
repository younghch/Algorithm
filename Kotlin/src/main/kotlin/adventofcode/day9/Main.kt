package adventofcode.day9

import adventofcode.util.InputUtil

fun main() {
    val numbers = InputUtil.getListFromStdin { it.toLong() }
    println(EncodingError.findFirstInvalidNumber(numbers))
}