import random
import time
from analyzer import Analyzer

def read_config(path="simple_analyzer/config/config.txt"):
    settings = {}
    with open(path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            settings[key] = int(value)
    return settings

if __name__ == "__main__":
    cfg = read_config()
    analyzer = Analyzer()
    start_time = time.time()

    while True:
        num = random.randint(1, 100)
        analyzer.add_number(num)
        if len(analyzer.numbers) > cfg["sequence_length"]:
            analyzer.numbers.pop(0)

        print(f"New number: {num}")
        print(f"Even: {analyzer.even_count()}, Odd: {analyzer.odd_count()}")
        print(f"Highest: {analyzer.highest_number()}, Increasing pairs: {analyzer.increasing_pairs()}")
        print("-" * 40)

        current_time = time.localtime()
        if len(analyzer.numbers) >= cfg["sequence_length"] and current_time.tm_sec == 0:
            print("Reached full sequence & full minute — stopping.")
            break

        time.sleep(cfg["interval"])
