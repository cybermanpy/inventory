# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Audit(models.Model):
    pkaudit = models.AutoField(primary_key=True)
    opaudit = models.CharField(max_length=20, blank=True, null=True)
    pktblaudit = models.TextField(blank=True, null=True)
    tblaudit = models.CharField(max_length=20, blank=True, null=True)
    usraudit = models.CharField(max_length=20, blank=True, null=True)
    dateaudit = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit'


class Bienes(models.Model):
    id_bien = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    cod_pat_mh = models.CharField(max_length=20, blank=True, null=True)
    id_org_fin = models.ForeignKey('OrgFin', models.DO_NOTHING, db_column='id_org_fin')
    cod_pat_of = models.CharField(max_length=20, blank=True, null=True)
    id_desc = models.ForeignKey('Descripciones', models.DO_NOTHING, db_column='id_desc')
    id_marca = models.ForeignKey('Marcas', models.DO_NOTHING, db_column='id_marca')
    modelo = models.CharField(max_length=100, blank=True, null=True)
    nro_serie = models.CharField(max_length=30, blank=True, null=True)
    caracteristicas = models.CharField(max_length=500, blank=True, null=True)
    referencia = models.CharField(max_length=30, blank=True, null=True)
    id_prov = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_prov')
    fec_com = models.DateField(blank=True, null=True)
    id_tipo_doc = models.ForeignKey('TipoDocumentos', models.DO_NOTHING, db_column='id_tipo_doc')
    nro_doc = models.CharField(max_length=30, blank=True, null=True)
    prec_com = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    plazo_gar = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obs_gar = models.CharField(max_length=500, blank=True, null=True)
    id_estado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='id_estado')
    obs_est = models.CharField(max_length=500, blank=True, null=True)
    id_conserv = models.ForeignKey('Conservacion', models.DO_NOTHING, db_column='id_conserv')
    obs_conserv = models.CharField(max_length=500, blank=True, null=True)
    obs_bien = models.CharField(max_length=500, blank=True, null=True)
    bien_padre = models.IntegerField(blank=True, null=True)
    codpatnew = models.CharField(max_length=20, blank=True, null=True)
    tipos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bienes'


class Bienform10(models.Model):
    fkform10 = models.ForeignKey('Form10', models.DO_NOTHING, db_column='fkform10')
    fkbien = models.ForeignKey(Bienes, models.DO_NOTHING, db_column='fkbien')

    class Meta:
        managed = False
        db_table = 'bienform10'
        unique_together = (('fkform10', 'fkbien'),)


class Cargos(models.Model):
    pkcargo = models.IntegerField(primary_key=True)
    descargo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargos'


class Conservacion(models.Model):
    id_conserv = models.IntegerField(primary_key=True)
    des_conserv = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conservacion'


class Descripciones(models.Model):
    id_desc = models.IntegerField(primary_key=True)
    des_desc = models.CharField(max_length=50, blank=True, null=True)
    tipo_bien = models.CharField(max_length=1, blank=True, null=True)
    fktipo = models.ForeignKey('Tipos', models.DO_NOTHING, db_column='fktipo')

    class Meta:
        managed = False
        db_table = 'descripciones'


class Direcciones(models.Model):
    pkdir = models.IntegerField(primary_key=True)
    sigladir = models.CharField(max_length=10, blank=True, null=True)
    namedir = models.TextField(blank=True, null=True)
    numdir = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'


class Docfc10(models.Model):
    pkdoc = models.IntegerField(primary_key=True)
    fkresp = models.ForeignKey('Responsables', models.DO_NOTHING, db_column='fkresp')
    fc10doc = models.CharField(max_length=500, blank=True, null=True)
    fechadoc = models.DateTimeField(blank=True, null=True)
    desdoc = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docfc10'


class Estados(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    des_estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'


class Fichas(models.Model):
    id_ficha = models.IntegerField(primary_key=True)
    id_bien = models.ForeignKey(Bienes, models.DO_NOTHING, db_column='id_bien', unique=True)
    proc_mar = models.CharField(max_length=50, blank=True, null=True)
    proc_mod = models.CharField(max_length=50, blank=True, null=True)
    proc_vel = models.CharField(max_length=20, blank=True, null=True)
    disco_mod = models.CharField(max_length=50, blank=True, null=True)
    disco_cap = models.CharField(max_length=20, blank=True, null=True)
    disco_vel = models.CharField(max_length=20, blank=True, null=True)
    mem_mod = models.CharField(max_length=50, blank=True, null=True)
    mem_cap = models.CharField(max_length=20, blank=True, null=True)
    mem_vel = models.CharField(max_length=20, blank=True, null=True)
    disketera = models.CharField(max_length=10, blank=True, null=True)
    un_optica = models.CharField(max_length=20, blank=True, null=True)
    tarj_red = models.CharField(max_length=200, blank=True, null=True)
    tarj_son = models.CharField(max_length=200, blank=True, null=True)
    parlante = models.CharField(max_length=10, blank=True, null=True)
    microfono = models.CharField(max_length=10, blank=True, null=True)
    cerra_tipo = models.CharField(max_length=10, blank=True, null=True)
    cerra_nro = models.CharField(max_length=10, blank=True, null=True)
    so_marca = models.CharField(max_length=20, blank=True, null=True)
    so_mod = models.CharField(max_length=50, blank=True, null=True)
    so_licen = models.CharField(max_length=10, blank=True, null=True)
    ip_add = models.CharField(max_length=20, blank=True, null=True)
    mac_add = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fichas'


class Form10(models.Model):
    pkform10 = models.IntegerField(primary_key=True)
    dateform10 = models.DateTimeField(blank=True, null=True)
    fkresp = models.ForeignKey('Responsables', models.DO_NOTHING, db_column='fkresp')
    uploadform10 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form10'


class Marcas(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    des_marca = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcas'


class OrgFin(models.Model):
    id_org_fin = models.IntegerField(primary_key=True)
    des_org_fin = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_fin'


class Profiles(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class Proveedores(models.Model):
    id_prov = models.IntegerField(primary_key=True)
    nom_prov = models.CharField(max_length=50, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    web = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'


class Reparaciones(models.Model):
    id_repar = models.IntegerField(primary_key=True)
    id_bien = models.ForeignKey(Bienes, models.DO_NOTHING, db_column='id_bien')
    motivo = models.CharField(max_length=500, blank=True, null=True)
    solucion = models.CharField(max_length=500, blank=True, null=True)
    id_prov = models.ForeignKey(Proveedores, models.DO_NOTHING, db_column='id_prov', blank=True, null=True)
    fec_danio = models.DateField(blank=True, null=True)
    fec_arreglo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reparaciones'


class Responsables(models.Model):
    id_resp = models.IntegerField(primary_key=True)
    nom_resp = models.CharField(max_length=50, blank=True, null=True)
    cargoresp = models.CharField(max_length=30, blank=True, null=True)
    fkubicacion = models.ForeignKey('Ubicaciones', models.DO_NOTHING, db_column='fkubicacion')
    fkestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='fkestado')
    fkcargo = models.ForeignKey(Cargos, models.DO_NOTHING, db_column='fkcargo')
    cedula = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'responsables'


class TipoDocumentos(models.Model):
    id_tipo_doc = models.IntegerField(primary_key=True)
    des_tipo_doc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_documentos'


class TipoTraslados(models.Model):
    id_tipo_tras = models.IntegerField(primary_key=True)
    des_tipo_tras = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_traslados'


class Tipos(models.Model):
    pktipo = models.IntegerField(primary_key=True)
    tiponame = models.CharField(max_length=50, blank=True, null=True)
    codtipo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos'


class Traslados(models.Model):
    id_traslado = models.IntegerField(primary_key=True)
    bien = models.ForeignKey(Bienes, models.DO_NOTHING)
    motivo = models.CharField(max_length=500, blank=True, null=True)
    id_resp = models.ForeignKey(Responsables, models.DO_NOTHING, db_column='id_resp')
    id_ubic1 = models.SmallIntegerField(blank=True, null=True)
    fec_traslado = models.DateTimeField(blank=True, null=True)
    id_tipo_tras = models.ForeignKey(TipoTraslados, models.DO_NOTHING, db_column='id_tipo_tras')
    ultimo = models.CharField(max_length=2, blank=True, null=True)
    filetras = models.CharField(max_length=100, blank=True, null=True)
    fc11tras = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traslados'


class Ubicaciones(models.Model):
    id_ubic = models.IntegerField(primary_key=True)
    des_ubic = models.CharField(max_length=50, blank=True, null=True)
    nom_depto = models.TextField(blank=True, null=True)
    num_depto = models.TextField(blank=True, null=True)
    fkdir = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='fkdir')

    class Meta:
        managed = False
        db_table = 'ubicaciones'


class Users(models.Model):
    email = models.TextField()
    password = models.TextField()
    profile = models.ForeignKey(Profiles, models.DO_NOTHING)
    remember_token = models.TextField(blank=True, null=True)
    available = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'users'
