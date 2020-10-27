import rdflib, pprint
from rdflib import URIRef, Graph
from rdflib.plugins import sparql

g = Graph()
g.load('galnet/rdf_galnet_glg.ttl', format='turtle')

#g.parse('galnet/rdf_galnet_glg.ttl', format='n3')