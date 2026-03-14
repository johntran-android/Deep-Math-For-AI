# Week 3 Algorithm

📊 **Progress:** `82` Notes | `143` Screenshots

---
<a id="node-474"></a>

<p align="center"><kbd><img src="assets/0ef2f26890b67e1c6d7810e5a15d152989f9e9be.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nhắc lại cái vụ tìm tên trong phone book bữa trước. Với
> việc tìm từng trang thì số lần phải lật trang là n, cách 2 trang
> thì n/2 (nhưng có thể sai và **cũng vẫn là thời gian tăng
> tuyến tính với n.**
>
> Còn cách **xé đô**i (ví dụ tên chữ A, lật cuốn sách ở giữa,
> thấy tên nó phải thuộc phần nào, xé đôi bỏ phần kia đi rồi lại
> tiếp tục vậy thì chỉ tốn l**og 2 n**. Nếu **double phone book
> lên thì chỉ tốn thêm 1 lần xé đôi**

<br>

<a id="node-475"></a>

<p align="center"><kbd><img src="assets/d534f9d881f1ab5884d4b5aac674ab7caaa6b457.png" width="100%"></kbd></p>

<br>

<a id="node-476"></a>

<p align="center"><kbd><img src="assets/f038f125c32c8dc137e5a26685dc2744c67b819e.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là đây là RAM, mỗi ô là 1 byte như đã viết

<br>

<a id="node-477"></a>

<p align="center"><kbd><img src="assets/432c049482312573349cc2cc483742036fc5af5d.png" width="100%"></kbd></p>

> [!NOTE]
> Và nó chứa các data với các dạng int, double, string,
> char...
>
> Ví dụ có array int như này thì ổng nói đại khái là máy
> tính nó không biết số nào nằm đâu

<br>

<a id="node-478"></a>

<p align="center"><kbd><img src="assets/bb821be1d0a3e0e1a6d1a2830d6dab9864ea88fc.png" width="100%"></kbd></p>

<br>

<a id="node-479"></a>

<p align="center"><kbd><img src="assets/cc6fce8dabae4c9049a12e8e694fca51ba617970.png" width="100%"></kbd></p>

> [!NOTE]
> Mọi bytes như những
> closed box với index

<br>

<a id="node-480"></a>

<p align="center"><kbd><img src="assets/e3ef054e2d758abbff7fe9b1cfe4f9ec97264e08.png" width="100%"></kbd></p>

<br>

<a id="node-481"></a>

<p align="center"><kbd><img src="assets/941918b044bedbc6366d8bf83126aead978ebc13.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta sẽ học cách **search**, như một algorithm
> nào đó**take input là 1 array**, và**output 1 bool value**
> cho biết **có số 50 ở trong đó ko**

<br>

<a id="node-482"></a>

<p align="center"><kbd><img src="assets/e173f0a1199b6bffbaa16186d10d6f5232632be0.png" width="100%"></kbd></p>

<br>

<a id="node-483"></a>

<p align="center"><kbd><img src="assets/180d5d758221877d3ec294267befdb7deea07bf2.png" width="100%"></kbd></p>

> [!NOTE]
> Đầu tiên là thử cái game tìm tờ
> 50$ trong 1 box nào đó.

<br>

<a id="node-484"></a>

<p align="center"><kbd><img src="assets/25b16d3180be183d34c30774490b31a7f43afc01.png" width="100%"></kbd></p>

> [!NOTE]
> Thì với **Linear Search** pseudo code như sau.
> **Cứ đi tìm từng cái thôi**

<br>

<a id="node-485"></a>

<p align="center"><kbd><img src="assets/80cd1a0d51280cb4a2966f3d069ffae6437a4fa8.png" width="100%"></kbd></p>

> [!NOTE]
> D: Xong ổng hỏi nếu sửa lại code như vầy thì, 
> sai chỗ nào?
>
> A: Làm vậy khi nó **không tìm thấy tờ 50$ ở ô thứ nhất**là nó **stop loop và return False ngay**

<br>

<a id="node-486"></a>

<p align="center"><kbd><img src="assets/3b4ab9c5955bccf81056ec73f0e54372a18b1742.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là thay vì**pseudo code hoàn toàn bằng
> English** (ý nói **ngôn ngữ con người**) thì nó có thể
> **cho nó giống với C (hay coding language) hơn xíu**

<br>

<a id="node-487"></a>

<p align="center"><kbd><img src="assets/77581bf58f5e4ec4f787bc8fe360f1a485e15d9c.png" width="100%"></kbd></p>

> [!NOTE]
> Bây giờ **nếu có ai đó đã sort các tờ đô la trong
> các box** theo thứ tự từ nhỏ tới lớn, thì ta có
> thể làm với **binary search**

<br>

<a id="node-488"></a>

<p align="center"><kbd><img src="assets/a53e3b8102aa165da1491b469a595c8e758eba13.png" width="100%"></kbd></p>

> [!NOTE]
> Với cách này có thể bắt đầu bằng cách**mở ô giữa** (hoặc
> gần giữa nếu là số ô chẵn).
>
> Nếu **đúng thì return True**. Nếu **không đúng thì xem nó
> nhỏ hay lớn so với tờ trong ô đó** để suy ra phải **tìm tiếp ở
> các ô bên trái hay phải** và tiếp tục cách làm này trên dãy ít
> ô hơn bên trái hay bên phải này.
>
> Thì ổng hỏi với cách làm này thì có thể có khả năng gì xảy
> ra?
>
> -> Đó là có thể đến một lúc nào đó **ví dụ search dãy có 2 ô**,
> và **chọn 1 ô bên trái thấy nó vẫn lớn hơn 50$** -> **phải tiếp
> tục tương tự tìm  tiếp những ô bên trái nó**. Nhưng đã không
> còn ô nào nữa. Nên lúc này sẽ phải return false để stop

<br>

<a id="node-489"></a>

<p align="center"><kbd><img src="assets/54a5c2716701691d3150a77762fc5f6a1d0e49be.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó phải sửa lại pseudocode **thêm vào
> case không còn ô nào để tìm**

<br>

<a id="node-490"></a>

<p align="center"><kbd><img src="assets/36da736b076e02e1f3accfd93eabc223fdb0217e.png" width="100%"></kbd></p>

<br>

<a id="node-491"></a>

<p align="center"><kbd><img src="assets/1e57e6a00a16aa1a6ab296c3a658cba543271285.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng giải thích lại quá trình với pseudo code:
>
> bắt đầu với **n là số ô**, thì anh này bằng cách nào đó
> tính toán trong đầu ra **vị trí ô ở giữa** (**có thể làm tròn**
> gì đó..) để được middle
>
> Các bước tiếp theo cũng dễ hiểu là nếu ô giữa mang giá
> trị cần tìm thì stop, return true ngay.
>
> Nếu không thì so sánh nếu nó mang số lớn hơn cần tìm
> thì tìm tiếp ở nữa bên trái.
>
> Nếu nó nhỏ hơn số cần tìm thì tìm tiếp ở nửa bên phải
>
> tiếp tục cho đến khi không còn ô nào để tìm thì return (base case)

<br>

<a id="node-492"></a>

<p align="center"><kbd><img src="assets/26c3d05b751b9821494404aa2268321055c8442e.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói **nếu list nhỏ thì linear search cũng không
> sao** nhưng nếu **list lớn hơn** hoặc để thông minh hơn
> thì có thể dùng **binary search.**
> D: Nhưng để làm được binary search phải cần **điều kiện** gì?
>
> A: Cái **list phải được sort**
>
> D: Yes, ta sẽ **phải tính lại việc sort tốn kém thêm bao nhiêu
> bước tính toán**

<br>

<a id="node-493"></a>

<p align="center"><kbd><img src="assets/7ab69d7f33f97f8fbb2514342a9f9415c24034f1.png" width="100%"></kbd></p>

<br>

<a id="node-494"></a>

<p align="center"><kbd><img src="assets/9057dde74eb561dc8b2e6f75748fbfcce3569fd5.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại biểu đồ này, một cái formally nói về hiệu qủa của
> algorithm là "**Running time**". Như **số lần phải lật
> trang** trong **linear search**, **số lần phải xé đôi** trong
> **binary search**
>
> Ổng có nhắc tới một khái niệm mới học trong Algorithm
> Spec là "**Worst case**" ví dụ như cái tên cần tìm là Z
> đứng cuối cuốn phone book gì đó thì số hành động (lật
> trang trong linear search) phải lật là n

<br>

<a id="node-495"></a>

<p align="center"><kbd><img src="assets/b065f412cf78319a1c98e3cd357d3e4f907d48d4.png" width="100%"></kbd></p>

> [!NOTE]
> Giới thiệu khái niệm **Big O notation**. Đại khái là ta sẽ
> **không care chi tiết** - kiểu như hơn thua so đo quá chi
> tiết trong việc tính toán running time của algorithm
> mà chỉ focus vào performance nói chung, nôm na là 
> kiểu như **tập trung và chiến lược chứ không so đó tiểu tiết**

<br>

<a id="node-496"></a>

<p align="center"><kbd><img src="assets/c402d0e6ee3cd3b0398b31fb0d53ca254228eca2.png" width="100%"></kbd></p>

> [!NOTE]
> Với nguyên tắc đó thì **n hay n/2 cũng như nhau**. Và
> **log base 2 hay log base e hay bao nhiêu cũng như
> nhau.**
>
> Nôm na ví dụ như **số n lên tới rất lớn** thì cái việc có
> **chia 2, hay chia 3 cũng không tạo ra khác biệt ở
> cấp chiến lược.**

<br>

<a id="node-497"></a>

<p align="center"><kbd><img src="assets/d4c383afe07cfab24ffdfc414e5278da663d1e80.png" width="100%"></kbd></p>

> [!NOTE]
> Và **ở cấp độ n rất lớn đó**, **chỉ có chiến lược tạo ra khác
> biệt**, thể hiện trong hình các đồ thị khi zoom out thì chỉ
> có khác biệt giữa O(logn) và O(n) chứ các O(n) hay
> O(n/2) không khác biệt mấy

<br>

<a id="node-498"></a>

<p align="center"><kbd><img src="assets/a182eec76de1de8f6799f5b63ffa92b07efa8288.png" width="100%"></kbd></p>

<br>

<a id="node-499"></a>

<p align="center"><kbd><img src="assets/f717858c61f95640dbb67e21cad88d5eb58eafa7.png" width="100%"></kbd></p>

> [!NOTE]
> D: **Linear Search** là O gì?
>
> A: **O(n)**
>
> D: Correct, tuy là mỗi lần nhỏ Stephani làm với một ô nó phải mở ô, lấy
> tờ trong ô đó ra, đọc số, so sánh .. nên **có thể nói là O(3n) hay O(4n)**
> nhưng **ta theo nguyên tắc bỏ qua tiểu tiết sẽ chỉ coi nó là O(n)**
>
> D: Còn cái**Binary Search?**
>
> A: **O(log n)** Chính xác là **log base 2 n**.
>
> Vì với **một số n thì cần chia hai x lần để được 1** (đại khái chiến lược
> của binary search là vậy, **chia hai array (và so sánh với cái ô ở giữa)**
> và chia hai array ..cho đến khi không còn chia hai được nữa (khi array
> chỉ còn 1 ô và return) thì **x chính là log base 2 của n.**Ví dụ trong 8 ô mang giá trị : 1-5$ 2-10$ 3-20$ 4-50$ 5-100$ 6-200$ 7-500$ 8-1000$, cần tìm số 200$:
> Mở ô giữa cho làm tròn là ô 5, thấy số 100$ nhỏ hơn số 200$ cần tìm, nên tìm tiếp ở dãy bên phải [6 7 8]
> Mở ô giữa của dãy bên phải là ô 7 thấy 500$ lớn hơn 200$ nên tìm tiếp bên trái [6]
> Mở ô giữa của dãy [6] tất nhiên là ô 6, thấy! 
>
> Vậy in worst case thì với 8 ô cần 3 lần chia và so sánh. Thì 3 chính là log 2 (8)

<br>

<a id="node-500"></a>

<p align="center"><kbd><img src="assets/733c7beffddf7b272f2f47fb12847f1ebe31372e.png" width="100%"></kbd></p>

> [!NOTE]
> Và những cái này kiểu như tạo thành **Upper Bound** -
> trong trường hợp tệ nhất thì số bước cần thực hiện cũng
> không vượt quá các con số này

<br>

<a id="node-501"></a>

<p align="center"><kbd><img src="assets/c3bb228a376380b522d1a0cbebd957a524e2e802.png" width="100%"></kbd></p>

<br>

<a id="node-502"></a>

<p align="center"><kbd><img src="assets/ec1091b98296e809c26f33e598e693232228c0ac.png" width="100%"></kbd></p>

> [!NOTE]
> Thì có khái niệm Upper Bound thì có **Lower Bound** nữa,
> kí hiệu bằng **Omega**. Là **số bước tính toán tối thiểu có
> thể giúp tìm được**

<br>

<a id="node-503"></a>

<p align="center"><kbd><img src="assets/f632bd7d4a9c5c43a7461278fa77276f59b5d687.png" width="100%"></kbd></p>

> [!NOTE]
> D: Thì trong **Linear Search**, lower bound là bao nhiêu?
>
> A: **Omega (1)** - khi nhỏ đó **hên** mở ra ô đầu tiên của
> array có ngay tờ 50$
>
> D: Correct! Trong binary Search?
>
> Cũng**Omega(1)** khi tờ **50$ nằm ngay ô ở giữa**D: Correct!

<br>

<a id="node-504"></a>

<p align="center"><kbd><img src="assets/1b62a4c27eca65e95961c5c14a5b0921af592529.png" width="100%"></kbd></p>

> [!NOTE]
> **Theta** là notation khi **Upper Bound bằng Lower Bound**
>
> Ví dụ một **algorithm lần lượt đếm số người trong hội
> trường**. Thì đ**ể đếm hết n người thì ít nhất hay nhiều
> nhất cũng phải đếm n lần**

<br>

<a id="node-505"></a>

<p align="center"><kbd><img src="assets/e3d85761c80182c9432bdc3877d001cd59a05fb0.png" width="100%"></kbd></p>

> [!NOTE]
> Một kiểu define mới đó là tạo
> array of int chứa các số này

<br>

<a id="node-506"></a>

<p align="center"><kbd><img src="assets/863c073386218f75f0ddd47d2f26a6abd11a57cb.png" width="100%"></kbd></p>

> [!NOTE]
> Làm thử cái Linear
> Search hồi nãy

<br>

<a id="node-507"></a>

<p align="center"><kbd><img src="assets/483df93891084a93c044174c7b143d6c310fb359.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng **thay bằng string array**và **ask user for a
> string muốn tìm** và sửa lại như vầy. Thì ổng nói cái So
> sánh string kiểu "==" này không work và tuần sau sẽ học
> nhưng cơ bản là vì string là gì?
>
> A: **Array of char**

<br>

<a id="node-508"></a>

<p align="center"><kbd><img src="assets/63a00e0b2ac7dbd86f2df40511f52b713f0f5176.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói dùng **muốn compare string trong C** thì không
> dùng **== được**
>
> Mà quay lại có**<string.h>** trong đó có **strcmp**() giúp,
> trong đó nó sẽ **so sánh các char của hai string  ở các vị trí
> tương ứn**g với nhau. Return **1, 0, hay -1** tuỳ vào việc hai
> char tương ứng đứng trước, sau, hay bằng nhau trong
> alphabet
>
> **0 là bằng nhau**

<br>

<a id="node-509"></a>

<p align="center"><kbd><img src="assets/80cf801e75f8ee89716c22e9b052441067e61244.png" width="100%"></kbd></p>

> [!NOTE]
> Xong thử chạy, thì với "thimble**"** nó Found, nhưng với
> race car - 1 cái không có trong list thì nó ra message:
> **Segmentation fault (core dumped)**

<br>

<a id="node-510"></a>

<p align="center"><kbd><img src="assets/964b6db79386cad982178a7df55e72021eafe95d.png" width="100%"></kbd></p>

> [!NOTE]
> Lý do lỗi này là **vì strings array chỉ có 6 items**, nên **index cao
> nhất của nó chỉ có 5**. Nhưng **loop nó loop tới 6**, nên đây
> tương đương lỗi "**Out of boundary**".. trong java
>
> **Hồi nãy không bị** là do **nó tìm thấy thimble** và**return trước**
> khi nó tới i = 6
>
> Sửa lại cho nó tới i < 6 thôi là hết lỗi

<br>

<a id="node-511"></a>

<p align="center"><kbd><img src="assets/cc77079b3e23ee7c4f25aa202db55853d2c0634b.png" width="100%"></kbd></p>

> [!NOTE]
> Có người hỏi là **cơ bản code vẫn chạy khi không cần return**vậy **return làm gì?**
> D: Ổng bỏ đi return đúng là nó vẫn chạy nhưng nó Found rồi
> lại Not Found. Why?
>
> A: Vì **nhờ có return mà khi tìm được rồi**, **nó exit function**
> nên nó không print dòng cuối nốt found ra

<br>

<a id="node-512"></a>

<p align="center"><kbd><img src="assets/8dc95e5baf559782e11749f094fcbd5064f3faa6.png" width="100%"></kbd></p>

> [!NOTE]
> Và return sẽ là cách để **signify rằng à
> function work as expect** (**return** **0**) hay
> **not as expect (return 1)**

<br>

<a id="node-513"></a>

<p align="center"><kbd><img src="assets/e58de2f781602e5555366043c1122ff731e8a70a.png" width="100%"></kbd></p>

> [!NOTE]
> Như tuần trước có nói có thể xem bằng **echo $?
> và quan trọng là trong tương lai có khi cần
> automatically check / test code thì exit code như
> này rất hữu ích**

<br>

<a id="node-514"></a>

<p align="center"><kbd><img src="assets/0fb514f6eb80392d5682da690b87062d547fbf37.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0fb514f6eb80392d5682da690b87062d547fbf37.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5949f4029711ebaeb2d3d363af7d389b2f9d6bf1.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng làm cái code nhập tên vào và nó search khi match
> name thì nó trả ra số phone. Có vẻ work khá ok nhưng
>
> Question: Có gì sai sai hay không ổn?
>
> A: Thứ nhất là đang dùng**linear search**, không hiệu quả
> khi số data lớn. Thứ hai là giả sử người ta nhập 'carter'
> thay vì 'Carter' nó cũng ko tìm ra.
>
> B: **Hard code số 2** không ổn
>
> C: Lỡ ta **thêm vào một name** mà **quên thêm số phone** 
> thì sẽ sai 
>
> Correct!

<br>

<a id="node-515"></a>

<p align="center"><kbd><img src="assets/15df024813fb12050ee5154e272e33ddbaf71b70.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/15df024813fb12050ee5154e272e33ddbaf71b70.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/01460e40c49717063c3b9b51d32313a099a7f552.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó ổng nói sẽ tốt hơn nếu ta **connect những data liên
> quan với nhau lại** như **1 person** sẽ có name và số phone.
> Từ đó dẫn dắt tới việc define **Model**

<br>

<a id="node-516"></a>

<p align="center"><kbd><img src="assets/3d0c8be2734a88202cbb1018901e95ce76599531.png" width="100%"></kbd></p>

> [!NOTE]
> Đây là cách **define một class** trong C
> **typedef** (type definition) **struct** (structure),
> {variable} name của class

<br>

<a id="node-517"></a>

<p align="center"><kbd><img src="assets/c5941d13d96238c1b302d78ac78ef8f025f33841.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng **define person struct** như vầy, và **tạo array chứa 2 person.**
> Cách thức assign value cho person variable thì biết rồi

<br>

<a id="node-518"></a>

<p align="center"><kbd><img src="assets/a2a48782b2415ccc964b89d1bcaab5f4f4de02c1.png" width="100%"></kbd></p>

<br>

<a id="node-519"></a>

<p align="center"><kbd><img src="assets/78fc1d1fd44b06415b327666f4ffe61bee15b69a.png" width="100%"></kbd></p>

<br>

<a id="node-520"></a>

<p align="center"><kbd><img src="assets/12ea45957af222119c3afbc23f73ab7e8481ba3e.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với cách tạo object như vậy ta sẽ**kiến trúc tốt hơn** là
> 1 array cho name, 1 array cho phone, ....
>
> Và khi cần thêm 1 loại thông tin gì đó thì  chỉ cũng dễ dàng add
> thêm variable cho person
>
> Và ổng nói **chưa phải là Object Oriented Programming, C chưa
> phải là như vậy**

<br>

<a id="node-521"></a>

<p align="center"><kbd><img src="assets/bf9c6357549cb9c4b441a16f70a4a7d3fe1c221b.png" width="100%"></kbd></p>

> [!NOTE]
> Ý nghĩa là: Open the door (memory) and **go inside
> và check or set the name or the number of
> that person**

> [!NOTE]
> Q: Có thể nào **set default value**cho các
> variable của person không
>
> D: **Không. C thì không**, các higher level language
> như Java, Python thì có.
> **Q: Tại sao như vầy là**bad design?
>
> D: Vì**thực tế khi ta load database** (people, phone)
> từ một file database như csv ta sẽ**dùng vài dòng
> code và load toàn bộ vào array** chứ không code 
> trực tiếp như thế này

<br>

<a id="node-522"></a>

<p align="center"><kbd><img src="assets/61bb972bcc13a4f31e26adad73d9ad17ba6e68de.png" width="100%"></kbd></p>

<br>

<a id="node-523"></a>

<p align="center"><kbd><img src="assets/89aba0983fd2fdbce36eaf568465cb34ac60b0df.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5b17fbac6aa4b0e6b5ebcb2b9b1700da407c46f3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/89aba0983fd2fdbce36eaf568465cb34ac60b0df.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5b17fbac6aa4b0e6b5ebcb2b9b1700da407c46f3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3cdd1afcee7103faa7e48a01a1737acce107f6ea.png" width="100%"></kbd></p>

> [!NOTE]
> **Selection Sort**: Rất đơn giản, cho l**oop đến khi sort xong.**
> Pseudo code phiên bản con người:
> David s**ẽ đi từ đầu đến cuối**, và **update vào bộ nhớ ông nào
> là nhỏ nhất**. 
> Khi hoàn thành, ổng sẽ **swap ông nhỏ nhất với ông đứng đầu**
> Tiếp tục David sẽ **đi từ ông thứ 2 đến cuối,** cố gắng **nhớ ông nhỏ 
> nhất**Khi hoàn thành,**swap ông nhỏ nhất với ông thứ 2**
> ..
> Tiếp tục vậy c**ho đến khi chỉ còn một ông nên không loop nữa, 
> kết thúc**

<br>

<a id="node-524"></a>

<p align="center"><kbd><img src="assets/e07adee041a836fab192418fb2334d2a369cd0f3.png" width="100%"></kbd></p>

> [!NOTE]
> Pseudo code cho Selection Sort

<br>

<a id="node-525"></a>

<p align="center"><kbd><img src="assets/97ea9fc64a1283cc67111c6b436a869ceb5e9a7d.png" width="100%"></kbd></p>

> [!NOTE]
> Burble sort:
>
> David sẽ đi từ **từng cặp**, và**swap nếu hai thằng không theo
> thứ tự.**
>
> Thì**khi hoàn thành lần loop thứ nhất** thì **ông số 7 (lớn nhất)
> đã về đúng vị trí cuối.**
> và **làm tương tự thì khi kết thúc lần thứ 2** thì**ông số 6 đã
> đứng đúng vị trí thứ 6**

<br>

<a id="node-526"></a>

<p align="center"><kbd><img src="assets/f4d48477caf9e4bff6397e0b7044b4999d45a7e1.png" width="100%"></kbd></p>

> [!NOTE]
> D: Làm sao máy tính biết mọi chuyện đã xong?
>
> A: Khi **không còn ai để swap**, hoặc nếu mỗi lần loop  ta chỉ
> đi đến vị trí lùi lại 1 ô thì khi đó sẽ đến lúc không cần loop
> nữa
>
> D: Correct, khi loop qua hết (vẫn full list) mà ko thấy cần
> swap ai nữa thì dừng

<br>

<a id="node-527"></a>

<p align="center"><kbd><img src="assets/2223843198f8f1d047b0b30d4c174c64f4353b6b.png" width="100%"></kbd></p>

> [!NOTE]
> D: Thử đoán xem cái nào tốt hơn?
>
> A: Cả hai đều giảm 1 vấn đề sau mỗi lần loop, Nhưng
> với **Bubble rõ ràng là nó phải swap rất nhiều lần  trong
> 1 lần đi**. Còn Selection Sort thì nó nhớ thằng nhỏ nhất
> và **chỉ dùng một lần swap nó lên đầu**. Đây là điểm
> cộng cho Selection Sort
>
> Thứ hai là **quãng đường David phải đi trong Selection
> sort ngắn dần**, còn với Burble sort thì không. Điều này
> có vẻ là Ưu điểm nhưng phải xem liệu Burble sort có
> giảm số lần đi hay không, nếu cùng số lần phải đi thì
> việc đi ngắn hơn là ưu điểm của Selection Sort.

<br>

<a id="node-528"></a>

<p align="center"><kbd><img src="assets/86608df1c3d741419b9d922834165efaf8e8c5ed.png" width="100%"></kbd></p>

<br>

<a id="node-529"></a>

<p align="center"><kbd><img src="assets/844755c72d069cac5563c0d7d4e0d42ada656700.png" width="100%"></kbd></p>

> [!NOTE]
> Để so sánh hai cách ta có thể đếm, xem bao nhiêu lần
> mình phải thực hiện việc so sánh hai số, swap ....
>
> Generalize array có n số.
>
> D: Để **tìm cái số nhỏ nhất ở lần đi đầu tiên** trong
> Selection sort mình cần bao nhiêu step?
>
> A: **Nhiều nhất là n step** vì**worst case là số nhỏ nhất đó
> nó  đứng ở cuối**. Mỗi step sẽ là so sánh số trong ô với số
> nhỏ nhất đang nhớ trong đầu
>
> D: Correct, chính xác hơn là**n-1 step** vì thằng đầu tiên hỏi
> so. Và cũng không cần phải worse case vì để tìm thằng
> nhỏ nhất ta buộc phải loop hết

<br>

<a id="node-530"></a>

<p align="center"><kbd><img src="assets/b740d0964d21d30f869a397bff304e3c3b476669.png" width="100%"></kbd></p>

> [!NOTE]
> D: TÌm số nhỏ thứ 2 thì sao?
>
> A: n-2 step

<br>

<a id="node-531"></a>

<p align="center"><kbd><img src="assets/12ca32c8b45dc7a47c8b25054ed38685368fb314.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó để thực hiện**Selection sort** ta
> sẽ cần **n**2/2 - n/2 bước**

<br>

<a id="node-532"></a>

<p align="center"><kbd><img src="assets/6f5f78122b17e5d69c57a0699c03c651adb8dfa2.png" width="100%"></kbd></p>

> [!NOTE]
> Và thể theo **quy ước không chi li tính toán** mới nói ở
> trên thì  D: Ta coi nó là bao nhiêu?
>
> A: **n^2**

<br>

<a id="node-533"></a>

<p align="center"><kbd><img src="assets/0b31108298fa923d033915e3ffe0806e9a6e04ad.png" width="100%"></kbd></p>

> [!NOTE]
> Correct: **O(n**2)**

<br>

<a id="node-534"></a>

<p align="center"><kbd><img src="assets/83ee923106d6594d34f5c3105796780688e8083b.png" width="100%"></kbd></p>

<br>

<a id="node-535"></a>

<p align="center"><kbd><img src="assets/2abca12aa64b7c95cc352136e41adfa8420a1c83.png" width="100%"></kbd></p>

> [!NOTE]
> D: Vậy **lower bound** là bao nhiêu, ví dụ 1 best
> case khi list đã được sort sẵn?
>
> A: **Vẫn là O(n^2)**. Vì ta vẫn phải đi y như vậy  chỉ
> là không phải thực hiện việc swap thôi.
>
> D: **Correct**! Vì Selection sort không có cơ chế nào
> để quick check rằng list đã được sort

<br>

<a id="node-536"></a>

<p align="center"><kbd><img src="assets/74670a525c076caf161f01add87b4d92566eda61.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó Selection sort vẫn là **Big Omega (n^2)**
>
> Nhận xét. Đây sẽ là sự lãng phí rất lớn

<br>

<a id="node-537"></a>

<p align="center"><kbd><img src="assets/93aa1cbd677621c484c221f92383de15f81face0.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó cũng là **Big Theta n^2** (Upper
> Bound = Lower Bound = n^2)

<br>

<a id="node-538"></a>

<p align="center"><kbd><img src="assets/292c21ae7f0a1fa0459a825c9024c8290856966f.png" width="100%"></kbd></p>

> [!NOTE]
> D: Tại sao phải i từ **0 : n-2** mà ko phải n-1
>
> A: Vì **để lấy từng cặp i và i+1** thì khi i = n-2 thì mới còn ông i+1 =
> n-1 để so sánh.
>
> D: Correct.
>
> Và **chỉ cần làm n times** (không cần check xem có swap hay
> không  để stop như hồi nãy nói) là vì với giả định là**mỗi lần đi
> ổng sẽ đẩy ông to nhất về cuối hay sắp đúng vị trí cho 1 số, thì
> với n số ổng sẽ đủ để xắp sếp đúng vị trí của n số**

<br>

<a id="node-539"></a>

<p align="center"><kbd><img src="assets/1298c41621078b9f80c0d82e13ede164cfdb522e.png" width="100%"></kbd></p>

> [!NOTE]
> Yes, techniquely thì **chỉ cần n-1 lần**, vì khi đã xếp đúng
> cho n-1 ông thì ông còn lại đương nhiên đúng

<br>

<a id="node-540"></a>

<p align="center"><kbd><img src="assets/feba9c1c361aa4f4af257f9a0f7d39c5bf5127e6.png" width="100%"></kbd></p>

> [!NOTE]
> Loop từ 0-1 là 2 vòng, loop từ
> 0-> n-2 là **n-1 vòng.**

<br>

<a id="node-541"></a>

<p align="center"><kbd><img src="assets/5806911be77b3f87eb37b9551bacc5b1ba4c9d59.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy Bubble sort cần **n-1*****n-1**
>
> Asymtoniclly (Khi n lớn) ta cũng coi nó là **O*(n^2)**

<br>

<a id="node-542"></a>

<p align="center"><kbd><img src="assets/97e951e84a412604b41867d3e0991cca21337e20.png" width="100%"></kbd></p>

> [!NOTE]
> D: **Lower bound?**
>
> A: 1. Vì nếu ta check việc swap có xảy ra hay không, và trong
> trường hợp tốt nhất khi list đã sort thì sau khi loop lần đầu tiên
> ta thấy is_swap = false, có thể kết luận list đã sort, và kết thúc
>
> D: Đúng mà sai. Đúng là ta có thể check việc có swap hay không
> để kết thúc.
>
> Sai là vẫn phải đi 1 lần, và trong 1 lần đó **vẫn là so sánh n-1 lần**
>
> Nên **Big OMEGA (n)** (n-1 coi như n)

<br>

<a id="node-543"></a>

<p align="center"><kbd><img src="assets/be293f73044b5cf68bb17b99f76a87d65108464d.png" width="100%"></kbd></p>

<br>

<a id="node-544"></a>

<p align="center"><kbd><img src="assets/d553feb5f73899101bbe03b6571c69ebce56c4fa.png" width="100%"></kbd></p>

<br>

<a id="node-545"></a>

<p align="center"><kbd><img src="assets/8cbfdfedb3d445c9347d135e549aadc3f44e2ba3.png" width="100%"></kbd></p>

<br>

<a id="node-546"></a>

<p align="center"><kbd><img src="assets/bb47a64b7ce8be9782ec341ba71ab4afdcda831e.png" width="100%"></kbd></p>

> [!NOTE]
> Kế ổng dùng 1 cái tool để visualize quá trình sort bởi các
> algorithm khác nhau
>
> Qua đó có thể cảm nhận được có những sự stupid,  lãng phí
> (looping) của các algorithm này

<br>

<a id="node-547"></a>

<p align="center"><kbd><img src="assets/20eaee40ba798a60428f2a9fef0a22a18ea85faf.png" width="100%"></kbd></p>

<br>

<a id="node-548"></a>

<p align="center"><kbd><img src="assets/69d517b8ecd44e86c8bd51be58676b886fd92321.png" width="100%"></kbd></p>

> [!NOTE]
> Khi function gọi chính nó
> thì ta có **recursion**

<br>

<a id="node-549"></a>

<p align="center"><kbd><img src="assets/a507affc83236680bd8c6e97e608d58fc41ebb25.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói cái pseudo code cho cái task tìm tở 50$ ở
> trên chính là Recursive khi nó có khúc**search left haft
> và right haft = gọi chính nó**
>
> Từ đây có lo ngại sẽ có vấn đề khi  function gọi chính nó
> nhiều lần.
>
> D: Tại sao không cần lo việc này?
>
> A: Vì **nó có dòng nếu ko còn doors nào nữa thì stop 
> (return false)**

<br>

<a id="node-550"></a>

<p align="center"><kbd><img src="assets/f7186f684073930c27253f393dafc3c501c50ce5.png" width="100%"></kbd></p>

> [!NOTE]
> Correct, và quan trọng hơn nữa là **mỗi lần recursive
> thì nó gọi trên một smaller smaller problem**
>
> Thì **đến lúc nào đó sẽ dừng**

<br>

<a id="node-551"></a>

<p align="center"><kbd><img src="assets/ebc74ae071d988549b9dec0b933ff2008df42bee.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại ví dụ search name trong phone book ta cũng
> có thể thay **Hành động mở trang giữa của phần bên
> trái và làm lại từ dòng 3** Thành **Search phần bên
> trái.**
>
> Ý là **thể hiện cách làm theo kiểu recursive** vì thật ra nó
> cũng là như nhau

<br>

<a id="node-552"></a>

<p align="center"><kbd><img src="assets/520913561c5912d3e5b4a9d52dd640ef4918282c.png" width="100%"></kbd></p>

<br>

<a id="node-553"></a>

<p align="center"><kbd><img src="assets/cabbc0a176503b358fd1f5d73eec4dee7235f844.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là ngay cả việc xây cái kim tự tháp này 
> Cũng có thể thể hiện dạng recursive.
>
> Type 4 pyramid = base 4 block + type 3 pyramid
> Type 3 pyramid = base 3 block + type 2 pyramid
> Type 2 pyramid = base 2 block + type 1 pyramid
> Type 1 pyramid = base 1 block

<br>

<a id="node-554"></a>

<p align="center"><kbd><img src="assets/f8c1490a6b7645c2376fe90463a81f3a50f9fedd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f8c1490a6b7645c2376fe90463a81f3a50f9fedd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2fb0e151eaabd69d2b48550052c9d369abb8fe97.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ổng v**iết đoạn code để in kim tự tháp**
> theo cách thông thường như tuần trước

<br>

<a id="node-555"></a>

<p align="center"><kbd><img src="assets/5718cf9ed7cb06f3bb98b60bca0f2758d1f282df.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5718cf9ed7cb06f3bb98b60bca0f2758d1f282df.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/05fd45f79918b048cc5ba79c1603244f43a3329e.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng viết theo kiểu này, trong function
> **draw(n)**nó**tự động gọi draw(n+1)**

<br>

<a id="node-556"></a>

<p align="center"><kbd><img src="assets/86809fbc5dd0b5358a9aefa4d40854a122c6624d.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả là sau khi **draw(1)**, trong function đó sau khi thực
> hiện xong nó tự động gọi **draw(2)....**
>
> Kết qủa ta có kim tự tháp với 1 block ở hàng 1, 2 block hàng 2
> ....
>
> Ổng nói cái này để minh hoạ thôi vì thực ra ổng**override
> cái gì đó của Clang giúp compile được** chứ Clang nó có
> cơ chế prevent cái này để tránh tràn bộ nhớ.

<br>

<a id="node-557"></a>

<p align="center"><kbd><img src="assets/737ae4c0d4b904dac74ef17c9edecd84c2bc866b.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng sửa lại kiểu này. Vì **kim tự tháp 4 tầng** cơ bản là
> một cái **kim tự tháp 3 tầng** + **1 dòng 4 block**.
>
> Nên trong function ổng sẽ cho nó **vẽ n-1 pyramid trước**,
> và assume nó sẽ work as expected
>
> Sau đó ổng **vẽ dòng n block.**

<br>

<a id="node-558"></a>

<p align="center"><kbd><img src="assets/46c957e38c121296f533b193bc840cace765369c.png" width="100%"></kbd></p>

> [!NOTE]
> D: Có gì không ổn?
>
> A: Đó là **khi n = 1 nó sẽ gọi function để vẽ kim tự tháp 0,
> và in 1 block.
>
> và tiếp tục gọi draw -1 , -2 ....**

<br>

<a id="node-559"></a>

<p align="center"><kbd><img src="assets/653de9e0e89d9bd53f237e487e9657fb45793fa4.png" width="100%"></kbd></p>

<br>

<a id="node-560"></a>

<p align="center"><kbd><img src="assets/c8e4cb14882f87eb2c0709c2c2d215dc5aacece9.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó, ổng**define BASE CASE**là khi **n <= 0 thì return.**
> Câu chuyện sẽ là như thế này, bắt đầu gọi draw(4) để in type 4 pyramid:
>
> draw (4): n = 4 > 0 nên nó gọi draw(3), dòng dưới (tạm gọi là base 4) 
> vẫn chưa chạy
>
> draw(3): n = 3 > 0 nên nó gọi draw(2), dòng base 3 vẫn chưa chạy
>
> draw(2): n = 2 > 0 nên nó gọi draw(1), dòng base 2 vẫn chưa chạy
>
> draw(1): n = 1 > 0 nên nó gọi draw(0), dòng base 1 vẫn chưa chạy
>
> draw(0): n = 0, thoả điều kiện, nó return. 
>
> Chạy dòng base 1, in 1 block. Kết thúc draw(1)
>
> Chạy dòng base 2, in 2 block, Kết thúc draw(2)
>
> Chạy dòng base 3, in 3 block, kết thúc draw(3)
>
> Chạy dòng base 4, in 4 block, kết thúc draw(4) -> Kết thúc function.

<br>

<a id="node-561"></a>

<p align="center"><kbd><img src="assets/d764809e13139bd81934ac0c55494182b12a6515.png" width="100%"></kbd></p>

<br>

<a id="node-562"></a>

<p align="center"><kbd><img src="assets/b4afdf61de24462c5d667283a353c09956d420d4.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Có thể dùng recursive với void function không -
> function ko có argument?
>
> D: Không

<br>

<a id="node-563"></a>

<p align="center"><kbd><img src="assets/5ada3965382f0b289f426fc319bcb0b47532ab8f.png" width="100%"></kbd></p>

<br>

<a id="node-564"></a>

<p align="center"><kbd><img src="assets/e811aa5e25120adefbef1d3c2d19ee150a03121f.png" width="100%"></kbd></p>

> [!NOTE]
> Nói qua cái Merge Sort mới
> học bên Algorithm Spec,

<br>

<a id="node-565"></a>

<p align="center"><kbd><img src="assets/e4fa2b73c0cca315a2226125a9d7046660a6c245.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8fc136be091722dea54515fc95bb20b873703de8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e4fa2b73c0cca315a2226125a9d7046660a6c245.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8fc136be091722dea54515fc95bb20b873703de8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4f512e2cf3d40ac7fd45e75103528d6a2a6bf480.png" width="100%"></kbd></p>

<br>

<a id="node-566"></a>

<p align="center"><kbd><img src="assets/7bf98130174425263b4bccc34f98ac36b47f062a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e10a7ad7bb290da739db31e739e96d0f84fa6585.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7bf98130174425263b4bccc34f98ac36b47f062a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e10a7ad7bb290da739db31e739e96d0f84fa6585.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/63f88dc360d4a4f745041c1d1d5032ab0495486a.png" width="100%"></kbd></p>

<br>

<a id="node-567"></a>

<p align="center"><kbd><img src="assets/516130bc567d1d05e706edd8a110fd8f77d03cfd.png" width="100%"></kbd></p>

> [!NOTE]
> Có thể hiểu đại khái như sau:
>
> Pseudo code con người của quá trình merge như sau:
>
> Start với số đầu tiên của 2 array. 2 và 0
>
> So sánh thấy 0 nhỏ hơn, lấy 0 ra bỏ vào kết quả.
>
> Dựng thằng tiếp theo của array #2 lên là số 1.
>
> So sánh 2 và 1 thấy 1 nhỏ, lấy nó ra bỏ vào kết quả.
>
>  Dựng thằng tiếp theo của array #2 lên, là số 3
>
> So sánh 2 và 3 thấy 2 nhỏ, lấy nó ra bỏ vào kết quả
>
> (Đến giờ vì mới lấy 2 là của array #1 ra, nên ta dựng
> thằng tiếp theo của array 1 lên, là số 4)
>
> So 4 với 3 thấy 3 nhỏ, lấy nó ra bỏ vào kết quả
>
> Dựng thằng tiếp theo của array #2 ra
>
> Tiếp tục như vậy.
>
> *Thì ổng nói các bạn **thấy tay của tôi luôn chỉ về tương lai,
> không có bước quay lại nào cả.**

<br>

<a id="node-568"></a>

<p align="center"><kbd><img src="assets/3f160aa36d69abb0a7684a90dc4ecb43f450280d.png" width="100%"></kbd></p>

<br>

<a id="node-569"></a>

<p align="center"><kbd><img src="assets/df513e7e8f34ed230d166968c57da0fd4ce4e903.png" width="100%"></kbd></p>

> [!NOTE]
> D: làm sao để sort 1st left?
>
> A: Thì gọi chính function đó, và nó theo pseudo code sẽ 
>
> Sort 1st left của 7254 = 72 (1)
> Sort 2nd left của 7254 = 54 (2)
> Merge (3)
>
> Sort 72: (1)
> Sort 1st left của 72 = 7: Done (1a)
> Sort 2nd left của 72 = 2: Done (1b)
> Merge -> 27 (1c)
>
> Sort 54: (2)
> Sort 1st left của 54 = 5 -> 5 Done (2a)
> Sort 2nd left của 54 = 4 -> 4 Done (2b)
> Merge -> 45 (2c)
>
> Merge (3)
> -> 2457

<br>

<a id="node-570"></a>

<p align="center"><kbd><img src="assets/e03eeed7a1c13e5dcf556eb94213614e141c1c10.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/112893efc7eca18d8013883991b966100ee5c28c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0be3c2a911870e4e16efb0f163dc7ce2ab8dfd14.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/cd3dceb8f2bec71a29c1d1dc2ce5c102deed10ea.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e03eeed7a1c13e5dcf556eb94213614e141c1c10.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/112893efc7eca18d8013883991b966100ee5c28c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0be3c2a911870e4e16efb0f163dc7ce2ab8dfd14.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/cd3dceb8f2bec71a29c1d1dc2ce5c102deed10ea.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b4ebae6b5f6d8812b541fd21b1212451557e30a2.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự

<br>

<a id="node-571"></a>

<p align="center"><kbd><img src="assets/ef55b57bc22e1a6d25145ac6219cb569ca5c2a8f.png" width="100%"></kbd></p>

> [!NOTE]
> Bước merge cuối

<br>

<a id="node-572"></a>

<p align="center"><kbd><img src="assets/7843d86d5f46d29f2bd676858923637d298eb96c.png" width="100%"></kbd></p>

<br>

<a id="node-573"></a>

<p align="center"><kbd><img src="assets/68e952be9bd97de25e88bd055cde510ef9db2ddd.png" width="100%"></kbd></p>

<br>

<a id="node-574"></a>

<p align="center"><kbd><img src="assets/2cf831e65f1cb8cf9831ce034ba418a25486414a.png" width="100%"></kbd></p>

> [!NOTE]
> D: Phải divide một nửa bao nhiêu lần?
>
> A: 3 từ 8 -> 4 -> 2 -> 1
>
> D: Correct! 
> Từ 8 để được 1 cần 3 lần chia 2 
> Thì ngược lại từ 1 cần nhân 2 3 lần để được 8
> 1x2 = 2
> 2x2 = 3
> 4x2 = 8
> Thì 3 chính là**log 2 (8)**= log 2 (2^3)
> Và khái quát hoá, **từ dãy n số**để được 1 thì **cần log 2 (n)**lần chia
>
> Và theo nguyên tắc bỏ qua tiểu tiết đó là ko care base 2 hay 3 
> hay 10 hay e. Thì nó sẽ là **log(n) phép tính**

<br>

<a id="node-575"></a>

<p align="center"><kbd><img src="assets/e9891674a181a0f5e35989f30184ac703dcc4812.png" width="100%"></kbd></p>

> [!NOTE]
> Như hồi nãy có nói mỗi lần ổng merge, ổng chỉ
> đụng mỗi con số 1 lần duy nhất chứ không hề có
> chuyện loop đi loop lại nhiều lần
>
> Và mỗi một "tầng" khi merge ổng chỉ "đụng" / thao
> tác mỗi số 1 lần
>
> Cho nên **mỗi 1 "tầng" (trong 3 tầng*) ổng chỉ thực hiện n
> động tác.**
>
> tầng 1 merge các cặp (1 số,1 số) 
>
> tầng 2 merge các cặp (2 số, 2 số)
>
> tầng 3 merge cặp (4 số, 4 số)

<br>

<a id="node-576"></a>

<p align="center"><kbd><img src="assets/efca71edc86a528d528afe0519650c87713af191.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy với log(n) lần chia để được **log(n) tầng**, mỗi tầng thao
> tác n lần nên tổng cộng cần **n*log(n) -> O(nlog(n))**

<br>

<a id="node-577"></a>

<p align="center"><kbd><img src="assets/1f9abc5f08656b4ae332537ebdc2e6b65b165d89.png" width="100%"></kbd></p>

<br>

<a id="node-578"></a>

<p align="center"><kbd><img src="assets/df7b40abc3169b213e7214772e99e5693d74b79d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là cái Merge Sort có O(nlogn) tuy nhanh hơn Selection
> Sort và Bubble Sort (đều O(n^2)) nhưng chậm hơn Linear Search
> = O(n)
>
> Do đó khi **tính cả việc Sort  sau đó mới Binary Search**(như đã
> học, **Binary Search sẽ nhanh hơn Linear Search nếu sort sẵn**)
> thì chưa chắc Binary Search sẽ ưu thế hơn.
>
> Tuy nhiên n**ếu sort 1 lần**, và **xài mãi mãi**, thì nó cách chắc chắn
> sẽ ưu thế hơn (giống như nôm na là**Google giúp sort thông tin
> 1 lần sẵn, và từ đó hàng triệu người được hưởng lợi**)

<br>

<a id="node-579"></a>

<p align="center"><kbd><img src="assets/3bf46407aabd86f6d4b4a937b938942d8819ec28.png" width="100%"></kbd></p>

> [!NOTE]
> Và merge sort cũng có
> lower bound là nlogn

<br>

<a id="node-580"></a>

<p align="center"><kbd><img src="assets/187313237e58588e30ed545e41d6a921a7511439.png" width="100%"></kbd></p>

<br>

<a id="node-581"></a>

<p align="center"><kbd><img src="assets/edcf32e4eb0375852ec3e1812f30bd92b4cb54a5.png" width="100%"></kbd></p>

<br>

<a id="node-582"></a>

<p align="center"><kbd><img src="assets/0af1903f3efa80da193196035467964643a236be.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ngoài cân nhắc thời gian của một
> algorithm thì  còn phải cân nhắc **Space**. Nữa.
> Nôm na là để thực hiện hết các bước của Merge
> Sort hồi nãy thì ổng cần có những cái khoảng
> không gian để thực hiện

<br>

<a id="node-583"></a>

<p align="center"><kbd><img src="assets/83ef553f0ed4a97a7ad43586602596375e247c56.png" width="100%"></kbd></p>

<br>

<a id="node-584"></a>

<p align="center"><kbd><img src="assets/705489c1dae33f2dda8a826f29fc52716ce13d4a.png" width="100%"></kbd></p>

<br>

<a id="node-585"></a>

<p align="center"><kbd><img src="assets/984eefa7d2175d1df62f747be8a5ed7a5dcba0ce.png" width="100%"></kbd></p>

> [!NOTE]
> Nhìn trực quan có thể thấy Merge
> Sort vượt trội như thế nào

<br>

<a id="node-586"></a>

<p align="center"><kbd><img src="assets/87aeab455283b905d3fdb0a61042f7c4422256e3.png" width="100%"></kbd></p>

<br>

<a id="node-587"></a>

<p align="center"><kbd><img src="assets/9810dd6c9e757fd1a08ac05f375aff2076623579.png" width="100%"></kbd></p>

<br>

<a id="node-588"></a>

<p align="center"><kbd><img src="assets/91b958ac154eaad42f74bca296e2da0cb0f6b3b7.png" width="100%"></kbd></p>

<br>

