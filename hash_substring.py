# python3

def read_input():
    # this function acquires input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    source = input().rstrip()
    # read two lines
    # first line is pattern
    # second line is text in which to look for pattern
    if source == 'F':
        with open('test.txt', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = input().rstrip()
        text = input().rstrip()

    # return both lines in one return
    return pattern, text

def print_occurrences(output):
    # this function controls output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function finds the occurrences using Rabin Karp algorithm
    p_len = len(pattern)
    t_len = len(text)
    prime = 10 ** 9 + 7
    multiplier = 31
    power_mod = pow(multiplier, p_len - 1, prime)
    pattern_hash = sum(ord(pattern[i]) * pow(multiplier, i, prime) for i in range(p_len)) % prime
    text_hash = sum(ord(text[i]) * pow(multiplier, i, prime) for i in range(p_len)) % prime
    result = []
    if pattern_hash == text_hash and pattern == text[:p_len]:
        result.append(0)
    for i in range(1, t_len - p_len + 1):
        text_hash = (text_hash - ord(text[i - 1]) * power_mod) % prime
        text_hash = (text_hash * multiplier + ord(text[i + p_len - 1])) % prime
        if pattern_hash == text_hash and pattern == text[i:i + p_len]:
            result.append(i)

    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

