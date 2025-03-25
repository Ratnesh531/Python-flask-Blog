from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json



with open('config.json','r') as c:
    params = json.load(c)["params"] 

localServer = params["local_server"]

app = Flask(__name__)

if(localServer):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_db_uri"] # "mysql+pymysql://root:@localhost/programmersblog"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_db_uri"] # "mysql+pymysql://root:@localhost/programmersblog"
db = SQLAlchemy(app)
class Contacts(db.Model):
    '''
    sno, name, phone, message, Date, E_mail
    '''
    sno = db.Column(db.Integer,primary_key = True)
    Name = db.Column(db.String(50), nullable=False)  
    Phone = db.Column(db.String(50),nullable = False)
    E_Mail = db.Column(db.String(50),nullable = False)
    Message = db.Column(db.String(200),nullable = False)
    Date = db.Column(db.String(50))

    # s.no.: Mapped[int] = mapped_column(primary_key=True)
    # username: Mapped[str] = mapped_column(unique=True)
    # email: Mapped[str]
class Blogs(db.Model):
    '''
    sno, title, slug, Content, date
    '''
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(50), nullable=False)  
    slug = db.Column(db.String(50),nullable = False)
    Content = db.Column(db.String(200),nullable = False)
    date = db.Column(db.String(50))

    # s.no.: Mapped[int] = mapped_column(primary_key=True)
    # username: Mapped[str] = mapped_column(unique=True)
    # email: Mapped[str]

@app.route('/')
def home():
    post = Blogs.query.filter_by().all()
    return render_template('index.html',params=params,posts=post)

@app.route('/login',methods = ['GET','POST'])
def login():
    if(request.method == 'POST'):
        pass
    else:
        return render_template('login.html',params=params)

@app.route('/about')
def about():
    
    return render_template('about.html',params=params)

@app.route('/post/<string:post_slug>',methods=['GET'])
def Post_route(post_slug):
    '''
    sno, title, slug, Content, date
    '''
    post = Blogs.query.filter_by(slug=post_slug).first() #avoid multiple slug though
    #print(f"title: {title}, Content: {Content}, date: {date}")
    return render_template('post.html',params=params, post=post)

@app.route('/contact', methods = {'GET','POST'})
def contact():
    if(request.method == 'POST'):
        ''' Add Entery to data Base'''
        '''sno, name phome message Date E_Mail'''

        name = request.form.get('name')
        phone = request.form.get('phone')
        message = request.form.get('message')
        Mail = request.form.get('email')
        print(f"Name: {name}, Phone: {phone}, Message: {message}, E-Mail: {Mail}")
        entry= Contacts(Name = name,Phone = phone, Message = message,Date=datetime.now(),E_Mail = Mail)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html',params=params)
# def bootstrap():
#     name  = "ratnesh"
#     return render_template('bootstrap.html',name = name)

if __name__ == '__main__':
    app.run(debug=True,port = 5001)



    

