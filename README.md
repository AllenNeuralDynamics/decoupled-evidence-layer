# Toward a Shared, Decoupled Evidence Layer for AI-Era Science

This repository is a MyST consensus perspective calling for data producers, data analysts, archivists, standards communities, repositories, and publishers to adopt an interoperable evidence layer. It argues for persistently identified evidence manifests that can support many independently credited derivatives without requiring one privileged interpretation. Computational reviews are one example within that larger derived space.

## Perspective and adoption effort

This repository is intended to become a versioned, co-authored perspective that motivates convergence and documents candidate requirements, mappings, examples, and interoperability tests. It is not intended to own the resulting standard or substitute for a community standards process. A normative profile could be developed through RO-Crate governance or another appropriate collaboration among standards communities, repositories, publishers, researchers, archivists, and infrastructure providers.

The target is not one repository, graph implementation, or AI system, but broad adoption of a small interoperability contract: a minimum evidence profile, typed persistent-identifier relations, representative cross-domain records, and a public conformance suite. Domain repositories, graph stores, interfaces, agents, and derived products can remain independently designed.

A useful first milestone is for two independent systems to exchange the same evidence record, validate it, resolve its dependencies, and preserve contributor attribution without bespoke translation. Contributions can advance that milestone by:

- mapping an existing repository or metadata schema to the proposed profile;
- contributing a representative evidence record from another discipline;
- reviewing relation, versioning, attribution, license, or access semantics; or
- implementing a validator, producer, consumer, or interoperability test.

Substantive contributions to requirements, mappings, fixtures, semantics, schema design, implementations, tests, or the resolution of design disagreements can support co-authorship. Review, implementation, adoption, and endorsement should be recorded separately when they do not involve responsibility for the full consensus text.

A candidate manuscript release is ready to finalize when its authors agree on scope and material interoperability objections have been resolved or documented. Examples, mappings, and tests developed here should be released as proposals that a standards community can reuse, revise, or reject. Cross-system exchange can demonstrate feasibility, but durable interoperability will require independent governance and adoption by publishing infrastructure. Convergence on interchange behavior matters more than convergence on terminology.

## Preview locally

```bash
npm install
npm install -g mystmd
myst start
```

## Build

```bash
myst build --html
```

The GitHub Pages workflow in `.github/workflows/deploy.yml` builds `_build/html` and deploys it with GitHub Actions. Before publishing, replace placeholder contributor records in `authors.yml` as needed.

## Authorship Explorer

The page vendors the upstream AuthorshipExtractor MyST plugin, widget, and CSS files locally so GitHub Pages can build the explorer without a separate package install. The article uses this directive:

````md
```{authorship-explorer}
:authors: ./authors.yml
:height: 760px
```
````

Contributor records live in `authors.yml` and include CRediT roles, contribution levels, section contributions, figure contributions, timeline entries, and contribution statements.
