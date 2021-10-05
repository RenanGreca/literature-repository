---
layout: post
title:  "Cost-benefit analysis of using dependency knowledge at integration testing"
date:   2015-11-11 09:48:54 +0200
categories: jekyll update

year: 2016
authors: "Tahvili, S; Bohlin, M; Saadatmand, M; Larsson, S; Afzal, W; Sundmark, D"
publisher: "Profess 2016"
doi: https://doi.org/10.1007/978-3-319-49094-6_17

tcp: true
tcs: false
tsr: false
tsa: false
context: "Embedded systems; NL test cases"

ind_motivation: true
ind_evaluation: true
ind_author: false
prac_feedback: false
avai_tool: true
put_practice: false

additional_url: false

approach: "the paper evaluates the ROI for the TCP approach proposed in row 42; here they build a cost model and compare the costs of using TCP or not. Note that the TCP uses dependencies among tests that are identifies manually"
metrics: "ROI"
open_challenges: "- do study on real data and not on simulation
-consider other criteria for TCP"
---

In software system development, testing can take considerable time and resources, and there are numerous examples in the literature of how to improve the testing process. In particular, methods for selection and prioritization of test cases can play a critical role in efficient use of testing resources. This paper focuses on the problem of selection and ordering of integration-level test cases. Integration testing is performed to evaluate the correctness of several units in composition. Further, for reasons of both effectiveness and safety, many embedded systems are still tested manually. To this end, we propose a process, supported by an online decision support system, for ordering and selection of test cases based on the test result of previously executed test cases. To analyze the economic efficiency of such a system, a customized return on investment (ROI) metric tailored for system integration testing is introduced. Using data collected from the development process of a large-scale safety-critical embedded system, we perform Monte Carlo simulations to evaluate the expected ROI of three variants of the proposed new process. The results show that our proposed decision support system is beneficial in terms of ROI at system integration testing and thus qualifies as an important element in improving the integration testing process. © Springer International Publishing AG 2016.