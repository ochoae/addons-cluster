#!/usr/bin/python
# -*- encoding: utf-8 -*-
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    Author: Cluster Brands
#    Copyright 2013 Cluster Brands
#    Designed By: Jose J Perez M <jose.perez@clusterbrands.com>
#    Coded by: Eduardo Ochoa  <eduardo.ochoa@clusterbrands.com.ve>
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from openerp.osv import osv, fields
from openerp.tools.translate import _

class hr_loan(osv.Model):
    _name = "hr.loan"

    _columns = {
        'employee_id':fields.many2one('hr.employee', 'Employee', required=True),
        'type_id':fields.many2one('hr.loan.type', 'Type', required=True), 
        'reason':fields.selection([
            ('apartment','Apartment'),
            ('health','Health'),
            ('studies','Studies')
            ], 'Reason', select=True),
        'amount': fields.float('Amount', digits=(16, 2), required=False), 
        'details': fields.text('Details'),
        'state':fields.selection([
            ('draft','Draft'),
            ('confirm','confirm'),
            ('paid','Paid'),
            ('decline', 'Declined')
            ], 'State', readonly=True),
    }

class hr_loan_type(osv.Model):
    _name = "hr.loan.type"

    _columns = {
        'name': fields.char('Name', size=255, required=True),
        'code': fields.char('Code', size=55, required=True), 
        'max_amount': fields.float('Max. Amount ', digits=(16, 2), required=False), 
        'min_discount': fields.float('Min. Discount ', digits=(16, 2), required=False), 
        # 'affect':fields.selection([
        #     ('payroll','Payroll'),
        #     ('holidays','Holidays'),
        #     ('social_benefits','Social Benefits'),
        #     ('eventual','Eventual'),
        #      ],    'State'),
        'affect_payroll':fields.boolean('Payroll', required=False), 
        'affect_holidays':fields.boolean('Holidays', required=False),
        'affect_social_benefits':fields.boolean('Social Benefits', required=False),
        'affect_eventual':fields.boolean('Eventuals', required=False),
        'details': fields.text('Details'), 
    }