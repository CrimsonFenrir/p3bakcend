from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Calificacion, CalificacionFactor
from decimal import Decimal
import datetime


class CalificacionModelTest(TestCase):
    def test_creacion_calificacion(self):
        cal = Calificacion.objects.create(
            instrumento="Bono",
            descripcion="Mercado local",
            fecha_pago=datetime.date.today(),
            valor_historico=Decimal("1000.00")
        )
        self.assertEqual(cal.instrumento, "Bono")
        self.assertEqual(cal.valor_historico, Decimal("1000.00"))


class CalificacionFactorModelTest(TestCase):
    def test_creacion_factor(self):
        cal = Calificacion.objects.create(
            instrumento="Acción",
            descripcion="Mercado internacional",
            valor_historico=Decimal("500.00")
        )
        factor = CalificacionFactor.objects.create(
            calificacion=cal,
            numero_factor=8,
            valor_factor=Decimal("0.12345678")
        )
        self.assertEqual(factor.numero_factor, 8)
        self.assertEqual(factor.valor_factor, Decimal("0.12345678"))


class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="juan", password="clave123")

    def test_login_exitoso(self):
        response = self.client.post(reverse("login"), {
            "username": "juan",
            "password": "clave123"
        })
        self.assertRedirects(response, reverse("lista_calificaciones"))

    def test_login_fallido(self):
        response = self.client.post(reverse("login"), {
            "username": "juan",
            "password": "incorrecta"
        })
        self.assertContains(response, "Usuario o contraseña incorrectos")


class CalificacionViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="juan", password="clave123")
        self.client.login(username="juan", password="clave123")

    def test_lista_calificaciones(self):
        response = self.client.get(reverse("lista_calificaciones"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "calificaciones_login.html")

    def test_api_calificaciones(self):
        Calificacion.objects.create(
            instrumento="ETF",
            descripcion="Mercado global",
            valor_historico=Decimal("200.00")
        )
        response = self.client.get(reverse("api_calificaciones"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
