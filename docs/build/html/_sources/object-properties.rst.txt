Object Properties
==================

Object properties relate one entity to another (not one class to another) [Harmse2018]_. For example, an organization may be 
"part of" another organization.  "part of" is an object property that describes the 
relations between the two individual organizations.

|BFO| uses the 
`Relation Ontology (RO) <http://www.ontobee.org/ontology/RO>`_ to define object properties.

Each object property can have a domain and a range.  When we say property p has domain D,
we mean that all triples of the form x P y, x is a D.  When we say property p has range R,
we mean that in all triples of the form x P y, y is an R.

For example, if we define an object property "author_of", we might define the domain to
be "Person" and the range to be "Information Content Entity". If we write x author_of y,
we know x is a Person and y is an Information Content Entity. [#]_

.. include:: toc-ObjectProperty.txt

Common Object Properties
------------------------

Some object properties are quite common in the representation of scholarship.  Many
representations involve the use of identifiers.  People, publications, organizations
and other entities may be "denoted_by" an identifier.  We assert, for example,::

    x a Person
    y a ORCID
    x denoted_by y
    
"denoted_by" has an *inverse property* "denotes."  If x is denoted_by y, then y denotes x.
We could write the above as::

    x a Person
    y a ORCID
    y denotes x

See :ref:`Table 3`. The pattern *entity1 bearer_of role; role realized_in process; process
has_output entity2* is quite common and describes the role entity1 had through a process in
the creation of entity2. Each of these properties has an inverse, so we could assert
equivalently, *entity2 output_of process; process realizes role; role inheres in entity1*. 

.. _Table 3:

.. table:: Table 3 Common Object Properties

    ===============  =======================  ================================================
    Property         Label                    Notes
    ===============  =======================  ================================================
    ``BFO_0000050``  part of                  An entity is part of another entity
    ``BFO_0000051``  has part                 Inverse of part of
    ``IAO_0000219``  denotes                  The relation between an identifier and entity
    ``IAO_0000235``  denoted by               Inverse of denotes
    ``RO_0000053``   bearer of                relation between a dependent and its bearer
    ``RO_0000052``   inheres in               The inverse of bearer of
    ``BFO_0000055``  realizes                 A process realizes a role
    ``BFO_0000054``  realized in              A role is realized in a process
    ``RO_0002234``   has output               An occurrent has a continuant as an output
    ``RO_0002353``   output of                A continuant is the output of an occurrent
    ===============  =======================  ================================================

All Object Properties
-----------------------

`Table 12`_ lists all the object properties in the ORG ontology.

.. _Table 12:

.. table:: Table 12 All Object Properties

    ======================  ========================  ================================================
    Term ID                 Label                     Definition
    ======================  ========================  ================================================
    ``BFO_0000050``         part of                   A core relation that holds between a part and it
    ``BFO_0000051``         has part                  A core relation that holds between a whole and i
    ``IAO_0000136``         is about                  A (currently) primitive relation that relates an
    ``IAO_0000219``         denotes                   A primitive, instance-level, relation obtaining 
    ``IAO_0000235``         denoted by                Inverse of the relation 'denotes'
    ``ORG_2000001``         occupies                  An organization occupies a geographical location
    ``ORG_2000002``         has occurent part         A has part relation that applies only to occuren
    ``ORG_2000003``         has time instant          The property that associates a process boundary 
    ``RO_0000053``          bearer of                 A relation between an independent continuant (th
    ``RO_0000056``          participates in           A relation between a continuant and a process, i
    ``RO_0000057``          has participant           A relation between a process and a continuant, i
    ``RO_0000091``          has disposition           A relation between an independent continuant (th
    ``RO_0001015``          location of               A relation between two independent continuants, 
    ``RO_0001025``          located in                A relation between two independent continuants, 
    ``RO_0002012``          occurent part of          A part of relation that applies only between occ
    ``RO_0002131``          overlaps                  X overlaps y if and only if there exists some z 
    ``RO_0002234``          has output                P has output c iff c is a participant in p, c is
    ``RO_0002323``          mereotopologically relat  A mereological relationship or a topological rel
    ``RO_0002353``          output of                 Inverse of has output
    ``unitType``            temporal unit type        An indicator of the temporal precision of a time
    ======================  ========================  ================================================



.. [Harmse2018] Harmse, Henrietta, A Common Misconception regarding OWL Properties,
    blog post, https://henrietteharmse.com/2018/06/22/a-common-misconception-regarding-owl-properties/ 
    
.. rubric:: Footnotes

.. [#] Are these the correct domain and range for such a property? Discuss.

.. We will have a script that can read the ontology and write documentation pages, one per
   property.  The property pages will be listed in a toctree directive generated by the script 
   and included here.  In this way, we make sure all the properties are documented and that
   the document for each is generated automatically from the ontology.