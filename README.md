# 📄 **PaperStatsExtractor – Research Paper Statistics Extractor**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-green)
![Requests](https://img.shields.io/badge/HTTP-Requests-orange)
![CSV](https://img.shields.io/badge/Output-CSV-yellow)
![Status](https://img.shields.io/badge/Status-Prototype-lightgrey)

---

## ✨ Overview

**PaperStatsExtractor** is a Python-based web scraping project that extracts useful statistics from a research paper page and saves the results into CSV files.

The project currently scrapes a Nature research article, extracts paper-level statistics, and collects reference information. The repository contains one main Python script, `chanllenge.py`, along with generated CSV outputs: `paper_stats.csv` and `references.csv`.

---

## 🎯 Problem Statement

Research papers often contain useful metadata and structural information, but manually collecting paper statistics and references can be time-consuming.

This project automates that process by extracting:

- Paper title
- Number of words in the abstract
- Number of words in the body
- Number of images
- Reference text
- Reference links

---

## 💡 Solution: PaperStatsExtractor

| Feature | Description |
|---------|-------------|
| 🔗 **Article Scraping** | Uses `requests` to fetch the research article webpage. |
| 🧾 **HTML Parsing** | Uses `BeautifulSoup` to parse article sections, title, images, and references. |
| 🔢 **Word Counting** | Counts words in the abstract and body after removing punctuation. |
| 🖼️ **Image Counting** | Counts article figures/images from selected HTML elements. |
| 📚 **Reference Extraction** | Extracts reference text and available reference links. |
| 📁 **CSV Export** | Saves paper statistics and references into separate CSV files. |

---

## 🧰 Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Language** | Python |
| **Web Requests** | Requests |
| **HTML Parsing** | BeautifulSoup |
| **Data Output** | CSV |
| **Target Source** | Nature research article page |

---

## 🏗️ Project Workflow

```text
Research Paper URL
        ↓
Fetch Webpage with Requests
        ↓
Parse HTML with BeautifulSoup
        ↓
Extract Title, Abstract, Body, Images, and References
        ↓
Clean Text and Count Words
        ↓
Save Paper Statistics to paper_stats.csv
        ↓
Save References to references.csv
```

---

## 📁 Project Structure

```text
PaperStatsExtractor/
├── README.md
├── chanllenge.py
├── paper_stats.csv
└── references.csv
```

---

## 🔑 Core Files

| File | Purpose |
|------|---------|
| `chanllenge.py` | Main scraping script that extracts paper statistics and references. |
| `paper_stats.csv` | Stores extracted paper-level statistics. |
| `references.csv` | Stores extracted reference text and reference links. |
| `README.md` | Minimal project README. |

---

## 📊 Output Files

### `paper_stats.csv`

Stores summary statistics for the scraped paper.

Example output includes the paper title, abstract word count, body word count, and number of images.

```text
title,no of words in abstract,no of words in body,no of images
Enhanced bacterial clearance in early secondary sepsis in a porcine intensive care model,182,2998,3
```

### `references.csv`

Stores extracted references from the article, including reference text and available links.

```text
reference text,reference links
Singer, M. et al. The third international consensus definitions for sepsis and septic shock...
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/lekshman-babu/PaperStatsExtractor.git
cd PaperStatsExtractor
```

### 2️⃣ Install Dependencies

```bash
pip install requests beautifulsoup4 lxml
```

### 3️⃣ Run the Script

```bash
python chanllenge.py
```

After running the script, the following CSV files are generated or updated:

```text
paper_stats.csv
references.csv
```

---

## 📌 Features

- Scrapes a research article webpage
- Extracts article title
- Counts words in the abstract
- Counts words in the body
- Counts article images
- Extracts reference text
- Extracts reference links when available
- Exports results to CSV files

---

## 🚀 Use Cases

- Research paper metadata extraction
- Academic reference collection
- Web scraping practice
- CSV data generation
- Text processing practice
- Beginner-friendly Python automation project

---

## 🔮 Future Improvements

- Add support for custom article URLs
- Add command-line arguments
- Improve error handling for missing HTML sections
- Support multiple research papers in one run
- Save output as JSON in addition to CSV
- Add pandas-based analysis
- Add `requirements.txt`
- Rename `chanllenge.py` to `challenge.py`
- Add tests for word counting and reference extraction
- Support more publishers beyond Nature

---

## 🧑‍💻 Author

**Lekshman Babu**

---

## 🪪 License

No license file is currently included. Add a license before using or distributing the project publicly.

---

> 📄 *PaperStatsExtractor automates research article analysis by scraping paper statistics and references into structured CSV files.*
