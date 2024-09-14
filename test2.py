import requests
from bs4 import BeautifulSoup

response = requests.get('https://vnexpress.net/hon-23-trieu-hoc-sinh-buoc-vao-nam-hoc-moi-4788964.html')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    #find the first <article> tag
    article_tag = soup.find('article')
    if article_tag:
        article_content = article_tag.get_text(strip=True)
        with open('article_content.txt', 'w', encoding='utf-8') as file:
                  file.write(article_content)
    else:
        print("No <article> tag found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")