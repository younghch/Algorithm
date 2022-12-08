package adventofcode.day4

class PassportProcessing {
    companion object {
        fun checkPassportValid(passport: Map<String, String>): Boolean {

            for (enum in enumValues<Passport>()) {
                val key = enum.name
                if (key == "cid") continue
                if (passport[key] == null) return false
            }
            return true
        }

        fun putLineInfoToPassport(line: String, passport: MutableMap<String, String>) {
            line.split(' ').forEach {
                val kv = it.split(':')
                if (kv.size == 2) passport.put(kv[0], kv[1])
            }
        }

        fun countNumOfValid(lines: List<String>): Int {
            var numOfValid = 0
            var passport = mutableMapOf<String, String>()

            lines.forEach {
                if (it.isEmpty()) {
                    if (checkPassportValid(passport)) numOfValid += 1
                    passport = mutableMapOf()
                } else {
                    putLineInfoToPassport(it, passport)
                }
            }
            return numOfValid
        }
    }
}