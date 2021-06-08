Translating from schema.org to the Organization Ontology
=========================================================

`schema.org <https:/schema.org>`_ is an important folksonomy and JSON model
for representing common entities on the web.  The organization model of
schema.org has organization types and properties which can be represented using the 
Organization Ontology.

Full interoperability with schema.org is not currently a goal of the Organization 
Ontology work [1]_

Translating Types
-----------------

The schema.org organization types are listed in `Table 19`_  schema.org types are 
high-level and can
be multi-valued, much as Organization Ontology dispositions are multi-valued.

`Table 19`_ provides a guide for translating schema.org organizational types to assertions
in the VIVO Organization Ontology. 

.. _Table 19:

.. table:: Table 19 Translating schema.org types to VIVO Organizational assertions

    ========================== ======================================
    schema.org Type            Organization Ontology Assertions
    ========================== ======================================
    Airline                    Unknown type.  Typically company.
                                
                               Disposition is airline.
    Consortium                 Unknown type.  Assert Organization only.
    
                               Type is often nonprofit
                               
                               Disposition is often association                 
    Corporation                Type is company.
    
                               Disposition is often commerce.
    EducationalOrganization    Type is unknown.  Assert Organization only.
    
                               Disposition is education.
    FundingScheme              Type is unknown.  Assert organization only. [2]_
                               
                               Disposition is funding.
    GovernmentOrganization     Type is government organization
    
                               Disposition is unknown.
    LibrarySystem              Type is unknown.  Organization only.
    
                               Disposition is library.
    LocalBusiness              Type is company.
    
                               Disposition is often commerce.
    MedicalOrganization        Unknown type.  Assert Organization only.
                                
                               Disposition is healthcare provider
    NGO                        Type is nonprofit 
                                                                                      
                               Disposition is unknown.                  
    NewsMediaOrganization      Type is unknown.  Assert Organization only.
    
                               Disposition is media.
    PerformingGroup            Type is unknown.  Assert Organization only.
    
                               Disposition is performing
    Project                    Type is unknown.  Perhaps informal. [3]_
                               
                               Disposition is project.
    SportsOrganization         Type is unknown.  Assert organization only.
    
                               Disposition is sports.
    WorkersUnion               Type is unknown.  Often nonprofit.
    
                               Disposition is labor union.
    ========================== ======================================
    
.. rubric:: Footnotes

.. [1] Full interoperability between schema.org and the Organization Ontology could be
       future goal.  It appears that all the ontological structure is in place to add 
       additional
       properties and entities from schema.org to the Organization Ontology.
.. [2] Unclear if a funding scheme is an organization.  It might be an informal
       organization of those participating in the "scheme" or it may be an
       organizational part of an organization with funding disposition.
.. [3] In |BFO| ontologies, the word "project" is used to describe a particular
       type of process, that is, an occurent.  A project is not an organization.  A 
       project may "have" an
       organization, an organization may conduct a project.  In english, when people
       refer to a "project," they may be referring to an organization that was created
       for the purpose of executing a defined piece of work.  Such an organization
       may be formal or informal, it may be an organizational part, or an organization
       of its own.
