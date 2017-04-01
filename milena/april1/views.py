from django.shortcuts import render, get_object_or_404
from .models import Tips

def index(request):
    question = get_object_or_404(Tips, id=1)
    print("INICIEI O JOGO!");
    return render(request, 'index.html', {'question': question})

def start(request):
    question = get_object_or_404(Tips, id=1)
    print("ESTOU NA PRIMEIRA FASE");
    return render(request, 'start.html', {'question': question})

def startDica(request):
    question = get_object_or_404(Tips, id=1)
    if(question.chances>0):
        question.chances = question.chances -1
        question.save()
        question = get_object_or_404(Tips, id=1)
        return render(request, 'start.html', {'question': question, 'message': 'Esta e a dica 1', 'dica': True});
    else:
        return render(request, 'start.html', {'question': question, 'message': 'Voce gastou todas as dicas', 'dica': False})

def tword(request):
    question = get_object_or_404(Tips, id=1)
    print("ESTOU NA SEGUNDA FASE");
    return render(request, 'tword.html', {'question': question})

def twordDica(request):
    question = get_object_or_404(Tips, id=1)
    if(question.chances>0):
        question.chances = question.chances -1
        question.save()
        question = get_object_or_404(Tips, id=1)
        return render(request, 'tword.html', {'question': question, 'message': 'Esta e a dica 1', 'dica': True});
    else:
        return render(request, 'tword.html', {'question': question, 'message': 'Voce gastou todas as dicas', 'dica': False})

def threerd(request):
    question = get_object_or_404(Tips, id=1)
    print("ESTOU NA TERCEIRA FASE");
    return render(request, 'threerd.html', {'question': question})

def threerdDica(request):
    question = get_object_or_404(Tips, id=1)
    if(question.chances>0):
        question.chances = question.chances -1
        question.save()
        question = get_object_or_404(Tips, id=1)
        return render(request, 'threerd.html', {'question': question, 'message': 'Esta e a dica 1', 'dica': True});
    else:
        return render(request, 'threerd.html', {'question': question, 'message': 'Voce gastou todas as dicas', 'dica': False})

def fourrd(request):
    question = get_object_or_404(Tips, id=1)
    print("ESTOU NA QUARTA FASE");
    return render(request, 'fourrd.html', {'question': question})

def fourrdDica(request):
    question = get_object_or_404(Tips, id=1)
    if(question.chances>0):
        question.chances = question.chances -1
        question.save()
        question = get_object_or_404(Tips, id=1)
        return render(request, 'fourrd.html', {'question': question, 'message': 'Esta e a dica 1', 'dica': True});
    else:
        return render(request, 'fourrd.html', {'question': question, 'message': 'Voce gastou todas as dicas', 'dica': False})

def fiverd(request):
    question = get_object_or_404(Tips, id=1)
    print("ESTOU NA QUINTA FASE");
    return render(request, 'fiverd.html', {'question': question})

def fiverdDica(request):
    question = get_object_or_404(Tips, id=1)
    if(question.chances>0):
        question.chances = question.chances -1
        question.save()
        question = get_object_or_404(Tips, id=1)
        return render(request, 'fiverd.html', {'question': question, 'message': 'Esta e a dica 1', 'dica': True});
    else:
        return render(request, 'fiverd.html', {'question': question, 'message': 'Voce gastou todas as dicas', 'dica': False})

def sixrd(request):
    question = get_object_or_404(Tips, id=1)
    print("ESTOU NA SEXTA FASE");
    return render(request, 'sixrd.html', {'question': question})

def sixrdDica(request):
    question = get_object_or_404(Tips, id=1)
    if(question.chances>0):
        question.chances = question.chances -1
        question.save()
        question = get_object_or_404(Tips, id=1)
        return render(request, 'sixrd.html', {'question': question, 'message': 'Esta e a dica 1', 'dica': True});
    else:
        return render(request, 'sixrd.html', {'question': question, 'message': 'Voce gastou todas as dicas', 'dica': False})
