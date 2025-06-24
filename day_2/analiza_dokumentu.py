from typing import List, Callable, Dict
from collections import Counter
from functools import partial
import re  # wyrażenia regularne


# tylko hinty, nie sprawdzają typów
def process_documents(docs: List[str], analisys_fn: Callable[[str], Dict[str, int]]) -> Dict[str, int]:
    """
    Funkcja wyższego rzędu, analizuje listę dokumentów
    :param docs:
    :param analisys_fn:
    :return:
    """
    aggregate_counter: Dict[str, int] = Counter()
    for doc in docs:
        result = analisys_fn(doc)
        aggregate_counter.update(result)
    return dict(aggregate_counter)


def word_frequency_analisys(text: str) -> Dict[str, int]:
    """
    Funkcja analizy tekstu  dokumentu
    :param text:
    :return: częstotliwość wystąpień słów
    """
    stopwords = {'the', 'and', 'this', 'that', 'with', 'from', 'which'}
    words = re.findall(r"\b\w+\b", text.lower())
    filtered_words = [w for w in words if len(w) > 3 and w not in stopwords]
    return dict(Counter(filtered_words))


def keyword_sentence_count(text: str, keyword: str = "text") -> Dict[str, int]:
    """
    funkcja liczy ile zdań w tekście zawiera wskazane słowa kluczowe
    :param text:
    :param keyword:
    :return:
    """
    sentences = re.split(f'[.!?]', text)
    count = sum(1 for sentence in sentences if keyword.lower() in sentence.lower())
    return {keyword: count}


documents = [
    "This is a sample document with some sample text and additional sample data. Big text",
    "Another document, which contains different text and information from the first one.",
    "Text mining and natural language processing are interesting fields. My text"
]

result = process_documents(documents, word_frequency_analisys)  # przekazujemy adres funkcji
print(result)

analisys_with_keyword = partial(keyword_sentence_count, keyword="text")
keyword_result = process_documents(documents, analisys_with_keyword)

print(keyword_result)
# mypy
# mypy .\analiza_dokumentu.py
