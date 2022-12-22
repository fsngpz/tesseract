#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[2]:


import os

path = r"C:\Users\User\KNN\DATASET\\"
files = os.listdir(path)
print(files)

classes={'0':0,'1':1,'2':2,'3':3, '4':4, '5':5, '6':6, '7':7, '1D':8, '2D':9, '3D':10, '4D':11, '5D':12, '6D':13, '7D':14, '1U':15, '2U':16, '3U':17, '4U':18, '5U':19, '6U':20, '7U':21, 'DOT':22}


# In[3]:


import cv2
from PIL import Image

x = []
y = []

for cl in classes:
    pth = path+cl
    for img_name in os.listdir(pth):
        if img_name != '.DS_Store':
#             image = Image.open(pth+"/"+img_name).convert('RGB') 
#             image = image.resize((28,28))

#             img = np.array(image)
#             img = img[:,:,0]
            img = cv2.resize(cv2.imread(pth+"/"+img_name), (28,28))[:,:,0]
            x.append(img)
            y.append(classes[cl])
# print("dataset successfully created")
        


# In[4]:


pd.Series(y).value_counts()


# In[5]:


x[0].shape


# In[6]:


print(type(x))
x = np.array(x)
y = np.array(y)
print(type(x))


# In[7]:


plt.imshow(x[21], cmap="gray")
print(y[21])


# In[8]:


x.shape


# In[9]:


x_new = x.reshape(len(x), -1)
print(x_new.shape)
print(y.shape)


# In[10]:


print(x.shape)
print(x.ndim)
print(x_new.ndim)


# In[11]:


xtrain, xtest, ytrain, ytest = train_test_split(x_new, y, test_size=.20, random_state=10)
print(xtrain.shape, ytrain.shape)
print(xtest.shape, ytest.shape)


# In[12]:


print(xtrain.max())
print(xtest.max())
x_train = xtrain/255
x_test = xtest/255
print(x_train.max())
print(x_test.max())


# In[13]:


from sklearn.decomposition import PCA
print(x_train.shape, x_test.shape)
pca = PCA(.98)
xtrain = pca.fit_transform(x_train)
xtest = pca.transform(x_test)
print(xtrain.shape, xtest.shape)
print(pca.n_components)
print(pca.n_features_)


# In[14]:


ytest[:10]


# In[15]:


log = LogisticRegression()
log.fit(xtrain, ytrain)


# In[16]:


tr_pred = log.predict(xtrain)
ts_pred = log.predict(xtest)


# In[17]:


print("Training score", accuracy_score(ytrain, tr_pred))
print("Testing Score", accuracy_score(ytest, ts_pred))


# In[18]:


plt.imshow(x_test[10].reshape(28,28), cmap='gray')
print(ytest[10])


# In[19]:


decode = {v: k for k, v in classes.items()}
for i in range(12):
    plt.subplot(3,4,i+1)
    plt.imshow(x_test[i].reshape(28,28), cmap='gray')
    plt.title(decode[ts_pred[i]])
    plt.axis('off')


# In[20]:


np.where(ts_pred!=ytest)
d = pd.DataFrame({'Actual':ytest, 'Prediction':ts_pred})
d[d['Actual'] != d['Prediction']]


# In[21]:


img = cv2.resize(cv2.imread('2U.png', 0), (28,28))
plt.imshow(img, cmap='gray')


# In[22]:


img = pca.transform(img.reshape(1,-1)/255)


# In[23]:


decode[log.predict(img)[0]]


# In[26]:


import pickle
model = log
model.fit(xtrain, ytrain)

knnPickle = open('final_model', 'wb')

pickle.dump(model, knnPickle)

knnPickle.close()


# In[27]:

def predict(imgPath):
    img = cv2.resize(cv2.imread(imgPath, 0), (28,28))
    img = pca.transform(img.reshape(1,-1)/255)
    loaded_model = pickle.load(open('final_model', 'rb'))
    result = loaded_model.predict(img)[0]
    return decode[result]


# In[ ]:




