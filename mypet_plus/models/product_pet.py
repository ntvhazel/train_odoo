# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class ProductPet(models.Model):
    _name = "product.pet"
    _inherits = {'my.pet': 'my_pet_id'}
    _description = "Product Pet"

    my_pet_id = fields.Many2one(
        'my.pet', 'My Pet',
        auto_join=True, index=True, ondelete="cascade", required=True)
    
    pet_type = fields.Selection([
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('vip', 'VIP'),
        ('cute', 'Cute'),
    ], string='Pet Type', default='basic')
    
    pet_color = fields.Selection([
        ('white', 'White'),
        ('black', 'Black'),
        ('grey', 'Grey'),
        ('yellow', 'Yellow'),
    ], string='Pet Color', default='white')
    
    bonus_price = fields.Float("Bonus Price", default=0)
    
    final_price = fields.Float("Final Price", compute='_compute_final_price')

    @api.depends("bonus_price")
    def _compute_final_price(self):
        for record in self:
            record.final_price = record.basic_price + record.bonus_price

    # @api.depends("bonus_price")
    # def _format_money(self):
    #     locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')
    #     self.bonus_price = locale.currency(self.bonus_price, grouping=True)
            