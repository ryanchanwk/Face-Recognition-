# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:14:15 2020

@author: saructk
"""
import pandas as pd

import os



def entry_system (csv_file):  
    
    df = pd.read_csv(csv_file, encoding="utf_8_sig")    
    df = df.sort_values(by = "name_id")
   
    return df
     
        
def add_entry(df, name, path):          
   
    if  name != '' and path != '':
        if (name not in df['name'].values) and (path not in df['path'].values): 
            name_id = "S" + str(int(df['name_id'].iloc[-1][1:])+1)
            print('\n Please confirm the input.\n')
            print('name_id: ', name_id)
            print('name: ', name)
            print('path: ', path)
            choice = input('Please input "1" to confirm entry: ')
            
            if choice == '1':
                to_append = [name_id, name, path]
                a_series = pd.Series(to_append, index = df.columns)                
                df = df.append(a_series, ignore_index=True)
                print('Input completed!')
            
            else:
                print('Input failed!')            
                            
        else:          
            print('\nDuplication! Please check.\n')
      
    else:
        print("\nNo data input.\n")
    
    return df
        

if __name__ == '__main__':
    
    path = './'

    csv_file = os.path.join(path, "name_list.csv")  
    
    print('Welcome to add entry system.\nBelow is last 10 data.\n')
    
    df = entry_system(csv_file)
    
    print(df.tail(10))
    
    on_system = True
    
    while on_system == True:
        
        leave_sys = input('Leave blank if continue to data input...: ')
        if leave_sys != '':
            on_system = False
            break
    
        name = input('Please input name: ')
        path = input('Please input path: ')
        
    
        df = add_entry(df,name,path)
        
        print("Data review (last 10)\n")
        print(df.tail(10))
        
    save_opt = input('Please input "1" to confirm save: ')
    
    if save_opt == '1':
        df.to_csv(csv_file, index = False, encoding="utf_8_sig")
        print('File save completed!') 
        
    else:
        print('File save failed!') 
    
    
    
    
    



    
    
    
    
    
    