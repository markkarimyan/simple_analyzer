def read_config(path="simple_analyzer/config/config.txt"):
    settings = {}
    with open(path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            settings[key] = int(value)
    return settings

if __name__ == "__main__":
    cfg = read_config()
    print(f"Interval: {cfg['interval']}, Sequence Length: {cfg['sequence_length']}")
