from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError
import datetime

class NeomedEpicrisis(models.Model):

    _name = 'neomed.epicrisis'




    @api.onchange('checkbox_HBV')
    def _get_default_HBV(self):
        if self.checkbox_HBV == True:
            self.HBV = self.mother_id.birth_day
            self.res_HBV = "доза 0,5 в/м   серия 228-1119  годен до 11.23 года"
        else:
            self.HBV = ""
            self.res_HBV = "отказ мамы"

    @api.onchange('checkbox_BCH')
    def _get_default_BCH(self):
        if self.checkbox_BCH == True:
            three_days = timedelta(3)
            self.BCH = self.mother_id.birth_day + three_days
            self.res_BCH = "доза 0,025  в/к  серия  661  годен до 04.21 г. г. Москва"
        else:
            self.BCH = ""
            self.res_BCH = "отказ мамы"

    @api.onchange('checkbox_N_scrin')
    def _get_default_N_scrin(self):
        if self.checkbox_N_scrin == True:
            four_days = timedelta(4)
            self.N_scrin = self.mother_id.birth_day + four_days
            self.res_N_scrin = "обследован"
        else:
            self.N_scrin = ""
            self.res_N_scrin = "не сделан (  )"

    @api.onchange('checkbox_A_scrin')
    def _get_default_A_scrin(self):
        if self.checkbox_A_scrin == True:
            three_days = timedelta(3)
            self.A_scrin = self.mother_id.birth_day + three_days
            self.res_A_scrin = "PASS прошел"
        else:
            self.A_scrin = ""
            self.res_A_scrin = "DON'T PASS "

    @api.onchange('checkbox_treat')
    def _get_default_treat(self):
        if self.checkbox_treat == True:
            self.treatm = self.treatm + "Антигеморрагическая терапия Sol.Vicasoli1 1% - " + str(round(self.mother_id.massa_birth / 10000, 2)) + "мл №1 в/м."
        elif self.checkbox_treat == False and self.checkbox_ARVT == True:
            self.treatm = "Совместное пребывание. Грудное вскармливание. " + "Сироп Ретровир по " + str(round(0.2 * self.mother_id.massa_birth/1000, 1)) + "мл по 4 р/сут: 06-00, 12-00, 18-00, 24-00. "
        else:
            self.treatm = "Совместное пребывание. Грудное вскармливание. "

    @api.onchange('checkbox_ARVT')
    def _get_default_ARVT(self):
        if self.checkbox_ARVT == True:
            self.treatm = self.treatm + "Сироп Ретровир по " + str(round(0.2 * self.mother_id.massa_birth/1000, 1)) + "мл по 4 р/сут: 06-00, 12-00, 18-00, 24-00 "
        elif self.checkbox_treat == True and self.checkbox_ARVT == False:
            self.treatm = "Совместное пребывание. Грудное вскармливание. " + "Антигеморрагическая терапия Sol.Vicasoli1 1% - " + str(round(self.mother_id.massa_birth / 10000, 2)) + "мл №1 в/м."
        else:
            self.treatm = "Совместное пребывание. Грудное вскармливание. "

    diagnosis_main = [('Новорожденный из группы риска по перинатальной патологии',
                       'Новорожденный из группы риска по перинатальной патологии'),
                      ('Здоровый новорожденный из группы риска по перинатальной патологии - Z03.8',
                       'Здоровый новорожденный из группы риска по перинатальной патологии  - Z03.8'),
                      ('Недоношенный новорожденный - Р07.3', 'Недоношенный новорожденный - Р07.3'),
                      ('Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС - P91.4',
                       'Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС - P91.4'),
                      ('Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС - P91.3',
                       'Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС - P91.3'),
                      ('Транзиторное тахипное новорожденного', 'Транзиторное тахипное новорожденного'),
                      ('Двусторонная кефалогематома - P12.0', 'Двусторонная кефалогематома - P12.0'),
                      ('Левотеменная кефалогематома - P12.0', 'Левотеменная кефалогематома - P12.0'),
                      ('Правотеменная кефалогематома - P12.0', 'Правотеменная кефалогематома - P12.0'),
                      ('Неонатальная желтуха, неуточненная - Р59.9', 'Неонатальная желтуха, неуточненная - Р59.9'),
                      ('Новорожденный от мамы с КСР (+)', 'Новорожденный от мамы с КСР (+)'),
                      ('Здоровый новорожденный от мамы с КСР (+) - Z00.1',
                       'Здоровый новорожденный от мамы с КСР (+) - Z00.1'),
                      ('Врожденная очаговая  пневмония, неуточненная, острое течение, средней тяжести',
                       'Врожденная очаговая  пневмония, неуточненная, острое течение, средней тяжести'),
                      ('main15', 'другой')]

    diagnosis_main2 = [('Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС',
                        'Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС'),
                       ('Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС',
                        'Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС'),
                       ('Недоношенный новорожденный', 'Недоношенный новорожденный'),
                       ('«Маловесный» для гестационного возраста новорожденный',
                        '«Маловесный» для гестационного возраста новорожденный'),
                       ('Малый размер новорожденного для гестационного возраста',
                        'Малый размер новорожденного для гестационного возраста'),
                       ('Крупный новорожденный', 'Крупный новорожденный'),
                       ('Чрезмерно крупный новорожденный', 'Чрезмерно крупный новорожденный'),
                       ('Двусторонная кефалогематома', 'Двусторонная кефалогематома'),
                       ('Левотеменная кефалогематома', 'Левотеменная кефалогематома'),
                       ('Правотеменная кефалогематома', 'Правотеменная кефалогематома'),
                       ('Первый ребенок из двойни', 'Первый ребенок из двойни'),
                       ('Второй ребенок из двойни', 'Второй ребенок из двойни'),
                       ('ВПС - дефект межжелудочковой перегородки', 'ВПС - дефект межжелудочковой перегородки'),
                       ('Перинатальный контакт по В-20', 'Перинатальный контакт по В-20'),
                       ('Перивентрикулярное кровоизлияние 1 степени', 'Перивентрикулярное кровоизлияние 1 степени'),
                       ('Внутрижелудочковое кровоизлияние 1 степени', 'Внутрижелудочковое кровоизлияние 1 степени'),
                       ('Внутрижелудочковое кровоизлияние 2 степени', 'Внутрижелудочковое кровоизлияние 2 степени'),
                       ('Внутрижелудочковое кровоизлияние 3 степени', 'Внутрижелудочковое кровоизлияние 3 степени'),
                       ('Межпредсердное сообщение', 'Межпредсердное сообщение'),
                       ('main15', 'другой')]

    doc = [("Костромин А.В.", "Костромин А.В."),
           ("Сулейманова И.Д.", "Сулейманова И.Д."),
           ("Хамматшина А.Р.", "Хамматшина А.Р."),
           ("Арсланова Ф.Р.", "Арсланова Ф.Р."),
           ("Первов Р.Г.", "Первов Р.Г."),
           ("Шумадалова А.В.", "Шумадалова А.В."),
           ("Аюпов Р.Ш.", "Аюпов Р.Ш."),
           ("Толпаков Х.Ф.", "Толпаков Х.Ф."),
           ("Вильданова А.И.", "Вильданова А.И."),
           ("Раева А.А.", "Раева А.А."),
           ("Зарипова А.Р.", "Зарипова А.Р."),
           ("Ганеева Э.К.", "Ганеева Э.К."),
           ("Идрисова А.Ф.", "Идрисова А.Ф.")]


    @api.onchange('checkbox_nevr', "checkbox_card",
                  "checkbox_nurt", "checkbox_gastr",
                  "checkbox_ARVT1", "checkbox_mass",
                  "checkbox_ARVT")

    def _get_default_checkbox_nevr(self):
        nablud = "Наблюдение участкового педиатра"
        vscarm = "\nГрудное вскармливание \n"
        tualet = "Туалет пупочной ранки/пуповинного остатка раствором бриллиантовой зелени \n" \
                 "Ежедневные прогулки и водные процедуры \n"
        card = ", кардиолога"
        card1 = " ЭхоКГ"
        nevr = ", невролога"
        nevr1 = " НСГ"
        gastr = ", гастроэнтеролога"
        gastr1 = " УЗИ ОБП"
        urlo = ", уролога"
        urlo1 = " УЗИ ОБП и забрюшинного пространства"

        if self.checkbox_card == True:
            self.rec = "Наблюдение участкового педиатра, кардиолога   \n" \
                "Грудное вскармливание \n" \
                "Туалет пупочной ранки/пуповинного остатка раствором бриллиантовой зелени \n" \
                "Ежедневные прогулки и водные процедуры \n" \
                "Повторное ЭхоКГ в 1 мес по месту жительства в Д/П"

        if self.checkbox_nevr == True:
            self.rec = nablud + card + nevr + vscarm + tualet + \
                       "Повторное " + nevr1 + card1 + " в 1 мес по месту жительства в Д/П"

        elif self.checkbox_card == True and self.checkbox_nevr == True:
            self.rec = nablud + card + nevr + vscarm + tualet + \
                       "Повторное " + nevr1 + card1 + " в 1 мес по месту жительства в Д/П"

        elif self.checkbox_nevr == True and self.checkbox_gastr == True:
            self.rec = nablud + gastr + nevr + vscarm + tualet + \
                       "Повторное " + nevr1 + gastr1 + " в 1 мес по месту жительства в Д/П"

        elif self.checkbox_ARVT1 == True:
            self.rec = nablud + urlo + vscarm +tualet + \
                       "Повторное " + urlo1 + " в 1 мес по месту жительства в Д/П"

        elif self.checkbox_nevr == True:
            # self.rec =  (self.rec).format(невролог="невролога")
            self.rec = nablud + nevr + vscarm + tualet + \
                       "Повторное " + nevr1 + " в 1 мес по месту жительства в Д/П"

        elif self.checkbox_card == True:
            self.rec = nablud + card + vscarm + tualet + \
                       "Повторное " + card1 + " в 1 мес по месту жительства в Д/П"


        elif self.checkbox_gastr == True:
            self.rec = nablud + gastr + vscarm + tualet + \
                       "Повторное " + gastr1 + " в 1 мес по месту жительства в Д/П"

        elif self.checkbox_nurt == True:
            self.rec = nablud + "\nИскусственное вскармливание\n" + tualet

        elif self.checkbox_ARVT == True:
            self.rec = nablud + "\nИскусственное вскармливание \n" + tualet + \
                       "Сироп Ретровир по 0,7 мл по 4 р/сут: 06-00, 12-00, 18-00, 24-00 1 месяц. Дозу Ретровира перерасчитывают при изменении массы тела ребенка на 10%: вес ребенка х 0,2. \n" \
                        "Наблюдение в центре СПИД. БЦЖ «М» - мед отвод до снятия с учета по ВИЧ инфекции "

        elif self.checkbox_mass == True:
            self.rec =self.rec = nablud + vscarm + tualet + \
                       "Повторное " + nevr1 + gastr1 + " в 1 мес по месту жительства в Д/П" +\
                        "\nРасчет питания калорийным методом до 10 суток жизни: 100-110 ккал*кг*100/68(кал смеси), с 10 сут обьемным методом: до 2 мес-1/5 массы, с 2- 4 мес-1/6 массы \n" \
                                  "Взвешивание каждый день до 1 мес жизни"

        else:
            self.rec = self.rec = nablud + vscarm + tualet

    @api.onchange('checkbox_discharge')
    def _get_default_checkbox_discharge(self):
        if self.checkbox_discharge == True:
            three_days = timedelta(4)
            date_discharge = self.mother_id.birth_day + three_days
            self.discharge = "Учитывая  раннюю  выписку из  род дома на 3 сутки, согласна приехать в род дом для  взятия анализа  на  неонатальный  скрининг моему  ребенку " + str(date_discharge) + \
                             " (приказ  № 185 'О массовом обследовании новорожденных детей  на  наследственные  заболевания') \n" \
                             "                                                                                                          Подпись мамы"
        else:
            self.discharge = " "


    checkbox_nevr = fields.Boolean(default=False, )
    checkbox_mass = fields.Boolean(default=False, )
    checkbox_card = fields.Boolean(default=False, )
    checkbox_gastr = fields.Boolean(default=False, )
    checkbox_nurt = fields.Boolean(default=False, )
    checkbox_ARVT1 = fields.Boolean(default=False, )
    checkbox_discharge = fields.Boolean(default=False, )

    checkbox_N_scrin = fields.Boolean('Сделан ли скрининг', default=True, )
    checkbox_A_scrin = fields.Boolean('Сделан ли скрининг', default=True, )
    checkbox_HBV = fields.Boolean('Проведена ли вакцинация', default=True, )
    checkbox_BCH = fields.Boolean('Проведена ли вакцинация', default=True, )

    checkbox_treat = fields.Boolean(string='Антигеморрагичесая терапия', default=False, )
    checkbox_ARVT = fields.Boolean(default=False, )

    mother_id = fields.Many2one('neomed.mothers', 'ФИО мамы')
    date = fields.Date(string='Дата', default=datetime.date.today())
    select = [('excharge', 'выписка'),
              ('transferable_OPN', 'перводной ОПН'),
              ('transferable_GKB', 'перевод в ГКБ №17 / РДКБ')]

    gr_health = [('A', '1'),
              ('B', '2А'),
              ('C', '2Б'),
                 ('D', '3'),
                 ('E', '4'),
                 ('F', '5')]

    blood_gr = [('О(I) Rh (+) положительная', 'О(I) Rh (+) положительная'),
                ('О(I) Rh (-) отрицательная', 'О(I) Rh (-) отрицательная'),
                ('А(II) Rh (+) положительная', 'А(II) Rh (+) положительная'),
                ('А(II) Rh (-) отрицательная', 'А(II) Rh (-) отрицательная'),
                ('В(III) Rh (+) положительная', 'В(III) Rh (+) положительная'),
                ('В(III) Rh (-) отрицательная', 'В(III) Rh (-) отрицательная'),
                ('АВ(IV) Rh (+) положительная', 'АВ(IV) Rh (+) положительная'),
                ('АВ(IV) Rh (-) отрицательная', 'АВ(IV) Rh (-) отрицательная')]



    excharge = fields.Selection(select, string='Тип документа')
    mother_age = fields.Char(string='Возраст мамы')
    address = fields.Char(string='Адрес проживания')
    N_scrin  = fields.Date(string='Неонатальный скрининг')
    A_scrin = fields.Date(string='Аудиологический скрининг')
    res_N_scrin = fields.Char(string=' ', default="сделан")
    res_A_scrin = fields.Char(string=' ', default="PASS прошел")
    BCH = fields.Date(string='БЦЖ «М»')
    res_BCH = fields.Char(string=' ', default="доза 0,025  в/к  серия  661  годен до 04.21г. г. Москва")
    HBV = fields.Date(string='ВПГ «В» ')
    res_HBV = fields.Char(string=' ', default="доза 0,5 в/м   серия 228-1119  годен до 11.23 года")
    treatm = fields.Text(string=' ', default="Совместное пребывание.  Грудное вскармливание. ")
    gr_health_sel = fields.Selection(gr_health, string='Группа здоровья', default="B")
    risk = fields.Char(string='Группа направленного риска', default="1,2,3")
    text_exch = fields.Text(string='Текст дневника')

    main = fields.Selection(diagnosis_main, string='Диагноз основной')
    main1 = fields.Char(string='Осложение основного')
    main2 = fields.Selection(diagnosis_main2, string='Сопутствующий диагноз')

    rec = fields.Text(string='Рекомендации', default="Наблюдение участкового педиатра \n" 
                                                        "Грудное вскармливание \n"
                                                        "Туалет пупочной ранки/пуповинного остатка раствором бриллиантовой зелени \n"
                                                        "Ежедневные прогулки и водные процедуры \n")
    main_otdel = fields.Char(string='Заведующий отделением', default="Хамматшина А.Р.")
    doc_otdel = fields.Selection(doc, string='Врач')

    dop1 = fields.Char(string=' ')
    dop2 = fields.Char(string=' ')

    blood_mother = fields.Selection(blood_gr, string='Группа крови мамы')
    discharge = fields.Text(string=' ')

    @api.onchange('select', 'date')
    def diagnoz(self):
        journal = self.mother_id.journal_ids
        for rec in journal:
            if self.number == rec.number and rec.checkbox_home == True:
                if rec.day_nomber == '3-е сутки':
                    self.main = rec.main
                    self.main1 = rec.main1
                    self.main2 = rec.main2
                    self.dop1 = rec.dop1
                    self.dop2 = rec.dop2
            if self.number == rec.number and rec.checkbox_OPN == True:
                self.main = rec.main
                self.main1 = rec.main1
                self.main2 = rec.main2
                self.dop1 = rec.dop1
                self.dop2 = rec.dop2


    # _____________________________Переводной в ОПН___________________________

    # @api.multi
    # def print_repair_OPN(self):
    #     return self.env.ref('neomed.report_patient_send').report_action(self)
    def _funct_time_check(self):
        for res in self:
            res.time_compute = res.time[:-3]

    def _funct_time(self):
        modelObj = self.env['neomed.journal']
        for day in modelObj.search([('number', '=', self.number), ('checkbox_OPN', '=', True)]):
            self.time = day.time

    time_compute = fields.Integer(string='Проверка времени', compute="_funct_time_check")
    time = fields.Text(string=' Время перевода', compute="_funct_time")

    checkbox_dop_note = fields.Boolean(default=False, )

    dateOPN = fields.Date(string='Дата', default=datetime.date.today())
    RW = fields.Text(string='Анализы мамы', default="RW - , ВИЧ - , HbsAg, ВГС - .\nПаритет:\n")
    anamnez = fields.Text(string='Анамнез мамы')
    check = fields.Text(string='На учете', default="состояла")
    analyzes_ids = fields.One2many(related='mother_id.analyzes_ids', readonly=False)



    @api.onchange('excharge')
    def dnevniki_OPN(self):
        for r in self:
            self.dnevniki = """Состояние при рождении: """
            self.obosn_diag = "На основании анамнеза, лабораторных данных и данных дополнительных методов исследования выставлен предварительный диагноз:"
            modelObj = self.env['neomed.journal']
            perevod = self.excharge
            ak_ds_osn = self.mother_id.Ak_ds

            if ak_ds_osn != 'main11':
                ak_ds = self.mother_id.Ak_ds + ' {} недель ГВ'.format(self.mother_id.GV)
            elif ak_ds_osn == 'main11':
                ak_ds = self.mother_id.Ak_ds_dop + ' {} недель ГВ'.format(self.mother_id.GV)


            for day in modelObj.search([('number', '=', r.number), ('checkbox_OPN', '=', True)]):
                sevirity = 'средней тяжести'
                dop_DS = ""
                DS_main = day.main

                dop_DS_sop = ""
                DS_main2 = day.main2
                if day.sevir == "main3":
                    sevirity = 'тяжелое'

                if day.main == "main15":
                    dop_DS = day.dop1
                    DS_main = ""
                if day.main2 == "main15":
                    dop_DS_sop = day.dop2
                    DS_main2 = ""

                main = ''
                main1 = self.mother_id.main1
                main2 = self.mother_id.main2
                if self.mother_id.main != 'main15':
                    main = self.mother_id.main
                else:
                    main = self.mother_id.main_dop


                if perevod == 'transferable_OPN':
                    self.dnevniki = self.dnevniki + " %s. Крик %s. Поза %s. Мышечный тонус %s. Рефлексы новорожденного %s. Большой родничок %s. " \
                                                    "Головка %s. Кожные покровы %s. \nSt.locali %s\n\n" \
                                                    "Состояние на момент перевода ребенка в ОПН роддома №3( %s )\n" \
                                                    "ЧСС %s/мин    ЧД %s/мин    t %s\n" \
                                                    "%s\n\n" \
                                                    "Результаты обследований:" % \
                                    (self.mother_id.severity, self.mother_id.inspection_ids.scream,
                                     self.mother_id.inspection_ids.posa, self.mother_id.inspection_ids.tonus,
                                     self.mother_id.inspection_ids.nerv, self.mother_id.inspection_ids.rodnich,
                                     self.mother_id.inspection_ids.head,
                                     self.mother_id.inspection_ids.skin, self.mother_id.inspection_ids.local,

                                     day.day_nomber, day.ChSS, day.ChD, day.C,
                                     day.text)
                    self.anamnez = 'На учете в ж/к - \nТечение беременности на фоне: {}' \
                                   '\nОколоплодные воды: - \n' \
                                   'Акушерский диагноз:\n' \
                                   'Осн: {}\n' \
                                   'Осл: \n' \
                                   'Соп: \n' \
                                   'Предварительный диагноз новорожденного при рождении:\n' \
                                   'Осн: {}\n' \
                                   'Осл: {}\n' \
                                   'Соп: {}'.format(self.mother_id.anamnez, ak_ds, main, main1, main2)

                    self.obosn_diag = self.obosn_diag + '\n' \
                                                        'Осн.: %s%s\n' \
                                                        'Осл.: %s\n' \
                                                        'Соп.: %s%s\n\n' \
                                                        'Переводится в ЛПУ_ ОПН р/д №3\n' \
                                                        'Дата перевода %s   %s' % (
                                          DS_main, dop_DS, day.main1, DS_main2, dop_DS_sop, day.date, day.time)


                elif perevod == 'transferable_GKB':
                    self.dnevniki = self.dnevniki + " %s. Крик %s. Поза %s. Мышечный тонус %s. Рефлексы новорожденного %s. Большой родничок %s. " \
                                                    "Головка %s. Кожные покровы %s. \nSt.locali %s\n\n" \
                                                    "Состояние на момент перевода ребенка( %s )\n" \
                                                    "ЧСС %s/мин    ЧД %s/мин    t %s\n" \
                                                    "%s\n\n" \
                                                    "Результаты обследований:" % \
                                    (self.mother_id.severity, self.mother_id.inspection_ids.scream,
                                     self.mother_id.inspection_ids.posa, self.mother_id.inspection_ids.tonus,
                                     self.mother_id.inspection_ids.nerv, self.mother_id.inspection_ids.rodnich,
                                     self.mother_id.inspection_ids.head,
                                     self.mother_id.inspection_ids.skin, self.mother_id.inspection_ids.local,

                                     day.day_nomber, day.ChSS, day.ChD, day.C,
                                     day.text)
                    self.anamnez = 'На учете в ж/к - \nТечение беременности на фоне: {}' \
                                   '\nОколоплодные воды: - \n' \
                                   'Акушерский диагноз:\n' \
                                   'Осн: {}\n' \
                                   'Осл: \n' \
                                   'Соп: \n' \
                                   'Предварительный диагноз новорожденного при рождении:\n' \
                                   'Осн: {}\n' \
                                   'Осл: {}\n' \
                                   'Соп: {}'.format(self.mother_id.anamnez, ak_ds, main, main1, main2)

                    self.obosn_perevod = 'Масса тела  %s гр         Сутки жизни (%s)' \
                                         '\n' \
                                         'Осн.: %s%s\n' \
                                         'Осл.: %s\n' \
                                         'Соп.: %s%s\n\n' \
                                         'Переводится в ОПН ГДКБ №17 по договоренности с зав.отделением\n' \
                                         'Согласие матери на перевод_______________подпись_________________тел:___________________ \n' \
                                         'Дата перевода %s   %s'\
                                         % (day.mass, day.day_nomber, DS_main, dop_DS, day.main1, DS_main2, dop_DS_sop, day.date, day.time)

                    self.treatm_perevod = "Детское отделение с %s по %s\n"\
                                          "с %s лечебно-охранительный режим отделения мать и дитя \n"\
                                          "с %s -  грудное вскармливание " \
                                          % (day.mother_id.birth_day, day.date, day.mother_id.birth_day, day.mother_id.birth_day)


    number = fields.Char(string=' ', related='mother_id.histoty_number')
    dnevniki = fields.Text(string='Остальное')
    obosn_diag = fields.Text(string='Обоснование')


    # _____________________________Переводной в ОПН ГКБ №17  /   РДКБ___________________________


    obosn_perevod = fields.Text(string='Остальное переводной')
    treatm_perevod = fields.Text(string='Проведенное лечение')



    @api.onchange('select', 'date')
    def def_exchage(self):
        journal = self.mother_id.journal_ids
        day = self.date - self.mother_id.birth_day
        pol = self.mother_id.sex
        gv = self.mother_id.GV
        sex = self.mother_id.sex
        massa = self.mother_id.massa_birth
        rost = self.mother_id.height_birth
        OG = self.mother_id.OG_birth

        pol_dnevnik = ''
        if pol == 'male':
            pol_dnevnik = "мужской"
        else:
            pol_dnevnik = "женский"

        if sex == 'male':
            # Мальчик 42 нед
            L_mas42 = list(range(3250, 3401))
            N_mas42 = list(range(3401, 4701))
            H_mas42 = list(range(4701, 5051))

            L_rost42 = list(range(49, 51))
            N_rost42 = list(range(51, 57))
            H_rost42 = list(range(57, 59))

            # Мальчик 41 нед
            L_mas41 = list(range(2950, 3201))
            N_mas41 = list(range(3201, 4451))
            H_mas41 = list(range(4451, 4801))

            L_rost41 = list(range(48, 50))
            N_rost41 = list(range(50, 55))
            H_rost41 = list(range(55, 57))

            # Мальчик 40 нед
            L_mas40 = list(range(2750, 3000))
            N_mas40 = list(range(3000, 4201))
            H_mas40 = list(range(4201, 4500))

            L_rost40 = list(range(47, 49))
            N_rost40 = list(range(49, 55))
            H_rost40 = list(range(55, 57))

            # Мальчик 39 нед
            L_mas39 = list(range(2550, 2800))
            N_mas39 = list(range(2800, 4001))
            H_mas39 = list(range(4001, 4301))

            L_rost39 = list(range(46, 48))
            N_rost39 = list(range(48, 54))
            H_rost39 = list(range(54, 56))

            # Мальчик 38 нед
            L_mas38 = list(range(2349, 2600))
            N_mas38 = list(range(2600, 3750))
            H_mas38 = list(range(3750, 4051))

            L_rost38 = list(range(45, 47))
            N_rost38 = list(range(47, 54))
            H_rost38 = list(range(54, 55))

            # Мальчик 37 нед
            L_mas37 = list(range(2150, 2401))
            N_mas37 = list(range(2401, 3551))
            H_mas37 = list(range(3551, 3851))

            L_rost37 = list(range(44, 46))
            N_rost37 = list(range(46, 52))
            H_rost37 = list(range(52, 54))

        else:
            # ------------------ДЕВОЧКИ------------------------
            # Девочка 42 нед
            L_mas42 = list(range(2900, 3150))
            N_mas42 = list(range(3150, 4500))
            H_mas42 = list(range(4500, 4900))

            L_rost42 = list(range(47, 49))
            N_rost42 = list(range(49, 54))
            H_rost42 = list(range(54, 56))

            # Девочка 41 нед
            L_mas41 = list(range(2750, 3000))
            N_mas41 = list(range(3000, 4300))
            H_mas41 = list(range(4300, 4700))

            L_rost41 = list(range(47, 49))
            N_rost41 = list(range(49, 54))
            H_rost41 = list(range(54, 56))

            # Девочка 40 нед
            L_mas40 = list(range(2600, 2850))
            N_mas40 = list(range(2850, 4100))
            H_mas40 = list(range(4100, 4500))

            L_rost40 = list(range(46, 47))
            N_rost40 = list(range(47, 53))
            H_rost40 = list(range(53, 55))

            # Девочка 39 нед
            L_mas39 = list(range(2400, 2650))
            N_mas39 = list(range(2650, 3900))
            H_mas39 = list(range(3900, 4250))

            L_rost39 = list(range(45, 46))
            N_rost39 = list(range(46, 52))
            H_rost39 = list(range(52, 54))

            # Девочка 38 нед
            L_mas38 = list(range(2250, 2500))
            N_mas38 = list(range(2500, 3700))
            H_mas38 = list(range(3700, 4050))

            L_rost38 = list(range(44, 45))
            N_rost38 = list(range(45, 52))
            H_rost38 = list(range(52, 53))

            # Девочка 37 нед
            L_mas37 = list(range(2050, 2300))
            N_mas37 = list(range(2300, 3500))
            H_mas37 = list(range(3500, 3800))

            L_rost37 = list(range(43, 44))
            N_rost37 = list(range(44, 51))
            H_rost37 = list(range(51, 52))

        phys_ras = ''
        # --------------Оцениваем физическое развитие 42 недель -------------------------
        if gv == '42':
            if massa in N_mas42 and rost in N_rost42:
                phys_ras = " гармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 10-90)'

            elif massa in H_mas42 and rost in N_rost42:
                phys_ras = " дисгармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 10-90)'

            elif massa > H_mas42[-1] and rost in N_rost42:
                phys_ras = " резко дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 10-90)'

            elif massa > H_mas42[-1] and rost in H_rost42:
                phys_ras = " дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 90-97)'

            elif massa in H_mas42 and rost in H_rost42:
                phys_ras = " гармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 90-97)'

            elif massa > H_mas42[-1] and rost > H_rost42[-1]:
                phys_ras = " гармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL > 97)'

            elif massa in N_mas42 and rost in H_rost42:
                phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 90-97)'

            elif massa in N_mas42 and rost > H_rost42[-1]:
                phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL > 97)'

            # ______________Оценка звур по гипотрофическому типу______________
            elif massa in L_mas42 and rost in N_rost42:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'

            elif massa < L_mas42[0] and rost in N_rost42:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'

            # ______________Оценка звур по гипопластическому типу______________
            elif massa < L_mas42[0] and rost in L_rost42:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM > 3, pL = 3-10)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
            else:
                phys_ras = "Требуется провести самостоятельный расчет"

        # --------------Оцениваем физическое развитие 41 недель -------------------------
        elif gv == '41':
            if massa in N_mas41 and rost in N_rost41:
                phys_ras = " гармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 10-90)'

            elif massa in H_mas41 and rost in N_rost41:
                phys_ras = " дисгармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 10-90)'

            elif massa > H_mas41[-1] and rost in N_rost41:
                phys_ras = " резко дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 10-90)'

            elif massa > H_mas41[-1] and rost in H_rost41:
                phys_ras = " дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 90-97)'

            elif massa in H_mas41 and rost in H_rost41:
                phys_ras = " гармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 90-97)'

            elif massa > H_mas41[-1] and rost > H_rost41[-1]:
                phys_ras = " гармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL > 97)'

            elif massa in N_mas41 and rost in H_rost41:
                phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 90-97)'

            elif massa in N_mas41 and rost > H_rost41[-1]:
                phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL > 97)'

            # ______________Оценка звур по гипотрофическому типу______________
            elif massa in L_mas41 and rost in N_rost41:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'

            elif massa < L_mas41[0] and rost in N_rost41:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'

            # ______________Оценка звур по гипопластическому типу______________
            elif massa < L_mas41[0] and rost in L_rost41:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM > 3, pL = 3-10)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
            else:
                phys_ras = "Требуется провести самостоятельный расчет"

        # --------------Оцениваем физическое развитие 40 недель -------------------------
        elif gv == '40':
            if massa in N_mas40 and rost in N_rost40:
                phys_ras = " гармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 10-90)'

            elif massa in H_mas40 and rost in N_rost40:
                phys_ras = " дисгармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 10-90)'

            elif massa > H_mas40[-1] and rost in N_rost40:
                phys_ras = " резко дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 10-90)'

            elif massa > H_mas40[-1] and rost in H_rost40:
                phys_ras = " дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 90-97)'

            elif massa in H_mas40 and rost in H_rost40:
                phys_ras = " гармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 90-97)'

            elif massa > H_mas40[-1] and rost > H_rost40[-1]:
                phys_ras = " гармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL > 97)'

            elif massa in N_mas40 and rost in H_rost40:
                phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 90-97)'

            elif massa in N_mas40 and rost > H_rost40[-1]:
                phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL > 97)'

            # ______________Оценка звур по гипотрофическому типу______________
            elif massa in L_mas40 and rost in N_rost40:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'

            elif massa < L_mas40[0] and rost in N_rost40:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'

            # ______________Оценка звур по гипопластическому типу______________
            elif massa < L_mas40[0] and rost in L_rost40:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM > 3, pL = 3-10)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
            else:
                phys_ras = "Требуется провести самостоятельный расчет"

        # --------------Оцениваем физическое развитие 39 недель -------------------------
        elif gv == '39':
            if massa in N_mas39 and rost in N_rost39:
                phys_ras = " гармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 10-90)'

            elif massa in H_mas39 and rost in N_rost39:
                phys_ras = " дисгармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 10-90)'

            elif massa > H_mas39[-1] and rost in N_rost39:
                phys_ras = " резко дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 10-90)'

            elif massa > H_mas39[-1] and rost in H_rost39:
                phys_ras = " дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 90-97)'

            elif massa in H_mas39 and rost in H_rost39:
                phys_ras = " гармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 90-97)'

            elif massa > H_mas39[-1] and rost > H_rost39[-1]:
                phys_ras = " гармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL > 97)'

            elif massa in N_mas39 and rost in H_rost39:
                phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 90-97)'

            elif massa in N_mas39 and rost > H_rost39[-1]:
                phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL > 97)'

            # ______________Оценка звур по гипотрофическому типу______________
            elif massa in L_mas39 and rost in N_rost39:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'

            elif massa < L_mas39[0] and rost in N_rost39:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'

            # ______________Оценка звур по гипопластическому типу______________
            elif massa < L_mas39[0] and rost in L_rost39:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM > 3, pL = 3-10)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
            else:
                phys_ras = "Требуется провести самостоятельный расчет"

        # --------------Оцениваем физическое развитие 38 недель -------------------------
        elif gv == '38':
            if massa in N_mas38 and rost in N_rost38:
                phys_ras = " гармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 10-90)'

            elif massa in H_mas38 and rost in N_rost38:
                phys_ras = " дисгармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 10-90)'

            elif massa > H_mas38[-1] and rost in N_rost38:
                phys_ras = " резко дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 10-90)'

            elif massa > H_mas38[-1] and rost in H_rost38:
                phys_ras = " дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 90-97)'

            elif massa in H_mas38 and rost in H_rost38:
                phys_ras = " гармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 90-97)'

            elif massa > H_mas38[-1] and rost > H_rost38[-1]:
                phys_ras = " гармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL > 97)'

            elif massa in N_mas38 and rost in H_rost38:
                phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 90-97)'

            elif massa in N_mas38 and rost > H_rost38[-1]:
                phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL > 97)'

            # ______________Оценка звур по гипотрофическому типу______________
            elif massa in L_mas38 and rost in N_rost38:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'

            elif massa < L_mas38[0] and rost in N_rost38:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'

            # ______________Оценка звур по гипопластическому типу______________
            elif massa < L_mas38[0] and rost in L_rost38:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM > 3, pL = 3-10)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
            else:
                phys_ras = "Требуется провести самостоятельный расчет"

        # --------------Оцениваем физическое развитие 37 недель -------------------------
        elif gv == '37':
            if massa in N_mas37 and rost in N_rost37:
                phys_ras = " гармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 10-90)'

            elif massa in H_mas37 and rost in N_rost37:
                phys_ras = " дисгармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 10-90)'

            elif massa > H_mas37[-1] and rost in N_rost37:
                phys_ras = " резко дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 10-90)'

            elif massa > H_mas37[-1] and rost in H_rost37:
                phys_ras = " дисгармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL = 90-97)'

            elif massa in H_mas37 and rost in H_rost37:
                phys_ras = " гармоничное, крупный новорожденный, ГВ " + str(gv) + ' недель; (pM = 90-97, pL = 90-97)'

            elif massa > H_mas37[-1] and rost > H_rost37[-1]:
                phys_ras = " гармоничное, чрезмерно крупный новорожденный, ГВ " + str(
                    gv) + ' недель; (pM > 97, pL > 97)'

            elif massa in N_mas37 and rost in H_rost37:
                phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL = 90-97)'

            elif massa in N_mas37 and rost > H_rost37[-1]:
                phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 10-90, pL > 97)'

            # ______________Оценка звур по гипотрофическому типу______________
            elif massa in L_mas37 and rost in N_rost37:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM = 3-10, pL = 10-90)'

            elif massa < L_mas37[0] and rost in N_rost37:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " резко дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 60 > k > 55:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 55 > k > 50:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'
                elif 50 > k:
                    phys_ras = " резко дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипотрофическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 10-90)'

            # ______________Оценка звур по гипопластическому типу______________
            elif massa < L_mas37[0] and rost in L_rost37:
                k = int(massa) / int(rost)
                k_str = str(round(k, 0))
                if k > 60:
                    phys_ras = " дисгармоничное, соответствует ГВ " + str(gv) + ' недель; (pM > 3, pL = 3-10)'
                elif 60 > k > 55:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "1 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 55 > k > 50:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "2 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
                elif 50 > k:
                    phys_ras = " дисгармоничное, задержка внутриутробного зарвития новорожденного " \
                               "3 ст по гипопластическому типу, массо-ростовой коэффициент =  " + k_str \
                               + '; ГВ ' + str(gv) + ' недель; (pM < 3, pL = 3-10)'
            else:
                phys_ras = "Требуется провести самостоятельный расчет"

        else:
            phys_ras = "Пожалуйста, проведите расчет самостоятельно. " \
                       "Создатель программы в будущем постарается доделать этот функционал "

        for i in self:
            for rec in journal:
                if day.days != 1 and day.days != 3:
                    if i.number == rec.number and i.date == rec.date:
                        self.text_exch = rec.text + '\nОценка физического развития:' + phys_ras
                else:
                    if i.number == rec.number and i.date == rec.date:
                        self.text_exch = rec.text


