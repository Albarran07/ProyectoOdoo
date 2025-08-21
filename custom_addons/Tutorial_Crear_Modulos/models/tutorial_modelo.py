from odoo import models, fields

class TutorialModulo(models.Model):
    _name = 'tutorial.modulo'
    _description = 'Tutorial Módulo'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripción")
