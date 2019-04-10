import pickle

with open('english_word_dict.txt', 'rb') as f:
    eng = pickle.load(f)

with open('german_word_dict.txt', 'rb') as f:
    ger = pickle.load(f)


def file_to_list(filename):
    sentence_list = []
    with open(filename, 'r') as f:
        for line in f:
            sentence_list.append(line.strip())
    return sentence_list


def list_to_file(sentences, filename):
    with open(filename, 'w') as f:
        for sentence in sentences:
            f.write('{}\n'.format(sentence))


def convert_english(sentence):
    # with open('english_word_dict.txt', 'rb') as f:
    #     eng = pickle.load(f)

    return [eng[word] for word in sentence if word in eng]


def convert_german(sentence):

    # with open('german_word_dict.txt', 'rb') as f:
    #     ger = pickle.load(f)
    return [ger[word] for word in sentence if word in ger]


def verbose_translation(source, prediction, target):
    english_source = " ".join(convert_english(source.split(' ')))
    german_pred = " ".join(convert_german(prediction.split(' ')))
    german_target = " ".join(convert_german(target.split(' ')))

    string = \
        "English source: \n" + \
        "{}\n".format(english_source) + \
        "German prediction: \n" + \
        "{}\n".format(german_pred) + \
        "German target: \n" + \
        "{}\n\n".format(german_target)

    return string


def print_translation(source, prediction, target):
    english_source = " ".join(convert_english(source))
    german_pred = " ".join(convert_german(prediction))
    german_target = " ".join(convert_german(target))

    print(
        "English source: \n" +
        "{}\n".format(english_source) +
        "German prediction: \n" +
        "{}\n".format(german_pred) +
        "German target: \n" +
        "{}\n".format(german_target)
    )


def print_predictions(source_file, prediction_file, target_file, out_filename):
    sources = file_to_list(source_file)
    predictions = file_to_list(prediction_file)
    targets = file_to_list(target_file)

    assert len(sources) == len(predictions) and len(sources) == len(targets)

    with open(out_filename, 'w') as f:
        for i, english in enumerate(sources):
            f.write(verbose_translation(english, predictions[i], targets[i]))
