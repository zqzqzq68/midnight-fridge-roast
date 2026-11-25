"""Midnight Fridge Roast entry.

Writes one roast line to /output/entry.txt and prints it to stdout.

The line is fixed, so every run produces byte-identical output.
"""

ROAST = (
    "My fridge locks at midnight like my leftovers are state secrets -- "
    "relax, it's Tuesday's pizza in there, not the nuclear codes."
)


def main() -> None:
    import os

    if not 1 <= len(ROAST) <= 200:
        raise ValueError("roast must be 1 to 200 characters")
    if "\n" in ROAST:
        raise ValueError("roast must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST)
    print(ROAST)


if __name__ == "__main__":
    main()
