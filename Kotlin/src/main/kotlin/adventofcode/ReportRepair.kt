// https://adventofcode.com/2020/day/1
package adventofcode

class ReportRepair {

    fun getAns(in_: String): Int {
        val numCount = mutableSetOf<Int>()
        var ans = -1
        in_.split('\n').map {
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