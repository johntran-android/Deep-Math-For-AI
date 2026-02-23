# Lecture 18: Properties Of Determinants

📊 **Progress:** `37` Notes | `41` Screenshots

---
<a id="node-570"></a>

<p align="center"><kbd><img src="assets/b8a491b951e6c9bfcdf5bbae29ef6458cb14da4c.png" width="100%"></kbd></p>

> [!NOTE]
> mở đầu gs nói rằng ta sẽ thảo luận một phần quan trọng
> tiếp theo, trong đó ta sẽ làm việc với **square** matrix, để bàn
> tới **determinant** và **eigenvalues.
>
> Có nghĩa là, determinant và eigenvectors và eigenvalues
> chỉ apply với square matrix**

<br>

<a id="node-571"></a>

<p align="center"><kbd><img src="assets/437f09ff965ec35a730b93e0eb2ffe439b87b77f.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì MỌI **SQUARE** MATRIX SẼ ĐỀU CÓ MỘT
> CON SỐ GẮN VỚI NÓ `-` **DETERMINANTS**

<br>

<a id="node-572"></a>

<p align="center"><kbd><img src="assets/aab1195cff7f7f61c92f28b667a65270b5694513.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: con số này tuy **không thể chứa mọi thông tin** của matrix
> nhưng nó CÓ KHẢ NĂNG**CHO BIẾT TÍNH INVERTIBILITY**
> CỦA MATRIX
>
> **DETERMINANT KHÁC 0, MATRIX NONSINGULAR 
> `/` INVERTIBLE**
>
> **DETERMINANT BẰNG 0, MATRIX SINGULAR**
> `(NON-INVERTIBLE)`

<br>

<a id="node-573"></a>

<p align="center"><kbd><img src="assets/252fc64f2710c5db3149c41ab63660e6886250fd.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói rằng ta sẽ không học ngay công thức của
> determinant.
>
> Mà sẽ làm quen với nó qua **3 tính chất đầu tiên**của nó.
> Trong đó **det I `=` 1** là tính chất thứ nhất. Và qua tính chất
> thứ 2 và 3, ta sẽ biết về determinant

> [!NOTE]
> Property #1: Det I `=` 1

<br>

<a id="node-574"></a>

<p align="center"><kbd><img src="assets/3ba1178e486a54125e1f55f52dd8965d5a3597ce.png" width="100%"></kbd></p>

> [!NOTE]
> Và tính chất thứ 2 đó là, nếu ta**đổi chỗ hai row,
> determinant sẽ bị chuyển dấu**

> [!NOTE]
> Property #2: đổi chỗ hai row,
> determinant sẽ bị chuyển dấu

<br>

<a id="node-575"></a>

<p align="center"><kbd><img src="assets/3a10542a2eb17a3dc4724e3688f8d5c5e2ea8e35.png" width="100%"></kbd></p>

> [!NOTE]
> Gs hỏi rằng, với hai tính chất này, thì ta có thể tính được
> determinant của matrix nào?
>
> Me: Đó là **permutation** matrix, bởi nó chỉ là matrix có
> được khi ta**exchange row từ identity matrix**, và ta đã
> biết **det I `=` 1**

<br>

<a id="node-576"></a>

<p align="center"><kbd><img src="assets/f800b9173cc253e076f57b8b022f54aaa0f8109c.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: correct. Từ hai tính chất này ta biết được det của
> permutation matrix, **sẽ là 1 hoặc `-1` tùy theo số lần
> exchange là chẵn hay lẻ.**
>
> Cái này cũng dễ hiểu thôi, **khi đổi chỗ một cặp row thì
> det sẽ đổi dấu**. Vậy nếu exchange 2 lần thì det sẽ về lại
> giá trị cũ
>
> Vậy nếu exchange số chẵn lần thì det bằng 1, còn số lẻ
> thì det `=` `-1`

<br>

<a id="node-577"></a>

<p align="center"><kbd><img src="assets/c51439a3b704cc8f3b784703d7787adf8b2de245.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ như này, nhờ hai property ta biết det của
> chúng. Chú ý cách ghi det là **det A** hoặc **|A|**

<br>

<a id="node-578"></a>

<p align="center"><kbd><img src="assets/b9f31b9ee2ba5111ccfe518cadac29e63e2ed546.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói về công thức**tính det của matrix (2, 2)** và ông
> cho rằng ta sẽ dùng nó làm **cơ sở để tính det của
> matrix (n, n)**

<br>

<a id="node-579"></a>

<p align="center"><kbd><img src="assets/1ad8f7a53374cd275ac68c8db4bc66a3d92fc12d.png" width="100%"></kbd></p>

> [!NOTE]
> Và **property thứ #3** là property mấu chốt. Ta sẽ có hai phần.
>
> 3a: Khi**nhân một row** (row bất kì, nhưng ví dụ là row đầu)
> của A cho t, và **các row còn lại giữ nguyên** thì determinant
> sẽ là gì?
>
> Thì nó sẽ bằng **t * det(A)**

> [!NOTE]
> Property #3a: Khi nhân một row (row bất kì, nhưng ví dụ là
> row đầu) của A cho t, và các row còn lại giữ nguyên thì
> determinant `=` t*det(A)

<br>

<a id="node-580"></a>

<p align="center"><kbd><img src="assets/88502ad0376f2ffa64c0bc0ee795ec1b54660b7b.png" width="100%"></kbd></p>

> [!NOTE]
> Và 3b là khi ta **xét một row**, **các row còn lại giữ nguyên**
> thì det của matrix `=` **tổng det của hai matrix** trong đó
> với row 1 matrix A1 `+` row 1 của matrix A2 `=` row 1 của
> matrix A, các row khác giữ nguyên.

<br>

<a id="node-581"></a>

<p align="center"><kbd><img src="assets/4c833824323b314141160e05309a67057b7cee52.png" width="100%"></kbd></p>

<br>

<a id="node-582"></a>

<p align="center"><kbd><img src="assets/13887131d8396be8c2b2ad48b264133506dd46e5.png" width="100%"></kbd></p>

> [!NOTE]
> Tức là, gs nhấn mạnh rằng determinant có tính chất
> **tuyến tính trong mỗi row**.
>
> ```text
> Không phải là det(A+B) = det A + det B mà là det A + det
> ```
> B nhưng **chỉ cộng hai hàng nào đó thôi**, ví dụ hàng số 2
> đi, để có matrix C (hàng 2 của C `=` tổng hàng 2 của A, B)
> thì khi đó det A `+` det B `=` det C

<br>

<a id="node-583"></a>

<p align="center"><kbd><img src="assets/bb0001737fdfa96d8547737959d2c111e3af8a4d.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi của thầy là, dựa vào properties 1,2,3 giải thích tại
> sao lại có tính chất 4: khi **hai hàng giống nhau thì det `=` 0**
>
> Me: Từ property 2 ta biết khi **switch row thì det đổi dấu**.
> Thế thì nếu hai hàng giống nhau, đổi chỗ thì cơ bản là  ta
> theo đó ta có hai matrix có det khác dấu. det A `=` `-` det B
> Tuy nhiên vì hai hàng giống nhau nên B vẫn là A, ta có
> det A `=` `-` det A Và điều này cho ta **det A `=` 0.**

<br>

<a id="node-584"></a>

<p align="center"><kbd><img src="assets/106c14ebdc9919e2214c29dd277901232233e6e4.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: Correct
>
> Và ta cũng có thể nghĩ theo cách nghĩ rằng, **matrix có hai
> row giống nhau thì đương nhiên sẽ sẽ có dependent row**,
> khiến nó**không thể full row rank** (và đang nói về square
> matrix nên nó **không thể full rank `->` không invertible**. Và
> như lúc nãy nói, **non-invertible matrix sẽ có det `=` 0**

<br>

<a id="node-585"></a>

<p align="center"><kbd><img src="assets/30143a1d60ac9201dbd47e8184147856a957d019.png" width="100%"></kbd></p>

> [!NOTE]
> tính chất thứ 5 là khi ta **trừ một hàng cho [scalar * một
> hàng khác]**thì **det không đổi**
>
> Gs nhắc ta nhớ rằng đây là "hành động" quen thuộc ta hay
> làm khi thực hiện elimination đưa A về U.
>
> Chính vì vậy mà **det A `=` det U:**hay quá trình **elimination**
> **không làm thay đổi determinant**. Tuy nhiên trong quá trình
> có thể cần **dùng đến row exchange, thành ra det có thể
> đổi dấu.**

<br>

<a id="node-586"></a>

<p align="center"><kbd><img src="assets/879f29a47b6443b4198b6f160e52b0f8d00e8c60.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/879f29a47b6443b4198b6f160e52b0f8d00e8c60.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fb075e0a2ec3acf6346775ad7fa7664f863d7021.png" width="100%"></kbd></p>

> [!NOTE]
> gs lấy ví dụ, cho matrix A, và ta sẽ trừ row 2 cho 2 * row 1
> thì det vẫn bằng nhau
>
> Giải thích vì sao lại vậy:
>
> Dùng property 3b để có det của matrix này bằng tổng det của 
> A và det của matrix A2 (có hàng 2 là `[-t*a` `-t*a])`
>
> Tiếp dựa vào property 3b để tách t ra. Tức det A2 `=` `-t*det` B2
>
> Và B2 có hai hàng bằng nhau nên theo properties 4, det nó
> bằng 0.
>
> Vậy **det của matrix không đổi** khi **trừ một row cho t*row 
> khác**

<br>

<a id="node-587"></a>

<p align="center"><kbd><img src="assets/5841ccf540f0e579d1c4775e2f64dbc8b17b5294.png" width="100%"></kbd></p>

<br>

<a id="node-588"></a>

<p align="center"><kbd><img src="assets/a761c7fdf01237eef93db159261bac734950d425.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 19: DETERMINANT FORMULAS AND COFACTORS](untitled.md#node-610)

> [!NOTE]
> Property thứ 6 là **nếu matrix có row `=` 0 thì det `=` 0**.
>
> Thế thì gs cho rằng ta có thể dễ hiểu ngay properties này vì **row
> `=` 0 tức là nó chính là một row dependent** (vì nó `=` một row khác
> * 0). Thành ra matrix **không thể full rank**, do đó cũng `non-invertible` 
> `->` **det `=` 0**
>
> Thế nhưng để giải thích nó từ các properties trước đó ta sẽ giải
> thích thế nào?
>
> Me: Ta có thể giải thích như sau:
>
> giả sử matrix 3x2 với row 3 `=` [0 0]. Thì ta có thể cho  row 3 `=`
> ```text
> tổng của hai row vector nào đó. ví dụ [0 0 ] = [-1 -1] + [1 1]
> ```
>
> Khi đó dựa vào 3b ta sẽ có det A `=` det B `+` det C (với B là matrix
> A nhưng row 3 là `[-1,` `-1],` C là matrix A nhưng row 3 là [1 1]
>
> Thế thì dựa vào 3b, det C chính là det B * `-1` (vì hàng 2 của B là
> bằng hàng 2 của C nhân `-1)`
>
> Vậy thì det A `=` det B `-` det B `=` 0

<br>

<a id="node-589"></a>

<p align="center"><kbd><img src="assets/ec8451b27cc0352a96ed73a41427f25fd77023bf.png" width="100%"></kbd></p>

> [!NOTE]
> gs: property 7 cho là về det của một UPPER TRIANGULAR 
> matrix.
>
> VÀ LOWER **TRIANGULAR** CŨNG VẬY. 
>
> Nói chung là triangular matrix
>
> Dựa vào các properties trước hãy tính thử nó là gì

<br>

<a id="node-590"></a>

<p align="center"><kbd><img src="assets/14864ca9af7425e4a7b06279d1377e75583db32c.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 2: ELIMINATION WITH MATRICES](untitled.md#node-29)

> [!NOTE]
> Me: lấy ví dụ matrix này, đầu tiên dễ thấy nó là d3*det
> U1 (đây là tính chất 3a)
>
> Tiếp, từ U1, ta trừ hàng 2 cho hàng 3 nhân k ta có U2.
> Và theo property 5, det không đổi.
>
> Tương tự vậy, cuối cùng ta sẽ có det(U) `=` d1d2...dn*det(I)
>
> và det(I) `=` 1 
>
> Vậy det U `=` **d1d2.....dn
>
> (Và bài sau sẽ biết chúng (d1,d2...) cũng là eigenvalues)**

<br>

<a id="node-591"></a>

<p align="center"><kbd><img src="assets/3ca240dc58319677b58d211231d6afe50f57dbbf.png" width="100%"></kbd></p>

> [!NOTE]
> Gs cho biết trước khi chứng minh, đó là nó sẽ là **tích các
> d1...dn**. Và vì đây là U, nên đây**chính là các pivot**.
>
> Thế thì gs cho biết rằng trong **matlab để tính det của matrix**,
> nó sẽ:
>
> i) **đưa A về U** (Qúa trình này, theo tính chất 5 hồi nãy đã
> nói, sẽ không làm thay đổi det) nếu có row exchange, det
> sẽ cũng chỉ đổi dấu
>
> ii)**nhân các pivots**.
>
> Vậy cần lưu ý det U có thể bằng hoặc ngược dấu với det A
> bởi lẽ từ A đến U CÓ THỂ TA PHẢI ROW EXCHANGE

<br>

<a id="node-592"></a>

<p align="center"><kbd><img src="assets/2af8e83f7620b3d3e07cc4a223109ccd1b572818.png" width="100%"></kbd></p>

> [!NOTE]
> và chứng minh nó thì
> đúng như mình nghĩ.

<br>

<a id="node-593"></a>

<p align="center"><kbd><img src="assets/79bcc9f49d60ed416d7c960a09bf376c562ed000.png" width="100%"></kbd></p>

> [!NOTE]
> Và property 8 chính thức nói về nhận định hồi đầu lúc nãy
> thầy nói: matrix `non-invertible,` hay**singular thì det `=` 0**
>
> Me: Thử xem tính chất thứ 8 này có thể chứng minh từ các
> properties khác: Đó là nếu A `non-invertible` thì nó sẽ không
> `full-rank,` đồng nghĩa**elimination sẽ cho U có ít nhất 1 row
> bằng 0**. Thì khi đó:
>
> det A `=` `+-` det U (do property 5)
>
> U có một row `=` 0 `->` det U `=` 0 (property 6)
>
> Do đó det A `=` 0
>
> Gs: Chính xác là như vậy. Nếu **A singular, elimination sẽ
> cho ra ít nhất một row `=` 0 `->` det `=` 0**
>
> Và nếu A **invertible**, ta biết nó full rank, tức mọi row đều là
> pivot, thì **elimination sẽ đưa nó thành U, và ta có det là
> d1*d2....dn và do đó sẽ khác 0**

<br>

<a id="node-594"></a>

<p align="center"><kbd><img src="assets/0d66fd03cda9bafe1cdfa0d8c7e62b13934495ba.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: Thế thì ta đã có một công thức, **quy trình để tìm
> det của matrix A (n,n)**
>
> Vậy thử xem tại sao với **2x2 matrix A** thì det A `=` **ad-bc**

<br>

<a id="node-595"></a>

<p align="center"><kbd><img src="assets/adc43ab512275aebd6a9c5c9ce8a7826b23a4c55.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 19: DETERMINANT FORMULAS AND COFACTORS](untitled.md#node-611)

> [!NOTE]
> chuyển A về U, bằng cách khử c, `=`
> trừ hàng 2 cho `c/a` * hàng 1.

<br>

<a id="node-596"></a>

<p align="center"><kbd><img src="assets/04edefa49a82aba9703e1d5525df4ce4d41183d3.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: Correct

<br>

<a id="node-597"></a>

<p align="center"><kbd><img src="assets/66feb2db6520b9566917fb64a32bdf3173036985.png" width="100%"></kbd></p>

> [!NOTE]
> Property 9: **det AB `=` (det A)*(det B)**. Gs cho biết đây là tính
> chất rất tiện lợi, ta không có tính linearity, như nãy đã nói
> **det A `+` B không bằng det A `+` det B**
>
> Nhưng **det AB thì bằng tích hai det.**
>
> Vậy gs hỏi từ 9, tính thử **det A_inv**
>
> Me: A.Ainv `=` I, nên det I `=` det A * det `A_inv` 
>
> `=>` det `A_inv` `=` det I `/` det A `=` **1 `/` det A**

<br>

<a id="node-598"></a>

<p align="center"><kbd><img src="assets/1eac69aa5f4cfa036b4770305ef58e1959cb72f4.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: Correct

<br>

<a id="node-599"></a>

<p align="center"><kbd><img src="assets/671975ad1eb67a8b2c99a2a7c00198f99e272e52.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/671975ad1eb67a8b2c99a2a7c00198f99e272e52.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5c8032349f8fa5ad79291fcfe7f712bffe1a2ac2.png" width="100%"></kbd></p>

> [!NOTE]
> Và ta có thể thấy lấy ví dụ A là matrix **upper triangular** như
> vậy,  thì ta biết det A `=` 2*3 `=` 6
>
> Và AinvA `=` I, nên ta cũng biết Ainv sẽ có giá trị `1/2,1/3` trên
> đường chéo. (nhân AinvA là nhìn vậy chứ không phải là
> element wise đâu, mà nhân matrix bình thường cả AAinv hay
> AinvA đều cho ra I)

<br>

<a id="node-600"></a>

<p align="center"><kbd><img src="assets/a22c30b799fa6d91ed7edd05a829980a9c6de5fc.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, gs: det (A**2)?
>
> det A.A `=` detA detA `=` detA **2

<br>

<a id="node-601"></a>

<p align="center"><kbd><img src="assets/96a0f64a1421e3047b717ea845564fb7a30af55c.png" width="100%"></kbd></p>

> [!NOTE]
> còn det (2*A) `=` 2^n det A

<br>

<a id="node-602"></a>

<p align="center"><kbd><img src="assets/aa760195d0e7940e84a4c69b148a137fa4ce4432.png" width="100%"></kbd></p>

> [!NOTE]
> dễ thấy cái này là hệ
> quả của property 3a

<br>

<a id="node-603"></a>

<p align="center"><kbd><img src="assets/613adef1265a9cd4d01e9a36151a74c2ae2e4198.png" width="100%"></kbd></p>

> [!NOTE]
> Như vậy property 9 giúp ta có **det Ainv `=` `1/det` A** hoàn toàn
> giúp ta liên hệ tới việc **nếu A invertible** (hay non singular)
> t**hì det A khác 0**, do đó **det Ainv `=` `1/det` A** là công thức 
> có hiệu lực. Ngược lại, **nếu A singular, thì Ainv không
> tồn tại thì công thức det Ainv cũng không hiệu lực** vì 
> lúc này det A `=` 0

<br>

<a id="node-604"></a>

<p align="center"><kbd><img src="assets/fce915b5cb8586bcf117be8606002392acda97b2.png" width="100%"></kbd></p>

> [!NOTE]
> property 10 cho biết **det của AT `=` det A**. Kiểm tra bằng
> 2x2 matrix ta thấy đúng là đều bằng `ad-bc`
>
> Thế thì hệ quả quan trọng của 10 đó là, **mọi thứ liên quan
> đến row đều đúng với cols**.
>
> Ví dụ như **switch column sẽ đổi dấu det**, hay **matrix có
> cols `=` 0** **thì det `=` 0**

<br>

<a id="node-605"></a>

<p align="center"><kbd><img src="assets/41aa1ac1472ce487585bb1412c586d23e9e9bbd1.png" width="100%"></kbd></p>

> [!NOTE]
> Để chứng minh, ta có **elimination chuyển A `->` U**, và
> được thể hiện qua phương trình **A `=` LU** tương tự **AT
> `=` UT.LT**
>
> Gs: **det L là gì `->` 1**. Bởi gs nhắc ta nhớ**L là Lower
> Triangular matrix có diagonal là 1** nên theo property 7,
> det nó là **tích các  pivot trên đường chéo `->`  `=` 1**. Còn
> LT đương nhiên là Upper triangular nên det cũng `=` 1.
>
> ```text
> Vậy vì A = LU => det A = det L * det U = det U vì det L = 1
> ```
> ```text
> và từ A = LU <=> AT = (LU)T = UTLT nên ta có:
> ```
>
> det (AT) `=` det UT * det LT `=` det UT (vì det LT cũng `=` 1)
>
> và cuối cùng matrix U là triangular matrix, det của nó bằng
> tích các giá trị trên đường chéo, mà khi UT cũng có cùng
> đường chéo  với U, thành ra det UT cũng bằng det U.
>
> Vậy từ đó đủ cơ sở để kết luận **det A `=` det AT**

<br>

<a id="node-606"></a>

<p align="center"><kbd><img src="assets/1b7906c45c1d9b00057e02d8cb370666caf16da6.png" width="100%"></kbd></p>

<br>

