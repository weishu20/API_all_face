
baidu 获取access_token
curl -i -k 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=oz5ugFF0Diyr6TK5UnMvqj8H&client_secret=tvhcjSBbEm2WRudmkS55GtP850dfm7Xt'

{"access_token":"24.d3c76b3b992fc7e5d35c51e761828092.2592000.1518171145.282335-10628712","session_key":"9mzdX+niCymHR\/0XNBWMG2RnFUDEhCSrHkz6JiSn0Wjmt1K90mUOnWXVdaLbJ\/TaSRoRAXtcMuoOtVKbiIa6LaRa9QQPgw==","scope":"public vis-faceverify_faceverify vis-faceattribute_faceattribute vis-faceverify_faceverify_v2 vis-faceverify_faceverify_match_v2 brain_all_scope vis-faceverify_vis-faceverify-detect wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower bnstest_fasf lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission","refresh_token":"25.2bcf3377377ca7e8675add7d91ba2d5b.315360000.1830939145.282335-10628712","session_secret":"122270c30dc9152b592fb82d62df1dff","expires_in":2592000}
curl -d "app_key=fef6cc2e6a084835b64670b8e2da2888" -d "app_id=6242aab536fe479ba79daac5c5c4aa4f" -d "url=https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87%20%E4%BA%BA%E7%89%A9&step_word=&hs=2&pn=18&spn=0&di=190087203680&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2949052360%2C3852946968&os=1881470458%2C3672958665&simid=4170734326%2C723035260&adpicid=0&lpn=0&ln=1959&fr=&fmq=1515566251873_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.taopic.com%2Fuploads%2Fallimg%2F110116%2F129-11011611103032.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bpw5rtv_z%26e3Bv54AzdH3Fp7h7AzdH3Fda88a8AzdH3Fd8c0a_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0" http://api.eyekey.com/face/Check/checking

HTTP/1.1 200 OK
Server: Tengine
Date: Wed, 10 Jan 2018 07:08:45 GMT
Content-Type: text/plain;charset=UTF-8
Content-Length: 94
Connection: keep-alive
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET,POST,OPTIONS

{"img_height":0,"img_width":0,"message":"未知或不支持的图片格式","res_code":"1084"}




curl -i -d "app_key=fef6cc2e6a084864670b8e2da2888" -d "app_id=6242aab536fe479ba79daac5c5c4aa4f" -d "img=@/home/shushi/Pic/IMDB-WIKI/wiki_crop/17/10000217_1981-05-05_2009.jpg" http://api.eyekey.com/face/Check/checking
HTTP/1.1 200 OK
Server: Tengine
Date: Wed, 10 Jan 2018 07:08:45 GMT
Content-Type: text/plain;charset=UTF-8
Content-Length: 94
Connection: keep-alive
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET,POST,OPTIONS

{"img_height":0,"img_width":0,"message":"未知或不支持的图片格式","res_code":"1084"}




curl -d "app_key=fef6cc2e6a084835b64670b8e2da2888" -d "app_id=6242aab536fe479ba79daac5c5c4aa4f" -d "File=@/home/shushi/Pic/IMDB-WIKI/wiki_crop/17/10000217_1981-05-05_2009.jpg" http://api.eyekey.com/face/Check/checking

HTTP/1.1 404 Not Found
Server: Tengine
Date: Wed, 10 Jan 2018 07:06:48 GMT
Content-Type: application/json;charset=utf-8
Content-Length: 0
Connection: keep-alive

curl -i -d "app_key=fef6cc2e6a084835b64670b8e2da2888" -d "app_id=6242aab536fe479ba79daac5c5c4aa4f" -d "face_id1=11a9d5dd4e4b43e7b8a88c87af94a210" -d "face_id2=78dfeb118ca941059a34894daddd885c" http://api.eyekey.com/face/Match/match_compare

HTTP/1.1 405 Method Not Allowed
Server: Tengine
Date: Wed, 10 Jan 2018 08:14:23 GMT
Content-Type: text/html;charset=utf-8
Content-Length: 1090
Connection: keep-alive
Allow: GET
Content-Language: en

<!DOCTYPE html><html><head><title>Apache Tomcat/8.0.23 - Error report</title><style type="text/css">H1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} H2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} H3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} BODY {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} B {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} P {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;}A {color : black;}A.name {color : black;}.line {height: 1px; background-color: #525D76; border: none;}</style> </head><body><h1>HTTP Status 405 - Request method 'POST' not supported</h1><div class="line"></div><p><b>type</b> Status report</p><p><b>message</b> <u>Request method 'POST' not supported</u></p><p><b>description</b> <u>The specified HTTP method is not allowed for the requested resource.</u></p><hr class="line"><h3>Apache Tomcat/8.0.23</h3></body></html>



curl -i http://api.eyekey.com/face/Match/match_compare?app_key=fef6cc2e6a084835b64670b8e2da2888&app_id=6242aab536fe479ba79daac5c5c4aa4f&face_id1=11a9d5dd4e4b43e7b8a88c87af94a210&face_id2=78dfeb118ca941059a34894daddd885c

 HTTP/1.1 400 Bad Request
Server: Tengine
Date: Wed, 10 Jan 2018 08:22:42 GMT
Content-Type: application/json;charset=utf-8
Content-Length: 67
Connection: keep-alive

{"message":"缺少请求参数, app_id不存在","res_code":"1004"}



curl -v -X POST "https://api.cognitive.azure.cn/vision/v1.0/analyze" -H "Content-Type:application/json" -H "Ocp-Apim-Subscription-Key:0b51d2c1e79646c497a238e9b080f050" --data-ascii "url:https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87%20%E4%BA%BA%E7%89%A9&step_word=&hs=2&pn=18&spn=0&di=190087203680&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2949052360%2C3852946968&os=1881470458%2C3672958665&simid=4170734326%2C723035260&adpicid=0&lpn=0&ln=1959&fr=&fmq=1515566251873_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.taopic.com%2Fuploads%2Fallimg%2F110116%2F129-11011611103032.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bpw5rtv_z%26e3Bv54AzdH3Fp7h7AzdH3Fda88a8AzdH3Fd8c0a_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0" 

curl -i -H "Content-Type:application/json" -H "Ocp-Apim-Subscription-Key:90319f7b17234a95be61c0d439d15007" -X POST -d "image=@/home/shushi/Pic/IMDB-WIKI/wiki_crop/17/10000217_1981-05-05_2009.jpg" https://api.cognitive.azure.cn/vision/v1.0/describe









