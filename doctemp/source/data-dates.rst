.. _datetimes:

.. index:: Dates, Data, Times, Datetimes

Dates Data
==========

The Organization Ontology includes a template (``templates\dates.tsv``) and 
data (``templates\dates.ttl``) built from the template for the dates
from 1800-2050 in year precision, one individual per year.  Most organizations have been 
established, or changed in this time
period, and year precision is often "good enough" for specifying these events.

The data have been created with standard URLs of the form

.. code-block::

    http://vivoweb.org/data/date/xxxx
    
A sample date is given below:

.. code-block::

	###  http://vivoweb.org/data/year/2021
	<http://vivoweb.org/data/year/2021> 
	    rdf:type owl:NamedIndividual ,
		         <http://www.w3.org/2006/time#Instant> ;
		<http://www.w3.org/2006/time#unitType> <http://www.w3.org/2006/time#unitYear> ;
		<http://www.w3.org/2006/time#inXSDDateTimeStamp> "2021-01-01T00:00:00Z"^^xsd:dateTimeStamp .
										
Including the file ``data/dates.ttl`` in your graph should provide you with all the
dates in year precision from 1800-2050.  You can then use these dates in
assertions about years.  For example, to assert organization x was
established in 1853 (see :doc:`Dates and Time <datetimes>`) you can say:

.. code-block::

  x output_of y
  y a founding_process
  y has_occurent_part z
  z a founding_process_boundary
  z has_instant <http://vivoweb.org/data/year/1853>




