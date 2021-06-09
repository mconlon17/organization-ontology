Translating from VIVO to the Organization Ontology
=======================================================

For those familiar with representing organizations using the VIVO Ontology,
we provide a guide for translating assertions in the VIVO Ontology to assertions
in the Organization Ontology [#]_.

Translating Types
-----------------

The VIVO Ontology organization types are presented in `Table 17`_ with instructions
for translating each.  The Organization Ontology separates the concept of
what the organization "is" (company, organization part, etc) from what the 
organization "does" (hospital, library, etc).  In many cases, the VIVO Ontology
combined these and information about one or the other ("is", "does") is missing.

For example, consider vivo:Museum.  This assertion of type is actually an
assertion of purpose.  The type of organization (organization part, nonprofit) is
missing.  We can assert the museum is an organization, and has a disposition of
museum.  We may be able to bring additional information to bear and assert a
a specific type [#]_.

`Table 17`_ provides a guide for translating Organizational types to assertions
in the Organization Ontology. 

.. _Table 17:

.. table:: Table 17 Translating VIVO types to Organizational Ontology assertions

    ========================== ================================
    VIVO Type                  Organization Ontology Assertions
    ========================== ================================
    Association                Unknown type.  Assert Organization only.
    
                               Type is often nonprofit.
                                
                               Disposition is association.
    Center                     Unknown type.  Assert organization only.
      
                               Type is often an organization part. 
                                                                                      
                               Unknown dispositions.  Often research.                  
    College                    Unknown type.  Assert organization only.
    
                               At a US university, an organizational part.
                               
                               At a US university, dispositions of education, service, 
                               research
    Company                    Type is Company
    
                               Disposition is often commerce
    Consortium                 Unknown type.  Assert Organization only.
    
                               Type is often nonprofit
                               
                               Disposition is often association
    CoreLaboratory             Type is organization part
    
                               Dispositions are laboratory and service provider
    Department                 Type is organizational part
    
                               Unknown dispositions
    Division                   Type is organizational part
    
                               Unknown dispositions
    ExtensionUnit              Type is organizational part
    
                               Disposition is agricultural extension
    ERO_00000565               Type is organizational part
    
                               Disposition is technology transfer
    Foundation                 Type may be nonprofit
    
                               Type may be organizational part
                               
                               May be affiliated with another organization
                               
                               Disposition is philanthropy
    
                               Disposition may be funder                        
    FundingOrganization        Unknown type.  Assert organization only.
    
                               Disposition is funder
    GovernmentAgency           Type is government organization or organizational part
    
                               Disposition is unknown
    Hospital                   Unknown type.  Assert organization only.
    
                               Disposition is hospital.
    Institute                  Unknown type.  Assert organization only.
    
                               Disposition is unknown.  Often research.
    Laboratory                 Unknown type.  Assert organization only.
    
                               Disposition is laboratory.
    Library                    Unknown type.  Assert organization only.
    
                               Disposition is library.
    Museum                     Unknown type.  Assert organization only.
    
                               Disposition is library.
    Program                    Type is organizational part.
    
                               Disposition is unknown.
    Publisher                  Type is unknown.  Assert organization only.
    
                               Often type is company.  But all others possible.
    
                               Disposition is publisher.
    ResearchOrganization       Unknown type.  Assert organization only.
    
                               Disposition is research.
    School                     Type is unknown.  Assert organization only.
    
                               At US university, an organizational part.
                               
                               Disposition is often education.                         
    ServiceProvidingLaboratory Type is unknown.  Assert organization only.
    
                               Dispositions are laboratory and service provider.
    StudentOrganization        Type is organizational part
    
                               Disposition is unknown
                               
                               Quality is student led.
    Team                       Type is unknown.  Assert organization only.
    
                               Disposition is unknown [#]_
    University                 Type is unknown.  Assert organization only.
    
                               Disposition is university
    
                               Dispositions are typically education, research, service
    ========================== ================================
    
A Cross Index
=============

`Table 10`_ provides a complete cross-reference for all terms in the VIVO 1 Ontology to
terms in the Organization Ontology.  This is **not** a translation table.  The cross
indicates which terms in the Organization Ontology have been linked via annotation
property 
:doc:`doc-ORG_1000001` with one or more terms in the VIVO 1 Ontology.  This "linking" 
indicates only that the terms are similar in their meaning and/or usage.

Some VIVO 1 terms map to multiple Organization Ontology terms.  For example, a
ServiceProvidingLaboratory in VIVO 1 is an organizaition with a service
providing disposition and a laboratory disposition in the Organization Ontology.
 

.. include:: tab-vivoxref.txt

.. rubric:: Footnotes

.. [#] We intend to provide SPARQL CONSTRUCT queries for automatica translation of
   VIVO Ontology organization assertions to Organization Ontology assertions
   in the future.  Consider this guide as advice to the adventurous, or to collaborators
   who would like to draft, test, and contribute such queries.
   
.. [#] Note that additional information is needed.  The Metropolitan Museum of Art
   in New York City is a nonprofit organization.  The Florida Museum of Natural
   History in Gainesville, Florida, is an organizational part of the University of 
   Florida.  In the VIVO
   Ontology, both would be asserted to be type vivo:Museum.  In the Organization
   Ontology, the first would be asserted to be nonprofit, the second organization
   part.  Both would be asserted to have disposition museum.

.. [#] Team may mean "sports team" or "project team" or other.  A sports team may
   be formal, such as Manchester United Football Club, or informal as in "my weekly
   bowling team."  A project team may be considered part of an organization, or
   informally organized to move work forward. 