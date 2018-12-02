# bbconnection



Update:
20181118 - update tambahkan previous result 1,2,3 pada result entri di area kerja
20181115 - jika di pencarian diinput nomor sampel, akan dapat extract nomor ordernya
20181113 - fix status workarea untuk hasil telah diprint
20181101 - Workarea bisa disetting di administration
20180910 - Unik untuk price dan priority
20181121 - Checkbox diperbesar di menu isi hasil dan order entry 3
20181202 - Dokumen API untuk order dan hasil
20181202 - Receipt dan bill konversi ke jasperreport

Pending:
tambahkan pencarian nomor RM untuk saat create user
1. isi hasil lebarnya dikecilkan jadi 1/2 dari yang sebelumnya 2
2. History semua hasil per test dimunculkan kalau butuh 2
5. Tambahkan menu receive sampel 5
6. Menu terpisah antara isi hasil dan QV 5
7. Formula perhitungan dibuatkan 5
8. Centang master untuk dikeluarkan saat print, ada juga centang menu QV untuk bisa user pilih keluar di report, atau tidak tanpa merubah master 5
9. Privilage per user, bisa edit hasil, bisa view, dan bisa print 5


API:
Authentikasi: Token
caranya:
1. login untuk mendapatkan token url: http://127.0.0.1:8000/api/login/ methode POST
dengan header:
Accept: application/json
content-type: application/json
conetent:
{
"username":"admin",
"password":"*******"
}

response:
{"token":"99c630d825eb911082c6620a0b2406af07e81045"}


untuk ambil Order ke:
Methode GET
http://127.0.0.1:8000/api/orders/
Header=
Accept: application/json
Authorization: Token 99c630d825eb911082c6620a0b2406af07e81045
output:
{"count":4145,"next":"http://127.0.0.1:8000/api/orders/?page=2","previous":null,"results":[{"id":4335,"order_date":"2018-12-02","number":"","note":"","conclusion":"","dateofcreation":"2018-12-02T19:44:10.447000","lastmodification":"2018-12-02T19:44:10.447000","service":null,"origin":null,"doctor":null,"diagnosis":null,"priority":null,"insurance":null,"patient":null,"lastmodifiedby":null},{"id":4338,"order_date":"2018-12-02","number":"123456789","note":"","conclusion":"","dateofcreation":"2018-12-02T22:57:28.038000","lastmodification":"2018-12-02T22:57:28.038000","service":null,"origin":null,"doctor":null,"diagnosis":null,"priority":null,"insurance":null,"patient":null,"lastmodifiedby":null},{"id":4339,"order_date":"2018-12-02","number":"1234567890","note":"","conclusion":"","dateofcreation":"2018-12-02T22:57:47.821000","lastmodification":"2018-12-02T22:57:47.821000","service":null,"origin":null,"doctor":null,"diagnosis":null,"priority":null,"insurance":null,"patient":null,"lastmodifiedby":null},{"id":98,"order_date":"2018-08-16","number":"1808160003","note":null,"conclusion":null,"dateofcreation":"2018-08-15T18:19:00.592000","lastmodification":"2018-08-15T18:23:39.776000","service":1,"origin":1,"doctor":77,"diagnosis":null,"priority":1,"insurance":7,"patient":null,"lastmodifiedby":null},{"id":99,"order_date":"2018-08-16","number":"1808160004","note":null,"conclusion":null,"dateofcreation":"2018-08-16T00:05:00.070000","lastmodification":"2018-08-16T00:35:45.960000","service":1,"origin":1,"doctor":null,"diagnosis":null,"priority":1,"insurance":null,"patient":84,"lastmodifiedby":null},{"id":101,"order_date":"2018-08-16","number":"1808160006","note":null,"conclusion":null,"dateofcreation":"2018-08-16T02:21:51.096000","lastmodification":"2018-08-16T02:24:18.422000","service":2,"origin":59,"doctor":40,"diagnosis":null,"priority":1,"insurance":7,"patient":85,"lastmodifiedby":null},{"id":102,"order_date":"2018-08-16","number":"1808160007","note":null,"conclusion":null,"dateofcreation":"2018-08-16T02:33:12.785000","lastmodification":"2018-08-16T02:36:13.432000","service":1,"origin":53,"doctor":31,"diagnosis":null,"priority":1,"insurance":17,"patient":86,"lastmodifiedby":null},{"id":103,"order_date":"2018-08-16","number":"1808160008","note":null,"conclusion":null,"dateofcreation":"2018-08-16T02:41:43.646000","lastmodification":"2018-08-16T02:44:57.321000","service":2,"origin":58,"doctor":433,"diagnosis":null,"priority":1,"insurance":7,"patient":87,"lastmodifiedby":null},{"id":104,"order_date":"2018-08-16","number":"1808160009","note":null,"conclusion":null,"dateofcreation":"2018-08-16T02:55:24.452000","lastmodification":"2018-08-16T02:57:18.005000","service":2,"origin":79,"doctor":298,"diagnosis":null,"priority":1,"insurance":7,"patient":88,"lastmodifiedby":null},{"id":105,"order_date":"2018-08-16","number":"1808160010","note":null,"conclusion":null,"dateofcreation":"2018-08-16T03:13:03.696000","lastmodification":"2018-08-16T03:16:41.885000","service":2,"origin":58,"doctor":436,"diagnosis":null,"priority":1,"insurance":10,"patient":89,"lastmodifiedby":null}]}


untuk post:
http://127.0.0.1:8000/api/orders/
Header=
Accept: application/json
Authorization: Token 99c630d825eb911082c6620a0b2406af07e81045
methode POST:
{
    "number": "",
    "note": "",
    "conclusion": "",
    "service": null,
    "origin": null,
    "doctor": null,
    "diagnosis": null,
    "priority": null,
    "insurance": null,
    "patient": null,
    "lastmodifiedby": null
}
ouput = 201 : Created sukses






