# Neuralist 
### A recurrent neural network (LSTM) based lyrical similarity analysis.

A siamese recurrent network (LSTM) architecture (Mueller & Thyagarajan 2016) implementation for analyzing pairwise lyrical similarity between songs of varying length. The model shows promising results in understanding semantic relationships between songs. When compared to bag of words based implementations, the neural network based model show significantly better results. Even with a small dataset the model is able to learn similarities across genres which opens up opportunities to generate recommendations that contrast with audio features as well as those that span languages.

![Neuralist Model](/paper/model.png)

## Training
The Million Song Dataset (MSD) is a freely available collection of audio features and metadata for a million contemporary popular music tracks until 2011. The companion to this is the **LastFM dataset** which we use as the ground truth for song similarities. LastFM dataset provides similarity information for 584,897 tracks. All together there are 56M paired track similarity information. Since training using 56M pairs will be a time-consuming endeavor, we narrow our focus to 4610 Billboard Top 100 songs between 1950-2011. Of these, there are 832 songs that are part of MSD. These songs result in 10k song pairs which we split to train and test set (80/20).

As we are interested in our model learning semantic representations of the songs, we make use of pre-computed wiki word embeddings. We configure the hyperparameters to as specified in the Mueller paper. The embedding dimension is set to 300, batch size is 64, dropout probability as 1 and number of hidden units as 50. For the first training run, we set the max document size to 15 to expedite training and to be able to run verification. For the final training run the max document size was set to 300 as most song’s lyrics were around that value.

![Accuracy](/paper/accuracy.png)
Training Accuracy (Yellow: 15words, Green: 300words)

![Loss](/paper/loss.png)
Training Loss (Yellow: 15words, Green: 300words)

## Evaluation
The 300 word document length model gives an evaluation accuracy of **96.2%** when evaluting based on 2 class (similar/dissimilar) outcome. The evaluation accuracy drops to 52.4% for 15 word document length model predicting 10 classes (similarity converted to decile bins) and 45.2% for 300 word document length model predicting 10 class outcome. This accuracy can be increased significantly by providing a larger training dataset.

## 2015 Billboard Top 100 songs
Finally we run the model against 2015 billboard top 100 songs and perform dimensionality reduction (PCA) to determine semantic similarities among them. As can be seen below, the model performs pretty well to discern semantic similarity within and across genre. Further the model was able to cluster similar songs which will be useful for recommendations.
![Top 100](/paper/top100.png)

## References
Mueller, Jonas, and Aditya Thyagarajan. 2016. Siamese Recurrent Architectures for Learning Sentence Similarity. AAAI (pp. 2786-2792)

Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. 2013. Distributed representations of words and phrases and their compositionality. Advances in neural information processing systems , (pp. 3111-3119).

Fell, Michael, and Caroline Sporleder. 2014. Lyrics based Analysis and Classification of Music.

Balakrishnan, Anusha, and Kalpit Dixit. 2016. Deep-Playlist: Using Recurrent Neural Networks to Predict Song Similarity.

Hochreiter, Sepp, and Jrgen Schmidhuber. 1997. Long short-term memory. Neural computation.

[Dhwaj Raj's deep-siamese-text-similarity implementation](https://github.com/dhwajraj/deep-siamese-text-similarity)
