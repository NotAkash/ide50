import nltk

class Analyzer():
    """Implements sentiment analysis."""
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        #Todo
        positives = open(positives,encoding='utf-8')
        negatives = open(negatives,encoding='utf-8')

        self.positives = []
        self.negatives = []

        for line in positives:
            if line.startswith(";") == False and line!=" \n":
                line = line.lower()
                self.positives.append(line.rstrip("\n"))
        for line in negatives:
            if line.startswith(";") == False and line!=" \n":
                line = line.lower()
                self.negatives.append(line.rstrip("\n"))

        positives.close()
        negatives.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        score = 0

        for i in (self.positives):
            for j in tokens:
                if i == j:
                    score+=1

        for i in (self.negatives):
            for j in tokens:
                if i == j:
                    score -= 1
        return score

"""
Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. ~ NLTK Plugin
word_tokenize
"""