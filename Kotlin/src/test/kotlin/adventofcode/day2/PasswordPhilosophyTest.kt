package adventofcode.day2

import adventofcode.util.InputUtil
import org.assertj.core.api.Assertions
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test

internal class PasswordPhilosophyTest {
    val s = "1-3 a: abcde\n" +
            "1-3 b: cdefg\n" +
            "2-9 c: ccccccccc"
    var solution: PasswordPhilosophy = PasswordPhilosophy()

    @BeforeEach
    fun initSolution() {
        solution = PasswordPhilosophy()
    }

    @Test
    fun convertPolicyPasswordPairFromString() {
        val policyPasswordPairs = InputUtil.getListFromString(s, PasswordPhilosophy::policyPasswordPairConverter)
        Assertions.assertThat(policyPasswordPairs[0])
            .isEqualToComparingFieldByField(PolicyPasswordPair(Triple(1, 3, 'a'), "abcde"))
    }

    @Test
    fun countValidFromStringCondition1() {
        val policyPasswordPairs = InputUtil.getListFromString(s, PasswordPhilosophy::policyPasswordPairConverter)
        solution.policyPasswordPairs = policyPasswordPairs
        Assertions.assertThat(solution.numOfValidCondition1).isEqualTo(2)
    }

    @Test
    fun countValidFromStringCondition2() {
        val policyPasswordPairs = InputUtil.getListFromString(s, PasswordPhilosophy::policyPasswordPairConverter)
        solution.policyPasswordPairs = policyPasswordPairs
        Assertions.assertThat(solution.numOfValidCondition2).isEqualTo(1)
    }


}