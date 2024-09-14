import requests
from bs4 import BeautifulSoup

# URL of the article page
url = 'https://vnexpress.net/hon-23-trieu-hoc-sinh-buoc-vao-nam-hoc-moi-4788964.html'

try:
    # Request the article page
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the article title
    title_tag = soup.find('h1')  # Assuming the title is inside an <h1> tag
    title = title_tag.get_text(strip=True) if title_tag else "No title found"

    # Find the article content
    article_tag = soup.find('article')  # Adjust if the tag/class is different

    # Try to find the posted date
    date_tag = soup.find('span', class_='date')  # Adjust class if necessary
    post_date = date_tag.get_text(strip=True) if date_tag else "Date not found"

    if article_tag:
        article_content = article_tag.get_text(strip=True)

        # Prepare the content with post date
        article_with_date = f"Ngày đăng bài: {post_date}\n\n{article_content}"

        # Save the article content to a file
        with open('article_content.txt', 'w', encoding='utf-8') as file:
            # Write the title followed by the article content
            file.write(title + "\n\n")
            file.write(article_with_date)
    else:
        print("No <article> tag found.")
except requests.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
