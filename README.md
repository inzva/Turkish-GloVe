# TurkishGloVe
Türkçe GloVe - Repository for Turkish GloVe Word Embeddings

## Training

We used official GloVe repository both to create word embeddings and evaluation.
<a href="https://github.com/stanfordnlp/GloVe">GloVe Github Repository</a>

## Download pre-trained word vectors

1. 570K Vocab, cased, 300d vectors, 1.6 GB Text, 2.6 GB Binary <a href="https://drive.google.com/drive/u/0/folders/1RYsIYKdHWDN5vbu1-JNJmIv9K33dTQdG">link</a>

2. 253K Vocab, uncased, 300d vectors, 720 MB Text 1.2 GB Binary <a href="https://drive.google.com/drive/folders/1q_zE2cvCf_eWDtBSrx6XJFrH3xKofbQX">link</a>:

## Corpus
Corpus collected from January-December 2018 Commoncrawl.
This corpus has 2,736B tokens.
Corpus size: 5.4GB
<a href="https://data.statmt.org/cc-100/">Corpus Link</a> \
<a href="https://arxiv.org/pdf/1911.02116.pdf">Paper Link</a>

## Intrinsic Evaluation
This benchmark dataset is used for intrinsic evaluation on analogy task.
We used synonyms, capitals, and antonyms for analogy task. 
<a href="https://figshare.com/articles/dataset/Turkish_Word_embedding_benchmark_seed_dataset/10026818">Benchmark Dataset Link</a>

### Results

| Semantic Evaluation |   Antonyms Analogy Task   | Capitals Analogy Task | Synonyms Analogy Task |   Total Accuracy   |
|:-------------------:|:-------------------------:|:---------------------:|:---------------------:|:------------------:|
|  GloVe Uncased      |          21.70            |        47.74          |		     19.48          |        27.88       |



## Extrinsic Evaluation
This dataset is used for extrinsic evaluation on text categorization.
The dataset has 7 different classes. 

### Accuracy

|                  |    SVC    | Logistic Regression | 
|:----------------:|:---------:|:-------------------:|
|  GloVe Cased     |  0.89306  |	  0.89959 	       |  
|  GloVe Uncased   |  0.89956  |		0.90530          |


### Precision

|                 |    SVC    | Logistic Regression | 
|:---------------:|:---------:|:-------------------:|  
|  GloVe Cased    |  0.89388  |		  0.89864  	      |  
|  GloVe Uncased  |  0.90015  |			0.90619		      |

### Recall

|                 |    SVC    | Logistic Regression | 
|:---------------:|:---------:|:-------------------:| 
|  GloVe Cased    |  0.89306  |		  0.89796 	      |  
|  GloVe Uncased  |  0.89959  |			0.90531	        |


We used the given machine learning techniques with default hyperparameters in scikit-learn.

<a href="https://www.kaggle.com/savasy/ttc4900">Text Categorization Dataset Link</a>

## Examples

```
model.most_similar(positive=['fransa', 'berlin'], negative=['almanya'])
```
![city](/image/city.png)

```
model.most_similar(positive=['geliyor', 'gitmek'], negative=['gelmek'])
```
![verb](/image/verb.png)

```
model.most_similar("kedi")
```
![animal](/image/animal.png)


## References
https://cs224d.stanford.edu/lecture_notes/notes2.pdf \
https://nlp.stanford.edu/pubs/glove.pdf

