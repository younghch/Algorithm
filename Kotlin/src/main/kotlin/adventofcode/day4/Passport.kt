package adventofcode.day4

enum class Passport() {
    byr {
        override fun isValid(s: String): Boolean {
            val rule = Regex("(19[2-9][0-9])|(200[0-2])")
            return rule.matchEntire(s) != null
        }
    },
    iyr {
        override fun isValid(s: String): Boolean {
            val rule = Regex("(201[0-9])|(2020)")
            return rule.matches(s)
        }
    },
    eyr {
        override fun isValid(s: String): Boolean {
            val rule = Regex("(202[0-9])|(2030)")
            return rule.matches(s)
        }
    },
    hgt {
        override fun isValid(s: String): Boolean {
            val rule = Regex("""(\d+)((cm)|(in))""")
            val match = rule.matchEntire(s) ?: return false
            val height = match.destructured.component1().toInt()
            when (match.destructured.component2()) {
                "cm" -> return height in 150..193
                "in" -> return height in 59..76
            }
            return false
        }
    },
    hcl {
        override fun isValid(s: String): Boolean {
            val rule = Regex("""#[\da-f]{6}+""")
            return rule.matches(s)
        }
    },
    ecl {
        override fun isValid(s: String): Boolean {
            val colors = listOf("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            return colors.contains(s)
        }
    },
    pid {
        override fun isValid(s: String): Boolean {
            val rule = Regex("""[0-9]{9}+""")
            return rule.matches(s)
        }
    },
    cid {
        override fun isValid(s: String): Boolean {
            return true
        }
    };

    abstract fun isValid(s: String): Boolean
}

