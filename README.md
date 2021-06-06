# Organization Ontology

**Early DRAFT**

This is draft work, and an effort to create an OBO-compliant, BFO-based,
reusable, maintained ontology based on data regarding research organizations
maintained by [ROR](http://ror.org) and pioneered by [GRID](http://grid.ac).

If successful, we hope to register the work as
http://obofoundry.org/ontology/org

For background regarding this work, see [Early Thoughts on Representing
Organizations in VIVO](http://bit.ly/2EhMdPq).  The ontology here is intended to
be useful to the [VIVO Project](http://vivoweb.org) but does not depend in any
way on VIVO, its ontologies, nor its software.

## Development

We use a simple build script (`build.sh`) to build terms from templates (see
templates folder), and merge these with a header file (see `org-header.ttl`).
The resulting ontology is verified using `robot report` and various sparql
queries are run on the ontology to provide reports and additional validation.

Editors of this ontology should edit the templates in the templates folder.
Imported terms are added to the `org-header.ttl` file using protege and the
MIREOT plug-in.

## Documentation

Documentation for the Organization Ontology is produced using ReadTheDocs,
Sphinx, and RestructuredText.  The documentation is built using GitHub Actions
and is available as [HTML](https://mconlon17.github.io/organization-ontology),
[PDF](https://github.com/mconlon17/organization-ontology/blob/master/docs/build/latex/theorganizationontology.pdf), and
[ePub](https://github.com/mconlon17/organization-ontology/blob/master/docs/build/epub/TheOrganizationOntology.epub).

## Data

We will provide tools for converting ROR entries into ORG ontology assertions.
See the data folder.

## Contact

Please use this GitHub repository's [Issue
tracker](https://github.com/mconlon17/organization-ontology/issues) to request
new terms/classes or report errors or specific concerns related to the ontology.

Requests for new organizations should be directed to [ROR](https://ror.org).