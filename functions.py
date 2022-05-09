# -*- coding: utf-8 -*-
"""
Created on Mon May  9 12:26:19 2022

@author: julio
"""
import nltk

#Stop Words do NLTK
stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
stopwordsnltk.append('vou')
stopwordsnltk.append('tão')

#Remoção das Stop Words das frases
def removestopwords(texto):
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        frases.append((semstop, emocao))
    return frases

#Remoção das Stop Words e extração dos radicais
def aplicastemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasesstemming = []
    for (palavras, emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasesstemming.append((comstemming, emocao))
    return frasesstemming

#Lista as palavras da base de dados
def buscapalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras

#Frequencia das palavras
def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

#Lista das palavras únicas
def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq

#Extração das palavras de cada frase
def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in documento:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas
