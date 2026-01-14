import math

def get_handfuls(num_smarties, handful_size):
    """
    Given the number of Smarties of one non-red color and the maximum handful size,
    return how many handfuls are needed.
    """
    return math.ceil(num_smarties / handful_size)


def get_time_for_non_red_color(num_smarties, handful_size, seconds_per_handful):
    """
    Return the time (in seconds) to eat all Smarties of a single non-red color.
    """
    handfuls = get_handfuls(num_smarties, handful_size)
    return handfuls * seconds_per_handful


def get_time_for_red_smarties(num_red, seconds_per_red):
    """
    Return the time (in seconds) to eat all the red Smarties.
    """
    return num_red * seconds_per_red


def get_box_time(color_counts, handful_size, seconds_per_handful, seconds_per_red):
    """
    Given a dictionary of color -> count, return total time (in seconds)
    to eat the whole box following the rules.
    """
    total_time = 0

    for color, count in color_counts.items():
        if color == "red":
            total_time += get_time_for_red_smarties(count, seconds_per_red)
        else:
            total_time += get_time_for_non_red_color(count, handful_size, seconds_per_handful)

    return total_time


def read_one_box():
    """
    Reads lines for ONE test case (one box) until we see 'end of box'.
    Returns a dictionary mapping color -> count.
    If EOF is reached before any color, returns None.
    """
    color_counts = {}
    started = False

    while True:
        try:
            line = input().strip()
        except EOFError:
            # If we never read anything at all, signal end of input
            if not started:
                return None
            else:
                break

        if line == "end of box":
            break

        started = True
        # Count this color
        color_counts[line] = color_counts.get(line, 0) + 1

    return color_counts


def main():
    HANDFUL_SIZE = 7
    SECONDS_PER_HANDFUL = 13
    SECONDS_PER_RED = 16

    # The problem says there are 10 test cases
    for _ in range(10):
        color_counts = read_one_box()
        if color_counts is None:
            break  # No more input

        total_time = get_box_time(
            color_counts,
            HANDFUL_SIZE,
            SECONDS_PER_HANDFUL,
            SECONDS_PER_RED
        )
        print(total_time)


if __name__ == "__main__":
    main()
