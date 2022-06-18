Django-app for sentiment classification
======
This is a web app made with Django for sentiment classification. User has possibility to input sentence that 
will be classified as possitive or negative by machine learning models. User also has possibility to see last five sentences which was input.

App uses three created machine learning models which was chose from among many created models. 
The entire selection and data preprocessing process is located in ml_code.ipnyb file. 

## Install

```sh
git clone https://github.com/PawelMichnowicz/Django-Blog-site.git
pip install -r requirement.txt
```

## Usage

```sh
py manage.py migrate
py manage.py runserver
```



## Appearance of application

![web1](https://user-images.githubusercontent.com/83020761/174457170-c557d9fd-ced6-449f-8a6a-54618b4ca590.png)

![web2](https://user-images.githubusercontent.com/83020761/174457182-9643c1c6-3e58-4471-8556-bdbd69fd384e.png)

