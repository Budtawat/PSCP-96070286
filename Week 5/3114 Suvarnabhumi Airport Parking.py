"""Suvarnabhumi Airport Parking"""


def main():
    """Calculate parking fee based on entry and exit time"""
    entry_raw = input().strip()
    exit_raw = input().strip()

    if "." not in entry_raw or "." not in exit_raw:
        print("ERROR")
        return
    in_h_str, in_m_str = entry_raw.split(".")
    out_h_str, out_m_str = exit_raw.split(".")

    in_h, in_m = int(in_h_str), int(in_m_str)
    out_h, out_m = int(out_h_str), int(out_m_str)
    if not (0 <= in_h <= 24 and 0 <= in_m < 60) or (in_h == 24 and in_m > 0):
        print("ERROR")
        return
    if not (0 <= out_h <= 24 and 0 <= out_m < 60) or (out_h == 24 and out_m > 0):
        print("ERROR")
        return
    entry_total_mins = (in_h * 60) + in_m
    exit_total_mins = (out_h * 60) + out_m
    diff_mins = exit_total_mins - entry_total_mins
    if diff_mins < 0 or diff_mins > 1440:
        print("ERROR")
        return
    if diff_mins <= 15:
        print("FREE")
        return
    hours = (diff_mins + 59) // 60
    rates = {
        1: 25,
        2: 50,
        3: 80,
        4: 110,
        5: 145,
        6: 180,
    }

    if 1 <= hours <= 6:
        print(rates[hours])
    elif 7 <= hours <= 24:
        print(250)
    else:
        print("ERROR")
main()
