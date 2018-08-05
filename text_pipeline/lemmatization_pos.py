import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from text_pipeline import statistic
lemmatizer = WordNetLemmatizer()
nltk.download('wordnet')


def get_wordnet_pos_tag(treebank_tag):
    """
        :param word: treebank tag data from nltk corpus
        :return: return tags that is compatible to WORDNET tags style so we can use the WordNetLemmatizer from nltk
    """

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def lemma(text, pos = False, static = False, file_name='lemma'):
    """
        :param file_name: Set the default statistic file name as lemma
        :param static: The default parameter static is False
        :param tokens: list of are the words has been tokenized
        :return: return list of lemma word
        For statistic call the statistic function
        and pass in the list of  org_words_effected and affected_words
    """

    pos_tokens = nltk.pos_tag(text)

    org_words = [word for (word, pos_tag) in pos_tokens]

    lemma_words = [lemmatizer.lemmatize(word, get_wordnet_pos_tag(pos_tag)) for (word, pos_tag) in pos_tokens]

    org_words_effected = [word for (word, pos_tag) in pos_tokens if word not in lemma_words]

    affected_words = [word for word in lemma_words if word not in org_words]

    lemma_pos_tokens = (lemma_words)

    if pos:
        lemma_pos_tokens = lemma_pos = (lemma_words, pos_tokens)

    if static:
        statistic.do_statistic(org_words_effected, affected_words, func_name=file_name)

    return(lemma_pos_tokens)


