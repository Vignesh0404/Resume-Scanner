

import re, operator, sys


def Is_Number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False


def Load_Stop_Words_List(stop_word_file):
    stop_words = []
    for line in open(stop_word_file):
        if line.strip()[0:1] != "#":
            for word in line.split():  # in case more than one per line
                stop_words.append(word)
    return stop_words


def Word_Seperation(text, min_word_return_size):
    splitter = re.compile('[^a-zA-Z0-9_\\+\\-/]')
    words = []
    for single_word in splitter.split(text):
        current_word = single_word.strip().lower()
        #leave numbers in phrase, but don't count as words, since they tend to invalidate scores of their phrases
        if len(current_word) > min_word_return_size and current_word != '' and not Is_Number(current_word):
            words.append(current_word)
    return words


def Split_Sentences(text):
    sentence_delimiters = re.compile(u'[.!?,;:\t\\\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
    sentences = sentence_delimiters.split(text)
    return sentences


def Build_Stop_Word_Regex(stop_word_file_path):
    stop_word_list = Load_Stop_Words_List(stop_word_file_path)
    stop_word_regex_list = []
    for word in stop_word_list:
        word_regex = r'\b' + word + r'(?![\w-])'  # added look ahead for hyphen
        stop_word_regex_list.append(word_regex)
    stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
    return stop_word_pattern


def Generate_Candidate_Keywords(sentence_list, stopword_pattern):
    phrase_list = []
    for s in sentence_list:
        tmp = re.sub(stopword_pattern, '|', s.strip())
        phrases = tmp.split("|")
        for phrase in phrases:
            phrase = phrase.strip().lower()
            if phrase != "":
                phrase_list.append(phrase)
    return phrase_list


def Calculate_Word_Scores(phraseList):
    word_frequency = {}
    word_degree = {}
    for phrase in phraseList:
        word_list = Word_Seperation(phrase, 0)
        word_list_length = len(word_list)
        word_list_degree = word_list_length - 1
        for word in word_list:
            word_frequency.setdefault(word, 0)
            word_frequency[word] += 1
            word_degree.setdefault(word, 0)
            word_degree[word] += word_list_degree
    for item in word_frequency:
        word_degree[item] = word_degree[item] + word_frequency[item]
    word_score = {}
    for item in word_frequency:
        word_score.setdefault(item, 0)
        word_score[item] = word_degree[item] / (word_frequency[item] * 1.0)
    return word_score


def Generate_Candidate_Keyword_Scores(phrase_list, word_score):
    keyword_candidates = {}
    for phrase in phrase_list:
        keyword_candidates.setdefault(phrase, 0)
        word_list = Word_Seperation(phrase, 0)
        candidate_score = 0
        for word in word_list:
            candidate_score += word_score[word]
        keyword_candidates[phrase] = candidate_score
    return keyword_candidates


class Rake(object):
    def __init__(self, stop_words_path):
        self.stop_words_path = stop_words_path
        self.__stop_words_List_pattern = Build_Stop_Word_Regex(stop_words_path)

    def run(self, text):
        sentence_list = Split_Sentences(text)
        phrase_list = Generate_Candidate_Keywords(sentence_list, self.__stop_words_List_pattern)
        word_scores = Calculate_Word_Scores(phrase_list)
        keyword_candidates = Generate_Candidate_Keyword_Scores(phrase_list, word_scores)
        sorted_keywords = sorted(keyword_candidates.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_keywords


def main():
    text = sys.argv[1]
    sentenceList = Split_Sentences(text)
    stoppath = "db\\Stop_Word_List.txt"
    stopwordpattern = Build_Stop_Word_Regex(stoppath)
    phraseList = Generate_Candidate_Keywords(sentenceList, stopwordpattern)
    wordscores = Calculate_Word_Scores(phraseList)
    keywordcandidates = Generate_Candidate_Keyword_Scores(phraseList, wordscores)
    sortedKeywords = sorted(keywordcandidates.items(), key=operator.itemgetter(1), reverse=True)
    totalKeywords = len(sortedKeywords)
    rake = Rake("db\\Stop_Word_List.txt")
    keywords = rake.run(text)
    print (keywords)


if __name__ == '__main__':
    print()
    main()
