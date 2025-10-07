def main(kvpair: tuple) -> tuple:
    word, counts = kvpair
    return (word, sum(counts))