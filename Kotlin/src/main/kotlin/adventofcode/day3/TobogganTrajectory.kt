package adventofcode.day3

class TobogganTrajectory {
    companion object {
        fun convertToList(line: String): List<Grid> {
            return line.map {
                if (it == '#') Grid.Tree else Grid.EMPTY
            }
        }

        fun countTreeOnMove(grids: List<List<Grid>>, right: Int, down: Int): Int {
            val depth = grids.size
            val repeatSize = grids[0].size
            var encounteredTrees = 0
            val coordinate = Coordinate()

            while (coordinate.y < depth) {
                if (grids[coordinate.y][coordinate.x % repeatSize] == Grid.Tree)
                    encounteredTrees++
                coordinate.moveY(down)
                coordinate.moveX(right)
            }
            return encounteredTrees
        }
    }
}