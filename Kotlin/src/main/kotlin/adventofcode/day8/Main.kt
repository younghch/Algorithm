package adventofcode.day8

import adventofcode.util.InputUtil

fun main(args: Array<String>) {
    val input = InputUtil.getListFromFile(args[0]) {
        it.split(' ')
    }
    val visited = mutableSetOf<Int>()
    var cur = 0
    var acc = 0

    while (!visited.contains(cur)) {
        visited.add(cur)
        val (operation, value) = input[cur]
        when (operation) {
            "nop" -> cur++
            "acc" -> {
                cur++
                acc += value.toInt()
            }

            "jmp" -> cur += value.toInt()
        }
    }
    println(acc)
}