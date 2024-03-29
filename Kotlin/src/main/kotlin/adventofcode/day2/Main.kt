package adventofcode.day2

import adventofcode.util.InputUtil

fun main() {
    val solution = PasswordPhilosophy()
    solution.policyPasswordPairs = InputUtil.getListFromStdin(PasswordPhilosophy::policyPasswordPairConverter)
    println(solution.numOfValidCondition1)
    println(solution.numOfValidCondition2)
}