from odoo import models, fields

class TodoPriority(models.Model):
    _inherit = "project.task"

    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta')
    ], string="Prioridad", default='1')
