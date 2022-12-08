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
            return rule.matchEntire(s) != null
        }
    },
    eyr {
        override fun isValid(s: String): Boolean {
            val rule = Regex("(202[0-9])|(2030)")
            return rule.matchEntire(s) != null
        }
    },
    hgt {
        override fun isValid(s: String): Boolean {
            TODO("Not yet implemented")
        }
    },
    hcl {
        override fun isValid(s: String): Boolean {
            TODO("Not yet implemented")
        }
    },
    ecl {
        override fun isValid(s: String): Boolean {
            TODO("Not yet implemented")
        }
    },
    pid {
        override fun isValid(s: String): Boolean {
            TODO("Not yet implemented")
        }
    },
    cid {
        override fun isValid(s: String): Boolean {
            TODO("Not yet implemented")
        }
    };

    abstract fun isValid(s: String): Boolean
}

