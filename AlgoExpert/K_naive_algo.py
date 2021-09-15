from collections import defaultdict
import math


class MultinomialNB:
    def __init__(self, articles_per_tag):
        self.articles_per_tag = articles_per_tag
        self.alpha = 1
        self.priors_per_tag = {}
        self.tags = articles_per_tag.keys()
        self.likelihoods_per_tag_per_word = {}
        self.train()

    def train(self):
        # Calculate prior for each tag  = number of articles per tag / total number of articles across all tags
        tag_count_map = {tag: len(self.articles_per_tag[tag]) for tag in self.tags}
        self.priors_per_tag = {tag: tag_count_map[tag] / sum(tag_count_map.values()) for tag in self.tags}
        self. likelihoods_per_tag_per_word = self.__get_word_likelihoods_per_tag()

    def predict(self, article):
        posterior_per_tag = {tag: math.log(prior) for tag, prior in self.priors_per_tag.items()}

        for word in article:
            for tag in self.tags:
                posterior_per_tag[tag] = posterior_per_tag[tag] + math.log(
                    self.likelihoods_per_tag_per_word[word][tag]
                )
        return posterior_per_tag

    def __get_word_likelihoods_per_tag(self):
        word_frequencies_per_tag = defaultdict(lambda: {t: 0 for t in self.tags})
        total_word_count_per_tag = defaultdict(int)
        for tag in self.tags:
            for article in self.articles_per_tag[tag]:
                for word in article:
                    word_frequencies_per_tag[word][tag] += 1
                    total_word_count_per_tag[tag] += 1

        word_likelihoods_per_tag = defaultdict(lambda: {t: 0.5 for t in self.tags})
        for word, tags_map in word_frequencies_per_tag.items():
            for tag in tags_map.keys():
                word_likelihoods_per_tag[word][tag] = (word_frequencies_per_tag[word][tag] + 1 * self.alpha) / (
                    total_word_count_per_tag[tag] + 2 * self.alpha)

        return word_likelihoods_per_tag

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