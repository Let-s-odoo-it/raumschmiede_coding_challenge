# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Raumschmiede CRM Adaption',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 1,
    'summary': 'Leads, Opportunities, Activities',
    'description': """This module adapts the CRM  models and views to the needs of Raumschmiede GmbH""",
    'depends': [
        'crm',
    ],
    'data': [
        'views/crm_lead_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
