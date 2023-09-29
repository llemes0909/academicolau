from django.db import models


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome_cidade}, {self.uf}"


class Ocupacao(models.Model):
    nome_ocupacao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_ocupacao}"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    def __str__(self):
       return f"{self.nome}"


class Instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=100)
    site_instituicao = models.CharField(max_length=100)
    telefone_instituicao = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.nome_instituicao}"


class Area(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"


class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    cargahorario_curso = models.CharField(max_length=100)
    duracao_curso = models.CharField(max_length=11, unique=True)
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)
    Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_curso}"


class Semestre(models.Model):
    nome_semestre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_semestre}"


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"


class Matricula(models.Model):
    Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsaotermino = models.DateField()

    def __str__(self):
        return f"{self.Instituicao}"


class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao}"


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    Disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numerodefaltas = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.curso}"


class Turma(models.Model):
    turno = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    periodo_semestre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.turno}"


class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao}"

class Periodo(models.Model):
    nome_periodo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_periodo}"

class DisciplinaPorCurso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"
