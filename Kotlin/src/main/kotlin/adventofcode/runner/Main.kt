package adventofcode.runner

import adventofcode.ReportRepair


fun main() {
    val solution = ReportRepair()
    val stream = solution.getStreamFromStdin()
    print(solution.getMultipleOfSum2020Pair(stream))
}
