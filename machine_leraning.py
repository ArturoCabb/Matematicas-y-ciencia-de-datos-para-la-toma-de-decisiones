import pandas_datareader as pdr
import pandas as pd
import statsmodels.api as sm
from statsmodels.regression.rolling import RollingOLS
import matplotlib.pyplot as plt
import seaborn

seaborn.set_style('darkgrid')
pd.plotting.register_matplotlib_converters()
#%matplotlib inline

factors = pdr.get_data_famafrench('F-F_Research_Data_Factors', start='1-1-1926')[0]
print(factors.head())
industries = pdr.get_data_famafrench('10_Industry_Portfolios', start='1-1-1926')[0]
print(industries.head())

endog = industries.HiTec - factors.RF.values
exog = sm.add_constant(factors['Mkt-RF'])
rols = RollingOLS(endog, exog, window=60)
rres = rols.fit()
params = rres.params
print(params.head())
print(params.tail())

fig = rres.plot_recursive_coefficient(variables=['Mkt-RF'], figsize=(14,6))

exog_vars = ['Mkt-RF', 'SMB', 'HML']
exog = sm.add_constant(factors[exog_vars])
rols = RollingOLS(endog, exog, window=60)
rres = rols.fit()
fig = rres.plot_recursive_coefficient(variables=exog_vars, figsize=(14,18))