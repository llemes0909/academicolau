from django.shortcuts import render
from . models  import*


def cidade(request):
    cidade = {
         'cidade':Cidade.objects.all()
        }

    return render(request,'cidades/cidades.html',cidade)

def ocupacao(request):
    ocupacao = {
         'ocupacao':Ocupacao.objects.all()
        }

    return render(request,'ocupacao/ocupacao.html',ocupacao)

def pessoa(request):
    pessoas = {
         'pessoa':Pessoa.objects.all()
        }

    return render(request,'pessoa/pessoa.html',pessoas)

def instituicao(request):
    instituicaos = {
         'instituicao':Instituicao.objects.all()
        }

    return render(request,'instituicao/instituicao.html',instituicaos)

def area(request):
    areas = {
         'area':Area.objects.all()
        }

    return render(request,'areadosaber/areadosaber.html',areas)

def curso(request):
    curso = {
         'curso':Curso.objects.all()
        }

    return render(request,'curso/curso.html',curso)

def semestre(request):
    semestre = {
         'semestre':Semestre.objects.all()
        }

    return render(request,'semestre/semestre.html',semestre)

def disciplina(request):
    disciplina = {
         'disciplina':Disciplina.objects.all()
        }

    return render(request,'disciplina/disciplina.html',disciplina)

def matricula(request):
    matricula= {
         'matricula':Matricula.objects.all()
        }

    return render(request,'matricula/matricula.html',matricula)

def tipoAvaliacao(request):
    tipoAvaliacao= {
         'tipoAvaliacao':TipoAvaliacao.objects.all()
        }

    return render(request,'tipoavaliacao/tipoavaliacao.html',tipoAvaliacao)

def avaliacao(request):
    avaliacao= {
         'avaliacao':Avaliacao.objects.all()
        }

    return render(request,'avaliacao/avaliacao.html',avaliacao)

def frequencia(request):
    frequencia= {
         'frequencia':Frequencia.objects.all()
        }

    return render(request,'frequencia/frequencia.html',frequencia)

def turma(request):
    turma= {
         'turma':Turma.objects.all()
        }

    return render(request,'turma/turma.html',turma)

def ocorrencia(request):
    ocorrencia= {
         'ocorrencia':Ocorrencia.objects.all()
        }

    return render(request,'ocorrencia/ocorrencia.html',ocorrencia)

def periodo(request):
    periodo= {
         'periodo':Periodo.objects.all()
        }

    return render(request,'periodo/periodo.html',periodo)

def disciplinaPorCurso(request):
    disciplinaPorCurso= {
         'disciplinaPorCurso':DisciplinaPorCurso.objects.all()
        }

    return render(request,'disciplinaporcurso/disciplinaporcurso.html',disciplinaPorCurso)