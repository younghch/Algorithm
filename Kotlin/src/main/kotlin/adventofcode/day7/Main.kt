package adventofcode.day7

import adventofcode.util.InputUtil

fun main(args: Array<String>) {
    val input = InputUtil.getListFromFile(args[0]) { it }

    val solution = HandyHaversacks()
    for (line in input) {
        solution.push(line)
    }
    println(solution.findPossibleParents("shiny gold").count())
    println(solution.getNumberOfDescendant("shiny gold"))
    
}