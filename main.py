# One Line, One Laugh entry for make.fun.
# Writes one funny line (at most 200 characters) to /output/entry.txt.
# Python 3.13, no dependencies.
import os

LINE = "My phone shamed me with my screen time, so now I check my screen time on my tablet."

# The gate only accepts UTF-8 text of 1 to 200 characters, not only
# whitespace. Fail loudly instead of writing an entry that cannot win.
if not LINE.strip() or len(LINE) > 200:
    raise SystemExit(f"Line must be 1-200 characters, got {len(LINE)}.")

if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read back and confirm the file holds exactly the line, so a partial
    # or failed write cannot pass silently.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("Wrote /output/entry.txt but its content differs.")
    print(f"Wrote {len(LINE)}-character line to /output/entry.txt")
