DjangoCon
=========

Pinax
------

[![Join us on Slack](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates.
This collection can be found at http://pinaxproject.com.


DjangoCon
---------
`DjangoCon` is a working demo of Symposion and the Symposion Starter Project.  Online at:

http://conference.pinaxproject.com/ (https://ky395.us2.gondor.io/ until DNS is configured)



Getting Started
----------------

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

```
createdb djangocon2016
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata fixtures/*
./manage.py createsuperuser
./manage.py runserver
```


Documentation
--------------

The `DjangoCon` documentation is currently under construction. If you would like to help us write documentation, please join our Slack team and let us know! The Pinax documentation is available at http://pinaxproject.com/pinax/.


Contribute
----------------

See [this blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/) including a video, or our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our [Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions, we would recommend for you to [join our Pinax Slack team](http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We would also highly recommend for your to read our [Open Source and Self-Care blog post](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).  


Code of Conduct
-----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a Code of Conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/. We'd like to ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


Pinax Project Blog and Twitter
-------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at [@pinaxproject](https://twitter.com/pinaxproject) and check out our blog http://blog.pinaxproject.com.
