# OpenRAGBench diverse_500 Result

## Dataset
- Dataset: vectara/open_ragbench
- Subset: diverse_500
- Queries evaluated: 3045
- Indexed positive docs: 396
- Indexed hard-negative docs: 604
- Indexed sections: 18840
- top_k: 20
- Retriever: hashed TF-IDF 2048d, lexical (no paid embeddings)
- Reranker: None

## Headline
- **Strict Section Direct Retrieval Accuracy@10: 94.6%**

## Supporting
- Relaxed Document Accuracy@10: 99.7%
- MRR@10: 0.7374  |  MRR@20: 0.739
- nDCG@10 (strict section): 0.7887
- Zero-source rate: 0.0%
- latency p50/p95/p99: 418.5 / 606.9 / 1126.1 ms

## Strict@K / Relaxed@K (overall)
- @1: strict_section=61.8%, relaxed_doc=93.7%
- @3: strict_section=83.9%, relaxed_doc=98.4%
- @5: strict_section=89.5%, relaxed_doc=99.1%
- @10: strict_section=94.6%, relaxed_doc=99.7%
- @20: strict_section=96.9%, relaxed_doc=99.8%

## Breakdown by source (strict@10)
- text: strict@10=96.7%, relaxed@10=99.8% (n=1914)
- text-image: strict@10=90.8%, relaxed@10=99.9% (n=763)
- text-table: strict@10=92.6%, relaxed@10=100.0% (n=148)
- text-table-image: strict@10=90.9%, relaxed@10=98.2% (n=220)

## Breakdown by type (strict@10)
- abstractive: strict@10=93.6% (n=1793)
- extractive: strict@10=96.0% (n=1252)

## Supported vs multimodal-degraded
- Supported-only (text, text-table): strict@10=96.4% (n=2062)
- Multimodal-degraded (text-image, text-table-image): strict@10=90.8% (n=983)
- NOTE: images are indexed as base64 with no captions/OCR; our text-only retrieval stack cannot read image content, so multimodal queries are reported separately and excluded from the supported-only headline.

## Conclusion
- Score kind: text-only / supported (headline = all selected queries)
- Failed queries (top 20): see failures report
- Next fix: review top failed queries for systematic retrieval gaps.

## Top 20 failed queries
- 00d954d0-d8b6-40ab-9506-3d5e99ac929f [text/abstractive] (right_doc_wrong_section): In what way do $L^{2}$-spaces differ from classical function spaces like $L^{2}(\Omega, \m
- 015f84f5-d694-4fad-bfa5-d2f3687bcd52 [text/extractive] (right_doc_wrong_section): Is the accuracy of NVILA compromised for efficiency gains?
- 024b9722-075d-4f35-8769-0e1ad6d2747d [text/extractive] (right_doc_wrong_section): What is a Gaussian process (GP) characterized by?
- 02ab673a-fbd0-420a-9a18-9e3a24de8b88 [text-image/abstractive] (right_doc_wrong_section): How are beam patterns analyzed in radio telescopes?
- 02b7db12-057d-4e26-bf4c-8000888465da [text-table-image/abstractive] (right_doc_wrong_section): Why is it important to simulate gravitational wave events using data-driven distributions 
- 02e11dcd-d7d5-44a7-9116-6db96345ca6a [text-image/abstractive] (right_doc_wrong_section): How does the piecewise polynomial approximation contribute to function smoothing?
- 0567dd8b-b11b-4340-b7f2-1bfc038e57ea [text/abstractive] (right_doc_wrong_section): What is the purpose of the Virtual Lung Screening Trial (VLST)?
- 0722fef4-627d-40b8-aca6-c551a40f737e [text/extractive] (right_doc_wrong_section): What is the attractive force formula in the Fruchterman-Reingold force model?
- 09a2213c-325e-4658-b91c-b646307732d0 [text/extractive] (right_doc_wrong_section): Does this breast cancer recurrence risk assessment research comply with any international 
- 09b50336-ba65-42f3-81f5-cd91882d2073 [text/extractive] (right_doc_wrong_section): Is the MoC-System related to model training?
- 0d9b8d7b-8035-4bb6-941d-0055d46dd076 [text/abstractive] (right_doc_wrong_section): What problem does hyperbolic geometry help to address in vector quantization?
- 0df49653-f6e0-4426-ad85-20d615dd22ed [text/abstractive] (right_doc_wrong_section): How does understanding hyperparameters affect differential privacy outcomes in machine lea
- 0ee612bf-042c-49d3-a100-6649f14956ff [text/extractive] (right_doc_wrong_section): Does the topological signature of the FQH state remain robust against non-local cavity vac
- 0f02b37a-15dd-4422-bb1f-0d155429d81d [text-table/abstractive] (right_doc_wrong_section): What role does a truncation function play in managing stopping criteria for statistical te
- 14a31cfb-3b0f-495d-bc0a-5ef17b3d1260 [text/extractive] (wrong_doc): Is Michael J. Plank associated with the University of Canterbury?
- 16d9fb2d-3619-4b33-885d-3cea5eae478e [text/abstractive] (right_doc_wrong_section): What conditions determine when two different L²-spaces are considered equivalent or isomet
- 186ed08c-8491-4166-93b5-9d1cd1edb2cf [text-table/abstractive] (right_doc_wrong_section): How does the sample size and time step affect the bias and variance in estimating paramete
- 1b943b7c-4717-4201-83c0-af1f8209b50e [text/abstractive] (right_doc_wrong_section): What is done to ensure privacy in medical data used for speech summarization?
- 1cbc50c6-69e9-4f6f-ac02-b5b6213227ad [text-image/abstractive] (right_doc_wrong_section): How do AutoStep and fixed step methods compare in terms of jump distance versus initial st
- 1d585069-a446-47fa-a74d-0387316ea330 [text-table/abstractive] (right_doc_wrong_section): In what areas do syllabic embeddings show potential for improvement based on current resea

## Examples: doc matched but section missed
- 00d954d0-d8b6-40ab-9506-3d5e99ac929f: gold sec 0 in doc 2412.13914v3 -> top returned sections [('2409.14733v2', 3), ('2405.04989v2', 0), ('2410.10364v2', 1), ('2410.03667v5', 4), ('2403.01012v4', 2)]
- 015f84f5-d694-4fad-bfa5-d2f3687bcd52: gold sec 5 in doc 2412.04468v2 -> top returned sections [('2412.04468v2', 19), ('2412.04468v2', 0), ('2412.04468v2', 16), ('2412.04468v2', 9), ('2404.12556v2', 0)]
- 024b9722-075d-4f35-8769-0e1ad6d2747d: gold sec 3 in doc 2410.22824v2 -> top returned sections [('2410.22292v2', 17), ('2411.02253v3', 2), ('2406.12070v3', 8), ('2405.16924v2', 27), ('2410.22824v2', 12)]
- 02ab673a-fbd0-420a-9a18-9e3a24de8b88: gold sec 9 in doc 2412.02582v2 -> top returned sections [('2412.02582v2', 1), ('2412.02582v2', 10), ('2412.02582v2', 16), ('2412.02582v2', 8), ('2412.02582v2', 0)]
- 02b7db12-057d-4e26-bf4c-8000888465da: gold sec 13 in doc 2411.13673v2 -> top returned sections [('2411.13673v2', 0), ('2411.07469v2', 4), ('2406.09983v2', 1), ('2412.00566v2', 8), ('2411.13673v2', 3)]
- 02e11dcd-d7d5-44a7-9116-6db96345ca6a: gold sec 20 in doc 2411.07984v2 -> top returned sections [('2404.18869v2', 6), ('2404.18869v2', 20), ('2404.18869v2', 8), ('2412.21038v2', 24), ('2411.07984v2', 2)]
- 0567dd8b-b11b-4340-b7f2-1bfc038e57ea: gold sec 2 in doc 2404.11221v4 -> top returned sections [('2404.11221v4', 0), ('2404.11221v4', 1), ('2404.11221v4', 10), ('2404.11221v4', 17), ('2404.11221v4', 11)]
- 0722fef4-627d-40b8-aca6-c551a40f737e: gold sec 30 in doc 2412.20317v3 -> top returned sections [('2412.20317v3', 2), ('2412.20317v3', 27), ('2412.09393v2', 11), ('2412.20317v3', 0), ('2408.16004v3', 13)]
- 09a2213c-325e-4658-b91c-b646307732d0: gold sec 13 in doc 2406.06650v2 -> top returned sections [('2406.06650v2', 1), ('2406.06650v2', 11), ('2406.06650v2', 0), ('2406.06650v2', 20), ('2406.06650v2', 2)]
- 09b50336-ba65-42f3-81f5-cd91882d2073: gold sec 2 in doc 2408.04307v3 -> top returned sections [('2408.04307v3', 0), ('2408.04307v3', 18), ('2408.04307v3', 3), ('2408.04307v3', 21), ('2408.04307v3', 5)]
- 0d9b8d7b-8035-4bb6-941d-0055d46dd076: gold sec 25 in doc 2403.13015v2 -> top returned sections [('2403.13015v2', 1), ('2403.13015v2', 10), ('2403.13015v2', 3), ('2403.13015v2', 0), ('2403.13015v2', 9)]
- 0df49653-f6e0-4426-ad85-20d615dd22ed: gold sec 0 in doc 2405.20769v2 -> top returned sections [('2405.20769v2', 9), ('2405.20769v2', 1), ('2408.16142v4', 15), ('2405.20769v2', 6), ('2405.20769v2', 11)]
- 0ee612bf-042c-49d3-a100-6649f14956ff: gold sec 27 in doc 2405.12292v3 -> top returned sections [('2405.12292v3', 20), ('2405.12292v3', 24), ('2405.12292v3', 10), ('2405.12292v3', 0), ('2405.12292v3', 13)]
- 0f02b37a-15dd-4422-bb1f-0d155429d81d: gold sec 14 in doc 2410.16076v3 -> top returned sections [('2402.02272v2', 4), ('2409.14197v1', 10), ('2410.16076v3', 3), ('2405.18521v2', 3), ('2408.07372v2', 12)]
- 16d9fb2d-3619-4b33-885d-3cea5eae478e: gold sec 0 in doc 2412.13914v3 -> top returned sections [('2412.13042v2', 21), ('2412.13914v3', 1), ('2412.13914v3', 5), ('2409.18681v6', 5), ('2410.11034v2', 5)]
- 186ed08c-8491-4166-93b5-9d1cd1edb2cf: gold sec 6 in doc 2412.06343v3 -> top returned sections [('2412.06343v3', 5), ('2409.05529v2', 28), ('2410.18929v2', 9), ('2409.05529v2', 9), ('2404.19707v4', 10)]
- 1b943b7c-4717-4201-83c0-af1f8209b50e: gold sec 37 in doc 2406.15888v2 -> top returned sections [('2406.15888v2', 1), ('2406.15888v2', 0), ('2407.02994v3', 15), ('2406.15888v2', 22), ('2404.05659v3', 19)]
- 1cbc50c6-69e9-4f6f-ac02-b5b6213227ad: gold sec 25 in doc 2410.18929v2 -> top returned sections [('2410.18929v2', 14), ('2410.18929v2', 9), ('2410.18929v2', 16), ('2410.18929v2', 24), ('2410.18929v2', 10)]
- 1d585069-a446-47fa-a74d-0387316ea330: gold sec 30 in doc 2410.07168v2 -> top returned sections [('2410.07168v2', 33), ('2409.15374v2', 13), ('2410.06188v2', 14), ('2410.07168v2', 1), ('2410.07168v2', 11)]
- 1f3418c5-cc0e-4ad6-84ad-414b40329a8c: gold sec 14 in doc 2408.16142v4 -> top returned sections [('2408.16142v4', 2), ('2408.16142v4', 15), ('2408.16142v4', 30), ('2408.16142v4', 0), ('2408.16142v4', 34)]
