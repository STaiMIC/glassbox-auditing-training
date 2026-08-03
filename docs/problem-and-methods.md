GlassBox AI Triage — Nextflow Summit Abstract: Draft Sections
<br>
Problem
<br>
The integration of artificial intelligence (AI) into genomic variant triage offers the potential to accelerate post-processing after sequencing pipelines such as nf-core/sarek (1), and AI-assisted variant prioritisation is increasingly being explored as a means of reducing the interpretive burden on analysts (2). However, AI systems—particularly those that employ probabilistic inference or large language model (LLM) components—are inherently stochastic: given identical inputs, they can produce different outputs across independent runs (3). This non-determinism is compounded by the near-universal absence of structured mechanisms for capturing the exact model version, prompt specification, container image digest, pipeline commit, and input data hash associated with any given triage decision. The result is a provenance gap: AI-generated prioritisation outputs cannot be reliably traced back to the conditions that produced them, making it impossible to audit a decision, reproduce a result, or attribute inconsistencies to their true source. Reproducibility challenges of this kind are recognised as a fundamental obstacle to the responsible deployment of AI in biomedical settings (4). For small research groups and teams operating with limited computational infrastructure, including those in low- and middle-income research settings, the absence of affordable, auditable AI tooling represents a meaningful barrier to the responsible adoption of AI-assisted variant analysis. A lightweight, Nextflow-native pattern that enforces output reproducibility and captures full execution provenance at negligible additional cost would address this gap directly.
<br>
Methods
<br>
Publicly available and synthetic annotated variant datasets are processed through an unmodified nf-core/sarek run (1), executed within the Nextflow workflow management framework (5,6) on GitHub Codespaces using CPU-only Docker containers. VCF outputs from the sarek run are passed directly to a bespoke post-processing Nextflow subworkflow implementing a lightweight, rule-based AI triage step. Triage is applied under two experimental conditions. In the minimally controlled (standard) condition, triage is executed without systematic provenance capture or output validation. In the glass-box condition, triage output is constrained to a fixed JSON schema enforced by a dedicated validation process (JSON_VALIDATION), and a structured audit bundle is generated for every run (AUDIT_BUNDLE), recording the AI model version, prompt version, container image digest, sarek commit hash, input file hash, and execution timestamp. Any output that fails schema validation is quarantined rather than passed downstream. Each condition is executed in ten independent repeat runs from identical inputs, consistent with recommendations for evaluating the run-to-run variability of non-deterministic AI systems (3). A baseline sarek run without any downstream triage quantifies the computational overhead attributable to the subworkflow. Primary outcome measures include: exact and field-level output concordance across replicate runs; schema-pass and quarantine rates; provenance completeness (i.e. the proportion of decisions for which a full audit trail can be reconstructed); and per-run wall-clock time and estimated cloud cost. These are assessed using evaluation approaches appropriate for machine learning models applied in genetics and genomics (7). A future cloud deployment path remains a possible extension but is outside the scope of the current comparison.
<br>
References

<br>
1. Hanssen F, Garcia MU, Folkersen L, et al. Scalable and efficient DNA sequencing analysis on different compute infrastructures aiding variant discovery. NAR Genomics and Bioinformatics. 2024;6:lqae031. doi:10.1093/nargab/lqae031.
<br>
2. Wilk EJ, Taluri S, Howton TC, et al. AI in variant analysis: fast track to genetic diagnoses. Human Genetics. 2026;145:54. doi:10.1007/s00439-026-02847-0.
<br>
3. Blackwell RE, Barry J, Cohn AG. Towards reproducible LLM evaluation: quantifying uncertainty in LLM benchmark scores. arXiv. 2024. doi:10.48550/arXiv.2410.03492.
<br>
4. Han H. Challenges of reproducible AI in biomedical data science. BMC Medical Genomics. 2025;18(Suppl 1):8. doi:10.1186/s12920-024-02072-6.
<br>
5. Di Tommaso P, Chatzou M, Floden EW, Prieto Barja P, Palumbo E, Notredame C. Nextflow enables reproducible computational workflows. Nature Biotechnology. 2017;35:316-319. doi:10.1038/nbt.3820.
<br>
6. Ewels PA, Peltzer A, Fillinger S, Patel H, Alneberg J, Wilm A, Garcia MU, Di Tommaso P, Nahnsen S. The nf-core framework for community-curated bioinformatics pipelines. Nature Biotechnology. 2020;38(3):276-278. doi:10.1038/s41587-020-0439-x.
<br>
7. Miller C, Portlock T, Nyaga DM, O'Sullivan JM. A review of model evaluation metrics for machine learning in genetics and genomics. Frontiers in Bioinformatics. 2024;4:1457619. doi:10.3389/fbinf.2024.1457619.
