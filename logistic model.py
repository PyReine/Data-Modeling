# Logistic model:

def logistic(x,beta1,beta2):
    y=1/(1+np.exp(-beta1*(x-beta2)))
    return y

