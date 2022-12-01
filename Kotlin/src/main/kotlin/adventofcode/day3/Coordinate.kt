package adventofcode.day3

class Coordinate() {
    var x = 0
    var y = 0

    fun moveX(d: Int) {
        x = x + d
    }

    fun moveY(d: Int) {
        y = y + d
    }
}
