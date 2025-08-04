import requests
from bs4 import BeautifulSoup
import re

# User input for the URL of the website
url = input("Enter the URL a website: ")

# Check whether the schema is present in the URL
if not re.match(r'^https?://', url):
    url = 'http://' + url

# Send HTTP request to the website and retrieve the HTML content
response = requests.get(url)

# Check whether the request was successful or not
if response.status_code == 200:
    # HTML content of the website
    html_content = response.text

    # Use BeautifulSoup to analyze the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Grab the title of the website, with fallback if title tag is missing
    title = soup.title.string if soup.title and soup.title.string else "No Title Found"
    title_length = len(title)

    # Grab Meta Tags (description and keywords)
    meta_tags = soup.find_all('meta')
    meta_data = {'description': '', 'keywords': ''}
    keywords_length = 0
    keywords_count = 0  # Initialize to prevent errors if no keywords tag is found

    for tag in meta_tags:
        if 'name' in tag.attrs and tag.attrs['name'] in ['description', 'keywords']:
            meta_data[tag.attrs['name']] = tag.attrs['content']
            if tag.attrs['name'] == 'keywords':
                keywords_length = len(tag.attrs['content'])
                keywords_count = len(tag.attrs['content'].split(','))

    # Retrieve headings (h1-h6) and count their content and number
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    headings_info = {}
    headings_length = {}

    for heading in headings:
        tag_name = heading.name
        heading_text = heading.get_text()
        heading_length = len(heading_text)

        if tag_name not in headings_info:
            headings_info[tag_name] = {'count': 1, 'text': [heading_text]}
            headings_length[tag_name] = heading_length
        else:
            headings_info[tag_name]['count'] += 1
            headings_info[tag_name]['text'].append(heading_text)
            headings_length[tag_name] += heading_length

    # Organize output into sections
    print("### Website Information ###")
    print(f"Title: {title} ({title_length} characters)\n")

    print("### Metadata ###")
    print(f"Description: {meta_data['description']} ({len(meta_data['description'])} characters)\n")
    print(f"Keywords: {meta_data['keywords']} ({keywords_length} characters, {keywords_count} words)\n")

    print("### Headings ###")
    for tag_name, info in headings_info.items():
        print(f"{tag_name}: {info['count']} Headings")
        for heading_text in info['text']:
            print(f"- {heading_text} ({len(heading_text)} characters)")
        print()

    total_characters = title_length + len(meta_data['description']) + keywords_length
    for tag_name, length in headings_length.items():
        total_characters += length

    print("### Total number of characters ###")
    print(f"{total_characters} characters in total")

else:
    print("Error when accessing the website. Status code:", response.status_code)
