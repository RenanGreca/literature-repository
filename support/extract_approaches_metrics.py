import csv
import json
from unidecode import unidecode

def split_papers (papers_string):
    if (len(papers_string) == 0):
        return []
    return papers_string.split(", ")

papers = []
with open("bibtex_list.txt") as input_file:
    # reader = csv.reader(input_file) #, delimiter=',', quitechar='"')
    # next(reader)
    # next(reader)
    for row in input_file.readlines():
        papers.append(row.replace("\n", ""))

metrics_map = []
approaches_map = []

effectiveness = "Effectiveness"
efficiency = "Efficiency"
other = "Other"

with open("metrics.csv") as metrics_file:
    reader = csv.reader(metrics_file)
    next(reader)
    metrics = {}
    
    for paper in papers:
        metrics[paper] = {efficiency: [], effectiveness: [], other: []}
    for row in reader:
        for paper in papers:
            if (effectiveness in row[0]):
                if (paper in row[2]) or (paper in row[3]) or (paper in row[4]) or (paper in row[5]) or (paper in row[6]):
                    metrics[paper][effectiveness].append(row[1])
            if (efficiency in row[0]):
                if (paper in row[2]) or (paper in row[3]) or (paper in row[4]) or (paper in row[5]) or (paper in row[6]):
                    metrics[paper][efficiency].append(row[1])
            if (other in row[0]):
                if (paper in row[2]) or (paper in row[3]) or (paper in row[4]) or (paper in row[5]) or (paper in row[6]):
                    metrics[paper][other].append(row[1])

        
        metric_key = unidecode(row[1])
        metric_key = ( metric_key.replace(",", "").replace(".", "")
                        .replace("/","_").replace("(","").replace(")","")
                        .replace(" ", "_").lower() )        
        metric = {
            "key": metric_key,
            "type": 'metric',
            "category": row[0],
            "name": row[1],
            "papers": {
                "tcp": split_papers(row[3]),
                "tcs": split_papers(row[4]),
                "tsr": split_papers(row[5]),
                "tsa": split_papers(row[6])
            },
            "description": row[7]
        }

        metrics_map.append(metric)
        

    # print ("Effectiveness metrics:")
    # for paper in papers:
    #     print(", ".join(metrics[paper][effectiveness]))
    
    # print ("Efficiency metrics:")
    # for paper in papers:
    #     print(", ".join(metrics[paper][efficiency]))

    # print ("Other metrics:")
    # for paper in papers:
    #     print(", ".join(metrics[paper][other]))

information = "Information"
algorithm = "Algorithm"

with open("approaches.csv") as metrics_file:
    reader = csv.reader(metrics_file)
    next(reader)
    approaches = {}
    for paper in papers:
        approaches[paper] = {information: [], algorithm: []}
    for row in reader:
        for paper in papers:
            if (information in row[0]):
                if (paper in row[2]) or (paper in row[3]) or (paper in row[4]) or (paper in row[5]) or (paper in row[6]):
                    approaches[paper][information].append(row[1])
            if (algorithm in row[0]):
                if (paper in row[2]) or (paper in row[3]) or (paper in row[4]) or (paper in row[5]) or (paper in row[6]):
                    approaches[paper][algorithm].append(row[1])

        approach_key = unidecode(row[1])
        approach_key = ( approach_key.replace(",", "").replace(".", "")
                        .replace("/","_").replace("(","").replace(")","")
                        .replace(" ", "_").lower() )        
        approach = {
            "key": approach_key,
            "type": 'approach',
            "category": row[0],
            "name": row[1],
            "papers": {
                "tcp": split_papers(row[3]),
                "tcs": split_papers(row[4]),
                "tsr": split_papers(row[5]),
                "tsa": split_papers(row[6])
            },
            "description": row[7]
        }

        approaches_map.append(approach)

    # print (information, " approaches:")
    # for paper in papers:
    #     print(", ".join(metrics[paper][information]))
    
    # print (algorithm, " metrics:")
    # for paper in papers:
    #     print(", ".join(metrics[paper][algorithm]))

with open("../_data/metrics.json", "w") as output_file:
    output_file.write(json.dumps(metrics_map))

with open("../_data/approaches.json", "w") as output_file:
    output_file.write(json.dumps(approaches_map))