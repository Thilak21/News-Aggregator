import requests
from bs4 import BeautifulSoup

def get_hindu_news():
    url = 'https://www.thehindu.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    
    # Find headlines and their corresponding links
    for item in soup.find_all('h3'):
        link = item.find('a')  # Find the <a> tag inside the <h2> tag
        if link:
            headline = link.get_text(strip=True)  # Get the headline text
            url = link.get('href')  # Get the link URL
            headlines.append((headline, url))
    
    return headlines


def get_ie_news():
    url = 'https://www.indianexpress.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []


    for item in soup.find_all('h3'):
        link = item.find('a')
        if link:
            headline = link.get_text(strip=True)
            url = link.get('href')
            headlines.append((headline, url))
            
    return headlines        

def main():
    print("News Aggregator")
    print("================")
    
    # Fetch Times of India headlines
    hindu_headlines = get_hindu_news()
    print("The Hindu News Headlines:")
    for headline, link in hindu_headlines[:5]:  # Display top 5 headlines with links
        print(f"- {headline} (Link: {link})")
        
    
    ie_headlines = get_ie_news()
    print("\nIndian Express News Headlines:")
    for headline, link in ie_headlines[:5]:
        print(f"- {headline}  (Link: {link})")

if __name__ == "__main__":
    main()





















    
