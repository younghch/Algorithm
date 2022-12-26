package adventofcode.day6

class CustomCustomers {
    companion object {
        fun collectAnswerByGroup(answers: List<String>): List<Set<Char>> {
            val groupAnsList = mutableListOf<Set<Char>>()
            var groupAns = setOf<Char>()
            for (ans in answers) {
                if (ans.isEmpty()) {
                    groupAnsList.add(groupAns)
                    groupAns = setOf()
                } else {
                    groupAns = groupAns.union(ans.toSet())
                }
            }
            groupAnsList.add(groupAns)
            return groupAnsList
        }

        fun getTotalAnsCount(groupAnsList: List<Set<Char>>): Int {
            return groupAnsList.map { it.size }.reduce { acc, ansCount -> acc + ansCount }
        }

        fun getAns1(input: List<String>): Int {
            return getTotalAnsCount(collectAnswerByGroup(input))
        }
    }
}