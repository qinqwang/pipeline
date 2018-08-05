import nltk
from nltk.chunk import RegexpParser
import itertools
from nltk.corpus import stopwords
stopwords= set(stopwords.words('english'))
from text_pipeline import statistic


def shallow_parse(tokens, static = False, file_name = 'entity_frequency'):

    """
        :param list of word tokens
        :return: return the noun phrase of the sentence as entities
    """

    grammar = r'NP: {<CD>? <DT>? <JJ>* <NN.*>+}'
    all_chunks = []

    chunker = nltk.chunk.regexp.RegexpParser(grammar)

    tagged_tokens = nltk.pos_tag(tokens)

    chunks = [chunker.parse(tagged_tokens)]

    flattened_chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(chunk) for chunk in chunks))

    valid_chunks_tagged = [(status, [chunked_sentence for chunked_sentence in chunk]) for status,
                         chunk in itertools.groupby(flattened_chunks, lambda x : x[2] != 'O')]


    valid_chunks = [' '.join(word.lower() for word, tag, chunk in wtc_group if word.lower() not in stopwords)
                                   for status, wtc_group in valid_chunks_tagged if status]

    all_chunks.extend(valid_chunks)


    if static == True:
         statistic.do_statistic_single(all_chunks,file_name)

    return all_chunks

