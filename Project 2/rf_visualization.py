# load dependencies
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# import data

from mega import model_df
df = model_df.copy()

# encode object columns as needed
# intialize encoders
ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False, dtype='int')
le = LabelEncoder()

# encode columns with only 2 unique values
df["D/N"] = le.fit_transform(df["D/N"])
df["H/A"] = le.fit_transform(df["H/A"])
df["W/L"] = le.fit_transform(df["W/L"])

# encode column with multiple values
encoded_opp = ohe.fit_transform(df[['Opp']])
encoded_df = pd.DataFrame(encoded_opp, columns=ohe.get_feature_names_out(['Opp']), index=df.index)


# concat encoded data to original dataframe, drop original "opp" column, save as new df
model_df = pd.concat([df, encoded_df], axis=1)
model_df = model_df.drop(columns= "Opp")

# debug: Locate the positions of "error"
error_positions = model_df.isin(['error'])

# get the indices of "error" values
error_indices = [(row, col) for row, col in zip(*error_positions.to_numpy().nonzero())]

# apply new values to those data cells
model_df.iloc[37, 15] = 0
model_df.iloc[1118, 13] = 0

# ensure column values are numerical
model_df['OPP_kk'] = pd.to_numeric(model_df['OPP_kk'], errors='coerce')
model_df['Opp_hits'] = pd.to_numeric(model_df['Opp_hits'], errors='coerce')

# Get target variable ("win/loss" column) - y 
y = model_df["W/L"]

# Get the features - X
X = model_df.copy()
X =X.drop(columns = "W/L", axis =1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=5)

# scale the data!
# Initialize the scaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Fit and transform the training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform the test data using the same parameters
X_test_scaled = scaler.transform(X_test)

# Create the random forest classifier model
# with n_estimators=128 | change as needed, or run multiple n_estimators...?
rf_model = RandomForestClassifier(n_estimators=128, criterion="gini", max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0, max_features="auto", random_state=5)

# Fit the model to the training data
rf_model.fit(X_train_scaled, y_train)