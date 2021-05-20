.. _organizations:

Organizations
=============
   
.. sidebar:: A new ORG ontology

   In :ref:`VIVO 1 <glossary>`, organizational representation was part of the VIVO ontology.  In the new VIVO ontology, organizational
   representation has been removed in favor of a new ORG ontology.  The ORG ontology is independent of VIVO and 
   can be used in any setting where information about organizations needs to be represented.
   
   The ORG ontology is based on |BFO| and is OBO-compliant [#]_ 

An organization is any collection of people with a purpose.  Organizations may be 
formal/legal, as in the case of universities and corporations, or they may be informal, 
as, for example, clubs.  Organizations may be parts of other organizations.

Subsumption 
----------------

Organizations are :ref:`generically dependent continuants <glossary>` [#]_ since they depend
on the people and documents which define them. All the people and documents may be replaced with
other people and documents, and the organization continues to exist.

Overview
----------

`Figure 1`_ shows the classes and properties used to represent organizations in ORG.
An overview of the classes and properties follows the figure.

.. _Figure 1:

.. figure:: ../img/org-overview.png
    :alt: Representation of organizations in ORG.  A complex ball and stick diagram

    Figure 1.  Representation of organizations.  The organization of interest is at the 
    center of the figure.  See notes below.
    
At the center of the figure note that an organization has a name (rdfs:label).

An organization has a type.  In the figure, the type of the organization is 
org:non-profit.  See below for a further discussion of types.

Now proceeding clockwise from type:

- An organization may be denoted by one or more identifiers.  Identifiers are represented
  using the Identifier Ontology (IDO).  Note that the identifier is an entity.  It exists
  independently of the organization to denotes.
- Orgs may be related to other orgs.  An org may be part of another organization.
- An org may be affiliated with another organization.
- An org may be denoted by a postal address.  See :doc:`Addresses <addresses>` for 
  details.  Addresses have
  properties that indicate how they are to be used.
- An org may have a predecessor organization.  Organizations undergo change.  The 
  resulting
  organization may be a new organization of a different type, different people, different 
  purpose.
- An organization may be a member of another organization.
- Organizations often have web sites.  Web sites are information content entities that are
  about the organization.  Note that the web site is an entity that exists with or without
  the organization it is about.
- Organizations have one or more dispositions.  Dispositions identify the purpose of an
  organization.  Dispositions of an organization may change over time.  See below for a 
  further discussion of dispositions.  A disposition is dependent the entity which
  has the disposition.  In BFO, a disposition is a specifically dependent continuant,
  dependent on the entity which has the specific disposition.
- An org may occupy zero or more facilities, such as an office building, or university 
  campus. A facility
  is typically a man-made structure attached to the ground.  As such, facilities have
  geographical locations -- in cities, for example.  See :doc:`Facilities <facilities>` 
  for more detail.
- Organizations come into being as the result of founding processes which have associated 
  dates.  See :doc:`Dates and Times <datetimes>` for
  a further discussion of the representation of dates and times related to organizations.
- Organizations may be denoted by one or more email addresses.  See :doc:`Addresses 
  <addresses>` for details.  As with postal addresses, email addresses may have 
  properties describing their purpose.

    
Types
------

Organizations have one of five types. See :ref:`Table 1`. These are mutually exclusive.  
An organization can
not be more than one type, just as an animal cannot be more than one species.

.. _Table 1:

.. table:: Table 1 Types of Organizations

    ===========  =======================  ===========================================================
    Term ID      Label                    Notes
    ===========  =======================  ===========================================================
    ORG_0000002  government organization  A government of some jurisdiction
    ORG_0000003  company                  An organization with a purpose to earn money for its owners
    ORG_0000004  non-profit organization  An organization which reinvests net revenue for its mission
    ORG_0000005  informal organization    An organization which is not formally constituted
    ORG_0000006  organization part        An organization which is a part of another organization
    ===========  =======================  ===========================================================
    
:ref:`Figure 2` shows the subsumption hierarchy for organization and its subclasses.

.. _Figure 2:

.. figure:: ../img/org-types.png
    :alt: Types of organizations.  A simple ball and stick diagram

    Figure 2.  Subclasses of organization and subsumption hierarchy.  The subclasses are 
    mutually exclusive.

Dispositions
------------

Organizations have dispositions which indicate the purposes organizations have.  An
organization might have a disposition of *library* or *healthcare* or *military*.
Dispositions are shown in :ref:`Table 13`  An organization may have any number 
of dispositions.

`Table 13`_ lists the dispositions  in the ORG ontology.

.. _Table 13:

.. table:: Table 13 All Dispositions

    ===================  ========================  ================================================
    Term ID              Label                     Definition
    ===================  ========================  ================================================
    ``ORG_0000007``      university                A disposition to award academic degrees and cond
    ``ORG_0000008``      association               A disposition to organize organizations or indiv
    ``ORG_0000009``      consortium                A disposition to organize organizations along in
    ``ORG_0000010``      service provider          A disposition to provide service with or without
    ``ORG_0000011``      laboratory service provi  A disposition to provide laboratory services.  I
    ``ORG_0000012``      extension provider        A disposition to provide extension services, typ
    ``ORG_0000013``      technology transfer       A disposition to create licenses for intellectua
    ``ORG_0000014``      philanthropy              A disposition to donate charitable causes, somet
    ``ORG_0000015``      funder                    A disposition to fund proposals, often is respon
    ``ORG_0000016``      health care service prov  A disposition to provider health care to humans
    ``ORG_0000017``      hospital service provide  A disposition to provide hospital-based health c
    ``ORG_0000018``      archive                   A disposition to collect, store, and provide acc
    ``ORG_0000019``      museum                    A disposition to collect, store, and provide acc
    ``ORG_0000020``      gallery                   A disposition to display collected works from an
    ``ORG_0000021``      publisher                 A disposition to publish information content ent
    ``ORG_0000022``      research                  A disposition to conduct research
    ``ORG_0000023``      education                 A disposition to teach, and provide experiential
    ``ORG_0000024``      training                  A disposition to train, and provide experiential
    ``ORG_0000025``      research administration   A disposition to provide resources and oversight
    ``ORG_0000026``      library                   A disposition to provide library services
    ``ORG_0000027``      commerce                  A disposition to sell things
    ``ORG_0000028``      military                  A disposition to engage in warfare
    ``ORG_0000029``      religious                 A disposition to engage in matters of spirtualit
    ``ORG_0000030``      governance                A disposition to provide governance
    ``ORG_0000031``      information address disp  A dispositon of an information content entity de
    ``ORG_0000032``      billing address disposit  A disposition of an address to be used to receiv
    ``ORG_0000033``      shipping address disposi  A disposition of an address to be used to receiv
    ``ORG_0000034``      preferred address dispos  A disposition of an address to be displayed in m
    ===================  ========================  ================================================

Examples
--------

.. topic:: Duke University

    Duke is a non-profit with a dispositions of university, education, and research
    
    Duke has an organization part, Duke Health, which has a disposition of
    healthcare.  Duke Health has an organizational part, Duke University Hospital,
    which has a disposition of hospital.
    
.. topic:: United States Navy

    The United States Navy is an organization part of the US Department of Defense 
    with disposition of military.
    
.. topic:: BASF

    BASF is a company with a disposition of commerce.

.. rubric:: Footnotes

.. [#] By OBO-complaint, we mean the ORG ontology has been developed in accordance with
   |OBOP|_.

.. [#] The OBO community is having an on-going conversation about the subsumption of
   organization.  OBI defines organization as a material entity.  The VIVO Project 
   disagrees with this
   assertion, as organizations can not be weighed, put in a box, or otherwise measured as
   material entities.  Their generic reliance on people *and* documents/understandings of 
   purpose seems to indicate that they are generically dependent on these components.