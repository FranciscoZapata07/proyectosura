from mailbox import NoSuchMailboxError
from django import forms
class FormularioMedico(forms.Form):
    
    ESPECIALIDADES=(
        (1,'Cardiologia'),
        (2,'Medicina Interna'),
        (3,'Medico General'),
        (4,'Ortopedia'),
        (5,'Pediatria')
    )
    JORNADAS=(
        (1,'06:00 AM - 02:00 PM'),
        (2,'02:00 PM - 10:00 PM'),
        (3,'10:00 PM - 06:00 AM')
    )
    SEDES=(
        (1,'Almacentro'),
        (2,'Punto Clave'),
        (3,'Los Molinos')
    )

    nombre=forms.CharField()
    apellidos=forms.CharField() 
    cedula=forms.CharField() 
    tarjetaProfesional=forms.CharField()
    especialidad=forms.ChoiceField()
    jornada=forms.ChoiceField()
    contacto=forms.CharField() 
    sede=forms.ChoiceField()