# STEP 1: Load the file
with open('raw_text_FF.txt', 'r', encoding='utf-8') as file:
    raw_text = file.read()

# STEP 2: Split into lines and clean
nouvelles = raw_text.split('\n')
cleaned_nouvelles = []

for line in nouvelles:
    cleaned = line.strip()
    if cleaned:  # only keep non-empty lines
        cleaned_nouvelles.append(cleaned)

# STEP 3: Save the cleaned text
with open('cleaned_text_FF.txt', 'w', encoding='utf-8') as out_file:
    for item in cleaned_nouvelles:
        out_file.write(item + '\n')

print(f"{len(cleaned_nouvelles)} cleaned nouvelles saved to cleaned_text_FF.txt")
