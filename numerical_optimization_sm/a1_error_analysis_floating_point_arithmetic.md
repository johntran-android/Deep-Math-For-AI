# A.1 Error Analysis & Floating-Point Arithmetic

📊 **Progress:** `5` Notes | `6` Screenshots

---
<a id="node-40"></a>

<p align="center"><kbd><img src="assets/da533dc24f4599600a8e4e03bca492c82aa45bab.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/50738d8049d1b9d29452cc7487134322b2e1e652.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý các algorithm và analysis trong sách này hầu hết đều deal với số thực
> Tuy nhiên thực tế máy tính, nó không tính toán với số thực, mà thật ra tính 
> toán với một một tạp con của R gọi là floating-point numbers.
>
> Mọi con số lưu trữ trên máy tính đều được xấp xỉ bởi một floating point
> number.
>
> Và ta sẽ cố gắng thực hiện các phép tính sao cho sai số là nhỏ nhất.
>
> Nói về ý này, trong CS50 mình đã được học rằng, máy tính lưu trữ thông ở
> dạng nhị phân.
>
> Ví dụ với integer, máy tính assign 4 bytes, tương đương 4*8 = 32 bits.
>
> Nói một cách đơn giản nhất, với 8 bit, mỗi bit mang một trong hai giá trị
> binary: 0 hoặc 1 thì 1 byte = 8 bits ta có thể thể hiện tổng cộng là 256 chuỗi
> nhị phân khác nhau: ứng với các số thập phân từ 0 (=0*2^0 + 0*2^1 + .._0*2^7)
> tới 255 (=1*2^0 + 1*2^1 + ...1*2^7).
>
> Với 4 bytes thì con số này mở rộng lên lớn hơn. Nên đại ý là với số nguyên
> máy tính có thể lưu con số lớn nhất là 1*2^0 + 1*2^1 + ...+ 1*2^31.
>
> Còn với số thập phân, khi khai báo loại float hoặc double. Thì máy sẽ gán
> cho 8 bytes (32 bits) hoặc 16 bytes (64 bits)
>
> Thì loại này nó có cái kiểu là, ta sẽ dùng 1 bit để biểu hiện dấu (âm / dương)
> vài bit cho số mũ,...đại khái là vậy.

<br>

<a id="node-41"></a>

<p align="center"><kbd><img src="assets/50e4887de3df0b951e3e4f588422827cf7989cc1.png" width="100%"></kbd></p>

> [!NOTE]
> Đoạn này gs yêu cầu ta phân biệt giữa sai số tuyệt đối và tương đối. Nếu
> x, x^ là giá trị chính xác và giá trị xấp xỉ với x là scalar, vector hay matrix
> thì sai số tuyệt đối được định nghĩa là norm của x - x^: ||x - x^||
>
> Còn sai số tương đối là tỉ số của cái này với norm x:
>
> ||x - x^|| / ||x||
>
> Và khi sai số tương đổi nhỏ hơn 1 nhiều thì có thể thay mẫu số bởi ||x^||

<br>

<a id="node-42"></a>

<p align="center"><kbd><img src="assets/4e7f3e8463535b04056e7565fd2bbc39af7c9bb0.png" width="100%"></kbd></p>

> [!NOTE]
> Phần này đại khái là gs nhắc lại một kiến thức trong cs, là về cái gọi là double precision arithmetic.
>
> Double, hay double precision có cái tên như vậy là vì trong lịch sử, lúc đầu người ta nghĩ ra cơ chế floating point để
> lưu số thập phân. Và dùng 4 bytes tức 32 bits để lưu trữ. Sau đó, người ta tăng gấp đôi lên, dành 64 bits (8 bytes) để
> lưu. Và do đó trong C, java ta có thể khai báo float hay double để lưu số thập phân (int là cho interger, 4 bytes, long thì
> lưu số lớn hơn, được 8 bytes)
>
> Trong cs50 mình đã biết việc máy tính lưu thông tin ở dạng binary thế nào rồi, nãy đã ôn lại.
>
> Thế thì với số double, với 64 bits, đại khái quy trình lưu một số vào ram sẽ diễn ra như sau:
>
> Quy trình là cho một số thực thập phân, yêu cầu lưu vào máy tính 64 bit
>
> 1) Chuyển phần nguyên thành chuỗi binary: số mũ tăng từ 0 → lên dương khi đi từ phải qua trái
>
> 2) Chuyển phần thập phân thành chuỗi binary: số mũ từ -1 → âm khi đi từ trái qua phải.
>
> 3) Dời dấu phẩy:
>
> Theo chuẩn IEEE: Dời cho đến khi đứng trước dấu phẩy là số 1: có dạng 1.d1d2....d52 (và ta sẽ lưu d1...d52 vào 52
> bit của fractional part)
>
> Ví dụ:
>
> Nếu đang có dạng 1.110 thì khỏi dời, e = 0, d1d2..d52 = 11[--50 số 0--]
>
> Nếu là 0.0101 thì dời qua phải thành 1.01, tính e = -2, d1d2..d52 = 01[--50 số 0--]
>
> Nếu đang là 100.001 thì dời qua trái thành 1.00001, tính e = 2, d1d2..d52 = 00001[--47 số 0--]
>
> Theo Nocedal: Dời cho khi có dạng 0.1d1d2...d52 (và ta cũng sẽ lưu d1...d52 vào ram)
>
> Ví dụ trên:
>
> Nếu đang có dạng 1.110 → dời thành 0.1110, e = 1, d1d2..d52 = 11[-50 số 0--], ⇨ vào ram là chuỗi 11[--50 số 0--] y
> như theo IEEE
>
> Nếu là 0.0101 → dời thành 0.101, e = -1, d1d2...d52 = 01[--50 số 0--] ⇨ lưu vào ram cũng là chuỗi 01[--50 số 0--] y
> như IEEE
>
> Nếu đang là 100.001 → dời thành 0.100001, e = 3, d1d2..d52 = 00001[--47 số 0--] ⇨ lưu vào ram cũng là chuỗi
> 00001[--47 số 0--] y như IEEE
>
> 4) Lưu trữ:
>
> 1 bit cho dấu: 0 là dương, 1 là âm
>
> 52 bit cho chuỗi d1d2...d52 ở trên, như đã thấy, dù dịch dấu phẩy theo kiểu nào thì chuỗi này cũng giống nhau
>
> 11 bit cho số e:  Đầu tiên đem cộng 1023 rồi chuyển thành binary, và lưu vào 11 bit của phần exponent
>
> Mục đích của việc này là để khỏi phải lưu dấu của exponent. Lí do đại khái là vì, phần exponent được cho 11 bits. Với
> 11 bits, thì nó có thể lưu được con số lớn nhất là 2^11-1 = 2, 047 (giống như  với 1 byte = 8 bits thì con số lớn nhất có
> thể lưu là 255 = 2^8-1),
>
> đồng nghĩa là với 11 bits, ta có thể biểu diễn 2^11 con số, gồm 0, 1, 2, ...2047.
>
> Nhưng phải chia làm đôi để cho số âm nữa, nên đại khái là ta sẽ dùng 11 bits này để biểu diễn 1023 con số âm và
> 1023 con số dương
>
> tức là được lngười ta sẽ làm như sau: Lấy 2048 / 2 - 1 = 1,023. Dùng nó làm cái mốc cứng.
>
> Để rồi với một số e đã tính, trước khi chuyển thành binary để lưu vào phần exponent, nó sẽ + cho 1023, khiến cho dù
> e có thể là âm (mà giá trị (âm) lớn nhất có thể có là -1023, thì sau khi cộng 1023 thì sẽ thành không âm:
>
> con số âm bé nhất: -1023 sẽ thành 0
>
> \-1022 sẽ thành 1
>
> \-1 sẽ thành 1022
>
> 0 sẽ thành 1023
>
> 1 sẽ thành 1024
>
> 1023 sẽ thành 2046
>
> Và như vậy máy tính sẽ lưu số e gốc (sau khi tính toán ở bước trên) như sau:
>
> e = -1022, chuyển thành 1, dịch sang binary, và lưu chuỗi 11 bit này: 0000..001
>
> e = 0, chuyển thành 1023, lưu chuỗi 11 bit ứng với số 1023
>
> e = 1023, chuyển thành 2046 và lưu chuỗi 11 bit ứng với 2046.
>
> Khi dịch ngược lại từ ram sang số thực, nó sẽ chuyển thành thập phân và trừ đi 1023 để có lại e.
>
> Nhưng như vậy sẽ còn thừa 2 vị trí (11 bits, như đã nói, có thể represent số từ 0 → 2047 cơ mà trong khi như trên chỉ
> mới xài các con số 1,2,..2046, chưa xài số 0, và 2047:
>
> Có nghĩa là ta còn một chuỗi 11 bits toàn 0: 00....0, một chuỗi 11 bits toàn 1: 11...11.
>
> Thì người ta dùng nó để biểu diễn số 0 tuyệt đối và số vô cực.
>
> \-----
>
> Ok, vậy khi dịch lại từ ram ra số thực:
>
> Trước khi qua phần "dịch lại": Chú ý, vì cách tính e khác nhau, nên giá trị lưu vào máy tính sẽ khác nhau tùy theo
> chuẩn nào (tất nhiên, trong thực tế, ta sẽ chỉ làm theo chuẩn IEEE, nhưng vì ở đây đang nói về cả hai chuẩn, nên phải
> ghi rõ là **GIÁ TRỊ e SẼ KHÁC NHAU**, chỉ chuỗi d1d2..d52 thì đều giống. Và vì sự khác nhau của e, nên tí nữa khi qua
> phần "dịch ra lại" ta sẽ hiểu vì sao nó sẽ ra cùng kết qủa số thực cuối cùng.
>
> i) Lấy giá trị 1 bit của sign, xem nó là 0 hay 1, để biết dấu
>
> ii) Lấy chuỗi binary của 11 bits của exponent, chuyển thành số thập phân. Đem trừ đi 1023 để ra giá trị e_real (trước
> khi + bias 1023)
>
> Cùng với chuỗi binary d1d2...d52 của 52 bit, ta sẽ ráp vào công thức nào dưới đây cũng được:
>
> **Theo chuẩn IEEE**: 
>
> Công thức sẽ là: 
>
> **{1 + [lôi cái chuỗi sau dấy phẩy đã dịch chuyển theo IEEE ra tính với các trọng số 2^-1, 2^-2...,} * 2^e_ieee**
>
> Và vì chuẩn IEEE chuyển dấu phẩy để có 1.d1d2..d52, nên: 
>
> (1 + d1*2^-1 + d2*2^-2 + ...d52*2^-52) 2^e_ieee, 
>
> Viết gọn: **(1 + Σi=1:52 di*2^-i) * 2^e_ieee**
>
> (e này là e được dịch chuyển dấu phẩy theo lối IEEE, ta viết là e_ieee)
>
> **Theo Nocedal**:  
>
> Công thức là: 
>
> **{[lôi cái chuỗi sau dấy phẩy đã dịch chuyển theo IEEE ra tính với các trọng số 2^-1, 2^-2...,]} * 2^e_nocedal**
>
> Nhưng vì chuẩn Nocedal chuyển dấu phẩy thành 0.1d1d2...d52, nên:
>
> (1*2^-1 + d1^2^-2 + d2*2^-3 + ...+ d52*2^-53) * 2^e
>
> Viết gọn: (1*2^-1 + Σi=1:**52** di*2^(-i-1)) * 2^e_nocedal
>
> Và ta hiểu d1d2...mới là thứ lưu trong ram. Nếu gọi f1f2...f53 = 1d1d2..d52 thì cái công thức trên
> sẽ thành (Σi=1:53 fi*2^-i) * 2^e, và công thức này MỚI LÀ CÁI CÔNG THỨC TRONG SÁCH NOCEDAL
> VIẾT LÀ (Σi=1:t di*2^-i) * 2^e với chú thích fractional part là .d1d2...dt
>
> (Nhắc lại, giá trị của e sẽ khác nhau ở hai công thức trên, e_nocedal = e_ieee + 1)
>
> Biến đổi chút ta sẽ ra lại công thức theo IEEE thôi:
>
> (1*2^-1 + Σi=1:52 di*2^(-i-1)) * 2^e_nocedal
>
> = (1*2^-1 + Σi=1:52 di*2^(-i-1)) * 2^(e_ieee + 1)
>
> = (1*2^-1 + Σi=1:52 di*2^(-i-1)) * 2^e_ieee * 2^1
>
> = (1*2^0 + Σi=1:52 di*2^-i) * 2^e_ieee 
>
> = **(1 + Σi=1:52 di*2^-i) * 2^e_ieee → y như công thức trên**
>
> \-----
>
> Câu hỏi 2: Vì sao công thức dịch ngược ra, lại có dạng (...) * 2^e ?
>
> Vì tương tự như 142.3678 = 0.1423678 * 10^3 = 1*10^-1 + 4*10^-2 + 2*10^-3 + ..
>
> Thì chuỗi 1010.1001 = 0.10101001 * 2^4 = (1*2^-1 + 0*2^-2 +1*2^-3 + ..) * 2^3
>
> Và chỗ này phải hiểu vầy:
>
> Trong hệ thập phân, nhân 0.1423678 với 10^3 tức là ta sẽ **dời dấu phẩy sang bên phải** 3 bước để có 142.3678
>
> Thì trong hệ nhị phân, nhân 0.10101001 với 2^4 cũng chính là**dời dấu phẩy sang phải** 4 bước, để có 1010.1001
>
> Nên khi ta thực hiện việc dời 142.3678 dấu phẩy sang bên trái để có dạng 0.1423678 theo kiểu nocedal, ví dụ, đã dời
> 3 bước, thì về bản chất ta đã làm số đó nhỏ đi 10^3 lần, do đó phải nhân với 10^3 để bù lại.
>
> Tương tự, khi dời 1010.1001 thành 0.10101001 thì ta đã làm cho nó nhỏ đi 2^4 lần, nên phải nhân với 2^4 để bù lại.
>
> Như vậy nếu ko làm theo nocedal mà chỉ làm theo IEEE, dời 1010.1001 thành 1.0101001, thì ta chỉ  đã dời 3 bước,
> làm cho nó nhỏ đi 2^3 lần. Do đó phải nhân thêm với chỉ 2^3 để bù lại.
>
> Vậy thì con số 1010.1001 thực chất là = 0.10101001 * 2^4 và cũng bằng 1.0101001 * 2^3 mà thôi.
>
> Và tính toán để chuyển nó ra số thập phân, cũng sẽ ra cùng kết qủa:
>
> 1010.1001 → **1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 + 1*2^-1 + 0*2^-2 + 0*2^-3 + 1*2^-4 +**
>
> Nocedal
>
> 0.10101001 * 2^4  → (1*2^-1 + 0*2^-2 + 1*2^-3 + 0*2^-4 + 1*2^-5 +0*2^-6 + 0*2^-7 + 1*2^-8) * 2^4
>
> (đây cũng chính là (Σi=1:53 di*2^-i) 2^e)
>
> = **1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 + 1*2^-1 +0*2^-2 + 0*2^-3 + 1*2^-4**, cũng y kết quả trên
>
> "IEEE"
>
> 1.0101001 * 2^3 → (1*2^0 + 0*2^-1 + 1*2^-2 + 0*2^-3 + 1*2^-4 + 0*2^-5 + 0*2^-6 + 1*2^-7) * 2^3
>
> (đây cũng chính là (1 + Σi=1:52 di*2^-i) 2^e
>
> = **1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 + 1*2^-1 + 0*2^-2 + 0*2^-3 + 1*2^-4**

<br>

<a id="node-43"></a>

<p align="center"><kbd><img src="assets/1d0d761e34f3485dc074541e10e7cd264ecf5f9a.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, ông nói 2^-t-1 chính là cái gọi là unit round off. kí hiệu là u.
>
> Vì sao?
>
> Là như vầy:
>
> Như vừa biết cái "quy trình" mà máy tính sẽ lưu con số thực nào đó vào 64 bits 
> của ram. 
>
> Chuyển phần nguyên, thập phân thành chuỗi binary. Dời dấu phẩy sang hết
> các chữ số, cũng chính là cho e = tổng số chữ số thập phân của chuỗi binary của
> phần nguyên. Lưu e vào 11 bits của phần exponent theo quy trình: +1023, chuyển
> thành binary. Lưu chuỗi binary của phần thập phân vào phần fractional (52 bits)
> Lưu dấu dương hay âm vào 1 bit còn lại.
>
> Vậy thì ta sẽ thấy thế này, với cái quy tắc khi chuyển phần nguyên và phần thập 
> phân thành chuỗi binary đã nói ở note trước đó là:
>
> Phần nguyên: Cho số mũ đi từ 0 → 1 → 2 ..khi dịch chuyển về bên trái. Ví dụ phần
> nguyên 10.xxx thì 10 sẽ là **1*2^3 + 0*2^2 + 1*2^1 + 0*2^0** (=10), kết quả sẽ là
> chuỗi 1010.
>
> Phần thập phân: Cho số mũ đi từ -1 → -2 →...khi dich dần sang phải. Ví dụ phần
> thập phân là .1234567 (số gốc là 10.1234567) thì cái chuỗi binary sẽ là d1d2...dt
> sao cho u1*2^**-1** + u2*2^**-2**+..+ut*2^**-k = 1234567** (k = t - 4 = 52 - 4)
>
> (Cách tìm chuỗi này thì có cách của nó)
>
> Nhưng cái chính ở đây là:
>
> Ta biết maximum ta chỉ có 52 bits để lưu cái chuỗi binary (của cả phần nguyên và
> phần thập phân sau khi dịch dấu phẩy đi, e = 4), tức là trong ví dụ này, ta sẽ lưu chuỗi
> d1d2...dt = 1010u1u2...uk vào 52 bits này.
>
> Và không khó để hiểu bằng cách đổi cái đổi cái bit cuối cùng (thứ t = 52) từ 0 sang 1,
> thì ta sẽ có được một mức tăng nhỏ nhất có thể mà máy tính lưu được.
>
> Ví dụ ta đang có số 10.1234567, giả sử chuỗi binary của fractional của nó là:
>
> 1010d5d6.....d52 với d52 = 0, 
>
> thì cái số gần nó nhất mà máy tính lưu được là cái số mà chuỗi binary fractional 
> của nó là:
>
> 1010d5d6.....d52 với d52 = 1, giả sử dịch ra thập phân là 10.1234568
>
> Còn bất kì cái số nào khác nằm giữa chúng để ko thể được thể hiện bởi máy tính,
> ví dụ 10.12345671,10.12345672,...10.12345679
>
> Do đó, khoảng cách nhỏ nhất giữa hai số sẽ chính là: cái khoảng tương ứng với
> việc chuyển dt từ 0 sang 1.
>
> Mà như khi làm vậy, thì dịch ra lại thập phân thì chúng sẽ khác nhau phần sau đây:
>
> { [1*2^-1 + 0*2^-2 + 1*2^-3 + 0*2^-4] + [d5*2^-5 + ..+ d47*2^-51 + **0***2^-52] } * 2^e (e = 4)
>
> và 
>
> { [1*2^-1 + 0*2^-2 + 1*2^-3 + 0*2^-4] + [d5*2^-5 + ..+ d47*2^-51 + **1***2^-52] } * 2^e
>
> → Chúng sẽ khác nhau 1 lượng bằng 1*2^-52 * 2^e
>
> Tức là 2^-t * 2^e
>
> Vậy thì sai số lớn nhất sẽ xảy ra khi máy tính cần thể hiện con số nào đó mà nó nằm
> ngay chính giữa hai số liền kề có thể lưu trên máy tính, vì đã nói bất kì con số nào
> nằm giữa đều ko thể thể hiện chính xác, cũng đồng nghĩa là phải làm tròn thành cái
> mốc gần nhất.
>
> Do đó, độ lệch giữa nó và kết quả làm tròn sẽ chính là "nửa quãng đường unit này":
>
> 2^-t * 2^e / 2 = 2^-t-1 * 2^e
>
> Và đây là sai số tuyệt đối, khi tính sai số tương đối, ta sẽ chia cho 2^e để có 2^-t-1
> là sai số tương đối lớn nhất. Gọi là unit roundoff

<br>

<a id="node-44"></a>

<p align="center"><kbd><img src="assets/1df83f2a85b4da18811bb2be25da118f5d974810.png" width="100%"></kbd></p>

> [!NOTE]
> Khi đã hiểu cái unit roundoff, thì cũng hiểu luôn khúc sau, như sau:
>
> Ôn lại nhanh về cách máy tính lưu số thực thập phân vào 64 bit:
>
> 1) Chuyển phần nguyên, phần thập phân thành chuỗi binary, theo quy luật: phần
> nguyên thì đi từ phải qua trái, số mũ tăng dần từ 0 phần thập phân thì đi từ trái qua
> phải, số mũ giảm dần từ -1.
>
> 2) Dời dấu phẩy: Theo chuẩn IEEE: qua phải / trái cho đến khi có dạng 1.xxxx  (ví dụ
> 101.01 → 1.0101, e = 2; 0.00101 → 1.01 e = -3). Tính e là số bước di chuyển (qua
> phải thì âm, qua trái thì dương).
>
> Theo Nocedal: Dời cho đến khi có dạng 0.1xxxx.
>
> (101.01 → 0.10101, e = 3; 0.00101 → 0.101 e = -2)
>
> Có nghĩa là theo e của Nocedal thì e của chuẩn IEEE + 1: e_nocedal = e_ieee + 1
>
> 3) Lưu e: Cộng nó cho 1023, chuyển thành binary, lưu vào 11 bits của exponent. Lưu
> fractional: Lưu chuỗi binary phần nguyên + thập phân vào 52 bit của fractional part
> (d1d2... d52). 1 bit còn lại lưu dấu (0 = dương, 1 = âm)
>
> Khi dịch ra lại:
>
> Dịch chuỗi binary của exponent thành thập phân, trừ đi 1023 để có e.
>
> Theo Nocedal: Tính (Σi=1:53 di*2^-i) * 2^e_nocedal
>
> Theo IEEE: Tính (1 + Σi=1:52 di*2^-i ) * 2^e_ieee
>
> Thực ra hai cái này là một mà thôi, như đã chứng minh ở note trước
>
> \-----
>
> Như vậy, có thể thấy thế này, giả sử ta đối mặt với một con số B nào đó mà khi thực
> hiện bước + 1023 ta ra con số vượt qua 2047. Ví dụ e = 1025 đi, cộng 1023 = 2048.
> Lúc này, khi chuyển sang binary, nó cần 12 bits để thể hiện.
>
> Vì với 11 bits, ta đi từ :
>
> 0 (chuỗi 11 số 0)
>
> tới
>
> 2047 (chuỗi 11 con số 1) = 1*2^10 + 1*2^9 + ...+ 1*2^1 + 1*2^0 = 2047
>
> Để thể hiện được 2048, ta cần chuỗi 1[11 số 0]:
>
> vì khi đó 1*2^11 + Σi=10:0 0*2^i = 2^11 = 2048
>
> (Chú ý, với b bit, con số lớn nhất có thể chỉ là 2^n - 1 = Σi=n-1:0 2^i)
>
> Ví dụ với 8 bit:
>
> 0 = 00000000 = 0
>
> 1 = 00000001 = 1*2^0
>
> ..
>
> 255 = 11111111 = 1*2^7 + 1*2^6 + ...+ 1*2^0
>
> Nên con số lớn nhất với 8 bit là 2^8 - 1 = 255
>
> Để có 256 thì phải là 1 00000000 (2^8 + 0*2^7 + 0*2^6 + ... = 256)
>
> Như vậy, với 11 bit, thì máy tính ko đủ chỗ để lưu e (sau khi cộng 1023) = 2048 và nó
> sẽ báo lỗi.
>
> \-----
>
> Tương tự, nếu con số e quá nhỏ, để khi + 1023, nó vẫn ra âm, ví dụ e = -1024, sau khi
> cộng 1023 ra -1. Thì -1 không thể biểu diễn bởi chuỗi 11 bits → error luôn.
>
> Và thực tế, chỉ cần e mang giá trị mà sau khi cộng 1023 chạm hai cái mốc là 0 hoặc
> 2047, máy tính sẽ trả về 0 hoặc infinity:
>
> e_real = -1023 → e = 0 → trả về 0
>
> e_real = 1024 → e = 2047 → trả về infinity.
>
> Do đó, e phải nằm trong phạm vi **L = -1022 ≤ e_real ≤ U = 1023**
>
> và đây là theo chuẩn IEEE, vì sao ư, là vì cái chuẩn Nocedal chỉ là cái chuẩn lí thuyết
> để phân tích toán học, chứ thực tế, ta sẽ tính e, và lưu e vào ram theo IEEE, tức là
> dời dấu phẩy về dạng 1.d1d2.. chứ ko phải dời thành 0.1d1d2.... 
>
> Vậy theo chuẩn IEEE: L = -1022 ≤ e_real_ieee ≤ U = 1023
>
> Còn theo chuẩn Nocedal thì range sẽ là **-1022 + 1 ≤ e_real_Nocedal ≤ 1023 + 1**
>
> (e_real_nocedal = e_real_IEEE + 1)
>
> Dẫn đến hai con số trong phạm vi cho phép sẽ là,
>
> dịch theo IEEE: (1 + Σi=1:52 di*2^-i) * 2^e_ieee
>
> Thì số lớn nhất được phép:
>
> (1 + Σi=1:52 di*2^-i) * 2^1023
>
> = (1 + Σi=1:52 1*2^-i) * 2^1023 (dĩ nhiên đang xét số lớn nhất nên di = 1 hết)
>
> = [1 + (1/2 + 1/4 + ....+ 2^-52)] * 2^1023
>
> = (1 + 1 - 2^-52) * 2^1023
>
> = (2 - 2^-52) * 2^1023
>
> ≈ **1.79 * 10^308**
>
> Còn số nhỏ nhất được phép:
>
> (1 + Σi=1:52 di*2^-i) * 2^-1022
>
> = (1 + Σi=1:52 0*2^-i) * 2^-1022 (dĩ nhiên đang xét số nhỏ nhất thì di = 0 hết)
>
> = (1 + 0) * 2^-1022
>
> = 2^-1022**≈ 2.2 * 10^-308**
>
> \-----
>
> Hoặc dịch theo Nocedal: 
>
> (Σi=1:53 fi*2^-i) * 2^e_nocedal với f1f2..f53 = 1d1d2...d52
>
> = (1*2^-1 + Σi=2:53 fi*2^-i) * 2^e_nocedal
>
> = (1*2^-1 + Σi=2:53 d_i-1*2^-i) * 2^e_nocedal (d1 = f2, d2 = f3...⇨ di-1 = fi)
>
> = (1*2^-1 + d1*2^-2 + d2*2^-3 + ...d52*2^-53) * 2^e_nocedal
>
> Số lớn nhất được phép: e_nocedal = 1024 và d1,d2,...d52 = 1
>
> = (1*2^-1 + 1*2^-2 + 1*2^-3 + ...1*2^-53) * 2^1024
>
> = (1 + 2^-1 + 2^-2 + ..+ 2^-52) * 2^1023
>
> = (1 + 1/2 + 1/4 + ..+ 2^-52) * 2^1023
>
> = (2 - 2^-52) * 2^1023
>
> **≈ 1.79 * 10^308**
>
> Số nhỏ nhất được phép: e = -1021, d1,d2,...d52 = 0
>
> (1*2^-1 + 0*2^-2 + 0*2^-3 + ...0*2^-53) * 2^-1021
>
> = 2^-1 * 2^-1021
>
> = 2^-1022
>
> **≈ 2.2 * 10^-308 (giống ở trên)
>
> Và đây chính là hai con số 2^L và 2^U nói đến trong sách.**

<br>

