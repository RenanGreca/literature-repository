import json
from posixpath import split
from unidecode import unidecode

papers = []
authors_set = {}
authors_list = []
with open("../_data/primaries.json") as input_file:
    primaries = json.load(input_file)
with open("../_data/secondaries.json") as input_file:
    secondaries = json.load(input_file)

papers = primaries + secondaries
for paper in papers:
    author_string = paper['authors']
    authors = author_string.split(";")
    for author in authors:
        author = author.strip(" ")
        if "," not in author:
            print("Incorrect formatting for author: "+author)
        author_key = unidecode(author)
        author_key = author_key.replace(",", "").replace(".", "").replace(" ", "_").lower()
        if author_key not in authors_set:
            authors_set[author_key] = {
                "key": author_key,
                "name": author,
                "type": 'author',
                "papers": [
                    paper['bibtex']
                ]
            }
        else:
            authors_set[author_key]["papers"].append(paper['bibtex'])

sorted_dict = {key: value for key, value in sorted(authors_set.items(), key = lambda e: e[0])}

# print(sorted_dict.keys())

with open("../_data/authors.json", "w") as output_file:
    output_file.write(json.dumps(list(sorted_dict.values())))

# for key, value in sorted_dict.items():
#     with open("../_data/authors.json", "w") as output_file:
#         output_file.write(json.dumps(value))