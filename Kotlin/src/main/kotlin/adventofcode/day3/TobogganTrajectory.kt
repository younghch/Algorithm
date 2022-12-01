package adventofcode.day3

class TobogganTrajectory {
    companion object {
        fun convertToList(line: String): List<Grid> {
            return line.map {
                if (it == '#') Grid.Tree else Grid.EMPTY
            }
        }

        fun countTreeOnMove(grids: List<List<Grid>>, right: Int, down: Int): Long {
            val depth = grids.size
            val repeatSize = grids[0].size
            var encounteredTrees = 0L
            val coordinate = Coordinate()

            while (coordinate.y < depth) {
                if (grids[coordinate.y][coordinate.x % repeatSize] == Grid.Tree)
                    encounteredTrees++
                coordinate.moveY(down)
                coordinate.moveX(right)
            }
            return encounteredTrees
        }

        fun getMultipleOfCount(grids: List<List<Grid>>, slopes: List<Pair<Int, Int>>): Long {
            if (grids.isEmpty()) return 0
            else {
                var mul = 1L
                slopes.forEach { (right, down) ->
                    mul *= countTreeOnMove(grids, right, down)
                }
                return mul
            }

        }
    }
}