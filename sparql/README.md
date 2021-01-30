# SPARQL queries

[SPARQL](https://www.w3.org/TR/rdf-sparql-query/) is a W3C standard
query language for RDF. This directory contains SPARQL queries for
checking and reporting on the ontology.

These queries are run during build and release processes to validate
the ontology and to provide reports.  Outputs of these queries
aere stored in the reports directory.

We use `robot` to perform the queries as this allows easy execution over any OWL file.

Queries are organized into three collections:

## Constraint Violation checks

These are all named `*violation.sparql`. 
Consult the individual sparql files to see the intent of the check.

## Construct queries

These are named `construct*.sparql`, and always have the form `CONSTRUCT ...`.

These are used to generate new OWL axioms that can be inserted back
into the ontology.

## Reports

The remaining SPARQL queries are for information purposes.