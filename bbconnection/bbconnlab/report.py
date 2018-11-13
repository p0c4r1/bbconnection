import base64
import requests
import token
from django.conf import settings

class JasperServer(object):
    

    def get_token(self):
        username = settings.JASPER_USER
        password = settings.JASPER_PASS
        token = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        return token
    
    def get_report(self,order_id,group_id):
        if not group_id:
            group_id = ''
        data = """
        <reportExecutionRequest>
            <reportUnitUri>/reports/bbconn/ciremaiReport</reportUnitUri>
            <async>false</async>
            <freshData>true</freshData>
            <saveDataSnapshot>false</saveDataSnapshot>
            <outputFormat>pdf</outputFormat>
            <interactive>true</interactive>
            <ignorePagination>false</ignorePagination>
            <parameters>
                <reportParameter name="ORDER_ID">
                    <value>{order_id}</value>
                </reportParameter>
                <reportParameter name="GROUP_ID">
                    <value>{group_id}</value>
                </reportParameter>
            </parameters>
        </reportExecutionRequest>
        """.format(order_id=order_id,group_id=group_id)
        
        #print data
        token = self.get_token()
        response = requests.post(url=settings.JASPER_REST+"reportExecutions",
                         headers={
                             "Authorization": "Basic " + token,
                             "Accept": "application/json",
                             "Content-Type": "application/xml",
                         },
                         data=data)
        data = response.json()
        #print data
        try:
            request_id = data.get("requestId")
            export_id = data.get("exports")[0].get("id")
            status = data.get("status")
        except Exception as e:
            return False,data

        
        if status == 'ready': 
            report_url = settings.JASPER_REST+"reportExecutions/{request_id}/exports/{export_id}/outputResource".format(
                request_id=request_id, export_id=export_id)
            
            report_resp = requests.get(url=report_url,headers=response.headers, cookies=response.cookies)
            return True,report_resp.content
        else:
            return False,data
        
        