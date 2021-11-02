import argparse
import sys
import codecs
import os
import spacy

'''
import es_dep_news_trf
nlp = es_dep_news_trf.load()
doc = nlp("El copal se usa principalmente para sahumar en distintas ocasiones como lo son las fiestas religiosas.")
print([(w.text, w.lemma_, w.pos_) for w in doc])
'''

def go():
    global nlp
    global inputfile
    global outputfile
    entrada=codecs.open(inputfile,"r",encoding="utf-8")
    sortida=codecs.open(outputfile,"w",encoding="utf-8")
    for linia in entrada:
        linia=linia.strip()
        doc=nlp(linia)
        taggedline=[]
        for token in doc:
            tt=token.text+"|"+token.lemma_+"|"+token.pos_
            taggedline.append(tt)
        taggedline=" ".join(taggedline)
        print(taggedline)
        sortida.write(taggedline+"\n")
    sortida.close()

if __name__ == "__main__":     
    parser = argparse.ArgumentParser(description='A script to postag a text file using the Spacy taggers .')
    parser.add_argument("-i", "--input", dest="inputfile", type=str, help="The input file to tag.", required=True)
    parser.add_argument("-o", "--output", dest="outputfile", type=str, help="The output tagged file.", required=True)
    parser.add_argument("-l", "--lang", dest="lang", type=str, help="The language (ca, da, es, en, fr, de, el, it, ja, lt, mk, nb, nl, po, pt, ro, ru).", required=True)
 
    args = parser.parse_args()
    inputfile=args.inputfile
    outputfile=args.outputfile
    lang=args.lang
    
    if lang=="ca":
        try:
            import ca_core_news_trf
            nlp = ca_core_news_trf.load()
        except:
            print("No ca_core_news_trf found. Run: python -m spacy download ca_core_news_trf")
            sys.exit()
    elif lang=="da":
        try:
            import da_core_news_trf
            nlp = da_core_news_trf.load()
        except:
            print("No da_core_news_trf found. Run: python -m spacy download da_core_news_trf")
            sys.exit()
    elif lang=="zh":
        try:
            import zh_core_web_trf
            nlp = zh_core_web_trf.load()
        except:
            print("No zh_core_web_trf found. Run: python -m spacy zh_core_web_trf")
            sys.exit()
    elif lang=="nl":
        try:
            import nl_core_news_lg
            nlp = nl_core_news_lg.load()
        except:
            print("No nl_core_news_lg found. Run: python -m spacy download nl_core_news_lg")
            sys.exit()
    elif lang=="en":
        try:
            import en_core_web_trf
            nlp = en_core_web_trf.load()
        except:
            print("No en_core_web_trf found. Run: python -m spacy download en_core_web_trf")
            sys.exit()
    elif lang=="fr":
        try:
            import fr_core_news_sm
            nlp = fr_core_news_sm.load()
        except:
            print("No fr_core_news_sm found. Run: python -m spacy download fr_core_news_sm")
            sys.exit()
    elif lang=="de":
        try:
            import de_dep_news_trf
            nlp = de_dep_news_trf.load()
        except:
            print("No de_dep_news_trf found. Run: python -m spacy download de_dep_news_trf")
            sys.exit()
    elif lang=="el":
        try:
            import el_core_news_lg
            nlp = el_core_news_lg.load()
        except:
            print("No el_core_news_lg found. Run: python -m spacy download el_core_news_lg")
            sys.exit()
    elif lang=="it":
        try:
            import it_core_news_lg
            nlp = it_core_news_lg.load()
        except:
            print("No it_core_news_lg found. Run: python -m spacy download it_core_news_lg")
            sys.exit()
    elif lang=="ja":
        try:
            import ja_core_news_lg
            nlp = ja_core_news_lg.load()
        except:
            print("No ja_core_news_lg found. Run: python -m spacy download ja_core_news_lg")
            sys.exit()
    elif lang=="lt":
        try:
            import lt_core_news_lg
            nlp = lt_core_news_lg.load()
        except:
            print("No lt_core_news_lg found. Run: python -m spacy download lt_core_news_lg")
            sys.exit()
    elif lang=="mk":
        try:
            import mk_core_news_lg
            nlp = mk_core_news_lg.load()
        except:
            print("No mk_core_news_lg found. Run: python -m spacy download mk_core_news_lg")
            sys.exit()
    elif lang=="nb":
        try:
            import nb_core_news_lg
            nlp = nb_core_news_lg.load()
        except:
            print("No nb_core_news_lg found. Run: python -m spacy download nb_core_news_lg")
            sys.exit()
    elif lang=="po":
        try:
            import po_core_news_lg
            nlp = po_core_news_lg.load()
        except:
            print("No po_core_news_lg found. Run: python -m spacy download po_core_news_lg")
            sys.exit()
    elif lang=="pt":
        try:
            import pt_core_news_lg
            nlp = pt_core_news_lg.load()
        except:
            print("No pt_core_news_lg found. Run: python -m spacy download pt_core_news_lg")
            sys.exit()
    elif lang=="ro":
        try:
            import ro_core_news_lg
            nlp = ro_core_news_lg.load()
        except:
            print("No ro_core_news_lg found. Run: python -m spacy download ro_core_news_lg")
            sys.exit()
    elif lang=="ru":
        try:
            import ru_core_news_lg
            nlp = ru_core_news_lg.load()
        except:
            print("No ru_core_news_lg found. Run: python -m spacy download ru_core_news_lg")
            sys.exit()
    elif lang=="es":
        try:
            import es_dep_news_trf
            nlp = es_dep_news_trf.load()
        except:
            print("No es_dep_news_trf found. Run: python -m spacy download es_dep_news_trf")
            sys.exit()

    
    go()