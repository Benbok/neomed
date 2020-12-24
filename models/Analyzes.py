from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError
import datetime


class NeomedAnalyzes(models.Model):

    _name = 'neomed.analyzes'

    number = fields.Char(string=' ', related='mother_id.histoty_number')


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
                ('ECHO', 'ЭхоКГ'),('Blood', 'Группа крови'),
                ('other', 'другое')]

    blood_gr = [('О(I) Rh (+) положительная','О(I) Rh (+) положительная'),
             ('О(I) Rh (-) отрицательная','О(I) Rh (-) отрицательная'),
             ('А(II) Rh (+) положительная','А(II) Rh (+) положительная'),
             ('А(II) Rh (-) отрицательная','А(II) Rh (-) отрицательная'),
             ('В(III) Rh (+) положительная','В(III) Rh (+) положительная'),
             ('В(III) Rh (-) отрицательная','В(III) Rh (-) отрицательная'),
             ('АВ(IV) Rh (+) положительная','АВ(IV) Rh (+) положительная'),
             ('АВ(IV) Rh (-) отрицательная','АВ(IV) Rh (-) отрицательная')]

    def _funct_time_check(self):
        for res in self:
            res.time_compute = res.time[:-3]


    mother_id = fields.Many2one('neomed.mothers', 'ФИО мамы')
    journal_id = fields.Many2one('neomed.journal', 'Анализы')
    sequence = fields.Integer(string='Sequence')

    time_compute = fields.Integer(string='Проверка времени', compute="_funct_time_check")
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
    USI = fields.Text(string="НСГ", default='без патологии')
    USI1 = fields.Text(string="УЗИ ОБП", default='без патологии')
    ECHO = fields.Text(string="ЭхоКГ", default='ООО (  мм), ОАП (  мм)')
    time = fields.Char(string='Время', default='10-00')
    bl = fields.Selection(blood_gr, string='Группа крови')
    name_anal = fields.Char(string='Название анализа')
    other_anal = fields.Text(string="Параметры")

    analis = fields.Char(string='Результаты', compute='_function_result')
    analis_name = fields.Char(string='Название анализа', compute='_function_result_anal')

    def _function_result(self):
        for res in self:
            if res.an_ez == 'USI':
                res.analis = 'НСГ - ' + res.USI + '\nУЗИ ОБП - ' + res.USI1
            elif res.an_ez == 'ECHO':
                res.analis = res.ECHO
            elif res.an_ez == 'GLU':
                res.analis = res.GLU + 'ммоль/л'
            elif res.an_ez == 'Derm':
                res.analis = res.Derm
            elif res.an_ez == 'Ocul':
                res.analis = res.Ocul
            elif res.an_ez == 'Nevr':
                res.analis = res.Nevr
            elif res.an_ez == 'Blood':
                res.analis = res.bl
            elif res.an_ez == 'KSHS':
                res.analis = "pH - %s, pO2 - %s, pCO2 - %s, lac - %s, BE - %s, HCO3 - %s, дополнительно - %s" % (res.PH,
                                                                                             res.P02, res.PC02,
                                                                                             res.lac, res.BE, res.HCO3, res.NOTE)
            elif res.an_ez == 'OAM':
                res.analis = "pH - %s, р - %s, лейк - %s, белок - %s, Нитраты - %s, дополнительно - %s" % (res.PH,
                                                                                             res.p, res.LEU,
                                                                                             res.BEL, res.NITR, res.NOTE)
            elif res.an_ez == 'other':
                res.analis = res.other_anal
            elif res.an_ez == 'BH_sh':
                res.analis = "Бил общий - %s мколь/л, бил связанный - %sмколь/л, СРБ - %s, дополнительно - %s" % (res.BILO, res.BILD, res.CRB, res.NOTE)
            elif res.an_ez == 'BH':
                res.analis = "Бил общий - %s мколь/л, бил связанный - %s мколь/л, СРБ - %s, дополнительно - %s" % (res.BILO, res.BILD, res.CRB, res.NOTE)
            elif res.an_ez == 'OAK':
                res.analis = "WBC - %s *10(9)/л, RBC - %s *12(9)/л, HGB - %s г/л, HTC - %s , PLT - %s *10(9), GLU - %s ммоль/л, дополнительно - %s" % (res.WBC, res.RBC, res.HGB, res.HTC, res.PLT, res.GLU, res.NOTE)

    def _function_result_anal(self):
        for res in self:
            if res.an_ez == 'other':
                res.analis_name = res.name_anal
            elif res.an_ez == 'OAK':
                res.analis_name = 'Общий клинический анализ крови'
            elif res.an_ez == 'OAM':
                res.analis_name = 'Общий клинический анализ мочи'
            elif res.an_ez == 'BH':
                res.analis_name = 'БХ крови развернутая'
            elif res.an_ez == 'GLU':
                res.analis_name = 'Сахар крови'
            elif res.an_ez == 'BH_sh':
                res.analis_name = 'БХ крови (фракции билирубина)'
            elif res.an_ez == 'Nevr':
                res.analis_name = 'Консультация невролога'
            elif res.an_ez == 'Ocul':
                res.analis_name = 'Консультация окулиста'
            elif res.an_ez == 'Derm':
                res.analis_name = 'Консультация дерматовенеролога'
            elif res.an_ez == 'KSHS':
                res.analis_name = 'Кислотно-щелочное состоние'
            elif res.an_ez == 'USI':
                res.analis_name = 'УЗИ ОБП, НСГ'
            elif res.an_ez == 'ECHO':
                res.analis_name = 'ЭхоКГ'
            elif res.an_ez == 'Blood':
                res.analis_name = 'Группа крови'