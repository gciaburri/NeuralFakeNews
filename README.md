# NeuralFakeNews
Group 12: Haley Snyder, Gabriel Ciaburri, Noemy Cervantes, Kaylie Batey, Nestor Govea
# To clone/ build: 
Clone NeuralFakeNews in terminal, cd into NeuralFakeNews, run app.py 

# What the code does: 
app.py displays the data (stored in articleResults.txt and results.txt) we obtained by inverting several articles through different LLMs and passing the inversions through Grover. We tested Grover to see if it could detect the AI inverted articles, and then we compared the LLMs looking to see which Grover performed best against. The code gives the user a few different options for displaying these results 

<img width="245" alt="Screenshot 2024-04-17 at 9 13 57 PM" src="https://github.com/gciaburri/NeuralFakeNews/assets/68760828/b2acac66-2981-4dac-8973-cc2f9c34aad6">

# Archaeologist:
1. Deep contextualized word representations
Matthew Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and
Luke Zettlemoyer. https://aclanthology.org/N18-1202.pdf
(refrenced by Defending Against Neural Fake News)

This article shows the researchers' improvement to language model's ability to analyze text, improving model's ability to detect context in writing. The authors of Defending Against Neural Fake News (our inspiration for this project) used this article in their research, because it showed that a language model could be a promising way to dectect fake LLM generated articles. 


2. The Limitations of Stylometry for Detecting Machine-Generated Fake News
Tal Schuster, Roei Schuster, Darsh J. Shah, Regina Barzilay https://direct.mit.edu/coli/article/46/2/499/93369/The-Limitations-of-Stylometry-for-Detecting
(refrences Defending Against Neural Fake News)

In this article the authors propose an improved way to detect LM generated fake news by suggesting an approach that does not focus on stylometry (since machine generated text is the same style regardless of whether it is fake or legitimate). They based their experiments on the methods used in Defending Against Neural Fake News, utilizing the Grover model in their experiment.
