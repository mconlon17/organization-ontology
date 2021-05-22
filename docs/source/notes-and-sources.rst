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
Protege [mireot]_ for
adding terms from other ontologies to ``org-header.ttl``  We use robot [robot]_ for
processing templates of properties, merging them and ``org-header.ttl`` together to
produce ``org.ttl`` and then to run reports against ``org.ttl`` for validation.

We have tried to represent organizations in a manner that is inclusive of ideas
regarding organizations that have been represented elsewhere.  The VIVO 
Ontology [vivo2013]_
provides organizational representation, but is not BFO or OBO conformant.  We
hope we have represented here what is represented in the VIVO Ontology.  The WC
Organization Ontology [Reynolds2014]_ has been a second source for terms and
concepts that might be included in a BFO/OBO conformant ontology.

Regarding the W3C Organization Ontology
---------------------------------------

The W3C Organization Ontology provides a set of useful terms for representing
organizations.  Many terms there are represented in this work.  Our work
uses BFO as an upper level ontology -- everything in the Organization Ontology
fits in the BFO subsumption hierarchy.  cross-walking the W3C Organization
Ontology and the VIVO Organization Ontology is straightforward.  Below are
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
  relationships in VORG.
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
   
.. [Musen2015] Musen, M.A. The Protégé project: A look back and a look forward. AI Matters. 
   Association of Computing Machinery Specific Interest Group in Artificial Intelligence, 
   1(4), June 2015. https://doi.org/10.1145/2757001.2757003.

.. [mireot]
   
.. [robot]

.. [vivo2013]

.. [Reynolds2014] Reynolds, Dave (ed) (2014) The Organization Ontology.  
   W3C.  https://www.w3.org/TR/vocab-org/