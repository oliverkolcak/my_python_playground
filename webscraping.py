import requests
from bs4 import BeautifulSoup
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="testuser",
    passwd="Password1*",
    database="test_db"
)

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS webscraping (
        id INT AUTO_INCREMENT PRIMARY KEY,
        header TEXT UNIQUE,
        paragraph TEXT,
        link TEXT
    )
""")

r = requests.get('https://www.novinky.cz/sekce/zahranicni-7')
soup = BeautifulSoup(r.content, 'html.parser')

headers = soup.find_all('h3', class_='c_aF c_aI q_hF')
paragraphs = soup.find_all('p', class_='q_hR')

for header, paragraph in zip(headers, paragraphs):
    header_text = header.get_text().strip()
    paragraph_text = paragraph.get_text().strip()
    link = header.find('a')['href'] if header.find('a') else None

    if not header_text:  
        continue

    cursor.execute("SELECT id FROM webscraping WHERE header = %s", (header_text,))
    result = cursor.fetchone()

    if result:
        print(f"Skipping duplicate header: {header_text}")
    else:
        print(f"Adding new entry: {header_text}")
        print(f"Paragraph: {paragraph_text}")
        print(f"Link: {link}")
        print('-' * 80)

        cursor.execute("""
            INSERT INTO webscraping (header, paragraph, link)
            VALUES (%s, %s, %s)
        """, (header_text, paragraph_text, link))

db.commit()

cursor.close()
db.close()
