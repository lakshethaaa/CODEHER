import pandas as pd
import numpy as np
import sys
import re

def createVector(diseases,diets,nutrients):

    # 1) createVector is used to create the binary vector for a user input
    
    #   These are the possible diseases , diets and nutrients that a user can input
    diseases=['kidney_disease','pregnancy','hypertension','anemia','scurvy','cancer','rickets','goitre',
            'obesity','diabetes','heart_disease','eye_disease']
    diets=['ketogenic_diet','dash_diet','type_a_diet','omni_diet','high_protein_diet','low_sodium_diet','vegan_diet',
        'high_fiber_diet','low_fat_diet','low_carb_diet','alkaline_diet','gluten_free_diet','Mediterranean_diet','paleo_diet','type_o_diet']
    nutrients=['vitamin_c','iron','phosphorus','vitamin_d','calcium','sodium','fiber','chloride','vitamin_a','magnesium',
            'protein','vitamin_e','selenium','carbohydrates','potassium','manganese','iodine']
    
    # Node js passes the list of strings as arguement to py file which can be acessed by sys.argv
    # ip=sys.argv[1:]

    # Initially the vector is empty, 44: is the sum of (possible number of diseases+diets+nutrients)
    v=[0]*44
    i=0
    
    # Adding 1's in the vector corresponding to their position
    while(i<len(diseases)):
        if(diseases[i] in diseases):
            v[i]=1
        i+=1
    j=0
    while(j<len(diets)):
        if(diets[j] in diets):
            v[i]=1
        i+=1
        j+=1
    j=0
    while(j<len(nutrients)):
        if(nutrients[j] in nutrients):
            v[i]=1
        i+=1
        j+=1
    return v

def process(diseases,diets,nutrients):

    # Process is used to compare similarity between each meal id and user input, and find most similar meals
    v=createVector(diseases,diets,nutrients)
    # Now v holds the input vector
    #Read the csv file - transformed one
    df=pd.read_csv(r".\Vector.csv")
    values=df.iloc[:,2:].values
    ids=df.iloc[:,0].values
    sums=[]
    
    # Compute similarity for each meal id and user input
    # similarity= sum of absolute (V_i - Input_i) , where i goes from 0 to 44
    # if less sum , more coincides so more similarity
    for i in range(values.shape[0]):
        s=0
        arr=values[i]
        for j in range(len(v)):
            s+=abs(arr[j]-v[j])
        sums.append([ids[i],s])
    sums.sort(key=lambda sums: sums[1])
    final=[x[0] for x in sums]

    return " ".join(final[:10])
