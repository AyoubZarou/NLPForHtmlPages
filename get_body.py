import re
import urllib.request as request
from config import FILE_NAME

def get_body(data):
    """ get the body from a web page
    input:
     :data - a string that contains the complete html page source code
    return :
     :body - a parsed body, after getting rid of all the html tags, scripts,multiple line breaks or spaces.
    """
    pattern = re.compile(r'<body(.|\n)*>(.|\n)*</body>') # Using regular expressions to find the text between the body tags
    body = pattern.search(data) # return the data on the body
    body = body.group() # get the result in a string
    body = re.sub(r'<script*>*</script>','',body) # delete all the scripts 
    body = re.sub(r'<[^>]*>','',body) # get rid of all the html tags
    body = re.sub(r'&#39;',"'",body) # the code for ' is &#39; , for some raison it's not processed with the decode function,
                                     # so we do it afterwards 
    body = re.sub(r'\n(\s)+','\n',body) # get rid of the multispaces and multilinebreaks and use instead one linebreak
    with open(FILE_NAME, 'w') as file:  
        file.write(body) # write the results on a text file named body.txt on the same directory as the script
        file.close()
    return body

if __name__ == "__main__":
    url = ("https://support.mozilla.org/fr/products/firefox/basic-browsing-firefox") 
    html_page = request.urlopen(url).read().decode('utf-8') # we get the body from the url
    get_body(html_page)



    
