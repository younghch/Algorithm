package adventofcode.day7

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

internal class HandyHaversacksTest {
    @Test
    fun isEmptyBag() {
        val empty = "faded blue bags contain no other bags."
        val notEmpty = "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags."

        Assertions.assertThat(HandyHaversacks.isEmptyBag(empty)).isTrue
        Assertions.assertThat(HandyHaversacks.isEmptyBag(notEmpty)).isFalse
    }

    @Test
    fun lineToEmptyBagPair() {
        val line = "dotted black bags contain no other bags."
        val pair = HandyHaversacks.lineToEmptyBagPair(line)

        Assertions.assertThat(pair.first).isEqualTo("dotted black")
        Assertions.assertThat(pair.second).isNull()
    }

    @Test
    fun lineToChildParentBagPair() {
        val line1 = "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags."
        val line2 = "bright white bags contain 1 shiny gold bag."

        val pair1 = HandyHaversacks.lineToParentChildrenPair(line1)
        Assertions.assertThat(pair1.first).isEqualTo("vibrant plum")
        Assertions.assertThat(pair1.second!!.get(0)).isEqualTo(Pair("faded blue", 5))
        Assertions.assertThat(pair1.second!!.get(1)).isEqualTo(Pair("dotted black", 6))

        val pair2 = HandyHaversacks.lineToParentChildrenPair(line2)
        Assertions.assertThat(pair2.first).isEqualTo("bright white")
        Assertions.assertThat(pair2.second!!.get(0)).isEqualTo(Pair("shiny gold", 1))

    }
}
