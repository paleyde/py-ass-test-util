from nose.tools import *
from sys import argv
import os.path
import os
import sys
import imp
import re
from mysite.core.src.table import TABLE
from mysite.core.src.convert import load
from mysite.core.src.save_pylint_score import pylint_result
#import argparse
#parser = argparse.ArgumentParser(
#         description='submit python file',
#         epilog="good luck")
#parser.add_argument("signature", help="identify the signature")
#parser.add_argument("filename", help="input valid python filename or filepath")                   
#args = parser.parse_args()         

def test_Assignment(signature,file_name,score):
    
    try:
        input_output_file_name = TABLE[signature] + '.dat'
        path_to_input_output_file = os.path.join('/home/pallabeedey/Xtras/profile-model/media/data_sol', input_output_file_name)
        path_to_text_file = os.path.join('data', TABLE[signature])
        if os.path.isfile(path_to_input_output_file) == True:
            reading_input_output_file = open(path_to_input_output_file, 'r').read()    
        else:
            loading_text_file = open(path_to_input_output_file, 'w')
            loading_text_file.write(str(load(path_to_text_file)))
            loading_text_file.close
            reading_input_output_file = open(path_to_input_output_file, 'r').read()
    except KeyError:
        return 'There is no such signature %r' % signature
    try:
        output_values = eval(reading_input_output_file.strip())  
    except SyntaxError:
        output_values = load(path_to_text_file) 
#    print output_values    
    passed=0
    failed=0
    path_to_submitted_file, submitted_module_name = os.path.split(file_name)
    sys.path.insert(0, path_to_submitted_file)
    class_name=submitted_module_name.strip('.py')
    function_name=signature.split(".")
    imported_module=__import__(class_name)  
#    print imported_module
    clas = getattr(imported_module,function_name[0])
#    print clas
    instance_calling=clas()
    function_calling=getattr(instance_calling,function_name[1])
#    print function_calling
    cases=len(output_values["inp"])
    for value in range(0,cases):
        INP=output_values["inp"][value]
        attributes=len(INP)
        if attributes==1:
            answer_submitted = function_calling(INP[0])
        elif attributes==2:    
            answer_submitted = function_calling(INP[0],INP[1])
        elif attributes==3:    
            answer_submitted = function_calling(INP[0],INP[1],INP[2])
        elif attributes==4:
            answer_submitted = function_calling(INP[0],INP[1],INP[2],INP[3])
        else:
            answer_submitted = function_calling(INP[0],INP[1],INP[2],INP[3],INP[4])    
        OUT=output_values["out"][value]
        exact_value = eval(OUT)    
        try: 
            assert answer_submitted==exact_value
            passed=passed+1
        except:
            assert answer_submitted!=exact_value
            failed=failed+1
#    print attributes       
#    score=pylint_result(file_name)        
    return {'total' : cases, 'pass' : passed, 'fail' : failed, 'pylint_score' : score }
