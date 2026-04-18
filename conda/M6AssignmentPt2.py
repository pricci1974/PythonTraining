import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Load data from CSV
df = pd.read_csv('loanDefault.csv', nrows=1000)
df.drop(columns=['Married/Single', 'House_Ownership', 'Car_Ownership', 'Profession', 'CITY', 'STATE', 'CURRENT_JOB_YRS', 'CURRENT_HOUSE_YRS', 'Income'], inplace=True)
print(df.head())

# 2. Convert to list of lists (transactions)
transactions = df.apply(lambda x: x.dropna().tolist(), axis=1).tolist()

# 3. One-hot encoding
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# 4. Extract frequent itemsets (min_support is a threshold from 0 to 1)
frequent_itemsets = apriori(df_encoded, min_support=0.05, use_colnames=True)

# 5. Extract association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Display the rules
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
