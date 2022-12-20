# coding=utf8

# Receives a CSV file from our Google Sheet and re-organizes the data that should be displayed on the website.

import csv
import json
from unidecode import unidecode

def get_author_keys(author_string):
    authors_list = []

    authors = author_string.split(";")
    for author in authors:
        author = author.strip(" ")
        if "," not in author:
            print("Incorrect formatting for author: "+author)
        author_key = unidecode(author)
        author_key = author_key.replace(",", "").replace(".", "").replace(" ", "_").lower()
        authors_list.append(author_key)
    
    return authors_list


papers = []
with open("primaries.csv") as input_file:
    reader = csv.reader(input_file) #, delimiter=',', quitechar='"')
    next(reader)
    next(reader)
    for row in reader:
        paper = {}

        paper['type'] = 'primary'
        i = 0
        paper['year'] = row[i]
        i += 1
        paper['authors'] = row[i]
        paper['author_keys'] = get_author_keys(paper['authors'])
        i += 1
        paper['title'] = row[i]
        i += 1
        paper['bibtex'] = row[i]
        i += 1
        paper['abstract'] = row[i]
        i += 1
        paper['published_in'] = row[i]
        i += 1
        paper['publisher'] = row[i]
        i += 2
        paper['doi'] = row[i]
        i += 1
        paper['date'] = row[i]

        i += 8
        paper['tcp'] = row[i]
        i += 1
        paper['tcs'] = row[i]
        i += 1
        paper['tsr'] = row[i]
        i += 1
        paper['tsa'] = row[i]

        i += 3
        paper['ind_motivation'] = row[i]
        i += 1
        paper['ind_evaluation'] = row[i]
        i += 1
        paper['exp_subjects'] = row[i]
        i += 1
        paper['prog_language'] = row[i]
        i += 1
        paper['ind_partner'] = row[i]
        i += 1
        paper['ind_author'] = row[i]
        i += 1
        paper['prac_feedback'] = row[i]
        i += 1
        paper['avai_tool'] = row[i]
        i += 1
        paper['put_practice'] = row[i]
        i += 1
        paper['suppl_url'] = row[i]

        i += 3
        paper['approach'] = row[i]
        i += 1
        paper['info_approach'] = row[i]
        i += 1
        paper['alg_approach'] = row[i]
        i += 1
        paper['metrics'] = row[i]
        i += 1
        paper['effe_metrics'] = row[i]
        i += 1
        paper['effi_metrics'] = row[i]
        i += 1
        paper['other_metrics'] = row[i]
        i += 1
        paper['open_challenges'] = row[i]
        
        papers.append(paper)

for paper in papers:
    with open("../_data/primary_jsons/"+paper['bibtex']+".json", "w") as output_file:
        output_file.write(json.dumps(paper))

with open("../_data/primaries.json", "w") as output_file:
    output_file.write(json.dumps(papers))

papers = []
with open("secondaries.csv") as input_file:
    reader = csv.reader(input_file) #, delimiter=',', quitechar='"')
    next(reader)
    next(reader)
    for row in reader:
        paper = {}

        paper['type'] = 'secondary'
        i = 0
        paper['year'] = row[i]
        i += 1
        paper['authors'] = row[i]
        paper['author_keys'] = get_author_keys(paper['authors'])
        i += 1
        paper['title'] = row[i]
        i += 1
        paper['abstract'] = row[i]
        i += 1
        paper['published_in'] = row[i]
        i += 1
        paper['publisher'] = row[i]
        i += 1
        paper['bibtex'] = row[i]
        i += 1
        paper['doi'] = row[i]
        i += 1
        paper['date'] = row[i]

        i += 1
        paper['tcp'] = row[i]
        i += 1
        paper['tcs'] = row[i]
        i += 1
        paper['tsr'] = row[i]
        i += 1
        paper['tsa'] = row[i]

        i += 1
        paper['paper_count'] = row[i]
        i += 1
        paper['years_covered'] = row[i]
        i += 1
        paper['systematic'] = row[i]

        i += 1
        paper['context'] = row[i]
        # paper['approach'] = row[27]
        # paper['metrics'] = row[28]
        # paper['conclusions'] = row[29]
        # paper['open_challenges'] = row[30]
        
        papers.append(paper)

for paper in papers:
    with open("../_data/secondary_jsons/"+paper['bibtex']+".json", "w") as output_file:
        output_file.write(json.dumps(paper))

with open("../_data/secondaries.json", "w") as output_file:
    output_file.write(json.dumps(papers))