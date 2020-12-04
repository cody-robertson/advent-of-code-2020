from typing import Optional


class Passport:
    def __init__(self, property_dictionary):
        self.properties = property_dictionary

    def get_birth_year(self):
        return self.properties.get("byr")

    def get_issue_year(self):
        return self.properties.get("iyr")

    def get_expiration_year(self):
        return self.properties.get("eyr")

    def get_height(self):
        return self.properties.get("hgt")

    def get_hair_color(self):
        return self.properties.get("hcl")

    def get_eye_color(self):
        return self.properties.get("ecl")

    def get_passport_id(self):
        return self.properties.get("pid")

    def get_country_id(self):
        return self.properties.get("cid")

    birth_year: Optional = property(get_birth_year)
    issue_year: Optional = property(get_issue_year)
    expiration_year: Optional = property(get_expiration_year)
    height: Optional = property(get_height)
    hair_color: Optional = property(get_hair_color)
    eye_color: Optional = property(get_eye_color)
    passport_id: Optional = property(get_passport_id)
    country_id: Optional = property(get_country_id)


class PassportValidator:
    def __init__(self):
        self.valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def is_passport_valid(self, passport: Passport) -> bool:
        if not self.is_birth_year_valid(passport.birth_year):
            return False
        elif not self.is_issue_year_valid(passport.issue_year):
            return False
        elif not self.is_expiration_year_valid(passport.expiration_year):
            return False
        elif not self.is_height_valid(passport.height):
            return False
        elif not self.is_eye_color_valid(passport.eye_color):
            return False
        elif not self.is_hair_color_valid(passport.hair_color):
            return False
        elif not self.is_passport_id_valid(passport.passport_id):
            return False
        else:
            return True

    def is_birth_year_valid(self, birth_year: str) -> bool:
        parsed_year = self.try_parse_year_int(birth_year)
        return parsed_year is not None and 1920 <= parsed_year <= 2002

    def is_issue_year_valid(self, issue_year: str) -> bool:
        parsed_year = self.try_parse_year_int(issue_year)
        return parsed_year is not None and 2010 <= parsed_year <= 2020

    def is_expiration_year_valid(self, expiration_year: str) -> bool:
        parsed_year = self.try_parse_year_int(expiration_year)
        return parsed_year is not None and 2020 <= parsed_year <= 2030

    def try_parse_year_int(self, year: str) -> Optional[int]:
        if year is not None and len(year) == 4:
            return self.try_parse_int(year)
        return None

    def is_height_valid(self, height: str) -> bool:
        if height is not None and len(height) > 2:
            unit = height[-2:]
            if unit == "in":
                parsed_height = self.try_parse_int(height[:-2])
                if parsed_height is not None and 59 <= parsed_height <= 76:
                    return True
            elif unit == "cm":
                parsed_height = self.try_parse_int(height[:-2])
                if parsed_height is not None and 150 <= parsed_height <= 193:
                    return True
        return False

    def try_parse_int(self, num: str) -> Optional[int]:
        try:
            return int(num)
        except ValueError:
            pass
        except TypeError:
            pass
        return None

    def is_hair_color_valid(self, hair_color: str) -> bool:
        if hair_color is not None and len(hair_color) == 7 and hair_color[0] == '#':
            parsed_color = self.try_parse_hex(hair_color[1:])
            if parsed_color is not None:
                return True
        return False

    def try_parse_hex(self, hexadecimal: str) -> Optional[int]:
        try:
            return int(hexadecimal, 16)
        except ValueError:
            pass
        except TypeError:
            pass
        return None

    def is_eye_color_valid(self, eye_color: str) -> bool:
        if eye_color is not None and eye_color in self.valid_eye_colors:
            return True
        return False

    def is_passport_id_valid(self, passport_id: str) -> bool:
        if passport_id is not None and len(passport_id) == 9:
            parsed_id = self.try_parse_int(passport_id)
            if parsed_id is not None:
                return True
        return False


if __name__ == "__main__":
    passports: list[Passport] = []
    with open("input.txt") as input_file:
        properties = {}
        for line in input_file:
            line = line.strip()
            if line == "":
                passports.append(Passport(properties))
                properties = {}
            else:
                pairs = line.split(" ")
                for pair in pairs:
                    key, value = pair.split(":")
                    properties[key] = value
        if len(properties) > 0:
            passports.append(Passport(properties))
    program = PassportValidator()
    valid_count = 0
    for passport_item in passports:
        if program.is_passport_valid(passport_item):
            valid_count += 1
    print("Total Passports:", len(passports))
    print("Valid Passports:", valid_count)
    print("Invalid Passports:", len(passports)-valid_count)
