# 04
# Medium

# Phone Number Mnemonics: Given an N digit phone number, print all the strings that can
# be made from that phone number. Since 1 and 0 don't correspond to any characters, ignore 
# them.

# For example:
# 213 => AD, AE, AF, BD, BE, BF, CE, CE, CF
# 456 => GJM, GJN, GJO, GKM, GKN, GKO,.. etc.


# -----------------------------------------------------

# Time Complexity:​ Exponential Complexity - O(4​n​), where ​n​ is the size of the phone number.
# Space Complexity:​ O(n), where ​n​ is the size of the phone number. The O(n) space is taken both by the buffer 
# and the call stack.

digits_to_letters = {
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
}

def phone_mnemonics_main(fonumbr: str) -> None:
    return phone_mnemonics(fonumbr, 0, [])

def phone_mnemonics(fonumbr: str, fonumbr_i: int, fonumbr_word: list) -> None:
    if fonumbr_i == len(fonumbr):
        print(''.join(fonumbr_word))
        fonumbr_word = []
        return
    digit = fonumbr[fonumbr_i]
    if digit not in digits_to_letters:
        phone_mnemonics(fonumbr, fonumbr_i+1, fonumbr_word)
        return
    for c in digits_to_letters[digit]:
        fonumbr_word.append(c)
        phone_mnemonics(fonumbr, fonumbr_i+1, fonumbr_word)
        fonumbr_word.pop()

# -----------------------------------------------------

phone_mnemonics_main('213')
phone_mnemonics_main('456')
