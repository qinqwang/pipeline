
# engineering-text_pipeline

- [engineering-text_pipeline](#text-pipeline)
    * [Tokenization](#tokenization)
        - [Stopwords Remove](#stopwords-removal)
        - [Code Convert](#code-convert)
        - [Punctuation Removal](#punctuation-removal)
    * [Language Identification](#language-identification)
    * [Spelling Correction](#spelling-correction)
    * [Stemming](#stemming)
    * [Lemmatization](#lemmatization)
    * [Word_frequency](#word-frequency)
    * [Entity_Recognition](#entity-recognition)
    * [Text Pipeline](#text-pipeline)
        - [String to Function](#string-to-function)
    * [Statistic](#statistic)
        - [Next ID](#next-id)
        - [Do statistic](#do-statistic)
        - [Reconstruct dictionary](#reconstruct-dictionary)
    * [Noise Removal](#noise-removal)
        - [Get txt files](#get-txt-files)
        - [Clean Data](#clean-data)

# Introduction
Model choose theory, modification, implementation and details available in the wiki:
[http://wiki.intranet.cliffordchance.com/display/DSL/Text+Pipeline]

# Getting Started

## Library Dependency
* Tokenization: [nltk](https://www.nltk.org/api/nltk.tokenize.html) 3.3
* Language Detect:[langdetect](https://pypi.org/project/langdetect/) 1.0.7
* Stemming: [nltk.stem.snowball](https://www.nltk.org/api/nltk.tokenize.html) 3.3
* Stopwords: [nltk](https://www.nltk.org/api/nltk.tokenize.html) 3.3
* Punctuations: [string](https://docs.python.org/2/library/string.html) 2.7


# How to use the pipeline
Firstly you need to import the model from the folder.
```python
from text_pipeline import pipeline

```
Construct the data. Here I use the data from the `data` folder `big.txt`.
```python
# get the directory path
DIR_NAME = os.path.dirname(__file__)

OUT_FOLDER = 'data'
# joint the path
relative_folder_path = os.path.join(DIR_NAME, OUT_FOLDER)
relative_path = os.path.join(relative_folder_path, 'big.txt')
# open the specific file
file = open(str(relative_path), 'r')
# read content of the file
lines = file.readlines()
n = 0
text = ''
for line in lines:
    text = text + line
# change the content into the list
text_list = [text]
```
Build your pipeline
```python
# construct your pipeline
my_pipeline = pipeline.Pipeline([('tokenize_words', {}), ('remove_punct', {}), ('stop_words_removal', {'static': True, 'file_name': 'stopwords filter'}), ('stemming_list', {'static': True, 'lang': 'en', 'file_name': 'stemming words changed'})])
```

Input the data
```python
results = my_pipeline(text_list)
file.close()
```


## Tokenization
NLTK PunktSentenceTokenizer which is capable of unsupervised machine learning.
```python
def tokenize_words(raw_data):
    """
    Use nltk to do tokenization.If the raw_data has the date information, the tokenizer won't split them up and it
    will keep it in the original form i.e ['I have a meeting in Jan 1st 1995-01-13']--->['I', 'have', 'a', 'meeting',
    'in', 'Jan 1st', '1995-01-13']
    :param raw_data: raw_data: List of plaintext
    :return: the list of tokenized word
    """
    pass

```

### Stopwords Remove
Move the stopwords from the list according to the language it uses
```python
def stop_words_removal(text, language='en'):
    """
    Filter out the stop words in the text according to the language it uses
    :param text: The list of tokenized text
    :param language: Detected language which is the IOS639-1 format
    :return: The list of the tokenized text without stopwords
    """
    pass

```

### Code Convert
Covert IOS639-1 format to the original readable language.
```python

def _code_convert(lang):
    """
    :param lang: IOS639-1 code
    :return: language
    """
    pass
```

### Punctuation Removal
 Filter out the punctuation from the tokenized data
 ```python

 def remove_punct(list_text):
    """
    :return:
    :param list_text: The list of tokenized data
    :return: The list of tokenized data without punctuations
    """
    pass
 ```

## Language Identification
Detect the which language of the text using and pick up the most likely language
```python
def detect_language(text):
    """
    :param text: The string of plaintext
    :return:  The most likely language which is the IOS639-1 form(english-->en)
    """
    pass

```


## Spelling Correction
Spelling correction is part of the text pipeline. The spelling corrections will detect wrong spelling word and correct the wrong spelling word by editing it.

#### How it works

1. The module will take an input word and
&nbsp;

2. Use the edit function to correct wrong spelling words, these operations are
- Transpose: "oragne" -> "orange"
- Delete: "bannana" -> "banana"
- Insert: "aple" -> "apple"
- Replace: "peech" -> peach"


```python
def edit_word(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    tranposes = [L + R[1] +R[0] + R[2:] for L, R in splits if len(R) >1]
    replaces = [L + c +R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + tranposes + replaces + inserts)
```
&nbsp;




3. Some mispelled words may require two edit operations, we want to consider these word too
- Delete and insert: 'aplle' -> 'apple'

```python
def edits_word_twice(word):
    return(twice_edited_word for one_edited_word in edit_word(word) for twice_edited_word in edit_word(one_edited_word))

```
&nbsp;


4. Collect all the words that have been edited from the mispelled word. We call these candidate words


```python
def candidates(word):
    return(known([word]) or known(edits1(word)) or known(edits2(word)  or [word]))
 ```
&nbsp;


5. Reduce the list of candidate words and check words validation
Check if the list of candidate words are the words in spelling corpus

```python
def get_known_word(words):

    return set(w for w in words if w in spelling_corpus)
```
&nbsp;



6. From the reduced list of candidates
Return the word with highest probabilty
This probabilty is counted base on the word occurence in the spelling corpus

```python
def correction(word):
    return max(candidates(word), key = word_probability)
 ```
&nbsp;


#### Usage
Make sure these modules are installed, they should be installed by default
- RE module
- Counter module
If not use pip install for this
- Load the spelling corpus, this can be any long text document with correct spelling in the topic domain you want to work with


## Stemming
 Stemming removes morphological affixes from words, leaving only the word stem.
 The first parameter **text** is the list og the bag words, the second **lang** is the
 language you choose for stemming. It uses the [ISO](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format.
 The default **lang** is in english.
```python

def stemming(text, lang='en'):
    """
    :param text: the list of tokenized words
    :param lang: the language use. Default is english
    :return: the list of words stem
    """
    pass

```

Every changed word will be record and write into the *.csv* file in *output* folder.
It is implemented by the private function *_static_stemming*
```python

def _static_stemming(origin_words_list, affected_words_list):
    """
    :param origin_words_list: The list of original words
    :param affected_words_list: The list of the changed words
    :return: True
    """
    pass
```

## Lemmatization and POS
Lemmatization and POS  will convert the input list of tokens(words that have been split) into the word basic form (lemma)
and return the POS tags if users choose pos = True

#### How it works
1.  Make Part of Speech (POS) tag from treebank compatitable with WordNetLemmatizer() from nltk

```python
def get_wordnet_pos_tag(treebank_tag):

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
```
&nbsp;

2. Get the POS tag for input tokens
This POS tag is passed to the NLTK WordNetLemmitazer()
so the function will consider the grammar of the input word when it return the lemma

```python
def lemma(text, pos = False, static = False, file_name='lemma'):

    pos_tokens = nltk.pos_tag(text)

    org_words = [word for (word, pos_tag) in pos_tokens]

    lemma_words = [lemmatizer.lemmatize(word, get_wordnet_pos_tag(pos_tag)) for (word, pos_tag) in pos_tokens]

    org_words_effected = [word for (word, pos_tag) in pos_tokens if word not in lemma_words]

    affected_words = [word for word in lemma_words if word not in org_words]

    lemma_pos_tokens = (lemma_words)

    if pos:
        lemma_pos_tokens = lemma_pos = (lemma_words, pos_tokens)
```

## Word Frequency
#### Usage
- Make sure Wordnet is installed in corpus
- To use function, pass in a list of tokens of words

#### How it works
User input a list of sentences, the function will tokenize the sentence
and calculate the occurrence of words in the list

```python
def count_word_frequency(text, file_name='word_frequency', static=False):
    """
    :param text: the list of tokens
    :param file_name: The default file name is word frequency
    :param static: if do statistic
    :return: The dictionary of tokens and each word corresponding frequency
    """
    pass
```

## Entity Recognition
#### Usage
- Make sure  nltk.chunk.regexp.RegexpParser is installed
- To use function, pass in a list of word tokens

#### How it works
User input a list of word tokens
The function will use shallow parsing to extract noun phrases which can be used as entities as followed:

1. Using regular expression grammar to define pattern for parsing the tokens

```python
def shallow_parse(tokens, static = False, file_name = 'entity_frequency'):

    grammar = r'NP: {<CD>? <DT>? <JJ>* <NN.*>+}'

    all_chunks = []

    chunker = nltk.chunk.regexp.RegexpParser(grammar)
```
2. The tokens are then tagged using part of speech tag
These tagged tokens are then parsed into noun phrase chunks according to the grammar pattern

```python
    tagged_tokens = nltk.pos_tag(tokens)

    chunks = [chunker.parse(tagged_tokens)]

    flattened_chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(chunk) for chunk in chunks))
```

3. The parsed chunks are extracted, to filter out non noun phrases
The function returns a list of noun phrases and output csv file for these phrases

```python
    valid_chunks_tagged = [(status, [chunked_sentence for chunked_sentence in chunk]) for status,
                         chunk in itertools.groupby(flattened_chunks, lambda x : x[2] != 'O')]


    valid_chunks = [' '.join(word.lower() for word, tag, chunk in wtc_group if word.lower() not in stopwords)
                                   for status, wtc_group in valid_chunks_tagged if status]

    all_chunks.extend(valid_chunks)


    if static == True:
         statistic.do_statistic_single(all_chunks,file_name)

    return all_chunks
```

## Text Pipeline
Pipeline provides the feature to customize the function. When you invoke function, you need to initialize
the variables and a new instance object is created. Then input the data to process in order and return the
result. For example:
```python
my_pipeline = pipeline.Pipeline([('tokenize_words', {}), ('remove_punct', {}), ('stop_words_removal', {'language': 'en'}), ('stemming_list', {})])
processed_data = my_pipeline(data)
```
The structure of the pipeline is base on the **Python Closures** which is a function object that remembers
values in enclosing scopes even if they are not present in memory.
```python
def Pipeline(functions):
    """
    :param functions: The functions users want to put into
    :return: trigger
    """
    pass
    def trigger(text):
       """
       :type text: object
       """
    pass
```
At the same time, it also provides the private function to records what functions the pipeline use and write
in to the .csv file

```python
def _static_pipe(functions):
    """
    :return: True
    """
    pass
```

### String to Function
This function provides the feature that can convert function name to the invokable function
```python
def string_to_function(func_name):
    """
    :param func_name: string of function name
    :return: function
    """
    pass
```


## Statistic
This function is used for recording the change of the input and output.
And then write file as *.csv* into the *output* folder

### Next ID
It is a private counter for version control which used for different files to static.csv
```python
def _next_id():
    """
    :return: The current id
    """
    pass
```

### Do statistic
Record the words change and word frequency in the list and write into a *.csv* file.
```python
def do_statistic(original_words_list, affected_words_list, func_name):
    """
    :param original_words_list: The list of original words
    :param affected_words_list: The list of the changed words
    :param func_name: function name
    :return: True
    """
    pass
```

### Reconstruct dictionary
Reconstruct the affected words list into a dictionary
```python
def reconstruct_dic(origin_list, affected_list):
    """
    :param origin_list:
    :param affected_list:
    :return:
    """
    pass
```

## Noise Removal
Use this module, you only need to input the (absolute)path of the folder and the it will automatically
take the `.txt` files and get rid of the noisy from the files and create the folder called `output` and
write the sanitized `.txt` files as the same name.
```python
def noise_removal(folder_path):
    """
    :param folder_path: The absolute path of the data folder
    """
    pass
```

### Get txt files
Get all the txt file's names according to the path of the folder
```python
def _get_txt_files(path):
    """
    :param path: the path of the folder
    :return: the list of the txt file name
    """
    pass
```

### Clean Data
Mainly use the regular expression to get rid of the noisy by the given pattern
```python
def _clean_data(rgx_list, text):
    """
    :param rgx_list: the list if the rgx pattern
    :param text: string text
    :return:the clean text of string
    """
    pass
```