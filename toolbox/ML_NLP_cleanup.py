
def clean(x):
    """Clean for NLP purposes"""

    # Remove_Punctuation
    import string
    for punctuation in string.punctuation:
        x = x.replace(punctuation, '')

    # Lower_Case
    x = x.lower()

    # Remove_Numbers
    x = ''.join(word for word in x if not word.isdigit())

    # Remove_StopWords
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(x)
    x = [w for w in word_tokens if not w in stop_words]

    # Lemmatize
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer() # instanciate the model
    x = [lemmatizer.lemmatize(word) for word in x]

    # make_a_string
    x = ' '.join(word for word in x)

    return x
