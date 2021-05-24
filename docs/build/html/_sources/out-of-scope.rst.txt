Out of Scope Terms
=======================================================

In designing and building ontologies, one seeks to find a coherent domain for the
ontology -- a set of terms that are useful in representing the entities of the domain,
include and reuse terms from other ontologies as appropriate, while not including terms
that belong elsewhere.  These choices are somewhat arbitrary, as long as we have a
cler view of the domain we are attempting to represent, and we are willing to "give away"
terms that we included, but can be reused.

For the Organization Ontology, we adhered as best we could to several guiding principles
regarding terms, domains, inclusion and exclusion.

And, of course, we may have a change of heart regarding any term or set of terms.

Out of Scope but Defined Here
------------------------------

.. topic:: `Locations <locations>`_

	It is important for organizations and their facilities to be located on the surface of
	the earth.  We found the existing OBI ontologies `ENVO 
	<https://sites.google.com/site/environmentontology/>`_ and `GAZ 
	<http://environmentontology.github.io/gaz/>`_ to have 
	inconsistencies
	and/or complexities that prohibited their reuse.  We created a simple  set of terms within
	the Organization Ontology to define a nested set of locations from continents down
	to rooms that can have geographical representations (latitude and longitude) attached 
	to them.

	We would be happy to use terms from another ontology that defines location terms we
	could use.

.. topic:: `Facilities <facilities>`_

  The Organization Ontology has a need to make assertions regarding occupancy of
  structures
  
Out of Scope and Included Here
------------------------------

An organization ontology should reuse terms it needs from other ontologies.

.. topic:: Upper Level Ontology and Annotation Properties

   |BFO|_ is used for an upper level ontology.  We use the |IAO|_ annotation properties to 
   annotate terms.  We use Dublin Core and OWL annotation properties annotate the 
   ontology.
   
.. topic:: Identifiers

   `The Identifier Ontology <https://github.com/mconlon17/identifier-ontology>` [#]_ 
   defines identifiers and semantics for using
   identifiers to identify organizations, people, and scholarly works.
   
.. topic:: Information Artifacts

   The |IAO|_ defines information artifacts needed here.
   
.. topic:: Time

   The |Time|_ is used to define time:Instant and associated properties for using
   time:Instant.  We have asserted a superclass for time:Instant to align it with
   BFO.
   
.. topic:: Concepts

   The |SKOS|_ issued to define skos:Concept.  We have asserted a superclass for skos:Concept
   to align it with BFO.

Out of Scope and Not Included Here
----------------------------------

.. topic:: Reports to / has report

	reports to / has report are properties in the `W3C Organization Ontology 
	<https://www.w3.org/TR/vocab-org/>`_ for
	asserting that individual people report to other individual people in an organization.

	We believe these are out of scope for an organization ontology, and are best left to an
	administrative ontology.

.. topic:: Additional detail regarding locations

  We have tried to include enough, but not too much.  This is not a locations 
  ontology. [#]_

.. topic:: Additional detail regarding structures

  We have tried to include enough, but not too much.  This is not a structures 
  ontology. [#]_.
  
.. topic:: Properties related to Academic Events

  We have not included properties related to organizations must host, sponsor or otherwise
  participate in.  See `The Academic Event Ontology 
  <https://github.com/tibonto/aeon>`_ for terms associating
  organizations and academic events.



.. rubric:: Footnotes

.. [#] We follow in the footsteps of :ref:`VIVO 1 <glossary>`, including terms that have 
   shown their value over a decade of use.
   
.. [#] Same as the comment on locations.

.. [#] The Identifier Ontology is underdeveloped as a planned expansion of |IAO|_