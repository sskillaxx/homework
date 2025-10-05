# использована книга 1984 Дж.Оруэлла

import nltk
nltk.download('punkt', quiet=True)
import string
import pymorphy3
from nltk.tokenize import word_tokenize

ignored_symbols = string.punctuation + '\n\xa0«»\t—…' # очищаем ненужные символы по типу знаков препинания и т.д.
WORDS = {}
UNIQE_WORDS = set()
NOUNS = {}
VERBS = {}
ADJECTIVES = {}
morphling = pymorphy3.MorphAnalyzer()

with open('book_for_tokenization.txt', 'r+', encoding='utf-8') as book:
    for string in book:
        clear_string = "".join([ch for ch in string if ch not in ignored_symbols]) # очищенная строка
        words = word_tokenize(clear_string.lower()) # для точности делаем все слова полностью в нижнем регистре
        for normalized_word in words:
            parsed = morphling.parse(normalized_word)
            if not parsed:
                continue
            our_word = parsed[0]
            word_lemma = our_word.normal_form
            pos = our_word.tag.POS
            if pos == 'NOUN':
                NOUNS[word_lemma] = NOUNS.get(word_lemma, 0) + 1
            elif pos == 'ADJF' or pos == 'ADJS':  # полные и краткие прилагательные
                ADJECTIVES[word_lemma] = ADJECTIVES.get(word_lemma, 0) + 1
            elif pos == 'VERB' or pos == 'INFN':  # личные формы и инфинитив
                VERBS[word_lemma] = VERBS.get(word_lemma, 0) + 1
            
            WORDS[normalized_word] = WORDS.get(normalized_word, 0) + 1
            UNIQE_WORDS.add(normalized_word)

all_words = sum(WORDS.values())
all_uniqe_words = len(UNIQE_WORDS)

most_adjective = max(ADJECTIVES, key=ADJECTIVES.get)
most_noun = max(NOUNS, key=NOUNS.get)
most_verb = max(VERBS, key=VERBS.get)

lexical_variety = all_uniqe_words / all_words

print(f'лексическое разнообразие - {round(lexical_variety, 2) * 100} \n'
      f'самое частое прилагательное - {most_adjective}, встречается {ADJECTIVES[most_adjective]} раз \n'
      f'самый частый глагол - {most_verb}, встречается {VERBS[most_verb]} раз \n'
      f'самое частое существительное - {most_noun}, встречается {NOUNS[most_noun]} раз \n' 
      f'общее кол-во слов - {all_words} \n'
      f'общее кол-во уникальных слов - {all_uniqe_words} \n')