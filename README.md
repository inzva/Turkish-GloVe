# TurkishGloVe
Türkçe GloVe - Repository for Turkish GloVe Word Embeddings

## Training

We used official GloVe repository both to create word embeddings and evaluation.
<a href="https://github.com/stanfordnlp/GloVe">GloVe Github Repository</a>

## Download pre-trained word vectors

1. 570K Vocab, cased, 300d vectors, 1.6 GB Text, 2.6 GB Binary link: 

2. 253K Vocab, uncased, 300d vectors, 800 MB Text 1.3 GB Binary link:

## Corpus
Corpus collected from January-December 2018 Commoncrawl.
This corpus has 2,736M tokens.
Corpus size: 21GB
<a href="http://data.statmt.org/cc-100/tr.txt.xz">Corpus Link</a>

### Paper
<a href="https://arxiv.org/pdf/1911.02116.pdf">Paper Link</a>

## Intrinsic Evaluation
This benchmark dataset is used for intrinsic evaluation on analogy task.
We used synonyms, capitals, and antonyms for analogy task. 

<a href="https://figshare.com/articles/dataset/Turkish_Word_embedding_benchmark_seed_dataset/10026818">Benchmark Dataset Link</a>


## Extrinsic Evaluation
This dataset is used for extrinsic evaluation on text categorization.
The dataset has 7 different classes. 

### Accuracy

|  Word Embedding  | Naive Bayes | Logistic Regression | 
|:-----------------|:-----------:|:-------------------:|
|  GloVe Cased     |     		|					  |  
|  GloVe Uncased   |     		|					  |


### Precision

|  Word Embedding | Naive Bayes | Logistic Regression | 
|:----------------|:-----------:|:-------------------:|  
|  GloVe Cased    |     		|					  |  
|  GloVe Uncased  |     		|					  |

### Recall

|  Word Embedding | Naive Bayes | Logistic Regression | 
|:----------------|:-----------:|:-------------------:| 
|  GloVe Cased    |     		|					  |  
|  GloVe Uncased  |     		|					  |


We used the given machine learning techniques with default hyperparameters in scikit-learn.!

<a href="https://www.kaggle.com/savasy/ttc4900">Text Categorization Dataset Link</a>

## Examples

```
model.most_similar(positive=['fransa', 'berlin'], negative=['almanya'])
```


```
model.most_similar(positive=['geliyor', 'gitmek'], negative=['gelmek'])
```



```
model.most_similar("kedi")
```



## References
https://cs224d.stanford.edu/lecture_notes/notes2.pdf
https://nlp.stanford.edu/pubs/glove.pdf

