from flask import Flask,render_template
app=Flask(__name__)


# @app.route("/test")
# def test():
#     py_name="すなばこ太郎"
#     return render_template("base.html",name=py_name)






if __name__=="__main__":
    app.run(debug=True)
