---
title: "Toward a Shared, Decoupled Evidence Layer for AI-Era Science"
short_title: Shared, decoupled evidence layer
subtitle: A consensus draft for data producers, analysts, archivists, and publishers
abstract: >
  AI can generate scientific narratives and syntheses at growing scale, but its
  conclusions are only as reliable as the evidence made visible to it. Today's
  article often bundles observations, methods, interpretation, and credit into a
  single publication. This limits reuse, can leave null or inconclusive work
  outside the record, and leaves AI systems to reconstruct evidence and provenance
  from prose. We argue for decoupling evidence sharing from narrative publication.
  A shared evidence layer would serve both goals: preserving completed work as
  inspectable, citable evidence and enabling people and AI to discover, connect,
  and synthesize it into multiple analyses, reviews, and applications. Narrative
  remains essential for interpretation, and credit and
  accountability should follow every layer. This consensus draft invites data
  producers, analysts, archivists, and publishers to shape that shared foundation while
  preserving diverse repositories, tools, and implementations.
---

```{authorship-explorer}
:authors: ./authors.yml
:height: 760px
```

## Rethinking the publication unit

Scientific publishing has historically compressed discovery into a long-form article, a sensible format when prose was the main carrier of context and credit. Digital publishing improved access but largely preserved that print-era unit {cite}`shotton2009`. Data, methods, figures, interpretation, and authorship still travel together, making it difficult to inspect evidence and synthesis as distinct but connected objects.

This coupling is not merely a packaging problem; it shapes which evidence becomes visible. When completed work enters the scholarly record mainly by supporting an article-sized narrative, sharing is tied to the demand for a coherent and often positive story. Positive results are more likely to appear {cite}`fanelli2012,dwan2008`, and selective reporting can make the published account differ from what was measured {cite}`chan2004`. Existing reforms address part of this problem. Registered Reports review questions and methods before results are known and may grant in-principle article acceptance, reducing selective publication, but they still culminate in a study-centered article {cite}`chambers2022`.

That ambiguity becomes more consequential as AI systems both synthesize and produce science. A model can summarize only what entered its corpus and cannot account for experiments never reported, so it inherits the availability bias of publication. Separating evidence sharing from narrative publication would not eliminate bias, but it could make null and inconclusive outcomes available for scrutiny. Meanwhile, LLM-based agents have designed and executed chemistry experiments, coordinated a computational workflow that produced nanobody candidates subsequently validated in the laboratory, and operated atomic-force microscopy across experimental tasks {cite}`boiko2023,swanson2025,mandal2025`. These systems remain narrow and brittle: evaluation of the microscopy agents found failures on basic tasks, sensitivity to prompting, and potentially unsafe instruction deviations {cite}`mandal2025`. When an agent selects inputs, changes parameters, invokes instruments, or interprets outputs, provenance becomes an operational requirement. It should consume versioned evidence and emit a traceable record of its actions, dependencies, and human approvals. A shared evidence layer would provide that interface, helping prevent faster experimentation from producing more results that remain difficult to audit, reproduce, or attribute.

Research Objects established linked resources and their context as first-class scholarly objects, while FAIR Digital Objects emphasize typed, persistently identified, machine-actionable packages {cite}`bechhofer2013,desmedt2020`. Many datasets and software releases are already independently citable. What is missing is a widely adopted publication convention for evidence: a citable, machine-readable record that connects existing research objects and describes their relationships, provenance, and contributors. A common profile would make these records interoperable across repositories. Each record would link authoritative versions rather than copy them, and it would not require a scientific claim. Claims and narratives would remain separate interpretive products that could cite one or many evidence records.

Semantic publishing, nanopublications, and the Open Research Knowledge Graph already make scholarly structure and assertions computable {cite}`shotton2009,kuhn2016,jaradeh2019`. The distinction here is that a primary record may stop at evidence and provenance rather than elevating one assertion. Interpretations can change while the observations beneath them remain stable enough to cite. {numref}`fig-publication-models` contrasts this layered model with the bundled article.

:::{figure} figures/publication-models.svg
:label: fig-publication-models
:align: center

Matching colors trace the bundled article's components into reusable evidence, analysis recipes, derived outputs, and object-level attribution.
:::

:::{dropdown} Figure source data

```{literalinclude} data/publication-models.json
:language: json
```
:::

## A layered publication model

Consider a neuroscience experiment whose recordings, code, and protocol are separately archived in DANDI, Zenodo, and protocols.io {cite}`dandiarchive,githubzenodo,protocolsio`. A generated figure may also identify the exact data, software, parameters, and rendering recipe used to produce it. DANDI itself is moving toward richer packaging: its Dandiset schema supports contributor roles, persistent protocol URLs, and typed relations to external resources {cite}`dandischema`. This is valuable, but the schema is designed for Dandisets and their assets, not as a repository-independent evidence unit spanning a dataset, software release, protocol, and derived figure. Today, the paper is still expected to bind these objects, which otherwise may not form a single citable record stating how they relate, which versions were used, and who contributed to each. The proposed evidence manifest would supply that record by linking authoritative identifiers and documenting their relationships and contributors, without requiring a narrative conclusion.

Decoupling evidence from prose should not decouple either from credit. Every evidence record and every derived object needs its own citable contribution record. ORCID can identify contributors, while CRediT or domain-specific roles describe what each person did {cite}`haak2012,brand2015`. Credit should also flow across layers without collapsing them. A review or decision tool should cite the evidence it uses, making reuse visible in scholarly evaluation {cite}`datacitation2014`. Those citations credit upstream contributors without making them authors of a downstream claim they did not write or endorse. Authors of derived products remain accountable for selection, scope, and interpretation, even when those products are regenerated as evidence changes. This distinction is central to incentives: evidence sharing will remain secondary if the narrative article is still the only prestigious object.

Making an output citable, however, does not ensure that its citations become visible or count toward a researcher's record. Google Scholar's public inclusion guidance is framed around papers, while Google provides a separate Dataset Search service for datasets {cite}`googlescholarinclusion,googledatasetsearch`. Dataset and protocol deposits can therefore carry persistent identifiers yet remain inconsistently represented in article-centered citation indexes, author profiles, and assessment workflows. Evidence records should appear as distinct contributions on academic CVs and in ORCID and institutional profiles, with their citations and documented reuse reported alongside those of articles. Repositories and publishers should expose the metadata and reference links needed for citation tracking, while funders, hiring panels, and promotion committees should evaluate the quality and impact of these outputs rather than treating them as supplements. This would extend existing calls to recognize datasets and software in research assessment {cite}`dora2012` and make evidence publication a credible scholarly outcome rather than invisible service work.

Timing creates a related barrier. Releasing evidence before an accompanying article may weaken the paper's perceived novelty and, as AI systems monitor repositories at scale, enable reuse before producers present their own interpretation. Early release may be the natural norm for dedicated data producers—observatories, shared facilities, consortia, and institutions whose mission is to serve broad research communities—because the release itself is their principal scholarly output. For study-led teams, synchronized release may be more practical, with evidence becoming public when the manuscript first appears, whether as a preprint or journal article. Both models require the same cultural shift: journals, funders, institutions, and evaluators must recognize timestamped evidence records as priority- and credit-bearing contributions. Completed work without an article would still need a recognized route after a time-limited embargo.

Independent evidence records could make completed null or inconclusive experiments queryable, helping synthesis distinguish *not studied* from *studied without support*. As {numref}`fig-evidence-visibility` illustrates, this could expose a more useful denominator and reduce repeated investment in unreported dead ends, although it would not remove methodological bias, selective sharing, or poor-quality evidence.

:::{figure} figures/evidence-visibility.svg
:label: fig-evidence-visibility
:align: center

An illustrative comparison of the same three completed studies. When visibility depends on article publication, null and inconclusive outcomes are less likely to enter the corpus available to AI. Independently citable evidence records can expose a more complete denominator and make synthesis traceable, although they cannot eliminate bias from missing or poor-quality evidence.
:::

:::{dropdown} Evidence visibility source data

```{literalinclude} data/evidence-visibility.json
:language: json
```
:::

## A proposed evidence record

Under this proposal, an evidence record would be a citable, machine-readable publication unit that connects the authoritative objects produced by a completed piece of research. It would identify rather than copy datasets, software, protocols, and figures, and state how their specific versions relate. It would record evidence and provenance without requiring a scientific claim; registrations, interpretations, and later claims could remain linked but distinct.

Unlike a Registered Report, an evidence record would require neither prospective review nor an eventual article and could also document exploratory work.

A future reader, human or machine, should not have to reconstruct those relationships from prose and pictures. One persistent identifier should resolve to both a readable landing page and a machine-actionable manifest. MyST could provide the presentation and visualization layer for the landing page, rendering linked figures, source data, citations, and interactive components as a web publication or static export; the manifest would remain independent of MyST or any other interface {cite}`mystmd`. Rather than a loose list of URLs, the manifest should contain typed persistent references that distinguish an input dataset from a protocol, a software dependency, or a later interpretation. At minimum, it should describe:

- **context:** study design, measured variables, uncertainty, and quality-control status;
- **object links:** typed, versioned identifiers for data, software, protocols, figures, and environments;
- **evidence links:** relations to other evidence, questions, registrations, and interpretations, such as *derived from*, *replicates*, or *extends*; and
- **credit and state:** contributors identified by ORCID and contribution roles, together with provenance, version, license, access, checksum, correction, and retraction status.

Conformance of this record should not be confused with validation of its scientific conclusions. A conformant manifest can establish that objects, versions, contributors, and declared relationships are machine-readable and traceable; it cannot certify methodological quality, absence of bias, reproducibility, or the validity of a downstream claim. Evidence records should nevertheless expose auditable quality signals—such as prespecified checks, exclusions, calibration, missingness, and review status—so that people and machines can assess fitness for purpose without reducing scientific trust to a single score.

These links would make evidence traversable as a knowledge graph without imposing one canonical interpretation. {numref}`fig-evidence-record-anatomy` shows this minimum anatomy.

:::{figure} figures/evidence-record-anatomy.svg
:label: fig-evidence-record-anatomy
:align: center

Proposed minimum evidence record. Existing data, software, protocols, and figures remain in their repositories. Typed links connect each record both to those objects and to related evidence, forming a knowledge graph. The record also carries context, contributor information, and lifecycle state, while one identifier resolves to human-readable and machine-readable views.
:::

:::{dropdown} Illustrative evidence record source data

```{literalinclude} data/evidence-record-anatomy.json
:language: json
```
:::

## Publishing and adopting evidence records

For an evidence record to function as a publication unit, archives, repositories, and publishers would need to register or deposit it, preserve its versions and attribution, and make it independently citable. They would also need to keep records and linked objects computable, comparable, and version-aware, extending FAIR principles from findable objects toward computable knowledge {cite}`wilkinson2016`. Independent citability need not imply unrestricted access: sensitive data can remain controlled while metadata and authorized interfaces remain interoperable.

Much of the technical infrastructure already exists. Data and software citation treat datasets and code as first-class outputs {cite}`fenner2019,smith2016`. DataCite supports typed relations among persistent identifiers {cite}`dataciteschema`, while RO-Crate packages research artifacts and metadata {cite}`soilandreyes2022`. The proposal therefore does not seek to replace RO-Crate, FAIR Digital Objects, DataCite, or disciplinary repository schemas. A practical implementation could instead compose them through a community-governed profile: authoritative repositories would continue to describe individual objects, an RO-Crate manifest could connect them, and persistent identifiers and DataCite relations could support discovery and citation.

Without fixing the architecture prematurely, a pilot-ready profile could test a small core of typed relations and explicit version and lifecycle behaviour. Corrections, withdrawals, and retractions should create linked states that preserve prior releases, allowing downstream systems to identify evidence that has been superseded rather than silently erasing its history.

The illustrative anatomy in {numref}`fig-evidence-record-anatomy` therefore expresses starting requirements, not a schema offered for adoption. This perspective does not seek to own the profile or establish a standards body. The next step is for standards communities, repositories, publishers, researchers, archivists, and infrastructure providers to refine and govern a minimum profile, then test it across disciplines, data types, and repository conventions.

## A larger derived space

Decoupling changes the relationship between evidence and its uses from one privileged article to the many-to-many space shown in {numref}`fig-publication-models`. One evidence record can support many analyses and narratives, while one derivative can combine evidence from many records. Secondary reuse would no longer be an exception, and no interpretation would become canonical merely because it accompanied the original release.

Observatory communities already approximate this pattern. Sloan Digital Sky Survey releases support questions not fixed during acquisition {cite}`york2000`, and opening Landsat enabled science and monitoring beyond any single mission narrative {cite}`wulder2012`. These precedents show that shared observations can accumulate value through repeated interpretation while producers remain identifiable and citable.

## Recovering past evidence

This proposal is necessarily both forward-looking and retrospective. New research could produce evidence records directly as part of its workflow. Past literature creates a different recovery problem: reviews and AI-assisted syntheses already reconstruct local evidence layers from papers by identifying studies, extracting designs and results, reconciling identifiers, and assembling evidence tables {cite}`thomas2017,marshall2019`. This work should not have to be repeated for every synthesis.

For older studies, quantitative evidence may survive only as a plot, while original data and computational context are dispersed across supplements or absent. Automated extraction could locate and recover fragments, but reconstructed records would require human validation and should state what came from original files, what was recovered from figures or prose, and what remains unknown. Making validated reconstructions citable and attributable would recognize recovery as scholarly infrastructure, let later syntheses reuse it, and gradually connect the paper-centered past to evidence records produced directly by new workflows.

## A computational research encyclopedia

This recovery points to an opportunity: a computational research encyclopedia organized around topics and questions rather than papers. As a maintained synthesis layer, not a replacement for evidence or interpretation, each page would state what is known, where findings converge or conflict, and what remains uncertain. It would provide a route from a field-level question to the evidence, analyses, and interpretations behind each statement, without becoming the source or final authority.

Computational reviews could supply and update these pages. Here, a computational review means an AI-generated synthesis of evidence on a defined topic, produced through an inspectable workflow that can be repeated across many topics {cite}`lecoq2026computationalreview`. Building on living reviews and human-machine synthesis {cite}`elliott2014,thomas2017,marshall2019`, such reviews would search for relevant evidence, organize findings and uncertainty, and draft changes as records are added or revised. Each review would expose its search space and inclusion criteria, cite persistent identifiers, and preserve methods, versions, and contributors. Human editors would remain responsible for scope, interpretation, and approval; automation would keep the encyclopedia current without becoming its authority.

Topic pages would spare readers from repeatedly reconciling a scattered literature and give researchers, educators, and decision-makers a current reference. Unlike static reviews, they could change as work is added, corrected, or retracted; unlike chatbot summaries, their scope and sources would remain inspectable. Null findings and disagreements could remain visible alongside convergent results rather than be compressed into one account.

A shared evidence layer would enable, not gatekeep, this encyclopedia. Local reconstructions could support it, but a common layer would make them reusable and give projects, review teams, and agents an inspectable starting point. Typed, versioned records could reduce repeated extraction, propagate corrections, preserve attribution, and connect multiple interpretations to the same observations. Open to competing syntheses and interfaces, it would provide a more level basis for sharing knowledge without imposing one canonical account.

## From proposal to pilot

The immediate goal should not be a universal standard imposed in advance. Standards communities, repositories, publishers, researchers, and archivists should jointly define a minimum, community-governed profile; publish reference manifests and a validator; and pilot the profile across several disciplines, data types, and access regimes. To limit authoring burden, implementations should harvest metadata from authoritative repositories, persistent identifiers, contributor registries, and computational workflows wherever possible, leaving researchers to confirm the context and relationship assertions that cannot be inferred reliably. AI could assist with extraction and mapping, but it can also make workflows more complex and propagate plausible metadata errors; its suggestions should therefore retain provenance and remain subject to human confirmation. Pilots should measure authoring time, completeness, correction handling, and burden across disciplines and resource settings, alongside discovery, citation and credit, reuse, and machine-assisted synthesis.

Success would mean that a completed contribution can enter the scholarly record even when no article follows; that its provenance, versions, access conditions, and contributors remain inspectable; and that its use is visible in academic assessment. Narrative articles would remain essential for argument and interpretation, but no longer the only route through which evidence becomes discoverable, citable, and consequential.
