## Repo layout
```bash
    SkewDrawdown
      └───src
          │   collect_eurekahedge.py
          │   collect_hfri.py
      └───notebooks
          │   KnowYourSkew.ipynb
      └───data
          │   hfri.parquet
          │   hfri.csv
          │   eurekahedge.csv
          │   eurekahedge.parquet
```

src files:
* ```collect_eurekahedge.py```: Collects data from Bloomberg Terminal for EurekaHedge Hedge Fund Indices
* ```collect_hfri.py```: Collects data from Bloomberg Terminal for HFRI Hedge Fund Indices

notebooks:
* ```KnowYourSkew.ipynb```: Replicates research from [*Know Your Skew Using Hedge Fund Return Volatility as a Predictor of Maximum Loss*](https://www.questpartnersllc.com/downloads/Quest_Research_Series_-_No_2_Know_Your_Skew_-_June_2011.pdf)

## Analysis
The idea behind the research is that skew tends to be a better predictor for managing drawdowns. This makes sense since skew determines which tail returns heads toward as volatility picks up. The common financial trend within markets is that negative skew which would exhibit greater drawdowns have greater positive expected return since their skew pushes their central tendency (mean) towards as positive value. 
![image](https://github.com/diegodalvarez/SkewDrawdown/assets/48641554/d54e814c-2bc7-4f8f-86f6-c21bfecec096)

Breaking skew down by quantile
![image](https://github.com/diegodalvarez/SkewDrawdown/assets/48641554/1702086d-dc94-40f3-85ca-cd7cfa3d4439)

Using skew as a predictor the strategies that exhibit more positive skew tend to have less drawdowns
![image](https://github.com/diegodalvarez/SkewDrawdown/assets/48641554/0f4f1a08-1e9c-4b95-b4af-a06fa7c1a4af)

Another interesting result of carrying positive skew within returns stream is that they carry less correlation to SPX since most of the names within SPX exhibit negative skew. 
![image](https://github.com/diegodalvarez/SkewDrawdown/assets/48641554/b1bc6ddf-1aaa-47a5-bf49-65a3a0b708ad)
