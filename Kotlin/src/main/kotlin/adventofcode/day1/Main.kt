package adventofcode.day1

import adventofcode.util.InputUtil


fun main() {
    val solution = ReportRepair()
    val list = InputUtil.getListFromStdin(String::toInt)
    println(solution.getMultipleOfSum2020Pair(list))
    println(solution.getMultipleOfSum2020Triple(list))
}
