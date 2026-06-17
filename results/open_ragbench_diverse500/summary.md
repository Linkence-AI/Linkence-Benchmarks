# OpenRAGBench diverse_500 Result

## Dataset
- Dataset: vectara/open_ragbench
- Subset: diverse_500
- Queries evaluated: 500
- Indexed positive docs: 286
- Indexed hard-negative docs: 250
- Indexed sections: 10432
- top_k: 10
- Embedding model: text-embedding-3-small
- Reranker: None

## Headline
- **Strict Section Direct Retrieval Accuracy@10: 96.6%**

## Supporting
- Relaxed Document Accuracy@10: 99.8%
- MRR@10: 0.7952
- Zero-source rate: 0.0%
- p50 latency: 387.1 ms
- p95 latency: 545.5 ms

## Strict@K / Relaxed@K (overall)
- @1: strict_section=68.2%, relaxed_doc=96.0%
- @3: strict_section=90.4%, relaxed_doc=99.6%
- @5: strict_section=92.8%, relaxed_doc=99.8%
- @10: strict_section=96.6%, relaxed_doc=99.8%

## Breakdown by source (strict@10)
- text: strict@10=98.4%, relaxed@10=99.7% (n=315)
- text-image: strict@10=92.0%, relaxed@10=100.0% (n=125)
- text-table: strict@10=95.8%, relaxed@10=100.0% (n=24)
- text-table-image: strict@10=97.2%, relaxed@10=100.0% (n=36)

## Breakdown by type (strict@10)
- abstractive: strict@10=96.3% (n=294)
- extractive: strict@10=97.1% (n=206)

## Supported vs multimodal-degraded
- Supported-only (text, text-table): strict@10=98.2% (n=339)
- Multimodal-degraded (text-image, text-table-image): strict@10=93.2% (n=161)
- NOTE: images are indexed as base64 with no captions/OCR; our text-embedding stack cannot read image content, so multimodal queries are reported separately and excluded from the supported-only headline.

## Conclusion
- Score kind: text-only / supported (headline = all selected queries)
- Failed queries (top 17): see failures report
- Next fix: review top failed queries for systematic retrieval gaps.

## Top 20 failed queries
- 0722fef4-627d-40b8-aca6-c551a40f737e [text/extractive] (right_doc_wrong_section): What is the attractive force formula in the Fruchterman-Reingold force model?
- 0cc52d57-c698-481f-8113-2eebdc3799e1 [text-image/extractive] (right_doc_wrong_section): What is a social welfare function in economics?
- 1d585069-a446-47fa-a74d-0387316ea330 [text-table/abstractive] (right_doc_wrong_section): In what areas do syllabic embeddings show potential for improvement based on current resea
- 2bac52cd-23d5-4128-a321-c325f49e59d9 [text/extractive] (wrong_doc): What is a pitchfork bifurcation in dynamical systems?
- 2cc9bf85-7258-45b7-b8a8-e1888c793c1f [text/abstractive] (right_doc_wrong_section): What type of processes do individual idiosyncratic noises form in classical mean field gam
- 3de6cbbd-b28f-49f6-9e13-45df9264bb07 [text-table-image/abstractive] (right_doc_wrong_section): What were the long-term socio-economic effects on individuals who experienced centralized 
- 4126e457-bb00-4de0-8202-3d5e2de4713f [text-image/abstractive] (right_doc_wrong_section): How does an even number of switch errors influence the output in diploid genome assembly u
- 52694833-7001-4896-a030-e767eec3467b [text-image/abstractive] (right_doc_wrong_section): What is the role of symmetric matrices in algebraic K-theory with involution?
- 5dccd210-faae-48b0-8052-b959455ccaf1 [text/abstractive] (right_doc_wrong_section): How does the performance of noise-based local learning compare with traditional algorithms
- 6e2c7363-89ae-4430-95fb-da8a4e9c04d7 [text-image/abstractive] (right_doc_wrong_section): What role does vapor pressure data play in understanding boiling points of materials like 
- 7b3343a0-8ec0-4d68-a3a6-81de181ed836 [text-image/abstractive] (right_doc_wrong_section): Why might TM-score be preferred over RMSD for evaluating RNA structures?
- 96356cf3-afe2-4230-b1f3-d7caa31c1fde [text-image/extractive] (right_doc_wrong_section): What is the best performing method for audio inpainting at a gap length of 10 ms?
- a6c723b4-b7c7-4269-b1bb-1e245f433ff5 [text-image/extractive] (right_doc_wrong_section): What does "J-AM-NoSpec-epsilon" refer to in terms of program counter (pc) conditions?
- b76a0e45-7cbb-4608-b8ee-2c771ea27ef0 [text-image/abstractive] (right_doc_wrong_section): What conditions make ultrametric balls equivalent to other geometric shapes like boxes or 
- b9f96e77-09e0-4795-ab19-9353bbac0f7e [text-image/abstractive] (right_doc_wrong_section): How do different infrared wavelengths perform in cyclone prediction models?
- f9ce4d40-606e-41e3-9f74-938ad0810117 [text/extractive] (right_doc_wrong_section): Are matrix techniques used in the improvements of Heron and Heinz inequalities?
- faa2bf74-b122-487f-972c-3f3e37b20e38 [text-image/abstractive] (right_doc_wrong_section): How does chemical homeostasis influence branching patterns in engineered cell clusters?

## Examples: doc matched but section missed
- 0722fef4-627d-40b8-aca6-c551a40f737e: gold sec 30 in doc 2412.20317v3 -> top returned sections [('2412.20317v3', 2), ('2412.20317v3', 27), ('2412.20317v3', 0), ('2412.09393v2', 11), ('2411.12375v3', 18)]
- 0cc52d57-c698-481f-8113-2eebdc3799e1: gold sec 3 in doc 2408.04814v3 -> top returned sections [('2410.09555v2', 9), ('2408.04814v3', 0), ('2408.04814v3', 9), ('2408.04814v3', 2), ('2406.14174v3', 2)]
- 1d585069-a446-47fa-a74d-0387316ea330: gold sec 30 in doc 2410.07168v2 -> top returned sections [('2410.07168v2', 33), ('2410.06188v2', 14), ('2411.04694v1', 7), ('2410.07168v2', 1), ('2410.07168v2', 11)]
- 2cc9bf85-7258-45b7-b8a8-e1888c793c1f: gold sec 4 in doc 2403.01012v4 -> top returned sections [('2403.01012v4', 0), ('2403.01012v4', 5), ('2403.01012v4', 1), ('2403.01012v4', 15), ('2408.11773v1', 7)]
- 3de6cbbd-b28f-49f6-9e13-45df9264bb07: gold sec 23 in doc 2402.04429v3 -> top returned sections [('2402.04429v3', 1), ('2402.04429v3', 3), ('2402.04429v3', 11), ('2402.04429v3', 9), ('2402.04429v3', 13)]
- 4126e457-bb00-4de0-8202-3d5e2de4713f: gold sec 7 in doc 2405.05734v3 -> top returned sections [('2405.05734v3', 1), ('2405.05734v3', 10), ('2405.05734v3', 11), ('2405.05734v3', 4), ('2405.05734v3', 9)]
- 52694833-7001-4896-a030-e767eec3467b: gold sec 11 in doc 2405.02054v2 -> top returned sections [('2405.02054v2', 12), ('2407.04378v2', 9), ('2405.02054v2', 1), ('2402.12350v3', 1), ('2409.09862v3', 24)]
- 5dccd210-faae-48b0-8052-b959455ccaf1: gold sec 1 in doc 2412.12783v2 -> top returned sections [('2412.12783v2', 2), ('2412.15021v4', 8), ('2412.12783v2', 13), ('2412.15021v4', 1), ('2406.18306v11', 10)]
- 6e2c7363-89ae-4430-95fb-da8a4e9c04d7: gold sec 5 in doc 2409.02293v3 -> top returned sections [('2412.02269v2', 4), ('2412.07042v1', 9), ('2409.02293v3', 18), ('2410.08642v2', 2), ('2409.04439v3', 7)]
- 7b3343a0-8ec0-4d68-a3a6-81de181ed836: gold sec 17 in doc 2406.13839v2 -> top returned sections [('2406.13839v2', 8), ('2406.13839v2', 5), ('2406.13839v3', 7), ('2406.13839v2', 7), ('2406.13839v2', 22)]
- 96356cf3-afe2-4230-b1f3-d7caa31c1fde: gold sec 8 in doc 2403.04433v3 -> top returned sections [('2403.04433v3', 1), ('2403.04433v3', 4), ('2403.04433v3', 7), ('2403.04433v3', 9), ('2403.04433v3', 3)]
- a6c723b4-b7c7-4269-b1bb-1e245f433ff5: gold sec 46 in doc 2405.10089v2 -> top returned sections [('2410.15824v2', 29), ('2405.10089v2', 50), ('2405.10089v2', 127), ('2403.19186v2', 18), ('2405.10089v2', 4)]
- b76a0e45-7cbb-4608-b8ee-2c771ea27ef0: gold sec 8 in doc 2401.07317v2 -> top returned sections [('2412.15576v4', 12), ('2401.07317v2', 7), ('2406.04259v2', 2), ('2403.08977v2', 2), ('2412.00566v2', 6)]
- b9f96e77-09e0-4795-ab19-9353bbac0f7e: gold sec 42 in doc 2409.16507v2 -> top returned sections [('2409.16507v2', 10), ('2401.03345v2', 18), ('2409.16507v2', 39), ('2411.15519v1', 10), ('2409.16507v2', 24)]
- f9ce4d40-606e-41e3-9f74-938ad0810117: gold sec 0 in doc 2409.16171v2 -> top returned sections [('2409.16171v2', 8), ('2409.16171v2', 2), ('2409.16171v2', 7), ('2409.16171v2', 1), ('2411.18627v2', 1)]
- faa2bf74-b122-487f-972c-3f3e37b20e38: gold sec 42 in doc 2407.06295v3 -> top returned sections [('2407.06295v3', 36), ('2407.06295v3', 4), ('2407.06295v3', 34), ('2407.06295v3', 3), ('2407.06295v3', 0)]
