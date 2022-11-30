// https://adventofcode.com/2020/day/2
/*
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
*/
package adventofcode.day2

import java.lang.Error

class PasswordPhilosophy {
    var policyPasswordPairs = listOf<PolicyPasswordPair>()
    val numOfValid: Int
        get() = calculateNumOfValid()


    fun calculateNumOfValid(): Int {
        var numOfValid = 0
        policyPasswordPairs.forEach {
            val (lower, upper, toCount) = it.policy
            var found = 0
            it.password.forEach {
                if (it == toCount) found++
            }
            if (found in lower..upper)
                numOfValid++
        }
        return numOfValid
    }

    companion object Helper {
        fun policyPasswordPairConverter(s: String): PolicyPasswordPair {
            val regex = "[-:\\s]+"
            with(s.split(regex.toRegex())) {
                if (size != 4) throw Error("Invalid input")
                return PolicyPasswordPair(Triple(get(0).toInt(), get(1).toInt(), get(2)[0]), get(3))
            }
        }
    }

}