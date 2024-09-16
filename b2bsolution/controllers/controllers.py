# -*- coding: utf-8 -*-
from odoo import http
import json

class Customer(http.Controller):
    @http.route('/api/customer/login', auth='public')
    def login(self, username, password):
        return json.dumps({username, password})

    @http.route('/api/customer/logout', auth='public')
    def list(self, username):
        return json.dumps({'message': 'logout'})
