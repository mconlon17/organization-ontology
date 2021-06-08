.. _addresses:

.. index:: addresses

Addresses
=========

The Organization Ontology represents addresses (postal and email) as "things" that denote
organizations.

Email Addresses
---------------

``IAO_0000429`` is the term id for the class email address. It is an information artifact 
that denotes an
organization and has a text string representation.

If y is the URI of an organization we can say y has email address info@abc.com by 
asserting:

.. code-block::

    y denoted_by x
    x a email_address
    x has_email_representation "info@abc.com"
    
Because the email address is a thing, we can assign qualities to it. Email addresses may
have purposes (dispositions) to help users route email effectively. We might say:

.. code-block::

    x has_disposition z
    z a information_address_disposition
    
to indicate that x is an email address that can be used by people to ask questions and
get help.

Postal Addresses
----------------

Postal addresses are represented in a manner analogous to email addresses -- postal
addresses are information artifacts that denote an organization. Like email
addresses they may have qualities (dispositions) that help people use the postal
address effectively. Postal addresses are things. The term ID is ``IAO_0000422``.

Postal addresses are text strings in which the "parts" of a postal address are 
delimited by semicolons. Applications can parse these strings into parts needed
by the application. Parts and parsing vary by jurisdiction but should conform to 
`Universal Postal Union <https://www.upu.int>`_ standards in implementations.

To say org y has a billing postal address, we can assert:

.. code-block::

    y denoted_by x
    x a postal_address
    x has_disposition z
    z a billing_address_disposition
    x has_postal_address_representation "line 1; line 2; city; region; country; postal-code"
    
Terms used to represent Addresses
---------------------------------

:ref:`Table 11` lists term ids used in the representation of addresses

.. _Table 11:

.. table:: Table 11 Terms used to represent addresses

    ======================  ===========================================================
    Term                    Notes
    ======================  ===========================================================
    :doc:`doc-IAO_0000235`  An organization is denoted by an address
    :doc:`doc-IAO_0000429`  An entity with properties and a value
    :doc:`doc-ORG_3000002`  A datatype property to contain an email address string
    :doc:`doc-RO_0000091`   Object property relating an entity to a disposition
    :doc:`doc-ORG_0000031`  A quality of an adress to obtain information
    :doc:`doc-IAO_0000422`  An entity with properties and a value for postal delivery
    :doc:`doc-ORG_0000032`  An address used to send bills to an entity
    :doc:`doc-ORG_3000003`  An datatype property to contain a postal address string
    ======================  ===========================================================

