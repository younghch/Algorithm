package adventofcode.util

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

class InputUtil {
    companion object Functions {
        fun getIntListFromString(s: String): List<Int> {
            return s.split('\n').map(String::toInt)
        }

        fun getIntListFromStdin(): List<Int> {
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

        fun getIntListFromFile(path: String): List<Int> {
            return File(path).readLines().map(String::toInt)
        }
    }

}