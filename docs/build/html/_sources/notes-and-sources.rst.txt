Notes and Sources
=================

For early work on the Organization Ontology and thoughts behind what might be needed 
and how things might be addressed, we relied on "Early Thoughts on Representing 
Organizations in VIVO" by the VIVO Ontology Interest Group [VOIG2021]_.  While not 
everything there 
has been implemented here, and not everything here is implemented as described there, 
the general outline of representing organizations using |BFO|_ according to |OBOP|_ was
first described there.

We use [Wikipedia]_, [Wiktionary]_, and [Wikidata]_ often.  Term definitions, 
references, fact-checking, and identifiers may come from these sources.

We use Ontobee [Ong2017]_ for looking up terms in OBO Foundry ontologies.

We use Protege [Musen2015]_ for modeling ``org-header.ttl`` and the MIREOT plug-in for 
Protege [Hannah2012]_ for
adding terms from other ontologies to ``org-header.ttl``  We use robot [Jackson2019]_ for
processing templates of properties, merging them and ``org-header.ttl`` together to
produce ``org.ttl`` and then to run reports against ``org.ttl`` for validation.

We have tried to represent organizations in a manner that is inclusive of ideas
regarding organizations that have been represented elsewhere.  The VIVO 
Ontology [vivo2013]_
provides organizational representation, but is not BFO or OBO conformant.  We
hope we have represented here what is represented in the VIVO Ontology.  The W3C
Organization Ontology [Reynolds2014]_ has been a second source for terms and
concepts that might be included in a BFO/OBO conformant ontology.

We have used the [GRID]_, [ROR21]_, and [schema.org]_ data models as sources of 
concepts and properties that may need to be represented in the Organization
Ontology.  See :doc:`vivo-to-org`, :doc:`ror-to-org`, and :doc:`schema-to-org` for 
details of how
types and other properties are mapped from these sources to the Organization Ontology.

Regarding the W3C Organization Ontology
---------------------------------------

The W3C Organization Ontology (W3CO) provides a set of useful terms for representing
organizations.  Many terms there are represented in this work.  Our work
uses BFO as an upper level ontology -- everything in the Organization Ontology
fits in the BFO subsumption hierarchy.  cross-walking the W3C Organization
Ontology and the VIVO Organization Ontology (VORG) is straightforward.  Below are
comments related to mapping.

- Purpose in W3CO is open-ended text.  In VORG, purpose is represented by dispositions
- Classification in W3CO are interests in VORG.
- Identifiers in VORG are handled using IDO
- Linked to in W3CO is replaced by semantic object properties indicating the 
  relationship between
  organizations 
- Formal Organization in W3CO is any organization that is not an Informal Organization
  in VORG.
- OrganizationUnit in W3CO is Organization Part in VORG.
- Membership in VORG is modeled using standard BFO roles and occurent part representation
- Posts in W3CO are modeled as positions in VORG in a manner analogous to memberships
  (same conceptual model, different roles and entities)
- Reports to in W3CO is deconstructed.  Personnel relationships are distinct from org
  relationships in VORG.  Person to person relationships are out of scope for VORG.
- Locations in VORG are modeled as BFO sites.  See `Locations <locations>`
- Addresses in VORG are modeled as IAO entities.  See `Addresses <addresses>`
- *based at* is a property of a person and is out of scope for VORG.
- OrganizationCollaboration is a project and is modeled using standard BFO constructs.
  Organizations have *participant in* projects
- Change event is a BFO process boundary
  
References
----------

.. [Wikipedia] Wikipedia (2021) we site.  http://wikipedia.org

.. [Wiktionary] Wiktionary (2021) web site. http://wiktionary.org

.. [Wikidata] Wikidata (2021) web site. http://wikidata.org

.. [Ong2017] Ong E, Xiang Z, Zhao B, Liu Y, Lin Y, Zheng J, Mungall C, Courtot M, 
   Ruttenberg A, He Y. Ontobee: A linked ontology data server to support ontology term 
   dereferencing, linkage, query, and integration. Nucleic Acid Research. 2017 
   Jan 4;45(D1):D347-D352. PMID: 27733503. PMCID: PMC5210626.

.. [VOIG2021] VIVO Ontology Interest Group (2021) Early Thoughts on the representation
   of organizations in VIVO.  on-line.  http://bit.ly/2EhMdPq
   
.. [Musen2015] Musen, M.A. The Protégé project: A look back and a look forward. AI 
   Matters. 
   Association of Computing Machinery Specific Interest Group in Artificial Intelligence, 
   1(4), June 2015. https://doi.org/10.1145/2757001.2757003.

.. [Hannah2012] Hannah, J, Chen, C, Crow, WA, et al. (2012) Simplifying MIREOT: A 
   MIREOT Protege Plugin. International Semantic Web Conference, 
   http://ceur-ws.org/Vol-914/paper_48.pdf
   
.. [Jackson2019] Jackson, R.C., Balhoff, J.P., Douglass, E. et al. ROBOT: A Tool 
   for Automating Ontology Workflows. BMC Bioinformatics 20, 407 (2019). 
   https://doi.org/10.1186/s12859-019-3002-3

.. [vivo2013] Conlon, M. Mitchell, S. (2018) VIVO Ontology for Researcher Discovery.
   Ontology. 
   https://bioportal.bioontology.org/ontologies/VIVO

.. [Reynolds2014] Reynolds, Dave (ed) (2014) The Organization Ontology.  
   Ontology.  https://www.w3.org/TR/vocab-org/
   
.. [GRID] Digital Science, (2021) GRID Global Research Identifier Database.
   https://grid.ac

.. [ROR21] ROR Community (2021) Research Organization Registry. Database.
   https://ror.org

.. [schema.org] W3C Schema.org Community Group (2021) Schema.org. Website. 
   https://schema.org