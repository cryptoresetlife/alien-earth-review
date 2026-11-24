"""Alien Field Notes: an alien tourist's one-line review of Earth."""
import os

LINE = (
    "3/5. Locals greet you with 'How are you?' and walk off before the answer. "
    "I answered fully, with diagrams, and am now banned from a dentist's waiting room."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE.strip())
