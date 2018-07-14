from django.contrib import admin
from .models import Tests,TestPrices,TestGroups,Priority,Insurance,Doctors, \
Genders,Patients,Orders,OrderTests,Parameters,Origins,Diagnosis,SuperGroups, \
Specimens,LabelPrinters,Instruments,Results,OrderResults,TestParameters, \
TestRefRanges,InstrumentTests,InstrumentFlags,BatchGroups,BatchGroupTests

class TestsInline(admin.TabularInline):
    model = Tests
    
class TestPriceInline(admin.TabularInline):
    model = TestPrices

class BatchgroupTestsInline(admin.TabularInline):
    model = BatchGroupTests

class TestGroupAdmin(admin.ModelAdmin):
    search_fields = ['name','sort']
    list_display = ('name','sort')
    inlines = [
        TestsInline,
    ]
    
class LabelPrinterAdmin(admin.ModelAdmin):
    list_display = ('name','active','com_port')
    list_filter = ('name','active',)

class ParAdmin(admin.ModelAdmin):
    search_fields = ['name','char_value','num_value']
    list_display = ('name','char_value','num_value')
    
class NameSortdmin(admin.ModelAdmin):
    search_fields = ['name','sort']
    list_display = ('name','sort')
    
class NameExtAdmin(admin.ModelAdmin):
    search_fields = ['name','ext_code']
    list_display = ('name','ext_code')
    
class NameSuffixAdmin(admin.ModelAdmin):
    search_fields = ['name','suffix_code']
    list_display = ('name','suffix_code')
    
class TestAdmin(admin.ModelAdmin):
    search_fields = ['sort','name']
    list_display = ('sort','test_group','name','specimen','can_request','ext_code')
    list_filter = ('test_group__name','can_request',)
    inlines = [
        TestPriceInline,
    ]
    
    
class InstTestInline(admin.TabularInline):
    model = InstrumentTests

class TestAdmin2(admin.ModelAdmin):
    list_display = ('test','unit','decimal_place','method','special_information')
    search_fields = ['test','unit','decimal_place','method','special_information']
    list_filter = ('unit','decimal_place','method','special_information')
    
class TestRefAdmin(admin.ModelAdmin):
    list_display = ('test','gender','age_from','age_from_type','age_to','age_to_type','operator', \
                    'any_age','lower','upper','operator_value','alfa_value','special_info')
    list_filter = ('gender','operator','any_age','alfa_value')
    search_fields = ['test','gender','age_from','age_from_type','age_to','age_to_type','operator', \
                    'any_age','lower','upper','operator_value','alfa_value','special_info']

class InstTestAdmin(admin.ModelAdmin):
    list_display = ('instrument','test','test_code','result_type')
    

class InstAdmin(admin.ModelAdmin):
    list_display = ('code','name','active','driver','connection_type','serial_port','serial_baud_rate','serial_data_bit','serial_stop_bit',\
                    'serial_data_bit','tcp_conn_type','tcp_host','tcp_port')
    list_filter = ('code','name','active','driver','connection_type')
    search_fields = ['code','name','active','driver','connection_type','serial_port','serial_baud_rate','serial_data_bit','serial_stop_bit',\
                    'serial_data_bit','tcp_conn_type','tcp_host','tcp_port']
    inlines = [
        InstTestInline,
    ]
    
    
class BatchGroupAdmin(admin.ModelAdmin):
    inlines = [
        BatchgroupTestsInline,
    ]
    



    

admin.site.register(Parameters,ParAdmin)
admin.site.register(Tests,TestAdmin)
admin.site.register(TestPrices)
admin.site.register(TestGroups,TestGroupAdmin)
admin.site.register(Priority,NameExtAdmin)
admin.site.register(Origins,NameExtAdmin)
admin.site.register(Insurance,NameExtAdmin)
admin.site.register(Doctors,NameExtAdmin)
admin.site.register(Genders,NameExtAdmin)
admin.site.register(Patients)
admin.site.register(Orders)
admin.site.register(OrderTests)
admin.site.register(Diagnosis)
admin.site.register(SuperGroups)
admin.site.register(Specimens,NameSuffixAdmin)
admin.site.register(LabelPrinters,LabelPrinterAdmin)
admin.site.register(BatchGroups,BatchGroupAdmin)
admin.site.register(Instruments,InstAdmin)
admin.site.register(InstrumentTests,InstTestAdmin)
admin.site.register(InstrumentFlags)
admin.site.register(Results)
admin.site.register(OrderResults)
admin.site.register(TestParameters,TestAdmin2)
admin.site.register(TestRefRanges,TestRefAdmin)





