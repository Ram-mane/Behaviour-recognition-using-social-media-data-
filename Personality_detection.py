bimport pandas as pd, numpy as np, re

from sklearn.metrics import classification_report, accuracy_score , confusion_matrix
from sklearn.model_selection import train_test_split
import tkinter as tk
from sklearn import svm
from PIL import Image, ImageTk
from tkinter import ttk
from joblib import dump , load
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
from nltk.corpus import stopwords
from sklearn import metrics
#from sklearn.model_selection import GridSearchCV
import pickle
import nltk

nltk.download('stopwords')
stop = stopwords.words('english')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
  
    
root = tk.Tk()
root.title("Behaviour Recognition Using Social Media")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
image2 =Image.open('main.png')
image2 =image2.resize((w,h), Image.ANTIALIAS)


background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)


label_l1 = tk.Label(root, text="Behaviour Recognition Using Social Media", font=("Times New Roman", 30, 'bold', 'italic'), fg="black", width=32, height=1)
label_l1.place(x=430, y=150)




def Data_Display():
    columns = ['ID', 'type', 'posts']
    print(columns)

    data1 = pd.read_csv(r"dataset1.csv", encoding='unicode_escape')

    data1.shape

    data1.shape

    data1.head()

    data1

    data1

    article_link = data1.iloc[:, 0]
    headline = data1.iloc[:, 1]
    is_sarcastic = data1.iloc[:, 2]


    display = tk.LabelFrame(root, width=300, height=400, )
    display.place(x=600, y=100)

    tree = ttk.Treeview(display, columns=(
    'ID', 'type', 'posts'))

    style = ttk.Style()
    style.configure('Treeview', rowheight=50)
    style.configure("Treeview.Heading", font=("Tempus Sans ITC", 15, "bold italic"))
    style.configure(".", font=('Helvetica', 15), background="blue")
    style.configure("Treeview", foreground='white', background="black")

    tree["columns"] = ("1", "2", "3")
    tree.column("1", width=200)
    tree.column("2", width=200)
    tree.column("3", width=200)

    tree.heading("1", text="ID")
    tree.heading("2", text="type")
    tree.heading("3", text="posts")

#    treeview = tree

    tree.grid(row=0, column=0, sticky=tk.NSEW)

    print("Data Displayed")

    for i in range(0, 304):
        tree.insert("", 'end', values=(
        article_link[i], headline[i], is_sarcastic[i]))
        i = i + 1
        print(i)


def RF():
    
    result = pd.read_csv(r"dataset1.csv",encoding = 'unicode_escape')

    result.head()
        
    result['headline_without_stopwords'] = result['posts'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    
    
    def pos(review_without_stopwords):
        return TextBlob(review_without_stopwords).tags
    
    
    os = result.headline_without_stopwords.apply(pos)
    os1 = pd.DataFrame(os)
    #
    os1.head()
    
    os1['pos'] = os1['headline_without_stopwords'].map(lambda x: " ".join(["/".join(x) for x in x]))
    
    result = result = pd.merge(result, os1, right_index=True, left_index=True)
    result.head()
    result['pos']
    review_train, review_test, label_train, label_test = train_test_split(result['pos'], result['type'],
                                                                              test_size=0.2, random_state=13)
    
    tf_vect = TfidfVectorizer(lowercase=True, use_idf=True, smooth_idf=True, sublinear_tf=False)
    
    X_train_tf = tf_vect.fit_transform(review_train)
    X_test_tf = tf_vect.transform(review_test)
    
    
    # def svc_param_selection(X, y, nfolds):
    #     Cs = [0.001, 0.01, 0.1, 1, 10]
    #     gammas = [0.001, 0.01, 0.1, 1]
    #     param_grid = {'C': Cs, 'gamma': gammas}
    #     grid_search = GridSearchCV(svm.SVC(kernel='linear'), param_grid, cv=nfolds)
    #     grid_search.fit(X, y)
    #     return grid_search.best_params_
    from sklearn.ensemble import RandomForestClassifier as RF
    clf = RF(n_estimators=9, criterion='entropy', random_state=123)  
    clf.fit(X_train_tf, label_train)
    pred = clf.predict(X_test_tf)
    
    #svc_param_selection(X_train_tf, label_train, 5)
    #
    
    clf = svm.SVC(C=10, gamma=0.001, kernel='linear')   
    clf.fit(X_train_tf, label_train)
    pred = clf.predict(X_test_tf)
    
    with open('vectorizer.pickle', 'wb') as fin:
        pickle.dump(tf_vect, fin)
    with open('mlmodel.pickle', 'wb') as f:
        pickle.dump(clf, f)
    
    pkl = open('mlmodel.pickle', 'rb')
    clf = pickle.load(pkl)
    vec = open('vectorizer.pickle', 'rb')
    tf_vect = pickle.load(vec)
    
    X_test_tf = tf_vect.transform(review_test)
    pred = clf.predict(X_test_tf)
    
    print(metrics.accuracy_score(label_test, pred))
    
    print(confusion_matrix(label_test, pred))
    
    print(classification_report(label_test, pred))

       
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(label_test, pred)))
    print("Accuracy : ",accuracy_score(label_test, pred)*100)
    accuracy = accuracy_score(label_test, pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(label_test, pred) * 100)
    repo = (classification_report(label_test, pred))
    
    label4 = tk.Label(root,text =str(repo),width=35,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=100)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as SVM_MODEL1.joblib",width=35,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=320)
    
    dump (clf,"SVM1_MODEL1.joblib")
    print("Model saved as SVM1_MODEL1.joblib")

def Train():
    
    result = pd.read_csv(r"dataset1.csv",encoding = 'unicode_escape')

    result.head()
        
    result['headline_without_stopwords'] = result['posts'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    
    
    def pos(review_without_stopwords):
        return TextBlob(review_without_stopwords).tags
    
    
    os = result.headline_without_stopwords.apply(pos)
    os1 = pd.DataFrame(os)
    #
    os1.head()
    
    os1['pos'] = os1['headline_without_stopwords'].map(lambda x: " ".join(["/".join(x) for x in x]))
    
    result = result = pd.merge(result, os1, right_index=True, left_index=True)
    result.head()
    result['pos']
    review_train, review_test, label_train, label_test = train_test_split(result['pos'], result['type'],
                                                                              test_size=0.3, random_state=9999)
    
    tf_vect = TfidfVectorizer(lowercase=True, use_idf=True, smooth_idf=True, sublinear_tf=False)
    
    X_train_tf = tf_vect.fit_transform(review_train)
    X_test_tf = tf_vect.transform(review_test)
    
    
    
    
    clf = svm.SVC(C=10,kernel='linear',random_state=9999)   
    clf.fit(X_train_tf, label_train)
    pred = clf.predict(X_test_tf)
    
    with open('vectorizer.pickle', 'wb') as fin:
        pickle.dump(tf_vect, fin)
    with open('mlmodel.pickle', 'wb') as f:
        pickle.dump(clf, f)
    
    pkl = open('mlmodel.pickle', 'rb')
    clf = pickle.load(pkl)
    vec = open('vectorizer.pickle', 'rb')
    tf_vect = pickle.load(vec)
    
    X_test_tf = tf_vect.transform(review_test)
    pred = clf.predict(X_test_tf)
    
    print(metrics.accuracy_score(label_test, pred))
    
    print(confusion_matrix(label_test, pred))
    
    print(classification_report(label_test, pred))

       
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(label_test, pred)))
    print("Accuracy : ",accuracy_score(label_test, pred)*100)
    accuracy = accuracy_score(label_test, pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(label_test, pred) * 100)
    repo = (classification_report(label_test, pred))
    
    label4 = tk.Label(root,text =str(repo),width=35,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=100)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as SVM_MODEL.joblib",width=35,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=320)
    
    dump (clf,"SVM1_MODEL.joblib")
    print("Model saved as SVM1_MODEL.joblib")

# frame = tk.LabelFrame(root,text="Control Panel",width=400,height=200,bd=3,background="cyan2",font=("Tempus Sanc ITC",15,"bold"))
# frame.place(x=500,y=350)


def reg():
    from subprocess import call
    call(["python","registration.py"])
    
def about():
    from subprocess import call
    call(["python","about.py"])
    #root.destroy()
def more():
    from subprocess import call
    call(["python","know.py"])
def log():
    from subprocess import call
    call(["python","login.py"])
    #root.destroy()
def window():
  root.destroy()
  


frame_alpr = tk.LabelFrame(root, text=" --HOME-- ", width=1600, height=100, bd=5, font=('times', 14, ' bold '),bg="orange")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=0, y=0)


button1 = tk.Button(frame_alpr, text="About us", command=about, width=12, height=1,font=('times', 12, ' bold '), bg="#008080", fg="white")
button1.place(x=10, y=10)

button1 = tk.Button(frame_alpr, text="Know more", command=more, width=12, height=1,font=('times', 12, ' bold '), bg="#008080", fg="white")
button1.place(x=150, y=10)





#button1 = tk.Button(frame_alpr, text="Login", command=log, width=12, height=1,font=('times', 12, ' bold '), bg="#008080", fg="white")
#button1.place(x=900, y=10)
#button2 = tk.Button(frame_alpr, text="Register",command=reg,width=12, height=1,font=('times', 12, ' bold '), bg="#008080", fg="white")
#button2.place(x=1050, y=10)
button3 = tk.Button(frame_alpr, text="Exit",command=window,width=12, height=1,font=('times', 12, ' bold '), bg="red", fg="black")
button3.place(x=1350, y=10)



entry = tk.Entry(root,width=30,font=('times new roman', 25),bg="skyblue",fg="black")
entry.insert(0,"Enter text here...")
entry.place(x=500,y=350)

def Test():
    predictor = load("SVM1_MODEL.joblib")
    Given_text = entry.get()
    #Given_text = "the 'roseanne' revival catches up to our thorny po..."
    vec = open('vectorizer.pickle', 'rb')
    tf_vect = pickle.load(vec)
    
    X_test_tf = tf_vect.transform([Given_text])
    y_predict = predictor.predict(X_test_tf)
    print(y_predict[0])
    if y_predict[0]=="INFJ":
        label4 = tk.Label(root,text ="INFJ: Introverted, Intuitive, Feeling, Judging \n - Insightful, empathetic, and idealistic. They are highly \n intuitive and focus on understanding others' \n emotions and motivations.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="ENFP":
        label4 = tk.Label(root,text ="ENFP: Extraverted, Intuitive, Feeling, Perceiving \n - Enthusiastic, compassionate, and expressive. They are \n highly creative and enjoy connecting with others.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="INTJ":
         label4 = tk.Label(root,text ="INTJ: Introverted, Intuitive, Thinking, Judging \n - Strategic, independent, and analytical. They are goal-oriented \n and excel in long-term planning and problem-solving.",width=50,height=5,bg='#C0C0C0',fg='black',font=("times",15,"bold"))
         label4.place(x=400,y=520)
    elif y_predict[0]=="ENTP":
        label4 = tk.Label(root,text =" ENTP: Extraverted, Intuitive, Thinking, Perceiving \n - Quick-witted, innovative, and intellectually curious. They excel \n in generating ideas and enjoy debating concepts.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)  
    elif y_predict[0]=="ESFJ":
        label4 = tk.Label(root,text =" ESFJ: Extraverted, Sensing, Feeling, Judging \n - Friendly, warm, and conscientious. They are dedicated to supporting \n others and maintaining harmony in relationships.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="ESFP":
        label4 = tk.Label(root,text =" ESFP: Extraverted, Sensing, Feeling, Perceiving \n - Outgoing, spontaneous, and fun-loving. They enjoy engaging with \n others and seek excitement and experiences.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="ESTJ":
        label4 = tk.Label(root,text =" ESTJ: Extraverted, Sensing, Thinking, Judging \n - Efficient, practical, and organized. They are natural leaders and \n value order and structure.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="ESTP":
        label4 = tk.Label(root,text =" ESTP: Extraverted, Sensing, Thinking, Perceiving \n - Energetic, action-oriented, and adventurous. They thrive in \n dynamic environments and enjoy taking risks.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="INFJ":
        label4 = tk.Label(root,text ="INFJ: Introverted, Intuitive, Feeling, Judging \n - Insightful, empathetic, and idealistic. They are highly intuitive \n and focus on understanding others' emotions and motivations.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="INFP":
        label4 = tk.Label(root,text ="INFP: Introverted, Intuitive, Feeling, Perceiving \n - Caring, creative, and idealistic. They value authenticity and \n seek meaning and purpose in their lives.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="INTJ":
        label4 = tk.Label(root,text ="INTJ: Introverted, Intuitive, Thinking, Judging \n- Strategic, independent, and analytical. They are goal-oriented and \n excel in long-term planning and problem-solving.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="INTP":
        label4 = tk.Label(root,text ="INTP: Introverted, Intuitive, Thinking, Perceiving \n - Analytical, curious, and inventive. They are independent thinkers \n and enjoy exploring abstract concepts.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="ISFJ":
        label4 = tk.Label(root,text ="ISFJ: Introverted, Sensing, Feeling, Judging \n - Warm, caring, and dependable. They are committed to serving others \n and have a strong sense of duty.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="ISFP":
        label4 = tk.Label(root,text ="ISFP: Introverted, Sensing, Feeling, Perceiving \n - Sensitive, gentle, and artistic. They appreciate beauty and \n enjoy creating harmonious environments.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    elif y_predict[0]=="ISTP":
        label4 = tk.Label(root,text ="ISTP: Introverted, Sensing, Thinking, Perceiving \n - Adaptable, logical, and hands-on. They enjoy exploring and \n manipulating the physical world to understand how things work.",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    else:
        label4 = tk.Label(root,text ="ISTP: Introverted, Sensing, Thinking, Perceiving \n - Adaptable, logical, and hands-on. They enjoy exploring and \n manipulating the physical world to understand how things work. ",width=50,height=5,bg='#C0C0C0',fg='black',font=("Times",15,"bold"))
        label4.place(x=400,y=520)
    
    
    
# button1 = tk.Button(frame,command=Data_Display,text="Data_Display",bg="gold",fg="black",width=15,font=("Times New Roman",15,"italic"))
# button1.place(x=5,y=50)

# button2 = tk.Button(frame,command=RF,text="Train",bg="red",fg="black",width=15,font=("Times New Roman",15,"italic"))
# button2.place(x=5,y=100)

button3 = tk.Button(root,command=Test,text="Submit",bg="orange",fg="Black",width=15,font=("Times New Roman",17,"bold"))
button3.place(x=650,y=430)


root.mainloop()