from utils import most_common_words, most_common_nouns, create_bag_of_words, similarity, nearest_coef, nearest_cos, change_to_emb
from dataset import load_data, load_file_to_string, load_files_to_string, load_vectors

data = 'data/shows'
number_of_words = 100
max_len = 20000

emb_dir = 'embedding/'
emb_file = 'wiki.en'

# batman_beyond = most_common_nouns(load_file_to_string(data+"/Batman Beyond/S1-Season 1, Episode 01 - Rebirth (Part 1)-eng.txt"),
#                                   number_of_words)
# batman_animated = most_common_nouns(load_file_to_string(data+"/Batman: The Animated Series/S1-Batman.The.Animated.Series.15.The.Cat.and.the.Claw.Part.I-OLLIE.eng.txt"),
#                                     number_of_words)
# dharma_greg = most_common_nouns(load_file_to_string(data+"/Dharma & Greg/S1-Dharma.And.Greg.S01E01.DVDRip.XviD-FoV.txt"),
#                                 number_of_words)

batman_beyond = most_common_nouns(load_files_to_string(data+"/Batman Beyond"),
                                  number_of_words)
batman_animated = most_common_nouns(load_files_to_string(data+"/Batman: The Animated Series"),
                                    number_of_words)
dharma_greg = most_common_nouns(load_files_to_string(data+"/Dharma & Greg"),
                                number_of_words)

teen_titans = most_common_nouns(load_files_to_string(data+"/Teen Titans"),
                                number_of_words)

will_grace = most_common_nouns(load_files_to_string(data+"/Will & Grace"),
                                number_of_words)

superman = most_common_nouns(load_files_to_string(data+"/Superman"),
                                number_of_words)

supergirl = most_common_nouns(load_files_to_string(data+"/Supergirl"),
                                number_of_words)


batman_beyond_list = [d[0] for d in batman_beyond]
batman_animated_list = [d[0] for d in batman_animated]
dharma_greg_list = [d[0] for d in dharma_greg]
teen_titans_list = [d[0] for d in teen_titans]
will_grace_list = [d[0] for d in will_grace]
superman_list = [d[0] for d in superman]
supergirl_list = [d[0] for d in supergirl]

# print(len(load_files_to_string(data+"/Batman Beyond")))
# print(len(load_files_to_string(data+"/Batman: The Animated Series")))
# print(len(load_files_to_string(data+"/Dharma & Greg")))
# print(len(load_files_to_string(data+"/Teen Titans")))
# print(len(load_files_to_string(data+"/Will & Grace")))
# print(len(load_files_to_string(data+"/Superman")))
# print(len(load_files_to_string(data+"/Supergirl")))

sum_list = batman_beyond_list + batman_animated_list + dharma_greg_list + teen_titans_list + will_grace_list + \
           superman_list + supergirl_list
all_words = list(set(sum_list))

batman_beyond_bow = create_bag_of_words(batman_beyond, all_words)
batman_animated_bow = create_bag_of_words(batman_animated, all_words)
dharma_greg_bow = create_bag_of_words(dharma_greg, all_words)
teen_titans_bow = create_bag_of_words(teen_titans, all_words)
will_grace_bow = create_bag_of_words(will_grace, all_words)
superman_bow = create_bag_of_words(superman, all_words)
supergirl_bow = create_bag_of_words(supergirl, all_words)

print("Batman i batman")
print(similarity(batman_beyond_bow, batman_animated_bow))
print("Batman i dharma")
print(similarity(batman_beyond_bow, dharma_greg_bow))
print("Will i dharma")
print(similarity(will_grace_bow, dharma_greg_bow))
print("Batman i teen titans")
print(similarity(batman_beyond_bow, teen_titans_bow))
print("Superman i supergirl")
print(similarity(superman_bow, supergirl_bow))
print("Superman i dharma")
print(similarity(superman_bow, dharma_greg_bow))
print("Superman i batman")
print(similarity(superman_bow, batman_animated_bow))

bow_list = [("Batman Beyond", batman_beyond_bow), ("Batman Animated", batman_animated_bow), ("Dharma i greg", dharma_greg_bow),
            ("Will and Grace", will_grace_bow), ("Teen titans", teen_titans_bow), ("Superman", superman_bow), ("Supergirl", supergirl_bow)]

print("Batman Beyond:")
print(nearest_cos(batman_beyond_bow, bow_list, "Batman Beyond"))
print("-----------------------")
print("Batman Animated:")
print(nearest_cos(batman_animated_bow, bow_list, "Batman Animated"))
print("-----------------------")
print("Dharma i greg:")
print(nearest_cos(dharma_greg_bow, bow_list, "Dharma i greg"))
print("-----------------------")
print("Will and Grace:")
print(nearest_cos(will_grace_bow, bow_list, "Will and Grace"))
print("-----------------------")
print("Teen titans:")
print(nearest_cos(teen_titans_bow, bow_list, "Teen titans"))
print("-----------------------")
print("Superman:")
print(nearest_cos(superman_bow, bow_list, "Superman"))
print("-----------------------")
print("Supergirl:")
print(nearest_cos(supergirl_bow, bow_list, "Supergirl"))
print("-----------------------")
