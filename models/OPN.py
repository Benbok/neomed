from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError
import datetime



class Opn(models.Model):
    _name = 'neomed.opn'
    # _inherit = 'neomed.mothers'
    _description = 'Patients Record'

    mother_id = fields.Many2one('neomed.mothers', string='Номер истории', required=True)

    @api.multi
    def print_repair_Inspection_OPN(self):
        return self.env.ref('neomed.report_inspection_OPN').report_action(self)

    @api.multi
    def print_repair_Journal_OPN(self):
        return self.env.ref('neomed.report_patient_OPN').report_action(self)

    @api.multi
    def print_repair_Epicrisis_OPN(self):
        return self.env.ref('neomed.report_epicrises_OPN').report_action(self)


    histoty_number = fields.Char(string='Номер истории', related='mother_id.histoty_number')
    name = fields.Char(string='ФИО мамы', related='mother_id.name')
    birth_day = fields.Date(string='Дата рождения', related='mother_id.birth_day')
    birth_time = fields.Char(string='Время рождения', related='mother_id.birth_time')
    anamnez = fields.Text(string='Анамнез мамы', related='mother_id.anamnez')
    sex = fields.Selection(string='Пол ребенка', related='mother_id.sex')
    birth_namber = fields.Integer('Роды по счету', related='mother_id.birth_namber')
    pregnancy_namber = fields.Integer('Беременность по счету', related='mother_id.pregnancy_namber')
    severity = fields.Selection(string="Состояние при рождении", related='mother_id.severity')
    Apgar = fields.Char(string='Апгар', related='mother_id.Apgar')
    #
    massa_birth = fields.Integer(string='Масса при рождении', related='mother_id.massa_birth')
    height_birth = fields.Integer(string='Рост', related='mother_id.height_birth')
    OG_birth = fields.Integer(string='Окружность головы', related='mother_id.OG_birth')
    OGK_birth = fields.Integer(string='Окружность грудной клетки', related='mother_id.OGK_birth')
    # main = fields.Selection(diagnosis_main, string='Диагноз основной')
    # main_dop = fields.Char(string='Диагноз основной')
    GV = fields.Char(string='Гестационный возраст(недель)', related='mother_id.GV')
    Ak_ds = fields.Selection([('main1', 'Срочные роды в переднем виде затылочного предлежания '),
                              ('main2', 'Срочные быстрые роды в переднем виде затылочного предлежания '),
                              ('main3', 'Запоздалые быстрые роды в переднем виде затылочного предлежания '),
                              ('main4', 'Срочные индуцированные роды в переднем виде затылочного предлежания '),
                              ('main5', 'Срочные оперативные роды в головном предлежании '),
                              ('main6', 'Срочные оперативные роды в смешанно-ягодичном предлежании'),
                              ('main7', 'Срочные оперативные  роды в чисто ягодичном предлежании '),
                              ('main8', 'Поздние преждевременные роды в переднем виде затылочного предлежании '),
                              ('main9', 'Поздние преждевременные оперативные роды в головном предлежании '),
                              ('main10', 'Преждевременные роды в переднем виде затылочного предлежании '),
                              ('main11', 'другое ')],
                             string='Акушерский диагноз', related='mother_id.Ak_ds')
    Ak_ds_dop = fields.Char(string='Акушерский диагноз', related='mother_id.Ak_ds_dop')
    # main1 = fields.Selection([('Дыхательная недостаточность 1 ст', 'Дыхательная недостаточность 1 ст'),
    #                           ('Дыхательная недостаточность 2 ст', 'Дыхательная недостаточность 2 ст'),
    #                           ('Дыхательная недостаточность 3 ст', 'Дыхательная недостаточность 3 ст')],
    #                          string='Осложение основного')
    # main2 = fields.Char(string='Сопутствующий диагноз')
    #
    # birth_day_kid = fields.Date(string='Дата рождения')
    # severity_kid = fields.Selection([('satisfactory', 'удовлетворительное'),
    #                                  ('moderate_сondition', 'средней тяжести'),
    #                                  ('severe_condition', 'тяжелое')], string="Состояние при рождении")

    date_transfer_opn = fields.Date(string='Дата перевода в ОПН', related='mother_id.epicrisis_ids.date')
    DS_perevod1 = fields.Char(string='Диагноз основной', compute='_function_result_view')
    DS_perevod2 = fields.Char(string='Диагноз осложнение', compute='_function_result_view')
    DS_perevod3 = fields.Char(string='Диагноз сопутствующий', compute='_function_result_view')


    def _function_result_view(self):
        for res in self:
            for i in res.mother_id.journal_ids:
                if res.histoty_number == i.number and i.checkbox_OPN == True:
                    res.DS_perevod1 = i.main_view
                    res.DS_perevod2 = i.main1
                    res.DS_perevod3 = i.main_view2

    analyzes_ids = fields.One2many(related='mother_id.analyzes_ids', readonly=False)
    journal_opn_ids = fields.One2many('neomed.journal_opn', 'opn_id')
    inspection_opn_ids = fields.One2many('neomed.inspection_opn', 'opn_id')
    epicrisis_opn_ids = fields.One2many('neomed.epicrises_opn', 'opn_id')