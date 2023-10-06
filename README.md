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
