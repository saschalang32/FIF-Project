#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:33:08 2019

@author: ashish
"""
from import_library import *

def cosine_similarity(reference_array, tfidf, number_of_values):
    distance_value = pairwise_distances(tfidf[-1], tfidf, metric = "cosine")
        
    matching_values = []
        
    for i in range(1, number_of_values + 1):
        index = distance_value.argsort()[0][i]
        matching_values.append(reference_array[index])
        
    if number_of_values == 1:
        return matching_values[0]
    else:
        return matching_values
