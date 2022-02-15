# Unified Molgenis Data Model

Welcome! The Unified Molgenis Data Model &mdash;or UMDM&mdash; is a *plug and play* [Molgenis EMX](https://molgenis.gitbook.io/molgenis/data-management/guide-emx) model for collating metadata on patients and samples, analyses that were performed on the samples, and files that were generated. The model comprises several modules built on the [FAIR data principles](https://www.go-fair.org/fair-principles/) and the [FAIR Genomes Semantic Model](https://github.com/fairgenomes/fairgenomes-semantic-model). The module system enables the model to be adapted for research or care contexts.

Download the [latest version of the model](https://github.com/molgenis/rd-datamodel/blob/main/dist/umdm-emx1/umdm.xlsx) or [view the model schema](https://github.com/molgenis/rd-datamodel/blob/main/dist/umdm_schema.md) to see what's in the model.

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
3. **Run the setup script**: Run the [UMDM Setup script](https://github.com/molgenis/rd-datamodel/blob/main/emx/dist/umdm-emx1/umdm_setup.sh). This will import the model and all datasets into your Molgenis instance.

### Updating, building and deploying the UMDM

To update the UMDM, follow the steps below.

#### 1 Make changes to the model

Make all of the changes that are requested. For new entities (i.e., tables), open the YAML file and scroll to the `entities` section and enter the following information.

```yaml
entities:
    ...
    - name: myNewTable
      label: My New Table
      description: some description about my new table will go here
      tags: https://url.to.some/ontology/code/that/describes/my_table
      attributes:
        ...
```

If you are adding a new lookup, use one of the predefined attribute templates.

- `attributeTemplateDefault`: the recommended attribute template where the column `value` is the primary key. The value, which is a label, will be displayed when referenced in another table
- `attributeTemplateCode`: an alternative template where the column `code` is the primary key. This is useful for lookups where the code should be displayed instead of the label

To add new attributes, locate the appropriate table in the yaml script and create a new block under `attributes`.

```yaml
entities:
    ...
    - name: myTableThatIWantToEdit
      label: My table that I want to edit
      description: The table that I want to edit
      tags: https://url.to.some/ontology/code/that/describes/my_table
      attributes:
        ...
        
        - name: myNewAttribute
          description: a description about my new attribute
          dataType: ...
        # refEntity: ... # if type is a ref
          tags: https://url.to.some/ontology/code/that/describes/my_attribute
```

#### 2 Building

Test the model once all changes have been made.

```shell
yarn test
```

This test runs some basic error checking to make sure the model contains valid EMX markup. At the end of test, a print summary of the errors will be provided (if errors were detected). Scroll through the report to see find the errors.

When all of the changes have been made, build the model. Make sure the python library [yamlemxconvert](https://pypi.org/project/yamlemxconvert/) is installed and run the following yarn script.

```shell
yarn build
```

Make sure all tag errors have been resolved (`Unable to process tag: None`).

#### 3 Deploying

When built, deploy to the server. **NOTE**: make sure you export all data before importing the new model.

```shell
yarn m:config
yarn m:predeploy
yarn m:deploy
yarn m:postdeploy

yarn m:demo # if setting up a demo database
```

If you have added a new lookup table, you will need to update the `setup.sh` script.

```shell
yarn m:refresh-setup
```
