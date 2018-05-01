"""it coverts the text file into a list"""
import re
        
def load(txt_file):
    final_list = []
    FILE = open(txt_file, 'r')
    raw_data = FILE.read()
    p1 = ('System Test Results')
    p2 = ('Passed')
    txt_data = raw_data[raw_data.find(p1) +len(p1)+ 1 : raw_data.rfind(p2)+ len(p2)].strip()
    final_data = re.sub('\n+', '\n',  txt_data)
    final_data1 = final_data.replace('{', '[').replace('}', ']')
    list_str = final_data1.split('\n')
    INPUT=[]
    OUTPUT=[]
    for item in list_str[1:]:
        value = item.strip().split('\t\t')
        v=value[0]
        output_value=value[1]
        p1="("+v+")"
        input_value=eval(p1)
        INPUT.append(input_value)
        OUTPUT.append(output_value)
    solution={"out":OUTPUT,"inp":INPUT} 
    return solution
