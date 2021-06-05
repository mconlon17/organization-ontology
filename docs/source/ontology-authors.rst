For Ontology Authors
====================

The Organization Ontology has been developed using |BFO|_ as an upper level ontology,
and in an attempt to follow the |OBOP|.  Many ontologies have been developed using
this approach.  Many of these ontologies can be found on `Ontobee <http://ontobee.org>`_

Domain
------

In designing the Organization Ontology, we first conceive of the domain of organizations,
that is we develop a use case for the ontology.  This *domain definition* guides us
throughout design and implementation, indicating terms that should be included and those
that should be defined elsewhere.  From time to time, terms must be defined to 
express important assertions regarding organizations, but have not been defined 
elsewhere in a forma that can be used here.  Such terms have a curation status
indicating that we we would prefer if these terms are defined elsewhere.

Reusing terms
-------------

We are generally cautious to reuse terms from other ontologies.  To reuse terms, we
require the ontology in which they are defined to:

1.  Use BFO has an upper level ontology.  We have made just a few exceptions and
    in each case we have provided a superclass for the term in BFO to create a
    consistent and complete subsumption hierarchy.
    
1.  Conform to OBO principles. Again, we have made just a few exceptions.

1.  An appropriate license for the ontology whose terms we will reuse.  When a license
    for an ontology is not clear, we cannot use its terms.
    
1.  Active maintenance.  Ontologies can be slow to add terms and to fix things that
    need fixing.  If an ontology is not actively maintained, we cannot use its terms.
    
1.  Use of MIREOT, a plug-in for protege.  When terms from other ontologies
    are needed, we use protege to edit `org-header.ttl` and add the the terms using
    the MIREOT plug-in.  This provides a consistent means for adding terms.
    
1.  We trim out annotation properties of included terms that are not of interest.

    
Use of templates
----------------

All terms defined in the Organization Ontology are created using templates.  There are
templates for classes, annotation properties, datatype properties, object properties,
and named individuals.  In each case, the columns correspond to annotations, class
expressions and other declarations used to create each term.

Consistent build
----------------

The ontology file ``org.ttl`` is built using a simple script, ``build.sh``  The script
performs four operations:

1.  Makes data useful for ontology users.

1.  Makes ontological assertions from the templates

1.  Merges org-header and the template assertions into ``org.ttl``

1.  Validates ``org.ttl``


Validation
----------

The ontology is validated on each build using *robot validate*

Documentation
-------------

We document the ontology as it is written.  See `For Documentation Authors 
<documentation-authors>_`  Documenting as we write the ontology helps with
consistency, accuracy, and completeness.