Translating from VIVO to the VIVO Organization Ontology
=======================================================

For those familiar with representing organizations using the VIVO Ontology,
we provide a guide for translating assertions in the VIVO Ontology to assertions
in the VIVO Organization Ontology [#]_.

Translating Types
-----------------

The VIVO Ontology organization types are presented in `Table 14`_ with instructions
for translating each.  The VIVO Organization Ontology separates the concept of
what the organization "is" (company, organization part, etc) from what the 
organization "does" (hospital, library, etc).  In many cases, the VIVO Ontology
combined these and information about one or the other ("is", "does") is missing.

For example, consider vivo:Museum.  This assertion of type is actually an
assertion of purpose.  The type of organization (organization part, non-profit) is
missing.  We can assert the museum is an organization, and has a disposition of
museum.  We may be able to bring additional information to bear and assert a
a specific type [#]_.

`Table 14`_ provides a guide for translating VIVO organizational types to assertions
in the VIVO Organization Ontology. 

.. _Table 14:

.. table:: Table 14 Translating VIVO types to VIVO Organizational assertions

	========================== ============================
	VIVO Type                  VIVO Organization Assertions
	========================== ============================
	Association                Unknown type.  Assert Organization only.
	
	                           Type is often non-profit.
	                           	
	                           Disposition is association.
	Center                     Unknown type.  Assert organization only.
	  
	                           Type is often an organization part. 
	                           							                              
	                           Unknown dispositions.  Often research.				   
	College                    Unknown type.  Assert organization only.
	
	                           At a US university, an organizational part.
	   						   
	                           At a US university, dispositions of education, service, research
	Company                    Type is Company
	
	                           Disposition is often commerce
	Consortium                 Unknown type.  Assert Organization only.
	
	                           Type is often non-profit
	                           
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
	Foundation                 Type may be non-profit
	
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
                               
	                           Quality is student led [#]_
	University                 Type is unknown.  Assert organization only.
	
	                           Disposition is university
	
	                           Dispositions are typically education, research, service
	========================== ============================

.. rubric:: Footnotes

.. [#] We in tend to provide SPARQL CONSTRUCT queries for automatica translation of
   VIVO Ontology organization assertions to VIVO Organization Ontology assertions
   in the future.  Consider this guide as advice to the adventurous, or to collaborators
   who would like to draft, test, and contribute such queries.
   
.. [#] Note that additional information is needed.  The Metropolitan Museum of Art
   in New York City is a non-profit organization.  The Florida Museum of Natural
   History in Gainesville, Florida, is an organizational part of the University of 
   Florida.  In the VIVO
   Ontology, both would be asserted to be type vivo:Museum.  In the VIVO Organization
   Ontology, the first would be asserted to be non-profit, the second organization
   part.  Both would be asserted to have disposition museum.
   
.. [#] To be determined.  