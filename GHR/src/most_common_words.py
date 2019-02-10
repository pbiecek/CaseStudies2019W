from utils import  most_common_nouns
from files import load_files_to_string, load_paths_from_dir

# Settings
data = 'data/shows'
number_of_words = 100
show_list = ["Taboo", "Game of Thrones"]

# Load names and paths of shows from chosen directory
names, paths = load_paths_from_dir(data, show_list)
print(names)

# Most common words in tv show
movies_common_words = []
print("Most common words.")
for path in paths:
    print(path)
    print(most_common_nouns(load_files_to_string(path, how_many=10), number_of_words))
