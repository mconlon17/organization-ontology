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
- :doc:`facilities <facilities>`

Properties of Locations
-----------------------

- located in.  The Louvre is located in Paris.  Paris is located in France.  Metropolitan 
  France is located in Europe.
- has geographic representation -- a text string of latitude and longitude of (hopefully)
  the centroid of the location.  For example, Paris has geographical representation
  "48.864716,2.349014"  Note there are no compass designations (E, W, N. S) in the 
  representation. A negative latitude is south of the equator, a positive latitude is
  north of the equator.  A negative longitude is east of the prime meridian,a positive
  longitude is west of the prime meridian.
   
Relations of Locations to Organizations and Facilities
------------------------------------------------------

Organizations occupy locations.  They are not "located in" locations for two reasons:

1.  Organizations are not material.  Only material things have locations.  An Organization
    such as a chess club may meet in a variety of locations, but they are not located
    in a location.  An organization such as Amazon has a presence in many locations.
2.  "located in" means all of something located wholly within something else.

Organizations occupy locations.  This means they have some legal right to the location 
(own, lease, title, other) or they have one or more persons affiliated with the 
organization who is at the location (all or some of the time). While
occupation may involve disputes, most do not.

We can then say

.. code-block::

  The University of Florida 'occupies' The University of Florida Gainesville campus
  The University of Florida Gainesville campus 'is located in' Gainesville
  The University of Florida Gainesville campus 'has geolocation representation' "29.6436325,-82.3571242" 
  
Note that 'located in' is transitive.  Gainesville is located in Florida.  Florida is 
located in the United States.  We can infer that the University of Florida campus is 
located in the United States.

:doc:`Organizations <organizations>` do not have locations.  Facilities, and buildings 
have locations. Campuses have locations.

:ref:`Table 14` lists terms used in the representation of locations

.. _Table 14:

.. table:: Table 14 Terms used to represent locations

    ======================    ===========================================================
    Term                      Notes
    ======================    ===========================================================
    :doc:`doc-ORG_0000040`    A man-made construction attached to the ground, a bauwerk
    :doc:`doc-ORG_0000041`    The grounds of a business, university, or other
    :doc:`doc-ORG_0000042`    An architectural structure with a function
    :doc:`doc-ORG_0000043`    A permanent walled and roofed construction
    :doc:`doc-ORG_0000044`    A space delineated by partitions in a building
    :doc:`doc-ORG_0000047`    One of the seven major land masses of the earth
    :doc:`doc-ORG_0000048`    The territory occupied by a sovereign state
    :doc:`doc-ORG_0000049`    Any subdivision of the territory of a country
    :doc:`doc-ORG_0000050`    Any named place on the earth occupied by people
    :doc:`doc-ORG_2000002`    The relation indicating an organization occupies a location
    :doc:`doc-RO_0001015`     Location of
    :doc:`doc-RO_0001025`     Located in
    :doc:`doc-ORG_0000045`    A geographical location on the earth
    :doc:`doc-ORG_0000046`    A point on the earth
    :doc:`doc-ORG_3000004`    A geolocation representation as lat,long
    ======================    ===========================================================

.. rubric:: Footnotes
  
.. [1] definition of "countries" is a matter of dispute and controversy.  Any list of
   countries is subject to dispute.

.. [2] A city often means a governed place, or the government of the place, "The City
   of New York"  For our purposes we do not distinguish between city, town, village or
   other possibly formal, legal designations.