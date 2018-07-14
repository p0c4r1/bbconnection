from __future__ import unicode_literals

from django.db import models
from django.db.models import ExpressionWrapper,F,Sum,DecimalField
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
import datetime
from datetime import date
from collections import defaultdict
from num2words import num2words



class Parameters(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Name"))
    char_value = models.CharField(max_length=100,verbose_name=_("Char value"),null=True,blank=True)
    num_value = models.IntegerField(verbose_name=_("Numeric value"),null=True,blank=True)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('parameters_detail', args=[str(self.id)])
    
    def __str__(self):
        return "%s %s %s" % (self.name,self.char_value,self.num_value)

    class Meta:
        verbose_name = _("Parameter")
        verbose_name_plural = _("Parameters")

class Priority(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Group Name"))
    ext_code = models.CharField(max_length=30,verbose_name=_("External code"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('priority_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Priority")
        verbose_name_plural = _("Priorities")
        
class Insurance(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Insurence Name"))
    ext_code = models.CharField(max_length=30,verbose_name=_("External code"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('insurence_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Insurence")
        verbose_name_plural = _("Insurences")
        
class Doctors(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Doctor Name"))
    ext_code = models.CharField(max_length=30,verbose_name=_("External code"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('doctors_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")
        
class Origins(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Origin Name"))
    ext_code = models.CharField(max_length=30,verbose_name=_("External code"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('origins_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Origin")
        verbose_name_plural = _("Origins")
        
        
class Diagnosis(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Diangosis Name"))
    ext_code = models.CharField(max_length=30,verbose_name=_("External code"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('diagnosis_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Diagnosis")
        verbose_name_plural = _("Diagnosis")
        
class Genders(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Gender Name"))
    code = models.CharField(max_length=30,verbose_name=_("Code"),null=True)
    ext_code = models.CharField(max_length=30,verbose_name=_("External code"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('priority_detail', args=[str(self.id)])
    
    def __str__(self):
        return ('%s (%s)' % (self.name,self.ext_code))

    class Meta:
        verbose_name = _("Gender")
        verbose_name_plural = _("Genders")
        
        
class Specimens(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Specimen Name"))
    suffix_code = models.CharField(max_length=3,verbose_name=_("Suffix code"))
    
    def get_absolute_url(self):
        return reverse('specimen_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Specimen")
        verbose_name_plural = _("Specimens")
        
class SuperGroups(models.Model):
    abbreviation = models.CharField(max_length=100,verbose_name=_("Abbreviation"))
    name = models.CharField(max_length=100,verbose_name=_("Name"))
    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s %s" % (self.abbreviation,self.name)

class TestGroups(models.Model):
    supergroup = models.ForeignKey(SuperGroups,on_delete=models.PROTECT,verbose_name=_("Super Group"),related_name='testgroup_supergroup',null=True)
    name = models.CharField(max_length=100,verbose_name=_("Group Name"))
    sort = models.IntegerField(verbose_name=_("Sort"),help_text=_("Sorted priority"))
    dateofcreation = CreationDateTimeField(verbose_name=_("Created at"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('testgroups_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Test group")
        verbose_name_plural = _("Test groups")
        permissions = (
            ('view_testgroups', 'Can view testgroups'),
        )
        ordering = ['name']
        
        
TEST_RESULT_TYPE = (
    ('NUM','NUMERIC'),
    ('ALF','ALFANUMERIC'),
    ('TXT','TEXT'),
    ('IMG','IMAGE')
    )        
class Tests(models.Model):
    NUMERIC = 'NUM'
    ALFANUMERIC = 'ALF'
    TEXT = 'TXT'
    IMAGE = 'IMG'
    test_group = models.ForeignKey(TestGroups,on_delete=models.PROTECT,verbose_name=_("Test Group"),related_name='tests')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    name = models.CharField(max_length=100,verbose_name=_("Test Name"),null=True)
    result_type =  models.CharField(
        max_length=3,
        verbose_name=_("Result Type"),
        choices=TEST_RESULT_TYPE,
        default=NUMERIC,
    )
    specimen = models.ForeignKey(Specimens,on_delete=models.PROTECT,verbose_name=_("Specimen"),related_name='test_specimen',null=True)
    can_request = models.BooleanField(verbose_name=_("Can request?"), default=True,blank=True)
    sort = models.IntegerField(verbose_name=_("Sort"),help_text=_("Sorted priority"))
    ext_code = models.CharField(max_length=30,verbose_name=_("External code"))
    dateofcreation = CreationDateTimeField(verbose_name=_("Created at"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('tests_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")
        permissions = (
            ('view_tests', 'Can view tests'),
        )
        ordering = ['test_group','name']
    
    
    
class TestPrices(models.Model):
    test = models.ForeignKey(Tests,on_delete=models.PROTECT,verbose_name=_("Test"),related_name='test_price')
    priority = models.ForeignKey(Priority,on_delete=models.PROTECT,verbose_name=_("Priority"))
    tariff = models.DecimalField(decimal_places=2, max_digits=20,verbose_name=_("tariff"),help_text=_("base tariff"))
    service = models.DecimalField(decimal_places=2, max_digits=20,verbose_name=_("Medc.Serv"),help_text=_("Medical service rate"))
    dateofcreation = CreationDateTimeField(verbose_name=_("Created at"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('testprices_detail', args=[str(self.id)])
    
    def __str__(self):
        return '%s %s' % (self.test,self.priority)

    class Meta:
        verbose_name = _("Test price")
        verbose_name_plural = _("Test prices")
        permissions = (
            ('view_testprices', 'Can view test prices'),
        )
        ordering = ['test','priority']
        
class Patients(models.Model):
    patient_id = models.CharField(max_length=100,verbose_name=_("Patient ID"),help_text=_("Medical record number"),unique=True)
    name = models.CharField(max_length=100,verbose_name=_("Name"),help_text=_("Patient Name"))
    gender = models.ForeignKey(Genders,on_delete=models.PROTECT,verbose_name=_("Gender"))
    dob = models.DateField(verbose_name=_("Date of birth"),help_text=_("Date format: DD-MM-YYYY"))
    address = models.CharField(max_length=100,verbose_name=_("Address"),help_text=_("Patient Address"))
    data0 = models.CharField(max_length=100,verbose_name=_("Data 0"),help_text=_("Additional data 0"),blank=True,null=True)
    data1 = models.CharField(max_length=100,verbose_name=_("Data 1"),help_text=_("Additional data 1"),blank=True,null=True)
    data2 = models.CharField(max_length=100,verbose_name=_("Data 2"),help_text=_("Additional data 3"),blank=True,null=True)
    dateofcreation = CreationDateTimeField(verbose_name=_("Created at"),null=True)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True) 
    
    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])
    
    def calculate_age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
    def create_order(self):
        order = Orders(patient=self)
        #order.doctor_id = 1
        #order.origin_id = 1
        #order.insurence_id = 1
        #order.priority_id = 1
        #order.lastmodifiedby_id = 1
        order.save()
        return order
    
    def __str__(self):
        return '%s %s' % (self.patient_id,self.name)

    class Meta:
        verbose_name = _("Patient")
        verbose_name_plural = _("Patients")
        permissions = (
            ('view_patients', 'Can view test patients'),
        )
        ordering = ['patient_id','name']
        
def auto_order_no():
        dtf = datetime.datetime.today().strftime('%y%m%d')
        par = Parameters.objects.filter(name='ORDER_NO',char_value=dtf)
        if par.count()==0:
            Parameters.objects.filter(name='ORDER_NO').delete()
            par = Parameters(name='ORDER_NO',char_value=dtf,num_value=1)
            par.save()
        par = Parameters.objects.filter(name='ORDER_NO',char_value=dtf)
        id = par.values('id')[0]['id']
        num_value = int(par.values('num_value')[0]['num_value'])
        par_upd = Parameters.objects.get(pk=id)
        par_upd.num_value=num_value+1
        par_upd.save()
        return dtf + ("%04d" % (num_value,))
    
    
class Orders(models.Model):
    order_date = models.DateField(verbose_name=_("Order date"),auto_now_add=True)
    number = models.CharField(max_length=100,verbose_name=_("Number"),default=auto_order_no,blank=True,null=True,unique=True)
    origin = models.ForeignKey(Origins,on_delete=models.PROTECT,verbose_name=_("Origin"),null=True,blank=True)
    doctor = models.ForeignKey(Doctors,on_delete=models.PROTECT,verbose_name=_("Sender doctor"),null=True,blank=True)
    diagnosis = models.ForeignKey(Diagnosis,on_delete=models.PROTECT,verbose_name=_("Diagnosis"),null=True,blank=True)
    priority = models.ForeignKey(Priority,on_delete=models.PROTECT,verbose_name=_("Order priority"),null=True,blank=True)
    insurance = models.ForeignKey(Insurance,on_delete=models.PROTECT,verbose_name=_("Insurance"),null=True,blank=True)
    note = models.CharField(max_length=100,verbose_name=_("Note/Comment"),blank=True,null=True)
    patient = models.ForeignKey(Patients,on_delete=models.PROTECT,verbose_name=_("Patient"))
    conclusion = models.CharField(max_length=1000,verbose_name=_("Conclusion"),blank=True,null=True)
    dateofcreation = CreationDateTimeField(verbose_name=_("Created at"),auto_now_add=True)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    #objects = OrdersManager()
    
    def has_tests(self):
        if OrderTests.objects.filter(order_id=self.pk).count() > 0:
            return True
        else:
            return False
    
    def get_tests(self):
        return Orders.objects.filter(pk=self.pk,
                                     order_items__test__test_price__priority=self.priority).values_list(
                                         'order_items__test__name',flat=True)
    
    def get_test_str(self):
        order_result = Orders.objects.filter(pk=self.pk,
                                     order_items__test__test_price__priority=self.priority).values_list(
                                         'order_items__test__name',flat=False)
        data = [entry[0] for entry in order_result]
        return ", ".join(map(str,data))
                            
                                     
    def get_test_price(self):
        return Orders.objects.filter(pk=self.pk,
                                     order_items__test__test_price__priority=self.priority).values(
                                         'order_items__test__name',
                                         'order_items__test__test_price__tariff',
                                         'order_items__test__test_price__service').annotate(
                                             sub_total=ExpressionWrapper(
                                                 F('order_items__test__test_price__tariff') + F('order_items__test__test_price__service'),
                                                 output_field=DecimalField(decimal_places=2) )
                                                                                            )
    def get_total_price(self):
        return Orders.objects.filter(pk=self.pk,
                                     order_items__test__test_price__priority=self.priority).aggregate(
                                         total=Sum(F('order_items__test__test_price__tariff')
                                                   +F('order_items__test__test_price__service'))
                                         )
    def get_sub_total_price(self):
        return Orders.objects.filter(pk=self.pk,
                                     order_items__test__test_price__priority=self.priority).aggregate(
                                         tariff_subtotal=Sum(F('order_items__test__test_price__tariff')),
                                         service_subtotal=Sum(F('order_items__test__test_price__service'))
                                         )   
    def get_sub_total_price_tariff(self):
        return Orders.objects.filter(pk=self.pk,
                                     order_items__test__test_price__priority=self.priority).aggregate(
                                         tariff_subtotal=Sum(F('order_items__test__test_price__tariff'))
                                         ).values()[0]
    def get_sub_total_price_service(self):
        return Orders.objects.filter(pk=self.pk,
                                     order_items__test__test_price__priority=self.priority).aggregate(
                                         tariff_subtotal=Sum(F('order_items__test__test_price__service'))
                                         ).values()[0]
                                                                      
    def get_total_price_words(self):
        return num2words(int(self.get_total_price()['total']),lang='id')
    
    def get_absolute_url(self):
        return reverse('orders_detail', args=[str(self.id)])
        
    def __str__(self):
        return '%s %s' % (self.number,self.patient)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        permissions = (
            ('view_orders', 'Can view orders'),
        )
        ordering = ['number','origin']

class OrderTests(models.Model):
    order = models.ForeignKey(Orders,on_delete=models.PROTECT,verbose_name=_("Order"),related_name='order_items')
    test = models.ForeignKey(Tests,on_delete=models.PROTECT,verbose_name=_("Test"),related_name='order_tests')
    dateofcreation = CreationDateTimeField(verbose_name=_("Created at"),auto_now_add=True)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('ordertests_detail', args=[str(self.id)])
    
    def __str__(self):
        return '%s %s' % (self.order,self.test)

    class Meta:
        verbose_name = _("Order test")
        verbose_name_plural = _("Order tests")
        permissions = (
            ('view_ordertests', 'Can view order tests'),
        )
        ordering = ['order','test']

class OrderSamples(models.Model):
    order = models.ForeignKey(Orders,on_delete=models.PROTECT,verbose_name=_("Order"),related_name='sample_order')
    specimen = models.ForeignKey(Specimens,on_delete=models.PROTECT,verbose_name=_("Specimen"),related_name='sample_specimen')
    sample_no = models.CharField(max_length=100,verbose_name=_("sample id"),help_text=_("Sample id"))
    dateofcreation = CreationDateTimeField(verbose_name=_("Created at"),auto_now_add=True)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('ordersamples_detail', args=[str(self.id)])
    
    def __str__(self):
        return '%s' % (self.sample_no)

    class Meta:
        verbose_name = _("Order samples")
        verbose_name_plural = _("Order samples")
        permissions = (
            ('view_ordersamples', 'Can view order samples'),
        )
        ordering = ['order','sample_no']
        
class LabelPrinters(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Name"),help_text=_("Printer barcode name"))
    active = models.BooleanField(default=True,verbose_name=_("is active?"))
    com_port = models.CharField(max_length=100,verbose_name=_("Com serial port name"),help_text=_("eq: COM10,COM11"))
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_absolute_url(self):
        return reverse('ordersamples_detail', args=[str(self.id)])
    
    def __str__(self):
        return '%s (%s)' % (self.name,self.com_port)
    
    
    
    
#### Lab Model #########
#######################
class ReceivedSamples(models.Model):
    order =  models.ForeignKey(Orders,on_delete=models.PROTECT,verbose_name=_("Order"),related_name='receivedsamples_order')
    sample =  models.ForeignKey(OrderSamples,on_delete=models.PROTECT,verbose_name=_("Specimen"),related_name='receivedsamples_tube')
    supergroup = models.ForeignKey(SuperGroups,on_delete=models.PROTECT,verbose_name=_("Super Group"),related_name='receivedsamples_supergrup')
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s%s" % (self.order.number,self.suffix)

CONN_TYPE = (
    ('SER','Serial'),
    ('TCP','TCP/IP')
    )
SER_PORT = (
    ('COM1','COM1'),
    ('COM2','COM2'),
    ('COM3','COM3'),
    ('COM4','COM4'),
    ('COM5','COM5'),
    ('COM6','COM6'),
    ('COM7','COM7'),
    ('COM8','COM8'),
    ('COM9','COM9'),
    ('COM10','COM10'),
    ('COM11','COM11'),
    ('COM12','COM12'),
    ('COM13','COM13'),
    ('COM14','COM14'),
    ('COM15','COM15'),
    ('COM16','COM16'),
    ('COM17','COM17'),
    ('COM18','COM18'),
    ('COM19','COM19'),
    ('COM20','COM20'),
    ('COM21','COM21'),
    ('COM22','COM22'),
    ('COM23','COM23'),
    ('COM24','COM24'),
    ('COM25','COM25'),
    ('COM26','COM26'),
    ('COM27','COM27'),
    ('COM28','COM28'),
    ('COM29','COM29'),
    ('COM30','COM30'),
    ('COM31','COM31'),
    ('COM32','COM32'),
    ('COM33','COM33'),
    ('COM34','COM34'),
    ('COM35','COM35'),
    ('COM36','COM36'),
    ('COM37','COM37'),
    ('COM38','COM38'),
    ('COM39','COM39'),
    ('COM40','COM40')
    )
SER_BAUDRATE = (
    ('9600','9600'),
    ('19200','19200')
    )
SER_DATABIT = (
    ('7','7'),
    ('8','8')
    )
SER_STOPBIT = (
    ('1','1'),
    ('2','2')
    )
SER_PARITY = (
    ('N','None'),
    ('E','Even')
    )
TCP_TYPE = (
    ('S','Server'),
    ('C','Client')
    )
class Instruments(models.Model):
    code = models.CharField(max_length=10,verbose_name=_("Code"),unique=True)
    name = models.CharField(max_length=100,verbose_name=_("Name"))
    active = models.BooleanField(verbose_name=_("Active?"), default=True,blank=True)
    driver = models.CharField(max_length=100,verbose_name=_("Driver name"),blank=True,null=True)
    connection_type = models.CharField(
        max_length=3,
        verbose_name=_("Connection type"),
        choices=CONN_TYPE,
        null=True,
        blank=True,
    )
    serial_port = models.CharField(
        max_length=3,
        verbose_name=_("Serial port name"),
        choices=SER_PORT,
        null=True,
        blank=True,
    )
    serial_baud_rate = models.CharField(
        max_length=3,
        verbose_name=_("Serial baud rate"),
        choices=SER_BAUDRATE,
        null=True,
        blank=True,
    ) 
    serial_data_bit = models.CharField(
        max_length=3,
        verbose_name=_("Serial data bit"),
        choices=SER_DATABIT,
        null=True,
        blank=True,
    )
    serial_stop_bit = models.CharField(
        max_length=3,
        verbose_name=_("Serial stop bit"),
        choices=SER_STOPBIT,
        null=True,
        blank=True,
    )
    serial_data_bit = models.CharField(
        max_length=3,
        verbose_name=_("Serial parity"),
        choices=SER_PARITY,
        null=True,
        blank=True,
    )
    tcp_conn_type = models.CharField(
        max_length=3,
        verbose_name=_("TCP/IP Connection type"),
        choices=TCP_TYPE,
        null=True,
        blank=True,
    )
    tcp_host = models.GenericIPAddressField(verbose_name=_("TCP Host name (IP Address)"),blank=True,null=True)
    tcp_port = models.IntegerField(verbose_name=_("TCP Port"),blank=True,null=True)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s" % (self.name)


REST_INST_TYPE = (
    ('R','RAW'),
    ('N','NUMBERIC'),
    ('A','ALFANUMERIC')
    )
class InstrumentTests(models.Model):
    instrument =  models.ForeignKey(Instruments,on_delete=models.PROTECT,verbose_name=_("Instrument"),related_name='instrumentflags_instrument')
    test =  models.ForeignKey(Tests,on_delete=models.PROTECT,verbose_name=_("Test"),related_name='instrumentflags_test')
    test_code = models.CharField(max_length=100,verbose_name=_("Host test code"))
    result_type = models.CharField(
        max_length=3,
        verbose_name=_("Result type"),
        choices=REST_INST_TYPE,
        default = 'R',
    )
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s %s" % (self.instrument,self.test)

class InstrumentFlags(models.Model):
    instrument =  models.ForeignKey(Instruments,on_delete=models.PROTECT,verbose_name=_("Instrument"),related_name='instrumenttests_instrument')
    flag_code = models.CharField(max_length=100,verbose_name=_("Host flag code"))
    flag_description = models.CharField(max_length=100,verbose_name=_("Host flag description"))
    flag_mark = models.CharField(max_length=100,verbose_name=_("Host flag mark"),null=True,blank=True)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s %s" % (self.instrument,self.flag_code)
 
AGE_UNIT = (
    ('D','DAY'),
    ('M','MONTH'),
    ('Y','YEAR')
    )
REF_OPERATOR = (
    ('-','NA'),
    ('>','GT'),
    ('>=','GTE'),
    ('<','LT'),
    ('<=','LTE'),
    )   
class TestRefRanges(models.Model):
    DAY = 'D'
    MONTH = 'M'
    YEAR = 'Y'
    NA ='-'
    GT = '>'
    GTE = '>='
    LT = '<'
    LTE = '<='
    test = models.ForeignKey(Tests,on_delete=models.PROTECT,verbose_name=_("Test"),related_name='refranges_test')
    gender = models.ForeignKey(Genders,on_delete=models.PROTECT,verbose_name=_("Gender"),related_name='refranges_gender',blank=True,null=True)
    age_from = models.IntegerField(verbose_name=_("Age from"), null=True,blank=True)
    age_from_type =  models.CharField(
        max_length=3,
        verbose_name=_("Age from unit"),
        choices=AGE_UNIT,
        null=True,
        blank=True,
    )
    age_to = models.IntegerField(verbose_name=_("Age to"), null=True,blank=True)
    age_to_type =  models.CharField(
        max_length=3,
        verbose_name=_("Age to unit"),
        choices=AGE_UNIT,
        null=True,
        blank=True,
    )
    operator = models.CharField(
        max_length=3,
        verbose_name=_("Operator"),
        choices=REF_OPERATOR,
        null=True,
        blank=True,
    )
    any_age = models.BooleanField(verbose_name=_("Any age?"), default=True,blank=True)
    lower = models.IntegerField(verbose_name=_("lower limit"), null=True,blank=True)
    upper = models.IntegerField(verbose_name=_("upper limit"), null=True,blank=True)
    operator_value = models.IntegerField(verbose_name=_("operator value"), null=True,blank=True)
    alfa_value = models.CharField(max_length=100,verbose_name=_("Alfanumberic value"),null=True,blank=True)
    special_info = models.TextField(verbose_name=_("Special information"),null=True,blank=True)

    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s" % (self.test)
    
    
    
class Results(models.Model):
    order =  models.ForeignKey(Orders,on_delete=models.PROTECT,verbose_name=_("Order"),related_name='results_order')
    test = models.ForeignKey(Tests,on_delete=models.PROTECT,verbose_name=_("Test"),related_name='results_test')
    numeric_result = models.FloatField(verbose_name=_("Numeric result"),null=True)
    alfa_result = models.CharField(max_length=100,verbose_name=_("Alfanumeric result"),null=True)
    text_result = models.TextField(verbose_name=_("Text result"),null=True)
    image_result = models.BinaryField(verbose_name=_("Image result"),null=True)
    ref_range = models.CharField(max_length=100,verbose_name=_("Reference range"),null=True)
    mark = models.CharField(max_length=3,verbose_name=_("Result mark"),null=True)
    instrument =  models.ForeignKey(Instruments,on_delete=models.PROTECT,verbose_name=_("Instrument"),related_name='results_instrument',null=True)
    flag = models.ForeignKey(InstrumentFlags,on_delete=models.PROTECT,verbose_name=_("Instrument flag"),related_name='results_instrumentflag',null=True,)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        
    def get_patient_age_in_day(self):
        return (self.order.order_date - self.order.patient.dob).days
             
    def setup_range(self,alfa_value=None,operator=None,operator_value=None,lower=None,upper=None):
        if alfa_value:
            self.ref_range = alfa_value
            if self.alfa_result <> str(alfa_value):
                self.mark = 'A'
        else:
            # numeric range
            if operator:
                self.ref_range = str(operator)+' '+str(operator_value)
                if self.is_number(self.alfa_result):
                    # GT
                    if str(operator)=='>':
                        if float(self.alfa_result)<=float(operator_value):
                            self.mark = 'L'
                    if str(operator)=='>=':
                        if float(self.alfa_result)<float(operator_value):
                            self.mark = 'L'
                    if str(operator)=='<':
                        if float(self.alfa_result)>=float(operator_value):
                            self.mark = 'H'
                    if str(operator)=='<=':
                        if float(self.alfa_result)>float(operator_value):
                            self.mark = 'H'
            else:
                # range
                self.ref_range = str(lower)+' - '+str(upper)
                if self.alfa_result:
                    if self.is_number(self.alfa_result):
                        if float(self.alfa_result)<float(lower):
                            self.mark = 'L'
                        if float(self.alfa_result)>float(upper):
                            self.mark = 'H'
                     
   
    def save(self, *args, **kwargs):
        refrange = TestRefRanges.objects.filter(test=self.test).values('any_age','gender','age_from_type','age_from','age_to','operator','operator_value','lower','upper','alfa_value','special_info','gender_id')
        if refrange.count()>0:
            for range in refrange:
                # any age & any gender
                if range['any_age']:
                    # check gender
                    if not range['gender']:
                        self.setup_range(alfa_value=range['alfa_value'],
                                         operator=range['operator'],
                                         operator_value=range['operator_value'],
                                         lower=range['lower'],
                                         upper=range['upper'])
                                        
                    else:
                        # gender set
                        if range['gender'] == self.order.patient.gender_id:
                            self.setup_range(alfa_value=range['alfa_value'],
                                         operator=range['operator'],
                                         operator_value=range['operator_value'],
                                         lower=range['lower'],
                                         upper=range['upper'])
                else:
                    # date range
                    # Days
                    if range['age_from_type']=='D':
                        #print str((self.order.order_date - self.order.patient.dob).days)
                        if int(range['age_from']) <= (self.order.order_date - self.order.patient.dob).days <= int(range['age_to']):
                            if (not range['gender']) or (range['gender'] == self.order.patient.gender_id) :
                                self.setup_range(alfa_value=range['alfa_value'],
                                         operator=range['operator'],
                                         operator_value=range['operator_value'],
                                         lower=range['lower'],
                                         upper=range['upper'])
                    # Months
                    if range['age_from_type']=='M':
                        if int(range['age_from']) <= (self.order.order_date - self.order.patient.dob).months <= int(range['age_to']):
                            if (not range['gender']) or (range['gender'] == self.order.patient.gender_id) :
                                self.setup_range(alfa_value=range['alfa_value'],
                                         operator=range['operator'],
                                         operator_value=range['operator_value'],
                                         lower=range['lower'],
                                         upper=range['upper'])
                    # Years
                    if range['age_from_type']=='Y':
                        if int(range['age_from']) <= (self.order.order_date - self.order.patient.dob).months <= int(range['age_to']):
                            if (not range['gender']) or (range['gender'] == self.order.patient.gender_id) :
                                self.setup_range(alfa_value=range['alfa_value'],
                                         operator=range['operator'],
                                         operator_value=range['operator_value'],
                                         lower=range['lower'],
                                         upper=range['upper'])
                                
                            
                #print range
        
        super(Results, self).save(*args, **kwargs)
    
    def __str__(self):
        return "%s %s %s %s" % (self.order,self.numeric_result,self.alfa_result,self.text_result)
    
class TestParameters(models.Model):
    test = models.OneToOneField(Tests,on_delete=models.CASCADE,primary_key=True,)
    method = models.CharField(max_length=100,verbose_name=_("Method"),null=True,blank=True)
    unit = models.CharField(max_length=100,verbose_name=_("Test unit"),null=True,blank=True)
    decimal_place = models.IntegerField(verbose_name=_("Decimal place"),null=True,default=1)
    special_information = models.CharField(max_length=1000,verbose_name=_("Special information"),null=True,blank=True)
    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s" % (self.test)


class OrderResults(models.Model):
    order =  models.ForeignKey(Orders,on_delete=models.PROTECT,verbose_name=_("Order"),related_name='orderresults_order')
    sample = models.ForeignKey(OrderSamples,on_delete=models.PROTECT,verbose_name=_("Order Sample"),related_name='sampleresults_order',null=True)
    test = models.ForeignKey(Tests,on_delete=models.PROTECT,verbose_name=_("Test"),related_name='orderresults_test')
    is_header = models.BooleanField(default=False,verbose_name=_("is header?"))
    result = models.ForeignKey(Results,on_delete=models.PROTECT,verbose_name=_("Result"),related_name='orderresults_result',null=True)
    unit = models.CharField(max_length=100,verbose_name=_("Result unit"),null=True)
    ref_range = models.CharField(max_length=200,verbose_name=_("Reference range"),null=True)
    patologi_mark = models.CharField(max_length=20,verbose_name=_("Patologi mark"),null=True)
    validation_status = models.IntegerField(verbose_name=_("Validation status"),default=0)
    techval_user = models.CharField(max_length=20,verbose_name=_("Techical validated by"),null=True)
    techval_date = models.DateTimeField(verbose_name=_("Technical Validated date"),null=True)
    medval_user = models.CharField(max_length=20,verbose_name=_("Medical validated by"),null=True)
    medval_date = models.DateTimeField(verbose_name=_("Medical validated date"),null=True)
    print_status = models.IntegerField(verbose_name=_("Print status"),default=0)
    print_user = models.CharField(max_length=20,verbose_name=_("Print by"),null=True)
    print_date = models.DateTimeField(verbose_name=_("Print date"),null=True)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s %s %s" % (self.order,self.test,self.result)
    
    def previous_result(self):
        return 'xxx'
    
class HistoryOrders(models.Model):
    order =  models.ForeignKey(Orders,on_delete=models.PROTECT,verbose_name=_("Order"),related_name='historyorder_order')
    test = models.ForeignKey(Tests,on_delete=models.PROTECT,verbose_name=_("Test"),related_name='historyorder_test',null=True)
    action_code = models.CharField(max_length=20,verbose_name=_("Action code"),null=True)
    action_user = models.CharField(max_length=20,verbose_name=_("Action by"),null=True)
    action_date = models.DateTimeField(verbose_name=_("Action date"),null=True)
    action_text = models.CharField(max_length=1000,verbose_name=_("Action text"),null=True)
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s %s %s" % (self.order,self.test,self.action_text)
    
    
class OrderExtended(models.Model):
    order = models.OneToOneField(Orders,on_delete=models.CASCADE,primary_key=True,)
    result_pdf_url = models.CharField(max_length=500,verbose_name=_("Result PDF url"),null=True)
    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def get_progress(self):
        ores = OrderResults.objects.filter(order=self.order,validation_status=0,is_header=0)
        if ores.count()>0:
            return 0
        ores = OrderResults.objects.filter(order=self.order,validation_status=1,is_header=0)
        if ores.count()>0:
            return 25
        ores = OrderResults.objects.filter(order=self.order,validation_status=2,is_header=0)
        if ores.count()>0:
            return 50
        ores = OrderResults.objects.filter(order=self.order,validation_status=3,is_header=0)
        if ores.count()>0:
            return 75
        ores = OrderResults.objects.filter(order=self.order,validation_status=4,is_header=0)
        if ores.count()>0:
            return 100
        
    
    def __str__(self):
        return "%s" % (self.order)
    
    
class BatchGroups(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Name"))
    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s" % (self.name)

class BatchGroupTests(models.Model):
    batch_group =  models.ForeignKey(BatchGroups,on_delete=models.PROTECT,verbose_name=_("Batch group"),related_name='batchtest_batchgroup')
    test = models.ForeignKey(Tests,on_delete=models.PROTECT,verbose_name=_("Test"),related_name='batchgroup_test')
    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s - %s" % (self.batch_group,self.test)

    
class Worklists(models.Model):
    batch_date = models.DateField(verbose_name=_("Batch date"),auto_now_add=True)
    batch_group =  models.ForeignKey(BatchGroups,on_delete=models.PROTECT,verbose_name=_("Batch group"),related_name='worklist_batchgroup')
    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)

    def get_absolute_url(self):
        return reverse('worklists_detail', args=[str(self.id)])
    
    def __str__(self):
        return "%s - %s" % (self.batch_date,self.batch_group)
    
class WorklistOrders(models.Model):
    worklist =  models.ForeignKey(Worklists,on_delete=models.PROTECT,verbose_name=_("Worklist"),related_name='worklist_order')
    order =  models.ForeignKey(Orders,on_delete=models.PROTECT,verbose_name=_("Order"),related_name='worklistorder_order')
    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)

class WorklistTests(models.Model):
    worklistorder =  models.ForeignKey(WorklistOrders,on_delete=models.PROTECT,verbose_name=_("Worklist order"),related_name='worklisttest_worklistorder')
    test = models.ForeignKey(Tests,on_delete=models.PROTECT,verbose_name=_("Test"),related_name='worklisttest_test')
    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s - %s - %s" % (self.worklist,self.order,self.test)
    
    
class Hosts(models.Model):
    code = models.CharField(max_length=10,verbose_name=_("Code"),unique=True)
    name = models.CharField(max_length=100,verbose_name=_("Name"))
    active = models.BooleanField(verbose_name=_("Active?"), default=True,blank=True)
    input_path = models.CharField(max_length=100,verbose_name=_("input path"))
    
    lastmodification = ModificationDateTimeField(verbose_name=_("Last modified"))
    lastmodifiedby = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True},
        blank=True, verbose_name=_("Last modified by"), null=True)
    
    def __str__(self):
        return "%s - %s" % (self.code,self.name)
    
    
    
    
@receiver(models.signals.post_save, sender=Worklists)
def create_worklist_test(sender, instance, created, **kwargs):
    if created:
        have_test = False
        res_pend = OrderResults.objects.filter(validation_status=0).all()
        for rp in res_pend:
            if BatchGroupTests.objects.filter(batch_group=instance.batch_group,test=rp.test).exists():
                if not WorklistTests.objects.filter(worklistorder__order=rp.order,test=rp.test).exists():
                    # insert
                    wl_order,msg = WorklistOrders.objects.get_or_create(worklist=instance,order=rp.order)
                    wl_tes = WorklistTests(worklistorder=wl_order,test=rp.test)
                    wl_tes.save()
                    have_test = True
                    
        if not have_test:
            instance.delete()
        

    