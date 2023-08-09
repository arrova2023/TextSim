The corpus used in this project is found in the following path:

corpus/corpus.csv

This CSV file contains the original and suspect texts that will be used to calculate the textual similarity. The corpus is structured with two columns:

     Original Statement: This column contains the original texts, which are the reference texts against which the suspect texts will be compared.
    
     Suspect Sentence: This column contains the suspect texts, which are the texts that will be evaluated to determine their similarity with the original texts.

     Similar: This column indicates whether the original and suspect statements have the same meaning or not. This information is used as a reference label for the calculation of similarity and to train Machine Learning models, it is a boolean value.

The objective is to calculate the similarity between the original utterances and the suspected utterances using Natural Language Processing and Machine Learning techniques. This similarity will allow us to understand how close the texts are and if they share the same meaning or content.

To run this project, make sure you have Python 3.11 or higher installed. You will also need the spacy library to perform stemming of the text. You can install it using the following command:

pip install spacy

In addition, the file "stopwords.txt" is required, which contains a list of function words in Spanish. Make sure you have this file in the "resources/stopwords.txt" path.
Use

Place the texts original.txt and suspect.txt in the "corpus/" folder.


If you want to run the project using Python 3.10 instead of Python 3.11, you can follow these steps:

     * Open a terminal in your operating system.
     * Navigate to the root directory of the project using the command cd path/del/project.
     * To run the linker.py script with Python 3.10, use the following command:

     python3.10 linker.py

This will start the execution sequence defined in the linker.py script, which includes generating files and running other scripts as needed by the project.
Remember that Python 3.10 must be installed on your system in order to run the project with this version.

Additional notes

     If you need to change the stopwords used in the project, you can edit the "stopwords.txt" file in the "resources/" folder.

     If you want to add more detail or functionality to the project, you can explore and modify the corresponding Python files. Comments in the code will guide you on how it works.

Accuracy: Accuracy is a measure that evaluates the proportion of correct predictions made by the model. In the context of this project, it represents the number of positive elements correctly identified in relation to the total number of elements identified as positive.

Coverage: Coverage is a measure that assesses what proportion of all existing positive elements were identified by the model. In the context of the project, coverage represents the number of positive elements correctly identified in relation to the total number of actual positive elements.

F1 Score: The F1 score is a measure that combines accuracy and coverage into a single metric, providing a more comprehensive assessment of model performance. It is especially useful when the classes are unbalanced. A higher F1 score indicates a balance between accuracy and coverage.

Each of these measures has its own importance in the evaluation of a textual similarity model and provides valuable information about its ability to correctly identify and classify original and suspect texts.

About Accuracy, Coverage and Future Updates

It is important to note that although the refinement.py script generates precision and coverage values, currently only the precision is calculated correctly. Coverage requires additional adjustment to provide accurate results. We are working on improving and fixing this, and an update will be released in the coming weeks that will correct the coverage and also include the F1 score column to provide a more complete evaluation of the model.
Last Update of the Year

We want to inform you that this is the penultimate update scheduled for this year. We are committed to continue improving and updating the project to offer more features, fixes and improvements in the future.

We appreciate your interest in the project and your patience while we work on updates and improvements. If you have any questions or comments, feel free to contact us. We hope you find this textual similarity project useful and valuable!