.. _identifiers:

.. index:: identifiers

Identifiers
===========

An identifier is a string or symbol, assigned to an organization by a :ref:`dubbing 
process <glossary>`

The Organization Ontology uses `The Identifier Ontology  
<https://github.com/mconlon17/identifier-ontology>`_ to represent identifiers for
organizations.

The Identifier Ontology is a small set of terms in |IAO|_ to represent identifiers,
and in particular, persistent identifiers, often called PIDs.  Persistent identifiers
are maintained by one or more maintainers interested in the persistence of the 
identifier and its assignment to an entity over time.

The table below lists identifiers available in the Organization Ontology [1]_

.. include:: tab-all-identifiers.txt

Usage
-----

To assert that an organization has an identifier, we assert the existence of the
identifier of a particular type, its value/representation, and its association to the 
organization.  We say:

.. code-block::

   x denoted_by y
   y a research_orgnization_registry_identifier
   y has_representation "ror-value"

.. rubric:: Footnotes

.. [1] If a needed organization identifier is not in the table, please open a 
   Github issue with the name and source of the identifier for inclusion in subsequent
   releases of the Organization Ontology.

