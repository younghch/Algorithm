package adventofcode.day8

import adventofcode.util.InputUtil

fun main(args: Array<String>) {
    val input = InputUtil.getListFromFile(args[0]) {
        val line = it.split(' ')
        Pair(line[0], line[1].toInt())
    }
    val sol1 = getIsInfiniteAndAcc(input)
    val sol2 = tryChangeGetAcc(input)
    println(sol1.second)
    println(sol2)
}

fun getIsInfiniteAndAcc(
    instructions: List<Pair<String, Int>>,
    curPointer: Int = 0,
    accumulated: Int = 0
): Pair<Boolean, Int> {
    var acc = accumulated
    var cur = curPointer
    val visited = mutableSetOf<Int>()

    while (!visited.contains(cur) && cur < instructions.size) {
        visited.add(cur)
        val (operation, value) = instructions[cur]
        when (operation) {
            "nop" -> cur++
            "acc" -> {
                cur++
                acc += value
            }

            "jmp" -> cur += value
        }
    }
    return Pair(cur < instructions.size, acc)
}

fun tryChangeGetAcc(instructions: List<Pair<String, Int>>): Int {
    var acc = 0
    var cur = 0
    var tried = Pair(true, 0)

    while (tried.first) {
        val (operation, value) = instructions[cur]
        when (operation) {
            "nop" -> {
                tried = getIsInfiniteAndAcc(instructions, cur + value, acc)
                if (tried.first)
                    cur++
            }

            "acc" -> {
                cur++
                acc += value
            }

            "jmp" -> {
                tried = getIsInfiniteAndAcc(instructions, cur + 1, acc)
                if (tried.first)
                    cur += value
            }
        }
    }
    return tried.second
}