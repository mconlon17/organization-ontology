
.. _Table ObjectProperty:

.. table:: ObjectProperty

    ===================  ========================  ================================================
    Property             Label                     Definition
    ===================  ========================  ================================================
    ``BFO_0000050``      part of                   a core relation that holds between a part and it
    ``BFO_0000051``      has part                  a core relation that holds between a whole and i
    ``BFO_0000062``      preceded by               x is preceded by y if and only if the time point
    ``BFO_0000063``      precedes                  x precedes y if and only if the time point at wh
    ``BFO_0000066``      occurs in                 b occurs_in c =def b is a process and c is a mat
    ``BFO_0000067``      contains process          [copied from inverse property 'occurs in'] b occ
    ``IAO_0000136``      is about                  A (currently) primitive relation that relates an
    ``ORG_2000001``      date established          Date the organizational was established.
    ``RO_0000056``       participates in           a relation between a continuant and a process, i
    ``RO_0000057``       has participant           a relation between a process and a continuant, i
    ``RO_0002012``       occurent part of          A part of relation that applies only between occ
    ``RO_0002013``       has regulatory component  A 'has regulatory component activity' B if A and
    ``RO_0002014``       has negative regulatory   A relationship that holds between a GO molecular
    ``RO_0002015``       has positive regulatory   A relationship that holds between a GO molecular
    ``RO_0002017``       has component activity    None
    ``RO_0002018``       has component process     w 'has process component' p if p and w are proce
    ``RO_0002022``       directly regulated by     None
    ``RO_0002023``       directly negatively regu  Process(P2) is directly negatively regulated by 
    ``RO_0002024``       directly positively regu  Process(P2) is directly postively regulated by p
    ``RO_0002025``       has effector activity     A 'has effector activity' B if A and B are GO mo
    ``RO_0002086``       ends after                None
    ``RO_0002087``       immediately preceded by   None
    ``RO_0002090``       immediately precedes      None
    ``RO_0002131``       overlaps                  x overlaps y if and only if there exists some z 
    ``RO_0002180``       has component             w 'has component' p if w 'has part' p and w is s
    ``RO_0002211``       regulates                 process(P1) regulates process(P2) iff: P1 result
    ``RO_0002212``       negatively regulates      Process(P1) negatively regulates process(P2) iff
    ``RO_0002213``       positively regulates      Process(P1) postively regulates process(P2) iff:
    ``RO_0002215``       capable of                A relation between a material entity (such as a 
    ``RO_0002216``       capable of part of        c stands in this relationship to p if and only i
    ``RO_0002222``       temporally related to     None
    ``RO_0002233``       has input                 p has input c iff: p is a process, c is a materi
    ``RO_0002263``       acts upstream of          c acts upstream of p if and only if c enables so
    ``RO_0002264``       acts upstream of or with  c acts upstream of or within p if c is enables f
    ``RO_0002304``       causally upstream of, po  None
    ``RO_0002305``       causally upstream of, ne  None
    ``RO_0002323``       mereotopologically relat  A mereological relationship or a topological rel
    ``RO_0002327``       enables                   None
    ``RO_0002328``       functionally related to   A grouping relationship for any relationship dir
    ``RO_0002329``       part of structure that i  this relation holds between c and p when c is pa
    ``RO_0002331``       involved in               c involved_in p if and only if c enables some pr
    ``RO_0002333``       enabled by                inverse of enables
    ``RO_0002334``       regulated by              inverse of regulates
    ``RO_0002335``       negatively regulated by   inverse of negatively regulates
    ``RO_0002336``       positively regulated by   inverse of positively regulates
    ``RO_0002352``       input of                  inverse of has input
    ``RO_0002404``       causally downstream of    inverse of upstream of
    ``RO_0002405``       immediately causally dow  None
    ``RO_0002410``       causally related to       This relation groups causal relations between ma
    ``RO_0002411``       causally upstream of      p is causally upstream of q if and only if p pre
    ``RO_0002412``       immediately causally ups  p is immediately causally upstream of q iff both
    ``RO_0002418``       causally upstream of or   p 'causally upstream or within' q iff (1) the en
    ``RO_0002427``       causally downstream of o  inverse of causally upstream of or within
    ``RO_0002428``       involved in regulation o  c involved in regulation of p if c is involved i
    ``RO_0002429``       involved in positive reg  c involved in regulation of p if c is involved i
    ``RO_0002430``       involved in negative reg  c involved in regulation of p if c is involved i
    ``RO_0002431``       involved in or involved   c involved in or regulates p if and only if eith
    ``RO_0002432``       is active in              c executes activity in d if and only if c enable
    ``RO_0002434``       interacts with            A relationship that holds between two entities i
    ``RO_0002436``       molecularly interacts wi  An interaction relationship in which the two par
    ``RO_0002447``       phosphorylates            None
    ``RO_0002448``       directly regulates activ  The entity A, immediately upstream of the entity
    ``RO_0002449``       directly negatively regu  The entity A, immediately upstream of the entity
    ``RO_0002450``       directly positively regu  The entity A, immediately upstream of the entity
    ``RO_0002464``       helper property (not for  None
    ``RO_0002479``       has part that occurs in   p has part that occurs in c if and only if there
    ``RO_0002481``       is kinase activity        None
    ``RO_0002500``       causal agent in process   A relationship between a material entity and a p
    ``RO_0002501``       causal relation between   p is causally related to q if and only if p or a
    ``RO_0002506``       causal relation between   None
    ``RO_0002559``       causally influenced by    None
    ``RO_0002563``       interaction relation hel  None
    ``RO_0002564``       molecular interaction re  None
    ``RO_0002566``       causally influences       The entity or characteristic A is causally upstr
    ``RO_0002578``       directly regulates        Process(P1) directly regulates process(P2) iff: 
    ``RO_0002584``       has part structure that   s 'has part structure that is capable of' p if a
    ``RO_0002595``       causal relation between   A relationship that holds between a material ent
    ``RO_0002596``       capable of regulating     Holds between c and p if and only if c is capabl
    ``RO_0002597``       capable of negatively re  Holds between c and p if and only if c is capabl
    ``RO_0002598``       capable of positively re  Holds between c and p if and only if c is capabl
    ``RO_0002608``       process has causal agent  Inverse of 'causal agent in process'
    ``RO_0002629``       directly positively regu  Process(P1) directly postively regulates process
    ``RO_0002630``       directly negatively regu  Process(P1) directly negatively regulates proces
    ``RO_0004031``       enables subfunction       Holds between an entity and an process P where t
    ``RO_0004032``       acts upstream of or with  None
    ``RO_0004033``       acts upstream of or with  None
    ``RO_0004034``       acts upstream of, positi  c 'acts upstream of, positive effect' p if c is 
    ``RO_0004035``       acts upstream of, negati  c 'acts upstream of, negative effect' p if c is 
    ``RO_0004046``       causally upstream of or   None
    ``RO_0004047``       causally upstream of or   None
    ``RO_0011002``       regulates activity of     The entity A has an activity that regulates an a
    ``TopProperty``      None                      None
    ===================  ========================  ================================================
