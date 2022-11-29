package adventofcode.runner

import adventofcode.ReportRepair


fun main() {
    val solution = ReportRepair()
    val list = solution.getListFromStdin()
    println(solution.getMultipleOfSum2020Pair(list))
    println(solution.getMultipleOfSum2020Triple(list))
}
