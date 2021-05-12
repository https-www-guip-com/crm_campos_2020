# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta


tipo_chip = [
    ('0', 'Claro'),
    ('1', 'Tigo'),
    ('2', 'Htelondu'),
    ('3', 'Otros'),
]


tipo_cliente = [
    ('0', 'Comerciante Individual'),
    ('1', 'Comerciante Sociedad'),
]

tipo_territorio = [
    ('t1', 'T1'),
    ('t2', 'T2'),
    ('t2', 'T3'),
]

tipo_deci = [
    ('No', 'NO'),
    ('Si', 'SI'),
]

grupo_financiero = [
    ('No', 'NO'),
    ('Si', 'SI'),
]

class creacion_listas_Proveedor_Internet(models.Model):
    _name = "lista_proveedor_internet"
    _order = 'nombre_prove_inter'
    _rec_name = 'nombre_prove_inter'

    #Esta herencia funciona para que se pueda mostrar el pie de pagina en los formularios con las notas y poder enviar correos
    _inherit = ['mail.thread', 'mail.activity.mixin']
                                   
    nombre_prove_inter = fields.Text("Proveedor Internet")
    
    _sql_constraints = [
        ('name_uniq', 'unique (nombre_prove_inter)', "El nombre de este proveedor ya existe !"),]

class CrmGuipTerritorio(models.Model):
    _name = "list.territory"
    _rec_name = 'name'
    _description = 'Lista de territorios iniciativas'
                                   
    name = fields.Char(string="Territorio")
    description = fields.Text(string="Descripción")
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "El territorio ya existe !"),]

class CrmGuipTipoInternet(models.Model):
    _name = "list.type.internet"
    _rec_name = 'name'
    _description = 'Lista de territorios iniciativas'
                                   
    name = fields.Char(string="Tipo internet")
    description = fields.Text(string="Descripción")
    
    _sql_constraints = [
        ('typeI_uniq', 'unique (name)', "El tipo de internet ya existe !"),]

class CrmGuipDepartamentos(models.Model):
    _name = "list.departamentos"
    _rec_name = 'name'
    _description = 'Lista de departamentos iniciativas'
                                   
    name = fields.Char(string="Departamento")
    description = fields.Text(string="Descripción")
    
    _sql_constraints = [
        ('depto_uniq', 'unique (name)', "El departamento ya existe !"),
    ]

class creacion_listas_Todo(models.Model):
    _name = "lista_giro_negocios"
    _order = 'nombre_giro'
    _rec_name = 'nombre_giro'

    #Esta herencia funciona para que se pueda mostrar el pie de pagina en los formularios con las notas y poder enviar correos
    _inherit = ['mail.thread', 'mail.activity.mixin']
                                   
    nombre_giro = fields.Text("Giro del Negocio")
    
    _sql_constraints = [
        ('name_uniq', 'unique (nombre_giro)', "El nombre de este giro ya existe !"),
    ]

class crm_add_campos(models.Model):
    _inherit = 'crm.lead'
    
    numero_id = fields.Char("ID Representante Legal",  required=True)
    edad = fields.Char(string="Edad")
    
    nombre_completo_dueno = fields.Char("Nombre Completo Dueño",  required=True)
    email_dueno = fields.Char("Email Dueño")
    numero_id_dueno = fields.Char("ID Dueño")


    deno_razon_social = fields.Char("Denominación  o razón social")
    email_negocio = fields.Char("Email del Negocio")
    telefono_negocio = fields.Char("Telefono del Negocio")
    antiguedad = fields.Char(string="Antiguedad del negocio(Años)",) 
    # valor_mensual = fields.Selection([('1', '5000-10000'),('2', '11000-20000'),('3', '21000-40000'),('4', 'Mayor a 50000')], 
    #                                default="1", string="Monto ventas mensual",
    #                                help="Ingres Monto aproximado ingreso  y/o ventas mensuales")
    valor_mensual = fields.Char(string="Monto ventas mensual")
    
    longitud = fields.Float("Longitud")
    latitud = fields.Float("Latitud")

    tiene_internet = fields.Selection([('Si', 'SI'),('No', 'NO')], 
                                   default="",
                                   string='Tiene Internet')
    
    # tipo_internet = fields.Selection([('Celular', 'Celular'),('Fibra_Optica', 'Fibra Optica'),('Residencial', 'Residencial')], 
    #                                default="Residencial", 
    #                                string='Tipo Internet')
    tipo_internet = fields.Many2one('list.type.internet', string="Tipo Internet")
    
    cantidad_productos = fields.Char("Cantidad de productos en inventario") 
    # cant_empleados = fields.Integer("Numero de empleados") 
    cant_empleados = fields.Char("Numero de empleados")
    # empleados_negocio = fields.Selection([
    #     ('1', '1-10'),
    #     ('2', '10-20'),
    #     ('3', '20-30'),
    #     ('4', '30-40'),
    #     ('5', 'Mayor a 50')
    #     ], default="1", string='Numero de empleados') 
    metodos_pago = fields.Selection([('1', 'Efectivo'),('2', 'POS'),('3', 'Otros')], 
                                    default="1",
                                    string='Metodo de Pago')

    user_creacion_ids = fields.One2many('creacion_usuarios_guip','user_creacion_id')
    tipo_chip_selec = fields.Selection(tipo_chip, string='Tipo Chip', index=True, default=tipo_chip[0][0])

    #Nuevos campos
    # tipo_cliente = fields.Selection(tipo_cliente, string='Tipo Cliente', index=True, default=tipo_cliente[0][0])
    tipo_cliente = fields.Selection([
        ('Comerciante_Individual', 'Comerciante Individual'),
        ('Sociedad_Mercantil', 'Sociedad Mercantil'),
        ], default='', string="Tipo Cliente")
    permiso_operacion = fields.Char("Permiso de Operaciones")
    numero_sucursale = fields.Integer("Numero sucursales", help="Numero entero de sucursales")

    tipo_giro_id = fields.Many2one('lista_giro_negocios', 
                                   string="Giro Negocio", 
                                   ondelete='cascade', 
                                   index=True)

    # tipo_terri = fields.Selection(tipo_territorio, string='Territorio', index=True, default='')
    tipo_terri = fields.Many2one('list.territory', string="Territorio")
    list_deptos = fields.Many2one('list.departamentos', string="Departamento")

    tipo_proveedor_inter_id = fields.Many2one('lista_proveedor_internet', 
                                   string="Proveedor Internet", 
                                   ondelete='cascade', 
                                   index=True)

    tipo_proveedor_inter_mejor = fields.Many2one('lista_proveedor_internet', 
                                   string="Operador Movil con mejor señal", 
                                   ondelete='cascade', 
                                   index=True)

    cargo_publico = fields.Selection(tipo_deci, string='¿Ha ejercido o ejerce usted algun cargo publico?  ', index=True, default=tipo_deci[0][0])
    nombre_cargo = fields.Char("Nombre Cargo")

    #Cambios de nombre a campos
    # user_id = fields.Many2one(string="Oficial Comercial")

    #Cliente - oportunidad
    sociedad_dilo_ids = fields.One2many('dilo_sociedad','lead_id')
    sociedad_dilo_junta_ids = fields.One2many('dilo_sociedad_junta','lead_id')
    celular_negocio = fields.Char(string="Tel. Celular")

    #agregados
    no_cliente = fields.Char(string="No. Cliente", index=True)
    rtn_cliente = fields.Char(string="RTN de Negocio", index=True)
    fecha_constitucion = fields.Date(string="Fecha de constitución", help="Ingrese la fecha de constitución del negocio")
    pregunta_grupo_financiero = fields.Selection(grupo_financiero, string="¿Pertenece a un grupo financiero o económico?", default="")
    respuesta_grupo_financiero = fields.Char(string="Detalle nombre del grupo")
    otras_actividades = fields.Char(string="Especifique Otros", help="Especifique otros tipos de activiades del negocio")
    fecha_registro = fields.Date(string="Fecha de toma datos")
    numero_transacciones = fields.Integer(string="No. Transacciones",)
    pos_disponible = fields.Selection([
        ('si', 'Si'),
        ('no', 'No'),
        ], default='', string="¿Cuenta con POS?")
    pos_banco = fields.Char(string="¿Qué Banco?")
    ancho_banda = fields.Selection([
        ('5_MB','5'),
        ('10_MB','10'),
        ('15_MB','15'),
        ('20_MB','20'),
        ('25_MB','25'),
        ],string="Ancho de banda", help="Ingrese ancho de banda en MB",index=True)
    monto_total_activos = fields.Float(string="Monto total activos (L.)", help="Ingrese Monto aproximado del total de Activos L.")
    monto_venta_anual = fields.Float(string="Monto venta anual (L.)", help="Ingrese Monto aproximado Ventas o Ingresos Anuales L.")
    cliente_1 = fields.Char(string="1. Cliente")
    cliente_2 = fields.Char(string="2. Cliente")
    cliente_3 = fields.Char(string="3. Cliente")
    proveedor_1 = fields.Char(string="1. Proveedor")
    proveedor_2 = fields.Char(string="2. Proveedor")
    proveedor_3 = fields.Char(string="3. Proveedor")
    proveedor_tel_1 = fields.Char()
    proveedor_tel_2 = fields.Char()
    proveedor_tel_3 = fields.Char()

    #datos de representante o propietario del negocio
    rtn_de_legal = fields.Char(string="RTN Representante")
    pasaporte_de_legal = fields.Char(string="Pasaporte")
    id_extranjero_de_legal = fields.Char(string="Carné de Residencia")
    estado_civil_de_legal = fields.Selection([
        ('Soltero', 'Soltero/a'),
        ('Casado', 'Casado/a'),
        ('Uni_n_Libre', 'Unión libre'),
        ('separado', 'Separado/a'),
        ('Divorciado', 'Divorciado/a'),
        ('Viudo', 'Viudo/a'),
        ], default='', string="Estado Civil")
    telefono_de_legal = fields.Char(string="Teléfono Fijo")
    celular_de_legal = fields.Char(string="Teléfono Móbil")
    sexo_de_legal = fields.Selection([
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ], default='', string="Sexo")
    lugar_nacio_de_legal = fields.Char(string="Lugar de Nacimiento")
    fecha_nacio_de_legal = fields.Date(string="Fecha de Nacimiento", help="Ingrese la fecha nacimiento de representante legal")
    nacionalidad_de_legal = fields.Char(string="Nacionalidad")
    email_de_legal = fields.Char(string="Correo Electrónico")
    profesion_de_legal = fields.Char(string="Profesión/Oficio")
    periodo_cargo_desde = fields.Date(string="Periodo")
    periodo_cargo_hasta = fields.Date(string="")

    #Uso de servicio digitales GUIP
    aplica_apertura = fields.Selection([
        ('Si', 'Si'),
        ('No', 'No'),
        ], default='', string="Aplica apertura cuenta", help="Aplica apertura de cuenta bancaria")
    numero_cta_banco = fields.Char(string="No. de cuenta banco", help="Numero de Cuenta Bancaria")
    tipo_cuenta = fields.Char(string="Tipo de cuenta", help="")
    datos_instalacion = fields.Text(string="Datos de instalación")
    aplicativo = fields.Char(string="Aplicativo", help="")
    cantidad_dispositivos = fields.Integer(string="Cantidad Dispositivos")
    tipo_dispositivo = fields.Char(string="Tipo Dispositivos", help="")
    usuarios_dispositivos = fields.Integer(string="Cantidad Usuarios Dispositivos")
    # solicita_sim = fields.Selection([
    #     ('si', 'Si'),
    #     ('no', 'No'),
    #     ], default='', string="Solicita SIM Card", help="")
    solicita_sim = fields.Char(string="Solicita SIM Card")
    disp_1_latitud = fields.Char(string="Coordenadas Disp. 1")
    disp_1_longitud= fields.Char(help="longitud Disp. 1")
    disp_2_latitud = fields.Char(string="Coordenadas Disp. 2")
    disp_2_longitud= fields.Char(help="longitud Disp. 2")
    address_disp_2 = fields.Char(string="Dirección dispositivo 2")   
    gestor = fields.Char(string="Nombre del gestor") 

    #Fotografias 
    id_representante = fields.Many2many('ir.attachment', string="ID Representante Legal")
    urls_images = fields.Text(string="URLs de imagenes DoForm")

    @api.onchange('fecha_constitucion')
    def onchange_fecha(self):
        for rec in self:
            if rec.fecha_constitucion:
                d1 = rec.fecha_constitucion
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.antiguedad = str(rd.years) + "  años"
            else:
                rec.antiguedad = "Ingrese fecha de consitución"

class DiloSociedad(models.Model):
    _name = "dilo_sociedad"
    _description = "Información socios de Red Dilo Sociedad"
    _rec_name = "name"

    lead_id = fields.Many2one('crm.lead',string="Oportunidad", readonly=True)
    name = fields.Char("Nombre Completo")
    id_socio = fields.Char("Número de identificación")
    porcentaje_socio = fields.Float(string="% Participación")
    nacionalidad_socio = fields.Char(string="Nacionalidad")

class DiloSociedadJunta(models.Model):
    _name = "dilo_sociedad_junta"
    _description = "Información junta directiva de Red Dilo Sociedad"
    _rec_name = "name"

    lead_id = fields.Many2one('crm.lead',string="Oportunidad", readonly=True)
    name = fields.Char(string="Nombre Completo")
    id_socio = fields.Char(string="Número de identificación")
    cargo = fields.Char(string="Cargo")
    nacionalidad_socio = fields.Char(string="Nacionalidad")
