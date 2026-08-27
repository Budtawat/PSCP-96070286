"""A-E-I-O-U"""


def main():
    """Count and display vowels that appear in the string"""
    text = input().lower()
    vowels = ["a", "e", "i", "o", "u"]

    for vowel in vowels:
        count = text.count(vowel)
        if count:
            print(f"{vowel} : {count}")
main()
