# Cornac examples directory

## Basic usage

[first_example.py](first_example.py) - Your very first example with Cornac.

[pmf_ratio.py](pmf_ratio.py) - Splitting data into train/val/test sets based on provided sizes (RatioSplit).

[given_data.py](given_data.py) - Evaluate the models with your own data splits.

[vbpr_tradesy.py](vbpr_tradesy.py) - Image features associate with items/users.

[c2pf_example.py](c2pf_example.py) - Items/users networks as graph modules.

[conv_mf_example.py](conv_mf_example.py) - Text data associate with items/users.

[param_search.py](param_search.py) - Hyper-parameter tuning with GridSearch and RandomSearch.

----

## Multimodal Algorithms (Using Auxiliary Data)

### Graph

[c2pf_example.py](c2pf_example.py) - Collaborative Context Poisson Factorization (C2PF) with Amazon Office dataset.

[mcf_office.py](mcf_office.py) - Fit Matrix Co-Factorization (MCF) to the Amazon Office dataset.

[pcrl_example.py](pcrl_example.py) - Probabilistic Collaborative Representation Learning (PCRL) Amazon Office dataset.

[sbpr_epinions.py](sbpr_epinions.py) - Social Bayesian Personalized Ranking (SBPR) with Epinions dataset.

[sorec_filmtrust.py](sorec_filmtrust.py) - Social Recommendation using PMF (Sorec) with FilmTrust dataset.

### Text

[cdl_example.py](cdl_example.py) - Collaborative Deep Learning (CDL) with CiteULike dataset.

[cdr_example.py](cdr_example.py) - Collaborative Deep Ranking (CDR) with CiteULike dataset.

[conv_mf_example.py](conv_mf_example.py) - Convolutional Matrix Factorization (ConvMF) with MovieLens dataset.

[ctr_example_citeulike.py](ctr_example_citeulike.py) - Collaborative Topic Modelling (CTR) with CiteULike dataset.

[cvae_example.py](cvae_example.py) - Collaborative Variational Autoencoder (CVAE) with CiteULike dataset.

[efm_example.py](efm_example.py) - Explicit Factor Model (EFM) with Amazon Toy and Games dataset.

[hft_example.py](hft_example.py) - Hidden Factor Topic (HFT) with MovieLen 1m dataset.

### Image

[vbpr_tradesy.py](vbpr_tradesy.py) - Visual Bayesian Personalized Ranking (VBPR) with Tradesy dataset.

[vmf_clothing.py](vmf_clothing.py) - Visual Matrix Factorization (VMF) with Amazon Clothing dataset.

## Unimodal Algorithms

[biased_mf.py](biased_mf.py) - Matrix Factorization (MF) with biases.

[bpr_netflix.py](bpr_netflix.py) - Example to run Bayesian Personalized Ranking (BPR) with Netflix dataset.

[ibpr_example.py](ibpr_example.py) - Example to run Indexable Bayesian Personalized Ranking.

[ncf_example.py](ncf_example.py) - Neural Collaborative Filtering (GMF, MLP, NeuMF) with Amazon Clothing dataset.

[nmf_example.py](nmf_example.py) - Non-negative Matrix Factorization (NMF) with RatioSplit.

[pmf_ratio.py](pmf_ratio.py) - Probabilistic Matrix Factorization (PMF) with RatioSplit.

[svd_example.py](svd_example.py) - Singular Value Decomposition (SVD) with MovieLens dataset.

[vaecf_citeulike.py](vaecf_citeulike.py) - Variational Autoencoder for Collaborative Filtering (VAECF) with CiteULike dataset.

[wmf_example.py](wmf_example.py) - Weighted Matrix Factorization with CiteULike dataset.
