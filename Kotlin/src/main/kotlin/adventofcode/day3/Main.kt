// https://adventofcode.com/2020/day/3
package adventofcode.day3

import adventofcode.util.InputUtil

fun main() {
    val grids = InputUtil.getListFromStdin(TobogganTrajectory::convertToList)
    val pairs = listOf(Pair(1, 1), Pair(3, 1), Pair(5, 1), Pair(7, 1), Pair(1, 2))

    println(TobogganTrajectory.countTreeOnMove(grids, 3, 1))
    println(TobogganTrajectory.getMultipleOfCount(grids, pairs))
}