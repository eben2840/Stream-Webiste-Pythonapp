from flask import Flask,redirect,url_for,render_template,request






app=Flask(__name__)
app.config['SECRET_KEY']= 'ADKADKFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


@app.route('/',methods=['GET','POST'])
def main2():
    return render_template('main2.html')

@app.route('/main',methods=['GET','POST'])
def main():
   return render_template('main.html')

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/bus',methods=['GET','POST'])
def bus():
   return render_template('bus.html')

@app.route('/sus',methods=['GET','POST'])
def sus():
   return render_template('sus.html')

@app.route('/media',methods=['GET','POST'])
def media():
   return render_template('media.html')

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