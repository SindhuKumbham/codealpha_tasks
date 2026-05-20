# CodeAlpha Data Analytics Internship 🎯

![Python](https://img.shields.io/badge/Python-3.x-blue)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-green)
![pandas](https://img.shields.io/badge/pandas-latest-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 👤 About Me

| Field | Details |
| **Name** | KUMBHAM SINDHU |
| **Internship** | CodeAlpha - Data Analytics |
| **Task** | Task 1 - Web Scraping |
| **Duration** | May 2026 |

---

## 📌 Task 1 - Web Scraping Using Python

### 🎯 Objective
The goal of this task was to use Python libraries like BeautifulSoup and Requests
to extract data from a public website, collect a relevant dataset,
and save it in a structured format for analysis.

---

### 🌐 Website Used

**books.toscrape.com**

This is a public practice website built specifically for web scraping practice.
- No login required
- No restrictions on scraping
- 50 pages of book data
- 1000 books in total

---

### 🛠️ Tools and Libraries Used

| Library | Purpose |
|---|---|
| Python 3 | Main programming language |
| requests | Visits websites and downloads HTML |
| BeautifulSoup4 | Reads and searches through HTML code |
| lxml | Helps BeautifulSoup parse HTML faster |
| pandas | Saves collected data as a CSV file |
| time | Adds delay between page requests |

---

### 📊 Data Collected

For every book, the following information was collected:

| Column Name | Description | Example |
|---|---|---|
| Title | Full name of the book | A Light in the Attic |
| Price (GBP) | Price in British pounds as a number | 51.77 |
| Rating (1-5) | Star rating converted to number | 3 |
| Availability | Whether the book is in stock | In stock |
| Book URL | Direct link to the book detail page | https://books.toscrape.com/... |
| Price Category | Price grouped into ranges | 40 to 60 |

---

### ⚙️ How the Scraper Works

1. The scraper visits page 1 of books.toscrape.com
2. It finds all 20 book cards on that page
3. For each book it extracts the title, price, rating, availability and URL
4. It then looks for the Next page

   
# 📌 Task 2 - Exploratory Data Analysis (EDA)

### 🎯 Objective
The objective of this task was to perform Exploratory Data Analysis (EDA)
on a dataset to understand its structure, discover patterns,
identify missing values, detect relationships between variables,
and generate useful insights using visualizations.

---

### 🛠️ Tools and Libraries Used

| Library | Purpose |
|---|---|
| Python 3 | Main programming language |
| pandas | Data loading and analysis |
| numpy | Numerical operations |
| matplotlib | Data visualization |
| seaborn | Statistical graphs and plots |

---

### 📊 EDA Operations Performed

1. Loaded the dataset using pandas
2. Displayed dataset shape and column information
3. Checked for missing/null values
4. Generated statistical summary of numerical columns
5. Identified duplicate records
6. Analyzed categorical and numerical features
7. Created visualizations for better understanding
8. Observed trends, distributions, and correlations

---

### 📈 Visualizations Created

| Visualization | Purpose |
|---|---|
| Histogram | Shows data distribution |
| Box Plot | Detects outliers |
| Heatmap | Displays feature correlations |
| Count Plot | Shows frequency of categories |
| Scatter Plot | Shows relationships between variables |

---

### 📁 Output Files

| File Name | Description |
|---|---|
| eda.py | Python script for EDA |
| dataset.csv | Dataset used for analysis |
| output graphs | Generated charts and plots |
| README.md | Project documentation |

---

### ▶️ How to Run the Project

1. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
