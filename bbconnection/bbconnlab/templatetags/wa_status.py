from django import template
register = template.Library()

from ..models import OrderResults,Tests,Workarea,WorkareaTestGroups
from django.utils.html import format_html

@register.filter
def status_of_wa(wa_id,order_id):
    wa_group = Workarea.objects.get(pk=wa_id)
    test_group = WorkareaTestGroups.objects.filter(workarea=wa_group).values('testgroup')

    
    
    
    
    html_div = """<td class="progs"><div class="progress progress-striped">         
<div class="progress-bar progress-bar-success" role="progressbar" style="width: 75%;">
         &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;        
</div>
</div>
</td>
"""
    #return format_html(html_div)
    
    order_res = OrderResults.objects.filter(order_id=order_id,validation_status=0,is_header=0,test__test_group__in = test_group)
    if order_res.count()>0:     
        return format_html("""<td class="progs"><div class="progress progress-striped">         
<div class="progress-bar progress-bar-danger" role="progressbar" style="width: 0%;">
         &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;        
</div>
</div>
</td>
""")
    
    order_res = OrderResults.objects.filter(order_id=order_id,validation_status=1,is_header=0,test__test_group__in = test_group)
    if order_res.count()>0:
        return format_html("""<td class="progs"><div class="progress progress-striped">         
<div class="progress-bar progress-bar-danger" role="progressbar" style="width: 25%;">
         &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;        
</div>
</div>
</td>
""")
                
    order_res = OrderResults.objects.filter(order_id=order_id,validation_status=2,is_header=0,test__test_group__in = test_group)
    if order_res.count()>0:
        return format_html("""<td class="progs"><div class="progress progress-striped">         
<div class="progress-bar progress-bar-warning" role="progressbar" style="width: 50%;">
         &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;        
</div>
</div>
</td>
""")
      
    order_res = OrderResults.objects.filter(order_id=order_id,validation_status=3,is_header=0,test__test_group__in = test_group)
    if order_res.count()>0:
        return format_html("""<td class="progs"><div class="progress progress-striped">         
<div class="progress-bar progress-bar-success" role="progressbar" style="width: 75%;">
         &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;        
</div>
</div>
</td>
""")
    
    order_res = OrderResults.objects.filter(order_id=order_id,validation_status=4,is_header=0,test__test_group__in = test_group)
    if order_res.count()>0:
        return format_html("""<td class="progs"><div class="progress progress-striped">         
<div class="progress-bar progress-bar-info" role="progressbar" style="width: 100%;">
         &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;        
</div>
</div>
</td>
""")    

    return format_html("""<td class="progs"><div class="progress progress-striped">         
<div class="progress-bar progress-bar-info" role="progressbar" style="width: 100%;">
         &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;        
</div>
</div>
</td>
""")