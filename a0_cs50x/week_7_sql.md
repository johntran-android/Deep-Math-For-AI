# Week 7: Sql

📊 **Progress:** `129` Notes | `160` Screenshots

---
<a id="node-1039"></a>

<p align="center"><kbd><img src="assets/a39240f70d97923796cd39913cdb248a59ab25f6.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là SQL là một language mới, làm được ít
> hơn so với C hay Python nhưng nó làm rất tốt cái
> việc của nó là work với data

<br>

<a id="node-1040"></a>

<p align="center"><kbd><img src="assets/900ab187e02f9e11a1bd0a8207a27087448061be.png" width="100%"></kbd></p>

<br>

<a id="node-1041"></a>

<p align="center"><kbd><img src="assets/e87d2520e7ed69c7f15b837aaec816f48d9da628.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là giả sử ta có dataset này (thống kê ghi nhận các
> problem set ưa thích nhất) thì nếu có thể tự mình
> manipulate và thấy các pattern của data (thay vì chỉ dùng
> các tool do Excel hay Google Spreadsheet làm ra)

<br>

<a id="node-1042"></a>

<p align="center"><kbd><img src="assets/eceebe7e4b357e4e36f4297efb3e1d87b2e386f2.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng đang dẫn dắt vào nhu cầu phải có SQL.
> Vì với C hay Python, việc làm việc với data không dễ
> dàng

<br>

<a id="node-1043"></a>

<p align="center"><kbd><img src="assets/785e80c9681744c7415ed53b29b55e8c83c1b6ab.png" width="100%"></kbd></p>

> [!NOTE]
> File csv có 3 cột Timestamp,
> language, problem

<br>

<a id="node-1044"></a>

<p align="center"><kbd><img src="assets/f300f93c11fb32874ffe8c8373062e4b242965f5.png" width="100%"></kbd></p>

<br>

<a id="node-1045"></a>

<p align="center"><kbd><img src="assets/d09ef6656e9f3469e29d8a4585537cf758ca38cd.png" width="100%"></kbd></p>

> [!NOTE]
> mở file và dùng csv.read(file) để
> đọc, reader sẽ là iterable

<br>

<a id="node-1046"></a>

<p align="center"><kbd><img src="assets/832cf4328f7f3e19c404d56f82fed4a16c5501b5.png" width="100%"></kbd></p>

> [!NOTE]
> D: Thay vì nó trả cho tôi nguyên một line / string dài
> của một row thì nó trả cho tôi cái gì, dựa vào cái
> syntax ở đây?
>
> A:**List các content** tương ứng của mỗi cột
>
> D: Correct! Vậy cái này sẽ in ra gì?
>
> A: Cột thứ 2 (vì index = 1) **Language**

<br>

<a id="node-1047"></a>

<p align="center"><kbd><img src="assets/c0651be01feb47f6a5acd59db1f7eaa5b2dd01cd.png" width="100%"></kbd></p>

> [!NOTE]
> D: Correct!

<br>

<a id="node-1048"></a>

<p align="center"><kbd><img src="assets/26c2f2471b6fbca2bf0418ec646ddb73bb61549c.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng define một variable
> "favorite" cho row[1]

<br>

<a id="node-1049"></a>

<p align="center"><kbd><img src="assets/c4fe9152270e69eb304f542ba6cdc6cc9cc30c98.png" width="100%"></kbd></p>

> [!NOTE]
> D: Tại sao define row[1] như này lại là bad design
>
> A: Vì ta không biết có bao nhiêu column, việc lấy  như vậy có
> thể dẫn đến error
>
> D: Đại khái là làm vậy ta phải nhớ row 1 là cái gì và **giả sử có
> người move cái cột đi** (cái này trong  excel có thể) thì cột có
> index = 1 này không còn là 'language' nữa.

<br>

<a id="node-1050"></a>

<p align="center"><kbd><img src="assets/27dd8f6f1c4c09609ccb9cf3deadbecbe7b75b6f.png" width="100%"></kbd></p>

> [!NOTE]
> D: Tại sao lại có chữ **language** ở đây?
>
> A: Vì nó là tên cái **cột**
>
> D: Correct -> header

<br>

<a id="node-1051"></a>

<p align="center"><kbd><img src="assets/8919d698c8afd3413bf5327fe3219a1b4bfdb64f.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói nếu không thích cái
> header ta có thể **next(row)** để **skip**

<br>

<a id="node-1052"></a>

<p align="center"><kbd><img src="assets/92c602438d17e723339e48c7b9d031328facee00.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái giờ ta dùng **csv.DictReader** thay vì reader thì
> như cái tên suggest nó sẽ**trả ra mỗi row là dạng
> dictionary**
>
> Dạng list (ở trước):
>
> row[0] = item 1 là time-stamp value,  row[1] = item 2 là
> language, row[2] = item 3 là problem
>
> Dạng dictionary:  **row['Timestamp']** = time-stamp value
> **row['language'] = language value**

<br>

<a id="node-1053"></a>

<p align="center"><kbd><img src="assets/54386fa636679f0fcee447c086efb19ccd026792.png" width="100%"></kbd></p>

> [!NOTE]
> Và với kiểu này, ta **không "bị dính" cái header**
> title 'language' trong đó mà **không cần skip(row)**
> Và cho dù có**"move column around"**, thì cũng
> **không ảnh hưởng gì** cả vì row["language"]
> luôn cho ra cột language
>
> không phải như khi dùng csv.reader cho row là
> list thì **row[1] chưa chắc luôn là cột language**

<br>

<a id="node-1054"></a>

<p align="center"><kbd><img src="assets/5beeac100ca2ff2902c80ccfe2232bc77a1b487c.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta sẽ đếm xem thử trong cột **language**
> sẽ **có mỗi loại bao nhiêu (người chọn)**

<br>

<a id="node-1055"></a>

<p align="center"><kbd><img src="assets/f9cb3fabb96e499a9ae320014d99253375e48c92.png" width="100%"></kbd></p>

> [!NOTE]
> Trong Python cho phép **initialize**
> kiểu này **a, b, c = 0, 0, 0**

<br>

<a id="node-1056"></a>

<p align="center"><kbd><img src="assets/b9ccfff027f5478eeaec325764c4c5c9cab6a1c1.png" width="100%"></kbd></p>

<br>

<a id="node-1057"></a>

<p align="center"><kbd><img src="assets/7323b43322958f3a39a62315d8a10289a4720fb5.png" width="100%"></kbd></p>

> [!NOTE]
> D: Có gì không ổn?
>
> A: Việc **gọi cụ thể tên language** như vậy không ổn, ta có thể
> **không cần care trong đó có gì**. Bằng cách dùng một **set** để
> **lọc ra trong cột có các kết quả gì**. Sau đó dùng nó để đếm.
> Hoặc có thể dùng dictionary
> Ví dụ:
>
> favorite  = **{}**
> for row in reader:
> // **Check xem trong dictionary có key là value của row['language']
> hay chưa** (ta không cần biết là cái gì). Nếu **có thì ++ (count up)**
> nếu **chưa thì add vào**
>
> Khi check có thể là favorite.keys() hay sao đó
> nhưng đại khái là check xem có trong các keys chưa
>
> if **row['language'] in favorite**: //Correct!
>   **favorite[row['language']] += 1**//Correct!
> else:
>   **favorite[row['language']]  = 1**  //Correct!

<br>

<a id="node-1058"></a>

<p align="center"><kbd><img src="assets/185ece4b0cd3522da3e42531af7e7beae4030930.png" width="100%"></kbd></p>

> [!NOTE]
> Chính xác, nhưng làm từ từ, đầu tiên ổng làm y
> như mình, **tạo** **counts là một dict**
>
> Và ổng hỏi làm vậy thì có gì không ổn?
>
> A: Phải check xem trong dictionary có key mang 
> giá trị là language value của cái row đó hay chưa.
> Nếu có mới ++ được, không thì phải set vào = 1

<br>

<a id="node-1059"></a>

<p align="center"><kbd><img src="assets/d5c4508937b3d7ce03b7439d3ddc5ea2fcc7b769.png" width="100%"></kbd></p>

> [!NOTE]
> Có con nhỏ hỏi liệu Python nó **có automatically
> tạo 1 cái key** hay không?
>
> **Không,** nó sẽ báo error

<br>

<a id="node-1060"></a>

<p align="center"><kbd><img src="assets/06e25683b89d2d8e9030d08dc38b0eba6c5de6e0.png" width="100%"></kbd></p>

> [!NOTE]
> Y chang luôn

<br>

<a id="node-1061"></a>

<p align="center"><kbd><img src="assets/1d277f1932f966f2e13183d53dc0297150201e85.png" width="100%"></kbd></p>

> [!NOTE]
> Có người hỏi làm sao để **in theo thứ tự** - D: Ta có thể **sorted
> cái dict counts** và lệnh **sorted** khi đọc trong doc sẽ thấy nó có
> các argument, ví dụ ở đây để **reverse = True** thì nó sẽ sort
> reverse (alphabetically)

<br>

<a id="node-1062"></a>

<p align="center"><kbd><img src="assets/019e2eabe03cecee5523980c425aa74241588ef2.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, đại khái có thể define thêm key = một function
> **get_value** như này, để rồi nó sẽ **sort dictionary**
> theo **giá trị tương ứng của cái key trong dict**
>
> Python có value cao nhất -> C > Scratch

<br>

<a id="node-1063"></a>

<p align="center"><kbd><img src="assets/108a48691d30f6b691c74c939b5e4e1bdd9a029d.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ta có thể **không cần define một function cụ thể** khi chỉ
> dùng có một lần trong đây, thay vào đó có thể dùng **lambda
> function**, (**anonymous function**) như vầy 
>
> key = **lambda language: counts[language]**

<br>

<a id="node-1064"></a>

<p align="center"><kbd><img src="assets/63f206eabc724661a0e829d256d29b506784917d.png" width="100%"></kbd></p>

> [!NOTE]
> D: Giờ tui đổi từ '**language**' sang '**problem'** chỗ này thì bây
> giờ các program làm gì?
>
> A: Nó sẽ**đếm các loại problem set** mà được nhắc đến
> trong column 'problem'

<br>

<a id="node-1065"></a>

<p align="center"><kbd><img src="assets/9c1873061c8696976826a8621512f8d7a65d60a5.png" width="100%"></kbd></p>

> [!NOTE]
> Correct! Và sort theo số lượng "vote"

<br>

<a id="node-1066"></a>

<p align="center"><kbd><img src="assets/dffd5b72945d10fdd7e684fe5c901695bcd34d65.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là làm thêm chút nữa, cho user
> **nhập loại problem set** họ thích, để**in ra số
> vote** cho problem set đó.
>
> Kết quả nhập Mario -> 39
>
> Xong có người hỏi nếu mà nhập **mario** thì sao 
>
> D: Thì nó không ra, như có thể thấy vì column's
> vì trong cột problem không có 'mario', nên trong dict
> ở đọan trên không có key 'mario'. Nhưng ta có thể giải
> quyết bằng cách nào?
>
> A: Thì check thêm lowercase:
>
> If favorite.lower() in counts:
>   print(....counts[favorite.lower()]
>
> D: Ok, có thể

<br>

<a id="node-1067"></a>

<p align="center"><kbd><img src="assets/bbc04c6c64b9bc695745feb4e42e415152a885b1.png" width="100%"></kbd></p>

> [!NOTE]
> Relational database

<br>

<a id="node-1068"></a>

<p align="center"><kbd><img src="assets/a13c21a1c1ca6c6f69f088840401ffc7a4ee3f47.png" width="100%"></kbd></p>

<br>

<a id="node-1069"></a>

<p align="center"><kbd><img src="assets/7a5affa6c29aa3942000873365702091c765dac7.png" width="100%"></kbd></p>

> [!NOTE]
> Về cơ bản chỉ có 4 loại hành động CRUD : 
>
> **C**reate data (**CREATE**, **INSERT**), 
>
> **R**eading data (**SELECT**), 
>
> **U**pdate data (**UPDATE**), 
>
> **D**elete data (**DELETE**, **DROP**)

<br>

<a id="node-1070"></a>

<p align="center"><kbd><img src="assets/7d6473003430f6104b2248c7b560e603074796af.png" width="100%"></kbd></p>

> [!NOTE]
> Hành động này tương tự như khi mở Google
> Spreadsheet lên, đặt tên file (save as), và gõ title của 3
> column **Timestamp, language, problem**

<br>

<a id="node-1071"></a>

<p align="center"><kbd><img src="assets/dc25fe8558ed3c5608608616f29944c8e8284946.png" width="100%"></kbd></p>

<br>

<a id="node-1072"></a>

<p align="center"><kbd><img src="assets/00ba5dd30aeb58356fc35f57443f13dab2f0bbf9.png" width="100%"></kbd></p>

> [!NOTE]
> Dòng code này sẽ đại khái là**tạo một
> empty database tên là favorites.db**

<br>

<a id="node-1073"></a>

<p align="center"><kbd><img src="assets/feae8184ca22bb92860be45ad3fa428ea6227b88.png" width="100%"></kbd></p>

> [!NOTE]
> Và đại khái là sau đó nó sẽ trở thành **terminal sqlite** thay
> vì**$** có nghĩa là ta **đang làm việc với database này**
>
> Và **tí nữa ta sẽ dùng python để tương tác với database**
> giống như swift, kotlin, ....trong đời thực cũng có thể
> tương tác với database

<br>

<a id="node-1074"></a>

<p align="center"><kbd><img src="assets/63ad3d00ca97e44373279f68d435aa20f8744818.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái hai câu lệnh này sẽ là:
>
> **Để chế độ (mode) csv**
>
> Và **import csv file** vào thành database

<br>

<a id="node-1075"></a>

<p align="center"><kbd><img src="assets/fd62f4813979d2adabe64080b8fa3647633d040a.png" width="100%"></kbd></p>

> [!NOTE]
> **.import favorites.csv favorites** 
>
> Ra lệnh cho máy tính **import file csv favorite**
> vào t**hành database có tên favorites**.
>
> Và dù **kết quả không có gì** nhưng như thông lệ,
> **không có gì có nghĩa là tốt**

<br>

<a id="node-1076"></a>

<p align="center"><kbd><img src="assets/37d785e25d31e773fc174030c17f101c575e9d15.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói thêm **command** **có dấu chấm** kiểu này là sqlite,
> **không thật sự là sql**
>
> Rồi đại khái **.schema** là giúp cho thấy làm cái gì thì ở đây
> có nghĩa là lệnh import ..ở trên  đã **gọi lệnh sql 
>
> CREATE TABLE IF NOT EXISTS "favorites" 
> ("Timestamp" TEXT, "language" TEXT, "problem" TEXT);**- tạo một table có tên là "favorites" trong đó có  "Timestamp"
> thuộc loại TEXT, "language" thuộc loại TEXT,  "problem" TEXT

<br>

<a id="node-1077"></a>

<p align="center"><kbd><img src="assets/53c34a4ce549f1c20ebead7becbee8d885e263d6.png" width="100%"></kbd></p>

<br>

<a id="node-1078"></a>

<p align="center"><kbd><img src="assets/fe90024e0b9bbd6d474660f2457cd05eadd9c607.png" width="100%"></kbd></p>

> [!NOTE]
> Chữ viết hoa **SELECT** là sql keyword thì dù bạn không cần
> phải viết hoa nhưng **khuyên nên viết** để **phân biệt với cái
> không phải sql keyword**như tên **columns, table...**
>
> Thì đại khái câu lệnh này sẽ**select data từ một hoặc nhiều
> column từ table có tên chỉ định**

<br>

<a id="node-1079"></a>

<p align="center"><kbd><img src="assets/40ef25f29b8c686fa71605d0a8a9f7e226ad86e2.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói tôi **muốn chọn cả 3 cột:**
>
> **SELECT** **Timestamp, problem, favorite** **FROM favorites**;
>
> Nhưng để chọn hết thì có thể dùng
>
> **SELECT * FROM favorites;**
>
> Thì nó sẽ kiểu như **chọn tất cả các row thuộc 3 column
> và in ra**

<br>

<a id="node-1080"></a>

<p align="center"><kbd><img src="assets/bd4b317c49e636fa866a23e36f3ad6669e797e4f.png" width="100%"></kbd></p>

<br>

<a id="node-1081"></a>

<p align="center"><kbd><img src="assets/dbf0e305500c75311686beffc97c3144e7d25b1d.png" width="100%"></kbd></p>

> [!NOTE]
> Và ls thì sẽ thấy trong directory có
> thêm một file là**favorites.db**

<br>

<a id="node-1082"></a>

<p align="center"><kbd><img src="assets/b6e42f5ee44e6c4f6fc824ba5de2b530fa2c4c2b.png" width="100%"></kbd></p>

> [!NOTE]
> gọi lại **sqlite3 favorite.db thì**nó sẽ kiểu như là
> **quay lại làm việc với database favorites.db**

<br>

<a id="node-1083"></a>

<p align="center"><kbd><img src="assets/913506517ee9b18d5893d8619a097a231d3cd492.png" width="100%"></kbd></p>

> [!NOTE]
> Gọi lại function SELECT mọi column

<br>

<a id="node-1084"></a>

<p align="center"><kbd><img src="assets/01aecf2b06ee32ec77ec92a37e8c356c27a67a84.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là ta vẫn thấy lại data như hồi nãy,
> nhưng đẹp hơn vì**không còn mode csv nữa**

> [!NOTE]
> Control L: Clean all things

<br>

<a id="node-1085"></a>

<p align="center"><kbd><img src="assets/90c8ed9a558bfecf92e1e3dc8a0f05809db0d5c4.png" width="100%"></kbd></p>

> [!NOTE]
> Ok giờ nếu muốn **select một cột
> language** thôi thì làm như này

<br>

<a id="node-1086"></a>

<p align="center"><kbd><img src="assets/4d78e1d7c59267899c286cfba6b14b8fa273b5e9.png" width="100%"></kbd></p>

<br>

<a id="node-1087"></a>

<p align="center"><kbd><img src="assets/b9ae99e8cbc8ba657a10c5ea727c0ee4f773e74e.png" width="100%"></kbd></p>

> [!NOTE]
> Và đây là các **function** của sql,
> AVG - tính trung bình
> COUNT - đếm row
> DISTINCT - đếm số value không trùng 
> LOWER
> MAX - chắc là lấy max value
> MIN - lấy min value
> UPPER ...

<br>

<a id="node-1088"></a>

<p align="center"><kbd><img src="assets/8b272a8061a53177b456dc3933273ed4a4313ebc.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT COUNT(*) FROM favorites; 
>
> Đại khái là đếm tất cả các row của database
>
> -> Có 430 rows

<br>

<a id="node-1089"></a>

<p align="center"><kbd><img src="assets/238008961a01621280cd3b33a2375c3eb4f45eea.png" width="100%"></kbd></p>

> [!NOTE]
> Gọi lệnh này **SELECT DISTINCT(language) FROM favorites;**
> Đại khái là nó sẽ chỉ **lấy ra các loại khác nhau** trong column 
> language (nôm na là trong cột language có các lọai gì)

<br>

<a id="node-1090"></a>

<p align="center"><kbd><img src="assets/83622a391125f402b0d0c0b665a90206dd4e28fb.png" width="100%"></kbd></p>

> [!NOTE]
> Giờ nếu **SELECT COUNT(DISTINCT(language))
> FROM favorites;**
>
> D: Thì nó ra gì?
>
> A: Lấy ra các loại khác nhau của cột language và đến số
> row: **3**

<br>

<a id="node-1091"></a>

<p align="center"><kbd><img src="assets/30f82d5d2f7f70fcf9848108b70664f2cc0ba2a7.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói đại khái là sql nó**trả về cho ta một subset**
> of your data (smaller table of data)
>
> Và kết quả này **không được save vào đâu cả**

<br>

<a id="node-1092"></a>

<p align="center"><kbd><img src="assets/5db1767ab6a3224055b01d5a2e57446dd0a46c8d.png" width="100%"></kbd></p>

> [!NOTE]
> Và thay vì để cái cột có tên **COUNT(DISTINCT(language))**thì có thể dùng **AS n** (có nghĩa là **aliase as**) để **thay cái tên
> đó bằng tên ngắn hơn "n"** (Aliase: Bí danh)

<br>

<a id="node-1093"></a>

<p align="center"><kbd><img src="assets/ec48d63529e5f96728c171fb371d1732f8b488a3.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Distinct?
>
> D: Chỉ đơn giản khi bạn distinct là 1 list thì cũng như bỏ vào
> set vậy, **chỉ giữ những các khác nhau**, **remove hết các duplicate**
> [1,2,3,1,3,4] => [1,2,3,4]

<br>

<a id="node-1094"></a>

<p align="center"><kbd><img src="assets/4f526d85cf3f8ffa398a980ec90ad1b002591d55.png" width="100%"></kbd></p>

> [!NOTE]
> **n** kiểu như một**nick name** và đại khái là có
> thể dùng lại được

<br>

<a id="node-1095"></a>

<p align="center"><kbd><img src="assets/c8bbe5896444a9d8f015ce4769eb413ebbe2119f.png" width="100%"></kbd></p>

> [!NOTE]
> Một số keyword khác

<br>

<a id="node-1096"></a>

<p align="center"><kbd><img src="assets/fd4d4fe1c7c60aa23145568a798aabc4bf2def25.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT COUNT(*) FROM favorites
> **WHERE language = 'C';**
>
> Trả về sub-table có 1 column là COUNT(*)
> có value là **đếm số row mà có language = C**
>
> Và nếu không có WHERE language = 'C';
>
> trả về sub-table có 1 column là COUNT(*)
> có value là đếm số row nói chung

<br>

<a id="node-1097"></a>

<p align="center"><kbd><img src="assets/aa348077a4c5977f2820ea87a41898d2e8213795.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT COUNT (*) FROM
> favorites WHERE language = 'C' AND problem = 'Mario';
>
> -> **Đếm số row mà language = 'C' và problem = 'Mario'**
> và trả về sub-table có 1 column là COUNT(*)

<br>

<a id="node-1098"></a>

<p align="center"><kbd><img src="assets/64f8f7a8ed0078bac9e72de7a73101c0a3e57408.png" width="100%"></kbd></p>

> [!NOTE]
> **SELECT language, COUNT(*) FROM favorites GROUP 
> BY language;**
>
> Tạo sub table có 2 cột: language và COUNT(*) tức là 
> "lấy các giá trị trong language", và "đếm xem mỗi loại 
> có mấy cái" 
>
> và sau đó là **gom lại theo language**. Có nghĩa là**chỉ 
> show ra mỗi loại (language) có mấy cái.**

<br>

<a id="node-1099"></a>

<p align="center"><kbd><img src="assets/93a6d8a32d82c8c6c39ec8cf3da5a32cf7dbff1f.png" width="100%"></kbd></p>

<br>

<a id="node-1100"></a>

<p align="center"><kbd><img src="assets/0f98bd059981f379f0adffc50b57d3c1d897af76.png" width="100%"></kbd></p>

> [!NOTE]
> Và nếu thêm **ORDER BY COUNT(*)** thì nó sẽ
> sort theo gía trị của**"số lượng" mỗi language**

<br>

<a id="node-1101"></a>

<p align="center"><kbd><img src="assets/2f6a57dd4b936836bed9a7bfebda9650c7af43fc.png" width="100%"></kbd></p>

> [!NOTE]
> Và nếu muốn từ **lớn đến
> nhỏ** thì thêm **DESC**

<br>

<a id="node-1102"></a>

<p align="center"><kbd><img src="assets/c2b418a973b9cb43af9a76be7a2b07750fc23c62.png" width="100%"></kbd></p>

> [!NOTE]
> Và nếu chỉ muốn thằng
> lớn nhất, thì**DESC LIMIT 1**

<br>

<a id="node-1103"></a>

<p align="center"><kbd><img src="assets/ae16791777c281fafbdf775cb009628bf5c8a9e7.png" width="100%"></kbd></p>

> [!NOTE]
> Giờ đến **INSERT vào table**

<br>

<a id="node-1104"></a>

<p align="center"><kbd><img src="assets/ee5595851124a2b55241c6c0abccfa67c3e7ac33.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ
>
> INSERT INTO favorites (language, problem) 
> VALUES('SQL', 'Fiftyville');
>
> -> Insert thêm 1 row, cột **language** thì là **'SQL'**, cột 
> **problem** thì là **'Fiftyville'**

<br>

<a id="node-1105"></a>

<p align="center"><kbd><img src="assets/d0d0aeba00c97c8f6ae697ac44948297d5cce8f1.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi tiếp muốn **xem tất cả các row** (và mọi cột)
> nhưng **language = 'C'**:
>
> SELECT * FROM favorites WHERE language = 'C';

<br>

<a id="node-1106"></a>

<p align="center"><kbd><img src="assets/0bcc55ab2b2ecdcee9f7610a9e292357759fd206.png" width="100%"></kbd></p>

<br>

<a id="node-1107"></a>

<p align="center"><kbd><img src="assets/b876bcb4848967a3808b163936aae030fdc2012f.png" width="100%"></kbd></p>

> [!NOTE]
> Qua update data

<br>

<a id="node-1108"></a>

<p align="center"><kbd><img src="assets/568c65050c8b43304fa7d495cd5dc9a512c7b32a.png" width="100%"></kbd></p>

> [!NOTE]
> UPDATE favorites SET language = 'C++' WHERE language = 'C';
>
> -> Update data, set giá trị của cột language của mọi hàng nào
> mà đang là C thành C++;

<br>

<a id="node-1109"></a>

<p align="center"><kbd><img src="assets/7e8ea6a34a96f36b19b33f95150738e88505ea93.png" width="100%"></kbd></p>

> [!NOTE]
> Xong giờ ổng muốn đổi lại, nhưng hỏi là nếu mà gọi
>
> UPDATE favorites SET language = 'C' 
>
> Thì sẽ làm sao?
>
> A: Thì mọi hàng trong cột language sẽ đều thành C hết

<br>

<a id="node-1110"></a>

<p align="center"><kbd><img src="assets/f704ea770649985829335fed81782aaf649b5b97.png" width="100%"></kbd></p>

> [!NOTE]
> Correct, do đó rất dễ gây tai họa. Cho nên phải**đảm bảo luôn
> backup data** và ít nhất cũng **luôn chắc chắn check kĩ** trước
> khi nhấn enter

<br>

<a id="node-1111"></a>

<p align="center"><kbd><img src="assets/1c1a5e70dac95bfbd2a30475d8849a876c277b37.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Có phải cái này là find và replace không?
>
> D: Correct

<br>

<a id="node-1112"></a>

<p align="center"><kbd><img src="assets/775b6f9f7b1358a439ad4c72a487c0a1bae689cd.png" width="100%"></kbd></p>

> [!NOTE]
> DELETE FROM favorites WHERE problem = 'Tideman';
>
> -> Delete mọi row mà giá trị của cột 'problem' = 'Tideman'

<br>

<a id="node-1113"></a>

<p align="center"><kbd><img src="assets/5c95b7865f4aee83ca9ee421d40f8ff5d387df40.png" width="100%"></kbd></p>

> [!NOTE]
> D: Cái này thì sẽ ntn 
>
> A: Delete hết table

<br>

<a id="node-1114"></a>

<p align="center"><kbd><img src="assets/3de4f367ed6465c02a85e3eebbcee6da3a4ab441.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về bộ database tên là **IMBb
> movies review**. Tí nữa ta sẽ làm việc
> với bộ data này

<br>

<a id="node-1115"></a>

<p align="center"><kbd><img src="assets/23088ee73600c28034cb25830f0cb5f3049a6528.png" width="100%"></kbd></p>

> [!NOTE]
> Cụ thể là nó có
> tới 6 bộ data

<br>

<a id="node-1116"></a>

<p align="center"><kbd><img src="assets/9b94dbc900990137bf2bfc6bc5120154ff99d06a.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là trong giờ nghỉ ổng đã download một file
> tên là **show.db** chuẩn bị trước rồi

<br>

<a id="node-1117"></a>

<p align="center"><kbd><img src="assets/1704f80d41aa0f9cb8241845f47d6d456a65ccc7.png" width="100%"></kbd></p>

> [!NOTE]
> **sqlite3 show.db** để bắt đầu làm việc với
> database này

<br>

<a id="node-1118"></a>

<p align="center"><kbd><img src="assets/5e1f0878680f3eac4240d338b00a7ba82b331531.png" width="100%"></kbd></p>

> [!NOTE]
> Gọi **.schema** hồi nãy đã nói để **xem
> thông tin về database này**

<br>

<a id="node-1119"></a>

<p align="center"><kbd><img src="assets/993d3263387e515ec5b2050f67b6669ca8b68297.png" width="100%"></kbd></p>

<br>

<a id="node-1120"></a>

<p align="center"><kbd><img src="assets/b2ac701f279822bee83d28288e1e15d737437460.png" width="100%"></kbd></p>

<br>

<a id="node-1121"></a>

<p align="center"><kbd><img src="assets/aae3a36ebddf9de784f0d3daa619ca7ed36d03ed.png" width="100%"></kbd></p>

<br>

<a id="node-1122"></a>

<p align="center"><kbd><img src="assets/61cca5b0bcc8c61112816c7ed215ef63140485d7.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng nói về các database này liên hệ / link tới nhau.
> Ví dụ như **shows - genres**, khi muốn biết cái show với id nọ có
> genres là gì (comedy, hay drama) thì chỉ cần**look up với id
> trong genres table.**
>
> D: Tại sao khổ vậy, sao không thêm một cột genres ngay trong
> table show?
>
> -> Đại khái là nếu làm vậy, sẽ khó (dù có thể) đó là**cho một show
> có nhiều genres**. Còn với một table genres riêng biệt thì có thể
> cùng **1 show id có thể có 3 row với 3 giá trị genres.**

<br>

<a id="node-1123"></a>

<p align="center"><kbd><img src="assets/636c8d317c8489c8296555abde523101ceccd207.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự, với people và stars, ta có
> thể có quan hệ **1 - nhiều**: **1 người
> tham gia nhiều show** và **1 show có nhiều
> người.**
>
> Ví dụ
>
> ...
> show #2 - person #5
> ...
> show #44 - person #5
> show #44 - person #16

<br>

<a id="node-1124"></a>

<p align="center"><kbd><img src="assets/d4663bb6f33632998a0eaac75a45481da7d21e59.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là trong **SQLite** (phiên bản nhẹ hơn của sql
> mà ta hay thấy dùng trên mobile ..) có các **datatype**
> chính như
>
> **BLOB** - Binary Large Object,
>
> **INTEGER** - Integer biết rồi
>
> **NUMBER** - Ổng nói ví dụ như date-time
>
> **REAL** - Như float
>
> **TEXT** - String

<br>

<a id="node-1125"></a>

<p align="center"><kbd><img src="assets/5a1a6d3f851a67626abc7ae22e554ecb5d7545d1.png" width="100%"></kbd></p>

> [!NOTE]
> Còn hai cái key **NOT NULL** và **UNIQUE** đại khái là
> để **constraint** rằng**data không được NULL** và phải 
> **không được trùng lặp.**
>
> Ví dụ như hồi nãy ổng insert **SLQ và 'fiftyville'** thì 
> không có **Time-stamp**, thì **nếu như có NOT NULL**
> config của cột time-stamp thì **sqlite nó sẽ complain**
>
> Nói chung là **có nhiều constraint khác nữa**

<br>

<a id="node-1126"></a>

<p align="center"><kbd><img src="assets/0413f5bd7f2b55067f0e6eda0f55c1e73125b443.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về **PRIMARY KEY** ví dụ như trong table shows này,
> PRIMARY KEY (id) có nghĩa là, cũng t**ương tự như keyword
> constraint UNIQUE**, thì cái này table nó sẽ **treat cột id một
> cách đặc biệt hơn**, dùng nó làm**unique identifier**.
>
> Ngoài ra xem qua ta thấy các datatype như id là INTEGER,
> Title là TEXT NOT NULL, text và không được null, nên như
> đã nói nếu insert mà không có title thì sql sẽ complain.
> Rồi year là NUMERIC, episode là INTEGER

<br>

<a id="node-1127"></a>

<p align="center"><kbd><img src="assets/15334477c302c69c380ff1e0498b14d4a661b211.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự, ở table people này ta cũng thấy,
> PRIMARY KEY (id) - cột id được treat specially
> dùng làm Unique Identifier

<br>

<a id="node-1128"></a>

<p align="center"><kbd><img src="assets/43af528583ce60bb4d75cea82895d324e5a5a7e3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/43af528583ce60bb4d75cea82895d324e5a5a7e3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/88745b5c45e6b6bfc3526ec4a89a52f5a31fc4d3.png" width="100%"></kbd></p>

> [!NOTE]
> Còn keyword**FOREIGN KEY(show_id) REFERENCES**
> **shows(id)** ý là **cột show_id chính là cột id của table 'shows'**
> và**FOREIGN KEY (person_id) REFERENCES people(id)**
> ý là **cột person_id chính là cột id của table people**
>
> Và cái này mô tả trong chart là mũi tên

<br>

<a id="node-1129"></a>

<p align="center"><kbd><img src="assets/bd38e23686326e1b10f253a57e855ae79d9906cb.png" width="100%"></kbd></p>

> [!NOTE]
> Sqlite .schema

<br>

<a id="node-1130"></a>

<p align="center"><kbd><img src="assets/7531b0f5661b47f419b4894c9d86855de1ccf03b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7531b0f5661b47f419b4894c9d86855de1ccf03b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/55ab7bd40a90ff2ca035b0ea707a27a026104e5f.png" width="100%"></kbd></p>

> [!NOTE]
> **SELECT * FROM people;** -> Chọn, tạo
> subtable **mọi hàng mọi cột** từ**table people**

<br>

<a id="node-1131"></a>

<p align="center"><kbd><img src="assets/91ff112126fd3b76dddf7757ce8488fb9235569d.png" width="100%"></kbd></p>

> [!NOTE]
> **SELECT * FROM people LIMIT 10;**
> -> **Tạo subtable mọi cột** từ **people**
> nhưng**limit 10 row**

<br>

<a id="node-1132"></a>

<p align="center"><kbd><img src="assets/1d035c5c1f27773b8d2c7031961abf5e83300a9f.png" width="100%"></kbd></p>

<br>

<a id="node-1133"></a>

<p align="center"><kbd><img src="assets/c610067e76dccd2a7f9daa65fb28acaf46c70149.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi xem qua **stars** table thì ta thấy **show_id** và **person_id**
> như nãy nói, nó là **FOREIGN KEY**, map **id** của **table shows**
> và **id** của **table people**
>
> Để ý thấy với kiểu này**1 show có thể có nhiều người tham gia**
> (như nói về việc tại sao phải chia ra nhiều table như hồi nãy)
> bằng cách như thấy ở đâu **show id 62614 có nhiều hàng với các
> Person id khác nhau.**
>
> Và ngược lại, nó cũng cho phép 1 người tham gia nhiều show
> Khi ví dụ ông 378823 có thể xuất hiện ở row khác với show id khác

<br>

<a id="node-1134"></a>

<p align="center"><kbd><img src="assets/4ab3e629c48fb340e130609e5f4afab3190dea15.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT * FROM genres WHERE genre = 'Comedy'
> LIMIT 10;
>
> -> Tạo subtable mọi cột, từ table genres, chỉ lấy row
> nào mà cột genre = 'Comedy' giới hạn 10 cái
>
> SLECT * FROM genres WHERE id = 62614;
>
> -> Tạo subtable mọi cột, từ table genres, chỉ lấy cái 
> row mà cột id = '62614'

<br>

<a id="node-1135"></a>

<p align="center"><kbd><img src="assets/4792eaedd197e100d272c9bf754fe8b26d81caf7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4792eaedd197e100d272c9bf754fe8b26d81caf7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/aa7ba843bfb510b6a6f632e6d4b9025999cc22fc.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT show_id FROM genres WHERE genre = 'Comedy';
>
> -> Tạo subtable với 1 cột là show_id từ table genres và chỉ 
> chọn row nào mà genre = 'Comedy' thôi.

<br>

<a id="node-1136"></a>

<p align="center"><kbd><img src="assets/6021abad07ca6928048f625856997d5b4e5540b1.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT COUNT(show_id) FROM genres WHERE genre = 'Comedy';
>
> Tạo subtable 1 cột là COUNT(show_id), mà các row = 'Comedy'
> -> đếm các row có genre = 'Comedy'

<br>

<a id="node-1137"></a>

<p align="center"><kbd><img src="assets/2eabad22c0ce893a5cddce83330e2f3df1b14409.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT show_id FROM genres
> WHERE genre = 'Comedy' 
>
> -> tạo / chọn subtable 1 cột show_id từ table genres
> nơi mà genre = 'Comedy'.
>
> (Lựa ra các id của các show thuộc loại hài kịch)
>
> Sau đó SELECT title FROM shows WHERE id IN (..)
>
> -> Chọn / tạo subtable 1 cột title từ table shows sao
> cho các row có cột id có giá trị chứa trong table ở trên
>
> (Lựa ra các tên của các show thuộc loại hài kịch)

<br>

<a id="node-1138"></a>

<p align="center"><kbd><img src="assets/be39183899de70cc0435892b3c476845dae3148d.png" width="100%"></kbd></p>

<br>

<a id="node-1139"></a>

<p align="center"><kbd><img src="assets/dab6daec1770e96807fd400292004fbf4c6f0f2b.png" width="100%"></kbd></p>

> [!NOTE]
> rồi thêm ORDER BY title LIMIT 10;
> để sort theo alphabetical

<br>

<a id="node-1140"></a>

<p align="center"><kbd><img src="assets/b8bed3f5c6a10569cd434a029edcd3a8e9a35163.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi bây giờ thử tìm các show mà Steve Carell
> có tham gia
>
> Đầu tiên là xem thử trong table people 
>
> SELECT * FROM people WHERE name = 'Steve Carell';
>
> Tạo subtable từ table people mà row có cột name là Steve
> Carell

<br>

<a id="node-1141"></a>

<p align="center"><kbd><img src="assets/d0e83b163b9b947248ce2e858956ab7c90045e7a.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi với id của ổng là 136797, tìm trong table stars:
>
> SELECT * FROM stars WHERE person_id = 136797;
>
> Tạo subtable từ stars, lấy mọi cột sao cho person_id bằng
> như vậy
>
> Ta có các show_id mà ông này có tham gia

<br>

<a id="node-1142"></a>

<p align="center"><kbd><img src="assets/8a107ec8be002ea4db4bdc2ac3bbbc8cb42ddc42.png" width="100%"></kbd></p>

> [!NOTE]
> Xong từ các show_id ta có thể SELECT title FROM shows
> WHERE id = show id;
>
> để tạo subtable từ shows lấy cột title sao cho id bằng show id
> để ra được title của show đó

<br>

<a id="node-1143"></a>

<p align="center"><kbd><img src="assets/c035c51441b83d886ffdd1ffff6ceb76ea336e36.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT title FROM shows WHERE id IN 
> (SELECT show_id FROM stars WHERE person_id = 
> (SELECT id FROM people WHERE name = 'Steve Carell'))
> ORDER BY title;
>
> Ý nghĩa nôm na:
>
> 1/ Tìm trong table people để cho cột id của row có name là
> Steve Carell
>
> 2/ Với giá trị id đó, tìm trong table stars những show_id mà
> tương ứng có person_id là id trên.
>
> 3. Với những show ids đó, tìm trong table shows những title
> mà id tương ứng.
>
> Sort theo alphabetically

<br>

<a id="node-1144"></a>

<p align="center"><kbd><img src="assets/9f081fd95dc32e079275e74623132d22cd634d87.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói qua JOINT là một trong
> những công cụ mạnh nhất của sql
>
> Đầu tiên là tạo hai table với:
>
> SELECT * FROM shows LIMIT 10;
> -> chọn 10 rows của table shows.
> SELECT * FROM genres LIMIT 10;
> -> chọn 10 rows của table genres
>
> Thì đại khái là hai table shows và genres
> đều có PRIMARY ID là show ids, nên kết quả
> đều giống nhau ở cột show_id
>
> bây giờ làm sao JOINT hay cái lại

<br>

<a id="node-1145"></a>

<p align="center"><kbd><img src="assets/fbc4925d0a54441ea485a83ac778248a7392c548.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT * FROM shows JOIN genres ON shows.id =
> genres.show_id;
>
> Chọn / tạo subtable với mọi cột, từ hai table shows và
> genres sao cho value của cột id trong table show bằng
> show_id trong table genres.

<br>

<a id="node-1146"></a>

<p align="center"><kbd><img src="assets/28f3a2a15a5b5329187893aac5404d8b09e887ad.png" width="100%"></kbd></p>

> [!NOTE]
> Thêm WHERE title = 'The office' để joint hai table và chỉ
> show những row mà title là 'The office' thôi
>
> Cho thấy sau khi join ta có hai cột chứa show id là id của 
> table show và show_id của table genres

<br>

<a id="node-1147"></a>

<p align="center"><kbd><img src="assets/91cd4584588e36b732e4367ec1bb12b93e3e8a26.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT * FROM shows JOIN ratings ON shows.id =
> ratings.show_id WHERE title = 'The Office';
>
> Tạo subtable bằng cách join shows và ratings lại nơi nào
> id của shows bằng với show_id của ratings và chỉ lấy row
> nào mà title = The Office thôi

<br>

<a id="node-1148"></a>

<p align="center"><kbd><img src="assets/d36e7fa57c6c7e116aa11609a223374157dc6329.png" width="100%"></kbd></p>

> [!NOTE]
> ...> có ghĩa là continue

<br>

<a id="node-1149"></a>

<p align="center"><kbd><img src="assets/0401b4b2866d0d08bc75876db8d52e15aefe425b.png" width="100%"></kbd></p>

> [!NOTE]
> SELECT title FROM people 
> JOIN stars ON people.id = stars.person_id
> JOIN shows ON stars.show_id = shows.id
> WHERE name = 'Steve Carell';
>
> Nó sẽ cho kết quả y như :
> SELECT title FROM shows WHERE id IN
> (SELECT show_id FROM stars WHERE person_id =
> (SELECT id FROM people WHERE name = 'Steve Carell'))

<br>

<a id="node-1150"></a>

<p align="center"><kbd><img src="assets/36f4bddc9ea8738e503757c72b170b49d18c2d0d.png" width="100%"></kbd></p>

<br>

<a id="node-1151"></a>

<p align="center"><kbd><img src="assets/9abdf96e0594c25c895848d09655786de0bb1a5d.png" width="100%"></kbd></p>

<br>

<a id="node-1152"></a>

<p align="center"><kbd><img src="assets/2d5d12cd4fe5327e0fc6d5d00f4935f39e75a026.png" width="100%"></kbd></p>

> [!NOTE]
> Và có thể viết kiểu khác đối với JOIN
>
> SELECT title FROM people, stars, shows
> WHERE people.id = stars.person_id
> AND stars.show_id = shows.id
> AND name = 'Steve Carell';

<br>

<a id="node-1153"></a>

<p align="center"><kbd><img src="assets/8c62720078a49c5d332ea727e1cb3cac83861b02.png" width="100%"></kbd></p>

<br>

<a id="node-1154"></a>

<p align="center"><kbd><img src="assets/79758d5e156998ccd74708fa6ee0b1ab1f23dc46.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói thêm một feature khá hữu ích nữa của sql
> là nôm na là mình cần tìm tên Steve Carel nhưng không 
> nhớ chính xác là Carell hay Carrel...
>
> Thì SELECT * FROM people WHERE name LIKE 'Steve C%'
>
> Có nghĩa là tìm các row trong people sao cho name nó **giống
> như Steve C.....**

<br>

<a id="node-1155"></a>

<p align="center"><kbd><img src="assets/776a9f39a62284aa3daa1ea438bbb3d30f9fd0fc.png" width="100%"></kbd></p>

<br>

<a id="node-1156"></a>

<p align="center"><kbd><img src="assets/d1f3cc9d4e728308940ed440aaed300ee260eaa1.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **indexes** có thể giúp tăng tốc
> quá trình (làm việc với database hơn)

<br>

<a id="node-1157"></a>

<p align="center"><kbd><img src="assets/e586ffd502ae6ccb6e567841a171cfa0b6685472.png" width="100%"></kbd></p>

> [!NOTE]
> Gọi cái này để bật chế độ timer
> để kiểu như ổng muốn show xem
> 1 lệnh mất bao lâu

<br>

<a id="node-1158"></a>

<p align="center"><kbd><img src="assets/40fa6688d97cb8891f7de4baa233228afab604a1.png" width="100%"></kbd></p>

> [!NOTE]
> Ok gọi lệnh SELECT * FROM shows WHER title = 'The Office';
>
> Cho thấy nó chỉ tốn 0.035 giạy

<br>

<a id="node-1159"></a>

<p align="center"><kbd><img src="assets/78fd0a35c56dbc36a86ebbf3e8afef3ba5619fa1.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là bằng cách tạo Index,
> việc search sẽ nhanh hơn

<br>

<a id="node-1160"></a>

<p align="center"><kbd><img src="assets/92f47a9cb0f1de0f334d6cb393ef6697e4795aae.png" width="100%"></kbd></p>

> [!NOTE]
> CREATE INDEX title_index ON shows (title);
>
> -> Nôm na là tạo index cho cột title trong table show

<br>

<a id="node-1161"></a>

<p align="center"><kbd><img src="assets/e34aefc0480cb209a575b84bd272b56f51d406f8.png" width="100%"></kbd></p>

> [!NOTE]
> Cách làm của nó là nó sẽ tạo ra cái này
> B-trees. B không phải là Binary

<br>

<a id="node-1162"></a>

<p align="center"><kbd><img src="assets/0144b4392e277e4a4fc62e371ccae9aa02aa4006.png" width="100%"></kbd></p>

> [!NOTE]
> D: Cái này có vẻ giống Binary Tree
> Nhưng bạn có biết tại sao cái này ko phải là Binary Tree?
>
> A: Vì binary tree thì chỉ chia 2 nhánh/ lần

<br>

<a id="node-1163"></a>

<p align="center"><kbd><img src="assets/1a73e4ce432fc6b4dcc2fcc9e858da32f535898b.png" width="100%"></kbd></p>

> [!NOTE]
> Xong hit enter nó mất nữa giây để tạo index
> nhưng ổng nói nó chỉ tốn lần thôi. Vì từ đây về
> sau nhờ cái này look up data sẽ nhanh hơn

<br>

<a id="node-1164"></a>

<p align="center"><kbd><img src="assets/a4efdabe3ea78b6980056309aebc08102fdefcd9.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, giờ gọi lệnh SELECT * FROM show WHERE
> title = 'The Office'; lại, thì chỉ mất 0.001 giây so
> với 0.0035
>
> Thì đại khái là cái này cho ta một công cụ để search
> nhanh hơn, hiệu qủa hơn những cái mà ta cần search

<br>

<a id="node-1165"></a>

<p align="center"><kbd><img src="assets/da851aebac38aaa2ef25207e3ecd16040dce0227.png" width="100%"></kbd></p>

> [!NOTE]
> D: Nhưng tại sao ta sẽ không muốn index mọi
> column, mọi table để search cho nhanh?
>
> A: Tốn kém resource nào đó. Vì nguyên tắc chung
> là không có gì miễn phí, để search nhanh thì 
> sẽ phải đánh đổi bằng cái gì đó như memory chẳng
> hạn.

<br>

<a id="node-1166"></a>

<p align="center"><kbd><img src="assets/26cd8571c6c1fdd9a3aedf5d2336cadd3a6d5cf9.png" width="100%"></kbd></p>

> [!NOTE]
> Correct, cái này phải nằm ở đâu đó phải ko,
> nên ta sẽ tốn memory / space

<br>

<a id="node-1167"></a>

<p align="center"><kbd><img src="assets/cfd1ab118a36aefcd3fa5b946c08b814531068f7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/cfd1ab118a36aefcd3fa5b946c08b814531068f7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/44bd330ea32f89836096386cfdd62f1a7357e95a.png" width="100%"></kbd></p>

> [!NOTE]
> Ok, giờ qua làm việc với sql nhưng bằng Python
>
> Thì trong khóa học bạn có thể dùng cs50's SQL dù
> rằng ở ngoài đời có thể dùng các lib khác

<br>

<a id="node-1168"></a>

<p align="center"><kbd><img src="assets/45d71e427795d9752df10bef438c71ad5b02526b.png" width="100%"></kbd></p>

> [!NOTE]
> db = SQL("sqlite:///favorites. db") có nghĩa là: **tạo sql
> database từ file datavase favorites.db** là file database chứa
> voting các language và problem set được ưa thích
>
> Và đại khái đây exactly là convention tiêu chuẩn để tạo db như
> mọi thư viện khác thôi vì cs50'SQL cũng làm theo các chuẩn
> thông thường

<br>

<a id="node-1169"></a>

<p align="center"><kbd><img src="assets/5372984c89a98bca5257c1c9acfcfe56cb4f5e28.png" width="100%"></kbd></p>

> [!NOTE]
> Thì để gọi lệnh SQL đơn giản là **tạo string chứa
> câu lệnh** và **gọi nó bằng db.execute()**
> Ta muốn**lấy ra mọi rows** (chứa mọi cột) từ database**show có 
> problem = 'Mario'**
>
> Kết quả nó sẽ **trả ra các rows** mà **problem là Mario**,**mỗi row
> là dictionary key = column name - value**
>
> Sau đó ổng **loop trong các row và lấy Timestamp ra.**

<br>

<a id="node-1170"></a>

<p align="center"><kbd><img src="assets/f5c0ecddf9edcdc8610b4ea94766669542baec42.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự, SELECT COUNT(*)
> AS n FROM favorite WHERE
> problem = 'Mario'; 
>
> Tạo subtable chỉ **1 cột đặt nick name (alias)
> là n**, mang giá trị là **đếm** **số lượng các row**
> với**các row chọn sao cho problem = 'Mario'**
>
> Kết quả trả ra rows với row là dict với key là n
> value là tổng số các row mà problem = 'Mario'
> Đương nhiên nó chỉ có 1 entry, nên lấy ra (rows[0])
> và cũng là dictionary với key là n

<br>

<a id="node-1171"></a>

<p align="center"><kbd><img src="assets/22c951f31d6ff1c58770bc22679b011893e8f383.png" width="100%"></kbd></p>

> [!NOTE]
> **Rows** là **list các dictionary**, trong đó **key là tên cột** mà
> **SELECT** chọn, (nếu *** thì chọn hết**)

<br>

<a id="node-1172"></a>

<p align="center"><kbd><img src="assets/3cd883bcec805fdf5817e36862648fc483b7195b.png" width="100%"></kbd></p>

> [!NOTE]
> Thì câu lệnh trên nếu gọi
> bằng sqlite> thì nó ra vầy

<br>

<a id="node-1173"></a>

<p align="center"><kbd><img src="assets/4f155b1677eb94f256f58aea797f081d90bc7109.png" width="100%"></kbd></p>

> [!NOTE]
> Cái dưới là tôi làm việc với favorites.db**trực tiếp bằng câu
> lệnh sql**, còn ở trên là **thông qua Python library cs50**

<br>

<a id="node-1174"></a>

<p align="center"><kbd><img src="assets/7cd7b745e99fb01f5450699814bb18bb79c9007f.png" width="100%"></kbd></p>

> [!NOTE]
> Và để n**hét user's input** vào câu lệnh sql
> thì ta sẽ **dùng place holder ?**

<br>

<a id="node-1175"></a>

<p align="center"><kbd><img src="assets/ef8b1c75887983ac00869a994496943d369723bb.png" width="100%"></kbd></p>

<br>

<a id="node-1176"></a>

<p align="center"><kbd><img src="assets/ccec3aad8699abb0eb05658221f6eaf39bb46f1f.png" width="100%"></kbd></p>

<br>

<a id="node-1177"></a>

<p align="center"><kbd><img src="assets/215b59b4e25f889ee468d20763749cd51fc92763.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng nói một tình huống có thể xảy ra trong
> thực tế khi Instagram**dùng câu lệnh này để update số
> like của một post**. Và nhiều người **bấm link cùng lúc có
> thể khiến data bị loss**. Nó gọi là **hiện tượng race condition.**

<br>

<a id="node-1178"></a>

<p align="center"><kbd><img src="assets/b2820bf4ccc948d21b29daf434fc0a0db4f8f260.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói về một ví von tương tự là tủ lạnh của phòng trọ.
> 1 ông về thấy trống nên đi mua sữa. Ông thứ 2 về vẫn
> thấy trống nên đi mua sữa tiếp (mà không biết ông kia
> đang đi mua) kết quả là hai ông vác hai bình sữa về thì
> lại không có chỗ để
>
> Thì tương tự như trong đoạn code update số like của
> post câu lệnh đầu chạy xong thì ông thứ nhất giả sử
> đang chuẩn bị update từ 100 like thành 101 like. Thì ông
> thứ 2 chạy lệnh và cũng lấy ra 100 like và chuẩn bị
> update thành 101. Nên kết quả là **2 ông like nhưng chỉ
> có 1 like được ghi nhận**

<br>

<a id="node-1179"></a>

<p align="center"><kbd><img src="assets/4aec15dbe643a155d973f5a1998b31c65b45808c.png" width="100%"></kbd></p>

> [!NOTE]
> Thì giải pháp đối với bài toán tủ lạnh là ông thứ nhất
> đi mua sữa thì dán cái giấy là "tao đang đi mua sữa
> rồi nhé" thì ông thứ hai có thể không đi mua sữa nữa
> mà đi mua mì gói
>
> Hoặc là khi ông thứ 1 đi mua sữa thì ổng **khóa cái tủ lạnh
> lại luôn**

<br>

<a id="node-1180"></a>

<p align="center"><kbd><img src="assets/1bca2b3cde5892755fbb9c2f5bb5113b50ee74f3.png" width="100%"></kbd></p>

<br>

<a id="node-1181"></a>

<p align="center"><kbd><img src="assets/015b5855720b8c1188c2f01a07c277cbd0f47185.png" width="100%"></kbd></p>

> [!NOTE]
> Thì giải pháp đó chính là **TRANSACTION**. Nó **đảm
> bảo, 3 dòng code này được thực hiện 1 lần**
>
> Chứ **không phải cái kiểu người này đang gọi dòng 1
> thì người kia cũng gọi dòng 1**

<br>

<a id="node-1182"></a>

<p align="center"><kbd><img src="assets/4a0991433a1624e67bc80d6c2a4853a6aa53f1fc.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về SQL
> injection attacks

<br>

<a id="node-1183"></a>

<p align="center"><kbd><img src="assets/04cc6df27114bb638eefbbdeed1743129a9160ef.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái trong sql **'--** có nghĩa là**ignore mọi thứ phía sau**
>
> Nên hacker nó có thể dùng kiểu này để hack vào website Nếu ta dùng
> cách gọi lệnh sql bằng  f"SELECT ...WHERE username = {user_name}
> AND password = {password}" như sau

<br>

<a id="node-1184"></a>

<p align="center"><kbd><img src="assets/a5c35720b2d62a86f9a10b09eeac40ff679647c9.png" width="100%"></kbd></p>

> [!NOTE]
> Gọi như này thì an toàn

<br>

<a id="node-1185"></a>

<p align="center"><kbd><img src="assets/1cbcc57aeaa3dc4927d4498ebad5c4c1102bd022.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng nếu gọi
> sql như này

<br>

<a id="node-1186"></a>

<p align="center"><kbd><img src="assets/56783532c68d3deb048ff10e29db0f3b3657b4fc.png" width="100%"></kbd></p>

> [!NOTE]
> Thì khi hacker dùng **malan@harvard.edu'--**
> thì câu lệnh trong sql trở thành ignore mọi thứ phía sau '-- 
> có nghĩa là nó sẽ**không check password nữa**

<br>

<a id="node-1187"></a>

<p align="center"><kbd><img src="assets/c90a3d7b3ffd8004421b5b282efded16473da821.png" width="100%"></kbd></p>

> [!NOTE]
> Và nó sẽ trả ra thông tin hay nói cách khác nó cho log in mà
> không cần password
>
> Ổng cũng nói thêm đây chính là cách mà **adversarial attack**,
> bắt đầu là nó **gõ bậy bạ các kí tự "nguy hiểm"** và**xem thử có
> break cái gì không**, và tuy có thể không vào được nhưng
> nếu có gì đó xảy ra thì hacker có thể **đoán được các điểm
> yếu** mà **tiếp tục thử các phương pháp tấn công khác**

<br>

<a id="node-1188"></a>

<p align="center"><kbd><img src="assets/6ed9a93a06575c4b109c5791c38d7fc71d57fc7e.png" width="100%"></kbd></p>

> [!NOTE]
> Nên làm vầy an toàn hơn

<br>

<a id="node-1189"></a>

<p align="center"><kbd><img src="assets/6c17baebec1f9e647a8d84ac8d0b04fb056be9b0.png" width="100%"></kbd></p>

<br>

<a id="node-1190"></a>

<p align="center"><kbd><img src="assets/3c8c90db7d7af4f2ef899fc08fdd8b147eb07557.png" width="100%"></kbd></p>

<br>

