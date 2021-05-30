
	echo Processing data templates    
	robot template \
  	    --template templates/dates.tsv \
  	    --prefix "time: http://www.w3.org/2006/time#" \
  	    convert --output data/dates.ttl	
  	    
	echo Processing ontology templates    
	robot template \
  	    --template templates/annotation-properties.tsv \
  	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
  	    --prefix "bfo: http://purl.obolibrary.org/obo/BFO_" \
  	    --prefix "ro: http://purl.obolibrary.org/obo/RO_" \
  	    --prefix "iao: http://purl.obolibrary.org/obo/IAO_" \
  	    --prefix "time: http://www.w3.org/2006/time#" \
  	    convert --output templates/annotation-properties.ttl
  	robot template \
  	    --template templates/object-properties.tsv \
  	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
  	    --prefix "bfo: http://purl.obolibrary.org/obo/BFO_" \
  	    --prefix "ro: http://purl.obolibrary.org/obo/RO_" \
  	    --prefix "iao: http://purl.obolibrary.org/obo/IAO_" \
  	    --prefix "time: http://www.w3.org/2006/time#" \
  	    convert --output templates/object-properties.ttl
  	robot template \
  	    --template templates/datatype-properties.tsv \
  	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
  	    --prefix "bfo: http://purl.obolibrary.org/obo/BFO_" \
  	    --prefix "ro: http://purl.obolibrary.org/obo/RO_" \
        --prefix "obi: http://purl.obolibrary.org/obo/OBI_" \
  	    --prefix "iao: http://purl.obolibrary.org/obo/IAO_" \
  	    --prefix "time: http://www.w3.org/2006/time#" \
  	    convert --output templates/datatype-properties.ttl
  	robot template \
  	    --template templates/classes.tsv \
  	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
  	    --prefix "bfo: http://purl.obolibrary.org/obo/BFO_" \
  	    --prefix "ro: http://purl.obolibrary.org/obo/RO_" \
  	    --prefix "iao: http://purl.obolibrary.org/obo/IAO_" \
  	    --prefix "time: http://www.w3.org/2006/time#" \
  	    convert --output templates/classes.ttl
  	    
  	echo Assembling ontology
	robot merge \
	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
	    --prefix "bfo: http://purl.obolibrary.org/obo/BFO_" \
  	    --prefix "ro: http://purl.obolibrary.org/obo/RO_" \
  	    --prefix "iao: http://purl.obolibrary.org/obo/IAO_" \
  	    --prefix "time: http://www.w3.org/2006/time#" \
	    --input org-header.ttl \
	    --input templates/annotation-properties.ttl \
	    --input templates/object-properties.ttl \
	    --input templates/datatype-properties.ttl \
	    --input templates/classes.ttl \
	    convert --output org.ttl

    echo Running reports
	robot report --input org.ttl --output org-report.tsv

