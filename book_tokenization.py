# использована книга 1984 Дж.Оруэлла

import nltk
from nltk.corpus import stopwords
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

import spacy
nlp = spacy.load('ru_core_news_sm')

stop_words = set(stopwords.words('russian'))
WORDS = {}
UNIQE_WORDS = set()
WORDS_CLEARED = {}
UNIQE_WORDS_CLEARED = set()
NOUNS = {}
VERBS = {}
ADJECTIVES = {}
ROOTS = {}

# самые частые части речи + лексическое разнообразие
with open('book_for_tokenization.txt', 'r+', encoding='utf-8') as book:
    text = book.read()
words = nlp(text)

for token in words:
    if token.is_punct or token.is_space:
        continue
    
    word = token.text.lower()
    lemma = token.lemma_.lower()
    pos = token.pos_
    # считаем слова и уникальные слова
    WORDS[word] = WORDS.get(word, 0) + 1
    UNIQE_WORDS.add(word)
    
    if pos == 'NOUN':
        NOUNS[lemma] = NOUNS.get(lemma, 0) + 1
    elif pos == 'ADJ':
        ADJECTIVES[lemma] = ADJECTIVES.get(lemma, 0) + 1
    elif pos == 'VERB':
        VERBS[lemma] = VERBS.get(lemma, 0) + 1
    
    # считаем слова и уникальные слова без стоп-слов
    if word in stop_words or len(word) <= 1:
        continue
    
    WORDS_CLEARED[word] = WORDS_CLEARED.get(word, 0) + 1
    UNIQE_WORDS_CLEARED.add(word)
    
all_words = sum(WORDS.values())
all_uniqe_words = len(UNIQE_WORDS)

all_words_cleared = sum(WORDS_CLEARED.values())
all_uniqe_words_cleared = len(UNIQE_WORDS_CLEARED)

most_adjective = max(ADJECTIVES, key=ADJECTIVES.get)
most_noun = max(NOUNS, key=NOUNS.get)
most_verb = max(VERBS, key=VERBS.get)

lexical_variety = all_uniqe_words / all_words

# самый частый корень предложения
for sentence in words.sents:
    for token in sentence:
        if token.dep_ == 'ROOT':
            root_lemma = token.lemma_.lower()
            ROOTS[root_lemma] = ROOTS.get(root_lemma, 0) + 1
most_root = max(ROOTS, key=ROOTS.get)

# выводы
# print(f'лексическое разнообразие - {round(lexical_variety * 100)}%\n'
#       f'самое частое прилагательное - {most_adjective}, встречается {ADJECTIVES[most_adjective]} раз \n'
#       f'самый частый глагол - {most_verb}, встречается {VERBS[most_verb]} раз \n'
#       f'самое частое существительное - {most_noun}, встречается {NOUNS[most_noun]} раз \n' 
#       f'общее кол-во слов - {all_words} \n'
#       f'общее кол-во уникальных слов - {all_uniqe_words} \n'
#       f'общее кол-во очищенных слов - {all_words_cleared} \n'
#       f'разница в объёме между очищенным и неочищенным текстом - {round((100 - (all_words_cleared / all_words) * 100))}% \n'
#       f'самый частый корень предложения - {most_root}, встречается {ROOTS[most_root]} раз \n')

print(VERBS)