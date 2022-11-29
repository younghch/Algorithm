// https://adventofcode.com/2020/day/1
package adventofcode

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.stream.Stream

class ReportRepair {

    fun getStreamFromString(s: String): Stream<String> {
        return s.split('\n').stream()
    }

    fun getStreamFromStdin(): Stream<String> {
        val list = mutableListOf<String>()
        with(BufferedReader(InputStreamReader(System.`in`))) {
            var line = this.readLine()
            while (line.isNotEmpty()) {
                list.add(line)
                line = this.readLine()
            }
        }
        return list.stream()
    }

    fun getMultipleOfSum2020Pair(stream: Stream<String>): Int {
        val numCount = mutableSetOf<Int>()
        var ans = -1
        stream.forEach {
            if (ans == -1) {
                val cur = it.toInt()
                if (numCount.contains(2020 - cur))
                    ans = cur * (2020 - cur)
                numCount.add(cur)
            }
        }
        return ans
    }
}