Translating from ROR to the Organization Ontology
=======================================================

|ROR|_ provides data on over 95,000 research organizations in the world.  ROR data
is available CC0, curated, and via an open API.

Translating Types
-----------------

The ROR Organization types are listed in `Table 15`_  ROR types are high-level and can
be multi-valued, much as Organization Ontology dispositions are multi-valued.

Organizations without research disposition are out of scope for ROR.  All organizations in
ROR can be asserted to have research disposition.

`Table 16`_ provides a guide for translating VIVO organizational types to assertions
in the VIVO Organization Ontology. 

.. _Table 16:

.. table:: Table 16 Translating ROR types to VIVO Organizational assertions

    ========================== ======================================
    ROR Type                   VIVO Organization Ontology Assertions
    ========================== ======================================
    Education                  Unknown type.  Assert Organization only.
                                
                               Disposition is education, research
    Healthcare                 Unknown type.  Assert organization only. 
                                                                                      
                               Disposition is healthcare, research.                  
    Company                    Type is company.
    
                               Disposition is research.
    Archive                    Type is unknown.  Assert Organization only.
    
                               Disposition is archive, research.
    Nonprofit                  Type is nonprofit
                               
                               Disposition is research.
    Government                 Type is government organization
    
                               Disposition is research.
    Facility                   Type is unknown.  Organization only.
    
                               Disposition is research.
    Other                      Type is unknown.
    
                               Disposition is research.
    ========================== ======================================

