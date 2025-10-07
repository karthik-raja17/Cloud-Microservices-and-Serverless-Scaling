def main(kvpair: tuple) -> list:
    line_number, line = kvpair
    words = line.split()
    return [(word, 1) for word in words]