# Setting up the system : installing all the necessary packages

To use the script, you need to have Python 3 installed. Then you need to install spacy, for that sake, please visit the spacy usage page [here](https://spacy.io/usage/)


# The different components on the script 

The file is a two functions based script : 
## `get_body`
 ```python
def get_body(html) :
'''
 input : 
        
 data : a string that contains the complete html page source code 
 
 return :
        
 body: a parsed body, after getting rid of all the html tags, scripts,multiple spaces and line breaks
 '''
 ```
 The get_body function takes an html page as a string, and processes the body of the page and, as it returns it as a string, it creates a text file named `body.txt` and stores the result on it
 ## `process_body`
 
```python
  def process_body(body=None)
    """
    input : 
    ----------
        body : a string that contains the body after being processed and structured, if body is not given, the scripts tries to 
        fond it on the body.txt if it's already created
    return :
    -----------

        associations: it contains the verbs on the file and all the nouns that may go hand in hand 
        with the verb, the result is stored in a python dictionary structure
        
    the result is also stored on a text file named processed_data.txt
    
    """  
```
# Execute the script 

The script may be executed from the terminal, all you need to do is execute `python get_body.py` at first, and then `python process_body.py`, the final result is stored on the text file `processed_data.txt`
