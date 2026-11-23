import os

TEXT = "The lighthouse keeper still lights the lamp for a ship that sank thirty years ago. Last Tuesday, someone on the water answered back."

def main():
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        # Probe writability; if it fails, fall back to a local output dir.
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEXT)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEXT)

if __name__ == "__main__":
    main()
