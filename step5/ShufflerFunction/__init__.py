from collections import defaultdict

def main(mapoutput: list) -> dict:
    shuffle_output = defaultdict(list)
    for word, count in mapoutput:
        shuffle_output[word].append(count)
    return shuffle_output