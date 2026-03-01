import math
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import accuracy_score, roc_curve, auc 
import matplotlib.pylab as plt
from dmba import regressionSummary, classificationSummary 
from dmba import liftChart, gainsChart

walmart_df = pd.read_csv('walmart.csv')

exclude_columns =('Weekly_Sales', 'Date', 'Holiday_Flag', 'Store',
                  'CPI', 'Temperature', 'Fuel_Price')

predictors = [s for s in walmart_df.columns if s not in exclude_columns] 

outcome = 'Weekly_Sales'

X = walmart_df[predictors]
y = walmart_df[outcome] 
train_X, valid_X, train_y, valid_y = train_test_split(X, y, test_size=0.4,
                                                       random_state=1)
reg = LinearRegression()
reg.fit(train_X, train_y)



# evaluate performance 

# # training
regressionSummary(train_y, reg.predict(train_X)) 
# validation
regressionSummary(valid_y, reg.predict(valid_X)) 

pred_error_train = pd.DataFrame({ 'residual': train_y - reg.predict(train_X), 'data set': 'training'
})
pred_error_valid = pd.DataFrame({ 'residual': valid_y - reg.predict(valid_X), 'data set': 'validation'
}) 
boxdata_df = pred_error_train._append(pred_error_valid, ignore_index=True)
fig, axes = plt.subplots(nrows=1, ncols=3)
fig.set_size_inches(9, 4) 
common = {'bins': 100, 'range': [-650000, 650000]}
pred_error_train.hist(ax=axes[0], **common)
pred_error_valid.hist(ax=axes[1], **common) 
boxdata_df.boxplot(ax=axes[2], by='data set')

axes[0].set_title('training') 
axes[1].set_title('validation') 
axes[2].set_title(' ')
axes[2].set_ylim(-650000, 650000)
plt.suptitle('Prediction errors') 
plt.subplots_adjust(bottom=0.1, top=0.85, wspace=0.35)
plt.savefig('mysave.jpg')
