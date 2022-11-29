// https://adventofcode.com/2020/day/1
package adventofcode

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

class ReportRepair {

    fun getMultipleOfSum2020Pair(list: List<Int>): Int? {
        val pair = getPairOfSum(list, 2020)
        return pair?.let { (a, b) -> a * b }
    }

    fun getMultipleOfSum2020Triple(list: List<Int>): Int? {
        val counter = getCounter(list)
        val triple = getTripleOfSum(list, counter, 2020)
        return triple?.let { (a, b, c) -> a * b * c }
    }

    fun getPairOfSum(list: List<Int>, target: Int): Pair<Int, Int>? {
        var found = false
        val numChecked = mutableSetOf<Int>()
        var pair: Pair<Int, Int>? = null

        list.forEach {
            if (!found) {
                if (numChecked.contains(target - it)) {
                    pair = Pair(it, target - it)
                    found = true
                } else {
                    numChecked.add(it)
                }
            }
        }
        return pair
    }

    fun getTripleOfSum(list: List<Int>, counter: Map<Int, Int>, target: Int): Triple<Int, Int, Int>? {
        return list.mapNotNull {
            val pair = getPairOfSum(list, target - it)
            if (pair != null && isAnswerValid(counter, it, pair.first, pair.second)) {
                Triple(it, pair.first, pair.second)
            } else
                null
        }.firstOrNull()
    }

    fun getCounter(list: List<Int>): Map<Int, Int> {
        val map = mutableMapOf<Int, Int>()
        list.forEach {
            if (map.containsKey(it))
                map[it] = map[it]!! + 1
            else
                map[it] = 1
        }
        return map
    }

    fun isAnswerValid(counter: Map<Int, Int>, vararg ans: Int): Boolean {
        val copiedCounter = counter.toMutableMap()
        for (i in ans) {
            if (copiedCounter[i] == 0) return false
            copiedCounter[i] = copiedCounter[i]!! - 1
        }
        return true
    }


    fun getListFromString(s: String): List<Int> {
        return s.split('\n').map(String::toInt)
    }

    fun getListFromStdin(): List<Int> {
        val list = mutableListOf<String>()
        with(BufferedReader(InputStreamReader(System.`in`))) {
            var line = this.readLine()
            while (line.isNotEmpty()) {
                list.add(line)
                line = this.readLine()
            }
        }
        return list.map(String::toInt)
    }

    fun getListFromFile(path: String): List<Int> {
        return File(path).readLines().map(String::toInt)
    }

    fun guideSolution(list: List<String>): Int {
        val numbers = list.map(String::toInt).toList()
        val complements = numbers.associateBy { 2020 - it }
        val pair = numbers.mapNotNull {
            val complement = complements[it]
            if (complement != null) Pair(it, complement) else null
        }.firstOrNull()
        return pair?.let { (a, b) -> a * b }!!
    }
}