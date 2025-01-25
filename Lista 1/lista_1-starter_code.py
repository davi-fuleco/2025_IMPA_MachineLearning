# Exercício 2(d)

import numpy as np

n = 50
Sigma = np.diag([10**((i-20)/5) for i in range(1,n+1)])

np.random.seed(0)
X = np.array([np.ones(n),np.random.normal(0,1,n)]).T
beta = np.array([1,0.25])
epsilon = np.random.multivariate_normal(np.zeros(n),Sigma)
y = X @ beta + epsilon

#########################################################################################################

# Exercício 3(f)

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

np.random.seed(1)

beta = np.array([-1.5, 2.0])
input_range = np.linspace(-1, 1, 100)
X = np.vstack([np.ones(100), input_range]).T
y = X @ beta + np.random.normal(0, 0.3, 100)

def calculate_laplacian_loss(parameters, X, y):
    return np.sum(np.abs(y - X @ parameters))

# Complete as linhas abaixo
beta_hat_gaussian = ...
beta_hat_laplacian = ... 

#########################################################################################################

# Exercício 3(f)-iii

y[80] = 10

#########################################################################################################

# Exercício 4(e)

import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

p = 5
n = 1000

np.random.seed(10)
beta = np.ones(p)
X = np.random.normal(loc=0,scale=1,size=(n,p))

logits = 1/(1+np.exp(-X@beta))
y = np.random.binomial(n=np.ones(n).astype(int),p=logits, size = n)

#########################################################################################################

# Exercício 4(h)

import statsmodels.api as sm
logit_model = sm.Logit(y, X)
print(logit_model.fit().summary())

#########################################################################################################

# Exercício 5 - primeira seção de código

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
from sklearn.linear_model import LogisticRegression as LR
from sklearn.naive_bayes import GaussianNB as NB
from sklearn.neighbors import KNeighborsClassifier as kNN
from sklearn import preprocessing

df = pd.read_csv("./soccer.csv")

X = df.drop("target", axis=1)
y = df[["target"]]

X_train, y_train = X.iloc[:2560], y.iloc[:2560]
X_test, y_test = X.iloc[2560:], y.iloc[2560:]

#########################################################################################################

# Exercício 5 - segunda seção de código

X_train = X_train.drop(["home_team", "away_team"], axis=1)
X_test = X_test.drop(["home_team", "away_team"], axis=1)

scaler = preprocessing.StandardScaler().fit(X_train)
X_train = preprocessing.scale(X_train)
X_test = scaler.transform(X_test)

#########################################################################################################

# Exercício 6

import statsmodels.api as sm
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn import preprocessing

bodyfat = pd.read_csv("../bodyfat.csv")

X = bodyfat.drop(columns=["BodyFat","Density"])
y = bodyfat["BodyFat"]
X_train, X_test, y_train, y_test = train_test_split(X,y,
test_size=0.2,
random_state = 10
)

kf = KFold(n_splits = 5, shuffle = True, random_state = 10)
cv_fold = np.zeros(len(y_train)).astype(int)
for i, (_, fold_indexes) in enumerate(kf.split(X_train)):
cv_fold[fold_indexes] = int(i)

#########################################################################################################

# Exercício 6(d)

alphas = 10**np.linspace(5,-2,100)