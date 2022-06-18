from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

import pickle

from core import forms
from core.utils import prepare_text
from core.models import Sentence


class MainView(TemplateView):
    template_name = 'core/main.html'
    sentences = Sentence.objects.annotate(positive=F(
        'result') + F('result2') + F('result3')).all()[:5]

    def post(self, request, *args, **kwargs):
        form = forms.TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            prepared_text = prepare_text(text)

            model = pickle.load(open("ml_models/logistic_uni.sav", "rb"))
            result = model.predict(prepared_text)

            model2 = pickle.load(open("ml_models/naive_uni.sav", "rb"))
            result2 = model2.predict(prepared_text)

            model3 = pickle.load(open("ml_models/svm_uni.sav", "rb"))
            result3 = model3.predict(prepared_text)

            sentence = Sentence(text=text, result=result,
                                result2=result2, result3=result3)
            sentence.save()
            sentences = Sentence.objects.annotate(positive=F(
                'result') + F('result2') + F('result3')).all()[1:6]

            return render(request, 'core/main.html', {'sentence': sentence, 'form': forms.TextForm(), 'sentences': sentences})
        return HttpResponse('Provided incorrect sentence')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.TextForm()
        context['sentences'] = self.sentences
        return context
