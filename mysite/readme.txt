>>> Django Polling Application <<<

This is Basic Django Polls Application with BootStrap.

Python2.7 and Django 1.9 are used. Please refer requirement.txt for setting up the project.


>>> Testing the application

++ Run the below command from your project root direcotry(where manage.py presents)

C:\Afiz\GitApps\djangoapps\mysite>python manage.py test polls

++ You should be getting results if everything goes well.

Creating test database for alias 'default'...
.....
----------------------------------------------------------------------
Ran 5 tests in 0.267s

OK
Destroying test database for alias 'default'...

>>> Dynamic url patterns with names:
<! a href= "{% url 'blog:detail' post.id %}"></a>
here blog is app name and detail is url name
ex: url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail')

C:\Afiz\GitApps\djangoapps\mysite>python manage.py test polls
Creating test database for alias 'default'...
......
----------------------------------------------------------------------
Ran 6 tests in 1.176s

OK
Destroying test database for alias 'default'...
