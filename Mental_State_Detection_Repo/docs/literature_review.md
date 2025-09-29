**Abstract:**

The recognition of human mental states through speech has become an
increasingly important research area at the intersection of psychology, signal
processing, and artificial intelligence. This study aims to develop and evaluate
models capable of identifying mental and emotional states from acoustic features
of speech using both classical machine learning and deep learning approaches.
The dataset, enriched through data augmentation techniques to address
imbalance, was analyzed using features such as Mel-Frequency Cepstral
Coefficients (MFCC), pitch, energy, and statistical descriptors. Random Forest
(RF) and Multi-Layer Perceptron (MLP) models were implemented and
compared, alongside a novel hierarchical classification framework that first
categorized utterances into broad groups (positive, negative, neutral) before
refining them into more specific states (e.g., happy, sad, anxious).
The results indicated that RF achieved stable and interpretable performance,
particularly highlighting pitch median and MFCC coefficients as key predictors.
MLP outperformed RF in certain categories, capturing more complex non-linear
relationships in the data, though it remained challenged by closely related states.
The hierarchical approach significantly improved classification accuracy by
reducing errors among psychologically and acoustically similar classes.
Overall, the findings demonstrate that speech signals provide a reliable and
independent source for detecting mental states, and that integrating classical
models with deep learning techniques, particularly within a hierarchical
framework, can yield promising results. This research contributes to advancing
human-computer interaction, mental health monitoring, and affective computing
applications.

**Keywords:** Speech Emotion Recognition; Mental State Detection; Machine
Learning; Deep Learning; Random Forest; Multi-Layer Perceptron; Hierarchical
Classification; Data Augmentation
