import nltk

sentence = "here is a very normal, sentence written in 2022 now that's easy wasn't it."
# this tokenizer uses regex and avoids capturing whitespace
# tokenizer = nltk.RegexpTokenizer(r'\w+|$[0-9.]+|\S+')
# words = tokenizer.tokenize(sentence)
# print(words)


# this tokenier helps with stemming by separating contractions into their respective words
tokenizer = nltk.TreebankWordTokenizer()
words = tokenizer.tokenize(sentence)
print(words)


# this tokenizer tokenizes informal speech from online media
message = "yo yo yo @something whaaaat are we eveeeeen doing here wtf"
casual_tokens = nltk.casual_tokenize(message)
print(casual_tokens)
# this strips userhandles from text and gets rid of a few repeated letters
# but for some reason it does not get rid of all repeated letters, idk why
stripped_tokens = nltk.casual_tokenize(message, reduce_len=True, strip_handles=True)
print(stripped_tokens)

# this creates 2grams
# to create ngrams with nltk, you have to tokenize the message first
message2 = "thomas jefferson began building monticello at the age of 29."
words2 = tokenizer.tokenize(message2)
two_grams = list(nltk.ngrams(words2, 2))
print(two_grams)

# stop words are words that occur so frequently in the language that they're not useful to keep track of
# case normalization is when you change everything to lowercase so that you don't end
# up with duplicate tokens (e.g, "APLLE" and "apple")
# sometimes you want distinct tokens based on capitalization tho (e.g., "doctor" and "Doctor")
# this lowercases everything in a document
tokens = ["House", "Visitor", "appleSauce"]
normalized_tokens = [x.lower() for x in tokens]
print(normalized_tokens)


# sometimes it is better to only lowercase the first word of every sentence, because
# this preserves important capitals like proper names (e.g., "Joe" and "Smith")
# this also prevents the Joe in "Joe Smith" from being confused with the joe in "cup of joe"
# this still causes problems though if a proper name starts a sentence
# you can lose a lot of valuable data if you case normalize, many NLP pipelines don't case normalize
# for this very reason


# dimension reduction helps generalize your language model, stemming helps a program
# detect that "houses" "housing" and "house" are all related to one another


