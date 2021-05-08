.. _locations:

.. index:: Locations

Locations
=========

The Organization Ontology represents locations as places on the earth.  The following
entities have locations:

- continents
- countries.  Including disputed countries [1]_.
- regions of countries.  These may have many different names based on the local
  jurisdiction, such as territory, state, region, province, or even "kingdom" in the
  case of the United Kingdom.
- populated places, which may be cities [2]_.  These need not be legally recognized,
  merely recognized by people outside the populated place.
- :ref:`Facilities`

   
Properties of Locations
-----------------------

-- located in.  Paris is located in France.  France is located in Europe.
-- has geographic representation -- a text string of latitude and longitude of (hopefully)
   the centroid of the location.  For example, Paris has geographical representation
   "48.864716,2.349014"  Note there are no compass designations (E, W, N. S) in the 
   representation. A negative latitude is south of the equator, a positive latitude is
   north of the equator.  A negative longitude is east of the prime meridian,a positive
   longitude is west of the prime meridian.
   
Relations of Locations to Organizations and Facilities
------------------------------------------------------

:ref:`Organizations` do not have locations.  :ref:`Facilities` have locations.

.. rubric:: Footnotes
  
.. [1] definition of "countries" is a matter of dispute and controversy.  Any list of
   countries is subject to dispute.

.. [2] A city often means a governed place, or the government of the place, "The City
   of New York"  For our purposes we do not distinguish between city, town, village or
   other possibly formal, legal designations.