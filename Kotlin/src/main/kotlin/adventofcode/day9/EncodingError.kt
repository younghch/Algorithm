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

        fun findContiguousList(numbers: List<Long>, target: Long): List<Long> {
            var start = 0
            var window = 1
            var sum = numbers[start] + numbers[start + window]

            while (sum != target && start < numbers.size - 1) {
                if (sum + numbers[window + 1] < target) {
                    window++
                    sum += numbers[start + window]
                } else {
                    sum -= numbers[start]
                    start += 1
                    window--
                }
            }
            return numbers.subList(start, start + window + 1)
        }
    }
}