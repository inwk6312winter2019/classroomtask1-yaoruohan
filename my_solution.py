import os
def traverse_1st(dict):
     res = []
     for files in os.listdir(dict):
       res.append(files)
          l = res[::-1]
            print(l)
reverse_list(dict)
    
