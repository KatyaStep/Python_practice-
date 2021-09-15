from collections import defaultdict
from collections import Counter
import math


class MultinomialNB:
    def __init__(self, articles_per_tag):
        self.articles_per_tag = articles_per_tag
        self.prior_per_tag = None
        self.tags = articles_per_tag.keys()
        self.likelihoods_per_tag = {}
        self.train()

    def train(self):
        # Calculate prior for each tag  = number of articles per tag / total number of articles across all tags
        prior_per_tag = defaultdict()
        prior_denominator = 0

        for key in self.tags:
            prior_denominator += len(self.articles_per_tag[key])

        for key in self.tags:
            prior_per_tag[key] = (len(self.articles_per_tag[key]) / prior_denominator)

        # Calculate likelihoods of each word per tag = how many times each word appears in the tag /
        # total number of words in the tag
        laplacian_smooth_numerator = 1
        laplacian_smooth_denominator = 2
        word_in_tag = defaultdict(lambda: {j: 0 for j in self.tags})
        total_words_count_per_tag = defaultdict(int)

        likelihoods_per_tag = defaultdict(lambda: {t: 0.5 for t in self.articles_per_tag.keys()})

        for tag in self.tags:
            for article in self.articles_per_tag[tag]:
                for word in article:
                    word_in_tag[word][tag] += 1
                    total_words_count_per_tag[tag] += 1
                    # likelihoods_per_tag[tag][word] = 0

        for word, tags_map in word_in_tag.items():
            for category in tags_map.keys():
                likelihoods_per_tag[word][category] = (word_in_tag[word][category] + laplacian_smooth_numerator) / \
                                                     (total_words_count_per_tag[category] + laplacian_smooth_denominator)

        self.prior_per_tag = prior_per_tag
        self.likelihoods_per_tag = likelihoods_per_tag


    def predict(self, article):
        # total_likelihood = 0
        result = {tag: math.log(prior) for tag, prior in self.prior_per_tag.items()}

        assert self.prior_per_tag is not None
        assert self.likelihoods_per_tag is not None

        for word in article:
            for tag in self.tags:
                result[tag] = result[tag] + math.log((self.likelihoods_per_tag[word][tag]))

        return result

articles_per_tag = {
    "politics": [
        ['article', "writes", "Joel"],
        ["Distribution", "world", "following", "posted", "writes"]
    ],
    "sports": [
        ['article', "writes", "just", "wanted"],
        ["Phillies", "team", "salvaged", "their", "weekend"]
    ],
    "tech": [
        ['Thanks', "Steve", "your", "helpful"],
        ["Please", "unsubscribe", "This", "user", "program", "helpful"]
    ]
}

article_list = ["article", "writes", "while", "when", "owned", "Plus", "wanted", "upgrade",
                "memory", "just", "ordered", "toolkit", "from", "Macwarehouse", "something",
                "like", "included", "antistatic"]

mb = MultinomialNB(articles_per_tag)
print(mb.predict(article_list))


# {'politics': -18.221253719255465, 'sports': -17.621665185461044, 'tech': -20.742299415659335}