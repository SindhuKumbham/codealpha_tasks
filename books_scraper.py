# ============================================================
#   CodeAlpha Internship Task - Web Scraping
#   Website : https://books.toscrape.com (all 50 pages)
#   Output  : books_dataset.csv
#   How to run : python books_scraper.py
# ============================================================


# STEP 1 - Import the libraries we need
import requests                   # visits websites for us
from bs4 import BeautifulSoup     # reads and searches HTML
import pandas as pd               # saves data as CSV file
import time                       # lets us pause between pages


# STEP 2 - Settings (you can change these if needed)
BASE_URL  = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
DELAY     = 1    # wait 1 second between each page


# STEP 3 - Convert rating words to numbers
RATING_MAP = {
    "One"  : 1,
    "Two"  : 2,
    "Three": 3,
    "Four" : 4,
    "Five" : 5,
}


# ============================================================
# FUNCTION 1 - Scrape one page and return list of books
# ============================================================
def scrape_page(url):

    # Visit the page
    response = requests.get(url)

    # If page did not load, skip it
    if response.status_code != 200:
        print("  Could not load page:", url)
        return []

    # Read the HTML
    soup  = BeautifulSoup(response.text, "lxml")

    # Find all book cards on the page
    books = soup.find_all("article", class_="product_pod")

    # Loop through each book and collect data
    page_data = []

    for book in books:

        # Get the title
        title = book.h3.a["title"]

        # Get the price and remove the pound symbol
        price_text = book.find("p", class_="price_color").text
        price = float(price_text.replace("£", "").replace("Â", "").strip())

        # Get the star rating and convert to number
        rating_word = book.p["class"][1]
        rating      = RATING_MAP.get(rating_word, 0)

        # Get availability (In stock / Out of stock)
        availability = book.find("p", class_="availability").text.strip()

        # Build the full URL for this book's detail page
        relative_link = book.h3.a["href"]
        clean_link    = relative_link.replace("../../../", "")
        full_link     = BASE_URL + clean_link

        # Add this book to our list
        page_data.append({
            "Title"        : title,
            "Price (GBP)"  : price,
            "Rating (1-5)" : rating,
            "Availability" : availability,
            "Book URL"     : full_link,
        })

    return page_data


# ============================================================
# FUNCTION 2 - Find the next page URL
# ============================================================
def get_next_page_url(soup):

    # Look for the Next button at the bottom of the page
    next_button = soup.find("li", class_="next")

    if next_button:
        next_href = next_button.a["href"]
        return BASE_URL + next_href

    # No next button means we are on the last page
    return None


# ============================================================
# FUNCTION 3 - Loop through ALL 50 pages
# ============================================================
def scrape_all_pages():

    all_books   = []
    current_url = START_URL
    page_number = 1

    print("=" * 55)
    print("  CodeAlpha Internship - Web Scraping Task")
    print("  Website : books.toscrape.com")
    print("  Scraping all 50 pages - please wait...")
    print("=" * 55)

    while current_url:

        print(f"  Scraping page {page_number} of 50 ...")

        # Scrape this page
        books_on_this_page = scrape_page(current_url)
        all_books.extend(books_on_this_page)

        # Load the same page again to find the next page link
        response = requests.get(current_url)
        soup     = BeautifulSoup(response.text, "lxml")
        next_url = get_next_page_url(soup)

        # Move to the next page
        current_url  = next_url
        page_number += 1

        # Wait 1 second before loading next page
        time.sleep(DELAY)

    return all_books


# ============================================================
# FUNCTION 4 - Save all data to CSV file
# ============================================================
def save_to_csv(all_books):

    # Convert list to a table (DataFrame)
    df = pd.DataFrame(all_books)

    # Add a Price Category column
    df["Price Category"] = pd.cut(
        df["Price (GBP)"],
        bins   = [0, 10, 20, 40, 60, 100],
        labels = ["Under 10", "10 to 20", "20 to 40", "40 to 60", "Over 60"]
    )

    # Save to CSV file
    df.to_csv("books_dataset.csv", index=False)

    # Print summary
    print()
    print("=" * 55)
    print("  DONE! Your dataset is ready.")
    print("=" * 55)
    print(f"  Total books collected  : {len(df)}")
    print(f"  Average price          : GBP {df['Price (GBP)'].mean():.2f}")
    print(f"  Cheapest book          : GBP {df['Price (GBP)'].min():.2f}")
    print(f"  Most expensive book    : GBP {df['Price (GBP)'].max():.2f}")
    print(f"  5-star rated books     : {(df['Rating (1-5)'] == 5).sum()}")
    print(f"  1-star rated books     : {(df['Rating (1-5)'] == 1).sum()}")
    print()
    print("  File saved as : books_dataset.csv")
    print("  Open it in Excel or Google Sheets to see your data!")
    print("=" * 55)

    # Show a small preview of first 5 books
    print()
    print("  Preview of first 5 books:")
    print()
    print(df[["Title", "Price (GBP)", "Rating (1-5)"]].head().to_string(index=False))
    print()


# ============================================================
# RUN EVERYTHING
# ============================================================
if __name__ == "__main__":
    all_books = scrape_all_pages()
    save_to_csv(all_books)