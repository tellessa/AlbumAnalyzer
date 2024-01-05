import nltk
from gensim.models import LdaModel
from gensim.corpora.dictionary import Dictionary

# The decimal numbers in the string representation of a topic, such as -0.340, 0.298, and 0.183, are called "topic-word probabilities" or "topic weights." These numbers play a crucial role in understanding and interpreting topic models.

# Here's a breakdown of what they signify:

# Strength of Association: The magnitude (absolute value) of these numbers indicates how strongly a word is associated with a particular topic. Higher absolute values (closer to 1) suggest a stronger connection, while lower values (closer to 0) suggest a weaker one.

# Positive vs. Negative Values:

# Positive values: Words that contribute positively to the meaning of the topic. They are characteristic and frequently used within that topic.
# Negative values: Words that are less characteristic of the topic or might even have an opposing meaning. They are less likely to appear in documents associated with that topic.
# Relative Importance: The relative magnitudes of the numbers within a topic help you understand the relative importance of different words in defining that topic. Words with higher absolute values are generally more important in characterizing the topic than those with lower values.

def main():
    # TODO: pull the lyrics from lyricsgenius or another api, once you provide the title.
    lyrics = """
    Mist hangs above hills
    Above mist hangs stone face of mountain
    Above mountain face hangs a net of sky --
    Crack! there are wings and they rip the net!
    And the dance flows on
    Everything flows toward the rim of that
    Shining cup

    Crossed sticks lie on earth
    Between crossed sticks -- pile of ash
    Something rises on the wisp of smoke
    Dog's feet move by fast
    And the dance flows on
    Everything flows toward the rim of that
    Shining cup

    Through these channels/words
    I want to touch you
    Touch you deep down
    Where you live
    Not for power but
    Because I love you
    So
    Love the Lord
    And in Him love me too
    And in Him go your way
    And I'll be right there with you
    Leaving
    No footprints when we go
    No footprints when we go
    Only where we've been, a faint and fading glow...
    """

    lyrics_lines = lyrics.split("\n")

    processed_lyrics = [preprocess_text(lyric) for lyric in lyrics_lines]

    dictionary = Dictionary(processed_lyrics)
    corpus = [dictionary.doc2bow(doc) for doc in processed_lyrics]

    lda_model = LdaModel(corpus, id2word=dictionary, num_topics=3)

    topics: list = lda_model.print_topics(num_words=5)

    cleaned_data: list[tuple] = []

    for i, topic in enumerate(topics):
        # topic_a: tuple[int, str] = topics[0]
        weights_and_words: str = topic[1]
        as_list = weights_and_words.split("+")
        stripped = [i.rstrip().lstrip() for i in as_list]

        for sample in stripped:
            sample_split = sample.split("*")
            weight = float(sample_split[0])
            word = sample_split[1]  # but without the double quotes
            stripped_word = word.replace('"', '')
            cleaned_data.append((i, stripped_word, weight))
    print()

def preprocess_text(text):
    text = text.lower()  # convert to lowercase
    tokens = nltk.word_tokenize(text)  # tokenize sentences
    tokens = [t for t in tokens if t.isalpha()]  # remove punctuation
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]  # lemmatize words
    stopwords = nltk.corpus.stopwords.words("english")  # remove stopwords
    tokens = [t for t in tokens if t not in stopwords]
    return tokens


# for word in lyrics.split():
#     if word.endswith('ing'):
#         print(word)

if __name__ == "__main__":
    main()