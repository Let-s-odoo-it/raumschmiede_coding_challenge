# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models 
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class Lead(models.Model):
    _inherit = 'crm.lead'

    tasks = fields.Many2many('crm.lead.task', string='Tasks')
    progress = fields.Float("Progress", compute='_compute_progress', store=True, group_operator="avg", help="Display progress of current lead.")

    def _get_completed_tasks_count(self):
        self.ensure_one()
        return len(self.tasks)

    def _get_all_tasks_count(self):
        return self.env['crm.lead.task'].search_count([])

    @api.depends('tasks')
    def _compute_progress(self):
        for lead in self:
            lead.progress = 0.0
            if len(lead.tasks) > 0:
                lead.progress = round(100.0 * lead._get_completed_tasks_count() / lead._get_all_tasks_count(), 2)

class LeadTask(models.Model):
    _name = 'crm.lead.task'
    _description = 'Tasks used in a CRM Lead'

    description = fields.Char('Description')

    def name_get(self):
        res = []
        for task in self:
            name = task.description
            res.append((task.id, name))
        return res
