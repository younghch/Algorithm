package adventofcode.day4

import org.assertj.core.api.Assertions
import org.junit.jupiter.api.Test
import kotlin.random.Random.Default.nextInt


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

    @Test
    fun hgtLower() {
        Assertions.assertThat(Passport.hgt.isValid("149cm")).isFalse
        Assertions.assertThat(Passport.hgt.isValid("150cm")).isTrue

        Assertions.assertThat(Passport.hgt.isValid("58in")).isFalse
        Assertions.assertThat(Passport.hgt.isValid("59in")).isTrue

    }

    @Test
    fun hgtCm() {
        for (i in 0..100)
            Assertions.assertThat(Passport.hgt.isValid(nextInt(150, 193).toString() + "cm")).isTrue
    }

    @Test
    fun hgtIn() {
        for (i in 0..100)
            Assertions.assertThat(Passport.hgt.isValid(nextInt(150, 193).toString() + "cm")).isTrue
    }

    @Test
    fun hgtUpper() {
        Assertions.assertThat(Passport.hgt.isValid("193cm")).isTrue
        Assertions.assertThat(Passport.hgt.isValid("194cm")).isFalse

        Assertions.assertThat(Passport.hgt.isValid("76in")).isTrue
        Assertions.assertThat(Passport.hgt.isValid("77in")).isFalse

    }

    @Test
    fun hcl() {
        Assertions.assertThat(Passport.hcl.isValid("#123abc")).isTrue
        Assertions.assertThat(Passport.hcl.isValid("#123abz")).isFalse
        Assertions.assertThat(Passport.hcl.isValid("#123bc")).isFalse
    }

    @Test
    fun ecl() {
        Assertions.assertThat(Passport.ecl.isValid("brn")).isTrue
        Assertions.assertThat(Passport.ecl.isValid("blue")).isFalse
    }

    @Test
    fun pid() {
        Assertions.assertThat(Passport.pid.isValid("000000001")).isTrue
        Assertions.assertThat(Passport.pid.isValid("0000000012")).isFalse
        Assertions.assertThat(Passport.pid.isValid("000012")).isFalse
    }


}