package adventofcode.day7

class HandyHaversacks {

    val childToParents = mutableMapOf<String, List<Pair<String, Int>>?>()

    fun push(line: String) {

    }

    companion object {
        val regEmpty = Regex("""(\S+ \S+) bags contain no other bags.""")
        val regParent = Regex("""(\S+ \S+) bags contain""")
        val regChild = Regex("""(\d+) (\S+ \S+) bags*[,.]""")
        fun isEmptyBag(line: String): Boolean {
            return regEmpty.matches(line)
        }

        fun lineToEmptyBagPair(line: String): Pair<String, List<Pair<String, Int>>?> {
            return Pair(regEmpty.matchEntire(line)!!.destructured.component1(), null)
        }

        fun lineToParentChildrenPair(line: String): Pair<String, List<Pair<String, Int>>?> {
            val parent = regParent.find(line)!!.destructured.component1()
            val children = regChild.findAll(line).map {
                Pair(it.destructured.component2(), it.destructured.component1().toInt())
            }.toList()
            return Pair(parent, children)
        }

        fun getChildParentPair(line: String): Pair<String, List<Pair<String, Int>>?> {
            return if (isEmptyBag(line)) lineToEmptyBagPair(line)
            else lineToParentChildrenPair(line)
        }
    }
}