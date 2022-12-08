package adventofcode.day4

import adventofcode.util.InputUtil
import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test

internal class PassportProcessingTest {

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
        val passport = mutableMapOf<String, String>()
        with(passport) {
            put("ecl", "gry")
            put("pid", "860033327")
            put("eyr", "2020")
            put("hcl", "#fffffd")
            put("byr", "1937")
            put("iyr", "2017")
            put("cid", "147")
            put("hgt", "183cm")
        }

        Assertions.assertThat(PassportProcessing.checkPassportValid(passport, '1')).isEqualTo(true)
    }

    @Test
    fun passportInvalid() {
        val invalid = mutableMapOf<String, String>()
        with(invalid) {
            put("hcl", "#ae17e1")
            put("iyr", "2013")
            put("eyr", "2024")
            put("ecl", "brn")
            put("pid", "760753108")
            put("byr", "1931")
        }

        Assertions.assertThat(PassportProcessing.checkPassportValid(invalid, '1')).isEqualTo(false)

    }

    @Test
    fun northPoleValid() {
        val passport = mutableMapOf<String, String>()
        with(passport) {
            put("hcl", "#ae17e1")
            put("iyr", "2013")
            put("eyr", "2024")
            put("ecl", "brn")
            put("pid", "760753108")
            put("byr", "1931")
            put("hgt", "179cm")
        }

        Assertions.assertThat(PassportProcessing.checkPassportValid(passport, '1')).isEqualTo(true)
    }

    @Test
    fun countNumOfValid1() {
        val lines = listOf(
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
            "",
            "hcl:#ae17e1 iyr:2013",
            "eyr:2024",
            "ecl:brn pid:760753108 byr:1931",
            "hgt:179cm",
            "",
            "hcl:#cfa07d eyr:2025 pid:166559648",
            "iyr:2011 ecl:brn hgt:59in"
        )
        val countValid = PassportProcessing.countNumOfValid(lines, '1')
        Assertions.assertThat(countValid).isEqualTo(2)
    }

    @Test
    fun countNumOfValid1FromInput() {
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

        val lines = InputUtil.getListFromString(s) { it }
        val countValid = PassportProcessing.countNumOfValid(lines, '1')
        Assertions.assertThat(countValid).isEqualTo(2)
    }

    @Test
    fun countNumOfValid2FromInputInvalid() {
        val s = """
                eyr:1972 cid:100
                hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
    
                iyr:2019
                hcl:#602927 eyr:1967 hgt:170cm
                ecl:grn pid:012533040 byr:1946
    
                hcl:dab227 iyr:2012
                ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
    
                hgt:59cm ecl:zzz
                eyr:2038 hcl:74454a iyr:2023
                pid:3556412378 byr:2007
        """.trimIndent()
        val lines = InputUtil.getListFromString(s) { it }
        val countValid = PassportProcessing.countNumOfValid(lines, '2')
        Assertions.assertThat(countValid).isEqualTo(0)
    }

    @Test
    fun countNumOfValid2FromInputValid() {
        val s = """
            pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
            hcl:#623a2f

            eyr:2029 ecl:blu cid:129 byr:1989
            iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

            hcl:#888785
            hgt:164cm byr:2001 iyr:2015 cid:88
            pid:545766238 ecl:hzl
            eyr:2022

            iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
        """.trimIndent()
        val lines = InputUtil.getListFromString(s) { it }
        val countValid = PassportProcessing.countNumOfValid(lines, '2')
        Assertions.assertThat(countValid).isEqualTo(3)
    }

}
