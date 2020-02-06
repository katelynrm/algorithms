morse_dict = {
    "A": "* ***",
    "B": "*** * * *",
    "C": "*** * *** *",
    "D": "*** * *",
    "E": "*",
    "F": "* * *** *",
    "G": "*** *** *",
    "H": "* * * *",
    "I": "* *",
    "J": "* *** *** ***",
    "K": "*** * ***",
    "L": "* *** * *",
    "M": "*** ***",
    "N": "*** *",
    "O": "*** *** ***",
    "P": "* *** *** *",
    "Q": "*** *** * ***",
    "R": "* *** *",
    "S": "* * *",
    "T": "***",
    "U": "* * ***",
    "V": "* * * ***",
    "W": "* *** ***",
    "X": "*** * * ***",
    "Y": "*** * *** ***",
    "Z": "*** *** * *",
    " ": "       ",
}


# def translate_to_and_from_morse(phrase):
#     translated = []
#     morse_word_break = " " * 7
#     morse_letter_break = " " * 3

#     if phrase[0].isalpha():
#         phrase_list = list(phrase.upper())
#         previous_character = ""

#         for character in phrase_list:
#             if previous_character.isalpha() and character.isalpha():
#                 translated.append(morse_letter_break)

#             translated.append(morse_dict[character])
#             previous_character = character
#     else:
#         word_list = phrase.split(morse_word_break)
#         previous_word = ""
#         for word in word_list:
#             letters = word.split(morse_letter_break)
#             if previous_word != "":
#                 translated.append(" ")
#             previous_word = word
#             for letter in letters:
#                 for k, v in morse_dict.items():
#                     if letter == v:
#                         translated.append(k)

#     return "".join(translated)


morse_word_break = " " * 7
morse_letter_break = " " * 3


def translate_into_english(morse_phrase):
    translated = []
    previous_word = ""
    word_list = morse_phrase.split(morse_word_break)

    for word in word_list:
        letters = word.split(morse_letter_break)
        if previous_word != "":
            translated.append(" ")
        previous_word = word
        for letter in letters:
            for k, v in morse_dict.items():
                if letter == v:
                    translated.append(k)
    return "".join(translated)


def translate_into_morse(english_phrase):
    translated = []
    previous_character = ""
    phrase_list = list(english_phrase.upper())

    for character in phrase_list:
        if previous_character.isalpha() and character.isalpha():
            translated.append(morse_letter_break)
        translated.append(morse_dict[character])
        previous_character = character
    return "".join(translated)


def translate_to_and_from_morse(phrase):
    if phrase[0].isalpha():
        return translate_into_morse(phrase)
    else:
        return translate_into_english(phrase)


hidden_message = "*** * *** *   * ***   ***   * * *       * ***   * *** *   *       *** * *** *   *** *** ***   *** *** ***   * *** * *"
eng_message = "CATS ARE COOL"
print(translate_to_and_from_morse(eng_message))
