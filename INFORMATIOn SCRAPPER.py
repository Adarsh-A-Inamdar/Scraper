import requests
from bs4 import BeautifulSoup
import nltk

# Download NLTK data (you only need to do this once)
nltk.download('punkt')

# Define a function to scrape and process data
def scrape_and_display(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the text content from the webpage
            text = soup.get_text()

            # Tokenize the text into sentences using NLTK
            sentences = nltk.sent_tokenize(text)

            # Display the sentences
            for idx, sentence in enumerate(sentences, start=1):
                print(f"Sentences {idx}: {sentence}\n")

        else:
            print(f"Failed to retrieve data from {url}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage: Provide the URL of the website you want to scrape
website_url = input('https://example.com')  # Replace with your desired URL
scrape_and_display(website_url)
