# Team GHR: TV show similarity

## Description

TVshow-sim (name is subject to change) is an application shows the most similar
TV series based on user input. The comparison between the input and TV series is based
on text similarity of transcripts.

The user input can be one of following:
  - another TV series in app's database (chosen from list)
  - a transcript, either from show not included in database or
    of their own creation

## Interface

App's functionality will be exposed in two ways:
  - a simple web interface
  - Python library

## Software requirements
There is only one hard requirement: ability to run Docker containers.

Apart from that, a web browser is required for accessing web interface.

## Similarity mechanism
### Method
Our method of choice is to use FastText embeddings and calculate dot product of
embeddings for pair of shows. For now, we will calculate document embeddings by
taking average of all word embeddings.

### Input & output
The input of the mechanism is any text written in English. There is no minimum requirement
on the length, but the more text is provided the more accurate results are returned (albeit up
to certain point, after that we could possibly encounter vanishing returns).

The output is numeric score for 0 to 1 interval, 1 meaning the most similar (identical) and 0 the least.

### Training requirements
There are currently none, as we are using pretrained word embeddings.

### Evaluation
Adequacy of our method of choice will be checked on evaluation set of
at least 200 pairs of shows, annotated either as similar or dissimalar.
