---
layout: page
title: Contribute
permalink: /contribute/

tags: help
---

This repository is meant to be live and continually updated according to advancements in the literature.
If you have published or read a paper that fits this repository, we kindly encourage you to submit this paper to our repository.

Contributions are made via [GitHub pull requests](https://github.com/RenanGreca/literature-repository/pulls).
You can create a Pull Request by forking the repository, making the necessary changes and using the GitHub Pull Request tool.
For further information on how to create and use Pull Request, please refer to the [GitHub documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

To add a paper to the repository, please create a new (JSON)[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON] file under `_data/primary_jsons`.
The filename must adhere to the BibTeX convention, that is, `[author surname]_[first word of title]_[year].json`.

Please use the following template to add an entry:

```
{
    "year": 2021,
    "authors": "Greca, Renan; Miranda, Breno; Bertolino, Antonia",
    "title": "Sample title",
    "bibtex": "author_test_2021",
    "abstract": "Something long",
    "published_in": "Name of the conference",
    "publisher": "Name of the publisher (e.g. IEEE, ACM, etc.)",
    "source": "Query",
    "doi": "XXXX/XXXXXXXXX (do not include http://doi.org/)",
    "date": "YYYY-mm-dd",
    "tcp": "X (if paper covers TCP, or else leave blank)",
    "tcs": "X (if paper covers TCS, or else leave blank)",
    "tsr": "X (if paper covers TSR, or else leave blank)",
    "tsa": "X (if paper covers TSA, or else leave blank)",
    "ind_motivation": "TRUE if paper has strong industrial motivation, FALSE otherwise.",
    "ind_evaluation": "TRUE if paper has industrial-scale evaluation, FALSE otherwise.",
    "exp_subjects": "Brief description of subjects used for evaluation.",
    "ind_partner": "Name and country of industrial partner, if any.",
    "ind_author": "TRUE if paper has co-author(s) from industry, FALSE otherwise.",
    "prac_feedback": "TRUE if paper describes feedback from practitioners, FALSE otherwise.",
    "avai_tool": "TRUE if paper contains a link to a tool or replication package, FALSE otherwise.",
    "put_practice": "TRUE if the paper's technique was put into practice on real software, FALSE otherwise.",
    "suppl_url": "URL of tool/replication package/dataset, if any",
    "approach": "Information and/or algorithm approach(es) used by the technique.",
    "metrics": "Effectiveness and/or efficiency metric(s) used to evaluate the technique.",
    "open_challenges": "Open challenges and/or future works listed by the author(s)."
  }
```

If you have any questions or experience difficulties during the process, please file an issue
on the project's [GitHub repository](https://github.com/RenanGreca/literature-repository).