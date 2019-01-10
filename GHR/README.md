# TV Show Recommendations based on Textual Similarity of Subtitles
*Authors*: Ivan Rukhavets, Kamil Grabowski, Piotr Halama

**TODO**: Abstract

## Introduction

  ### Wstęp
  Celem projektu jest określenie podobieństwa seriali na podstawie napisów z ich kilku pierwszych odcinków oraz przygotowanie aplikacji, która dla serialu wybranego z przygotowanej przez nas listy wskaże kilka najbardziej podobnych seriali.

**TODO**: use cases

## Usage

### Frontend

To start a server, do:

```{bash}
yarn # to install dependencies
yarn start # to start server
```

Then you can see the app running at `localhost:3000`

## Solution

### Data preparation

As a training data set we have used items from the [IMDb datasets](https://datasets.imdbws.com/) tagged as `tvSeries` or `tvMiniSeries`  created after 1970 with at least 10000 user rates. This has given us 990 shows. Next we have tried to download and unpack first episodes' subtitles of each season of each show from [opensubtitles.org](opensubtitles.org). As a result we have gathered more than 4000 episodes for 872 shows. The next step is removing metadata (i.e. indexes or timestamps) from the `.srt` file. The resulting corpus of TV series subtitles can be found [here](https://drive.google.com/open?id=1EydDpkS8LuP_vjp7g1A6hEa08ezL7Jf7).
  

### Comparison method

  ### Metoda porównywania seriali
  Najpierw łączymy kilka pierwszych odcinków serialu w jeden napis, a następnie wybieramy z niego sto najczęściej występujących rzeczowników. Przy pomocy fastTextu znajdujemy dla każdego z tych rzeczowników word embedding. Wyznaczamy word embedding serialu jako średnią z wcześniej otrzymanych embeddingów. Ostatecznie dla każdego serialu znajdujemy te, które są do niego podobne przy użyciu podobieństwa kosinusowego:

![](./imgs/eq1.png)

[comment]: # (\[\frac{\sum_{i=1}^{n}A_i*B_i}{\sqrt{\sum_{i=1}^{n}A_i^2}*\sqrt{\sum_{i=1}^{n}B_i^2}}\])

### Implementation details
**MAYBE**

## Results
The quality of our solution has been tested by comparing it to TasteDive, website which helps to find similar music, movies, tv shows, books, authors and games.
We conducted surveys, which can by found at the following address: [](https://goo.gl/forms/tHUYKyld723O0ptw1).
Each participant had a task to assign to each of the 24 tv shows one of the 4 answers: show chosen by our algorithm, show chosen by TasteDive, "Both are equally similar" and "I can not tell".

![](./imgs/survey_results.png)
<!---
Shows chosen by our algorithm have been selected 16 times, shows chosen by TasteDive have been selected 56 times, answer "Both are equally similar" has been chosen only 2 times and answer "I can not tell" has been chosen 71 times.
-->
We consider that one of pairs of series assigned to a given tv show won if it had more votes.
Shows chosen by our algorithm won 6 times and shows chosen by TasteDive won 14 times.

Assignment of similar series to "Death Note" and "Cowboy Bebop" gave interesting results.

### Death Note
"Death Note" is anime and crime show, our algorithm found the series the most similar to it to be "Sherlock", which is also crime show, but not animation.
TasteDive chose "Code Geass" which is anime like "Death Note", but subject matter of series is completely different.

### Cowboy Bebop
Similar situation is with "Cowboy Bebop", it is anime, the action takes places in the future (space ships and interplanetary travels are important elements of plot).
Our algorithm chose "Futurama" to be the most similar to it.
It is cartoon, which takes places in future and spaceships and interplanetary travels are also important elements of plot. TasteDive chose "Samurai Champloo", which is anime, but it takes place in completely different time than "Cowboy Bebop".

<!---
## Related work 
**TODO**
-->

## Conclusion
In both cases described above most people chose shows proposed by TasteDive.
It shows that our algorithm sometimes makes decisions, which are not obvious to people, because it is based only on words and there are other things, that are important to people watching tv shows.
Such as style of animation or fact, that show is live action.



