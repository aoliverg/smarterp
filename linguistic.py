from TBXTools import *

extractor=TBXTools()
extractor.create_project("linguistic.sqlite","eng",overwrite=True)
extractor.load_sl_tagged_corpus("HIV_AIDS-l3-tagged-en.txt")
extractor.load_linguistic_patterns("POS-patterns.txt")
extractor.tagged_ngram_calculation(nmin=1,nmax=3,minfreq=2)
extractor.linguistic_term_extraction(minfreq=2)
extractor.save_term_candidates("candidates-linguistic-eng.txt",minfreq=2)
