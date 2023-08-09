API:

http://localhost:8000/api/

POSTMAN test:

POST: http://localhost:8000/recibirCorpus/

Headers:
Accept application/json

Content-Type application/json

JSON Body Request:
{
"original": ["Fish is a perishable food", "Hello world"],
"suspicious": ["Fish is a vegan food", "Hello world"],
"sim": [false, true]
}

In the previous example the following 2 statements were compared:
1.- "Fish is a perishable food" && "Fish is a vergan food", are they the same? = false
2.- "Hello world" && "Hello world" Are they the same? =true

in the first place of each array is placed the original statement, the suspect statement and its value that indicates whether or not they are similar in the "original", "suspect", "sim" arrays respectively.

This project is another line of research of the "Textual Similarity" project, the only difference is that in this project a REST API was developed through which the Recurrent Neural Network model can be used, said REST service was developed with Django.

Run with Python 10 or higher

python3.10 manage.py runserver

The "TextualSimiliraty" and "TextSimil" projects meet the same objective, the only difference between them is the paradigm in which each solution is implemented, which are described below:

1.- Text Similiraty:
Hopfield Recurrent Neural Network based on the Ising Model to generate a combinatorial analysis which allows us to know if a pair of statements are linguistically related with respect to their semantic load, their entire execution cycle is Stand-alone and is executed from the line of commandos, is a project of the Natural Language Processing, Machine Learning, Pattern Recognition and Artificial Intelligence areas in general.

2.- TextSimil(this project):
This project is an implementation of the "TextSimilarity" functionalities using Django 4.2.4 to be able to use this PLN Machine Learning model through a REST API to be able to consume the Hopfield Recurrent Neural Network under any possible circumstance, either for testing laboratory (precision, coverage, f1score), unit tests for chatbot development or whatever way this API decides to be consumed by the user, this project is focused within the Service Oriented Architecture so it is a plus to facilitate the implementation of "TextSimilarity" under any controlled environment of experimentation, tests or any type of event related to the generation of the results of this Learning Machine based on the Hopfield Recurrent Neuron Network.

In short, "TextSim" acts as a bridge between Hopfield's Recurrent Neural Network model and users looking to access its capabilities through a friendly and robust interface. The project provides an opportunity to take advantage of textual similarity analysis in a variety of scenarios, thanks to its focus on REST APIs and its adaptability in controlled R&D environments.

In short, this project represents a natural evolution of the original "Textual Similarity" research, opening new doors to the world of practical applications through a REST API developed with Django. "TextSim" offers not only the functionality of the Hopfield Recurrent Neural Network, but also an efficient and convenient way to use it in multiple contexts. As technology advances and needs change, "TextSim" stands out as an example of how a strong research base can converge with real-world practical demands through innovative solutions.