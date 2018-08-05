import nltk
from text_pipeline import statistic

def entity_recognition(sentence, static = False, file_name='entity_list1'):
    """
        the entity recognition wont detect entity if there is no space between word and punctuation
        such as "California,"
        :param file_name: Set the default statistic file name as entity_list
        :param static: The default parameter static is False
        :return: list of tuples (entity_label, entity) such as (GPE, 'New York')
        For statistic call the statistic function
        and pass in the list of entity labels and list of entities
    """

    parse_tree = nltk.ne_chunk(nltk.tag.pos_tag(sentence.split()), binary=False)

    entity_label = [t.label() for t in parse_tree.subtrees() if t.label() != 'S']

    entity_list = [" ".join(word for word, tag in entities) for entities in parse_tree if isinstance(entities, nltk.Tree)]

    entity = list(zip(entity_label, entity_list))

    if static:
        statistic.do_statistic(entity_list,entity_label ,func_name=file_name)

    return entity

