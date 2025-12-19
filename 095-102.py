import re

text = "ggggG eeeEeee hhhH AAAAa Dddd"

letters = re.findall(r"\b[a-z]*([A-Z])[a-z]*\b", text)
print("".join(letters))

