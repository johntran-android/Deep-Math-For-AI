# Week 8: Html Css Js

📊 **Progress:** `116` Notes | `199` Screenshots

---
<a id="node-1192"></a>

<p align="center"><kbd><img src="assets/eccbfec89cd35a6d6ca5d337f895f03a9ce94cd0.png" width="100%"></kbd></p>

> [!NOTE]
> Mở đầu bằng 1 trò chơi để diễn tả khái niệm router =
> bộ định tuyến Hiểu nôm na là cái tool giúp xác định
> hướng đi, tuyến đường của 1 thông tin từ A (Phyllis)
> đến B (Brian)

<br>

<a id="node-1193"></a>

<p align="center"><kbd><img src="assets/bbf807b5c2a4c18f2a108c10b639158e8c5b9f23.png" width="100%"></kbd></p>

<br>

<a id="node-1194"></a>

<p align="center"><kbd><img src="assets/c26655baefdb2005e166d1c6d25a5587f48b535e.png" width="100%"></kbd></p>

<br>

<a id="node-1195"></a>

<p align="center"><kbd><img src="assets/e10733affbe8066b43fa9bd0f0801051dca25a3b.png" width="100%"></kbd></p>

<br>

<a id="node-1196"></a>

<p align="center"><kbd><img src="assets/dae182f810d07be21726a14b12deba004b935a57.png" width="100%"></kbd></p>

> [!NOTE]
> IP **Internet Protocol** đại khái là một **quy tắc giao tiếp giữa
> máy tính với nhau**. Giống như việc bắt tay là quy tắc
> giao tiếp giữa người và người vậy.

<br>

<a id="node-1197"></a>

<p align="center"><kbd><img src="assets/84b5ec9205c160305dac073ef2b96fc68ef57839.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái địa chỉ của một
> máy tính là 4 con số

<br>

<a id="node-1198"></a>

<p align="center"><kbd><img src="assets/6ed612b09227ab7150c051b5c9309fba39d39b4e.png" width="100%"></kbd></p>

> [!NOTE]
> Mỗi số mang giá trị từ 0-255 vậy thì mỗi số dùng mấy bit?
>
> A: 8 
>
> D: Correct IP address cơ bản là 32 bit
>
> D vậy có bao nhiêu computer address với 32 bit?
>
> A: Tương tự như int (unsign) 4 byte = 32 bit, range của nó
> là **4 tỉ mấy.**

<br>

<a id="node-1199"></a>

<p align="center"><kbd><img src="assets/8511f6064531723d9210d3e3065cba3a324895cd.png" width="100%"></kbd></p>

> [!NOTE]
> Thì với version 6, người ta cho **128 bit** để cho phép nhiều
> IP address hơn

<br>

<a id="node-1200"></a>

<p align="center"><kbd><img src="assets/fed86c88f5f38e18261e8f87fac8c5891e6a778c.png" width="100%"></kbd></p>

> [!NOTE]
> Giả sử Julia ở address 5.6.7.8 muốn gửi
> envelope này đén Brian ở address 1.2.3.4

<br>

<a id="node-1201"></a>

<p align="center"><kbd><img src="assets/08ba51b799bbdca27fd392170d8d47621ab0c560.png" width="100%"></kbd></p>

> [!NOTE]
> **TCP Transmission Control Protocol** có mục đích
> thứ nhất là **phân biệt các loại service khác nhau**
> (email hay video...)

<br>

<a id="node-1202"></a>

<p align="center"><kbd><img src="assets/3283e19785d14d15eb7c4879638eaeab3482910b.png" width="100%"></kbd></p>

> [!NOTE]
> 80 là HTTP, 443 là HTTPS (S
> stand for secured/encrypted/safety)

<br>

<a id="node-1203"></a>

<p align="center"><kbd><img src="assets/dadb50ca150256fe697de1dbc389fdf315c9daf5.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là giả sử Brian có webpage và Phyllis cần request
> home page thì bên cạnh **IP address của Brian 1.2.3.4**, sẽ có
> thêm **443** (dùng HTTPS - Secured)
>
> Ngoài ra máy tính của Phylis **luôn generate thêm Port number
> là IP của Phyllis** để Brian có thể **liên lạc ngược lại**

<br>

<a id="node-1204"></a>

<p align="center"><kbd><img src="assets/3d3b37416d5c243434ef10a79f47816cde853c44.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói giả sử Phyllis muốn **upload
> cái hình con mèo lên webpage**
>
> Thì **xé nhỏ nó ra làm 4,** rồi bỏ phần 1 vào
> envelope. Ghi thêm 1/4

<br>

<a id="node-1205"></a>

<p align="center"><kbd><img src="assets/754d1a539ae93b875d4c30104d0aa9bc21e339b6.png" width="100%"></kbd></p>

> [!NOTE]
> Kế ổng nói giả sử vì**lí do gì đó cái 2/4 (envelop chứa cái
> phần số 2 của ảnh mèo) bị lạc** thì Khi máy tính của Brian
> nhận envelop có 1/4, 3/4, 4/4 thì sao?
>
> A: Nó sẽ r**equest phần 2/4**
>
> D: Correct. Và khi Brian **đã nhận đủ 4 phần thì nó báo lại là
> Ok, đủ rồi**

<br>

<a id="node-1206"></a>

<p align="center"><kbd><img src="assets/df75cfd7a6f4f489109ca5aae33718972fc57705.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là sẽ **rất khó nhớ (cho con người) khi phải
> nhớ ip address**. **Không phù hợp cho marketing** một
> webpage....
>
> Do đó **DNS** = **Domain Name System** để map /**convert
> IP address sang human friendly string** như harvard.
> edu hay **google.com** và ngược lại

<br>

<a id="node-1207"></a>

<p align="center"><kbd><img src="assets/ab5a017ed7d480b5d2082b0e17d2d32822ad76ba.png" width="100%"></kbd></p>

> [!NOTE]
> Và cơ bản nó là một table, một **hash table, hoặc
> sql, linked-list**... map giữa **Domain name và IP
> address**

<br>

<a id="node-1208"></a>

<p align="center"><kbd><img src="assets/a269851cf363872c853fa5bef706b57747ec496f.png" width="100%"></kbd></p>

> [!NOTE]
> Và không phải chỉ là google. com mà
> thật ra là đầy đủ **www.google.com**

<br>

<a id="node-1209"></a>

<p align="center"><kbd><img src="assets/ded5211faa50a1f1cb5a0b763fc2b7e9a91a1eea.png" width="100%"></kbd></p>

> [!NOTE]
> **HTTP** = Hypertext Transfer Protocol
>
> Đại khái **TCP/IP stuff, DNS stuff là tầng dưới, nền tảng**, là
> **hệ thống đường ống giúp truyền dữ liệu**
>
> Thì **HTTP là tầng trên, tầng software application level**
> giúp **build ứng dụng dựa trên các pipeline system đó**

<br>

<a id="node-1210"></a>

<p align="center"><kbd><img src="assets/86c3f889fd77374909d9f0ad82ebbecc8e3acb04.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ngày nay **tuy ít thấy hết toàn bộ url**nhưng **nó vẫn ở đó vì lí do UX thôi**, ví dụ google.
> com thật ra đầy đủ là **https://www.google.com**
>
> Thì đại khái khi ta **ghi example.com thì thật ra nó
> là  example.com/** với **slash '/' là default, là orginal
> url**

<br>

<a id="node-1211"></a>

<p align="center"><kbd><img src="assets/8318f23c440079e39b3511866d7d25862afcfbfa.png" width="100%"></kbd></p>

> [!NOTE]
> Bên cạnh đó nó
> có thể có path

<br>

<a id="node-1212"></a>

<p align="center"><kbd><img src="assets/fa0db93a054d5b54e47aaa641eccb6ee57f0c145.png" width="100%"></kbd></p>

<br>

<a id="node-1213"></a>

<p align="center"><kbd><img src="assets/ccca211b33b1a55c7586960ee97335f35f28bca2.png" width="100%"></kbd></p>

<br>

<a id="node-1214"></a>

<p align="center"><kbd><img src="assets/9cc168279301505c826b075bf44ba965acd60b6a.png" width="100%"></kbd></p>

<br>

<a id="node-1215"></a>

<p align="center"><kbd><img src="assets/284b6f80c2cc2e17d9e2a2f2c08cd4cefdc6917a.png" width="100%"></kbd></p>

> [!NOTE]
> Example.com gọi là
> **domain name**

<br>

<a id="node-1216"></a>

<p align="center"><kbd><img src="assets/c7659956bece0ed7a21fd3f09bd2aea34fe46826.png" width="100%"></kbd></p>

> [!NOTE]
> **.com** là **Top Level Domain** : TLD
> Và ngày nay thì **.com không nhất thiết phải là business**, 
> **.net không nhất thiết phải là network**, ngoại trừ một số
> như **.gov, .edu thì còn tương đối strictly regulated** thôi

<br>

<a id="node-1217"></a>

<p align="center"><kbd><img src="assets/2cdd19978ddbf4ec1ca55f0fca93a5a7cce3cedc.png" width="100%"></kbd></p>

> [!NOTE]
> Host name www cơ bản **chỉ là convention.**

<br>

<a id="node-1218"></a>

<p align="center"><kbd><img src="assets/de7977dc7dabebc2342040a0a11143f5892fbc12.png" width="100%"></kbd></p>

> [!NOTE]
> cuối cùng **http/https là protocol**. Có những cái
> khác nữa những chỉ focus hai cái này

<br>

<a id="node-1219"></a>

<p align="center"><kbd><img src="assets/f7806b73447669d20dabef73e02df0d8f227239c.png" width="100%"></kbd></p>

> [!NOTE]
> Q: **Local host** là gì
>
> D: Đại khái là **convention của human cho IP address** để
> **luôn chỉ máy tính của chính mình: 127.0.0.1**
>
> Có vai trò **hữu ích khi development** trên máy tính của mình

<br>

<a id="node-1220"></a>

<p align="center"><kbd><img src="assets/4502f6b103a231990cb085018219fcab87cda68b.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là trong cái envelope mà Phyllis gửi Brian cơ bản
> là có 1 trong 2 keyword này. **GET và POST**. Nôm na GET
> là get data. POST là post data

<br>

<a id="node-1221"></a>

<p align="center"><kbd><img src="assets/35960d727bbaf0564c90fc134df5c55347376984.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là giả dụ Phyllis "request" thay vì Brian'
> s webpage mà là example.com thì her message
> sẽ có dạng dạng như này:
>
> **GET / HTTP/1.1
> Host: www.example.com**
>
> 1.1 là version

<br>

<a id="node-1222"></a>

<p align="center"><kbd><img src="assets/2174efbfb1acf09709a44a6361333c359ebacee0.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là incognito sẽ hữu ích vì nó giống như
> cho một**fresh start**, không có các remnant các
> website mình đã visit

<br>

<a id="node-1223"></a>

<p align="center"><kbd><img src="assets/b60845014967fed7156494dcac0abe83b42bdb03.png" width="100%"></kbd></p>

<br>

<a id="node-1224"></a>

<p align="center"><kbd><img src="assets/a42f8f62c39762bf1555ea8769f1a4528a5aeaf7.png" width="100%"></kbd></p>

<br>

<a id="node-1225"></a>

<p align="center"><kbd><img src="assets/b6c64f2360c950c4ed59a9266e6b98b5387e40f0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b6c64f2360c950c4ed59a9266e6b98b5387e40f0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0836532f0ac4702a11cc730778b94e63f3f1f09b.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng thử dùng tính năng **inspector** của web
> browser để cho ta thấy **các thông tin trong request
> header.**
> Với method **GET**,
>
> với domain name **www.harvard.edu**
>
> với path là origin | default **/**,
>
> với scheme hay protocol như mới  biết - **https**

<br>

<a id="node-1226"></a>

<p align="center"><kbd><img src="assets/83db24084f487a150deb98c793035a865c169b71.png" width="100%"></kbd></p>

> [!NOTE]
> Và cái response sẽ có dạng như này
>
> Với 1.1 như hồi nãy, là version
>
> 200 là **response code** = OK
>
> Loại trả về là **text/html**có nghĩa là nó**trả về một webpage**

<br>

<a id="node-1227"></a>

<p align="center"><kbd><img src="assets/7b36bd153030ba69cd4bd7fd1a28825beb403df1.png" width="100%"></kbd></p>

> [!NOTE]
> Ngoài ra nó **còn trả về
> cả đống detail**

<br>

<a id="node-1228"></a>

<p align="center"><kbd><img src="assets/00fefd804aec46ae847141454cecc7f37f3bb55c.png" width="100%"></kbd></p>

> [!NOTE]
> **curl** = connect url: Đại khái là công cụ **cho phép giả bộ là
> web browser**

<br>

<a id="node-1229"></a>

<p align="center"><kbd><img src="assets/dd70f18f4e8ddc2d01d17f99f17cfa1d80cafba9.png" width="100%"></kbd></p>

<br>

<a id="node-1230"></a>

<p align="center"><kbd><img src="assets/e5f194be64277932c7f1933b7c299ad81f734922.png" width="100%"></kbd></p>

> [!NOTE]
> Đây là toàn bộ thông tin nó trả về.
>
> Ta có thể thấy **HTTT/2 (version 2)**
>
> **200** response code = OK
>
> rồi có c**ontent_type text/html charset UTF-8**
>
> (nhớ lại**UTF-8 cũng tương tự như ASCII**, ý là **bộ tiêu
> chuẩn nào thôi)**

<br>

<a id="node-1231"></a>

<p align="center"><kbd><img src="assets/248e1199a5f939ab166bde2e789617f144a77f36.png" width="100%"></kbd></p>

> [!NOTE]
> giờ thử **http (ko s)**

<br>

<a id="node-1232"></a>

<p align="center"><kbd><img src="assets/ff28898a996b7044727a2f5c82b1ebb7af0d01e1.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nó trả về **301** = **Moved Permanently** ý
> là Harvard **đã chuyển về đây https://...**(https chứ không
> phải http)
>
> Và với các Chrome hay Firefox **người ta lập trình sẵn
>  là khi gặp response 301 nó sẽ tự động chuyển tới 
> https://www.harvard.edu/**

<br>

<a id="node-1233"></a>

<p align="center"><kbd><img src="assets/be994af41866fef61c1922f573d2e3997551730d.png" width="100%"></kbd></p>

<br>

<a id="node-1234"></a>

<p align="center"><kbd><img src="assets/7fefa77050cfc5241287fd315b73118101daa6db.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự khi request url này.
>
> Đây là lí do tại sao khi mình **gõ google.com** trong 
> web browser thì nó**tự động vào www.google.com**

<br>

<a id="node-1235"></a>

<p align="center"><kbd><img src="assets/3203d7ada9d86bbb68fd09a85dff29c153ab1624.png" width="100%"></kbd></p>

> [!NOTE]
> 404 Not Found

<br>

<a id="node-1236"></a>

<p align="center"><kbd><img src="assets/f253dbcfadbc5936bdc903ffb6c76241574332d0.png" width="100%"></kbd></p>

> [!NOTE]
> Một số response code khác:
> **500** tương tự như **Segmentation Fault**của C, là **lỗi của developer**

<br>

<a id="node-1237"></a>

<p align="center"><kbd><img src="assets/991fe7804f0f3bca2c28159b21fd37e853e29256.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói về cái này
> **search?q=cat....**
>
> Ý là khi ta **search google bằng google form** thì thật ra
> **chính là request url như vầy**

<br>

<a id="node-1238"></a>

<p align="center"><kbd><img src="assets/49ea19177eca54a2d936c1c17eb7599f4dc5db51.png" width="100%"></kbd></p>

<br>

<a id="node-1239"></a>

<p align="center"><kbd><img src="assets/5f55345908038f238029527ebb3c09a036db4926.png" width="100%"></kbd></p>

<br>

<a id="node-1240"></a>

<p align="center"><kbd><img src="assets/0169d64a611b8e574db7a1b87e7e4f9a4083806c.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói có cái joke gì đó ở đây khi
> ta **dùng url safetyschool.org** thì nó
> chuyển tới**Yale webpage**

<br>

<a id="node-1241"></a>

<p align="center"><kbd><img src="assets/94e9b0e1e2648abd2a9570fe6dd03cd3ea4ec123.png" width="100%"></kbd></p>

<br>

<a id="node-1242"></a>

<p align="center"><kbd><img src="assets/63ffe253cc4fb80999b88f57782403e9b51586eb.png" width="100%"></kbd></p>

<br>

<a id="node-1243"></a>

<p align="center"><kbd><img src="assets/856474dd7ccda4b8b1dac4fd100bcedbe76164a4.png" width="100%"></kbd></p>

<br>

<a id="node-1244"></a>

<p align="center"><kbd><img src="assets/659c2a9e0475e98574f8fa38f4787ece541cb7fb.png" width="100%"></kbd></p>

<br>

<a id="node-1245"></a>

<p align="center"><kbd><img src="assets/0c0ef8e126a4afdf1e49a45994a1be0194feb34c.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là cần phải có cái **web server** để **serve** (cung cấp) 
> cái này (html file này) cho người ta khi cần (**request**) có 
> thể xem nó.
>
> Và ổng nói **với server ta hay liên tưởng tới các hệ thống 
> máy server** nhưng thật ra nó **chính là cái program để
> serve request bằng cách trả về response chấm hết.**
>
> Và cs50 nó có sẵn cái lệnh **http-server** này để tạo một 
> cái web server.

<br>

<a id="node-1246"></a>

<p align="center"><kbd><img src="assets/dfd7a47a3a595beecab09436eac6b42d064e3046.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói là nó sẽ **tạo ra một cái url**. (Mỗi người khi làm
> thử sẽ cho url khác nhau)
>
> Nhưng đại khái là nó sẽ**cho phép bạn có thể access  cái
> file hello.html này thông qua web browser**
>
> Và nếu **làm thêm một số điều chỉnh có thể khiến nó visible
> với thế giới.**
>
> Nhưng khi mà ta**log out, hay shutdown máy tính** thì
> website sẽ **go down.**

<br>

<a id="node-1247"></a>

<p align="center"><kbd><img src="assets/ad312fb66b8aecbc32f881f4e21203d95a35530b.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng **open cái url
> trên trên web browser**

<br>

<a id="node-1248"></a>

<p align="center"><kbd><img src="assets/a03c7dbc634525a6af3827cf46dbae8735f513f1.png" width="100%"></kbd></p>

> [!NOTE]
> Mở cái link mở ra cái
> page hello.html ra

<br>

<a id="node-1249"></a>

<p align="center"><kbd><img src="assets/227b15357820c92c641e231f45b7ffbe6b4d0d81.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là **nó trỏ tới cái file
> hello.html**

<br>

<a id="node-1250"></a>

<p align="center"><kbd><img src="assets/be5f612d0786db8462356fb867fe9c03e3b4fe99.png" width="100%"></kbd></p>

> [!NOTE]
> Trên cùng là **<!DOCTYPE html>** đại khái là **declare bạn
> đang dùng latest version của HTML**

<br>

<a id="node-1251"></a>

<p align="center"><kbd><img src="assets/134fd163ba5ab01d99c031db6f636467e587fe75.png" width="100%"></kbd></p>

> [!NOTE]
> **<html> <head>** ... và **</html> </head>** gọi là **start
> và end tag** **lang='en'**giống như **attribute** để
> modify behavior, ở đây đại khái là c**ho web browser,
> search engine biết ở trong đây  sẽ là English**

<br>

<a id="node-1252"></a>

<p align="center"><kbd><img src="assets/2c37282a9e7b1dd8cfecf0dfb60c2fe5da1f7ec7.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là quan hệ giữa **html** tag - **head**
> tag - **title** tag giống như **ông nội - cha - cháu**

<br>

<a id="node-1253"></a>

<p align="center"><kbd><img src="assets/482556b6b36d92dbad4ab0621db681b875ba7521.png" width="100%"></kbd></p>

<br>

<a id="node-1254"></a>

<p align="center"><kbd><img src="assets/a7eb01c460a8423de936af937f108abe05dd1c76.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta viế**t html code như vầy**, nhưng trong 
> máy tính nó sẽ tạo cái tree như vầy gọi là **DOM**
>
> Và khi tí nữa ta sẽ dùng**java script để move, add 
> các nhánh này dynamically**
> Cũng như**Gmail khi ta có một email mới nó không
> cần phải reload mà nó chỉ cần add thêm 1 node**

<br>

<a id="node-1255"></a>

<p align="center"><kbd><img src="assets/e7869fafdb53cc0325dbdcec9508fb4120ee0591.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng tạo mới một file khác. Và nói là **thật ra indentation
> không quan trọng trong html.**
>
> Việc indentation **chỉ có tác dụng giúp human dễ nhìn
> và tránh sai sót thôi**

<br>

<a id="node-1256"></a>

<p align="center"><kbd><img src="assets/edf0d753bd951b202b82c7c5f5e358273c50c4c8.png" width="100%"></kbd></p>

> [!NOTE]
> Và với đó,**index page** **có thêm 1 url
> paragraphs.html mới tạo**

<br>

<a id="node-1257"></a>

<p align="center"><kbd><img src="assets/0d1860e15e5b2080c2af9c5d90276ff98f0fc397.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng click vào có vẻ**mọi thứ đều lộn xộn** chứ không
> phải là có 3 đoạn như expect. Why?
>
> A: **Vì 3 đoạn đều nằm trong <body>** và  **dù có chia khoảng
> cách nhưng như nãy nói nó không care vấn đề
> indentation.**
> Nên **phải bỏ mỗi đoạn vào 1 children tag thì nó mới
> separate ra được**D: Correct

<br>

<a id="node-1258"></a>

<p align="center"><kbd><img src="assets/6cec54f16202c0d93ee6387c129b769bc3d89d1e.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng dùng **<br>** này để làm cái việc xuống dòng
> **(line break)**và nói thêm là **cái này không cần close tag**,
> nó chỉ đứng mình ên

<br>

<a id="node-1259"></a>

<p align="center"><kbd><img src="assets/2e69884bb12d45789c4de967c653f8a3a220edbd.png" width="100%"></kbd></p>

> [!NOTE]
> Nhìn đã ok hơn

<br>

<a id="node-1260"></a>

<p align="center"><kbd><img src="assets/8d855f63a47155c69c0442adb415050f54ff5bd2.png" width="100%"></kbd></p>

> [!NOTE]
> Tuy nhiên dùng **<p> tag** - paragraph tag cho mỗi
> paragraph nó thuận tự nhiên hơn vì p được design
> cho mục đích đó

<br>

<a id="node-1261"></a>

<p align="center"><kbd><img src="assets/baaea4232424a6b7cde35c0e3efb20a707bb0129.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là nó **vẫn có hiệu quả như vậy** nhưng
> **semantically better**
>
> Và có những các tag khác, tự tìm hiểu

<br>

<a id="node-1262"></a>

<p align="center"><kbd><img src="assets/632065fbba617654690d181b9ea9553f36294187.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/632065fbba617654690d181b9ea9553f36294187.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0386273509ccca7fd804ac4928f3b27723ae3851.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ h1, h2...h6 giúp tạo các heading - tiêu đề

<br>

<a id="node-1263"></a>

<p align="center"><kbd><img src="assets/a8cb5a880a4e58772a6e3bafc34dd2322b658694.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a8cb5a880a4e58772a6e3bafc34dd2322b658694.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/65041af6211cefe634d9404a0ba106963d2f2047.png" width="100%"></kbd></p>

> [!NOTE]
> **Muốn dạng list** thì dùng **<ul>**
> (**unordered list**) hoặc **<ol>** (ordered list) và **<li>** (list)

<br>

<a id="node-1264"></a>

<p align="center"><kbd><img src="assets/5e8b8c70b99329d70afc5dd3a18aac4586c640f9.png" width="100%"></kbd></p>

> [!NOTE]
> Hoặc có thể dùng tag <table>

<br>

<a id="node-1265"></a>

<p align="center"><kbd><img src="assets/b6d9126794f6a821e646f343c8cac25fc006bf92.png" width="100%"></kbd></p>

<br>

<a id="node-1266"></a>

<p align="center"><kbd><img src="assets/e633caba22e5f73d773ac771580f16036f5d834a.png" width="100%"></kbd></p>

> [!NOTE]
> Đến**<img>** ổng nói**có thể để alt** để **có thêm thông tin
> cho Google bot khi quét cái hình**nó biết nó là thông tin gì
> dù rằng ngay nay AI đã có thể giúp việc này rất tốt

<br>

<a id="node-1267"></a>

<p align="center"><kbd><img src="assets/c62c28ddc6e843d1bb194a20d12eef89b411b356.png" width="100%"></kbd></p>

<br>

<a id="node-1268"></a>

<p align="center"><kbd><img src="assets/670a3a2a57dfcc5a407f6e6df6a987b47667f9c4.png" width="100%"></kbd></p>

<br>

<a id="node-1269"></a>

<p align="center"><kbd><img src="assets/04ed647388987f3b22bc295ab5abc4ed2288bba4.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi giới thiệu qua **video tag.**
>
> vài **attribute**, **có cái cần value có cái không**,

<br>

<a id="node-1270"></a>

<p align="center"><kbd><img src="assets/54d23b8a8b7bcd826512c6f8130cb45c45688567.png" width="100%"></kbd></p>

<br>

<a id="node-1271"></a>

<p align="center"><kbd><img src="assets/35bdd215151e6c2e0b552797e6592a2688459daa.png" width="100%"></kbd></p>

<br>

<a id="node-1272"></a>

<p align="center"><kbd><img src="assets/898213341cfaf488a7969af47698d67bf112b663.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/898213341cfaf488a7969af47698d67bf112b663.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/47c9652bccdd107d4399c14371a938789302dd88.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái nói qua **link tag, giúp link các page với nhau**

<br>

<a id="node-1273"></a>

<p align="center"><kbd><img src="assets/f98b7b402a5993cb968403493eebc807d57b3e7c.png" width="100%"></kbd></p>

<br>

<a id="node-1274"></a>

<p align="center"><kbd><img src="assets/07587df2095488d529d7e82d8bdd64a301c92e33.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về **meta tag**, giúp **view
> page better trên mobile**

<br>

<a id="node-1275"></a>

<p align="center"><kbd><img src="assets/feb6f42cf0492b0e91835a342892ad95d13b8c6c.png" width="100%"></kbd></p>

> [!NOTE]
> Nói thêm về vài cái **meta open graph tag** để
> **define thêm thông tin cho browser** biết bạn **muốn 
> nó show default title, description...**

<br>

<a id="node-1276"></a>

<p align="center"><kbd><img src="assets/823c95ee9d403f5af56e2c503f4bc8c942d00e57.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/823c95ee9d403f5af56e2c503f4bc8c942d00e57.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3dba24051f938053b600baf33e68d16b1e9bc6aa.png" width="100%"></kbd></p>

<br>

<a id="node-1277"></a>

<p align="center"><kbd><img src="assets/e7ca54e471efb58443e2357f4ab2c1da76472119.png" width="100%"></kbd></p>

> [!NOTE]
> Dùng **form**,**input** tag
> để **tạo cái form**

<br>

<a id="node-1278"></a>

<p align="center"><kbd><img src="assets/e917a25da46c1312ea80f1d494b48b8bfcefe80c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e917a25da46c1312ea80f1d494b48b8bfcefe80c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/90dcf9cfe40800d90298c25f5cf268e8c82fb191.png" width="100%"></kbd></p>

<br>

<a id="node-1279"></a>

<p align="center"><kbd><img src="assets/ada7f323aaf47c71c0e8ac7e13975c6c70a07126.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái **đây là cách mà form nó hoạt động**, nó sẽ**tự động thêm ?** và**sau đó là key value pair vào url**

<br>

<a id="node-1280"></a>

<p align="center"><kbd><img src="assets/f7b9464114ba6c7926c5ad119a4011a50aa66301.png" width="100%"></kbd></p>

<br>

<a id="node-1281"></a>

<p align="center"><kbd><img src="assets/d382c484c50bcd825927ba4989982772f80ddffe.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d382c484c50bcd825927ba4989982772f80ddffe.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bf2cb3176ed3b97f4b334766ddead91648918e6d.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, nếu thích thì có thể đổi **Submit** thành **Google Search**
> Và **method="get"** dù **ở đây không cần vì default là get
> rồi**

<br>

<a id="node-1282"></a>

<p align="center"><kbd><img src="assets/834cf648fbb5fa3de0f52b0537e58c6c6f11503d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/834cf648fbb5fa3de0f52b0537e58c6c6f11503d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/66f3d41adb6f0d5971f2b0b97a34c9011bef3c03.png" width="100%"></kbd></p>

> [!NOTE]
> Và có thể **thêm các attribute** như **autocomplete** **= "
> off"** để nó  **không autocomplete**
>
> **autofocus** (cái này là no key-value attribute) để nó**tự focus**
> vào form
>
> và **placeholder** =**"Query"** để nó **show cái place holde**r text

<br>

<a id="node-1283"></a>

<p align="center"><kbd><img src="assets/79bff1487a167b9f502584d78e3e82abac9e9f2a.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ổng nói **cơ bản HTML là vậy**, **có thể có thêm
> các tag khác, các attribute khác**, nhưng cơ bản là vậy,
> **có thể từ từ tìm hiểu thêm các loại tag đó**

<br>

<a id="node-1284"></a>

<p align="center"><kbd><img src="assets/58ff87f26edb928e586bee6b840de3e75cd284ee.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái với công cụ inspector hồi này có thể xem
> html của webpage

<br>

<a id="node-1285"></a>

<p align="center"><kbd><img src="assets/7394644836bb93facfb757e864aa5b8d05d0ea7a.png" width="100%"></kbd></p>

> [!NOTE]
> Hoặc **một phần nào
> đó của webpage**

<br>

<a id="node-1286"></a>

<p align="center"><kbd><img src="assets/8ff129c6e340c553e0b5627175b8c3cd66de2d3c.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ví dụ ở đây có
> **button's id**

<br>

<a id="node-1287"></a>

<p align="center"><kbd><img src="assets/e95d788d6eae8f6155e05bd7fd5e9cf712dd61f2.png" width="100%"></kbd></p>

<br>

<a id="node-1288"></a>

<p align="center"><kbd><img src="assets/3d8d658845473dea2e21e67b8259f61c894da89a.png" width="100%"></kbd></p>

> [!NOTE]
> Xong **ổng vô trang web của Yale** và **đổi cái text.**
>
> D: Có phải tôi đã thật sự **hack được web site** của Yale
> không?
>
> A: Không, **chỉ là đổi cái html mà ông nhận được sau khi
> request từ Yale's server thôi**.
>
> D: Correct

<br>

<a id="node-1289"></a>

<p align="center"><kbd><img src="assets/df9a01de549b97dab8f73164992ec3793c845434.png" width="100%"></kbd></p>

> [!NOTE]
> Qua **CSS** Cascading Style Sheet, là **markup
> language** giúp làm các **aesthetic** = **font, size,
> color.. ..**

<br>

<a id="node-1290"></a>

<p align="center"><kbd><img src="assets/07652267bfa619016dd0c99c4b498294cdfae47f.png" width="100%"></kbd></p>

> [!NOTE]
> Nói sơ về **một số properties**của **CSS**

<br>

<a id="node-1291"></a>

<p align="center"><kbd><img src="assets/7b63a7792e021cc0790607bee40600cd6b3b6d9a.png" width="100%"></kbd></p>

<br>

<a id="node-1292"></a>

<p align="center"><kbd><img src="assets/16e1d7d9fce0fc27384e524f44058df486286eeb.png" width="100%"></kbd></p>

> [!NOTE]
> Và một **số tag mới** trong html
> dùng để **define style**

<br>

<a id="node-1293"></a>

<p align="center"><kbd><img src="assets/6ba127c2e8cf50cf4961f0f440bf60244bb70add.png" width="100%"></kbd></p>

> [!NOTE]
> Nói chung là mới nói lướt chưa có gì cụ thể, ví dụ ở đây
> ổng nói có thể link tới file css để riêng để tách riêng phần
> content html và style

<br>

<a id="node-1294"></a>

<p align="center"><kbd><img src="assets/32ece5fd67f6d86d7afb781f5290644a8594e118.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/32ece5fd67f6d86d7afb781f5290644a8594e118.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7a96d841353739e09513bb740cc06bf0a4ff193a.png" width="100%"></kbd></p>

> [!NOTE]
> Ok, start lại với simple
> html page như này

<br>

<a id="node-1295"></a>

<p align="center"><kbd><img src="assets/2b5ed11310a041e51dc99388ce30f4773b7d3040.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2b5ed11310a041e51dc99388ce30f4773b7d3040.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2046e676f5e2e4019a2c8daef1851e15942daf22.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp để**bắt đầu "styling"** cho nó. Ổng bắt đầu với kiểu này
> -**không phải là style tag** mà là kiểu như **inline attribute**
> **style = font-size: large/medium.**.
>
> Kết quả cho thấy đã có thể thay đổi kích thước chữ
>
> Ổng nói để biết có **các key-value như thế nào** thì search
> thêm trên mạng, reading book

<br>

<a id="node-1296"></a>

<p align="center"><kbd><img src="assets/a22456d28ccf2b11f1cdf960a5bbb078ad747f9b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a22456d28ccf2b11f1cdf960a5bbb078ad747f9b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8c8776836324542d78dbf8e6ddbbbc535454ecec.png" width="100%"></kbd></p>

> [!NOTE]
> Define thêm style
> attribute**text-align: center**để **centers text**

<br>

<a id="node-1297"></a>

<p align="center"><kbd><img src="assets/41186bf523c60277699c9cebdfb8729d8676f69f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/41186bf523c60277699c9cebdfb8729d8676f69f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/21537e0957fac35c11829c8b82a966f38fbf1319.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, để làm cái **kí hiệu copy right** đúng hơn thì dùng cái
> này **&#169;** - và ổng nói **mấy cái này có thể tra trên mạng
> để biết, không có gì to tát**
>
> D: Dù bạn chưa bao giờ biết CSS, HTML thì **tại sao cái
> này bad design.**
>
> A: Vì **design style kiểu này khá manual**, khi phải **define
> style cho từng p**

<br>

<a id="node-1298"></a>

<p align="center"><kbd><img src="assets/00e0f5d1c46ad61d75b49aa21cd5a31f4a08b8f2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/00e0f5d1c46ad61d75b49aa21cd5a31f4a08b8f2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/86e3c9cf35d0a0500fd3527bd1e0e166e9912792.png" width="100%"></kbd></p>

> [!NOTE]
> **Correct**. Do đó ta có thể làm vầ, giới thiệu thêm
> **div tag - division**, bỏ **text-align attribute ở parent
> div** và **những cái div con sẽ tự động được thừa
> hưởng**
>
> Kết quả **tuy mất đi cái space ở giữ**a (có thể fix dễ dàng
> sau) nhưng ta **vẫn có cái vụ text centered mà không
> cần define cho mỗi cái paragraph**

<br>

<a id="node-1299"></a>

<p align="center"><kbd><img src="assets/527aa5a1beb73fd000d7ca0625e18a50d50380bd.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **trend mới nhất ngày nay** thay vì dùng
> **division**  tag - div. Thì người ta dùng **"more semantic"** - ý là có ý  nghĩa hơn, đó là **dùng header** (không
> phải heading), **main** và **footer**.
>
> Có những**lợi điểm như giúp cho search engine** như
> Google dễ dàng **biết được à, đó là header, main nơi ta
> có thể focus vào tìm kiếm.**

<br>

<a id="node-1300"></a>

<p align="center"><kbd><img src="assets/0896fee396ff4298b8c7aef27f9aa572d11494c8.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói làm vầy **vẫn có một problem** đó là giả sử
> **muốn  đổi style, thì phải sửa chung cho file này** (có cả
> content) **sẽ tốt hơn nếu có thể tách bạch phần content và
> phần style ra**

<br>

<a id="node-1301"></a>

<p align="center"><kbd><img src="assets/297763c9419a1275e14bcff03b3dfb77ad0f52e2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/00e0f5d1c46ad61d75b49aa21cd5a31f4a08b8f2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/297763c9419a1275e14bcff03b3dfb77ad0f52e2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/00e0f5d1c46ad61d75b49aa21cd5a31f4a08b8f2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6ee5ab4cbc81b59cf5bcd16c7ade56bebd6abd53.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó có thể làm thế này: **define style tag ở trên
> cùng**.
>
> Các k**ey-value attribute vẫn the same** nhưng **chỉ có
> cái là define ở đây**, và **cái nào dành cho phần nào thì
> define như vầy**.
>
> Kết quả y chang **nhưng content clear hơn**, không
> phải **chung đụng giữa content và style**

<br>

<a id="node-1302"></a>

<p align="center"><kbd><img src="assets/7dc4a3ff41a6e3aae72e7e05e475a4107ed2d97e.png" width="100%"></kbd></p>

> [!NOTE]
> Xong thay vì vậy, ổng nói có thể**define với kiểu này .
> centered, .large... nó gọi là class** - chỉ là collection of
> **key-value pair** và ta **tự đặt tên** để tiện sử dụng

<br>

<a id="node-1303"></a>

<p align="center"><kbd><img src="assets/e26d5fe958e5122b05de02531d1a6364dbf4d97f.png" width="100%"></kbd></p>

> [!NOTE]
> Thì với cái này đại khái là ta lại **lùi lại một chút khi lại add 
> chung với content một code** dành cho **style** tuy nhiên **nó
> giúp ra rõ ràng hơn kiểm soát tốt hơn**

<br>

<a id="node-1304"></a>

<p align="center"><kbd><img src="assets/8e1b6be79e257558bc7d0c44cc037b5571b41f0f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8e1b6be79e257558bc7d0c44cc037b5571b41f0f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a7053802956426cc825788a50a5f2f93cc3ddf5b.png" width="100%"></kbd></p>

> [!NOTE]
> Làm thêm một cái nữa đó là **tách bạch hai file css và 
> html** bằng cách dùng **link tag**: 
>
> **<link href="styles.css" red = "stylesheet">**

<br>

<a id="node-1305"></a>

<p align="center"><kbd><img src="assets/3fa409aede7b15933642f74f93949d6822fcd93d.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là ta sẽ qua **framework** (đoán đoán là ta sẽ
> xài  những cái framework **có sẵn để build web page nhanh
> hơn**)
>
> Thì ổng nói **ổng đã chuẩn bị cái này,** trong đó c**ó mấy
> cái tag như head**, **tr**, **th**....thì ổng nói là **không có gì
> ghê gớm chẳng qua lúc đọc documentation** tui thấy **xài
> mấy cái này thì đẹp hơn  thì xài thôi**

<br>

<a id="node-1306"></a>

<p align="center"><kbd><img src="assets/a351017f89771581ce56c398f089646b422b7b96.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái nó là cái **csv thống kê favorite language**,
> **problem set bữa trước**. Nhưng**ổng đã chuyển thành dạng
> html thôi không có gì**

<br>

<a id="node-1307"></a>

<p align="center"><kbd><img src="assets/78188e77bee6d4632453bd09febc69560799cfbe.png" width="100%"></kbd></p>

> [!NOTE]
> Thì giờ ổng muốn làm cho nó đẹp hơn, nhưng đại khái
> là **liệu có cách nào không phải tự code hết các css**, mà
> **dùng lại những cái design đẹp của những người khác
> làm sẵn không**. Đó chính là **framework**

<br>

<a id="node-1308"></a>

<p align="center"><kbd><img src="assets/260f187a2f82f6da5eb8dd0b3af3ead09281e04a.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói tui chỉ **cần add thêm cái link như
> vầy**. Dùng một cái lib gọi là **bootstrap**

<br>

<a id="node-1309"></a>

<p align="center"><kbd><img src="assets/a628d057a1bc9bbb059682a9c4ece8b44f088f28.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái nó là một cái **popular library** **free**, có
> nhiều **css file, có thể dùng free**
>
> Và để dùng nó tui **chỉ đơn giản là đọc documentation**
> và **add cái link như thế này vào**

<br>

<a id="node-1310"></a>

<p align="center"><kbd><img src="assets/dcc782d1da36f7d3008da9c2d78246bf4bd9ac7e.png" width="100%"></kbd></p>

> [!NOTE]
> Và cũng theo document của **bootstrap** nó nói tui phải **add
> thêm cái class gọi là table**, và dùng attribute **table striped 
> để nó có cái màu xám** giữa các cột và hàng.
>
> Chỉ vậy thôi

<br>

<a id="node-1311"></a>

<p align="center"><kbd><img src="assets/d2fcdc4ac885ccd969a67184f8e6e3e024672bbb.png" width="100%"></kbd></p>

> [!NOTE]
> Và chỉ nhiêu đó đã **khiến nó
> đẹp hơn đáng kể rồi**

<br>

<a id="node-1312"></a>

<p align="center"><kbd><img src="assets/46fc9ad5dfd660df34c55270cbf3effbcd794bbf.png" width="100%"></kbd></p>

<br>

<a id="node-1313"></a>

<p align="center"><kbd><img src="assets/b56214578d58fee267b0843534fda6dac256a00c.png" width="100%"></kbd></p>

> [!NOTE]
> Nói**lướt nhanh về một syntax của javascript**
> không khó nên khỏi note

<br>

<a id="node-1314"></a>

<p align="center"><kbd><img src="assets/1b1574ead708a45b06df38a0d3c9e97b30f204b6.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái javascript sẽ **cho phép ta manipulate cái
> DOM này**. Từ đó cho phép **không cần phải mỗi lần mỗi
> reload page**

<br>

<a id="node-1315"></a>

<p align="center"><kbd><img src="assets/827504cc99ce571b14e9cb21168fba67e0bcd0d6.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là js sẽ **chạy trên client size web**
> **browser** chứ **không phải server**

<br>

<a id="node-1316"></a>

<p align="center"><kbd><img src="assets/7be5bf79cd180dfc9e990081f406cbcf36dbb2cb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7be5bf79cd180dfc9e990081f406cbcf36dbb2cb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6533bae9201df3c86d19a197b02448aea9c45ec1.png" width="100%"></kbd></p>

> [!NOTE]
> Xong, quay lại cái page này, thử làm cái gọi là thay
> vì Hello! thì **enter tên vào và Hello David!**
>
> Thì hiện tại khi **click button chưa có gì xảy ra** vì **chưa
> implement cái gì**

<br>

<a id="node-1317"></a>

<p align="center"><kbd><img src="assets/af4453ceb132557b9d176b34e6799e9cd9113fb3.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đây, các **event** trong javascript

<br>

<a id="node-1318"></a>

<p align="center"><kbd><img src="assets/4e47d59d6e134d2a9f4539496b3cfb02260270be.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4e47d59d6e134d2a9f4539496b3cfb02260270be.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/72c2952b5bc073008a28e78fb9602c73ed8bd5b9.png" width="100%"></kbd></p>

> [!NOTE]
> Thế là ta có thể dùng **onsubmit** = greet() như vầy,
> define function **greet**() bằng cách**define trong tag
> script**.
>
> Ta sẽ cho nó show một cái **alert** say hello world **dù là
> không đẹp mắt lắm nhưng tạm thời vậy**

> [!NOTE]
> Đồng thời, ta cũng sẽ làm vầy, **return false**, để nó không
> thật sự submit mà như hồi nãy ta biết là nó sẽ **gắn cái
> query của form vào url và gọi url lại.**
>
> Thì ổng nói cái này đơn giản là **tui đọc trong doc thấy
> vậy**

<br>

<a id="node-1319"></a>

<p align="center"><kbd><img src="assets/bb0791b7c48b8d3658321cd9089efe15534da608.png" width="100%"></kbd></p>

> [!NOTE]
> Load lại, **click submit
> nó show alert dialog**

<br>

<a id="node-1320"></a>

<p align="center"><kbd><img src="assets/82d3cd2b69ea41c64b3ae6d9adc5a2395c146175.png" width="100%"></kbd></p>

> [!NOTE]
> Để **lấy value user enter vào form**, đầu tiên ta **gán id cho input**,
> (cái này thì giống java rồi) là**id = "name"**
>
> Và "lấy nó" bằng cách: **document.querySelector(' #name').value**
>
> Và **concatenate nó với hello.**

<br>

<a id="node-1321"></a>

<p align="center"><kbd><img src="assets/9f5f7819482fc32e9dec8c5a457334a9de8d1558.png" width="100%"></kbd></p>

<br>

<a id="node-1322"></a>

<p align="center"><kbd><img src="assets/b680c2a54ff45d1edda0c8fd5245f76ed9a3808e.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo đại khái là **sẽ tốt hơn nếu có thể tách js** ra khỏi
> **content**, giống như **ta làm với css vậy.**
>
> Nên có thể làm vầy, ở đây giống java, đó là **ta có thể gọi /
> lấy cái form và addEventListener cho nó**.
>
> Trong đó define tên function không có on, ví dụ **onsubmit**
> thì ở đây là **submit**, và có thể dùng **anonymous / lambda
> function** nhận có argument là một event (**cái kiểu nó vậy**)
>
> Còn lại thì như trên chỉ có thêm là gọi **event.preventDefault() 
> có tác dụng chỉ giống như cái vụ return false ở cách làm 
> hồi nãy**

<br>

<a id="node-1323"></a>

<p align="center"><kbd><img src="assets/e7790b2567db5ff56f6e42f3c964c8208a024cd9.png" width="100%"></kbd></p>

> [!NOTE]
> Xong nhưng khi làm
> thử thì nó ko work

<br>

<a id="node-1324"></a>

<p align="center"><kbd><img src="assets/b71df1d8ecb201f518cef7cd7aa3245fb36fb10c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b71df1d8ecb201f518cef7cd7aa3245fb36fb10c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/93f8c84944c17ae934b9992fb689b82a208fe25a.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói vấn đề là giống như ta **từng gặp trong C,** đó
> là**tại  thời điểm nó gọi document.query...
> addEventListener...** thì c**ái form chưa tồn tại.**
>
> Nên **move cái script tag xuống dưới thì nó work**

<br>

<a id="node-1325"></a>

<p align="center"><kbd><img src="assets/8b0c69e6351874e91e2a666e144c86d3ef84e9d2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8b0c69e6351874e91e2a666e144c86d3ef84e9d2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/25cbdbffe9be678718fbc88b75f9de57e6f270ae.png" width="100%"></kbd></p>

> [!NOTE]
> Thì giải pháp hay hơn đó là**bỏ nó vào một cái event 
> listener là DOMContentLoaded.**
> Với cách này thì **đoạn code add event listener cho form
> chỉ được chạy sau khi DOM content đã loaded xong**

<br>

<a id="node-1326"></a>

<p align="center"><kbd><img src="assets/cebbf4f2b83e59de6bc5986ea078c7fd8d24d01c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/cebbf4f2b83e59de6bc5986ea078c7fd8d24d01c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/95721844fd74267adde446269899876aa6915ed2.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp làm động tác**tương tự với css đó là
> ta tách nó ra thành file riêng**

<br>

<a id="node-1327"></a>

<p align="center"><kbd><img src="assets/2baad84196e14347b281222eba3025549ad5f5fb.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói có thể cho nó vui hơn, bằng làm như cái
> này (ổng mở 1 file làm sẵn rồi) trong đó khi **gõ dòng
> chữ ở dưới tự động update không cần button submit gì
> cả**
>
> Thì cái này đại khái là **có liên quan đến finger up/down
> event**

<br>

<a id="node-1328"></a>

<p align="center"><kbd><img src="assets/7a17bae63e2b2a16dd9f318f11836b352cf58e16.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7a17bae63e2b2a16dd9f318f11836b352cf58e16.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/86bee6e0a778a3deaaecc9f15abdfe5c2a6b3952.png" width="100%"></kbd></p>

> [!NOTE]
> Cũng dễ hiểu, vài ghi chú thôi
>
> **if (input.value)**: **check trong đó có text hay chưa giống
> như check null vậy**
>
> Có cái **syntax để show string hơi weird trong js** là **thay 
> vì dùng 'a' hay "a"  thì  nó dùng back stick là cái này `a`**
> (dưới nút escape)
>
> Và dùng **${....}** để **infer value giống như f"{...}" trong 
> python**

<br>

<a id="node-1329"></a>

<p align="center"><kbd><img src="assets/bba02ad1fa4d859025747a90c0603c74394bfa4c.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp đại khái là ta có thể dùng
> javascript để làm cái này: **sort**

<br>

<a id="node-1330"></a>

<p align="center"><kbd><img src="assets/f54c2953f580c00a1fdd3f763bce4a7de7e8de8c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f54c2953f580c00a1fdd3f763bce4a7de7e8de8c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/91bdb059f6e78c6585ff63a62d3c094d14242e6e.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái cũng như **nhờ bootstrap** **làm đẹp thêm cho 
> webpage** thì ở đây cũng có thể **nhờ nó làm cái này**.
>
> Ổng nói tui đọc **documentation** và**copy paste** những cái
> link này 
>
> Rồi thêm cái **syntax** thế là xong

<br>

<a id="node-1331"></a>

<p align="center"><kbd><img src="assets/1c3cd3a3d36fe2443c7ebbbaa037109e01b54da0.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi ổng nói qua cái ví dụ khác là bấm
> để **change background color**

<br>

<a id="node-1332"></a>

<p align="center"><kbd><img src="assets/06919e169fa612030d8b3e11fdff2cd1d693318d.png" width="100%"></kbd></p>

<br>

<a id="node-1333"></a>

<p align="center"><kbd><img src="assets/c4982f7f8fc36466b359e1fd64ab511dca76e8d1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c4982f7f8fc36466b359e1fd64ab511dca76e8d1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ff19c62a47bcf9b2c9befb80ebd3ec8e815ccf12.png" width="100%"></kbd></p>

> [!NOTE]
> Cũng đơn giản. Chỉ là **add event listener** và **set value
> cho**
>
> **body.style.backgroundColor** thôi.
>
> Và trong **css, red, là ...'red'**. That's it

<br>

<a id="node-1334"></a>

<p align="center"><kbd><img src="assets/e30ef1ccacbf01b1fcb19b916828c3363fb993cd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e30ef1ccacbf01b1fcb19b916828c3363fb993cd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7e98f530df79f0f72ec72cf806c09d739fed84fb.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp ổng show một ví dụ khác trong đó chữ**hello, world** cứ 
> nhấp nháy (**blink**)
>
> Thì đại khái là dùng cái này: **window.setInterval(blink, 50)**
> có nghĩa là nó cứ **50 millisecond** thì gọi function này một lần
>
> Ổng nói thêm là không để **blink**() mà chỉ là blink

> [!NOTE]
> Function **blink** cũng đơn giản, chỉ là **toggle**
> state visibility thôi

<br>

<a id="node-1335"></a>

<p align="center"><kbd><img src="assets/fd2ac5bef03db93c479ed3e8430e7014a7cdb03b.png" width="100%"></kbd></p>

> [!NOTE]
> Xong **ổng show hàng cái** này, cơ bản là dùng **key-up
> event** và **search trong dictionary** như đã làm trong
> **PS5 thôi**

<br>

<a id="node-1336"></a>

<p align="center"><kbd><img src="assets/4650d405a1148b2aa906299a9b73769bad5f1162.png" width="100%"></kbd></p>

> [!NOTE]
> **Final example** đại khái là (với đoạn code này) khi nào 
> **web browser biết được location của user** thì nó sẽ **gọi 
> function này**
>
> Và ở đây **chỉ đơn giản là write nó ra** (kiểu như **in ra**)
> bằng **function document.write()**

<br>

<a id="node-1337"></a>

<p align="center"><kbd><img src="assets/f864cdee5fa9bd7a4bf04cedf26df8d4326d6346.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f864cdee5fa9bd7a4bf04cedf26df8d4326d6346.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e4c03bf30262c0118921e093c47c04e3f3998348.png" width="100%"></kbd></p>

<br>

<a id="node-1338"></a>

<p align="center"><kbd><img src="assets/47fc6f671428ed142c6853e342b55b4353c03f24.png" width="100%"></kbd></p>

<br>

