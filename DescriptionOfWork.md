# LDE Trial Day - Description of Work

<!-- vim-markdown-toc GitLab -->

* [Introduction](#introduction)
* [Initial Preparation](#initial-preparation)
* [Product Data Integration](#product-data-integration)
    * [Source Data](#source-data)
    * [Your Tasks](#your-tasks)
        * [Task 1: Ontology Engineering](#task-1-ontology-engineering)
        * [Task 2: Ontology Review (with domain expert)](#task-2-ontology-review-with-domain-expert)
        * [Task 3: Map source files](#task-3-map-source-files)
        * [Task 4: Answer business questions](#task-4-answer-business-questions)
        * [Optional Task: Showcase individual skills](#optional-task-showcase-individual-skills)
        * [Final Presentation](#final-presentation)
    * [The following technologies / constraints should be used:](#the-following-technologies-constraints-should-be-used)

<!-- vim-markdown-toc -->

## Introduction

Welcome to your eccenca Linked Data Expert (LDE) / Knowledge Engineer / Data Architect Trial Day Smile :).
We hope this document provides all relevant information you need in order to showcase your skills based on the given task.

If you see yourself unable to work on all the tasks (in full) we would like to see your best efforts and/or additional ideas.
As some of the latter task built upon earlier ones you might reach out to your host asking for reference material to work on such in case you did not completed the prerequisite task(s). 

If you are in doubt or need help, do not hesitate to ask your host.

## Initial Preparation 

The following things have to be done at the beginning of the trial day:

- You need to tell us your account name at gitlab.com
    - create a new account, if you do not have a gitlab.com account or if you do not want to use your existing account
- We will create a repository at https://gitlab.com/eccenca/lde-trial-day-yourname and give you access to it
    - please do not publish your trial work in a public repository

## Product Data Integration

### Source Data

- [orgmap.xml](./data/orgmap.xml) - an organisational structure of the client
- [products.xlsx](./data/products.xlsx) - a list of products
- [services.csv](./data/services.csv) - a list of services that are applicable for some products (e.g. can be maintenance services, or other add ons)

### Your Tasks

![Task Overview](./DescriptionOfWork.png "Task Overview")

Based on the given (customer) datasets, an ontology should be engineered, the data shall be integrated in a knowledge graph as well as the business questions should be answered from that graph:

#### Task 1: Ontology Engineering

As an LDE, I want to have a domain ontology that is capable to represent and integrate the data points from my (disparate) source datasets
create an RDF/RDFS/OWL ontology for representing the content of the given source files

- document the tool(s) you use to create it
- commit a turtle serialized version of the ontology into the repository

#### Task 2: Ontology Review (with domain expert)

As an LDE, I want to discuss and verify my ontology modelling with a domain expert, therefor I need to prepare proper materials for presentation and discussion with such a persona (non graph/non RDF/non tech-savvy)

- describe how you would envision an effective iteration with a domain expert and what you would prepare for such discussion
- prepare an human-readable documentation and/or graph visualization and/or ... and commit them to the repository

#### Task 3: Map source files 

As an LDE, I want to integrate the source datasets into a knowledge graph / RDF representation

- turn the source data into RDF
- use the approach / tools of your preference and document it
- commit the result instance RDF data in turtle serialization into the repository

#### Task 4: Answer business questions

As an LDE, I want to answer business questions based on the created knowledge graph (e.g. using SPARQL queries)

- demonstrate how you use the knowledge graph to answer two or more of the following business questions:
    - Find related products (e.g. cluster by packaging size or weight)
    - Find services / products without a product manager
    - Find services / products without responsible department
    - Identify alternative experts that can take over responsibility

#### Optional Task: Showcase individual skills

In case you have tools or techniques in mind that could be used to the benefit of this potential customer please feel free to describe and/or showcase, this could include but is not limited to:
- usage of data mining, dashboarding or other analytics tools
- usage of Machine Learning or other algorithms 
- ... surprise us (wink)

#### Final Presentation

As an LDE, I want to present my working results to the customer in order to close the project

- prepare a slide deck, which summarizes your project work
- prepare to give us this talk and try stay under 15min with result presentation
- Target audience is partially technical folks but includes also non technical persons

### The following technologies / constraints should be used:

- Vocabulary / Ontology modelling based on OWL / RDFS and RDF 
    - https://www.w3.org/TR/rdf-schema/
    - https://www.w3.org/OWL/
- turtle serialization for ontology and instance data
- git repository usage (gitlab) using adequate (developer like) standards
- gitlab.com based project management (organise versions, tasks / issues, spec there, communicate there)
- basic documentation (README.md, ontology and data artifacts)

