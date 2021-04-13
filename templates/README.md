# Templates for building the Organization Ontology

[`robot`](http://robot.obolibrary.org/) templates are used to build the ontology.  Templates are
simple TSV files with one row per entity and columns representing
entity properties.  Special format headers are used as instruction
to `robot` for constructing OWL assertions from template entries.

Editors edit infoprmation in the templates, adding rows for new
entities.

During the build process, theb uild script executes `robot` on 
the template files to create corresponding OWL files in TTL format.  These
OWL files are then merged with a `org-header.ttl` to produce the Organization Ontology.

There are four templates corresponding to the four types of
OWL entities:

1. Annotation properties template for defining annotation properties
1. Object properties template for defining object properties
1. Datatype properties template for defining datatype properties
1. Classes template for defining classes


