{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "icmc-4.py",
      "provenance": [],
      "authorship_tag": "ABX9TyOZc0yiK7tNCQ0gybbElSV8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LauraSteinert/PNL/blob/main/first-try.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JXRsfFNes8r2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3fbc2c29-68c6-45e5-9faf-9d6adea591f5"
      },
      "source": [
        "# Aula 4 - PLN #\n",
        "\n",
        "## Strings ##\n",
        "r = 'roney'\n",
        "nr = 'l' + r[1:]\n",
        "print(nr)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "loney\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "vlhM0fsY1mp_",
        "outputId": "39cea018-96d0-4edb-ebc5-6731ebec42e4"
      },
      "source": [
        "nr = nr + ' santos'\n",
        "nr"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'loney santos'"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VZRdSXU9gQ3g",
        "outputId": "57cad33a-5847-4cf6-f15c-7d513e4ee01c"
      },
      "source": [
        "# Modo de instalação fora do Codelab #\n",
        "!pip install nltk"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: nltk in /usr/local/lib/python3.7/dist-packages (3.2.5)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.7/dist-packages (from nltk) (1.15.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "30sFlIyMiIcf"
      },
      "source": [
        "import nltk"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZR_7v2poiVCH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9f2c88fe-c097-4569-d677-cf933c36be7d"
      },
      "source": [
        "nltk.download()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "NLTK Downloader\n",
            "---------------------------------------------------------------------------\n",
            "    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit\n",
            "---------------------------------------------------------------------------\n",
            "Downloader> d\n",
            "\n",
            "Download which package (l=list; x=cancel)?\n",
            "  Identifier> all\n",
            "    Downloading collection 'all'\n",
            "       | \n",
            "       | Downloading package abc to /root/nltk_data...\n",
            "       |   Unzipping corpora/abc.zip.\n",
            "       | Downloading package alpino to /root/nltk_data...\n",
            "       |   Unzipping corpora/alpino.zip.\n",
            "       | Downloading package biocreative_ppi to /root/nltk_data...\n",
            "       |   Unzipping corpora/biocreative_ppi.zip.\n",
            "       | Downloading package brown to /root/nltk_data...\n",
            "       |   Unzipping corpora/brown.zip.\n",
            "       | Downloading package brown_tei to /root/nltk_data...\n",
            "       |   Unzipping corpora/brown_tei.zip.\n",
            "       | Downloading package cess_cat to /root/nltk_data...\n",
            "       |   Unzipping corpora/cess_cat.zip.\n",
            "       | Downloading package cess_esp to /root/nltk_data...\n",
            "       |   Unzipping corpora/cess_esp.zip.\n",
            "       | Downloading package chat80 to /root/nltk_data...\n",
            "       |   Unzipping corpora/chat80.zip.\n",
            "       | Downloading package city_database to /root/nltk_data...\n",
            "       |   Unzipping corpora/city_database.zip.\n",
            "       | Downloading package cmudict to /root/nltk_data...\n",
            "       |   Unzipping corpora/cmudict.zip.\n",
            "       | Downloading package comparative_sentences to\n",
            "       |     /root/nltk_data...\n",
            "       |   Unzipping corpora/comparative_sentences.zip.\n",
            "       | Downloading package comtrans to /root/nltk_data...\n",
            "       | Downloading package conll2000 to /root/nltk_data...\n",
            "       |   Unzipping corpora/conll2000.zip.\n",
            "       | Downloading package conll2002 to /root/nltk_data...\n",
            "       |   Unzipping corpora/conll2002.zip.\n",
            "       | Downloading package conll2007 to /root/nltk_data...\n",
            "       | Downloading package crubadan to /root/nltk_data...\n",
            "       |   Unzipping corpora/crubadan.zip.\n",
            "       | Downloading package dependency_treebank to /root/nltk_data...\n",
            "       |   Unzipping corpora/dependency_treebank.zip.\n",
            "       | Downloading package dolch to /root/nltk_data...\n",
            "       |   Unzipping corpora/dolch.zip.\n",
            "       | Downloading package europarl_raw to /root/nltk_data...\n",
            "       |   Unzipping corpora/europarl_raw.zip.\n",
            "       | Downloading package floresta to /root/nltk_data...\n",
            "       |   Unzipping corpora/floresta.zip.\n",
            "       | Downloading package framenet_v15 to /root/nltk_data...\n",
            "       |   Unzipping corpora/framenet_v15.zip.\n",
            "       | Downloading package framenet_v17 to /root/nltk_data...\n",
            "       |   Unzipping corpora/framenet_v17.zip.\n",
            "       | Downloading package gazetteers to /root/nltk_data...\n",
            "       |   Unzipping corpora/gazetteers.zip.\n",
            "       | Downloading package genesis to /root/nltk_data...\n",
            "       |   Unzipping corpora/genesis.zip.\n",
            "       | Downloading package gutenberg to /root/nltk_data...\n",
            "       |   Unzipping corpora/gutenberg.zip.\n",
            "       | Downloading package ieer to /root/nltk_data...\n",
            "       |   Unzipping corpora/ieer.zip.\n",
            "       | Downloading package inaugural to /root/nltk_data...\n",
            "       |   Unzipping corpora/inaugural.zip.\n",
            "       | Downloading package indian to /root/nltk_data...\n",
            "       |   Unzipping corpora/indian.zip.\n",
            "       | Downloading package jeita to /root/nltk_data...\n",
            "       | Downloading package kimmo to /root/nltk_data...\n",
            "       |   Unzipping corpora/kimmo.zip.\n",
            "       | Downloading package knbc to /root/nltk_data...\n",
            "       | Downloading package lin_thesaurus to /root/nltk_data...\n",
            "       |   Unzipping corpora/lin_thesaurus.zip.\n",
            "       | Downloading package mac_morpho to /root/nltk_data...\n",
            "       |   Unzipping corpora/mac_morpho.zip.\n",
            "       | Downloading package machado to /root/nltk_data...\n",
            "       | Downloading package masc_tagged to /root/nltk_data...\n",
            "       | Downloading package moses_sample to /root/nltk_data...\n",
            "       |   Unzipping models/moses_sample.zip.\n",
            "       | Downloading package movie_reviews to /root/nltk_data...\n",
            "       |   Unzipping corpora/movie_reviews.zip.\n",
            "       | Downloading package names to /root/nltk_data...\n",
            "       |   Unzipping corpora/names.zip.\n",
            "       | Downloading package nombank.1.0 to /root/nltk_data...\n",
            "       | Downloading package nps_chat to /root/nltk_data...\n",
            "       |   Unzipping corpora/nps_chat.zip.\n",
            "       | Downloading package omw to /root/nltk_data...\n",
            "       |   Unzipping corpora/omw.zip.\n",
            "       | Downloading package opinion_lexicon to /root/nltk_data...\n",
            "       |   Unzipping corpora/opinion_lexicon.zip.\n",
            "       | Downloading package paradigms to /root/nltk_data...\n",
            "       |   Unzipping corpora/paradigms.zip.\n",
            "       | Downloading package pil to /root/nltk_data...\n",
            "       |   Unzipping corpora/pil.zip.\n",
            "       | Downloading package pl196x to /root/nltk_data...\n",
            "       |   Unzipping corpora/pl196x.zip.\n",
            "       | Downloading package ppattach to /root/nltk_data...\n",
            "       |   Unzipping corpora/ppattach.zip.\n",
            "       | Downloading package problem_reports to /root/nltk_data...\n",
            "       |   Unzipping corpora/problem_reports.zip.\n",
            "       | Downloading package propbank to /root/nltk_data...\n",
            "       | Downloading package ptb to /root/nltk_data...\n",
            "       |   Unzipping corpora/ptb.zip.\n",
            "       | Downloading package product_reviews_1 to /root/nltk_data...\n",
            "       |   Unzipping corpora/product_reviews_1.zip.\n",
            "       | Downloading package product_reviews_2 to /root/nltk_data...\n",
            "       |   Unzipping corpora/product_reviews_2.zip.\n",
            "       | Downloading package pros_cons to /root/nltk_data...\n",
            "       |   Unzipping corpora/pros_cons.zip.\n",
            "       | Downloading package qc to /root/nltk_data...\n",
            "       |   Unzipping corpora/qc.zip.\n",
            "       | Downloading package reuters to /root/nltk_data...\n",
            "       | Downloading package rte to /root/nltk_data...\n",
            "       |   Unzipping corpora/rte.zip.\n",
            "       | Downloading package semcor to /root/nltk_data...\n",
            "       | Downloading package senseval to /root/nltk_data...\n",
            "       |   Unzipping corpora/senseval.zip.\n",
            "       | Downloading package sentiwordnet to /root/nltk_data...\n",
            "       |   Unzipping corpora/sentiwordnet.zip.\n",
            "       | Downloading package sentence_polarity to /root/nltk_data...\n",
            "       |   Unzipping corpora/sentence_polarity.zip.\n",
            "       | Downloading package shakespeare to /root/nltk_data...\n",
            "       |   Unzipping corpora/shakespeare.zip.\n",
            "       | Downloading package sinica_treebank to /root/nltk_data...\n",
            "       |   Unzipping corpora/sinica_treebank.zip.\n",
            "       | Downloading package smultron to /root/nltk_data...\n",
            "       |   Unzipping corpora/smultron.zip.\n",
            "       | Downloading package state_union to /root/nltk_data...\n",
            "       |   Unzipping corpora/state_union.zip.\n",
            "       | Downloading package stopwords to /root/nltk_data...\n",
            "       |   Unzipping corpora/stopwords.zip.\n",
            "       | Downloading package subjectivity to /root/nltk_data...\n",
            "       |   Unzipping corpora/subjectivity.zip.\n",
            "       | Downloading package swadesh to /root/nltk_data...\n",
            "       |   Unzipping corpora/swadesh.zip.\n",
            "       | Downloading package switchboard to /root/nltk_data...\n",
            "       |   Unzipping corpora/switchboard.zip.\n",
            "       | Downloading package timit to /root/nltk_data...\n",
            "       |   Unzipping corpora/timit.zip.\n",
            "       | Downloading package toolbox to /root/nltk_data...\n",
            "       |   Unzipping corpora/toolbox.zip.\n",
            "       | Downloading package treebank to /root/nltk_data...\n",
            "       |   Unzipping corpora/treebank.zip.\n",
            "       | Downloading package twitter_samples to /root/nltk_data...\n",
            "       |   Unzipping corpora/twitter_samples.zip.\n",
            "       | Downloading package udhr to /root/nltk_data...\n",
            "       |   Unzipping corpora/udhr.zip.\n",
            "       | Downloading package udhr2 to /root/nltk_data...\n",
            "       |   Unzipping corpora/udhr2.zip.\n",
            "       | Downloading package unicode_samples to /root/nltk_data...\n",
            "       |   Unzipping corpora/unicode_samples.zip.\n",
            "       | Downloading package universal_treebanks_v20 to\n",
            "       |     /root/nltk_data...\n",
            "       | Downloading package verbnet to /root/nltk_data...\n",
            "       |   Unzipping corpora/verbnet.zip.\n",
            "       | Downloading package verbnet3 to /root/nltk_data...\n",
            "       |   Unzipping corpora/verbnet3.zip.\n",
            "       | Downloading package webtext to /root/nltk_data...\n",
            "       |   Unzipping corpora/webtext.zip.\n",
            "       | Downloading package wordnet to /root/nltk_data...\n",
            "       |   Unzipping corpora/wordnet.zip.\n",
            "       | Downloading package wordnet31 to /root/nltk_data...\n",
            "       |   Unzipping corpora/wordnet31.zip.\n",
            "       | Downloading package wordnet_ic to /root/nltk_data...\n",
            "       |   Unzipping corpora/wordnet_ic.zip.\n",
            "       | Downloading package words to /root/nltk_data...\n",
            "       |   Unzipping corpora/words.zip.\n",
            "       | Downloading package ycoe to /root/nltk_data...\n",
            "       |   Unzipping corpora/ycoe.zip.\n",
            "       | Downloading package rslp to /root/nltk_data...\n",
            "       |   Unzipping stemmers/rslp.zip.\n",
            "       | Downloading package maxent_treebank_pos_tagger to\n",
            "       |     /root/nltk_data...\n",
            "       |   Unzipping taggers/maxent_treebank_pos_tagger.zip.\n",
            "       | Downloading package universal_tagset to /root/nltk_data...\n",
            "       |   Unzipping taggers/universal_tagset.zip.\n",
            "       | Downloading package maxent_ne_chunker to /root/nltk_data...\n",
            "       |   Unzipping chunkers/maxent_ne_chunker.zip.\n",
            "       | Downloading package punkt to /root/nltk_data...\n",
            "       |   Unzipping tokenizers/punkt.zip.\n",
            "       | Downloading package book_grammars to /root/nltk_data...\n",
            "       |   Unzipping grammars/book_grammars.zip.\n",
            "       | Downloading package sample_grammars to /root/nltk_data...\n",
            "       |   Unzipping grammars/sample_grammars.zip.\n",
            "       | Downloading package spanish_grammars to /root/nltk_data...\n",
            "       |   Unzipping grammars/spanish_grammars.zip.\n",
            "       | Downloading package basque_grammars to /root/nltk_data...\n",
            "       |   Unzipping grammars/basque_grammars.zip.\n",
            "       | Downloading package large_grammars to /root/nltk_data...\n",
            "       |   Unzipping grammars/large_grammars.zip.\n",
            "       | Downloading package tagsets to /root/nltk_data...\n",
            "       |   Unzipping help/tagsets.zip.\n",
            "       | Downloading package snowball_data to /root/nltk_data...\n",
            "       | Downloading package bllip_wsj_no_aux to /root/nltk_data...\n",
            "       |   Unzipping models/bllip_wsj_no_aux.zip.\n",
            "       | Downloading package word2vec_sample to /root/nltk_data...\n",
            "       |   Unzipping models/word2vec_sample.zip.\n",
            "       | Downloading package panlex_swadesh to /root/nltk_data...\n",
            "       | Downloading package mte_teip5 to /root/nltk_data...\n",
            "       |   Unzipping corpora/mte_teip5.zip.\n",
            "       | Downloading package averaged_perceptron_tagger to\n",
            "       |     /root/nltk_data...\n",
            "       |   Unzipping taggers/averaged_perceptron_tagger.zip.\n",
            "       | Downloading package averaged_perceptron_tagger_ru to\n",
            "       |     /root/nltk_data...\n",
            "       |   Unzipping taggers/averaged_perceptron_tagger_ru.zip.\n",
            "       | Downloading package perluniprops to /root/nltk_data...\n",
            "       |   Unzipping misc/perluniprops.zip.\n",
            "       | Downloading package nonbreaking_prefixes to\n",
            "       |     /root/nltk_data...\n",
            "       |   Unzipping corpora/nonbreaking_prefixes.zip.\n",
            "       | Downloading package vader_lexicon to /root/nltk_data...\n",
            "       | Downloading package porter_test to /root/nltk_data...\n",
            "       |   Unzipping stemmers/porter_test.zip.\n",
            "       | Downloading package wmt15_eval to /root/nltk_data...\n",
            "       |   Unzipping models/wmt15_eval.zip.\n",
            "       | Downloading package mwa_ppdb to /root/nltk_data...\n",
            "       |   Unzipping misc/mwa_ppdb.zip.\n",
            "       | \n",
            "     Done downloading collection all\n",
            "\n",
            "---------------------------------------------------------------------------\n",
            "    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit\n",
            "---------------------------------------------------------------------------\n",
            "Downloader> q\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wq9RWt8ckO81",
        "outputId": "b269c3fc-19b2-45ed-9af9-132c93da2a25"
      },
      "source": [
        "len(nltk.corpus.mac_morpho.words())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1170095"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aQHTO5Wmk_GE",
        "outputId": "2cedacff-5be6-4a8a-9154-bccee977d467"
      },
      "source": [
        "nltk.corpus.mac_morpho.sents()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['Jersei', 'atinge', 'média', 'de', 'Cr$', '1,4', 'milhão', 'em', 'a', 'venda', 'de', 'a', 'Pinhal', 'em', 'São', 'Paulo'], ['Programe', 'sua', 'viagem', 'a', 'a', 'Exposição', 'Nacional', 'do', 'Zebu', ',', 'que', 'começa', 'dia', '25'], ...]"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uKOHpkCjsh0J",
        "outputId": "15b32682-68c5-4ec8-f8dd-e7fe28c63b38"
      },
      "source": [
        "texto = \"O jogador é um palerma, obviamente\"\n",
        "nltk.word_tokenize(texto)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['O', 'jogador', 'é', 'um', 'palerma', ',', 'obviamente']"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bi-8CmP9wGS-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "459f800a-6f5a-4bb1-9261-137948991d51"
      },
      "source": [
        "from nltk.tokenize import RegexpTokenizer\n",
        "texto = \"Running away is easy, 1s the living thaats haard\"\n",
        "tokenizer = RegexpTokenizer(r'\\w+')\n",
        "tokens = tokenizer.tokenize(texto)\n",
        "print(tokens)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Running', 'away', 'is', 'easy', '1s', 'the', 'living', 'thaats', 'haard']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sTl6F_jDVQFF",
        "outputId": "b814a6fe-60ff-4ad0-c8df-fcc99a732346"
      },
      "source": [
        "#Regex improved#\n",
        "tokenizer = RegexpTokenizer(r'[a-zA-Z]\\w+')\n",
        "tokens = tokenizer.tokenize(texto)\n",
        "print(tokens)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Running', 'away', 'is', 'easy', 'the', 'living', 'thaats', 'haard']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pfTzNdsAbQ0j",
        "outputId": "064238ec-d0cf-486c-8865-1383dfddb010"
      },
      "source": [
        "#Frequencia#\n",
        "frequencia = nltk.FreqDist(tokens)\n",
        "frequencia.most_common()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('Running', 1),\n",
              " ('away', 1),\n",
              " ('is', 1),\n",
              " ('easy', 1),\n",
              " ('the', 1),\n",
              " ('living', 1),\n",
              " ('thaats', 1),\n",
              " ('haard', 1)]"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H81qiLKnbp-b",
        "outputId": "6bd68ab3-808b-4059-8499-0cd81c9bd23d"
      },
      "source": [
        "#Tudo minusculo#\n",
        "nova_lista = []\n",
        "for token in tokens:\n",
        "  nova_lista.append(token.lower())\n",
        "frequencia = nltk.FreqDist(nova_lista)\n",
        "frequencia.most_common()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('running', 1),\n",
              " ('away', 1),\n",
              " ('is', 1),\n",
              " ('easy', 1),\n",
              " ('the', 1),\n",
              " ('living', 1),\n",
              " ('thaats', 1),\n",
              " ('haard', 1)]"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IBl1UyhZAljE"
      },
      "source": [
        "#Stopwords#\n",
        "\n",
        "stopwords = ntlk.corpus.stopwords.words('portuguese')\n",
        "\n",
        "#tokeniza dnv#\n",
        "\n",
        "lista = []\n",
        "\n",
        "for token in tokens:\n",
        "  if token.lower() not in stopwords:\n",
        "    lista.append(token.lower())\n",
        "\n",
        "#calculo de frequencia dnv#"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tZ9crzS8DEjm",
        "outputId": "d3582260-1f06-421d-f6d1-9ec2860406d6"
      },
      "source": [
        "# N - gramas # \n",
        "texto = nltk.corpus.mac_morpho.sents()\n",
        "stopwords = nltk.corpus.stopwords.words('portuguese')\n",
        "from nltk.tokenize import RegexpTokenizer\n",
        "tokenizer = RegexpTokenizer(r'[a-zA-z]\\w+')\n",
        "tokens = tokenizer.tokenize(str(texto))\n",
        "lista = []\n",
        "for token in tokens:\n",
        "  if token.lower() not in stopwords:\n",
        "    lista.append(token.lower())\n",
        "print(lista)\n",
        "frequencia = nltk.FreqDist(lista)\n",
        "# N - gramas #\n",
        "from nltk import bigrams\n",
        "from nltk import trigrams\n",
        "from nltk import ngrams\n",
        "\n",
        "lista_bigrams = list(bigrams(lista))\n",
        "\n",
        "lista_bigrams"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['jersei', 'atinge', 'média', 'cr', 'milhão', 'venda', 'pinhal', 'paulo', 'programe', 'viagem', 'exposição', 'nacional', 'zebu', 'começa', 'dia']\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('jersei', 'atinge'),\n",
              " ('atinge', 'média'),\n",
              " ('média', 'cr'),\n",
              " ('cr', 'milhão'),\n",
              " ('milhão', 'venda'),\n",
              " ('venda', 'pinhal'),\n",
              " ('pinhal', 'paulo'),\n",
              " ('paulo', 'programe'),\n",
              " ('programe', 'viagem'),\n",
              " ('viagem', 'exposição'),\n",
              " ('exposição', 'nacional'),\n",
              " ('nacional', 'zebu'),\n",
              " ('zebu', 'começa'),\n",
              " ('começa', 'dia')]"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dQ_AdK4_GbHy",
        "outputId": "5d356f9a-a648-42ab-a37f-c790557691e0"
      },
      "source": [
        "# Trigramas #\n",
        "lista_trigrams = list(trigrams(lista))\n",
        "\n",
        "lista_trigrams"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('jersei', 'atinge', 'média'),\n",
              " ('atinge', 'média', 'cr'),\n",
              " ('média', 'cr', 'milhão'),\n",
              " ('cr', 'milhão', 'venda'),\n",
              " ('milhão', 'venda', 'pinhal'),\n",
              " ('venda', 'pinhal', 'paulo'),\n",
              " ('pinhal', 'paulo', 'programe'),\n",
              " ('paulo', 'programe', 'viagem'),\n",
              " ('programe', 'viagem', 'exposição'),\n",
              " ('viagem', 'exposição', 'nacional'),\n",
              " ('exposição', 'nacional', 'zebu'),\n",
              " ('nacional', 'zebu', 'começa'),\n",
              " ('zebu', 'começa', 'dia')]"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WPVKNDZqGglo",
        "outputId": "ad85dc01-2ab1-4ce5-e1f4-5857f9a70857"
      },
      "source": [
        "# N - gramas #\n",
        "lista_ngrams = list(ngrams(lista, 4))\n",
        "\n",
        "lista_ngrams"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('jersei', 'atinge', 'média', 'cr'),\n",
              " ('atinge', 'média', 'cr', 'milhão'),\n",
              " ('média', 'cr', 'milhão', 'venda'),\n",
              " ('cr', 'milhão', 'venda', 'pinhal'),\n",
              " ('milhão', 'venda', 'pinhal', 'paulo'),\n",
              " ('venda', 'pinhal', 'paulo', 'programe'),\n",
              " ('pinhal', 'paulo', 'programe', 'viagem'),\n",
              " ('paulo', 'programe', 'viagem', 'exposição'),\n",
              " ('programe', 'viagem', 'exposição', 'nacional'),\n",
              " ('viagem', 'exposição', 'nacional', 'zebu'),\n",
              " ('exposição', 'nacional', 'zebu', 'começa'),\n",
              " ('nacional', 'zebu', 'começa', 'dia')]"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Q0QrdfMoluva",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "757b7f74-6f67-47c1-bbcb-463dc7fb103b"
      },
      "source": [
        "for bigrama in lista_bigrams:\n",
        "  print(bigrama[0][0])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "j\n",
            "a\n",
            "m\n",
            "c\n",
            "m\n",
            "v\n",
            "p\n",
            "p\n",
            "p\n",
            "v\n",
            "e\n",
            "n\n",
            "z\n",
            "c\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8uEIVXYvldZL",
        "outputId": "2d4d493d-8b15-4464-8f4d-16da719eda3f"
      },
      "source": [
        "# Stemming e Lematização #\n",
        "\n",
        "stemmer = nltk.RSLPStemmer()\n",
        "\n",
        "print(stemmer.stem(\"amigão\"))\n",
        "print(stemmer.stem(\"amigos\"))\n",
        "print(stemmer.stem(\"amigo\"))\n",
        "print(stemmer.stem(\"propõem\"))\n",
        "print(stemmer.stem(\"propuseram\"))\n",
        "print(stemmer.stem(\"propondo\"))\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "amig\n",
            "amig\n",
            "amig\n",
            "propõ\n",
            "propus\n",
            "prop\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 231
        },
        "id": "W9MGJhwznNbo",
        "outputId": "cf7c0785-e63d-4cf8-aa4d-dc0b5712449a"
      },
      "source": [
        "# Etiquetador #\n",
        "from nltk.corpus  import mac_morpho\n",
        "from nltk.tag import UnigramTagger\n",
        "\n",
        "\n",
        "tokens = nltk.word_tokenize(corpus)\n",
        "\n",
        "treinadoras_natacao = mac_morpho.tagged_sents()\n",
        "etiquetador = UnigramTagger(treinadoras_natacao)\n",
        "\n",
        "etiquetado = etiquetador.tag(tokens)\n",
        "\n",
        "print(etiquetado)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-20-80fe7c44be05>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mtokens\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mword_tokenize\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcorpus\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0mtreinadoras_natacao\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmac_morpho\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtagged_sents\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'corpus' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F6elSi_PpWXl"
      },
      "source": [
        "from nltk.corpus  import mac_morpho\n",
        "from nltk.tag import UnigramTagger\n",
        "from nltk.tag import DefaultTagger\n",
        "\n",
        "tokens = nltk.word_tokenize(corpus)\n",
        "\n",
        "etiq_padrao = DefaultTagger('N')\n",
        "treinadoras_natacao = mac_morpho.tagged_sents()\n",
        "etiquetador = UnigramTagger(treinadoras_natacao, backoff=etiq_padrao)\n",
        "\n",
        "etiquetado = etiquetador.tag(tokens)\n",
        "\n",
        "print(etiquetado)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VT4uBZlAqlIo"
      },
      "source": [
        "# Chunking #\n",
        "\n",
        "from nltk.chunk import RegexpParser\n",
        "\n",
        "pattern = 'NP: {<NPROP><NPROP> | <N><N>}'\n",
        "analise_gramatical = RegexpParser(pattern)\n",
        "arvore =  analise_gramatical.parse(etiquetador)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}