from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def reg_prep(dfnr, to_pred_cols_lst):
    # Create arrays for features and target variable
    df_to_pred = dfnr[to_pred_cols_lst]
    y = df_to_pred.values
    df_wo_y = dfnr.drop(to_pred_cols_lst, axis="columns")
    X = df_wo_y.values

    y_labels = df_to_pred.columns
    x_labels = df_wo_y.columns
    return X, y, x_labels, y_labels


def reg_prep_scaled(dfnr, to_pred_cols_lst):
    # Create arrays for features and target variable
    df_to_pred = dfnr[to_pred_cols_lst]
    df_wo_y = dfnr.drop(to_pred_cols_lst, axis="columns")

    scaler_x = MinMaxScaler()
    scaler_y = MinMaxScaler()
    X = scaler_x.fit_transform(df_wo_y)
    y = scaler_y.fit_transform(df_to_pred)

    y_labels = df_to_pred.columns
    x_labels = df_wo_y.columns
    return X, y, x_labels, y_labels, scaler_x, scaler_y


def reg_prep_split(X, y, test_size=0.3):
    # Create training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    return X_train, X_test, y_train, y_test


def categorical_prep(df1, col):
    # if CATEGORICAL data
    # Create dummy variables:
    df2 = df1.join(pd.get_dummies(df1[col]))
    df2.drop([col], axis="columns", inplace=True)
    return df2


def categorical_code(pds):
    return pds.astype("category").cat.codes


# from sklearn import preprocessing
# le = preprocessing.LabelEncoder()


def importants(labels, coefs):
    df1 = pd.DataFrame()
    df1["a"] = labels
    df1["b"] = coefs
    df1 = df1.sort_values("b", key=lambda x: -abs(x))[df1.b.abs() > 0.0]
    return df1
