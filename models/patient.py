# -*- coding: utf-8 -*-
from odoo import api, fields, models

class HospitalPatient(models.Model):
    
    #Properties
    _name="hospital.patient"
    _description ="Hospital Patient"

    name = fields.Char(string ='Name', required=True)
    age = fields.Integer(string ='Age')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ],required=True,default='other')
    note = fields.Text(string = 'Description')
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirmed'),
        ('done','Done'),
        ('cancel','Cancelled')
    ],string="Status",default='draft')
    

    #Métodos

    # Método que cambia la propiedad state para el botón del header
    def action_confirm(self):
        self.state = 'confirm'

    # Método que cambia la propiedad state para el botón del header
    def action_done(self):
        self.state = 'done'
    
    # Método que cambia la propiedad state para el botón del header
    def action_draft(self):
        self.state = 'draft'
    
    # Método que cambia la propiedad state para el botón del header
    def action_cancel(self):
        self.state = 'cancel'