import pandas as pd
from scipy import stats


def mere(x:pd.Series)->dict:
    x=pd.to_numeric(x,errors="coerce").dropna().astype(float)

    positive = x[x>0]

    summary = stats.describe(x)

    q3=x.quantile(q=0.75)
    q1=x.quantile(q=0.25)

    return{
        "n":len(x),
        "aritmeticka_sredina":x.mean(),
        "geometrijska_sredina":stats.gmean(x),
        "harmonijska_sredina":stats.hmean(x),
        "10_perc_trimovana":stats.trim_mean(x,proportiontocut=0.1),
        "raspon":x.describe().loc['max']-x.describe().loc['min'],
        "varijansa_uzorka":x.var(),
        "std_devijacija":x.std(),
        "IQR":q3-q1,
        "koeficijent_varijacije_perc":stats.variation(x),
        "asimetrija":stats.skew(x),
        "spljostenost":stats.kurtosis(x,bias=False),
        "q1":q1,
        "q3":q3,
        "p95":x.quantile(0.95),
        "mod":x.mode().iloc[0],
        "medijana":x.median()
    }

