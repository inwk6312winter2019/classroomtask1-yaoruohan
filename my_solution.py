import os
def traverse_1st(dict):
     res = []
     for files in os.listdir(dict):
       res.append(files)
          print(res)
    
