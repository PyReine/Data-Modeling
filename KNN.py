from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
#try k from 1 to 11 to see which K is most accurate
ks=11
a=np.zeros(ks-1)
for k in range(1,11):

   neigh=KNeighborsClassifier(n_neighbors=k)
   neigh.fit(X_train,y_train)
   y_pred=neigh.predict(X_test)
   a[k-1]=metrics.accuracy_score(y_test,y_pred)
   
