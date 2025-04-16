import spacy
import csv

# Load French language model
nlp = spacy.load('fr_core_news_md')

# Load the cleaned text file
with open('data/cleaned_text_FF.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Prepare a list to hold results
results = []

# Process each nouvelle
for line in lines:
    doc = nlp(line.strip())
    locations = [ent.text for ent in doc.ents if ent.label_ == 'LOC']
    results.append({'text': line.strip(), 'locations': locations})

# Save to CSV with BOM for correct Excel display
with open('data/nouvelles_with_locations.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
    fieldnames = ['text', 'locations']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in results:
        writer.writerow({
            'text': item['text'],
            'locations': '; '.join(item['locations'])
        })

print(f"{len(results)} nouvelles processed. Results saved to nouvelles_with_locations.csv.")
