from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError
import datetime


class NeomedInspection(models.Model):

    _name = 'neomed.inspection'
    mother_id = fields.Many2one('neomed.mothers', 'ФИО мамы')

    diagnosis_main = [('Новорожденный из группы риска по перинатальной патологии', 'Новорожденный из группы риска по перинатальной патологии'),
                      ('Здоровый новорожденный из группы риска по перинатальной патологии', 'Здоровый новорожденный из группы риска по перинатальной патологии'),
                      ('Недоношенный новорожденный', 'Недоношенный новорожденный'),
                      ('Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС', 'Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС'),
                      ('Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС', 'Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС'),
                      ('Транзиторное тахипное новорожденного', 'Транзиторное тахипное новорожденного'),
                      ('Двусторонная кефалогематома', 'Двусторонная кефалогематома'),
                      ('Левотеменная кефалогематома', 'Левотеменная кефалогематома'),
                      ('Правотеменная кефалогематома', 'Правотеменная кефалогематома'),
                      ('Неонатальная желтуха, неуточненная', 'Неонатальная желтуха, неуточненная'),
                      ('Новорожденный от мамы с КСР (+)', 'Новорожденный от мамы с КСР (+)'),
                      ('Здоровый новорожденный от мамы с КСР (+)', 'Здоровый новорожденный от мамы с КСР (+)'),
                      ('Врожденная очаговая  пневмония, неуточненная, острое течение, средней тяжести', 'Врожденная очаговая  пневмония, неуточненная, острое течение, средней тяжести'),
                      ('main15', 'другой')]

    diagnosis_main2 = [('Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС', 'Церебральная ишемия 1 степени, острый период, синдром угнетения ЦНС'),
                       ('Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС', 'Церебральная ишемия 1 степени, острый период, синдром возбуждения ЦНС'),
                       ('Недоношенный новорожденный', 'Недоношенный новорожденный'),
                       ('«Маловесный» для гестационного возраста новорожденный', '«Маловесный» для гестационного возраста новорожденный'),
                       ('Малый размер новорожденного для гестационного возраста', 'Малый размер новорожденного для гестационного возраста'),
                       ('Крупный новорожденный', 'Крупный новорожденный'),
                       ('Чрезмерно крупный новорожденный', 'Чрезмерно крупный новорожденный'),
                       ('Двусторонная кефалогематома', 'Двусторонная кефалогематома'),
                       ('Левотеменная кефалогематома', 'Левотеменная кефалогематома'),
                       ('Правотеменная кефалогематома', 'Правотеменная кефалогематома'),
                       ('ВПС - дефект межжелудочковой перегородки', 'ВПС - дефект межжелудочковой перегородки'),
                       ('Перинатальный контакт по В-20', 'Перинатальный контакт по В-20'),
                       ('Перивентрикулярное кровоизлияние 1 степени', 'Перивентрикулярное кровоизлияние 1 степени'),
                       ('Межпредсердное сообщение', 'Межпредсердное сообщение '),
                       ('main15', 'другой')]


    @api.onchange('severity_birth')
    def _get_default_dop_severity_birth(self):
        if self.severity_birth == 'main1':
            self.severity = 'удовлетворительное'
            self.posa = 'физиологическая'
            self.scream = 'громкий'
            self.activnost = 'удовлетворительная'
            self.react = 'живая'
            self.stigm = 'правильное'
            self.skin = 'розовые, чистые, влажные'
            self.rash = 'высыпаний нет, кожные покровы чистые'
            self.eyes = 'чистые, розовые'
            self.eyes1 = 'нет'
            self.fat = 'развита удовлетворительно, равномерно'
            self.turgor = 'достаточный'
            self.elast = 'удовлетворительная'
            self.limph = 'не пальпируются'
            self.pupov = 'в скобе'
            self.head = 'конфигурированная'
            self.skull = 'плотные, швы на стыке'
            self.rodnich = 'размеры 1,5*1,5, не напряжен'
            self.chest = 'правильная, симметричная'
            self.percus = 'легочный звук'
            self.nose = 'свободное'
            self.breath = 'физиологическое, ЧД 40/мин  '
            self.ausk = 'дыхание пуэрильное'
            self.ausk1 = 'тоны ясные, ритмичные. Пульс 140 в минуту, ЧСС 140/мин'
            self.nerv = 'рефлексы вызываются'
            self.scladki = 'симметричны'
            self.phon = 'есть'
            self.react_sound = 'есть'
            self.simmetr_neba = 'симметричны'
            self.shoulder = 'срединное'
            self.tonus = 'удовлетворительный'
            self.slisist = 'чистые, розовые, язык чистый, влажный'
            self.stomach = 'мягкий, печень не увеличена, селезенка не пальпируется'
            self.stul = 'было'
            self.mocha = 'было'
            self.anus = 'есть'
            self.tas = 'движение в полном обьеме '
            self.lac = 'достаточная'
            self.local = 'без особенностей'


        elif self.severity_birth == 'main2' or self.severity_birth == 'main3':
            self.severity = 'средней тяжести'
            self.posa = 'физиологическая'
            self.scream = 'средней силы'
            self.activnost = 'снижена'
            self.react = 'вялая'
            self.stigm = 'правильное'
            self.skin = 'розовые, чистые, влажные'
            self.rash = 'высыпаний нет, кожные покровы чистые'
            self.eyes = 'чистые, розовые'
            self.eyes1 = 'нет'
            self.fat = 'развита удовлетворительно, равномерно'
            self.turgor = 'достаточный'
            self.elast = 'удовлетворительная'
            self.limph = 'не пальпируются'
            self.pupov = 'в скобе'
            self.head = 'конфигурированная'
            self.skull = 'плотные, швы на стыке'
            self.rodnich = 'размеры 1,5*1,5, не напряжен'
            self.chest = 'правильная, симметричная'
            self.percus = 'легочный звук'
            self.nose = 'свободное'
            self.breath = 'физиологическое, ЧД 40/мин  '
            self.ausk = 'дыхание пуэрильное'
            self.ausk1 = 'тоны ясные, ритмичные. Пульс 140 в минуту, ЧСС 140/мин'
            self.nerv = 'рефлексы вызываются с истощением'
            self.scladki = 'симметричны'
            self.phon = 'есть'
            self.react_sound = 'есть'
            self.simmetr_neba = 'симметричны'
            self.shoulder = 'срединное'
            self.tonus = 'снижен'
            self.slisist = 'чистые, розовые, язык чистый, влажный'
            self.stomach = 'мягкий, печень не увеличена, селезенка не пальпируется'
            self.stul = 'было'
            self.mocha = 'было'
            self.anus = 'есть'
            self.tas = 'движение в полном обьеме '
            self.lac = 'достаточная'
            self.local = 'без особенностей'


    sev = [('main1', 'удовлетворительное'),
           ('main2', 'средней тяжести'),
           ('main3', 'тяжелое')]
    pol1 = [('по мужскому типу', 'по мужскому типу'),
           ('по женскому типу', 'по женскому типу')]

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
    severity_birth = fields.Selection(sev, required=True)

    # sex_inspection = fields.Char(string=' ')

    @api.depends('severity')
    def _function_sex(self):
        # self.sex_inspection = self.mother_id.sex
        for record in self:
            if record.mother_id.sex == 'male':
                record.pol = 'по мужскому типу'
                if self.mother_id.Ak_ds == 'main5':
                    record.head = 'округлая'
            else:
                record.pol = 'по женскому типу'
                if self.mother_id.Ak_ds == 'main5':
                    record.head = 'округлая'


    date = fields.Date(string='Дата', related='mother_id.birth_day')
    # date_birth = fields.Date(string='Дата', default=datetime.date.today())
    time_what = fields.Char(string='Время осмотра', required=True)
    time_birth = fields.Char(string='Время родов', related='mother_id.birth_time')
    severity = fields.Char(string='Общее состояние')
    posa = fields.Char(string='Поза')
    scream = fields.Char(string='Крик')
    activnost = fields.Char(string='Активность спонтанная')
    react = fields.Char(string='Реакция на осмотр')
    stigm = fields.Char(string='Телосложение, стигмы дизэмбриогенеза')
    skin = fields.Text(string='Кожные покровы')
    rash = fields.Text(string='Характер высыпаний')
    eyes = fields.Char(string='Конъюнктивы')
    eyes1 = fields.Char(string='Отделяемое из глаз')
    fat = fields.Text(string='Подкожно-жировой слой')
    turgor = fields.Char(string='Тургор тканей')
    elast = fields.Char(string='Эластичность мягких тканей')
    limph = fields.Char(string='Лимфатические узлы')
    pupov = fields.Char(string='Пуповинный остаток')
    head = fields.Char(string='Головка')
    skull = fields.Char(string='Состояние костей черепа')
    rodnich = fields.Char(string='Большой родничек, швы черепа')
    chest = fields.Text(string='Форма грудной клетки')
    percus = fields.Char(string='Перкуссия')
    breath = fields.Text(string='Дыхание')
    nose = fields.Char(string='Носовое дыхание')
    ausk = fields.Text(string='Аускультация легких')
    ausk1 = fields.Text(string='Аускультация сердца')
    nerv = fields.Text(string='Нервная система')
    scladki = fields.Char(string='Симметричность кожных кладок на лице')
    react_sound = fields.Char(string='Реакция на звук')
    simmetr_neba = fields.Char(string='Симметричность дужек мягкого неба, язычка')
    phon = fields.Char(string='Фонация')
    shoulder = fields.Char(string='Положение головы и плеч')
    tonus = fields.Char(string='Характер спонтанных движений, состояние мышечного тонуса')
    slisist = fields.Char(string='Слизистые полости рта')
    stomach = fields.Text(string='Живот')
    stul = fields.Char(string='Отхождение мекония')
    mocha = fields.Char(string='Мочеиспускание')
    pol = fields.Char(string='Наружные половые органы', compute='_function_sex')
    # pol = fields.Selection(pol1, string='Наружные половые органы', required=True)
    anus = fields.Char(string='Наличие ануса')
    tas = fields.Char(string='Состояние тазобедренных суставов')
    lac = fields.Char(string='Характер лактации у матери')
    local = fields.Char(string='St.localis')
    ds_main = fields.Selection(diagnosis_main, string='основной диагноз', related='mother_id.main')
    ds_main1 = fields.Char(string='сопутствующий диагноз', related='mother_id.main2')
    ds_main2 = fields.Selection([('Дыхательная недостаточность 1 ст', 'Дыхательная недостаточность 1 ст'),
                              ('Дыхательная недостаточность 2 ст', 'Дыхательная недостаточность 2 ст'),
                              ('Дыхательная недостаточность 3 ст', 'Дыхательная недостаточность 3 ст')],string='осложнение', related='mother_id.main1')
    doc_otdel = fields.Selection(doc, string='Врач', required=True)
    dop_ds = fields.Char(string='дополнение', related='mother_id.main_dop')
    dop_ds1 = fields.Char(string='дополнение')
