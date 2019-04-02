# -*- coding: utf-8 -*-
"""
Created on Thursday 14th February 2019
@author: Ashish Chouhan
Description:
    RToS Implementation without LDA but all Algorithm Covered
    (Micro Service Architecture)
"""
# Import Libraries required for Processing
import sys
import pandas as pd
import numpy as np
import nltk
import re
from collections import Counter

# NLP Processing Library
# Tokenization
from nltk.tokenize import word_tokenize, sent_tokenize
# Stop Words    
from nltk.corpus import stopwords
# Word Net
from nltk.corpus import wordnet
# Importing Gensim
from gensim import corpora

# Evaluation Library Import
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances

# Database Related Library
import MySQLdb

# Table Display Library
from prettytable import PrettyTable

# Filter Methods Library
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler, Imputer




