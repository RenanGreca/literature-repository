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
with open("Secondary Study - Final List.csv") as input_file:
    reader = csv.reader(input_file) #, delimiter=',', quitechar='"')
    next(reader)
    next(reader)
    for row in reader:
        paper = {}

        paper['type'] = 'primary'
        paper['year'] = row[0]
        paper['authors'] = row[1]
        paper['author_keys'] = get_author_keys(paper['authors'])
        paper['title'] = row[2]
        paper['bibtex'] = row[3]
        paper['abstract'] = row[4]
        paper['published_in'] = row[5]
        paper['publisher'] = row[6]
        paper['doi'] = row[8]
        paper['date'] = row[9]

        paper['tcp'] = row[17]
        paper['tcs'] = row[18]
        paper['tsr'] = row[19]
        paper['tsa'] = row[20]

        paper['ind_motivation'] = row[23]
        paper['ind_evaluation'] = row[24]
        paper['exp_subjects'] = row[25]
        paper['ind_partner'] = row[26]
        paper['ind_author'] = row[27]
        paper['prac_feedback'] = row[28]
        paper['avai_tool'] = row[29]
        paper['put_practice'] = row[30]

        paper['suppl_url'] = row[31]

        paper['approach'] = row[34]
        paper['metrics'] = row[35]
        paper['open_challenges'] = row[36]
        
        papers.append(paper)

for paper in papers:
    with open("../_data/primary_jsons/"+paper['bibtex']+".json", "w") as output_file:
        output_file.write(json.dumps(paper))

with open("../_data/primaries.json", "w") as output_file:
    output_file.write(json.dumps(papers))

papers = []
with open("Tertiary Study - Data Collection.csv") as input_file:
    reader = csv.reader(input_file) #, delimiter=',', quitechar='"')
    next(reader)
    next(reader)
    for row in reader:
        paper = {}

        paper['type'] = 'secondary'
        paper['year'] = row[0]
        paper['authors'] = row[1]
        paper['author_keys'] = get_author_keys(paper['authors'])
        paper['title'] = row[2]
        paper['bibtex'] = row[7]
        paper['abstract'] = row[3]
        paper['published_in'] = row[4]
        paper['publisher'] = row[5]
        paper['doi'] = row[8]
        paper['date'] = row[9]

        paper['tcp'] = row[15]
        paper['tcs'] = row[16]
        paper['tsr'] = row[17]
        paper['tsa'] = row[18]

        paper['paper_count'] = row[19]
        paper['years_covered'] = row[21]
        paper['systematic'] = row[22]

        paper['approach'] = row[27]
        paper['metrics'] = row[28]
        paper['conclusions'] = row[29]
        paper['open_challenges'] = row[30]
        
        papers.append(paper)

for paper in papers:
    with open("../_data/secondary_jsons/"+paper['bibtex']+".json", "w") as output_file:
        output_file.write(json.dumps(paper))

with open("../_data/secondaries.json", "w") as output_file:
    output_file.write(json.dumps(papers))