import sys
import re
from collections import defaultdict


def load_config(config_file):
    replacements = {}
    with open(config_file, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            replacements[key] = value
    return replacements


def replace_values(text, replacements):
    statistics = defaultdict(int)

    for key, value in replacements.items():
        text = re.sub(re.escape(key), value, text)
        statistics[key] += text.count(value)

    return text, statistics


def main(config_file, text_file):
    replacements = load_config(config_file)

    with open(text_file, 'r') as file:
        text = file.read()

    modified_text, stats = replace_values(text, replacements)

    sorted_stats = sorted(stats.items(), key=lambda item: -item[1])

    print("modified text:")
    for line in modified_text.splitlines():
        print(line)

    print("\nSubstitution statistics (from the most changed):")
    for key, count in sorted_stats:
        print(f"{key} : {count} replace")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <config_file> <text_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    text_file = sys.argv[2]

    main(config_file, text_file)