import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Logistical Regression:

person = {'finance': [4,56,7,8,9,2,3,4,5,6,7,4,56,43,2,4,5,6,54,7],
            'management': [2,3,4,5,1,2,3,45,5,2,12,3,2,45,45,2,23,45,21,1],
            'logistic': [23,4,32,3,54,6,7,8,4,2,11,2,34,4,5,6,7,8,1,7],
            'get_work': [1,2,3,4,5,6,7,8,9,10,1,11,12,2,14,15,17,18,19,3]
        }
data = pd.DataFrame(person,columns=['finance','management','logistic','get_work'])
# print(data)
X = data[['finance' , 'management' , 'logistic']]
y = data['get_work']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0) # 30% for testing purpose

lr = LogisticRegression()
lr.fit(X_train,y_train)
y_predictn = lr.predict(X_test)

cnfun_mtrx = pd.crosstab(y_test,y_predictn,rownames=['True'],colnames=['prevision'])
sn.heatmap(cnfun_mtrx, annot=True)
print("Accuracy: ", metrics.accuracy_score(y_test,y_predictn))

plt.show()
