"""Train Station."""


def parse_times(raw_text):
    """Parse list of time strings to minutes from midnight."""
    cleaned = raw_text.strip().strip("[]")
    times = []
    if not cleaned:
        return times

    for item in cleaned.split(","):
        val = item.strip().strip("'\"")
        if val:
            parts = val.split(".")
            hours = int(parts[0])
            minutes = int(parts[1].ljust(2, "0"))
            times.append(hours * 60 + minutes)

    return times


def find_platforms(arr_times, dep_times):
    """Calculate minimum platforms needed."""
    events = []
    for arr_t, dep_t in zip(arr_times, dep_times):
        events.append((arr_t, 0))
        events.append((dep_t, 1))

    events.sort()

    curr_count = 0
    max_count = 0

    for _, is_departure in events:
        if not is_departure:
            curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
        else:
            curr_count -= 1

    return max_count


def main():
    """Run program."""
    arr_times = parse_times(input())
    dep_times = parse_times(input())
    print(find_platforms(arr_times, dep_times))


main()
