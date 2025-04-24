# Félix Fénéon Digital Edition

*A Digital Humanities Project by Vicky Liakopoulou*  
✒️ *A born-digital, semantically enriched edition of* **Nouvelles en trois lignes** *(1906)*

---

## 🎯 Overview

This project presents a digital edition of **Félix Fénéon’s** micro-stories originally published in *Le Matin* in 1906. It is not simply a transcription — it is a **computationally structured intellectual edition**, connecting literature, geography, metadata, and political history.

Through custom metadata, geolocation, and future NLP integration, this repository forms the foundation for:

- 💡 Close reading and distant reading
- 🌍 Geospatial storytelling
- 🧩 Linked open data (LOD) ontologies
- 📚 Historical contextualization
- 🤖 Semantic enrichment and machine-readable texts

---

## ✨ Features (So Far)

- 🛠️ Django-based interface for uploading and editing nouvelles
- 🗂️ Custom metadata schema for people, places, events, institutions, etc.
- 🌐 Geonames API integration for automated geolocation
- 🧭 Static homepage with historical sketch and navigation
- 🎨 Typography and visual styling using Cormorant Garamond
- 🧠 Metadata typology designed for NLP + CIDOC CRM integration
- 📁 Manual correction of 1,300+ entries underway with entity tagging

---

## 🗂️ File Structure

```
├── feneon_site/             # Django core config  
├── feneon/                  # Django app: models, views, admin, templates  
├── data/                    # CSV files, Geonames extractions  
├── scripts/                 # Python tools for API, NLP, and validation  
├── static/feneon/           # Portraits, CSS, homepage visuals  
├── db.sqlite3               # SQLite DB (dev mode)  
├── FF_step_by_step.docx     # Daily project log  
├── Feneon_Metadata_Typology_v0.1.docx # Living schema  
```



---

## 🧭 Vision

The goal is to build the **ultimate guide** to *Nouvelles en trois lignes*:

- Link every story to its **original source** in *Le Matin* via BnF archives
- Display every location on an **interactive map**
- Annotate entities with context, from **crime statistics to political unrest**
- Allow **thematic exploration** via filters and search
- Structure everything with a **semantic ontology** suitable for LOD, RDF, and TEI

---

## 🧠 In Development

This project is in **active development** and currently maintained privately.  
Features coming soon:

- 📊 NLP: sentiment, frequency, and syntactic analysis
- 🗺️ Map-based browsing of Fénéon’s France (and colonies)
- 🔗 Link-outs to BnF, Wikipedia, and Wikidata for historical context
- 🕰️ Timeline of political, military, and cultural references

---

## 📬 Author

**Vicky Liakopoulou**  
Digital Humanist | Research Software Engineer  
Project Lead, Developer, and Metadata Architect  
[GitHub Profile](https://github.com/VickyLiakopoulou11)

---

## 👀 How to Access

This repository is currently private for development.  
If you're an employer, researcher, or reviewer, feel free to request access by contacting the author.

---

