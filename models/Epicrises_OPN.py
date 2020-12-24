from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError
import datetime


class NeomedEpicrises_OPN(models.Model):

    _name = 'neomed.epicrises_opn'
    _inherit = 'neomed.inspection_opn'

    opn_id = fields.Many2one('neomed.opn', 'ОПН')

    selection = [('Выписной эпикриз','Выписной эпикриз'),
                 ('Переводной эпикриз','Переводной эпикриз')]


    @api.onchange('select')
    def _def_treatment_period(self):
        if self.select != False:
            day_of_admission = self.opn_id.date_transfer_opn
            for rec in self.opn_id.journal_opn_ids:
                if rec.checkbox_home == True or rec.checkbox_OPN == True:
                    day_of_discharge = rec.date
                    my = self.opn_id.birth_day
                    sample = self.day_of_discharge - my
                    self.treatment_period = "находился на лечении в ОПН ГБУЗ РБ Роддом №3 с " \
                                            "{} по {} с диагнозом:".format(day_of_admission, day_of_discharge)

                    self.condition_at_discharge = rec.text + "\n\n" \
                                                             "Масса тела {}гр                    Сутки жизни {}-е сутки\n" \
                                                             "Группа здоровья - 2Б              Группа направленного риска - 1, 2, 3".format(rec.mass, sample.days)

                if rec.day_nomber == "3-е сутки":
                    main = " "
                    main2 = " "
                    if rec.main == "main15":
                        main = rec.dop1
                    else:
                        main = rec.main

                    if rec.main2 == "main15":
                        main2 = rec.dop2
                    else:
                        main2 = rec.main2
                    self.discharge_diagnosis = "Осн.:" + str(main) + "\n" + \
                                               "Осл.:" + str(rec.main1) + "\n" + \
                                               "Соп.:" + str(main2) + "\n"

    day_of_discharge = fields.Date(string="Дата выписки", default=datetime.date.today())
    dop_discharge = fields.Text(string="Дополнение у выписке(масса при выписке, сутки жизни)")


    select = fields.Selection(selection, string="Выбор типа документа")
    treatment_period = fields.Text(string="Период лечения")

    discharge_diagnosis = fields.Text(string="Диагноз при выписке")

    treatment_performed = fields.Text(string="Проведенное лечение")
    @api.onchange('select')
    def _def_treatment_performed(self):
        if self.select != False:
            day_of_admission = self.opn_id.date_transfer_opn
            day_of_discharge = " "
            for rec in self.opn_id.journal_opn_ids:
                if rec.checkbox_home == True or rec.checkbox_OPN == True:
                    day_of_discharge = rec.date
            antihemorrhagic_therapy = round(self.opn_id.massa_birth / 10000, 2)
            ampicillini = round(self.opn_id.massa_birth / 1000, 2) * 25
            amicacini = round(self.opn_id.massa_birth / 1000, 2) * 15
            nutr1 = round((round(self.opn_id.massa_birth / 1000, 2) * 25 * 68) / 100 , 0)
            nutr2 = round((round(self.opn_id.massa_birth / 1000, 2) * 100 * 68) / 100, 0)

            self.treatment_performed = " - Лечебно-охранительный режим ОПН роддома №3 \n" \
                                       " - Респираторная терапия: \n" \
                                       " - Антибактериальная терапия: Sol.Ampicillini {} 4р/д " \
                                       "(10-00, 16-00, 22-00, 04-00) с {} по {}, " \
                                       "Sol.Amikacini {} 1р/д (13-00) с {} по {}\n" \
                                       " - ИТ по физиологической потребности, с учетом водно – электролитных нарушений с {} по {}\n" \
                                       " - Парентеральное питание. Аминовен инфант 10%, Липофундин 20% по схеме с {} по {}\n" \
                                       " - Энтеральное кормление сцеженным молоком по {} - {}\n" \
                                       " - Гемостатическая терапия: Дицинон-12,5 мг/кг в/в 2 р/д, викасол 1 мг/кг\n" \
                                       " - Фототерапия с {} по {}\n" \
                                       " - Пункция кефалогематомы ".format(ampicillini, day_of_admission, day_of_discharge,
                                                                           amicacini, day_of_admission, day_of_discharge,
                                                                           day_of_admission, day_of_discharge,
                                                                           day_of_admission, day_of_discharge, nutr1, nutr2,
                                                                       day_of_admission, day_of_discharge,)

    condition_at_discharge = fields.Text(string="Состояние при выписке")
    discharge = fields.Text(string="Перевод")
    recommendation = fields.Text(string="Рекомендации")
    @api.onchange('select')
    def _def_recommendation(self):
        if self.select != False:
            self.recommendation = " - Наблюдение участкового педиатра, невролога, окулиста, кардиолога, уролога, деткого хирурга \n" \
                                  " - Грудное вскармливание \n" \
                                  " - Туалет пупочной ранки/пуповинного остатка раствором бриллиантовой зелени \n" \
                                  " - Ежедневные прогулки и водные процедуры \n" \
                                  " - Повторное НСГ, УЗИ ОБП забрюшинного пространства, ЭхоКГ в 1 мес по месту жительства в Д/П \n" \
                                  " - Наблюдение за цветом кожных покровов, при усилении желтушности – повторное исследование БХ крови на уровень общего билирубина \n" \
                                  " - Повторное исследование ОАК в динамике в 1 мес по месту жительства в Д/П \n" \
                                  " - Повторный осмотр нейрохирургом в течении 1 недели после выписки из роддома №3 в ГДКБ №17"
            self.discharge = "Переводится в ОПН ГДКБ №17 по договоренности с зав. отделением \n" \
                             "Согласие матери на перевод _________________ подпись _____________________ тел. __________________________________________"
    discharge_diagnosis_main = fields.Char(string="Диагноз основной", compute="def_discharge_diagnosis_main")
    discharge_diagnosis_main2 = fields.Char(string="Диагноз сопутствующий", compute="def_discharge_diagnosis_main")

    @api.depends('select')
    def def_discharge_diagnosis_main(self):
        for i in self:
            for res in self.opn_id.journal_opn_ids:
                if res.day_nomber == "3-е сутки":
                    if res.main != 'main15':
                        i.discharge_diagnosis_main = res.main
                    else:
                        i.discharge_diagnosis_main = res.dop1

                    if res.main2 == False:
                        i.discharge_diagnosis_main2 = res.dop2
                    elif res.main2 != 'main15' and res.dop2 != False:
                        i.discharge_diagnosis_main2 = res.main2 + ' ' + res.dop2
                    elif res.main2 != 'main15':
                        i.discharge_diagnosis_main2 = res.main2
                    else:
                        i.discharge_diagnosis_main2 = res.dop2

    vaccination = fields.Text(string="Вакцинация")
    @api.onchange('select')
    def _def_vaccination(self):
        if self.select != False:
            hepatitis = self.opn_id.birth_day + timedelta(days=1)
            tuberculosis = self.opn_id.birth_day + timedelta(days=3)
            neonat = self.opn_id.birth_day + timedelta(days=4)
            audio = self.opn_id.birth_day + timedelta(days=3)
            self.vaccination = "ВПГ «В» от {} доза 0,5 в/м серия 228-1119 годен до 11.23 года \n" \
                               "БЦЖ «М» от  {} доза 0,025 в/к серия 661 годен до 04.21 г. г.Москва\n" \
                               "Неонатальный скрининг сделан {}\n" \
                               "Аудиологический скрининг проыеден, Pass {}".format(hepatitis, tuberculosis, neonat, audio)

            # Связь с моделью Перыичный осмотр ОПН

    blood_gr = [('О(I) Rh (+) положительная', 'О(I) Rh (+) положительная'),
                ('О(I) Rh (-) отрицательная', 'О(I) Rh (-) отрицательная'),
                ('А(II) Rh (+) положительная', 'А(II) Rh (+) положительная'),
                ('А(II) Rh (-) отрицательная', 'А(II) Rh (-) отрицательная'),
                ('В(III) Rh (+) положительная', 'В(III) Rh (+) положительная'),
                ('В(III) Rh (-) отрицательная', 'В(III) Rh (-) отрицательная'),
                ('АВ(IV) Rh (+) положительная', 'АВ(IV) Rh (+) положительная'),
                ('АВ(IV) Rh (-) отрицательная', 'АВ(IV) Rh (-) отрицательная')]

    blood_mother = fields.Selection(blood_gr, string='Группа крови мамы', related='opn_id.inspection_opn_ids.blood_mother')
    zrelost = fields.Char(string='Оценка МФ-зрелости', related='opn_id.inspection_opn_ids.zrelost')
    phis_ras = fields.Char(string='Оценка физ развития', related='opn_id.inspection_opn_ids.phis_ras')
    mother_age = fields.Char(string='Возраст мамы', related='opn_id.inspection_opn_ids.mother_age')