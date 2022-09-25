from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['base_information'] = [
            "ФИО: Иожица Сергей Максимович",
            "Город: Москва",
            "Возраст: 15 лет",
            "Школа: ГБОУ Лицей №1580 при МГТУ им. Баумана",
            "Класс: 10",
            "Профиль класса: Информационно-Технический"
        ]
        kwargs['big_projects'] = [
            "FamilyCalendar (PyQt5, sqlite3)",
            "XDecy (Pygame)",
            "mint.edu (Flask, HTML, CSS)",
            "FactorioModInstaller (PyQt5, os, json)"
        ]
        kwargs['main_hobbies'] = [
            "Программирование",
            "Точные науки (физика, математика, информатика)"
        ]
        kwargs['code_experience'] = [
            '2 года в Яндекс.Лицее (с отличием)',
            '1 год в школе (Pascal)'
        ]
        context = super().get_context_data(**kwargs)
        return context
