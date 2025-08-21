from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Propiedad"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    postcode = fields.Char(string="Código postal")
    date_availability = fields.Date(string="Disponible desde")
    expected_price = fields.Float(string="Precio esperado", required=True)
    selling_price = fields.Float(string="Precio de venta", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Habitaciones", default=2)
    living_area = fields.Integer(string="Área habitable (m²)")
    garden = fields.Boolean(string="Jardín")
    garden_area = fields.Integer(string="Área del jardín (m²)")
    garden_orientation = fields.Selection(
        [("north", "Norte"), ("south", "Sur"), ("east", "Este"), ("west", "Oeste")],
        string="Orientación del jardín",
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [
            ("new", "Nueva"),
            ("offer_received", "Con oferta"),
            ("offer_accepted", "Oferta aceptada"),
            ("sold", "Vendida"),
            ("cancelled", "Cancelada"),
        ],
        string="Estado",
        default="new",
        copy=False,
    )
