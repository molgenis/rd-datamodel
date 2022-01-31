# Unified Molgenis Data Model

Welcome! The Unified Molgenis Data Model &mdash;or UMDM&mdash; is a *plug and play* [Molgenis EMX](https://molgenis.gitbook.io/molgenis/data-management/guide-emx) model for collating metadata on patients and samples, analyses that were performed on the samples, and files that were generated. The model comprises several modules built on the [FAIR data principles](https://www.go-fair.org/fair-principles/) and the [FAIR Genomes Semantic Model](https://github.com/fairgenomes/fairgenomes-semantic-model). The module system enables the model to be adapted for research or care contexts.

Download the [latest version of the model](https://github.com/molgenis/rd-datamodel/blob/main/emx/dist/umdm.xlsx) or [view the model schema](https://github.com/molgenis/rd-datamodel/blob/main/emx/schemas/umdm_schema.md) to see what's in the model.

## Features

Here is what is included.

- :package: **Unified Model**: a *plug and play* FAIR data model for Molgenis databases on rare diseases. The model contains modules for patients, studies, consent, clinical events, biomaterials collected, preparation of samples, sample sequencing, and metadata from generated files.
- :books: **Reference Datasets**: an extensive library of reference datasets standardized to ontologies, international standards, and field specific standards.
- :busts_in_silhouette: **User Module**: table structure and script tracking users, registrations, and authorization levels. Ideal for auditing and database management!
- :wrench: **Jobs**: table structure for logging custom jobs and results. This is an extension of the existing jobs entity, but geared towards database management.

For more information on Molgenis, visit [molgenis.org](https://www.molgenis.org/).

## Getting Started

This repository includes scripts for building the model and collating lookup datasets, but you only need the model and a few other things to get started with building your own database. See the steps below.

1. **Install Molgenis**: you will need a server running the latest version of Molgenis. See the [Molgenis Documentation](https://molgenis.gitbook.io/molgenis/) for more information about setting up Molgenis. Alternatively, you can use the [latest Molgenis Docker container](https://github.com/molgenis/docker) to create an instance on your local machine.
2. **Install the Molgenis Commander**: Install the latest version of [Molgenis commander](https://github.com/molgenis/molgenis-tools-commander)
3. **Run the setup script**: Run the [UMDM Setup script](https://github.com/molgenis/rd-datamodel/blob/main/emx/dist/umdm_setup.sh). This will import the model and all datasets into your Molgenis instance.
