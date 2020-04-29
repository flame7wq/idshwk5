# idshwk5

### Detection Requirement
* Detect the DGA domains from the corpus

### What is the DGA
* Domain Generating Algorithm
* using seed(E.g. Date) to generate random domains to escapethe detection

### Corpus Description
### Benign Domain : Random selected from Alexa TOP1M
### Malicious Domain: [http://data.netlab.360.com/dga/](http://data.netlab.360.com/dga/)
---

* test.py will read train.txt and test.txt, then labeled thedomains in test.txt and output them to result.txt
* Python3 Prefered
* Hint
    * domain name length
    * numbers in the domain name
    * entropy of letteres
    * segmentation
