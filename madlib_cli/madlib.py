import re
def wlcMsg():
    print("""
    *************************************
        Welcome to MAD LIB  Game


    Autohr:Abedalqader Alkhatib 

    Try a word puzzle and fill the Blanks

    *************************************    
    """)
wlcMsg()

def read_template(path):
    """ This function read text file and return a stripped string of the file’s contents. """
    try:
     with open(path) as tmp_file:
        file_content=tmp_file.read().strip()
        print('\n'+file_content+'\n')
        return file_content
    except:
        raise FileNotFoundError(f"({path}) was not found ")


def parse_template(str):
    """ This function takes string from the template file and returns a string with removed parts and a list of parts """
    new_list=[]
    partslist=re.findall(r'\{.*?\}',str)
    #print(partslist)    
    removed_parts_str=re.sub(r'\{.*?\}','{}',str)
    #print(removedPartsStr)
    for words in partslist:
        new_words=words.strip('{}')
        new_list.append(new_words)
    return removed_parts_str, tuple(new_list)

def merge(str,text):
    """This function takes empty template and the user entered parts then mearged it and return the merged string  """    
    print(text)
    merged_str=str.format(*text)
    print(merged_str)
    with open('madlib_cli/assets/test_result.txt','w') as test_result:
        test_result.write(merged_str)
    return merged_str

if __name__=="__main__":
    read_file=read_template('madlib_cli/assets/madlib_template.txt')
    text,words=parse_template(read_file)  
    res_arr=[]
    for i in words:
        user_entry=input(f"insert{i}>>") 
        res_arr.append(user_entry)
        game_res=merge(text,res_arr)