from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError
import datetime



class Mothers(models.Model):
    _name = 'neomed.mothers'
    # _inherit = 'mail.thread'
    _description = 'Patients Record'
    _sql_constraints = [('histoty_number_unique', 'unique(histoty_number)', 'Такой номер истории уже существует!')]

    @api.multi
    def print_repair_Journal(self):
        return self.env.ref('neomed.report_patient').report_action(self)


    @api.multi
    def print_repair_Inspection(self):
        return self.env.ref('neomed.report_patient_ins').report_action(self)

    @api.multi
    def print_repair_Epicrisis(self):
        return self.env.ref('neomed.report_patient_exch').report_action(self)

    @api.onchange('main')
    def _get_default_gv(self):
        gv = self.GV
        if self.main == "main4":
            self.main_dop = str(gv) + " недель"

    diagnosis_main = [('Новорожденный из группы риска по перинатальной патологии',
                       'Новорожденный из группы риска по перинатальной патологии'),
                      ('Недоношенный новорожденный', 'Недоношенный новорожденный'),
                      ('Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС',
                       'Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС'),
                      ('Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС',
                       'Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС'),
                      ('Транзиторное тахипное новорожденного', 'Транзиторное тахипное новорожденного'),
                      ('Двусторонная кефалогематома', 'Двусторонная кефалогематома'),
                      ('Левотеменная кефалогематома', 'Левотеменная кефалогематома'),
                      ('Правотеменная кефалогематома', 'Правотеменная кефалогематома'),
                      ('Асфиксия средней тяжести при рождении', 'Асфиксия средней тяжести при рождении'),
                      ('Асфиксия тяжелая при рождении', 'Асфиксия тяжелая при рождении'),
                      ('Перинатальный контакт по В-20', 'Перинатальный контакт по В-20'),
                      ('Новорожденный от мамы с КСР (+)', 'Новорожденный от мамы с КСР (+)'),
                      ('Врожденная очаговая  пневмония, неуточненная, острое течение, средней тяжести',
                       'Врожденная очаговая  пневмония, неуточненная, острое течение, средней тяжести'),
                      ('main15', 'другой')]


    histoty_number = fields.Char(string='Номер истории')
    name = fields.Char(string='ФИО мамы', required=True)
    birth_day = fields.Date(string='Дата рождения', required=True)
    birth_time = fields.Char(string='Время рождения', required=True)
    anamnez = fields.Text(string='Анамнез мамы', required=True)
    sex = fields.Selection([
        ('male', 'мужской'),
        ('fermale', 'женский')], string='Пол ребенка')
    birth_namber = fields.Integer('Роды по счету')
    pregnancy_namber = fields.Integer('Беременность по счету')
    severity = fields.Selection([('удовлетворительное', 'удовлетворительное'), ('средней тяжести', 'средней тяжести'),
                                 ('тяжелое', 'тяжелое')], string="Состояние при рождении")
    Apgar = fields.Char(string='Апгар', required=True)

    massa_birth = fields.Integer(string='Масса при рождении', required=True)
    height_birth = fields.Integer(string='Рост')
    OG_birth = fields.Integer(string='Окружность головы')
    OGK_birth = fields.Integer(string='Окружность грудной клетки')
    main = fields.Selection(diagnosis_main, string='Диагноз основной')
    main_dop = fields.Char(string='Диагноз основной')
    GV = fields.Char(string='Гестационный возраст(недель)')
    Ak_ds = fields.Selection([('Срочные роды в переднем виде затылочного предлежания', 'Срочные роды в переднем виде затылочного предлежания'),
                             ('Срочные быстрые роды в переднем виде затылочного предлежания', 'Срочные быстрые роды в переднем виде затылочного предлежания'),
                             ('Запоздалые быстрые роды в переднем виде затылочного предлежания', 'Запоздалые быстрые роды в переднем виде затылочного предлежания'),
                             ('Срочные индуцированные роды в переднем виде затылочного предлежания', 'Срочные индуцированные роды в переднем виде затылочного предлежания'),
                             ('Срочные оперативные роды в головном предлежании', 'Срочные оперативные роды в головном предлежании'),
                             ('Срочные оперативные роды в смешанно-ягодичном предлежании', 'Срочные оперативные роды в смешанно-ягодичном предлежании'),
                             ('Срочные оперативные  роды в чисто ягодичном предлежании', 'Срочные оперативные  роды в чисто ягодичном предлежании'),
                              ('Поздние преждевременные роды в переднем виде затылочного предлежании', 'Поздние преждевременные роды в переднем виде затылочного предлежании'),
                             ('Поздние преждевременные оперативные роды в головном предлежании', 'Поздние преждевременные оперативные роды в головном предлежании'),
                              ('Преждевременные роды в переднем виде затылочного предлежании', 'Преждевременные роды в переднем виде затылочного предлежании'),
                              ('main11', 'другое')],
                            string='Акушерский диагноз')
    Ak_ds_dop = fields.Char(string='Акушерский диагноз')
    main1 = fields.Selection([('Дыхательная недостаточность 1 ст', 'Дыхательная недостаточность 1 ст'),
                              ('Дыхательная недостаточность 2 ст', 'Дыхательная недостаточность 2 ст'),
                              ('Дыхательная недостаточность 3 ст', 'Дыхательная недостаточность 3 ст')], string='Осложение основного')
    main2 = fields.Char(string='Сопутствующий диагноз')


    birth_day_kid = fields.Date(string='Дата рождения')
    severity_kid = fields.Selection([('satisfactory', 'удовлетворительное'),
                                     ('moderate_сondition', 'средней тяжести'),
                                     ('severe_condition', 'тяжелое')], string="Состояние при рождении")
    journal_ids = fields.One2many('neomed.journal', 'mother_id')
    analyzes_ids = fields.One2many('neomed.analyzes', 'mother_id')
    epicrisis_ids = fields.One2many('neomed.epicrisis', 'mother_id')
    inspection_ids = fields.One2many('neomed.inspection', 'mother_id')








