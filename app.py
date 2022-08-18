#!/usr/bin/env python
# coding: utf-8

# In[23]:


from flask import Flask,request,render_template


# In[24]:


app = Flask(__name__) #__xx__ is for reserved words


# In[25]:


import joblib


# In[26]:


@app.route("/", methods = ["GET","POST"]) #decorator. Any function that you declare below, you must run this first.

def index():
    if request.method == "POST": ##After you press enter
        rates = float(request.form.get("rates"))
        print(rates)
        
        model1= joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        
        
        return(render_template("index.html", result1=r1, result2 = r2))
    elif request.method == "GET": #before you press enter
        return(render_template("index.html", result1="waiting", result2 = "waiting"))
        


# In[ ]:


if __name__ == "__main__": # if you are in the cloud environment. __name__ will only be main if the code you are running is 
                            #the main file
        
    app.run() #this will run all the functions under app.route


# In[ ]:




