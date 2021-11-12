# Unified Rare Diseases Data Model

Welcome! The Unified Rare Disease Model &mdash;or URDM&mdash; is a *plug and play* [Molgenis EMX](https://molgenis.gitbook.io/molgenis/data-management/guide-emx) model for collating metadata on patients and samples, analyses that were performed on the samples, and files that were generated. The model comprises several modules built on the [FAIR data principles](https://www.go-fair.org/fair-principles/) and the [FAIR Genomes Semantic Model](https://github.com/fairgenomes/fairgenomes-semantic-model). The module system enables the model to be adapted for research or care contexts.

This repository contains the necessary files and scripts for getting started with the Unified Rare Disease Model. To see what's in the model, checkout the [Unified Rare Disease Data Model Schema](https://github.com/molgenis/rd-datamodel/blob/main/emx/schemas/urdm_schema.md).

Here is a list of features.

- :package: **Rare Disease Model**: a *plug and play* FAIR data model for Molgenis databases on rare diseases. The model contains modules for patients, studies, consent, clinical events, biomaterials collected, preparation of samples, sample sequencing, and metadata from generated files.
- :books: **Reference Datasets**: an extensive library of reference datasets standardized to ontologies, international standards, and field specific standards.
- :busts_in_silhouette: **User Module**: table structure and script tracking users, registrations, and authorization levels. Ideal for auditing and database management!
- :wrench: **Jobs**: table structure for logging custom jobs and results. This is an extension of the existing jobs entity, but geared towards database management.

For more information on Molgenis, visit [molgenis.org](https://www.molgenis.org/).

## Getting Started

To get started, you will need **a Molgenis instance** running on the latest version. See the [Molgenis Documentation](https://molgenis.gitbook.io/molgenis/) for more information about setting up Molgenis.

*TBD*
