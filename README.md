# dsci-310-group-11 - Wine Quality Analysis

## Contributors
- Rudy Ma
- Oscar Cheng
- Tyler Stevenson

## Project Summary
This project analyzes the UCI Machine Learning Wine Quality datasets (https://archive.ics.uci.edu/dataset/186/wine+quality) to see if the quality of red wine samples can be determined based on their physicochemical properties and if so, which properties are the strongests indicators to the quality of a wine.

The classification model used for the analysis is a Logistic Regression model from Pythons scikit-learn library

The analysis suggests that physicochemical proporties are indeed robust predictors of the sensory quality of red wine, with alcohol content standing out as a strong predictor, however the error rate present in the analysis shows that chemical features are not the only determinators for wine quality.

Overall, the model shows that it is possible and viable to use the chemical properties of wine to identify lower quality wines, which can be used by wineries in the production process to flag low quality batches. 

## Dependencies
The project has the following dependencies:
- pandas (2.2.0)
- matplotlib (3.8.3)
- seaborn (0.13.2)
- scikit-learn (1.4.2)

## Installation
The project utilizes Docker for dependencies. Ensure you have Docker installed and running. To set up the Docker environment, do the following.

1. Pull the pre-built Docker image from Docker Hub by running the following command in your terminal:

```bash
docker pull oscarcheng77/dsci-310-group-11:latest
```

2. Run the container using the following command in the terminal:
```
docker run --rm -p 8888:8888 -v "$(pwd):/home/jovyan/work" oscarcheng77/dsci-310-group-11:latest
```

This will allow the project to be accessed from the brower at localhost:8888. It will ask for a token for access. The token can be found in the terminal output following a url with the form `?token=`


## Running the Analysis

The analysis can be run from the browser using the previous steps. The `predict_wine_quality.ipynb` file can be opened, which contains the analysis model. Code blocks can be run sequentially using `Shift + Enter`. 

## Licensing
- **Code:** MIT License  
- **Project Report:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

See the `LICENSE.md` file for full license texts.
