import os

TEXT = "The lighthouse keeper still lights the lamp for a ship that sank thirty years ago. Last Tuesday, someone on the water answered back."


def main():
    # Standard library only, no network: write exactly one text.
    output_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
