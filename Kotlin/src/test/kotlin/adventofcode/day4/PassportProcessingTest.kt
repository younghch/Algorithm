package adventofcode.day4

import adventofcode.util.InputUtil
import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

internal class PassportProcessingTest {
    val s = """
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in
    """.trimIndent()

    @Test

    fun putLineInfoToPassportSingle() {
        val line = "hgt:179cm"

        val passport = mutableMapOf<String, String>()
        PassportProcessing.putLineInfoToPassport(line, passport)
        with(passport) {
            Assertions.assertThat(size).isEqualTo(1)
            Assertions.assertThat(get("hgt")).isEqualTo("179cm")
            Assertions.assertThat(get("notAKey")).isNull()
        }
    }

    @Test
    fun putLineInfoToPassportMultiple() {
        val line = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd"

        val passport = mutableMapOf<String, String>()
        PassportProcessing.putLineInfoToPassport(line, passport)
        with(passport) {
            Assertions.assertThat(size).isEqualTo(4)
            Assertions.assertThat(get("pid")).isEqualTo("860033327")
            Assertions.assertThat(get("notAKey")).isNull()
        }
    }

    @Test
    fun putLineInfoToPassportEmpty() {
        val line = ""

        val passport = mutableMapOf<String, String>()
        PassportProcessing.putLineInfoToPassport(line, passport)
        with(passport) {
            Assertions.assertThat(size).isEqualTo(0)
            Assertions.assertThat(get("pid")).isNull()
        }
    }

    @Test
    fun passportValid() {
        val passport = listOf<String>()
        """
            ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
            byr:1937 iyr:2017 cid:147 hgt:183cm
        """.trimIndent()
        val invalid = """
            iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
            hcl:#cfa07d byr:1929
        """.trimIndent()
        val northPole = """
            hcl:#ae17e1 iyr:2013
            eyr:2024
            ecl:brn pid:760753108 byr:1931
            hgt:179cm
        """.trimIndent()

        TODO()
    }

    @Test
    fun countNumOfValid() {
        TODO()
    }

    @Test
    fun countNumOfValidFromInput() {
        InputUtil.getListFromString(s) { it }
        TODO()
    }

}
