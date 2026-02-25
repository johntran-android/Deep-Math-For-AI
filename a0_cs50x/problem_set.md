# Problem Set

📊 **Progress:** `13` Notes | `64` Screenshots

---
<a id="node-1735"></a>

<p align="center"><kbd><img src="assets/eb4a0f6fbd3dc3258b548de2446b47fe8dde2976.png" width="100%"></kbd></p>

<br>

<a id="node-1736"></a>

<p align="center"><kbd><img src="assets/e3e7e607d21136329e11585fafc7ec2a2a554114.png" width="100%"></kbd></p>

<br>

<a id="node-1737"></a>

<p align="center"><kbd><img src="assets/fbfa599704ce4b6177c491ee6287f30858dd82d6.png" width="100%"></kbd></p>

<br>

<a id="node-1738"></a>

<p align="center"><kbd><img src="assets/ac485d4677bca0424618527ef201e86ba101322a.png" width="100%"></kbd></p>

<br>

<a id="node-1739"></a>

<p align="center"><kbd><img src="assets/2e7d19b32f98732e4a256e61acf7b8962b990404.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2e7d19b32f98732e4a256e61acf7b8962b990404.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d66b64004fe49f18fb8227beddbd1f6f619866b9.png" width="100%"></kbd></p>

> [!NOTE]
> Table **user** có 4 cột: id, username, hash,
> cash. Chưa có row nào cả

<br>

<a id="node-1740"></a>

<p align="center"><kbd><img src="assets/665351fd931b751b1028956e07906fb47ee1825d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/665351fd931b751b1028956e07906fb47ee1825d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9c22b564cdbd3efef3360e3aac49ef1b63531d39.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là khúc đầu file **app.py**có những cái sau đây:
>
> Import các thứ, trong đó có CS50's **SQL**.
>
> rồi **Flask, redirect, render_templat, request, session** từ **flask** đã biết
>
> rồi **Session** từ **flask_session**
>
> Sau đó là configure Flask : **app = Flask(__name__)**
> Họ nói là ở đây**disable cái caching của response**, có thể là dòng này: 
> **app.config["SESSION_PERMANENT"] = False**, nôm na hiểu là để
> khi ta thay đổi gì đó mà browser không notice. Tạm hiểu vậy.
>
> Kế đến là **configure Jinja với function filters** để giúp **format value as US 
> dollars dễ hơn**.
>
> Rồi tiếp nó **configure Flask để store sessions trên local filesystem**
> **thay vì cookies** (vốn là default).
>
> Cuối cùng là nó **configure SQL module dùng finance.db**

<br>

<a id="node-1741"></a>

<p align="center"><kbd><img src="assets/88e638a59cbe299fbf383bca9ffdd331e284d09d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e28bf5084315924635d8f86dc2275a2322c4607f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/88e638a59cbe299fbf383bca9ffdd331e284d09d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e28bf5084315924635d8f86dc2275a2322c4607f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6a4f181c974dd3049caf866fa3070a0d9afbafe8.png" width="100%"></kbd></p>

> [!NOTE]
> Function route "/login" này làm gì?
>
> Đầu tiên nó **clear session**. Như ta biết session là cookies là một cái dictionary.
>
> Nếu là POST, nó sẽ **xem request có gửi lên username** và **password** không
> (vì là POST nên check trong **request.form** thay vì request.get 
> dành cho GET). 
>
> Nếu **có thì đi tiếp không thì gọi function apology()** - Xem trong helper thì nó 
> cơ bản là **render_template** cái html file **apology.html** truyền vào message.
>
> Sau đó nó **gọi sql query** để **lấy mọi row** mà có **username** **bằng username
> gửi lên.**
>
> Rồi **check tiếp xem có row nào không** và nếu có ít nhất một row thì lấy ra
> (row[0]). Rồi **lấy giá trị của cột hash** cùng với **password gửi lên** bỏ vào
> function **check_password_hash**() là function kiểu như **dịch password sang
> hash number** và **so sánh với nhau.**
>
> Nếu ok tức là có một user trở lên và password giống thì đi tiếp, tới đây nó sẽ
> Thực hiện việc**đóng dấu = set key "user_id" bằng id của user vào session.**
>
> Và **redirect tới default route "../"**

<br>

<a id="node-1742"></a>

<p align="center"><kbd><img src="assets/134c988995406f9e10de8ab88184dcbf3f44f1a2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/134c988995406f9e10de8ab88184dcbf3f44f1a2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f1346b5b4ba60483ea93fb791a02d1f47b14d043.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là khi user visit các url khác (các route khác) thì
> cái **decorator @login_required** của các "route
> function" đó sẽ gọi function login_required() này. Trong
> đó, nó sẽ check xem user login hay chưa biểu hiện là
> trong session có key " user_id" hay không, vốn được set
> khi user login thành công. Việc này cũng y như hình
> tượng khi ta vào bảo tàng, ông bảo vệ soát vé xong thì
> ổng đóng dấu vào tay ta, hoặc đeo một cái vòng vào tay
> ta thể hiện ta đã có vé rồi. Thì giả sử có đi ra mua nước
> và vào lại thì thay vì phải chìa cái vé ra lại thì ổng chỉ cần
> thấy cái dấu đóng là ổng cho vô. Thì hành động set "
> user_id" vào session chính là hành động đóng dấu đó.
> Và việc check "user_id" ở đây chính là việc xem user có
> đóng dấu hay chưa.

<br>

<a id="node-1743"></a>

<p align="center"><kbd><img src="assets/443f35fa724a5554a3a847814724755aada4fe84.png" width="100%"></kbd></p>

> [!NOTE]
> Logout đơn giản là**clear session** đi, từ đó khi**user có
> quay lại, thì không còn con dấu trên tay nữa** (**không
> còn key user-id trong session nữa**)  thì **phải chìa vé ra
> lại.**
>
> Tới đây nhắc lại là ổng nói **Session của Flask sẽ đảm
> bảo là khi user log in thành công**, **nó sẽ đóng dấu,** và
> tương đương **trả về cookie của user's browser có cái
> user-id,** để **khi user quay lại = web browser gửi cookie
> lên thì nó sẽ có cái user-id trong session**

<br>

<a id="node-1744"></a>

<p align="center"><kbd><img src="assets/88e638a59cbe299fbf383bca9ffdd331e284d09d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/88e638a59cbe299fbf383bca9ffdd331e284d09d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/52c60c968de7aca20f89a8275e8adb6074127f61.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là trong function **apology có define và dùng
> một function escape.** Đơn giản là để mình nó xài thôi.
> Vụ này trong java không có.
>
> Kế tới function login_required mới giải thích rồi, ở đây
> họ nói thêm đây chính là một **minh họa cho việc function
> lại return một function** trong python (nó define và return 
> function **decorated_function** ()

<br>

<a id="node-1745"></a>

<p align="center"><kbd><img src="assets/6e129be718f40753d69ff9104b8173a9e2f07fe2.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về function loop up, đại khái là nó giúp **gọi API của 
> Yahoo Finance** **gửi lên mã stock để lấy về thông tin** tên
> công ty, giá và kí hiệu. Họ cũng không nói kĩ hơn
>
> Nhưng ta thấy nó start với việc **chuẩn bị url với các argument**
> có thể là theo Yahoo API 's definition.
>
> Sau đó nó **request.get() để gọi api** với **url, cookies, headers,**
>
> Khi **nhận kết quả thì nó parse (decode) từ response content
> ra, để lấy ra price**. Rồi cuối cùng **tạo một cái dict có 3 key** là
> **name, price, symbol trả về**

<br>

<a id="node-1746"></a>

<p align="center"><kbd><img src="assets/cce802d4275c5b416dbded7e831847fa7377a110.png" width="100%"></kbd></p>

> [!NOTE]
> Cái helper's function cuối cùng là usd() chỉ đơn giản
> là format cái value thành dạng float có 2 số thập
> phân, chia 3 số bởi dấu phẩy và có kí hiệu $ ở đầu
>
> Ví dụ 1234.56 thì nó thành $1,234.56

<br>

<a id="node-1747"></a>

<p align="center"><kbd><img src="assets/e87f6c22a3763c33043689b8a4f39fc0aa5a3a94.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e87f6c22a3763c33043689b8a4f39fc0aa5a3a94.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d0b673e96bf36a5651c1cf0898f8e02023a36f6c.png" width="100%"></kbd></p>

> [!NOTE]
> requirement.txt đơn giản là define các package (lib) thôi.
> Trong MLOps Spec có cái lab dùng docker deploy
> model  Trong dockerfile có cái command dựa vào File
> requirement này để install các package vào docker
> image
>
> Còn static đơn giản là chứa các static file như css,
> image...

<br>

<a id="node-1748"></a>

<p align="center"><kbd><img src="assets/276cf2b386913c3d72cea4d5b92220b65add5f16.png" width="100%"></kbd></p>

<br>

<a id="node-1749"></a>

<p align="center"><kbd><img src="assets/079a6d591298b797ddb88d048dd2906c2c9b2972.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/079a6d591298b797ddb88d048dd2906c2c9b2972.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/de68a2af6ebd53ff4d2b3aff960150ec58077284.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái cái apology.html sẽ extend từ layout.html (chứa các
> phần html chung chung) và trong cái main block thì đại khái
> là nó dùng img tag để show một cái hình, cái hình này "lấy
> từ" một cái service kiểu như cho phép tạo cái meme image
> với nội dung mà ta gửi lên. Trong trường hợp này là lấy nội
> dung truyền vào từ render_template.

<br>

<a id="node-1750"></a>

<p align="center"><kbd><img src="assets/a1abe63d3b87fe6460051ea0ae3fdde91ff68ea2.png" width="100%"></kbd></p>

> [!NOTE]
> Xem qua cái layout.html.
> Khúc đầu là bootstrap

<br>

<a id="node-1751"></a>

<p align="center"><kbd><img src="assets/2e3e814184feb90ddc94f8ba75f7911049684bbb.png" width="100%"></kbd></p>

> [!NOTE]
> Cái body, khúc này là define cho cái NavBar
> mobile-friendly. Define như này là do Bootstrap nó
> chỉ vậy

<br>

<a id="node-1752"></a>

<p align="center"><kbd><img src="assets/f97e31bbe31ba8ca580eee2b8c3cb1e1009c9374.png" width="100%"></kbd></p>

> [!NOTE]
> Cuối cùng là main block sẽ chứa cái nội dung của
> những thằng apology.html, login. html khi extend từ
> layout.html
>
> Còn cái vụ Flask's message flashing là sao chưa hiểu
> để quay lại sau

<br>

<a id="node-1753"></a>

<p align="center"><kbd><img src="assets/8d61f48370e7d4b1c4b070b188ab120ef968be4b.png" width="100%"></kbd></p>

<br>

<a id="node-1754"></a>

<p align="center"><kbd><img src="assets/1d0beef6844966c84a7f000e9482688208ac418e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/729215ddfae37beb02e9ea22360cf7a1a216cf3b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1d0beef6844966c84a7f000e9482688208ac418e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/729215ddfae37beb02e9ea22360cf7a1a216cf3b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4f8699ea8b396df3c3164f6bfb084d14ff114428.png" width="100%"></kbd></p>

<br>

<a id="node-1755"></a>

<p align="center"><kbd><img src="assets/6ca24db4653a1b3abaec7ee4ae6f8ffeec20124a.png" width="100%"></kbd></p>

<br>

<a id="node-1756"></a>

<p align="center"><kbd><img src="assets/ec8f2d95e624fd807e7f2adf8f39507f0ed8aa74.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c585087a08b7d8ac1c56ac6eaf1a78f8acf752cd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ec8f2d95e624fd807e7f2adf8f39507f0ed8aa74.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c585087a08b7d8ac1c56ac6eaf1a78f8acf752cd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a6f6a6f6b2d1a6e150283dcd051116363c25f771.png" width="100%"></kbd></p>

<br>

<a id="node-1757"></a>

<p align="center"><kbd><img src="assets/2a5916bb160ead7d8b017e55fbe8b52d95081c02.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2a5916bb160ead7d8b017e55fbe8b52d95081c02.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fe5e622625431fa11c4ebd4d1b0069102ca20d53.png" width="100%"></kbd></p>

<br>

<a id="node-1758"></a>

<p align="center"><kbd><img src="assets/3a5a36a46703937eda111ed01ab17e02408b23f4.png" width="100%"></kbd></p>

<br>

<a id="node-1759"></a>

<p align="center"><kbd><img src="assets/fc71dec5fc50deb853ad346da380e3844124ce46.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fc71dec5fc50deb853ad346da380e3844124ce46.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/61e6ba2493164e7308d97252e15be2b1fa7c29e4.png" width="100%"></kbd></p>

<br>

<a id="node-1760"></a>

<p align="center"><kbd><img src="assets/7974d479e22c0292a319b28bb55375e2d0ec65c6.png" width="100%"></kbd></p>

<br>

<a id="node-1761"></a>

<p align="center"><kbd><img src="assets/a459437f1ee57a63e615fc116e8e53d7820e8934.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7684cf4b69f758618643bc83d664270dfe990bcc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a459437f1ee57a63e615fc116e8e53d7820e8934.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7684cf4b69f758618643bc83d664270dfe990bcc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1668783e1bad5652e5573d5daad8a81705c2bf89.png" width="100%"></kbd></p>

<br>

<a id="node-1762"></a>

<p align="center"><kbd><img src="assets/ddf7e753940daa45bb8142b540b7a1e07d1c457b.png" width="100%"></kbd></p>

<br>

<a id="node-1763"></a>

<p align="center"><kbd><img src="assets/8425d3df127a8ec6180374ac8638bc8425bafe2e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8425d3df127a8ec6180374ac8638bc8425bafe2e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1f97b21e4d1ec4e4d87067ba2381bd8271bf7b0a.png" width="100%"></kbd></p>

<br>

<a id="node-1764"></a>

<p align="center"><kbd><img src="assets/e69629080995cbfaf001670d3c6fb1d85c85d582.png" width="100%"></kbd></p>

<br>

