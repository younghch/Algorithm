package adventofcode.day6

import adventofcode.util.InputUtil

fun main() {
    val answers = InputUtil.getListFromStdin { it }
    println(CustomCustomers.getAns(answers))
    println(CustomCustomers.getAns(answers, 2))
}