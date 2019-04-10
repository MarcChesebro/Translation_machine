import re
from collections import Counter
from nltk.corpus import comtrans


def retrieve_corpora(translated_sentences_l1_l2='alignment-de-en.txt'):
    als = comtrans.aligned_sents(translated_sentences_l1_l2)
    sentences_l1 = [sent.words for sent in als]
    sentences_l2 = [sent.mots for sent in als]
    return sentences_l1, sentences_l2


def clean_sentence(sentence):
    regex_splitter = re.compile("([!?.,:;$\"')( ])")
    clean_words = [re.split(regex_splitter, word.lower()) for word in sentence]
    return [w for words in clean_words for w in words if words if w]


def filter_sentence_length(sentences_l1, sentences_l2, min_len=0, max_len=20):
    filtered_sentences_l1 = []
    filtered_sentences_l2 = []
    for i in range(len(sentences_l1)):
        if (min_len <= len(sentences_l1[i]) <= max_len) and (min_len <= len(sentences_l2[i]) <= max_len):
            filtered_sentences_l1.append(sentences_l1[i])
            filtered_sentences_l2.append(sentences_l2[i])
    return filtered_sentences_l1, filtered_sentences_l2


def create_indexed_dictionary(sentences, dict_size=10000):
    count_words = Counter()
    dict_words = {}
    for sen in sentences:
        for word in sen:
            count_words[word] += 1

    vocab = []
    for idx, item in enumerate(count_words.most_common(dict_size)):
        dict_words[item[0]] = idx
        vocab.append((dict_words[item[0]], count_words[item[0]]))

    return dict_words, vocab


def sentences_to_indexes(sentences, indexed_dictionary):
    indexed_sentences = []
    not_found_counter = 0
    for sent in sentences:
        idx_sent = []
        for word in sent:
            try:
                idx_sent.append(indexed_dictionary[word])
            except KeyError:
                idx_sent.append(-1)
                not_found_counter += 1
        indexed_sentences.append(idx_sent)
    print('[sentences_to_indexes] Did not find {} words'.format(not_found_counter))
    return indexed_sentences

