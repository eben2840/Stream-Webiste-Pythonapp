from flask import Flask,redirect,url_for,render_template,request






app=Flask(__name__)
app.config['SECRET_KEY']= 'ADKADKFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/blog',methods=['GET','POST'])
def blog():
    return render_template('blog.html')

@app.route('/wedding',methods=['GET','POST'])
def wedding():
    return render_template('main2.html')

@app.route('/main',methods=['GET','POST'])
def main():
   return render_template('main.html')

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/our-businesses',methods=['GET','POST'])
def ourbusinesses():
   return render_template('base.html')

@app.route('/sustainability',methods=['GET','POST'])
def sustainability():
   return render_template('sus.html')

@app.route('/media',methods=['GET','POST'])
def media():
   return render_template('blog.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
   return render_template('contact.html')



# @app.route('/',methods=['GET','POST'])
# def home():
#     if request.method=='POST':
#         # Handle POST Request here
#         return render_template('index.html')
#     return render_template('index.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)