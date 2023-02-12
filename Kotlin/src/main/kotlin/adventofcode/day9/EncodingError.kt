package adventofcode.day9

class EncodingError {
    companion object {
        fun isPairExist(window: MutableSet<Long>, target: Long): Boolean {
            for (i in window) {
                if (window.contains(target - i))
                    return true
            }
            return false
        }

        fun findFirstInvalidNumber(numbers: List<Long>, windowSize: Int = 25): Long {
            val window = numbers.subList(0, windowSize).toMutableSet()
            for (i in windowSize until numbers.size) {
                if (!isPairExist(window, numbers[i])) return numbers[i]
                window.remove(numbers[i - windowSize])
                window.add(numbers[i])
            }
            return -1
        }
    }
}