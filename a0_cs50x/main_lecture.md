# Main Lecture

📊 **Progress:** `136` Notes | `208` Screenshots

---
<a id="node-1575"></a>

<p align="center"><kbd><img src="assets/7f9e096cb003caac5a6c50f0f92ad28186af279f.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái tuần trước ta đã dùng **http-server** này, được
> **cài sẵn trong cs50** cho phép **serve cái webpage**
> của mình. Thì đại khái là nó chỉ là một trong các
> tools như vậy

<br>

<a id="node-1576"></a>

<p align="center"><kbd><img src="assets/08e7c0b1f5d6cec950a619292ab76c4b4201f5ec.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/08e7c0b1f5d6cec950a619292ab76c4b4201f5ec.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e84c633d557199194d22a5682aa2e501a49ffeca.png" width="100%"></kbd></p>

> [!NOTE]
> Ta cũng nhớ `.../` là **original
> address**, và có thể có **path**

<br>

<a id="node-1577"></a>

<p align="center"><kbd><img src="assets/1fe46265a8958c3c520086bc08d30ca966bb9c84.png" width="100%"></kbd></p>

> [!NOTE]
> ở đây ta sẽ gọi chung là "**route"** `-`
> common terminology

<br>

<a id="node-1578"></a>

<p align="center"><kbd><img src="assets/d88aa8753820a53a7b509dac1e9e5bc30eba0128.png" width="100%"></kbd></p>

<br>

<a id="node-1579"></a>

<p align="center"><kbd><img src="assets/8a1ec2772e0f2c744c16c2db435362babb0b17a2.png" width="100%"></kbd></p>

> [!NOTE]
> Nhắc lại chút về nội dung của cái phong bì mà Phyllis
> gửi cho Brian. Nó sẽ có cái **host**, kiểu như **địa chỉ**, và
> Cái query **search?q=cats** ổng nói **cần phải có một
> cái giúp parse nó ra**

<br>

<a id="node-1580"></a>

<p align="center"><kbd><img src="assets/b407c7fbe8634cb0d2816aca8fdb71bfc91d4677.png" width="100%"></kbd></p>

<br>

<a id="node-1581"></a>

<p align="center"><kbd><img src="assets/b333516e84a4eb23cc7dfc8007c20652c4f2b8e5.png" width="100%"></kbd></p>

> [!NOTE]
> **Flask** là framework cho phép ta kiểu như
> **kết dính các ngôn ngữ khác như html, css,
> sql, js lại**

<br>

<a id="node-1582"></a>

<p align="center"><kbd><img src="assets/14ab539e3c78a546843f0aed9a84b4f48e77a1f6.png" width="100%"></kbd></p>

> [!NOTE]
> **Jinja** không phải là programming language mà
> là c**ollection các syntax.**
>
> Và ổng **cũng phổ biến** khi một**framework này
> lại `mượn/dùng` một language khác** kiểu như
> để khỏi phải reinvent the wheel

<br>

<a id="node-1583"></a>

<p align="center"><kbd><img src="assets/7ee6d066707f5013efe759567f4be83915f3a3f9.png" width="100%"></kbd></p>

> [!NOTE]
> **Bootstrap** là lib **giúp làm
> webpage nhanh hơn dễ hơn**
> thì **flask** sẽ giúp trong việc tạo
> **web server**

<br>

<a id="node-1584"></a>

<p align="center"><kbd><img src="assets/3e11ffef842c88f7231faba4330d55fcd9078f62.png" width="100%"></kbd></p>

> [!NOTE]
> Và để build một cái google.com với
> flask thì đây là convention, ta cần
> **app.py** và **templates**

<br>

<a id="node-1585"></a>

<p align="center"><kbd><img src="assets/0cfee61f1b36f5d374a9c8b8dbb314d26e7e91fa.png" width="100%"></kbd></p>

> [!NOTE]
> Ngoài ra còn có **requirements.txt** là nơi **chứa
> các lib** mà có thể ta cần.
>
> và **static/** là nơi **chứa các static file** như image,
> css, js

<br>

<a id="node-1586"></a>

<p align="center"><kbd><img src="assets/d9956983e807c432e147001cf99473048bc45442.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ổng nói đây, đoạn code này là cách để ta 
> **implement và serve một web application** sao cho**khi 
> có ai đó truy cập** sẽ in ra chữ hello world
>
> Nhìn qua có thể thấy bắt đầu với việc**import Flask,**
> **render_template**
>
> Xong để mấy dòng sau sẽ giải thích sau nhưng có cái
> quen quen đó là **index.html**

<br>

<a id="node-1587"></a>

<p align="center"><kbd><img src="assets/8f7940741c92ad20f5d187ae4bf74689be6cfe37.png" width="100%"></kbd></p>

<br>

<a id="node-1588"></a>

<p align="center"><kbd><img src="assets/fffd37e3e2a3e803e1bf86ce021940c87e69eec1.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng tạo file simple này, chỉ có chữ **hello, world**.
>
> Và để  nó có thể **view tốt trên mobile** ta thêm dòng code **magical:
>
> <meta `name="viewport"` content `=` `"initial_scale=1,` width=device-width">**

<br>

<a id="node-1589"></a>

<p align="center"><kbd><img src="assets/2b05354d55c121ae10700dcb8f6fb31c14c860a6.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng tạo file **app.py** (như convention nói hồi nãy).
>
> Và đầu tiên, **import Flask, `render_template,` request**
> từ flask. Thì ổng nói cái này do tui đọc trong doc, nên
> biết và làm theo vậy, đây là 3 cái building block giúp
> ta làm

<br>

<a id="node-1590"></a>

<p align="center"><kbd><img src="assets/6f8030ac369faa4dc28895af57f8739117d12229.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ổng hỏi là có ai nhớ tại sao lại để **__name__**như vầy không (tương tự ở đâu đó đã học)?
>
> D: Thì đại khái là đây là cách để cho máy tính nó biết ta
> muốn "**biến cái file này thành Flask application**" chứ không
> phải gọi nó. Chưa hiểu lắm

<br>

<a id="node-1591"></a>

<p align="center"><kbd><img src="assets/bf89f3b2a7216214678e602e47b7e7437bcad050.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái tiếp theo là ở đây, "tôi sẽ là người **chịu trách
> nhiệm cho việc serve cái file nào** khi được request.
>
> Mà tuần trước với **http-server**, nó "làm giùm mình"
>
> Còn bây giờ nôm na là ta sẽ **viết function**, **handle việc serve `/` trả
> kết quả** khi được request (từ web browser). Hay chính là
> viết API

<br>

<a id="node-1592"></a>

<p align="center"><kbd><img src="assets/3fbce217405368184eb25f6f3a4d3036e386a8a3.png" width="100%"></kbd></p>

> [!NOTE]
> **@app.route()** ổng nói là gọi là Python **decorator**
>
> Và **@app.route("/")** sẽ thể hiện là đây là đoạn
> code mà ta muốn nó**execute khi nhận
> request là slash ".../"** `=` khi user visit **default page**của website

<br>

<a id="node-1593"></a>

<p align="center"><kbd><img src="assets/5c42a75e91949bbef6302d19d705d085f251640f.png" width="100%"></kbd></p>

> [!NOTE]
> Và ta return "hello, world"
>
> Gọi flask run để start server

<br>

<a id="node-1594"></a>

<p align="center"><kbd><img src="assets/0b6be5a4f120b9873cad59d5f86fe188dc319305.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0b6be5a4f120b9873cad59d5f86fe188dc319305.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fd0311b4357e4fcc8f26e3077a7da455b7a0b882.png" width="100%"></kbd></p>

> [!NOTE]
> thì kết quả (khi mở link bằng web browser) ta cũng thấy dòng 
> chữ hello, world nhưng inspect thì thấy nó chỉ là dòng text `-` 
> Chính là kết quả trả về của function index()

<br>

<a id="node-1595"></a>

<p align="center"><kbd><img src="assets/a5f9f6dc28308fddb8809678830950e608fba407.png" width="100%"></kbd></p>

> [!NOTE]
> Và khi ta muốn nó **serve/trả về cái file `/` page index.html** thì ta
> có thể làm vầy: **render_template("index.html")**

<br>

<a id="node-1596"></a>

<p align="center"><kbd><img src="assets/f6e579a5b087c347e1b87bf650ce957ec4b897ee.png" width="100%"></kbd></p>

> [!NOTE]
> Và kết quả cũng chỉ là dòng chỉ **hello, world** nhưng
> inspect sẽ thấy nó (response) là cái **html code** ở trong
> **index.html chứ không phải text khơi khơi**

<br>

<a id="node-1597"></a>

<p align="center"><kbd><img src="assets/cc66ae2d26dfddf0a32241ede1f0fe7355faa456.png" width="100%"></kbd></p>

> [!NOTE]
> Kế tới ổng muốn làm cái mà tuần trước với
> **http-servers không thể giúp** được đó là làm sao
> để user khi visit url **.../?name=David** thì nó serve
> **"Hello, David"**

<br>

<a id="node-1598"></a>

<p align="center"><kbd><img src="assets/39f7ed22b8cbbd011a2917b69be75dd179938b49.png" width="100%"></kbd></p>

> [!NOTE]
> Thì muốn vậy phải dùng cái **request**: cụ thể là
> **request.args** sẽ mang **argument** gửi lên với
> request

<br>

<a id="node-1599"></a>

<p align="center"><kbd><img src="assets/29dccfdc5ee29f0b5f9bf56d944dd97bb5afe519.png" width="100%"></kbd></p>

> [!NOTE]
> Thì dùng như vầy, ổng **check xem 'name' có trong** 
> **request.args** không có thì lấy ra (**request.args['name']**)
> không thì cho name `=` 'world'
>
> Thì question là dựa vào đây thử đoán cái request.args
> có data type là cái gì?
>
> A: **dictionary**D: Correct

<br>

<a id="node-1600"></a>

<p align="center"><kbd><img src="assets/882e47e2cc156783a4bbf91e94da253c80243195.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói chuyện gì sẽ xảy ra khi tui cứ **blindly** 
> **lấy cái value của key name** ?
>
> A: **Nếu dictionary không có key name**, thì nó sẽ bị **lỗi
> không tìm thấy key
>
> D: Correct**

<br>

<a id="node-1601"></a>

<p align="center"><kbd><img src="assets/83fed015bc30f08586a43d5e74edb087063c950c.png" width="100%"></kbd></p>

> [!NOTE]
> Thì có vài điều ở đây:
>
> Ta muốn nó **place holder cho một cái name value**
> được đưa vào (để có thể hiện hello, David.)
>
> Thì đây chính là **convention của flask** (mà thật ra
> chính cái này**{{..}}** là Jinja, như đã nói, không phải
> programming language mà là **syntax**)
>
> Thì cái này tương đương **%s** trong C, **f"{}"** trong
> Python, **?** Trong SQL....

<br>

<a id="node-1602"></a>

<p align="center"><kbd><img src="assets/3603b91abbbeb7b1e3009334cf03dff9c8d3ad58.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3603b91abbbeb7b1e3009334cf03dff9c8d3ad58.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/cd335e97d922cf38cb6ac8c1b8dd5c8ff21d64dc.png" width="100%"></kbd></p>

> [!NOTE]
> thì, **render_template** sẽ nhận sau cái **arg đầu
> tiên**là cái **file** thì những arg cái sau là các**argument
> value cho các place holder**
>
> Trong file ta để {{**placeholder**}} thì gọi ở đây sẽ gọi 
> `render_file("index.html",` **placeholder** `=` name)

<br>

<a id="node-1603"></a>

<p align="center"><kbd><img src="assets/152fa0fa15a4b97477a544140c95eead35814928.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả là ta đã có thể show Hello David
> khi user access `".../?name=David"`

<br>

<a id="node-1604"></a>

<p align="center"><kbd><img src="assets/8a37973349e1079b60550ffb9f03ef8b5f54f1bb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8a37973349e1079b60550ffb9f03ef8b5f54f1bb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b47b1b157af3aa75f0634ba8c4acbda20638ecb8.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói để **place_holder** không ổn vì **không thể hiện
> được ý nghĩa**, và sẽ **có thể có nhiều place holder khác**,
> nên ổng đổi về lại **name**, và ta sẽ phải chấp nhận dù nhìn
> **có vẻ hơi stupid** trong code **name=name**. Nhưng đó là
> the norm, là **thông thường người ta cũng làm vậy**

<br>

<a id="node-1605"></a>

<p align="center"><kbd><img src="assets/4803e0f5cec8f5bc3983532ddd84e72b3fa6e346.png" width="100%"></kbd></p>

> [!NOTE]
> Kế đến thay vì**access dictionary theo lối thông thường []**,
> thì python có support **get(key, default value)**. Trong đó
> nếu không define default value thì khi không có key nó sẽ
> trả về **'None'**
>
> Ta có thể override cái default value là "world" này do đó không 
> cần phải check if else nữa

<br>

<a id="node-1606"></a>

<p align="center"><kbd><img src="assets/22fbbc95a3b53a3f4fada430177326fba542e2dd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/22fbbc95a3b53a3f4fada430177326fba542e2dd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/02f50a27ed4d51d6c03d5889ca0a2f33d3e70d6f.png" width="100%"></kbd></p>

> [!NOTE]
> Kế tiếp ổng đổi thành thế này, tạo cái **form** với các
> attribute như bữa trước đã biết qua như **autocomplete**,
> **autofocus** **placeholder**
>
> Sau đó ổng nói tui sẽ **vừa làm front end vừa làm back
> end**, với cái này: **action="greet"** **method="get"**.
>
> Ý là đoạn code này sẽ **handle hành động sau khi user
> submit button Greet**. Đó là nó sẽ **truy cập url ".../greet"**với****method**GET**và**với submit nó sẽ gắn `?name="giá` trị enter vào form"**

<br>

<a id="node-1607"></a>

<p align="center"><kbd><img src="assets/858c7fd790491b6b62af7e1642a91575e583459b.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, ổng tạo html file thứ hai **greet.html**

<br>

<a id="node-1608"></a>

<p align="center"><kbd><img src="assets/f29df779ea437b30b9fdba80163015cfe78bf5b0.png" width="100%"></kbd></p>

> [!NOTE]
> Và tạo function **@app.route("/greet")** như vầy. Nhưng
> question là nếu tôi muốn nó hiện thị "hello, David" thì phải
> sửa ntn?
>
> A: `@app.route("/greet")`
>         name `=` request.args.get("name", "world")
>         return `render_template("greet.html",` `name=name)`
>
> D: Correct!

<br>

<a id="node-1609"></a>

<p align="center"><kbd><img src="assets/561e7847a8945f03423e4e103b907aeb7de057b4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/561e7847a8945f03423e4e103b907aeb7de057b4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ba3bc7514248a461fbb77ba3e51fb3d0747d0d87.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả là khi click button Greet, url đổi từ `.../`
> thành **.../greet?name=David** và với `../greet,` server
> sẽ serve file **greet.html,**nhét name vào place holder

<br>

<a id="node-1610"></a>

<p align="center"><kbd><img src="assets/531cad96e834931a0dd2d4b8cace42584fe3b137.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng hỏi là tới đây có thể có ai đó nghĩ rằng đây
> không phải good design, tại sao?
>
> A: Vì chỉ có **1 cái đơn giản mà phải tốn 2 file html**
>
> D: Correct. Đại khái là vì **hai cái file chỉ khác  nhau chỗ cái
> body.**
>
> Gỉai pháp là **Layout**

<br>

<a id="node-1611"></a>

<p align="center"><kbd><img src="assets/4926661dbacbadd95e3556f7a734deecafb3934f.png" width="100%"></kbd></p>

> [!NOTE]
> ổng mới tạo file **layout.html** như vầy, trong body 
> Dùng một syntax của **jinja**: **{%block body%}{%endblock%}**
> Thì đại khái nó **cũng là một placeholder**

<br>

<a id="node-1612"></a>

<p align="center"><kbd><img src="assets/4071ec7cdf8201fd1105b164951db58ba924b30a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4071ec7cdf8201fd1105b164951db58ba924b30a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/46e9e1521ab0fa065726e87895aad8a6877e25d9.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi qua file index.html sửa lại thành vầy, bỏ hết chỉ giữ cái 
> form
>
> Thì cái dòng đầu tiên {% extends "layout.html" %} đại khái 
> sẽ bảo máy tính là, hãy**lấy cái file layout.html** và **có nhiêu 
> trong đó thì show ra**, có điều, trong cái block tên là body của 
> nó (layout.html) thì show cái nội dung dưới đây".
>
> và nội dung sẽ nằm ở trong hai cái {%block body%}
> và {%end block%}

<br>

<a id="node-1613"></a>

<p align="center"><kbd><img src="assets/ed5472dddc5ea1157a8abcb4bb1fe8e6f48f226e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ed5472dddc5ea1157a8abcb4bb1fe8e6f48f226e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ab8d1c3b82177812bc175099b90e698a36e11da6.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự như vậy đối với file **greet.html**
>
> Chú ý rằng, trong **app.py** vẫn là **serve hai file**,
> **index.html** và **greet.html**, chẳng qua, nội dung
> hai file thay vì bị duplicate nhiều chỗ giống nhau
> như header,...thì giờ sẽ được khắc phục bằng
> việc **cùng lấy phần đầu và đít từ file layout.html**

<br>

<a id="node-1614"></a>

<p align="center"><kbd><img src="assets/267f0a73723832c71f1e03578f12e714f03a1e8c.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả run lại thì vẫn không đổi, nhưng code thì tốt hơn

<br>

<a id="node-1615"></a>

<p align="center"><kbd><img src="assets/3a2c38eff079de1873740d8c98150c649690c07b.png" width="100%"></kbd></p>

> [!NOTE]
> và khi ta inspect sẽ thấy, nội dung ở **phần đầu sẽ lấy từ
> layout.html**, và nó (máy tính) **gắn cái body chứa cái  form
> define trong index.html vào**.
>
> Và vì nó nhét vào nên indentation không đẹp lắm nhưng
> ổng nói indentation (trong html) là để cho human xem chứ
> máy nó  không care

<br>

<a id="node-1616"></a>

<p align="center"><kbd><img src="assets/52203d7796b9a6263f7a77ec853efe39763a4d1d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/52203d7796b9a6263f7a77ec853efe39763a4d1d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b293625d37f2a19ed6dc4885d91d19df33149029.png" width="100%"></kbd></p>

> [!NOTE]
> Trả lời câu hỏi là l**àm sao biết chắc user visit họ sẽ tới cái 
> form trước** (index.html) 
>
> D: Thì đó là vì ta define `@app.route("/")` 
> `->` `"..(hostname).../"` là default

<br>

<a id="node-1617"></a>

<p align="center"><kbd><img src="assets/7d2d07d370aebdbd2a08ec0eed34f7bc7a701f91.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Tại sao đây là bad design. Khi tui gõ tên tui
> vào và nó hiện lên url như vầy
>
> A: Vấn đề security, khi nó hiện thông tin cá nhân
> trên url. Thằng nào đó ngồi gần có thể nhìn lén
> và biết name, password của mình

<br>

<a id="node-1618"></a>

<p align="center"><kbd><img src="assets/8f4d25fbb9694a259fef45e27d5369d7de815b25.png" width="100%"></kbd></p>

> [!NOTE]
> Có cách giải quyết đơn giản là **thay "get" bằng "post"**

<br>

<a id="node-1619"></a>

<p align="center"><kbd><img src="assets/23945f5598d677f562af69a118b870e7d298b09f.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng submit tên vào nó ra lỗi này 405 error

<br>

<a id="node-1620"></a>

<p align="center"><kbd><img src="assets/8d4f0faf7292143715b8b78215cb75828e8b9b64.png" width="100%"></kbd></p>

> [!NOTE]
> Ta cần **sửa lại app.py**, với việc thêm arg **methods**, mà 
> vốn dĩ **default** **khi không khai báo gì thêm sẽ là GET**,
> ta sẽ **define methods `=` ["POST"]**
>
> Thì ổng nói đại khái là máy tính sẽ vẫn đọc thông tin
> đại khái trong envelope **nhưng đưa nó vào `header/` 
> nôm na là che giấu nó**
>
> Chỗ này David quên sửa lại (lúc sau mới sửa) là với POST
> phải dùng **request.form.get("name", "world")**chứ không
> phải**request.arg.get("name", "world")**

<br>

<a id="node-1621"></a>

<p align="center"><kbd><img src="assets/942da533e8054e6bafce3b3468264acd8d7e5a44.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/942da533e8054e6bafce3b3468264acd8d7e5a44.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a6ef296019d0bf863eb3a1e3987dc659b18faf00.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả là, nó sẽ **vẫn show hello David** nhưng**không
> show tên David trên url**

> [!NOTE]
> (Thật ra là cái bug (Không show David) mà ổng cũng không
> để ý, sửa lại dùng request.form thay vì request.arg thì sẽ
> được)

<br>

<a id="node-1622"></a>

<p align="center"><kbd><img src="assets/c4ffc9e4330f4849b48af6c19ec5ab0422ebddfd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c4ffc9e4330f4849b48af6c19ec5ab0422ebddfd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b66b5f9ec013b6536d52c51a169f562b09b0a625.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ổng cho xem lại cái **payload** của
> **Inspection** khi click Submit **để thấy cái tên David
> được gửi lên.**
> Và nói là bạn**có toàn quyền access tới các thông
> tin mà browser gửi tới cho bạn.**

<br>

<a id="node-1623"></a>

<p align="center"><kbd><img src="assets/df1c2426b31e321c06b39d0db7534f9d33875341.png" width="100%"></kbd></p>

<br>

<a id="node-1624"></a>

<p align="center"><kbd><img src="assets/fa38db58bd11e4cacba0d6278f9ac95d362a1a91.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fa38db58bd11e4cacba0d6278f9ac95d362a1a91.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/16a1179eac7f6195e99ed84f43a6450e7b1b66cb.png" width="100%"></kbd></p>

> [!NOTE]
> Kế tiếp ổng nói ở đây thật ra tui **không cần tới 2 route  khác
> nhau**.
>
> Mà **chỉ cần dùng cái default path "/"** và **check  cái method
> để nếu là GET** `=` là method default thì tui **serve nó cái
> index.html.**
>
> Còn **nếu nó là POST** (khi submit cái form, có method là
> POST) thì nó s**erve cái greet.html**

<br>

<a id="node-1625"></a>

<p align="center"><kbd><img src="assets/bd9d8211c36ecaaba1b4f828bff96798f19358cc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bd9d8211c36ecaaba1b4f828bff96798f19358cc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8dd57aca39ddc5bbf738aac0597ab8d0a90a4f3f.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả nó vẫn như vậy và **chỉ cần 1 route**

> [!NOTE]
> (Thật ra là cái bug, đáng lẽ phải hello David mà ổng
> cũng không để ý, sửa lại dùng **request.form** thay vì
> **request.arg** thì sẽ được)

<br>

<a id="node-1626"></a>

<p align="center"><kbd><img src="assets/d94287eacedadf37d79911f9b73f5e00e67514a8.png" width="100%"></kbd></p>

> [!NOTE]
> Khi reload, nó sẽ hỏi confirm. Thì cái này chỉ là **browser
> nó careful** giống như khi ta add item vào giỏ hàng trên
> tiki và reload thì nó cũng sẽ confirm.
>
> Thì có thể **click vào url và nhấn enter** (thay vì bấm nút
> reload)

<br>

<a id="node-1627"></a>

<p align="center"><kbd><img src="assets/7acde6f45b6dc3a163c685f9dd865ae46ead12a3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7acde6f45b6dc3a163c685f9dd865ae46ead12a3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6582d5a3bcd0473b1c1e76e3b3cc607c18276aa6.png" width="100%"></kbd></p>

> [!NOTE]
> Xong để sửa cái bug là submit với David mà nó vẫn hiện
> hello world, thì mới nói qua là **với POST**, thì cái argument (ở
> đây là name enter vào) phải lấy từ **request.form** thay vì
> **request.arg `-` vốn chỉ dùng cho GET**

<br>

<a id="node-1628"></a>

<p align="center"><kbd><img src="assets/9c1fbb42aed35ce5662ee93af633a97e14b3f36a.png" width="100%"></kbd></p>

> [!NOTE]
> Tới đây ổng nói về cái web hồi xưa ổng làm,
> cho phép **user register sport**gì đó. Giờ ta
> thử sẽ làm lại

<br>

<a id="node-1629"></a>

<p align="center"><kbd><img src="assets/dab7d7a174ee1802062df3b17c8bc7b78c2bc6b7.png" width="100%"></kbd></p>

<br>

<a id="node-1630"></a>

<p align="center"><kbd><img src="assets/b91e22e4b0eb71d4e88c67d56c44df14df9e31ce.png" width="100%"></kbd></p>

> [!NOTE]
> Đầu tiên ổng code cái**app.py để serve html file**

<br>

<a id="node-1631"></a>

<p align="center"><kbd><img src="assets/a149059a6be8b4ace376c53cad054a6a38faaad3.png" width="100%"></kbd></p>

> [!NOTE]
> File index thì có cái **form** như hay làm thôi  với các
> **argument**, **action="/register"** phương thức **post**.
>
> Như đã biết có nghĩa là khi **submit** nó sẽ gọi **url: .../register**, 
> với method **POST, và gửi thông tin name lên.**Chú ý là ở đây mình để **name `=` "password"** thì trong 
> kia sẽ lấy ra: **request.form.get("password", "default value")**

<br>

<a id="node-1632"></a>

<p align="center"><kbd><img src="assets/764da2ed2e42c404d01a2ccdd831a047210a0693.png" width="100%"></kbd></p>

> [!NOTE]
> Ở dưới ổng làm cái "Selection" để chọn
> với **<select> tag** và **<option>** như này

<br>

<a id="node-1633"></a>

<p align="center"><kbd><img src="assets/e341af75f143d109ab96070e03f40b23c11d9b48.png" width="100%"></kbd></p>

> [!NOTE]
> Chạy **flask run** để start server

<br>

<a id="node-1634"></a>

<p align="center"><kbd><img src="assets/1ff67a6d7bad4a6aaeccebac356f9d14b0211604.png" width="100%"></kbd></p>

> [!NOTE]
> Thì nó ra vầy, cũng ok, nhưng ổng nói để tui cải tiến chút xíu
> để cho nó đừng có chọn basketball sẵn như vậy

<br>

<a id="node-1635"></a>

<p align="center"><kbd><img src="assets/8bb3f9be858ba2df0b7045bfcf36cfa27b2f0943.png" width="100%"></kbd></p>

> [!NOTE]
> Bằng cách là ổng **thêm một option tên** là**Sport** để dạng
> **disabled**, và **chọn sẵn (selected)**

<br>

<a id="node-1636"></a>

<p align="center"><kbd><img src="assets/0f32d44b9bd12101fddff9290a7d8eb757638b1c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0f32d44b9bd12101fddff9290a7d8eb757638b1c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c00a882558746499566e1580b3c458ba085d32d4.png" width="100%"></kbd></p>

> [!NOTE]
> Thì nhìn nó better, kiểu như Sport giống như cái title vậy

<br>

<a id="node-1637"></a>

<p align="center"><kbd><img src="assets/f13a23389951578dcb780b514f6f6cf23ef4413f.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng khi ổng bấm Soccer và submit thì nó ra lỗi
> 404 not found, và thấy url là **.../register.**
> D: Tại sao?
>
> A: Vì**app.py chưa define function cho "../register"**
> D: Correct

<br>

<a id="node-1638"></a>

<p align="center"><kbd><img src="assets/623969ed1d3ce4fb90ff71e40976c792fdeba7ea.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng vào app.py thêm cái **@app.route("/register")**Trong đó **render_template("success.html")**

<br>

<a id="node-1639"></a>

<p align="center"><kbd><img src="assets/80bfa68b2f9785fc0864106d4bca97176a4e5455.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/80bfa68b2f9785fc0864106d4bca97176a4e5455.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/cdc04d6beb2db1efd4786cba0a73e1bf193d2eb9.png" width="100%"></kbd></p>

> [!NOTE]
> Xong như đã biết, ổng tạo **layout.html** để **"nhúng" nhiều
> content khác nhau vào** tùy từng page để không phải copy
> paste nhiều đoạn code giống nhau. Từ đó **index.html và
> success.html chỉ cần extend từ layout.html**

<br>

<a id="node-1640"></a>

<p align="center"><kbd><img src="assets/dd44f68635193eca2c4d95c114e11e186434a0ac.png" width="100%"></kbd></p>

> [!NOTE]
> Và làm file **success.html** extend từ **layout.html**,
> tạm thời chỉ say 1 câu như này

<br>

<a id="node-1641"></a>

<p align="center"><kbd><img src="assets/88e3c602d04ff28cb9908e4590259ea4991ed04d.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng chọn soccer, và submit nó vẫn error, không phải
> 404 not found nữa mà là **405 not allowed**
>
> D: Why?
>
> D: là vì **chưa define method POST cho @app.route("
> /register")** nên nó chỉ đang mặc định với **GET**, mà**submit form
> dùng POST nên nó không cho phép**

<br>

<a id="node-1642"></a>

<p align="center"><kbd><img src="assets/33a3348ccebbac7d3282583a3a9c7aa05d4e6b9c.png" width="100%"></kbd></p>

> [!NOTE]
> Phải declare **methods=["POST"]** cho route `/register`

<br>

<a id="node-1643"></a>

<p align="center"><kbd><img src="assets/eeebce168330960b80950553808ad96a4c4c7e0c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/eeebce168330960b80950553808ad96a4c4c7e0c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/89221b5684d4f0c38c43b0a1709e9cf78da5f7cb.png" width="100%"></kbd></p>

> [!NOTE]
> Và kết quả là giờ
> nó đã work

<br>

<a id="node-1644"></a>

<p align="center"><kbd><img src="assets/c618765e96985ba780d976511d770122640cd7b8.png" width="100%"></kbd></p>

> [!NOTE]
> Xong, để thử **thật sự save registered data**,  thì ổng**tạo một cái dictionary registrants như vầy**.
>
> Và khi user  submit với route `.../register,` **lấy name và
> sport  từ request.form và bỏ vào dictionary:**

<br>

<a id="node-1645"></a>

<p align="center"><kbd><img src="assets/091b269497b6f55448bff56ef68c7196385a9405.png" width="100%"></kbd></p>

> [!NOTE]
> Tạo thêm một cái route:**/registrants**, response về cái 
> **registrants.html**với **registrants** data. Và again, dù 
> nhìn có vẻ stupid (**registrants=registrants**) nhưng đó
> là bình thường

<br>

<a id="node-1646"></a>

<p align="center"><kbd><img src="assets/f9507b6a6321225650e61311ad54c3ffbf25e412.png" width="100%"></kbd></p>

> [!NOTE]
> Xong đại khái là tạo cái file **registrants. html** extends từ
> layout.html
>
> Và syntax như vầy: Dùng **unordered** list và với **jinja**
> syntax, nó chính là **run một for loop Python trong các
> value của registrants**, và tạo các <li> tag có value

<br>

<a id="node-1647"></a>

<p align="center"><kbd><img src="assets/7cb8721cdbf02f2f2ef974564bbd41237a22a8e6.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng chạy thử thì nó bị lỗi thì ổng nói ta có thể xem lại
> cái log để track vấn đề

<br>

<a id="node-1648"></a>

<p align="center"><kbd><img src="assets/ccac4cbe9f0954bac58f7c9c2903f25284d2d9ed.png" width="100%"></kbd></p>

> [!NOTE]
> Thì vấn đề là ta đặt dictionary variable **registrants**
> trùng tên với function **registrants**()
>
> Giải pháp là **đổi lại dùng REGISTRANTS** cho
> dictionary

<br>

<a id="node-1649"></a>

<p align="center"><kbd><img src="assets/7c9da7a1ef3b8d29443a7f969a5c92ac85ec1e4e.png" width="100%"></kbd></p>

> [!NOTE]
> Và khi submit để registered hai cái tên, và manually access vào ..
> `/registrants` Ta thấy nó đã show hai cái tên trong dictionary

<br>

<a id="node-1650"></a>

<p align="center"><kbd><img src="assets/923f256b550ca68b4c6eefe431c8d6b18ebb5970.png" width="100%"></kbd></p>

> [!NOTE]
> Thử show thêm value với các
> name đó để ra sport

<br>

<a id="node-1651"></a>

<p align="center"><kbd><img src="assets/563df37093e19e24f4918ee3de7a2ae7660b6124.png" width="100%"></kbd></p>

<br>

<a id="node-1652"></a>

<p align="center"><kbd><img src="assets/ce45b128958a802a285d3e062521ef42929cdc67.png" width="100%"></kbd></p>

> [!NOTE]
> D: Thiếu cái gì? mà nó lại không show ra tên sport
>
> A: Thì **khi submit Register** thì nó**chỉ post cái name lên**, còn
> **chưa thấy chỗ nào gửi sport lên**
>
> D: Correct

<br>

<a id="node-1653"></a>

<p align="center"><kbd><img src="assets/3f527a897ad511069d03e4cc86dd641e6d872a2a.png" width="100%"></kbd></p>

> [!NOTE]
> Phải thêm **name="sport"** cho <select> tag
>
> thì khi submit nó sẽ gửi 2 argument là name và sport
> lên

<br>

<a id="node-1654"></a>

<p align="center"><kbd><img src="assets/b6b4ed0c19de9868eda019b1ec17e3e89b07376e.png" width="100%"></kbd></p>

> [!NOTE]
> Và nó đã work!

<br>

<a id="node-1655"></a>

<p align="center"><kbd><img src="assets/c5470f886725ebb32b752a2d63b4905c54cd2f5d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là giả sử **có kẻ muốn phá phách** muốn
> submit một cái sport không có trong líst ví dụ
> **volleyball**. Thì họ có thể **inspect, vào và change
> value của trong đó**. Và **submit**, thì **nó hoàn toàn có
> thể submit volleyball**

<br>

<a id="node-1656"></a>

<p align="center"><kbd><img src="assets/093352f19771f19bcdae3c4f22429ea7d87346f3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/093352f19771f19bcdae3c4f22429ea7d87346f3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a3bbd2c1c5c9bbdaca28946f267cfd6d148e8a59.png" width="100%"></kbd></p>

<br>

<a id="node-1657"></a>

<p align="center"><kbd><img src="assets/cdb121f02c8fa7ed389370f2a545240ff4bf203f.png" width="100%"></kbd></p>

> [!NOTE]
> Và đây là cái nguy hiểm, vì giả sử ta làm một cái
> shopping web page và **user có thể change cái giá
> và submit**. Thì ta **phải có cơ chế check xem đó có
> phải là valid submit** không

<br>

<a id="node-1658"></a>

<p align="center"><kbd><img src="assets/2a3c83ba79a06f9a4591c81afc1f64ac1464c5d7.png" width="100%"></kbd></p>

> [!NOTE]
> Để sửa vấn đề này, ổng **define các valid
> sport**và**truyền nó vào index.html**

<br>

<a id="node-1659"></a>

<p align="center"><kbd><img src="assets/5ed111b4594338e1244891a2c3990e999137a578.png" width="100%"></kbd></p>

> [!NOTE]
> Sửa lại index.html, **không hardcode các
> option** nữa mà**lấy từ value trong sports đưa vào nhờ
> jinja syntax** như hồi nãy
>
> {% for sport in **sports** %}
>    ...
> {% endfor %}

<br>

<a id="node-1660"></a>

<p align="center"><kbd><img src="assets/298b10b8d64e2e4f10acf24783852259069afbd8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/298b10b8d64e2e4f10acf24783852259069afbd8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8e9bf065d8399556a2c9f534d398201b122d28cc.png" width="100%"></kbd></p>

> [!NOTE]
> Và **thêm checking việc name không trống** và
> **sport có trong SPORTS** thì **mới return
> success**

<br>

<a id="node-1661"></a>

<p align="center"><kbd><img src="assets/f445f6fed94d197197c927717d2c8c49b5d6509f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f445f6fed94d197197c927717d2c8c49b5d6509f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4b3e519f062f678af98cc925d52093172fbfe145.png" width="100%"></kbd></p>

> [!NOTE]
> Nói thêm về một**attribute required vào input**.
> Thì đại khái là **khi user không nhập tên thì browser sẽ báo**

<br>

<a id="node-1662"></a>

<p align="center"><kbd><img src="assets/054e8e1c33f1bfde3786a8eaad3fa7ae152dad10.png" width="100%"></kbd></p>

> [!NOTE]
> Tuy nhiên ổng nói **người ta vẫn có thể inspect vào cái
> http**, **xóa đi cái required attribute** đi và**vẫn sẽ submit
> được**, nhưng nếu ta **có cơ chế để ngăn chặn** thì nó sẽ
> vẫn không qua được cái check của ta.

<br>

<a id="node-1663"></a>

<p align="center"><kbd><img src="assets/4756961634330248d2ee5eaaab9e90fbc851a100.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó ta **phải có server's side
> validation**

<br>

<a id="node-1664"></a>

<p align="center"><kbd><img src="assets/b4ab8edd807c2d041cf635d1b5c89b12fee7a2cc.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái có người hỏi là **liệu người ta có thể access
> file app.py được không**
>
> D: Trên **lý thuyết là không**, tuy nhiên khi code ta
> **sẽ tránh để username, password trong code** mà để
> trong **variable**,**save vào trong memory** để tránh
> trường hợp nào đó người ta vào code được

<br>

<a id="node-1665"></a>

<p align="center"><kbd><img src="assets/7a3eee0f3341846a7ab5958888b8febe755f08d4.png" width="100%"></kbd></p>

> [!NOTE]
> Tại sao**save data vào global variable lại không
> phải là ý hay?**
>
> A: Vì đơn giản là**khi tắt chương trình thì nó sẽ mất**D: Correct

<br>

<a id="node-1666"></a>

<p align="center"><kbd><img src="assets/a3ab8ea424b5c431e52e4dca1692282bad0616b0.png" width="100%"></kbd></p>

> [!NOTE]
> D: Correct. Do đó ta **phải save data**, có thể vào **csv file** như 
> bữa trước, nhưng giờ ta đã có một công cụ mạnh hơn là **SQL**
>
> Ổng mới **mở cái file** (cũng vậy chỉ là **add thêm import SQL 
> từ cs50.**
>
> Dòng **db `=` SQL("sqlite:///froshims.db")**: kiểu như
> ổng **đã tạo file db này rồi**, giờ sẽ dùng nó, như đã biết tuần 
> trước

<br>

<a id="node-1667"></a>

<p align="center"><kbd><img src="assets/2df97bf0e1c431b1ed70d40181a72bdbeafbcf13.png" width="100%"></kbd></p>

> [!NOTE]
> Còn ở dưới cái api register:
>
> Sau khi validate entered info. 
>
> dòng **db.execute("INSERT INTO registrants (name, sport) VALUE(?,?)", name, sport)**
> Chính là để **gọi SQL function từ python**, **insert hai value name và sport vào hai
> column**. Chú ý là dùng **? (Place holder)** thay vì concatenate để tránh tình trạng
> bị hack như bữa trước có nói
>
> Cuối cùng cái dòng **redirect("/registrants")** chính là **redirect đến cái url `/registrants` 
> để xem saved data**

<br>

<a id="node-1668"></a>

<p align="center"><kbd><img src="assets/988c6881417685a53d995a50046f864851729f4b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/de69fce60c83f2150ffaa3279a6b5d6b6c5e14e8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/988c6881417685a53d995a50046f864851729f4b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/de69fce60c83f2150ffaa3279a6b5d6b6c5e14e8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c844991395b4edb7200b939ddd91364feacf4707.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **check thử (dùng .schema như đã biết) cái db
> này**, **có 3 column id, name, sport**. hiện giờ chưa có gì

<br>

<a id="node-1669"></a>

<p align="center"><kbd><img src="assets/625656bfe2613f6e8c297a3e5e4f6d0998eb9b01.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/625656bfe2613f6e8c297a3e5e4f6d0998eb9b01.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b569b69be63ed835e15565d26619a36f0a427ee6.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng run **flask run** để chạy cái server. Và với phiên bản
> **froshims4** thì có cải tiến chút là **thay vì dùng menu thì dùng 
> radio button.**

<br>

<a id="node-1670"></a>

<p align="center"><kbd><img src="assets/d8791d03671d6cfbbc771a741b8f5d7dd79dfd0f.png" width="100%"></kbd></p>

> [!NOTE]
> Nhập tên và bấm **submit** thì nó show như thế này:
>
> Đó là nó đã ở url: **.../registrants** và đã show thông tin
> David, Soccer

<br>

<a id="node-1671"></a>

<p align="center"><kbd><img src="assets/dddd6c2d99b5360185d948e14f8840ec158a8b10.png" width="100%"></kbd></p>

> [!NOTE]
> Và **check thử trong db thì thấy nó đã có**, có nghĩa
> là có **tắt server mở lại thì vẫn còn data**

<br>

<a id="node-1672"></a>

<p align="center"><kbd><img src="assets/c7712cd85c778f37c459b7d4b43aea93663551e4.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng show cái code của **index.html** bây giờ  (với
> radio button thay cho selected menu)
>
> Thì cũng tương tự không có gì, khi dùng **jinja** để chạy
> cái **python code loop trong các sports** để **add các
> input có type là "radio" để nó dạng radio button**
>
> **Nói thêm name="sport"** thì ổng nói để khi **chọn cái
> này thì nó unselect cái kia.**

<br>

<a id="node-1673"></a>

<p align="center"><kbd><img src="assets/96a2a681fc5ea6d82152d39ae205ffe86ed8bdaf.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng show code của **registrants.html**
> Có **table** **tag**, cột **Name**, **Sport**, và **một cột
> để trống** **để cho cái button Deregister**

<br>

<a id="node-1674"></a>

<p align="center"><kbd><img src="assets/a37effd069adb608812b85f435fc8281c6401179.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a37effd069adb608812b85f435fc8281c6401179.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/51aad6be4c39469f8460e1a5e45fb028329e8185.png" width="100%"></kbd></p>

> [!NOTE]
> Trong body cũng là **jinja task** loop trong **registrants** 
> (được truyền vào) và **tạo 3 cái <td> tag**

<br>

<a id="node-1675"></a>

<p align="center"><kbd><img src="assets/88bd2dba64258e85dfef7312274040f23bf930a3.png" width="100%"></kbd></p>

> [!NOTE]
> Coi cái route `"/registrants"` thì thấy ổng lấy registrants bằng
> cách gọi lệnh **sql: db.execute("SELECT * FROM registrants")**
> và **truyền vào registrants.html**

<br>

<a id="node-1676"></a>

<p align="center"><kbd><img src="assets/a9082ff75b8bed3e11e6a07fb188819b6050798e.png" width="100%"></kbd></p>

<br>

<a id="node-1677"></a>

<p align="center"><kbd><img src="assets/d8544d9273912db843767aa899a2c9d7f6b78bb1.png" width="100%"></kbd></p>

> [!NOTE]
> Xong để xem cái **Deregister** làm gì, ổng cho ta **coi cái
> Inspect code trước**, (tí mới nói cách làm), đó là nó có 
> cái dạng là cái **form**, với input với **name="id"**, value, 
> **type `=` "hidden"** `->` nó sẽ hidden, không show ra, vậy
> thôi.
>
> Và khi submit, nó sẽ POST cái id có value như vậy lên 
> **url: ..../deregister**

<br>

<a id="node-1678"></a>

<p align="center"><kbd><img src="assets/4f2251373948063228d0f2f4c81877a4adca511c.png" width="100%"></kbd></p>

> [!NOTE]
> Xem cái app.py, của r**oute "/deregister"** cho thấy nó 
> nhận phương thức **POST**, 
>
> và với **id** (lấy từ**request.form.get("id")**)
>
> nó **check id**có khác trống không, trước khi **gọi lệnh sql
> để delete row nào có id bằng như vậy.**
>
> Và cuối cùng là **redirect tới .../registrants**

<br>

<a id="node-1679"></a>

<p align="center"><kbd><img src="assets/e033c1db2c699e559eeb92af7307dc0694b39d75.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng hỏi **có gì không an toàn ở đây?**
>
> Đại khái là**họ có thể inspect, và change value
> của hidden input và xóa data**

<br>

<a id="node-1680"></a>

<p align="center"><kbd><img src="assets/aecdcbc151dce81df8aae55ed18363f70a9ef5b5.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói **cần phải có tính năng log in** để **chỉ cho
> phép một số action** dành cho người**đã log in ví dụ như "
> delete"**
>
> Thì nói sơ qua về **cookies**, là cách mà khi ta**log in vào
> google**, web browser sẽ dùng cookie kiểu như khi vào rạp
> chiếu phim, sau khi bảo vệ **đã check id `card/` Check vé
> vào cửa** họ sẽ **đóng một con dấu** để khi **ta ra rồi vào
> lại vào chỉ cần chìa con dấu ra thay vì phải check id card
> lại**

<br>

<a id="node-1681"></a>

<p align="center"><kbd><img src="assets/eda72a36bb0f9ce21423df134e975502450942b3.png" width="100%"></kbd></p>

<br>

<a id="node-1682"></a>

<p align="center"><kbd><img src="assets/87995355504506e0f599398cbfe7551b6b25f343.png" width="100%"></kbd></p>

> [!NOTE]
> Lấy ví dụ gmail, thì **khi ta đã log in thành công**, nó sẽ trả
> về **200 OK**, nhưng bên cạnh đó sẽ còn có cái **header**
> tên là **set-cookie**, với **key `-` value là session=value**.
>
> Thì đại khái đây **chính là tương đương việc bảo vệ đóng
> dấu cho ta**

<br>

<a id="node-1683"></a>

<p align="center"><kbd><img src="assets/a55fe74079659d5bb58d0064d5ea06497ea08ea5.png" width="100%"></kbd></p>

> [!NOTE]
> Và khi máy tính, hay ta "vào lại" thì ta **gửi cho server cái
> envelope như này** trong đó **có chứa cookie: session=value.**
> **Gmail nó sẽ  dựa vào đó mà "cho ta vào"**, cũng như **phân
> biệt ta là ai** mà show gmail cho đúng. Nôm na là vậy

<br>

<a id="node-1684"></a>

<p align="center"><kbd><img src="assets/7af855ea4e66f2a072caa88745a319fba350b8c4.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng mở một version khác (cái project nãy giờ đang làm
> nhưng ổng làm trước nhiều version) thì version này bắt
> đầu có session
>
> Thì ổng nói **Flask nó sẽ handle mọi thứ**: **set cookie**,
> **check cookie**. Và nó có cái **session**: kiểu như cái
> **dictionary**, trong đó khi ta **set `key-value` vào trong đó** thì
> **nó vẫn còn y nguyên miễn là cùng một user.**
>
> Và **Flash nó sẽ đảm bảo là khi David visit website**, thì nó
> sẽ **dùng cái session của David**. Còn khi **Carter visit website
> thì nó sẽ là cái session của Carter.**

<br>

<a id="node-1685"></a>

<p align="center"><kbd><img src="assets/013140b9a5ffaf6643d94665073da6f59f42649c.png" width="100%"></kbd></p>

> [!NOTE]
> Đoạn code này đại khái là
> các để **initialize session**

<br>

<a id="node-1686"></a>

<p align="center"><kbd><img src="assets/a19f262a795c58dff955a5de4b3f521100f0b544.png" width="100%"></kbd></p>

<br>

<a id="node-1687"></a>

<p align="center"><kbd><img src="assets/8a18e2cf5ca90aa3ad763b1c1f8930550666f9de.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8a18e2cf5ca90aa3ad763b1c1f8930550666f9de.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1f33f50b6c1878ad2e3bdb97b797348dd8bb59de.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **tính năng log `in/log` out
> dù không có password**

<br>

<a id="node-1688"></a>

<p align="center"><kbd><img src="assets/9df9c97f0ec202806128ca1eabb1f657e8e46564.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9df9c97f0ec202806128ca1eabb1f657e8e46564.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/487b26deba313054ca13b0bda565d8147b3f45d1.png" width="100%"></kbd></p>

> [!NOTE]
> Xem**route `("/")` index** nó làm gì: Nó sẽ **check trong
> session có cái key nào là "name"** hay không,
>
> Nếu **không có thì redirect về /login,** **có thì cho vào
> index.html.**

> [!NOTE]
> Xem html của **index.html**. Thì cơ bản chỉ là**jinja syntax
> chạy python code** trong đó **check session["name"]** có
> value hay không.
>
> Nếu **có thì show là đã log in** với **tên**, và có **button logout** `-`
> chỉ là cái <a> tag  với link.

<br>

<a id="node-1689"></a>

<p align="center"><kbd><img src="assets/78c71c3c98a31e21172753f3f724b22948db97c9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/78c71c3c98a31e21172753f3f724b22948db97c9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2cc3d5496d8670cc1425c793d581449e86bfb427.png" width="100%"></kbd></p>

> [!NOTE]
> Xem html của **login** chỉ là cái **form**, khi **submit thì nó POST
> cái name lên.**
>
> Và trong route "**/login**", nó**lấy cái tên từ trong request pos**t
> lên, **bỏ vào session với key là name**

<br>

<a id="node-1690"></a>

<p align="center"><kbd><img src="assets/fbe1f83a2c8166c4aa3563b2c3d1b59d1fd122cf.png" width="100%"></kbd></p>

> [!NOTE]
> Còn **/logout** thì **xóa cái value của key name đi.**
> Thì ta hiểu là **khi David visit cái url đó**, **Flask sẽ trả về cho 
> máy tính của ổng một cái cookie có tên của David**.
>
> Khi **Carter visit cái url đó**,**Flask sẽ trả về cho máy tính của
> của ổng một cái cookie có tên Carter.**

<br>

<a id="node-1691"></a>

<p align="center"><kbd><img src="assets/f5f1678ad86c70a28fcf47f334ab560877c68057.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng mở cái file

<br>

<a id="node-1692"></a>

<p align="center"><kbd><img src="assets/99cbb296cc8f16fd6fd8558d353cf4c420e78291.png" width="100%"></kbd></p>

> [!NOTE]
> Thì khi inspect nó ta thấy nó có các **h2 tag**,
> form có action **POST** tới user "**/cart**". 
>
> input tag **hidden** có **name="id"** **value `=` 1,2,3...**tức khi submit, nó sẽ **POST** lên với **id** có **value `=` 1,2,3**
>
> Thì ổng nói trong trường hợp này thì**không sợ hack**,
> vì t**ệ nhất là nó inspect vào và sửa lại cái id của book** thôi
> và dẫn đến là nó add những cuốn sách khác vào thôi
> nên không có gì phải sợ cả

<br>

<a id="node-1693"></a>

<p align="center"><kbd><img src="assets/8de0271cd2b021dc84e427e51666798e2b511bb8.png" width="100%"></kbd></p>

> [!NOTE]
> XOng ổng mở app.py ra. Thì khúc đầu cơ bản là không có gì
> mới với các lib SQL từ **cs50, Flask, redirect, `render_template,` 
> request,  session.**
>
> có db mở từ **store.db**
>
> và **3 dòng 12,13,14 là initialize cái session**

<br>

<a id="node-1694"></a>

<p align="center"><kbd><img src="assets/a2ebf85c757550e5982e9cb509ffb674e59b8304.png" width="100%"></kbd></p>

> [!NOTE]
> Với default path `"/"` show các cuốn sách thì đơn giản là
> **Query từ SQL**, rồi **truyền vào books.html**

<br>

<a id="node-1695"></a>

<p align="center"><kbd><img src="assets/ff66cef2445dcc64d59bc67cd75a96450c7bafb1.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, xem qua **index.html**, ta thấy cũng không có gì, nó extend 
> từ layout.html cho gọn.
>
> Rồi nó dùng **jaja syntax** để run Python code, **loop trong
> các books được truyền vào** để add các**h2 `+` form**
>
> Trong **form** tag có **hidden tag input**, **name="id"**, và **value
> lấy từ book['id']**
>
> Và submit thì nó**POST cái id value là lấy từ book[id] lên, 
> route "/cart"**

<br>

<a id="node-1696"></a>

<p align="center"><kbd><img src="assets/b05681b626a8d588fc0e0b568395e79ee36be4a8.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi qua xem cái **route "/cart"**
>
> nó accept cả hai method **GET và POST**.
>
> Thì đầu tiên nó **check trong session có (cái key) "cart"**
> **hay chưa** nếu chưa thì**tạo một cái mang value là empty list**
>
> Xong nếu là **POST**, nó **lấy id truyền lên** (từ request.form.get("id"))
> và **check nếu id not empty thì nó bỏ vào cái cart list** trong session
> **session["cart"].append(id)**
>
> Và **return và redirect tới /cart,** (cái việc redirect tới cart này nó sẽ
> "dùng" default value là GET)
>
> Và ở dưới chính là **handle khi GET**, nó thực hiện SQL query
> **db.query(SELECT * FROM books WHERE id IN (?)", session["cart"])**
> nhớ lại (?) chính là SQL placeholder, nó sẽ **truyền các id trong list
> session["cart"]**vào và từ đó **kết quả của sql query return là list
> các books có id như vậy.**
>
> Cuối cùng nó **render_template** và**truyền books vào và cart.html**

<br>

<a id="node-1697"></a>

<p align="center"><kbd><img src="assets/664f96d6bdda40824d3b3f3bd74cb12e4e15f17b.png" width="100%"></kbd></p>

> [!NOTE]
> Và ổng làm thử, add hai cuốn sách vào cart.
>
> Và khi reload thì nó luôn có hai cuốn này.
>
> Ổng nói như hồi nãy đã nói đó là khi tui (David) visit
> page thì  Flask sẽ đảm bảo session của tui có hai cuốn
> sách này, và khi carter visit thì session của Carter sẽ có
> các cuốn của Carter

<br>

<a id="node-1698"></a>

<p align="center"><kbd><img src="assets/bad614dd361d7fc675db542e20c70bbb0607b521.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là mỗi người sẽ (được đóng dấu) trả cho một cookies 
> khác nhau, nên **không thể có session giống nhau được**
> Và mỗi khi server **trả cookies về hoặc browser chìa cookies
> ra**(như hành chìa cái tay đã đóng dấu ra cho ông bảo vệ)
> thì nó **đều được encrypted**

<br>

<a id="node-1699"></a>

<p align="center"><kbd><img src="assets/3bb45c620de11764fdc708d6bc3071e4e8bca067.png" width="100%"></kbd></p>

> [!NOTE]
> Q: khi nào bao lâu thì **session expired?**
>
> D: Do **configured**. Với bank web server thì có thể sẽ cho expire
> ngay khi bạn close the tab
>
> Nhưng với email có thể cả tháng

<br>

<a id="node-1700"></a>

<p align="center"><kbd><img src="assets/0229e5f3e62d37557e46c6332d0fc9d996525de7.png" width="100%"></kbd></p>

> [!NOTE]
> Và nên dùng inconito mode là
> để khi close là nó clear mọi
> cookies giùm mình

<br>

<a id="node-1701"></a>

<p align="center"><kbd><img src="assets/6b76337f915f5a10ae8d93454d4a5a0fecf0e7e3.png" width="100%"></kbd></p>

> [!NOTE]
> Cuối cùng sẽ nói qua API, thì ổng nói về cơ bản
> tất cả những lệnh ta gọi để tương tác với C,
> SQL web server đều là API

<br>

<a id="node-1702"></a>

<p align="center"><kbd><img src="assets/d8ff603a1dd3d8429e552e14cda576a355da1450.png" width="100%"></kbd></p>

<br>

<a id="node-1703"></a>

<p align="center"><kbd><img src="assets/077f18d8277e209e39b7add7f7cf551e206884a1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/077f18d8277e209e39b7add7f7cf551e206884a1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0a41fba7622023798b87618371ddb52e726831eb.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng làm thử cái example này, gõ office, bấm
> search nó cho ra kết quả list các bộ film này.
>
> Url: `.../search?q=office`

<br>

<a id="node-1704"></a>

<p align="center"><kbd><img src="assets/12122cf1d49c8cff909e8342170df6937fa13087.png" width="100%"></kbd></p>

<br>

<a id="node-1705"></a>

<p align="center"><kbd><img src="assets/47772aef60c89af31eca4b6be7b4d536351f8fbf.png" width="100%"></kbd></p>

> [!NOTE]
> Xem qua route `"/search"` thì cơ bản là gọi sql query:
>
> ("SELECT * FROM shows WHERE title LIKE ?", "%" request.args.get("q") `+` "%")
>
> nhớ lại SQL thì SELECT * FROM shows WHERE title LIKE %abc% tức là tìm hết
> các row (và lấy hết các cột) từ table shows sao cho title chứa "abc" trong đó.
>
> Và **render_template search.html** và **truyền shows vào**

<br>

<a id="node-1706"></a>

<p align="center"><kbd><img src="assets/1afe7b0ad3fa7d30c6e50552fb510ab56d0cb5c0.png" width="100%"></kbd></p>

> [!NOTE]
> Và cái search.html cũng đơn giản: extend từ layout.html,
> Dùng jinja để chạy Python loop, loop trong shows (được
> truyền vào) và tạo các <li> tag với text là **show["title"]**.

<br>

<a id="node-1707"></a>

<p align="center"><kbd><img src="assets/f4e1047e95c4619a3caa1016e85312b6cb754dd0.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói chưa có API gì ở đây hết, chỉ là basic
> HTTP, submit the form và **đến another route** và**xem
> kết quả**. Ta sẽ xem một ví dụ khác

<br>

<a id="node-1708"></a>

<p align="center"><kbd><img src="assets/ed2f20745f6edf6e0f2e58589ad79686d2ec1dcd.png" width="100%"></kbd></p>

> [!NOTE]
> Thì với ví dụ này ta không thấy button submit nữa.
> Thì cơ bản ổng nói ta**dùng AJAX** nôm na là dùng
> **javascript** để **listen event**, và khi **user gõ thì nó thực
> hiện hành động query** và trả về kết quả

<br>

<a id="node-1709"></a>

<p align="center"><kbd><img src="assets/feb4ab4796cc73e375b40501bb0e852ce8bcbf02.png" width="100%"></kbd></p>

<br>

<a id="node-1710"></a>

<p align="center"><kbd><img src="assets/24480acebaebd4d5f69f8e9feb35e4b4192e2bd6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/24480acebaebd4d5f69f8e9feb35e4b4192e2bd6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/396c803bbfe534cd2614f4ee897cde429c9672a4.png" width="100%"></kbd></p>

> [!NOTE]
> thì khi ổng gõ là nó search và hiện kết quả. Ta sẽ
> xem ổng làm như thế nào

<br>

<a id="node-1711"></a>

<p align="center"><kbd><img src="assets/dad3b15c904ffd00f7fc4993e9757e47e5834e2c.png" width="100%"></kbd></p>

> [!NOTE]
> Xem cái route**/search** thì thấy nó cơ bản vẫn như hồi nãy, đó
> là nếu **q `=` request.args.get("q")** có value thì gọi **sql query** như
> này tìm các rows có title như vậy, và lần này **giới hạn 50 cái**
> thôi
>
> Còn không thì không show gì với việc cho shows `=` empty list
>
> Vẫn **render_template** và**truyền shows vào**

<br>

<a id="node-1712"></a>

<p align="center"><kbd><img src="assets/b0aa23d1044216808df609835207c627f70eb60d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b0aa23d1044216808df609835207c627f70eb60d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/db3d40cb4eb7b768db719b97cb27b13d310c1908.png" width="100%"></kbd></p>

> [!NOTE]
> Xem thử cái **search.html** thì thấy lần này nó **không extend layout.**
> html nữa. Thì cơ bản ổng nói là để **giới thiệu khái niệm API**, đó là ví
> dụ khi gọi api ..**./search?q="Office"**nó sẽ không trả cho bạn html mà
> **chỉ là data thôi và bạn sẽ tự display**

<br>

<a id="node-1713"></a>

<p align="center"><kbd><img src="assets/86b7d0dcf5369de06245fb8d1b01d767f460e217.png" width="100%"></kbd></p>

<br>

<a id="node-1714"></a>

<p align="center"><kbd><img src="assets/872790e4fadb4e735bf0e57f0a10a52f7b3801ba.png" width="100%"></kbd></p>

> [!NOTE]
> Giải thích cái javascript: 
>
> Đầu tiên là lấy cái **<input>:**
> let input `=` **document.querySelector('input')**;
>
> Sau đó **add event listener** cho nó với event '**input**'
> và khi **event xảy ra thì gọi function async (tức là chạy background)**
> Trong đó: 
>
> Thực hiện việc**await fetch `('/search?q='` `+` input.value)**: fetch (gọi và lấy
> data từ url **/search** với **q `=` input.value**, 
> như hồi nãy đã biết nó **trả về các bộ phim** (có title chứa q's value) mỗi 
> cái một **<li> tag.**
>
> **Await** ý là **chờ cho khi nó trả về** thì **mới lấy ra (response.text()**) và 
> S**et nó vào innerHTML của 'ul'**

<br>

<a id="node-1715"></a>

<p align="center"><kbd><img src="assets/490a038e8eea72b7fc6d6d8a79ab25db8a5acb27.png" width="100%"></kbd></p>

> [!NOTE]
> Qua index.html thì thấy nó có cái **<input> tag** thì biết
> rồi, **nhưng dưới là cái <ul> để trống** để khi **search
> nó nhét cái kết quả vào đó**

<br>

<a id="node-1716"></a>

<p align="center"><kbd><img src="assets/01e158478f08201af6c33efd882b84ee27c7daee.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói cái API ..**/search?q=**.. nó **trả về list các <li> tag** như
> này thì **không phải lúc nào tui cũng cần html** do đó **đặt ra vấn đề
> là làm sao đó để nó trả về 1 dạng chung chung**

<br>

<a id="node-1717"></a>

<p align="center"><kbd><img src="assets/35cbd23dac90102f8ccdee2392c20d054f8a62a3.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đó chính là JSON

<br>

<a id="node-1718"></a>

<p align="center"><kbd><img src="assets/8b840cfb66eda59079b227d2930aaed0407956ac.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng mở cái version cuối
> cùng của cái web app này

<br>

<a id="node-1719"></a>

<p align="center"><kbd><img src="assets/24e404e4c1a50294626507ac92085e8b3a05a779.png" width="100%"></kbd></p>

> [!NOTE]
> Thì nó có dạng là **1 list** (vì start và end với **square bracket []**)
> các **dictionary {}**

<br>

<a id="node-1720"></a>

<p align="center"><kbd><img src="assets/9ad9bf77270b95f43ecb6596a388079d473a41e2.png" width="100%"></kbd></p>

<br>

<a id="node-1721"></a>

<p align="center"><kbd><img src="assets/7e0aaede521df4dcf2594a65a854f037b2290b17.png" width="100%"></kbd></p>

> [!NOTE]
> thì trong cái script thì **chỉ khác ở chỗ** cái data trả về sẽ
> được **biến thành json()** thay vì**text()**:
>
> let show `=` await **response.json**() thay vì **response.text**()
>
> và với json data đó. 
>
> Ổng loop trong đó (như đã nói nó là list các dictionary)
> nên hiểu rằng id trong for (let id in shows) thì id chỉ như
> index 0, 1, 2...
>
> Với mỗi id, mới **lấy cái dictionary ra**, **show[id]** và**access
> key "title" của nó.**
>
> Có thêm hai dòng replace...cơ bản là để .**..replace mấy
> cái kí tự có thể khiến html bị lỗi** (cái này bên SM series làm quài)
>
> Cuối cùng là **nhét nó vào giữa hai <li> `</li>` tag** và**concat với html.**
>
> Kết qua là **set cái html vào innerHTML của <ul>**

<br>

<a id="node-1722"></a>

<p align="center"><kbd><img src="assets/e09bfd2e87ac08189993990e5af978b43cf5dec8.png" width="100%"></kbd></p>

> [!NOTE]
> Và ổng nói tới đây ta đã được trang bị đủ đồ
> chơi để build một cái full web application rồi

<br>

