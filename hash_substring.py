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
    # This function finds the occurrences of pattern in text using Rabin Karp's algorithm.

    p = 1000000007  # A large prime number
    x = random.randint(1, p - 1)  # A random integer between 1 and p-1
    result = []

    def poly_hash(s):
        """Function to calculate the polynomial hash of string s."""
        hash_value = 0
        for char in reversed(s):
            hash_value = (hash_value * x + ord(char)) % p
        return hash_value

    # Precompute hashes for all substrings of length |pattern| in text
    h = [0] * (len(text) - len(pattern) + 1)
    h[-1] = poly_hash(text[-len(pattern):])
    y = 1
    for i in range(len(pattern)):
        y = (y * x) % p
    for i in range(len(text) - len(pattern) - 1, -1, -1):
        h[i] = (x * h[i + 1] + ord(text[i]) - y * ord(text[i + len(pattern)])) % p

    # Calculate the hash of pattern
    pattern_hash = poly_hash(pattern)

    # Compare the hash of pattern to the hashes of all substrings of length |pattern| in text
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash != h[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)

    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

