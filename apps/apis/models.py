# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Almacen(models.Model):
    codigoalmacen = models.CharField(primary_key=True, max_length=5)
    nombrealmacen = models.CharField(max_length=100, blank=True, null=True)
    tiempoalmacenaje = models.IntegerField(blank=True, null=True)
    estadoalmacen = models.CharField(max_length=1, blank=True, null=True)
    usuariocreacion = models.CharField(max_length=15)
    fechacreacion = models.DateTimeField()
    usuariomodificacion = models.CharField(max_length=15)
    fechamodificacion = models.DateTimeField()
    direccion = models.CharField(max_length=140, blank=True, null=True)
    telefonodirecto = models.CharField(max_length=20, blank=True, null=True)
    telefonofax = models.CharField(max_length=20, blank=True, null=True)
    codigoaduanero = models.CharField(max_length=4, blank=True, null=True)
    ruc = models.CharField(max_length=11, blank=True, null=True)
    tipoalmacen = models.CharField(max_length=3, blank=True, null=True)
    tiempoalmacenajeexpo = models.IntegerField(blank=True, null=True)
    clasificacion_sunat = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        db_table = 'almacen'


class Persona(models.Model):
    codigopersona = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=140)
    codigopais = models.CharField(max_length=2)
    codigociudad = models.CharField(max_length=3, blank=True, null=True)
    codigoubigeo = models.CharField(max_length=6, blank=True, null=True)
    telefonodirecto = models.CharField(max_length=20, blank=True, null=True)
    telefonocentral = models.CharField(max_length=20, blank=True, null=True)
    telefonofax = models.CharField(max_length=20, blank=True, null=True)
    tipodocumento = models.CharField(max_length=3, blank=True, null=True)
    numerodocumento = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    paginaweb = models.CharField(max_length=100, blank=True, null=True)
    estadopersona = models.CharField(max_length=1, blank=True, null=True)
    usuariocreacion = models.CharField(max_length=15)
    fechacreacion = models.DateTimeField()
    usuariomodificacion = models.CharField(max_length=15)
    escliente = models.CharField(max_length=1, blank=True, null=True)
    esproveedorlocal = models.CharField(max_length=1, blank=True, null=True)
    fechamodificacion = models.DateTimeField()
    esclientevip = models.CharField(max_length=1, blank=True, null=True)
    esagenteexterior = models.CharField(max_length=1, blank=True, null=True)
    escoloader = models.CharField(max_length=1, blank=True, null=True)
    esproveedorclienteexterior = models.CharField(max_length=1, blank=True, null=True)
    diascredito = models.IntegerField(blank=True, null=True)
    montolimitecredito = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cuentacontable = models.CharField(max_length=10, blank=True, null=True)
    esagenteportuario = models.CharField(max_length=1, blank=True, null=True)
    esagenteretenedor = models.CharField(max_length=1, blank=True, null=True)
    esagenteaduana = models.CharField(max_length=1, blank=True, null=True)
    codigoagenteaduana = models.CharField(max_length=4, blank=True, null=True)
    grupopersona = models.CharField(max_length=3, blank=True, null=True)
    obligatorioreferencia = models.CharField(max_length=1, blank=True, null=True)
    tipocredito = models.CharField(max_length=3, blank=True, null=True)
    esclienteguia = models.CharField(max_length=1, blank=True, null=True)
    esclienteincalines = models.CharField(max_length=1, blank=True, null=True)
    esclienteadualink = models.CharField(max_length=1, blank=True, null=True)
    esclienteobjetivogamma = models.CharField(max_length=1, blank=True, null=True)
    serespetacontactocoti = models.CharField(max_length=1, blank=True, null=True)
    observacioncrediticia = models.CharField(max_length=240, blank=True, null=True)
    codigodistrito = models.CharField(max_length=3, blank=True, null=True)
    claveweb = models.CharField(max_length=10, blank=True, null=True)
    respetarasignacionejcomercial = models.CharField(max_length=1, blank=True, null=True)
    esclienteobjetivoguia = models.CharField(max_length=1, blank=True, null=True)
    clienteproblema = models.CharField(max_length=1, blank=True, null=True)
    guiamaritimapublicidad = models.CharField(max_length=1, blank=True, null=True)
    guiamaritimasuscripcion = models.CharField(max_length=1, blank=True, null=True)
    guiamaritimasereditorial = models.CharField(max_length=1, blank=True, null=True)
    guiamaritimalector = models.CharField(max_length=1, blank=True, null=True)
    logistapublicidad = models.CharField(max_length=1, blank=True, null=True)
    logistasuscripcion = models.CharField(max_length=1, blank=True, null=True)
    logistasereditorial = models.CharField(max_length=1, blank=True, null=True)
    logistalector = models.CharField(max_length=1, blank=True, null=True)
    guialogisticapublicidad = models.CharField(max_length=1, blank=True, null=True)
    guialogisticasuscripcion = models.CharField(max_length=1, blank=True, null=True)
    guialogisticasereditorial = models.CharField(max_length=1, blank=True, null=True)
    guialogisticalector = models.CharField(max_length=1, blank=True, null=True)
    unidadnegocio = models.CharField(max_length=3, blank=True, null=True)
    observacionacuerdostarifas = models.TextField(blank=True, null=True)
    direccion2 = models.CharField(max_length=140, blank=True, null=True)
    esclientegls = models.CharField(max_length=1, blank=True, null=True)
    clientemorosoincobrable = models.CharField(max_length=1, blank=True, null=True)
    contactosxro = models.CharField(max_length=1, blank=True, null=True)
    codigointernoglob = models.CharField(max_length=10, blank=True, null=True)
    tieneseguimientogls = models.CharField(max_length=1, blank=True, null=True)
    medidasobligatorias = models.CharField(max_length=1, blank=True, null=True)
    knownshipper = models.CharField(max_length=1, blank=True, null=True)
    escombi = models.CharField(max_length=1, blank=True, null=True)
    fechainicialcombi = models.DateTimeField(blank=True, null=True)
    fechafinalcombi = models.DateTimeField(blank=True, null=True)
    cantidadro_combi = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    esbanco = models.CharField(max_length=1, blank=True, null=True)
    agentegeneranroblexpo = models.CharField(max_length=1, blank=True, null=True)
    sectoreconomico = models.CharField(max_length=3, blank=True, null=True)
    tipocliente = models.CharField(max_length=3, blank=True, null=True)
    subtipocliente = models.CharField(max_length=3, blank=True, null=True)
    observacionacuerdostarifas_expo = models.TextField(blank=True, null=True)
    tienetarifanegociadaorigen = models.CharField(max_length=1, blank=True, null=True)
    agaduana_donde_vino = models.CharField(max_length=5, blank=True, null=True)
    obligatorio_fechabooking_expo = models.CharField(max_length=1, blank=True, null=True)
    codigoejecutivocobranza = models.CharField(max_length=15, blank=True, null=True)
    fechaultimaavisocobranza = models.DateTimeField(blank=True, null=True)
    observacion_ultimaavisocobranza = models.CharField(max_length=240, blank=True, null=True)
    eliminar_gastos_destino_coti = models.CharField(max_length=1, blank=True, null=True)
    nombre_corto = models.CharField(max_length=100, blank=True, null=True)
    categoriacliente = models.CharField(max_length=3, blank=True, null=True)
    cliente_tarifavip = models.CharField(max_length=1, blank=True, null=True)
    no_envia_email_primer_status = models.CharField(max_length=1, blank=True, null=True)
    no_envia_email_ningun_status = models.CharField(max_length=1, blank=True, null=True)
    urbanizacion = models.CharField(max_length=150, blank=True, null=True)
    ubigeo = models.CharField(max_length=6, blank=True, null=True)
    codigopersona_aci = models.CharField(max_length=5, blank=True, null=True)
    codigotiponegociacion = models.CharField(max_length=3, blank=True, null=True)
    tienecredito = models.CharField(max_length=1, blank=True, null=True)
    esprospecto = models.CharField(max_length=1, blank=True, null=True)
    codigoejecutivoventaprospecto = models.CharField(max_length=15, blank=True, null=True)
    fechainicioprospecto = models.DateTimeField(blank=True, null=True)
    fechafinprospecto = models.DateTimeField(blank=True, null=True)
    no_valida_vb = models.CharField(max_length=1, blank=True, null=True)
    bloquear_alerta_auto = models.CharField(max_length=1, blank=True, null=True)
    cliente_enlazado_adualink = models.CharField(max_length=1, blank=True, null=True)
    fecha_maxima_liberacion_vb = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'persona'


class Routingorder(models.Model):
    numeroroutingorder = models.CharField(primary_key=True, max_length=10)
    tipooperacion = models.CharField(max_length=1, blank=True, null=True)
    codigovia = models.CharField(max_length=3, blank=True, null=True)
    codigoshipper = models.CharField(max_length=5, blank=True, null=True)
    codigocontactoshipper = models.CharField(max_length=5, blank=True, null=True)
    codigoconsignee = models.CharField(max_length=5, blank=True, null=True)
    codigocontactoconsignee = models.CharField(max_length=5, blank=True, null=True)
    codigoejecutivoventa = models.CharField(max_length=15, blank=True, null=True)
    codigoejecutivoseguimiento = models.CharField(max_length=15, blank=True, null=True)
    codigoejecutivomanifiesto = models.CharField(max_length=15, blank=True, null=True)
    fechaemision = models.DateTimeField(blank=True, null=True)
    codigopaisorigen = models.CharField(max_length=2, blank=True, null=True)
    codigociudadpuertoorigen = models.CharField(max_length=3, blank=True, null=True)
    codigopaisdestino = models.CharField(max_length=2, blank=True, null=True)
    codigociudadpuertodestino = models.CharField(max_length=3, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    codigoagenteexterior = models.CharField(max_length=5, blank=True, null=True)
    codigoempresatransporte = models.CharField(max_length=5, blank=True, null=True)
    numeroguiamaster = models.CharField(max_length=25, blank=True, null=True)
    tipoempresatransporte = models.CharField(max_length=1, blank=True, null=True)
    numeroguiahija = models.CharField(max_length=25, blank=True, null=True)
    numerointernoguiamaster = models.CharField(max_length=10, blank=True, null=True)
    numerointernoguiahija = models.CharField(max_length=10, blank=True, null=True)
    codigoagentecoloader = models.CharField(max_length=5, blank=True, null=True)
    fechaetd = models.DateTimeField(blank=True, null=True)
    fechaeta = models.DateTimeField(blank=True, null=True)
    tipocarga = models.CharField(max_length=3, blank=True, null=True)
    tipocondicionflete = models.CharField(max_length=3, blank=True, null=True)
    tipocondicioncarga = models.CharField(max_length=3, blank=True, null=True)
    nombrenavesalida = models.CharField(max_length=60, blank=True, null=True)
    nombrenavellegada = models.CharField(max_length=60, blank=True, null=True)
    tienetrasbordo = models.CharField(max_length=1, blank=True, null=True)
    nombrenavetrasbordo = models.CharField(max_length=60, blank=True, null=True)
    puertofinaltrasbordo = models.CharField(max_length=3, blank=True, null=True)
    codigosegmentacion = models.CharField(max_length=3, blank=True, null=True)
    referenciacliente = models.CharField(max_length=240, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    tipoprioridad = models.CharField(max_length=1, blank=True, null=True)
    usuariocreacion = models.CharField(max_length=15)
    fechacreacion = models.DateTimeField()
    usuariomodificacion = models.CharField(max_length=15)
    fechamodificacion = models.DateTimeField()
    codigocommodity = models.CharField(max_length=5, blank=True, null=True)
    anocotizacion = models.CharField(max_length=4, blank=True, null=True)
    numerocotizacion = models.CharField(max_length=7, blank=True, null=True)
    esrutaejecutivoventa = models.CharField(max_length=1, blank=True, null=True)
    codigoincoterm = models.CharField(max_length=3, blank=True, null=True)
    descripcionmerca = models.TextField(blank=True, null=True)
    paisfinaltrasbordo = models.CharField(max_length=2, blank=True, null=True)
    sli = models.CharField(max_length=1, blank=True, null=True)
    numeroproforma = models.CharField(max_length=15, blank=True, null=True)
    fechacutoff = models.DateTimeField(blank=True, null=True)
    bloquearfacturacion = models.CharField(max_length=1, blank=True, null=True)
    lugarnegociado = models.CharField(max_length=1, blank=True, null=True)
    tarifaactualizada = models.CharField(max_length=1, blank=True, null=True)
    blglobelink = models.CharField(max_length=1, blank=True, null=True)
    obsanulacion = models.CharField(max_length=200, blank=True, null=True)
    esmultimodal = models.CharField(max_length=1, blank=True, null=True)
    esnvocc = models.CharField(max_length=1, blank=True, null=True)
    fechaincoterm = models.DateTimeField(blank=True, null=True)
    confirmacionfechaincoterm = models.CharField(max_length=1, blank=True, null=True)
    fechaincotermreal = models.DateTimeField(blank=True, null=True)
    codigocontactoagenteexterior = models.CharField(max_length=5, blank=True, null=True)
    ultimostatus = models.TextField(blank=True, null=True)
    codigoitemultimostatus = models.CharField(max_length=5, blank=True, null=True)
    direccionrecojoentrega = models.CharField(max_length=240, blank=True, null=True)
    fechavigenciarouting = models.DateTimeField(blank=True, null=True)
    zip_code = models.CharField(max_length=50, blank=True, null=True)
    ingresoalmacenorigen = models.DateTimeField(blank=True, null=True)
    fechacargacontenedor = models.DateTimeField(blank=True, null=True)
    fechamodificacion_pi = models.DateTimeField(blank=True, null=True)
    fechaprealertaok = models.DateTimeField(blank=True, null=True)
    prealertaok = models.CharField(max_length=1, blank=True, null=True)
    fecharecojocarga_exw = models.DateTimeField(blank=True, null=True)
    tipoemision = models.CharField(max_length=1, blank=True, null=True)
    etaprimertramo = models.DateTimeField(blank=True, null=True)
    etdprimertramo = models.DateTimeField(blank=True, null=True)
    etasegundotramo = models.DateTimeField(blank=True, null=True)
    etdsegundotramo = models.DateTimeField(blank=True, null=True)
    cantidadtransbordos = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    correlativonave = models.CharField(max_length=10, blank=True, null=True)
    seguigls = models.CharField(max_length=1, blank=True, null=True)
    fecharecepcionprealertadelagente = models.DateTimeField(blank=True, null=True)
    fechaprocesoedi = models.DateTimeField(blank=True, null=True)
    numerodua = models.CharField(max_length=50, blank=True, null=True)
    anoorden = models.CharField(max_length=4, blank=True, null=True)
    numeroorden = models.CharField(max_length=6, blank=True, null=True)
    tipodespacho = models.CharField(max_length=3, blank=True, null=True)
    fechadocumentoscompletos = models.DateTimeField(blank=True, null=True)
    etaalmacendestino = models.DateTimeField(blank=True, null=True)
    codigoaduana = models.CharField(max_length=3, blank=True, null=True)
    track_id = models.CharField(max_length=50, blank=True, null=True)
    enviocorreotarifa = models.CharField(max_length=1, blank=True, null=True)
    fechaentregabl_operaciones = models.DateTimeField(blank=True, null=True)
    fechatarja = models.DateTimeField(blank=True, null=True)
    fechalevante = models.DateTimeField(blank=True, null=True)
    canal = models.CharField(max_length=1, blank=True, null=True)
    fechaenvio_doc_aa = models.DateTimeField(blank=True, null=True)
    fechaenviotraduccion_aa = models.DateTimeField(blank=True, null=True)
    codigoagenciaaduana = models.CharField(max_length=5, blank=True, null=True)
    comentario_nacionalizacion = models.CharField(max_length=240, blank=True, null=True)
    observacion_agenciaaduana = models.CharField(max_length=3, blank=True, null=True)
    codigoclientefinal = models.CharField(max_length=5, blank=True, null=True)
    numerosolicitud = models.CharField(max_length=8, blank=True, null=True)
    atendido_cso = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    numerobooking_ro = models.CharField(max_length=30, blank=True, null=True)
    fechasolicitudbooking = models.DateTimeField(blank=True, null=True)
    fechaemisionbooking = models.DateTimeField(blank=True, null=True)
    fechaliberacionbooking = models.DateTimeField(blank=True, null=True)
    fechatransbordo = models.DateTimeField(blank=True, null=True)
    semigro_edi_cliente = models.CharField(max_length=1, blank=True, null=True)
    no_cumplimiento_destino = models.CharField(max_length=3, blank=True, null=True)
    no_cumplimiento_origen = models.CharField(max_length=3, blank=True, null=True)
    no_cumplimiento_transito = models.CharField(max_length=3, blank=True, null=True)
    valor_fob = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fecha_numeracion_dua = models.DateTimeField(blank=True, null=True)
    transbordotrabajadopor = models.CharField(max_length=3, blank=True, null=True)
    diassobreestadia = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    etd_cotizacion = models.DateTimeField(blank=True, null=True)
    eta_cotizacion = models.DateTimeField(blank=True, null=True)
    fechacierrefile = models.DateTimeField(blank=True, null=True)
    afectofechanaviera = models.CharField(max_length=1, blank=True, null=True)
    totalcantidadseries = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    observacionfinancieras = models.TextField(blank=True, null=True)
    viatransito = models.CharField(max_length=100, blank=True, null=True)
    numeroviajesalida = models.CharField(max_length=20, blank=True, null=True)
    numeroviajellegada = models.CharField(max_length=20, blank=True, null=True)
    codigocustomercare = models.CharField(max_length=15, blank=True, null=True)
    esbacktoback = models.CharField(max_length=1, blank=True, null=True)
    fecha_ultimostatus = models.DateTimeField(blank=True, null=True)
    estadobloqueo = models.CharField(max_length=1, blank=True, null=True)
    codigomotivobloqueo = models.CharField(max_length=4, blank=True, null=True)
    comentariobloqueo = models.TextField(blank=True, null=True)
    usuariobloqueo = models.CharField(max_length=15, blank=True, null=True)
    fechabloqueo = models.DateTimeField(blank=True, null=True)
    comentatiodesbloqueo = models.TextField(blank=True, null=True)
    usuariodesbloqueo = models.CharField(max_length=15, blank=True, null=True)
    fechadesbloqueo = models.DateTimeField(blank=True, null=True)
    venta_al_agente = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rebate_gamma_hbl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rebate_gamma_m3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rebate_gamma_m3_minimo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    air_importe_flete_origen = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    air_importe_gastos_origen = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    noaplica_aes = models.CharField(max_length=1, blank=True, null=True)
    gastos_no_cobrados_favor_gamma_x_ro = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fee_agente_fcl = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    codigoagenteexterior_incalines = models.CharField(max_length=5, blank=True, null=True)
    es_apll = models.CharField(max_length=1, blank=True, null=True)
    numeroviaje = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'routingorder'


class Tablageneral(models.Model):
    codigotabla = models.CharField(max_length=4)
    tipotabla = models.CharField(primary_key=True, max_length=3)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    codigoalternativo = models.CharField(max_length=7, blank=True, null=True)
    generacorrelativo = models.CharField(max_length=1, blank=True, null=True)
    usuariocreacion = models.CharField(max_length=15, blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    usuariomodificacion = models.CharField(max_length=15, blank=True, null=True)
    fechamodificacion = models.DateTimeField(blank=True, null=True)
    codigoalternativo2 = models.CharField(max_length=7, blank=True, null=True)
    codigosunat = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'tablageneral'
        unique_together = (('tipotabla', 'codigotabla'),)
