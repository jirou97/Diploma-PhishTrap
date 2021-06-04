# PhishTrap 💻
*A web app to check if given URL leads to phishing sites*

### Phishing 
Phishing is one of the luring techniques used by phishing artist in the intention of exploiting the personal details of unsuspected users. Phishing website is a mock website that looks similar in appearance but different in destination. The unsuspected users post their data thinking that these websites come from trusted financial institutions. Several antiphishing techniques emerge continuously but phishers come with new technique by breaking all the antiphishing mechanisms. Hence there is a need for efficient mechanism for the prediction of phishing website.

### PhishTrap
PhishTrap classifies a given URL as phishing or legitimate and therefore is a first tool in the hands of the internet user protect him from visiting
malicious sites.
PhishTrap uses machine learning algorithms to predict the legitimacy of any given website, depending upon the 63 features extracted from it.
It also uses a CNN model and a voting scheme that combines the prediction probabilities from each classifier.
## Accuracy of models:
![models metrics](https://github.com/souliotispanagiotis/PhishTrap/blob/master/final_models_voting.jpg)

## Features extracted: 
The features and their explanation can be found [here](http://83.212.77.114:8080/) under the tab features.

### Website
We have developed the website using Flask, providing simple and easy mode for interaction. Just enter the URL, the click on search button to see the prediction.
User can also see the probabilities provided by each classifier.
Website can be found [here](http://83.212.77.114:8080/)

### Models not in github
- [Gradient Boosting](https://1drv.ms/u/s!AlWc1s-bBYW7gmTFQ20EXM4uBqSX?e=WFcqA9)
- [Random Forest](https://1drv.ms/u/s!AlWc1s-bBYW7gmNCQp6UAR-dMUGF?e=3aSrf5)

## To download the website
- Pull this github repository
- cd ./PhishTrap
- pip install -r requirements.txt
- Download the [models not in github](https://github.com/souliotispanagiotis/PhishTrap/tree/master#models-not-in-github) and add them to the folder models
- python app.py
- Have fun!
