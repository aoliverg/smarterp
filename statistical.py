from TBXTools import *
extractor=TBXTools()
extractor.create_project("statistical.sqlite","eng",overwrite=True)
extractor.loadSLTokenizer("MTUOC_tokenizer_eng")
extractor.load_sl_corpus("Occupational_safety_and_health-l1-en.txt")
extractor.ngram_calculation(nmin=2,nmax=3)
extractor.load_sl_stopwords("stop-eng.txt")
extractor.load_sl_inner_stopwords("inner-stop-eng.txt")
extractor.statistical_term_extraction()
extractor.case_normalization(verbose=True)
extractor.nest_normalization(verbose=True)
extractor.load_sl_exclusion_regexps("regexps.txt")
extractor.regexp_exclusion(verbose=True)
extractor.save_term_candidates("candidates-stat-eng.txt")

 
