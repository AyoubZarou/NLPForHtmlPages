# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:44:55 2019

@author: ZAROU AYOUB
"""
import re
import spacy 
nlp=spacy.load('fr_core_news_sm') # this might take a little time
def process_body(body=None):
    """
    input : 
    *****
        body : a string that contains the body after being processed and structured
    return :
    ******
        associations: it contains the verbs on the file and all the nouns that may go hand in hand 
        with the verb, the result is stored in a python dictionary structure
        
    the result is also stored on a text file named processed_data.txt
    
    """    
    if not body: 
        try :  # if body not given , we try to read it from a text file
            with open('body.txt','r') as f :
                body= f.read()
                f.close()
        except : 
            print('No body given, the parameter is necessary if there is no file body.txt, you may need t execute get_body first')
            return
    associations={}
    for line in body.splitlines(): # we process each line on its own
        doc=nlp(line)
        verb_pattern=re.compile(r'.*ée?s?$') # a pattern to spot all the adjectives that nlp happens to identify as verbs
        verb_in_the_line=None
        for token in doc :
            if token.pos_=="VERB" and not verb_pattern.match(token.text):
               verb_in_the_line=token.text
            if verb_in_the_line and token.pos_=="NOUN":
                if verb_in_the_line in associations:
                    associations[verb_in_the_line].append(token.text)
                else : 
                    associations[verb_in_the_line]=[token.text]
    with open('processed_data.txt','w') as f : # we store the results on a text file 
        for key in associations : 
            line=key +" "*(20-len(key))+':  '+', '.join(associations[key])+'\n'
            f.write(line)
    return associations
process_body()
