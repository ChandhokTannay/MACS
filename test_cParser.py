#!/usr/bin/env python
# Python 3 Integration : Tannay Chandhok
from MACS2.IO.cParser import BEDParser

#fhd = gzip.open("peakcalling/ChIP_0.1.bam","r")

a_parser = BEDParser("ChIP_0.1.bed.gz")

a = parser.build_fwtrack()

b_parser = BEDParser("Control_0.1.bed.gz")

b = parser.build_fwtrack()
