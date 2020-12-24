from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError
import datetime


class NeomedAnalyzes_OPN(models.Model):
    _name = 'neomed.analyzes_opn'

    opn_id = fields.Many2one('neomed.opn', 'анализы')

    @api.onchange('WBC')
    def _function_of_WBC(self):
        if not self.WBC:
            return
        # elif self.WBC != float:
        #     raise ValidationError("Пожалуйста, при вводе дисятичных цифр в качестве разделителя пишите точку (.)")
        elif float(self.WBC) > 30:
            self.WBC = self.WBC + '↑'
        elif float(self.WBC) < 5:
            self.WBC = self.WBC + '↓'

    @api.onchange('RBC')
    def _function_of_RBC(self):
        if not self.RBC:
            return
        elif float(self.RBC) > 5.8:
            self.RBC = self.RBC + '↑'
        elif float(self.RBC) < 4.0:
            self.RBC = self.RBC + '↓'

    @api.onchange('HGB')
    def _function_of_HGB(self):
        if not self.HGB:
            return
        elif float(self.HGB) > 215:
            self.HGB = self.HGB + '↑'
        elif float(self.HGB) < 150:
            self.HGB = self.HGB + '↓'

    @api.onchange('HTC')
    def _function_of_HTC(self):
        if not self.HTC:
            return
        elif float(self.HTC) > 68:
            self.HTC = self.HTC + '↑'
        elif float(self.HTC) < 45:
            self.HTC = self.HTC + '↓'

    @api.onchange('GLU')
    def _function_of_GLU(self):
        if not self.GLU:
            return
        elif float(self.GLU) > 10:
            self.GLU = self.GLU + '↑'
        elif float(self.GLU) < 2.6:
            self.GLU = self.GLU + '↓'

    @api.onchange('PLT')
    def _function_of_PLT(self):
        if not self.PLT:
            return
        elif float(self.PLT) < 150:
            self.PLT = self.PLT + '↓'

    @api.onchange('BILO')
    def _function_of_BILO(self):
        if not self.BILO:
            return
        elif float(self.BILO) > 256:
            self.BILO = self.BILO + '↑'

    @api.onchange('BILT')
    def _get_default_BIL(self):
        if self.BILD != 0:
            bil_per1 = float(self.BILD) * 100 / (float(self.BILD) + float(self.BILT))
            if 100 - bil_per1 < 80:
                self.BILD = self.BILD + '↑'

    analyzes = [('OAK', 'ОАК'),
                ('BH', 'БХ крови(развернутая)'),
                ('GLU', 'сахар крови'), ('BH_sh', 'БХ крови(фракции)'),
                ('Nevr', 'Консультация невролога'),
                ('Ocul', 'Консультация окулиста'),
                ('Derm', 'Консультация дерматовенеролога'),
                ('OAM', 'ОАМ'),
                ('KSHS', 'КЩС'),
                ('USI', 'УЗИ ОБП, НСГ'),
                ('ECHO', 'ЭхоКГ'), ('Blood', 'Группа крови'),
                ('other', 'другое')]

    blood_gr = [('О(I) Rh (+) положительная', 'О(I) Rh (+) положительная'),
                ('О(I) Rh (-) отрицательная', 'О(I) Rh (-) отрицательная'),
                ('А(II) Rh (+) положительная', 'А(II) Rh (+) положительная'),
                ('А(II) Rh (-) отрицательная', 'А(II) Rh (-) отрицательная'),
                ('В(III) Rh (+) положительная', 'В(III) Rh (+) положительная'),
                ('В(III) Rh (-) отрицательная', 'В(III) Rh (-) отрицательная'),
                ('АВ(IV) Rh (+) положительная', 'АВ(IV) Rh (+) положительная'),
                ('АВ(IV) Rh (-) отрицательная', 'АВ(IV) Rh (-) отрицательная')]


    date = fields.Date(string='Дата', default=datetime.date.today())
    an_ez = fields.Selection(analyzes, string='Анализы/Консультации')
    WBC = fields.Char(string='Лейкоциты (109/л)')
    RBC = fields.Char(string='Эритроциты (1012/л)')
    HGB = fields.Char(string='Гемоглобин (г/л)')
    HTC = fields.Char(string='Гематокрит (%)')
    # MCV = fields.Char(string='Средний обьем эритроцита', default=' фл')
    # MCH = fields.Char(string='Среднее содержание гемоглобина', default=' пг')
    # MCHC = fields.Char(string='Средняя концентрация гемоглобина', default=' г/л')
    # RDW = fields.Char(string='Индекс распределения эритроцитов', default=' %')
    PLT = fields.Char(string='Тромбоциты (109/л)')
    NEU = fields.Char(string='Нейтрофилы (%)')
    LYM = fields.Char(string='Лимфоциты (%)')
    MON = fields.Char(string='Моноциты (%)')
    GLU = fields.Char(string='Сахар крови (ммоль/л)')
    NOTE = fields.Text(string='Дополнение')
    BILO = fields.Char(string='Билирубин общий (мколь/л)')
    BILD = fields.Char(string='Билирубин связанный (мколь/л)')
    BILT = fields.Char(string='Билирубин непрямой (мколь/л)')
    PROT = fields.Char(string='Общий белок (г/л)')
    ALB = fields.Char(string='Альбумины (г/л)')
    KREAT = fields.Char(string='Креатинин (мкмоль/л)')
    URO = fields.Char(string='Мочевина (ммоль/л)')
    K = fields.Char(string='Калий (ммоль/л)')
    Na = fields.Char(string='Натрий (ммоль/л)')
    ALT = fields.Char(string='АЛТ (Ед/л)')
    AST = fields.Char(string='АСТ (Ед/л)')
    CRB = fields.Char(string='СРБ (мг/л)')
    Cl = fields.Char(string='Cl (ммоль/л)')
    Ca = fields.Char(string='Кальций (ммоль/л)')
    Nevr = fields.Text(string=' ', default="Церебральная ишемия I ст, острый период, синдром угнетения ЦНС")
    Ocul = fields.Text(string=' ', default="Фоновая ангиопатия сетчатки")
    Derm = fields.Text(string=' ', default="Явка на сероконтроль через 3 мес в ГБУЗ РКВД")
    PH = fields.Char(string='pH ')
    p = fields.Char(string='p ')
    LEU = fields.Char(string='лей ')
    BEL = fields.Char(string='бел ')
    NITR = fields.Char(string='нитр ')
    PC02 = fields.Char(string='РсО2 ')
    P02 = fields.Char(string='РО2 ')
    lac = fields.Char(string='лактат ')
    BE = fields.Char(string='BE ')
    HCO3 = fields.Char(string='HCO3 ')
    USI = fields.Text(string="УЗИ", default='без патологии')
    ECHO = fields.Text(string="ЭхоКГ", default='ООО (  мм), ОАП (  мм)')
    time = fields.Char(string='Время')
    bl = fields.Selection(blood_gr, string='Группа крови')
    name_anal = fields.Char(string='Название анализа')
    other_anal = fields.Text(string="Параметры")

    analis = fields.Char(string='Результаты', compute='_function_result')

    def _function_result(self):
        for res in self:
            if res.an_ez == 'USI':
                res.analis = res.USI
            elif res.an_ez == 'ECHO':
                res.analis = res.ECHO
            elif res.an_ez == 'Derm':
                res.analis = res.Derm
            elif res.an_ez == 'Ocul':
                res.analis = res.Ocul
            elif res.an_ez == 'Nevr':
                res.analis = res.Nevr
            elif res.an_ez == 'Blood':
                res.analis = res.bl
            elif res.an_ez == 'OAK':
                res.analis = "WBC - %s, RBC - %s, HGB - %s, HTC - %s, PLT - %s, GLU - %s" % (
                res.WBC, res.RBC, res.HGB, res.HTC, res.PLT, res.GLU)
