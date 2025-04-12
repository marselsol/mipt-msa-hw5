import requests
from collections import Counter

def get_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def count_word_frequencies(text, words):
    word_counts = Counter(text.split())
    return {word: word_counts[word] for word in words}

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    with open(words_file, 'r') as file:
        words_to_count = set(line.strip() for line in file if line.strip())

    text = get_text(url)
    frequencies = count_word_frequencies(text, words_to_count)

    print(frequencies)

if __name__ == "__main__":
    main()
