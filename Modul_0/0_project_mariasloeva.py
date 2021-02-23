#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Searching the random number with minimum iteration

import numpy as np
count = 0
number = np.random.randint(1,101)      # Guessing the number 
print ("Загадано число от 1 до 100")  
 

def game_core(number):                 # Function for searching the random number
    count = 1
    left = 1
    right = 100
    predict = np.random.randint(1,101)
    
    while predict != number:
        count+=1

        if number > predict: 
            left=predict+1
            
        else:
            right=predict-1
        predict=(left+right)//2
            
    return(count) 

print (f"Вы угадали число {number} за {game_core(number)} попыток")  
        
        
def score_game(game_core):              # Function for counting the mean number of interactions
    count_ls = []
    np.random.seed(1)  
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(game_core)


# In[ ]:




