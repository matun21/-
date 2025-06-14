import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

class TextProcessor:
    def __init__(self, url):
        self.url = url
        self.chapter_text = self.get_chapter_text()

    def get_chapter_text(self):
        response = requests.get(self.url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        chapter_text = ''
        for tag in soup.find_all(['h1', 'h2', 'p']):
            if tag.name == 'h2' and re.search(r'chapter 1', tag.text, re.IGNORECASE):
                for sibling in tag.find_next_siblings():
                    if sibling.name == 'h2':
                        break
                    if sibling.name == 'p':
                        chapter_text += sibling.get_text(separator=' ', strip=True) + ' '
        return chapter_text

    def find_in_context(self, target_word, left_len, right_len):
        result = []
        text = self.chapter_text.lower()
        sentences = re.split(r'(?<=[.!?]) +', text)
        with open('word_contexts.txt', 'w', encoding='utf-8') as f:
            for sentence in sentences:
                tokens = re.findall(r'\b\w+\b', sentence)
                for i, word in enumerate(tokens):
                    if word == target_word:
                        left_context = tokens[max(0, i - left_len):i]
                        right_context = tokens[i + 1:i + 1 + right_len]
                        context = ' '.join(left_context + [word] + right_context)
                        f.write(context + '\n')
                        print(context)
                        result.append(context)
        return result

url = 'https://www.gutenberg.org/files/4300/4300-h/4300-h.htm'
text_processor = TextProcessor(url)
text_processor.find_in_context('buck', 3, 3)

