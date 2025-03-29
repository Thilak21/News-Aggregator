## News Aggregator - Python Web Scraping

## Project Overview
             This Python-based News Aggregator scrapes headlines from multiple news websites, including **The Hindu** and **The Indian Express**. Using libraries such as `requests` and
`BeautifulSoup`, this tool fetches the latest news and displays it in a clean and simple format. The aggregator extracts headlines and links from each website and provides users with the top 5 news articles. This script can be expanded to include more news sources, categories, or customized filters.

## Features
- **Web Scraping**: Automatically fetches news headlines from popular Indian news sources like The Hindu and Indian Express.
- **BeautifulSoup Parsing**: Uses BeautifulSoup to extract headline text and links from the websites.
- **Multi-Source Support**: Currently aggregates news from The Hindu and The Indian Express, with the option to add more sources.
- **Simple Output**: Displays the latest headlines in the terminal with clickable links.
- **Extendable**: Easily add more websites or modify the current scraping logic for different layouts.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

### Installation
To install the required libraries, you can use pip:

       pip install requests beautifulsoup4


## How It Works
1. **Fetching News**: The script uses `requests` to fetch the HTML content of the news websites.
2. **Parsing Content**: `BeautifulSoup` is used to parse and extract relevant information (headlines and URLs) from the page.
3. **Displaying Output**: The top 5 headlines from each source are displayed in the terminal, with clickable links to read more.


## How to Run
1. Clone the repository:
    
    git clone https://github.com/yourusername/news-aggregator.git
   
    cd news-aggregator
    

3. Install the libraries:

         pip install requests beautifulsoup4


4. Run the script:
   
    python news_aggregator.py
 

## Conclusion
         The News Aggregator project is a simple yet powerful tool to gather and display the latest headlines from popular news sources like The Hindu and The Indian Express. By utilizing Python’s requests and BeautifulSoup libraries, this script offers an easy way to aggregate news in a clean and readable format.
