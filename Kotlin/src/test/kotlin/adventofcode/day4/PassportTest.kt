package adventofcode.day4

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test
import kotlin.random.Random.Default.nextInt


//byr (Birth Year) - four digits; at least 1920 and at most 2002.
//iyr (Issue Year) - four digits; at least 2010 and at most 2020.
//eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
//hgt (Height) - a number followed by either cm or in:
//If cm, the number must be at least 150 and at most 193.
//If in, the number must be at least 59 and at most 76.
//hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
//ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
//pid (Passport ID) - a nine-digit number, including leading zeroes.
//cid (Country ID) - ignored, missing or not.

internal class PassportTest {

    @Test
    fun byrLower() {
        Assertions.assertThat(Passport.byr.isValid("1919")).isFalse
        Assertions.assertThat(Passport.byr.isValid("1920")).isTrue
    }

    @Test
    fun byr1921to2000() {
        for (i in 0..100)
            Assertions.assertThat(Passport.byr.isValid(nextInt(1921, 2003).toString())).isTrue
    }

    @Test
    fun byrUpper() {
        Assertions.assertThat(Passport.byr.isValid("2002")).isTrue
        Assertions.assertThat(Passport.byr.isValid("2003")).isFalse
    }

    @Test
    fun byrInvalid() {
        Assertions.assertThat(Passport.byr.isValid("3")).isFalse
        Assertions.assertThat(Passport.byr.isValid("1950hi")).isFalse
        Assertions.assertThat(Passport.byr.isValid("h1950")).isFalse
        Assertions.assertThat(Passport.byr.isValid("")).isFalse
        Assertions.assertThat(Passport.byr.isValid("19501")).isFalse
    }

}