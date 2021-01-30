# Templates for building the Organization Ontology

`robot` templates are used to build the ontology.  Templates are
simple TSV files with one row per entity and columns representing
entity properties.  Special format headers are used as instruction
to `robot` for constructing OWL assertions from template entries.

Editors edit infoprmation in the templates, adding rows for new
entities.

During the build process, the Makefile executes `robot` on 
changed template files to create corresponding OWL files.  These
OWL files are then merged to produce the Organization Ontology.

There are four templates corresponding to the four types of
OWL entities:

1. Annotation template for annotation properties
1. Object property template for defining object properties
1. Datatype properties template for defining datatype properties
1. Classes template for defining classes


