.. _facilities:

.. index:: Facilities

Facilities
==========

A facility is a human-made structure, attached to the ground.  Examples include

- buildings, including special purpose building such as hospitals and libraries
- campuses and other collections of building in contiguous space
- bridges, monuments, parks, parking lots, towers, dams, and all other human-made 
  structures on the ground

Note that we exclude structures in space, non human made structures such as ant hills,
and geological "structures" such as caves.

We also exclude spaces in facilities that that may have a specific purpose.  We may say
"the gene sequencing facility located in Building 42," but the gene sequencing
"facility" in this sentence is not a facility in the sense described here.

Facilities in the Organization Ontology
---------------------------------------

The Organization Ontology is focused on organizations.  Organizations have relations
to Facilities -- they may occupy, own, lease, or otherwise be related.  It is
not the purpose of the Organization Ontology to provide extensive representation of
facilities.  The Organization Ontology has simple representations that appear to cover
important use cases, particularly in the representation of organizations in scholarship.

Types of Facilities
-------------------

 - building
 - campus
 
Perhaps we do do not need more than these to start.

Properties of Facilities
------------------------

- have names, abbreviations, nicknames, and acronyms.
- have locations.  Facilities may be "located in" a city, or may have
  a geolocation with a latitude/longitude representation.
- have identifiers. These are represented using the Identifier Ontology (IDO).
- A facility may be part of a campus.
- A room may be located in a building.

Relation of Organizations and Facilities
-----------------------------------------

- occupies.  The organization has zero or more of its people residing in or working at
  or regularly visiting the facility.  Occupies can be used when the ownership
  of a facility is not of interest, ambiguous, or unknown.
  
No other relations are anticipated for the Organization Ontology.