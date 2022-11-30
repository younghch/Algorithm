package adventofcode.runner

import adventofcode.day1.ReportRepair
import adventofcode.util.InputUtil


fun main() {
    val solution = ReportRepair()
    val list = InputUtil.getIntListFromStdin()
    println(solution.getMultipleOfSum2020Pair(list))
    println(solution.getMultipleOfSum2020Triple(list))
}
