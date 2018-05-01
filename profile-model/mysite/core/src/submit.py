from mysite.core.src.convert import load
from mysite.core.src.update import update
import os
from sys import argv
import argparse
#parser = argparse.ArgumentParser(
#         description='submit assignment file',
#         epilog="Thank you")
#parser.add_argument("signature", help="identify the signature")
#parser.add_argument("text_file", help="input valid text file or text filepath")                
#args = parser.parse_args()
#script,signature,text_file = argv

def add_assignment(signature,text_file):
    
    try:
        class_name=signature.split(".")[0]
        function_name=signature.split(".")[1]
        directory_to_data = os.path.dirname("/home/pallabeedey/Xtras/profile-model/media/data")
        if not os.path.exists("/home/pallabeedey/Xtras/profile-model/media/data") & os.path.exists("/home/pallabeedey/Xtras/profile-model/media/data_sol") :
            os.makedirs("/home/pallabeedey/Xtras/profile-model/media/data")
            os.makedirs("/home/pallabeedey/Xtras/profile-model/media/data_sol")
            submitted_file=open(text_file,"r")
            path_to_text_file="/home/pallabeedey/Xtras/profile-model/media/data/"+class_name+'.sol.txt'
            fp=open(path_to_text_file,"w")
            fp.write(submitted_file.read())
            fp.close()
            path_to_sol_file="/home/pallabeedey/Xtras/profile-model/media/data_sol/"+class_name+'.sol.txt.dat'
            loading = open(path_to_sol_file,"w")
            loading.write(str(load(path_to_text_file)))
            loading.close()
            text_file_name=class_name+'.sol.txt'
            update({signature:text_file_name})
            return "ASSIGNMENT ADDED SUCCESFULLY"
        else:        
            result_output=os.path.dirname("/home/pallabeedey/Xtras/profile-model/media/data/")
            submitted_file=open(text_file,"r")
            path_to_text_file="/home/pallabeedey/Xtras/profile-model/media/data/"+class_name+'.sol.txt'
            fp=open(path_to_text_file,"w")
            fp.write(submitted_file.read())
            fp.close()
            path_to_sol_file="/home/pallabeedey/Xtras/profile-model/media/data_sol/"+class_name+'.sol.txt.dat'
            loading = open(path_to_sol_file,"w")
            loading.write(str(load(path_to_text_file)))
            loading.close()
            text_file_name=class_name+'.sol.txt'
            update({signature:text_file_name})
            return "ASSIGNMENT ADDED SUCCESFULLY"
    except KeyError:
        return "NOT FUNCTIONING"

#if __name__=="__main__":
#    print add_assignment(signature,text_file)

