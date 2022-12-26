package adventofcode.day7

class HandyHaversacks {

    val childToParents = mutableMapOf<String, MutableList<Pair<String, Int>>?>()

    fun push(line: String) {
        val parentToChildren = getParentToChildrenWithCount(line)
        val parent = parentToChildren.first
        val children = parentToChildren.second

        for (child in children) {
            if (childToParents.containsKey(child.first)) {
                childToParents.get(child.first)!!.add(Pair(parent, child.second))
            } else {
                childToParents.put(child.first, mutableListOf(Pair(parent, child.second)))
            }
        }
    }

    fun findPossibleParents(child: String): Set<String> {
        if (!childToParents.containsKey(child))
            return setOf()
        
        var parents = childToParents[child]!!.map { it.first }.toSet()
        for (directParent in childToParents[child]!!) {
            parents = parents.union(findPossibleParents(directParent.first))
        }
        return parents
    }

    companion object {
        val regEmpty = Regex("""(\S+ \S+) bags contain no other bags.""")
        val regParent = Regex("""(\S+ \S+) bags contain""")
        val regChild = Regex("""(\d+) (\S+ \S+) bags*[,.]""")
        fun isEmptyBag(line: String): Boolean {
            return regEmpty.matches(line)
        }

        fun lineToEmptyBagPair(line: String): Pair<String, List<Pair<String, Int>>> {
            return Pair(regEmpty.matchEntire(line)!!.destructured.component1(), listOf())
        }

        fun lineToParentChildrenPair(line: String): Pair<String, List<Pair<String, Int>>> {
            val parent = regParent.find(line)!!.destructured.component1()
            val children = regChild.findAll(line).map {
                Pair(it.destructured.component2(), it.destructured.component1().toInt())
            }.toList()
            return Pair(parent, children)
        }

        fun getParentToChildrenWithCount(line: String): Pair<String, List<Pair<String, Int>>> {
            return if (isEmptyBag(line)) lineToEmptyBagPair(line)
            else lineToParentChildrenPair(line)
        }
    }
}