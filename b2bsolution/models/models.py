# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Customer(models.Model):
    _name = 'customer'
    _description = 'Customers'

    name = fields.Char(string="Customer Name")
    username = fields.Char(string="Customer Username")
    password = fields.Char(string="Customer Password")

class Order(models.Model):
    _name = 'order'
    _description = 'Orders'

