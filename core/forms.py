from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from . import models

class ProdutorRuralForm(forms.ModelForm):
    class Meta:
        model = models.ProdutorRural
        fields = (
            'nomeProdutorRural', 'cpfcnpj',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        nomeProdutorRural = cleaned_data.get('nomeProdutorRural')

        if nomeProdutorRural == '':
            msg = ValidationError(
                'Nome do Produtor Rural não pode ficar em branco',
                code='invalid'
            )
            self.add_error('nomeProdutorRural', msg)

        return super().clean()

    def clean_nomeProdutorRural(self):
        nomeProdutorRural = self.cleaned_data.get('nomeProdutorRural')

        if nomeProdutorRural == 'ABC':
            self.add_error(
                'nomeProdutorRural',
                ValidationError(
                    'Nome do Produtor Rural é um nome Inválido',
                    code='invalid'
                )
            )

        return nomeProdutorRural

class TipoCulturaForm(forms.ModelForm):
    class Meta:
        model = models.TipoCultura
        fields = (
            'tipoCultura',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        tipoCultura = cleaned_data.get('tipoCultura')

        if tipoCultura == '':
            msg = ValidationError(
                'Nome do Tipo de Cultura não pode ficar em branco',
                code='invalid'
            )
            self.add_error('tipoCultura', msg)

        return super().clean()

    def clean_tipoCultura(self):
        tipoCultura = self.cleaned_data.get('tipoCultura')

        if tipoCultura == 'ABC':
            self.add_error(
                'tipoCultura',
                ValidationError(
                    'Nome do Tipo de Cultura está Inválido',
                    code='invalid'
                )
            )

        return tipoCultura

class FazendaForm(forms.ModelForm):
    class Meta:
        model = models.Fazenda
        fields = (
            'nomeFazenda','cidade','estado','areaTotal','areaAgricultavel','areaVegetacao','produtorRural',
        )

    @property
    def clean(self):
        cleaned_data = self.cleaned_data
        nomeFazenda = cleaned_data.get('nomeFazenda')
        cidade = cleaned_data.get('cidade')
        estado = cleaned_data.get('estado')
        areaTotal = cleaned_data.get('areaTotal')
        areaAgricultavel = cleaned_data.get('areaAgricultavel')
        areaVegetacao = cleaned_data.get('areaVegetacao')

        if nomeFazenda == '':
            msg = ValidationError(
                'Nome da Fazenda não pode ficar em branco',
                code='invalid'
            )
            self.add_error('nomeFazenda', msg)

        if cidade == '':
            msg = ValidationError(
                'Nome da Cidade não pode ficar em branco',
                code='invalid'
            )
            self.add_error('cidade', msg)

        if estado == '':
            msg = ValidationError(
                'Nome do Estado não pode ficar em branco',
                code='invalid'
            )
            self.add_error('estado', msg)

        if areaTotal == '':
            msg = ValidationError(
                'É necessário entrar com algum valor de Área Total',
                code='invalid'
            )
            self.add_error('areaTotal', msg)

        if areaAgricultavel == '':
            msg = ValidationError(
                'É necessário entrar com algum valor de Área Agricultável',
                code='invalid'
            )
            self.add_error('areaAgricultavel', msg)

        if areaVegetacao == '':
            msg = ValidationError(
                'É necessário entrar com algum valor de Área de Vegetação',
                code='invalid'
            )
            self.add_error('areaAgricultavel', msg)

        if (areaAgricultavel + areaVegetacao) > areaTotal:
            msg = ValidationError(
                'A Área de uso do Solo (Área Agricultável + Área de Vegetação) não pode ser maior que a Área Total',
                code='invalid'
            )
            self.add_error('areaTotal', msg)

        return super().clean

    def clean_nomeFazenda(self):
        nomeFazenda = self.cleaned_data.get('nomeFazenda')

        if nomeFazenda == 'ABC':
            self.add_error(
                'nomeFazenda',
                ValidationError(
                    'Nome da Fazenda está Inválido',
                    code='invalid'
                )
            )

        return nomeFazenda

    def clean_cidade(self):
        cidade = self.cleaned_data.get('cidade')

        if cidade == 'ABC':
            self.add_error(
                'cidade',
                ValidationError(
                    'Nome da Cidade está Inválido',
                    code='invalid'
                )
            )
        return cidade

    def clean_estado(self):
        estado = self.cleaned_data.get('estado')

        if estado == 'AB':
            self.add_error(
                'estado',
                ValidationError(
                    'O Estado está Inválido',
                    code='invalid'
                )
            )
        return estado

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )

        return email

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Porfavor, adicione no mínimo 2 letras.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use a mesma senha de antes',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1
