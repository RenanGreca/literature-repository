---
layout: page
title: Contribute
permalink: /contribute/

tags: help
---

This repository is meant to be live and continually updated according to advancements in the literature.
If you have published or read a paper that fits this repository, we kindly encourage you to submit this paper to our repository.

Contributions are made via GitHub Pull Requests.
You can create a Pull Request by forking the repository, making the necessary changes and using the GitHub Pull Request tool.
For further information on how to create and use Pull Request, please refer to the [GitHub documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

To add a paper to the repository, please create a new (JSON)[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON] file under `_data/jsons`.
The filename must adhere to the BibTeX convention, that is, `[author surname]_[first word of title]_[year].json`.

Please use the following template to add an entry:

```
{
    "year": 2021,
    "authors": "Greca, Renan; Miranda, Breno; Bertolino, Antonia",
    "title": "Test of GitHub action",
    "bibtex": "author_test_2021",
    "abstract": "Something long",
    "published_in": "2016 42th Euromicro Conference on Software Engineering and Advanced Applications (SEAA)",
    "publisher": "IEEE",
    "source": "Query",
    "doi": "https://doi.org/10.1109/SEAA.2016.29",
    "date": "2016-10-18",
    "categories": "Orchestration technique",
    "tcp": "X",
    "tcs": "",
    "tsr": "",
    "tsa": "",
    "context": "General",
    "ind_motivation": "FALSE",
    "ind_evaluation": "TRUE",
    "exp_subjects": "Undisclosed system from Toshiba (300 TCs)",
    "ind_partner": "Toshiba (Japan)",
    "ind_author": "TRUE",
    "prac_feedback": "FALSE",
    "avai_tool": "FALSE",
    "put_practice": "MAYBE",
    "suppl_url": "",
    "included": "TRUE",
    "approach": "Similarity-based",
    "metrics": "GLC (number of versions in which a certain test T was not run), failure rate",
    "open_challenges": "Apply in other software domains and compare with other TCP techniques."
  }
```