package adventofcode.day6

class CustomCustomers {
    companion object {
        fun collectAnswerByGroup(answers: List<String>, part: Int = 1): List<Set<Char>> {
            val groupAnsList = mutableListOf<Set<Char>>()
            var groupAns: Set<Char>? = null
            for (ans in answers) {
                if (ans.isEmpty()) {
                    groupAnsList.add(groupAns!!)
                    groupAns = null
                } else {
                    groupAns =
                        if (groupAns == null)
                            ans.toSet()
                        else if (part == 1)
                            groupAns.union(ans.toSet())
                        else
                            groupAns.intersect(ans.toSet())
                }
            }
            if (groupAns != null)
                groupAnsList.add(groupAns)
            return groupAnsList
        }

        fun getTotalAnsCount(groupAnsList: List<Set<Char>>): Int {
            return groupAnsList.map { it.size }.reduce { acc, ansCount -> acc + ansCount }
        }

        fun getAns(input: List<String>, part: Int = 1): Int {
            return getTotalAnsCount(collectAnswerByGroup(input, part))
        }
    }
}