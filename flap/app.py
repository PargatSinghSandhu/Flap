from flask import Flask, render_template  #render_temlate is a function to render the template


app = Flask(__name__) #__name__ special variable that is the name of the module
#that is like flask can know where to look for files, templates

#this is sort of list of dictonaries to make a temporary database
posts = [{'author':'Robinn Hood', 'title':'Life of a Human', 'price':'$20'},
         {'author':'Jason', 'title':'The fin', 'price':'$30'}]


@app.route("/") #route is what we put into our browsers to go into specific page
@app.route("/home")
def home():
    #return ''' html doctype code ''' #this is the genral code we can do, but it will create a mess
    return render_template('home.html', db = posts) # this posts will give us the access to the posts DB, and can use that
#posts is a argument which is passed in the home template, and using that we can access the psots DB.
@app.route("/about")
def about():
    return render_template('about.html', title = 'About')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5556, debug = True)