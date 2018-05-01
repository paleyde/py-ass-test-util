import os

def pylint_result(submitted_file):

    pylint_file_path="/home/pallabeedey/py-ass/r/output2.txt"
    pylint_output = 'pylint ' + submitted_file + '>' + pylint_file_path
    os.system(pylint_output)
    fp_pylint = open(pylint_file_path, 'r')
    pylint_out = fp_pylint.read()
    pylint_out = pylint_out.split('Your code has been rated at ')
    updated_pylint_out=str(pylint_out[1])
    os.remove(pylint_file_path)
    return updated_pylint_out
    
    
   
