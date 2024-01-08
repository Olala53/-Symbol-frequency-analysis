import sys
from collections import Counter
import math


def calculate_entropy(frequencies):
    total_symbols = sum(frequencies.values())
    probabilities = {symbol: count / total_symbols for symbol, count in frequencies.items()}
    entropy = -sum(p * math.log2(p) for p in probabilities.values())
    return entropy


def letters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            frequencies = Counter(text)
            total_symbols = sum(frequencies.values())

            print("Symbol frequencies:")
            for symbol, count in frequencies.items():
                probability = count / total_symbols
                print(f"{symbol} {probability:.3f}")

            entropy = calculate_entropy(frequencies)
            print(f"\nBinary entropy: {entropy:.3f}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py <file_path>")
    else:
        file_path = sys.argv[1]
        letters(file_path)
