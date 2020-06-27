{"filter":false,"title":"analyzer.py","tooltip":"/pset6/sentiments/analyzer.py","undoManager":{"mark":34,"position":34,"stack":[[{"start":{"row":0,"column":0},"end":{"row":18,"column":3},"action":"remove","lines":["import nltk","","class Analyzer():","    \"\"\"Implements sentiment analysis.\"\"\"","","    def __init__(self, positives, negatives):","        \"\"\"Initialize Analyzer.\"\"\"","","        # TODO","","    def analyze(self, text):","        \"\"\"Analyze text for sentiment, returning its score.\"\"\"","","        # TODO","        return 0","","\"\"\"","Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. ~ NLTK Plugin","\"\"\""],"id":1},{"start":{"row":0,"column":0},"end":{"row":35,"column":51},"action":"insert","lines":["import nltk","","class Analyzer():","    \"\"\"Implements sentiment analysis.\"\"\"","","    def __init__(self, positives, negatives):","        \"\"\"Initialize Analyzer.\"\"\"","        #Todo","        positives = open(positives)","        negatives = open(negatives)","","        self.positives = []","        self.negatives = []","","        for line in positives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                self.positives.append(line.rstrip(\"\\n\"))","","","        positives.close()","","        for line in negatives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                self.positives.append(line.rstrip(\"\\n\"))","","        negatives.close()","","    def analyze(self, text):","        \"\"\"Analyze text for sentiment, returning its score.\"\"\"","","        return 0","","\"\"\"","Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. ~ NLTK Plugin","\"\"\"","Analyzer(\"positive-words.txt\",\"negative-words.txt\")"]}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":51},"action":"remove","lines":["Analyzer(\"positive-words.txt\",\"negative-words.txt\")"],"id":2}],[{"start":{"row":34,"column":3},"end":{"row":35,"column":0},"action":"remove","lines":["",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":34,"column":3},"action":"remove","lines":["import nltk","","class Analyzer():","    \"\"\"Implements sentiment analysis.\"\"\"","","    def __init__(self, positives, negatives):","        \"\"\"Initialize Analyzer.\"\"\"","        #Todo","        positives = open(positives)","        negatives = open(negatives)","","        self.positives = []","        self.negatives = []","","        for line in positives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                self.positives.append(line.rstrip(\"\\n\"))","","","        positives.close()","","        for line in negatives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                self.positives.append(line.rstrip(\"\\n\"))","","        negatives.close()","","    def analyze(self, text):","        \"\"\"Analyze text for sentiment, returning its score.\"\"\"","","        return 0","","\"\"\"","Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. ~ NLTK Plugin","\"\"\""],"id":4},{"start":{"row":0,"column":0},"end":{"row":34,"column":3},"action":"insert","lines":["import nltk","","class Analyzer():","    \"\"\"Implements sentiment analysis.\"\"\"","","    def __init__(self, positives, negatives):","        \"\"\"Initialize Analyzer.\"\"\"","        #Todo","        positives = open(positives,encoding='utf-8')","        negatives = open(negatives,encoding='utf-8')","","        self.positives = []","        self.negatives = []","","        for line in positives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                self.positives.append(line.rstrip(\"\\n\"))","","","        positives.close()","","        for line in negatives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                self.positives.append(line.rstrip(\"\\n\"))","","        negatives.close()","","    def analyze(self, text):","        \"\"\"Analyze text for sentiment, returning its score.\"\"\"","","        return 0","","\"\"\"","Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. ~ NLTK Plugin","\"\"\""]}],[{"start":{"row":0,"column":0},"end":{"row":34,"column":3},"action":"remove","lines":["import nltk","","class Analyzer():","    \"\"\"Implements sentiment analysis.\"\"\"","","    def __init__(self, positives, negatives):","        \"\"\"Initialize Analyzer.\"\"\"","        #Todo","        positives = open(positives,encoding='utf-8')","        negatives = open(negatives,encoding='utf-8')","","        self.positives = []","        self.negatives = []","","        for line in positives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                self.positives.append(line.rstrip(\"\\n\"))","","","        positives.close()","","        for line in negatives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                self.positives.append(line.rstrip(\"\\n\"))","","        negatives.close()","","    def analyze(self, text):","        \"\"\"Analyze text for sentiment, returning its score.\"\"\"","","        return 0","","\"\"\"","Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. ~ NLTK Plugin","\"\"\""],"id":5},{"start":{"row":0,"column":0},"end":{"row":46,"column":3},"action":"insert","lines":["import nltk","","class Analyzer():","    \"\"\"Implements sentiment analysis.\"\"\"","","    def __init__(self, positives, negatives):","        \"\"\"Initialize Analyzer.\"\"\"","        #Todo","        positives = open(positives,encoding='utf-8')","        negatives = open(negatives,encoding='utf-8')","","        self.positives = []","        self.negatives = []","","        for line in positives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                line = line.lower()","                self.positives.append(line.rstrip(\"\\n\"))","        for line in negatives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                line = line.lower()","                self.positives.append(line.rstrip(\"\\n\"))","","        positives.close()","        negatives.close()","","    def analyze(self, text):","        \"\"\"Analyze text for sentiment, returning its score.\"\"\"","        tokens = nltk.tokenizer.tokenize(text)","","        score = 0","","        for i in (self.positives):","            for j in tokens:","                if i == j:","                    score+=1","","        for i in (self.negatives):","            for j in tokens:","                if i == j:","                    score -= 1","        return score","","\"\"\"","Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. ~ NLTK Plugin","word_tokenize","\"\"\""]}],[{"start":{"row":0,"column":0},"end":{"row":46,"column":3},"action":"remove","lines":["import nltk","","class Analyzer():","    \"\"\"Implements sentiment analysis.\"\"\"","","    def __init__(self, positives, negatives):","        \"\"\"Initialize Analyzer.\"\"\"","        #Todo","        positives = open(positives,encoding='utf-8')","        negatives = open(negatives,encoding='utf-8')","","        self.positives = []","        self.negatives = []","","        for line in positives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                line = line.lower()","                self.positives.append(line.rstrip(\"\\n\"))","        for line in negatives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                line = line.lower()","                self.positives.append(line.rstrip(\"\\n\"))","","        positives.close()","        negatives.close()","","    def analyze(self, text):","        \"\"\"Analyze text for sentiment, returning its score.\"\"\"","        tokens = nltk.tokenizer.tokenize(text)","","        score = 0","","        for i in (self.positives):","            for j in tokens:","                if i == j:","                    score+=1","","        for i in (self.negatives):","            for j in tokens:","                if i == j:","                    score -= 1","        return score","","\"\"\"","Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. ~ NLTK Plugin","word_tokenize","\"\"\""],"id":6},{"start":{"row":0,"column":0},"end":{"row":46,"column":3},"action":"insert","lines":["import nltk","","class Analyzer():","    \"\"\"Implements sentiment analysis.\"\"\"","","    def __init__(self, positives, negatives):","        \"\"\"Initialize Analyzer.\"\"\"","        #Todo","        positives = open(positives,encoding='utf-8')","        negatives = open(negatives,encoding='utf-8')","","        self.positives = []","        self.negatives = []","","        for line in positives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                line = line.lower()","                self.positives.append(line.rstrip(\"\\n\"))","        for line in negatives:","            if line.startswith(\";\") == False and line!=\" \\n\":","                line = line.lower()","                self.positives.append(line.rstrip(\"\\n\"))","","        positives.close()","        negatives.close()","","    def analyze(self, text):","        \"\"\"Analyze text for sentiment, returning its score.\"\"\"","        tokens = tokenizer.tokenize(text)","","        score = 0","","        for i in (self.positives):","            for j in tokens:","                if i == j:","                    score+=1","","        for i in (self.negatives):","            for j in tokens:","                if i == j:","                    score -= 1","        return score","","\"\"\"","Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. ~ NLTK Plugin","word_tokenize","\"\"\""]}],[{"start":{"row":28,"column":17},"end":{"row":28,"column":18},"action":"insert","lines":["s"],"id":7}],[{"start":{"row":28,"column":18},"end":{"row":28,"column":19},"action":"insert","lines":["e"],"id":8}],[{"start":{"row":28,"column":19},"end":{"row":28,"column":20},"action":"insert","lines":["l"],"id":9}],[{"start":{"row":28,"column":20},"end":{"row":28,"column":21},"action":"insert","lines":["f"],"id":10}],[{"start":{"row":28,"column":21},"end":{"row":28,"column":22},"action":"insert","lines":["."],"id":11}],[{"start":{"row":21,"column":21},"end":{"row":21,"column":30},"action":"remove","lines":["positives"],"id":12},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["e"],"id":13}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["g"],"id":14}],[{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["a"],"id":15}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":26},"action":"insert","lines":["t"],"id":16}],[{"start":{"row":21,"column":26},"end":{"row":21,"column":27},"action":"insert","lines":["i"],"id":17}],[{"start":{"row":21,"column":27},"end":{"row":21,"column":28},"action":"insert","lines":["v"],"id":18}],[{"start":{"row":21,"column":28},"end":{"row":21,"column":29},"action":"insert","lines":["e"],"id":19}],[{"start":{"row":21,"column":29},"end":{"row":21,"column":30},"action":"insert","lines":["s"],"id":20}],[{"start":{"row":27,"column":62},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":28,"column":0},"end":{"row":28,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":28,"column":8},"end":{"row":28,"column":49},"action":"insert","lines":["tokenizer = nltk.tokenize.TweetTokenizer("],"id":22}],[{"start":{"row":28,"column":49},"end":{"row":28,"column":50},"action":"insert","lines":[")"],"id":23}],[{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"remove","lines":["."],"id":24}],[{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"remove","lines":["f"],"id":25}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"remove","lines":["l"],"id":26}],[{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"remove","lines":["e"],"id":27}],[{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"remove","lines":["s"],"id":28}],[{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"insert","lines":["s"],"id":29}],[{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"insert","lines":["e"],"id":30}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":["l"],"id":31}],[{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"insert","lines":["f"],"id":32}],[{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["."],"id":33}],[{"start":{"row":28,"column":0},"end":{"row":29,"column":46},"action":"remove","lines":["        tokenizer = nltk.tokenize.TweetTokenizer()","        tokens = self.tokenizer.tokenize(text)"],"id":34},{"start":{"row":28,"column":0},"end":{"row":29,"column":41},"action":"insert","lines":["        tokenizer = nltk.tokenize.TweetTokenizer()","        tokens = tokenizer.tokenize(text)"]}],[{"start":{"row":3,"column":40},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":35}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":3,"column":40},"end":{"row":3,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1512555705710,"hash":"e5ed5317b59d6ec104ddf1f9451a6c96e92696f9"}