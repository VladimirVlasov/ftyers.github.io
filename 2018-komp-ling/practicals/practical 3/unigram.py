from tqdm import tqdm
from numpy import random
import re


class unigram_model():
    def __init__(self, file):
        self.freq_of_word = {}
        self.freq_of_word_tag = {}
        self.train(file)
        del self.freq_of_word

    def add_word(self, word, tag):
        if word not in self.freq_of_word:
            self.freq_of_word[word] = 0
            self.freq_of_word_tag[word] = {}
        if tag not in self.freq_of_word_tag[word]:
            self.freq_of_word_tag[word][tag] = 0
        self.freq_of_word[word] = self.freq_of_word[word] + 1
        self.freq_of_word_tag[word][tag] = self.freq_of_word_tag[word][tag] + 1

    def train(self, file):
        with open(file) as train_file:
            for line in tqdm(train_file):
                if line[0] in '1234567890':
                    splited = line.split('\t')
                    word = splited[1].lower()
                    tag = splited[3]
                    self.add_word(word, tag)
        self.finish_train()

    def finish_train(self):
        for word in self.freq_of_word:
            for tag in self.freq_of_word_tag[word]:
                self.freq_of_word_tag[word][tag] = self.freq_of_word_tag[word][tag] / self.freq_of_word[word]

    def predict_word(self, word):
        word = word.lower()
        if word in self.freq_of_word_tag:
            tags = []
            probs = []
            for tag, prob in self.freq_of_word_tag[word].items():
                tags.append(tag)
                probs.append(prob)
            return random.choice(tags, p=probs)
        else:
            return None

    def predict_for_line_with_stdout(self, line):
        print('#text = {}'.format(line))
        counter = 0
        for word in re.findall(r'[\w]+\b', line):
            counter += 1
            print('{}\t{}\t{}'.format(counter, word, self.predict_word(word)))

    def transform_file(self, file):
        with open(file) as input_file:
            for line in input_file:
                self.predict_for_line_with_stdout(line)