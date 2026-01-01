from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Mensagem
from django.shortcuts import render, redirect
from .forms import MensagemForm
from django.db.models import Q
from django.contrib.auth.views import LoginView
from .forms import LoginForm

def landing(request):
    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            form = MensagemForm()
            return redirect("landing")
    else:
        form = MensagemForm()

    return render(request, "landing.html", {"form": form})

def login(request):
    return render(request, "login.html")

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"

@login_required
def painel(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Acesso restrito ao administrador.")
    
    q = request.GET.get('q', "").strip()

    mensagens=Mensagem.objects.all().order_by("-data_envio")
    inicio = request.GET.get("inicio")
    fim = request.GET.get("fim")

    if inicio:
        mensagens = mensagens.filter(data_envio__date__gte = inicio)

    if fim:
        mensagens = mensagens.filter(data_envio__date__lte = fim)
    
    if q:
        mensagens = mensagens.filter(
            Q(nome__icontains = q) |
            Q(email__icontains = q) |
            Q(mensagem__icontains = q)
        )
    
    total_mensagens = mensagens.count()
    
    context = {"mensagens":mensagens,
               'q': q,
               "total_mensagens": total_mensagens,
               "inicio": inicio,
               "fim": fim}
    
    return render(request, "painel.html", context)

def excluir_mensagem(request, id):
    msg = get_object_or_404(Mensagem, id=id)
    msg.delete()
    return JsonResponse({"deleted": True})