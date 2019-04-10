from corpora_utils import clean_sentence, retrieve_corpora, filter_sentence_length, create_indexed_dictionary, \
    sentences_to_indexes

import pickle


def output_to_file(sentences_1, sentences_2, filename):

    with open('english_{}.txt'.format(filename), 'w') as f:
        for sentence in sentences_2:
            string = " ".join([str(string_int) for string_int in sentence]) + '\n'
            f.write(string)

    with open('german_{}.txt'.format(filename), 'w') as f:
        for sentence in sentences_1:
            string = " ".join([str(string_int) for string_int in sentence]) + '\n'
            f.write(string)


def vocab_to_file(vocab1, vocab2, filename):
    with open('german_{}.txt'.format(filename), 'w') as f:
        for pair in vocab1:
            string = "\t".join([str(string_int) for string_int in pair]) + '\n'
            f.write(string)

    with open('english_{}.txt'.format(filename), 'w') as f:
        for pair in vocab2:
            string = "\t".join([str(string_int) for string_int in pair]) + '\n'
            f.write(string)


if __name__ == '__main__':

    print("------------------------------------------------------------------------------")
    print('loading data')

    sen_l1, sen_l2 = retrieve_corpora()

    print("------------------------------------------------------------------------------")
    print('cleaning data')

    clean_sen_l1 = [clean_sentence(s) for s in sen_l1]
    clean_sen_l2 = [clean_sentence(s) for s in sen_l2]

    filt_clean_sen_l1, filt_clean_sen_l2 = filter_sentence_length(clean_sen_l1, clean_sen_l2)

    print("------------------------------------------------------------------------------")
    print('Indexing sentence data')

    dict_l1, vocab_dict_l1 = create_indexed_dictionary(filt_clean_sen_l1, dict_size=15000)
    dict_l2, vocab_dict_l2 = create_indexed_dictionary(filt_clean_sen_l2, dict_size=10000)
    idx_sentences_l1 = sentences_to_indexes(filt_clean_sen_l1, dict_l1)
    idx_sentences_l2 = sentences_to_indexes(filt_clean_sen_l2, dict_l2)

    train = 10351
    test = 2957
    dev = 1480

    inverted_ger_dict = {str(v): k for k, v in dict_l1.items()}
    inverted_eng_dict = {str(v): k for k, v in dict_l2.items()}

    with open('english_word_dict.txt', 'wb') as f:
        pickle.dump(inverted_eng_dict, f)

    with open('german_word_dict.txt', 'wb') as f:
        pickle.dump(inverted_ger_dict, f)

    vocab_to_file(vocab_dict_l1, vocab_dict_l2, "vocab")

    output_to_file(idx_sentences_l1[:train], idx_sentences_l2[:train], 'train')
    output_to_file(idx_sentences_l1[train:(train + test)], idx_sentences_l2[train:(train + test)], 'test')
    output_to_file(idx_sentences_l1[(train + test):(train + test + dev)], idx_sentences_l2[(train + test):(train + test + dev)], 'dev')
