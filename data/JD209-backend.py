import random
import array

class Backend():
    def __init__(self):
        self.DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', ';', ',', '>', '}', '{', '[', ']', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '`', '+', '-', '_']
    
    def generate_password(self, length: int, locase: bool, upcase: bool, symbols: bool) -> str:
        COMBINED_LIST = self.DIGITS
        rand_digit = random.choice(self.DIGITS)
        temp_pass = rand_digit
        temp_pass_len = 1

        if locase == True:
            rand_locase = random.choice(self.LOCASE_CHARACTERS)
            temp_pass = temp_pass + rand_locase
            temp_pass_len += 1
            COMBINED_LIST = COMBINED_LIST + self.LOCASE_CHARACTERS

        if upcase == True:
            rand_upcase = random.choice(self.UPCASE_CHARACTERS)
            temp_pass = temp_pass + rand_upcase
            temp_pass_len += 1
            COMBINED_LIST = COMBINED_LIST + self.UPCASE_CHARACTERS

        if symbols == True:
            rand_symbol = random.choice(self.SYMBOLS)
            temp_pass = temp_pass + rand_symbol
            temp_pass_len += 1
            COMBINED_LIST = COMBINED_LIST + self.SYMBOLS

        for x in range(length - temp_pass_len):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)

            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)

        password = ""
        for x in temp_pass_list:
                password = password + x

        return password