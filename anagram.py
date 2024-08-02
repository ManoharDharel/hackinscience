import unicodedata


def remove_diacritics(input_str):
    normalized_str = unicodedata.normalize('NFD', input_str)
    return ''.join(char for char in normalized_str if not unicodedata.combining(char))


def is_anagram(str1, str2):
    # Remove diacritics and convert to lower case
    str1 = remove_diacritics(str1).lower()
    str2 = remove_diacritics(str2).lower()

    # Remove non-alphanumeric characters
    str1 = ''.join(char for char in str1 if char.isalnum())
    str2 = ''.join(char for char in str2 if char.isalnum())

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)


# Examples
print(is_anagram("funeral", "real fun"))  # True
print(is_anagram("Madam Curie", "Radium came"))  # True
print(is_anagram("crâné", "crane"))  # True
print(is_anagram("hello", "world"))  # False
