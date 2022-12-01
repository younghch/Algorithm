package adventofcode.day3

import adventofcode.util.InputUtil
import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

internal class TobogganTrajectoryTest {
    val sampleInput = """
        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#
    """.trimIndent()

    @Test
    fun convertLineFromString() {
        val grids = InputUtil.getListFromString(sampleInput, TobogganTrajectory::convertToList)
        Assertions.assertThat(grids[0]).isEqualTo(
            listOf(
                Grid.EMPTY,
                Grid.EMPTY,
                Grid.Tree,
                Grid.Tree,
                Grid.EMPTY,
                Grid.EMPTY,
                Grid.EMPTY,
                Grid.EMPTY,
                Grid.EMPTY,
                Grid.EMPTY,
                Grid.EMPTY
            )
        )
    }

    @Test
    fun countEncounteredTreeOnR3D1() {
        val grids = InputUtil.getListFromString(sampleInput, TobogganTrajectory::convertToList)
        Assertions.assertThat(TobogganTrajectory.countTreeOnMove(grids, 3, 1)).isEqualTo(7)
    }

    @Test
    fun multipleOfCount() {
        val grids = InputUtil.getListFromString(sampleInput, TobogganTrajectory::convertToList)
        val mul = TobogganTrajectory.getMultipleOfCount(
            grids,
            listOf(Pair(1, 1), Pair(3, 1), Pair(5, 1), Pair(7, 1), Pair(1, 2))
        )
        Assertions.assertThat(mul).isEqualTo(336)
    }
}