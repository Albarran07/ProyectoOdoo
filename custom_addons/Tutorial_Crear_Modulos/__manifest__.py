# Se intentara crear un modulo nuevo sin dependencias el cual 
# mostrara un tutorial para la creacion de nuevos modulos.

{
    'name': 'Tutorial Módulo',
    'version': '1.0',
    'license': 'LGPL-3',
    'summary': 'Módulo de ejemplo para aprender a crear módulos desde cero',
    'description': 'Este módulo sirve como tutorial para crear módulos en Odoo sin dependencias',
    'category': 'Tools',
    'author': 'Marco Albarrán',
    'depends': [],  # Sin dependencias
    'data': [
        'security/ir.model.access.csv',
        'views/tutorial_modelo_views.xml',
    ],
    'installable': True,
    'application': True,
}
