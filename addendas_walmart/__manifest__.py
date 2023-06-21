# -*- coding: utf-8 -*-
{
    'name': "addendas_walmart",
    'summary': """Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """Long description of module's purpose""",
    'author': "Xmarts",
    'contributors': "victoralonso@xmarts.com, javier.hilario@xmarts.com",
    'website': "http://www.xmarts.com",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['base', 'l10n_mx_edi', 'fields_functions_adendas', 'l10n_mx_edi_extended_40'],
    'data': [
        # 'security/ir.model.access.csv',
        'data/inherit_cfdi.xml',
        'views/addenda_walmart.xml',
    ],
}
