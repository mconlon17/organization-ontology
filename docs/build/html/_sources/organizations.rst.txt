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

:ref:`Figure 1` shows the classes and properties used to represent organizations in ORG.

.. _Figure 1:

.. figure:: ../img/org-overview.png
    :alt: Representation of organizations in ORG.  A complex ball and stick diagram

    Figure 1
    
    Representation of organizations.  The organization of interest is at the center of the
    figure
    
Types
------

Organizations have one of five types. See :ref:`Table 1`. These are mutually exclusive.  An organization can
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
    
:ref:`Figure 2` shows the classes and properties used to represent organizations in ORG.

.. _Figure 2:

.. figure:: ../img/org-types.png
    :alt: Types of organizations.  A simple ball and stick diagram

    Figure 2
    
    Subclasses of organization and subsumption hierarchy.  The subclasses are mutually exclusive.

Dispositions
------------

Organizations have dispositions which indicate the purposes organizations have.  An
organization might have a disposition of *library* or *healthcare* or *military*.
Dispositions are shown in :ref:`Table Dispositions`  An organization may have any number of
dispositions.

`Table Dispositions`_ lists the dispositions in the ORG ontology.
 
.. include:: tab-dispositions.rst

Examples
--------

.. topic:: Duke University

    Duke is a non-profit with a dispositions of university, education, and research
    
    Duke has an organization part, Duke Health, which has a disposition of
    healthcare.  Duke Health has an organizational part, Duke University Hospital,
    which has a disposition of hospital.
    
.. topic:: United States Navy

    The United States Navy is an organizational part with disposition of military.
    
.. topic:: BASF

    BASF is a company with a disposition of commerce.

.. rubric:: Footnotes

.. [#] By OBO-complaint, we mean the ORG ontology has been developed in accordance with
   |OBOP|_.

.. [#] The OBO community is having an on-going conversation about the subsumption of
   organization.  OBI defines organization as a material entity.  The VIVO Project disagrees with this
   assertion, as organizations can not be weighed, put in a box, or otherwise measured as
   material entities.  Their generic reliance on people *and* documents/understandings of 
   purpose seems to indicate that they are generically dependent on these components.