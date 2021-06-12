#!/bin/bash

#       You will need to install json2rdf, riot, and robot to run this script
#       You may need to edit the script to provide the path to these tools on your system
#
#       This script builds a sample organization from data provided by ROR (ror.org)  You
#       can modify this script to produce organization data for any organization in ROR.
#       Set rorID to the ROR ID of the oragnization whose data you wish to fetch from ROR.
#       Set fileName to the name of the output file you wish to create to contain the rdf.
#       The resulting file will be in the build directory as fileName.ttl


        echo Build dates data using a template
        robot template \
            --template ../templates/dates.tsv \
            --prefix "time: http://www.w3.org/2006/time#" \
            convert --output build/dates.ttl
        echo Done
        echo ' '

        echo Build locations data by converting spreadsheet data to json to rdf
        echo "Convert local tsv data to JSON"
        python3 util/csv2json.py <source/locations.tsv >locations.json
        echo "Convert to Raw RDF"
        json2rdf http://my.org# <locations.json | riot --formatted=TURTLE >locations-raw.ttl
        echo "Convert to Organization Ontology RDF"
        robot query --input locations-raw.ttl --query source/locations.sparql build/locations.ttl
        rm locations-raw.ttl locations.json 
        echo Done
        echo ' '
        
        rorID=02y3ad647
        fileName=university-of-florida
        echo Build an organization by fetching ROR data
		echo "Get data for $filename from ROR"
		wget https://api.ror.org/organizations/https://ror.org/$rorID -qO- >$fileName.json
		echo "Convert to Raw RDF"
		json2rdf http://my.org# <$fileName.json | riot --formatted=TURTLE >$fileName-raw.ttl
		echo "Convert to ${3-new} Organization Ontology RDF"
		robot query --input $fileName-raw.ttl --query source/ror2org.sparql build/$fileName.ttl
		rm $fileName-raw.ttl $fileName.json 
		echo Done
