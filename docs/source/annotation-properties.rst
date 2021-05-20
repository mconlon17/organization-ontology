Annotation properties
======================

Annotation properties provide text for readers of ontologies to explain the
use of terms.  |IAO|_ defines annotation properties used throughout the VIVO ontologies
for defining terms.  :ref:`Table 5` lists the IAO properties used to annotate terms in the
ontologies.  :ref:`Table 6` lists the terms in the controlled vocabulary for curation
status.  To assert that a term's metadata is complete, the assertion is:

    <term> IAO:0000114 IAO_0000120
    
Alternative terms (IAO_0000118) are not common in the VIVO ontologies.  All other
annotations are expected for all terms.

.. include:: toc-AnnotationProperty.txt

.. _Table 8:

.. table:: Table 8 All Annotation Properties

    ===================  ========================  ================================================
    Term ID              Label                     Definition
    ===================  ========================  ================================================
    ``IAO_0000111``      editor preferred term     The concise, meaningful, and human-friendly name
    ``IAO_0000112``      example of usage          A phrase describing how a term should be used an
    ``IAO_0000114``      has curation status       A specification of the state of the metadata for
    ``IAO_0000115``      definition                The official definition, explaining the meaning 
    ``IAO_0000116``      editor note               An administrative note intended for its editor. 
    ``IAO_0000117``      term editor               Name of editor entering the term in the file. Th
    ``IAO_0000118``      alternative term          An alternative name for a class or property whic
    ``IAO_0000119``      definition source         Formal citation, e.g. identifier in external dat
    ``IAO_0000232``      curator note              An administrative note of use for a curator but 
    ``IAO_0000233``      term tracker item         An IRI or similar locator for a request or discu
    ``IAO_0000412``      imported from             For external terms/classes, the ontology from wh
    ``ORG_1000001``      organization annotation   This is a demo
    ===================  ========================  ================================================

.. _Table 5:

.. table:: Table 5 Common Annotation Properties

    ===============  =======================  ===================================================
    Property         Label                    Notes
    ===============  =======================  ===================================================
    ``IAO_0000112``  example of usage         A phrase describing how a term should be used
    ``IAO_0000114``  has curation status      A term from a controlled vocabulary
    ``IAO_0000115``  definition               Explains the meaning of a term or property
    ``IAO_0000116``  editor note              An administrative note intended for the term editor
    ``IAO_0000117``  term editor              Name of the editor
    ``IAO_0000118``  alternative term         Alternative name for the term
    ``IAO_0000119``  definition source        Definition citation, may be a link to definition
    ===============  =======================  ===================================================
    
.. _Table 6:

.. table:: Table 6 Curation Status

    ===============  =======================  ================================================
    Property         Label                    Notes
    ===============  =======================  ================================================
    ``IAO_0000120``  metadata complete        Term has all metadata, but may not be final
    ``IAO_0000121``  organizational term      Tags used to aid ontology development
    ``IAO_0000122``  ready for release        No further edits needed for term
    ``IAO_0000123``  metadata incomplete      Term is under development
    ``IAO_0000124``  uncurated                Name and class ID, little else
    ``IAO_0000125``  pending final vetting    Complete, awaiting final review
    ``IAO_0000423``  to be replaced with ext  The term is a placeholder and belongs elsewhere
    ===============  =======================  ================================================
    
Non IAO Annotation Properties
-----------------------------

The VIVO ontologies use other annotation properties to describe terms and the ontologies.

``rdfs:label`` is required for all terms and for the ontology itself.  All labels must be unique.  This greatly simplifies
the use of the ontologies -- one can search for the label and unambiguously find the
corresponding term.


Ontology annotations
....................

Several annotation are used to describe the ontology and are not used further.

``terms:license`` is required for all ontologies.  The license should be CC0 or CC-BY, no
other restrictions are acceptable for use in the VIVO ontologies.

``owl:versionIRI`` a URL identifying the ontology version

``owl:versionInfo`` a text string identifying the ontology version

``dc:created`` a date string specifying the date the ontology was originally created

``dc:creator`` a text string with the name and URL of the creator of the ontology

``dc:description`` a text description of the ontology, its domain, and purpose

``dc:title`` the name of the ontology to be used in citations

``rdfs:comment`` additional text describing the context of the ontology

Term annotations
................

The following annotations are used to describe terms that are imported to the ORG
ontology.  Most of these are substitutes for the standardized annotation 
properties describe above in :ref:`Table 5`.

``skos:altLabel``
``skos:definition``
``skos:example``
``skos:prefLabel``
``skos:scopeNote``
