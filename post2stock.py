from textblob import TextBlob
from nltk.stem.snowball import EnglishStemmer

def nouns_array_of_txt(text:str):
    candidate_arr = TextBlob(text).noun_phrases
    result_arr = []
    for candidate in candidate_arr:
        for word in candidate.split():
            result_arr.append(word)
    return result_arr

def nouns_correlation(post_noun_arr,stock_noun_arr):
    stemmer = EnglishStemmer()
    # Pre-process stock_arr to reduce running time
    for s in stock_noun_arr:
        s = stemmer.stem(s)
    distinct_noun_count = 0
    total_noun_count = 0
    appeared_noun_arr = []
    for p_noun in post_noun_arr:
        stemmer.stem(p_noun) # reduces a word to its dictionary form
        for s_noun in stock_noun_arr:
            if p_noun == s_noun: 
                if not s_noun in appeared_noun_arr:
                    appeared_noun_arr.append(s_noun)
                total_noun_count += 1
    distinct_noun_count = len(appeared_noun_arr)
    # Distinct overlapped n. * (total overlapped n. / total n.) : n. is Post_noun
    return distinct_noun_count * (total_noun_count / len(post_noun_arr))
            