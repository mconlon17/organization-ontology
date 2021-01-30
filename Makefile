# Simple Makefile
all:
	robot extract --method BOT --input imports/bfo.owl --term-file imports/bfo_terms.txt \
	    convert --output imports/bfo_import.ttl
	robot extract --method BOT --input imports/iao.owl --term-file imports/iao_terms.txt \
	    convert --output imports/iao_import.ttl
	robot extract --method BOT --input imports/time.owl --term-file imports/time_terms.txt \
	    convert --output imports/time_import.ttl
	    
	robot template \
  	    --template templates\annotation-properties.tsv \
  	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
  	    convert --output annotation-properties.ttl
  	robot template \
  	    --template templates\object-properties.tsv \
  	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
  	    convert --output object-properties.ttl
  	robot template \
  	    --template templates\datatype-properties.tsv \
  	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
  	    convert --output datatype-properties.ttl
  	robot template \
  	    --template templates\classes.tsv \
  	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
  	    convert --output classes.ttl
  	    
	robot merge \
	    --prefix "org: http://purl.obolibrary.org/obo/ORG_" \
	    --input org-header.ttl \
	    --input imports/bfo_import.ttl \
	    --input imports/iao_import.ttl \
	    --input templates\annotation-properties.ttl \
	    --input templates\object-properties.ttl \
	    --input templates\datatype-properties.ttl \
	    --input templates\classes.ttl \
	    convert --output org.ttl

	robot report --input org.ttl --output org-report.tsv

