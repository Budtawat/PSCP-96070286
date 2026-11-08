"""Solar System."""


def get_first_word(text):
    """Get the first word of a string."""
    if " " in text:
        return text[: text.index(" ")]
    return text


def get_last_word(text):
    """Get the last word of a string."""
    if " " in text:
        return text[text.rindex(" ") + 1 :]
    return text


def determine_hot(left_str, right_str, left_cnt, right_cnt):
    """Determine hottest planets."""
    if left_cnt > 0 and right_cnt > 0:
        return get_last_word(left_str) + " " + get_first_word(right_str)
    if left_cnt > 0:
        return get_last_word(left_str)
    return get_first_word(right_str)


def determine_cool(left_str, right_str, left_cnt, right_cnt):
    """Determine coolest planets."""
    if left_cnt > right_cnt:
        return get_first_word(left_str)
    if right_cnt > left_cnt:
        return get_last_word(right_str)
    return get_first_word(left_str) + " " + get_last_word(right_str)


def main():
    """Run solar system planet analysis."""
    text = input().strip()
    padded = " " + text + " "
    sun_idx = padded.index(" Sun ")

    left_str = padded[:sun_idx].strip()
    right_str = padded[sun_idx + 5 :].strip()

    left_cnt = left_str.count(" ") + 1 if left_str else 0
    right_cnt = right_str.count(" ") + 1 if right_str else 0

    hot_planets = determine_hot(left_str, right_str, left_cnt, right_cnt)
    cool_planets = determine_cool(left_str, right_str, left_cnt, right_cnt)

    print("Hot:", hot_planets)
    print("Cool:", cool_planets)


main()
