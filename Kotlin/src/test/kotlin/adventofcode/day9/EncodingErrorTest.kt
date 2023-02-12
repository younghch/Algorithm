package adventofcode.day9


import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

class EncodingErrorTest {
    @Test
    fun pairExist() {
        val window = mutableSetOf(35L, 20L, 15L, 25L, 47L)
        val target = 40L
        Assertions.assertThat(EncodingError.isPairExist(window, target)).isTrue
    }

    @Test
    fun pairNotExist() {
        val window = mutableSetOf(95L, 102L, 117L, 150L, 182L)
        val target = 127L
        Assertions.assertThat(EncodingError.isPairExist(window, target)).isFalse
    }

    @Test
    fun findFirstInvalid() {
        val numbers = listOf(
            35L,
            20L,
            15L,
            25L,
            47L,
            40L,
            62L,
            55L,
            65L,
            95L,
            102L,
            117L,
            150L,
            182L,
            127L,
            219L,
            299L,
            277L,
            309L,
            576L
        )
        Assertions.assertThat(EncodingError.findFirstInvalidNumber(numbers, 5)).isEqualTo(127L)
    }
}