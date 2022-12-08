package adventofcode.util

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

class InputUtil {
    companion object Functions {

        fun <T> getListFromStdin(converter: (s: String) -> T): List<T> {
            val list = mutableListOf<String>()

            with(BufferedReader(InputStreamReader(System.`in`))) {
                var line = this.readLine()
                var wasEmpty = false
                while (!wasEmpty || line.isNotEmpty()) {
                    wasEmpty = line.isEmpty()
                    list.add(line)
                    line = this.readLine()
                }
            }
            return list.map(converter)
        }

        fun <T> getListFromString(s: String, converter: (s: String) -> T): List<T> {
            return s.split('\n').map(converter)
        }

        fun <T> getListFromFile(path: String, converter: (s: String) -> T): List<T> {
            return File(path).readLines().map(converter)
        }
    }

}