# faloodehproject
Hi every one this project is first iranian python web framwork it is base on WSGI and using webob for manage requests and responses
but This project has a difference with other frameworks is that you are free to create your own middleware. Better to say, upgrade the
layer you create for yourself, the framework, and you can even combine parts of other frameworks and create your favorite system, for 
example, I like the Django database model system and I use it in Faloodeh for the database system.(if your layer was good create pull for to here
for use us and maybe marge here or create new packge and feedback me!
now let's watching the part of project

Documentation
-------------

Documentation for Faloodeh can be found on `Read The Docs`_.

.. _Read The Docs: https://amirmohammaddehghan.github.io/faloodehproject/


## installion

you can follow this link for  guide https://amirmohammaddehghan.github.io/faloodehproject/installation/

Or

  use pip install Faloodeh

## More details

**Faloodeh_Ui**

faloodeh ui is html, css and javascript compiler use this you can code all af them in python and if you like jinja2 no problem

easily you can send code compiled use this as context in jinja2 and and use that in your templates 

so why i wrote it becuose when you are develop the web programs in python as fullstack you should use html css javascript with that fucking carly brackets

i mean is this --> {} and <tag> </tag>.

ok this part have many tool first is html 5

and you can use this like here:
    
        >>> from Faloodeh.Faloodeh_UI import html5
        >>> code = html5()
        >>> code.h1(inner=' Hello World!', pyclass='Faloodeh', pyid='Faloodeh_UI')
        >>> print(code)
  
        result: <h1 class=" Faloodeh " id="Faloodeh_UI">  Hello World!</h1>
        
and you can use this object every where easily and you can use it as jinja2 context and use it in your template!

secend is py2js use this you can write python code and after run you have javascript code 

        >>> from Faloodeh.Faloodeh_UI.py2js import js2py
        >>> def func(a, b):
        >>>    console.log(a + b)
        >>> code = js2py( func , { a=4 , b=6 } )
        >>> print(code)
  
        result: 
                var a = 4
                var b = 6
                function func(a, b){
                    console.log(a + b)
                };

ta da! you wrote python but now you have javascrip code you have two why to use this at frist you can take print and copy and paste 

secend you can return code to jinja2 context like this:

    context = { 'my_js_code':code }

and about 

**Faloodeh_WSGI and Faloodeh_Framwork and Faloodeh_Sqlalchemy I wrote a simple blog in this repository and you can go and watch examples
code**

here: * `faloodeh_blog`_
.. _faloodeh_blog : /faloodeh_blog
