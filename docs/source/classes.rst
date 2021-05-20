Classes
==============
**Classes** are collections of **individuals**.  A university, a non-profit, a government agency, and a role in a project are
all individuals.  Classes of individuals are defined by specifying members (extension) or more frequently 
in scholarship, by specifying conditions (intension).

In ontologies, and using :ref:`OWL <glossary>`, individuals
instances of classes. Classes are arranged
in subsumption hierarchies, indicating that individuals in one class are members of some 
higher class.  For example, a cat is a mammal.  Your cat is an instance of the
class cat.  All cats are mammals.  We say cat is a subclass of mammal.  We can infer that all individuals that are
cats are mammals.  Your cat is a cat, so we can infer your cat is a mammal.

.. include:: toc-Class.txt


All Classes
-----------------

`Table 9`_ lists all the classes in the ORG ontology.

.. _Table 9:

.. table:: Table 9 All Classes

    ===================  ========================  ================================================
    Term ID              Label                     Definition
    ===================  ========================  ================================================
    ``BFO_0000001``      entity                    The fundamental thing that has existence. All th
    ``BFO_0000002``      continuant                An entity which has existence in time
    ``BFO_0000003``      occurrent                 An entity which occurs in time
    ``BFO_0000004``      independent continuant    B is an independent continuant = Def. b is a con
    ``BFO_0000008``      temporal region           An occurent which is some part of time
    ``BFO_0000015``      process                   P is a process = Def. p is an occurrent that has
    ``BFO_0000016``      disposition               A realizable entity that presents in a continuan
    ``BFO_0000017``      realizable entity         To say that b is a realizable entity is to say t
    ``BFO_0000020``      specifically dependent c  B is a specifically dependent continuant = Def. 
    ``BFO_0000029``      site                      B is a site means: b is a three-dimensional imma
    ``BFO_0000031``      generically dependent co  B is a generically dependent continuant = Def. b
    ``BFO_0000035``      process boundary          P is a process boundary =Def. p is a temporal pa
    ``BFO_0000038``      one-dimensional temporal  A one-dimensional temporal region is a temporal 
    ``BFO_0000040``      material entity           A material entity is an independent continuant t
    ``BFO_0000141``      immaterial entity         An immaterial entity is the boundary or interior
    ``BFO_0000148``      zero-dimensional tempora  A temporal region of no duration.
    ``IAO_0000030``      information content enti  A generically dependent continuant that is about
    ``IAO_0000422``      postal address            A textual entity that is used as directive to de
    ``IAO_0000429``      email address             A designation used to deliver email to a recipie
    ``ORG_0000001``      organization              A group of people recognized as such by people o
    ``ORG_0000002``      government organization   An organization which is the body of persons tha
    ``ORG_0000003``      company                   A legal entity of associated persons created for
    ``ORG_0000004``      non-profit organization   A legal entity of associated persons created for
    ``ORG_0000005``      informal organization     A group of people recognized as such by people o
    ``ORG_0000006``      organization part         An organization which exists as part of another 
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
    ``ORG_0000035``      architectural structure   A material entity that is a human made strcuture
    ``ORG_0000036``      facility                  An architectural structure that bears some funct
    ``ORG_0000037``      building                  A permanent walled and roofed construction
    ``ORG_0000038``      geographical location     A place on the earth
    ``ORG_0000039``      geographical point        A point located on the earth
    ``ORG_0000040``      founding process          The process by which the organization was founde
    ``ORG_0000041``      founding process boundar  The process boundary which defines the moment of
    ``ORG_0000042``      dissolution process       The process by which an organization no longer e
    ``ORG_0000043``      dissolution process boun  The process boundary which marks the moment at w
    ``ORG_0000044``      campus                    The geographic location consisting of the  groun
    ``Instant``          Time instant              A zero-dimensional part of time.  Precision may 
    ``TemporalUnit``     Temporal unit             A specification of a time duration.  Used to spe
    ===================  ========================  ================================================

.. We have have a script that can read the ontology and write documentation pages, one per
   class.  The class pages will be listed in a toctree directive generated by the script 
   and included here.  In this way, we make sure all the classes are documented and that
   the document for each is generated automatically from the ontology.
