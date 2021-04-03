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

.. figure:: ../img/OrganizationModel.png
    :alt: Representation of organizations in ORG.  A complex ball and stick diagram

    Figure 1
    
    Representation of organizations.  Dark blue is the organization class.  Light blue
    are entities dependent on the existence of a particular individual organization.  Green
    are entities which would exist if the organization is removed.
    
Types
------

Organizations have one of five types. See :ref:`Table 1`. These are mutually exclusive.  An organization can
not be more than one type, just as an animal cannot be more than one species.

.. _Table 1:

.. table:: Table 1 Types of Organizations

    ===========  =======================  ================================================
    Class        Label                    Notes
    ===========  =======================  ================================================
    ORG_0000001  Government Organization  A government of some jurisdiction
    ORG_0000002  Company                  An org to earn money for its owners
    ORG_0000003  Non-Profit               An org to reinvest money for its mission
    ORG_0000004  Informal                 An org which is not formally constituted
    ORG_0000005  Organization Part        An org which is a part of another org
    ===========  =======================  ================================================

Dispositions
------------

Organizations have dispositions which indicate the purposes organizations have.  An
organization might have a disposition of *library* or *healthcare* or *military*.
Dispositions are shown in :ref:`Table 2`  An organization may have any number of
dispositions.

.. _Table 2:

.. table:: Table 2 Dispositions of Organizations

	===========  ==========  ================================================
	Class        Label        Notes
	===========  ==========  ================================================
	ORG_0000021  Hospital    Provides in-patient healthcare services
	ORG_0000022  Healthcare  Provides any of a variety of healthcare services
	ORG_0000023  Library     Provides access to information resources
	ORG_0000024  University  Conducts higher education activities
	ORG_0000025  Commerce    Conducts commercial activities
	ORG_0000026  Military    Conducts military activities
	ORG_0000027  Education   Provides opportunties for teaching and learning
	ORG_0000028  Research    Advance knowledge through research activities
	ORG_0000029  Archive     Collects, curates, and preserves materials
	ORG_0000030  Religious   Conducts religious activities
	===========  ==========  ================================================

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