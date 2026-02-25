# Lecture 1: The Geometry Of Linear Equations

📊 **Progress:** `19` Notes | `20` Screenshots

---
<a id="node-3"></a>

<p align="center"><kbd><img src="assets/4af6ab1e86ea99d55cc07624f3b897f8b4d0eae8.png" width="100%"></kbd></p>

<br>

<a id="node-4"></a>

<p align="center"><kbd><img src="assets/6b448886747022427181af735655197d1fd98830.png" width="100%"></kbd></p>

> [!NOTE]
> gs đặt ra **equation system** như này, và **dạng matrix**
> của nó với **coefficient** matrix A, **variable vector x**

<br>

<a id="node-5"></a>

<p align="center"><kbd><img src="assets/1bc9aa24b5018574c262ab519f432a093a18d95d.png" width="100%"></kbd></p>

> [!NOTE]
> tiếp, gs **tìm tất cả các điểm giúp solve equation thứ 1**,
> tạo nên **đường thẳng 2x - y = 0**
>
> Đương nhiên ta **có thể tìm hai điểm đặc biệt** là **giao
> điểm của nó với hai trục** rồi **vẽ đường thẳng qua hai
> điểm đó**

<br>

<a id="node-6"></a>

<p align="center"><kbd><img src="assets/fac4233294064ab3b53e21ecf91f9d6aa723cf84.png" width="100%"></kbd></p>

> [!NOTE]
> tương tự, gs **vẽ tập hợp các điểm thỏa 2nd equation**,
> chính là **đường thằng -x + 2y = 0**. Cho thấy nó giao
> với 1st line ở x = 1; y = 2
>
> Nãy giờ ở đây gs nói về **Row picture** kiểu như **góc
> nhìn về matrix theo các row.** Dưới góc nhìn này, việc
> **solve equation system này là việc tìm ra bộ x,y giúp
> solve cả hai equation**, hay nói cách khác chính là:
>
> **Tìm ra điểm giao của hai linear line**

<br>

<a id="node-7"></a>

<p align="center"><kbd><img src="assets/25085d455318080604c853f02a925e808372deeb.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói qua**Column picture**

<br>

<a id="node-8"></a>

<p align="center"><kbd><img src="assets/3b78615a42d8de3affc9e7dfd17b262ca73805d3.png" width="100%"></kbd></p>

> [!NOTE]
> và với bức tranh này, câu hỏi sẽ là **tìm ra một linear
> combination của hai vector cột để ra vector b**
>
> và **linear combination** là một trong những **fundamental
> concept của linear algebra**

<br>

<a id="node-9"></a>

<p align="center"><kbd><img src="assets/b0efff2eaa59a3fdc669ee85fc766be200b94e4b.png" width="100%"></kbd></p>

> [!NOTE]
> Gs vẽ hai **vector columns** ra, câu hỏi là combination
> của chúng như thế nào để ra b. Thế thì như ta đã biết
> x = 1, y = 2 ở trên.

<br>

<a id="node-10"></a>

<p align="center"><kbd><img src="assets/395080f4c694270a6eda4f9ece993996b4b36def.png" width="100%"></kbd></p>

> [!NOTE]
> Thành ra ta sẽ cộng **1*col1 với 2*col2**
>
> Hình ảnh sẽ là ta **đi theo hướng col1 một đoạn = 1*col1** và
> **đi theo hướng col2 một đoạn = 2*col2**sẽ **dẫn tới chính là
> vector b (0,3)**

<br>

<a id="node-11"></a>

<p align="center"><kbd><img src="assets/486d3f7cbc486b274b5c5c7b366e6191bcc04367.png" width="100%"></kbd></p>

> [!NOTE]
> Gs mở rộng ý tưởng ra, vậy thì **mọi possible
> combination** sẽ cho ta kết quả là gì -> **Toàn bộ mặt
> phẳng**

<br>

<a id="node-12"></a>

<p align="center"><kbd><img src="assets/e0f2f2a0cabb3e18d888d97a082df0e7f651fcc5.png" width="100%"></kbd></p>

> [!NOTE]
> Gs lấy ví dụ khác equation
> system có 3 equation

<br>

<a id="node-13"></a>

<p align="center"><kbd><img src="assets/4e7229c38c63820304e6f0bca4568f288930afbc.png" width="100%"></kbd></p>

> [!NOTE]
> gs vẽ **tập hợp các điểm giúp solve equation thứ 2**, nó
> sẽ là **1 plane**

<br>

<a id="node-14"></a>

<p align="center"><kbd><img src="assets/d385e2c63e6c60d4cad22889ef511156def8cf8a.png" width="100%"></kbd></p>

<br>

<a id="node-15"></a>

<p align="center"><kbd><img src="assets/f181dd5b0366c3031c0a6f31e68c1d3e2584add3.png" width="100%"></kbd></p>

> [!NOTE]
> và **mỗi equation là một plane**, thế thì **giao
> của 3 plane** đó là **solution của equation system**

<br>

<a id="node-16"></a>

<p align="center"><kbd><img src="assets/dccfb65aa5955defb5fbab3de1dab933fcfbe38c.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự, ta sẽ giải theo "column picture", bài toán sẽ
> trở thành tìm linear combination của ba column vector để
> được vector b

<br>

<a id="node-17"></a>

<p align="center"><kbd><img src="assets/154c8de5e921fe5d21018ae5a8fa213e6bcaedbd.png" width="100%"></kbd></p>

> [!NOTE]
> (với việc cố tình chọn equation system) thì dễ thấy 
> linear combination sẽ là
>
> 0*col1 + 0*col2 + 1*col3
>
> Để rồi **vector b chính là trùng vector col3**

<br>

<a id="node-18"></a>

<p align="center"><kbd><img src="assets/9ab06b00b312178b44f0b81b4d2970410176f6cd.png" width="100%"></kbd></p>

> [!NOTE]
> câu hỏi gs đặt ra là liệu ta **có thể solve equation system
> này với MỌI vector b ko**?
>
> Hay điều này **tương tự** như hỏi rằng:
>
> **Liệu với 3 vector col1,2,3,** **ta có thể cover mọi điểm
> trong không gian 3D** ko?

<br>

<a id="node-19"></a>

<p align="center"><kbd><img src="assets/28752b36fb57628a943a4e8ee5c77a8884b0e7bd.png" width="100%"></kbd></p>

> [!NOTE]
> Thì câu trả lời là **đối với matrix A** thì là "có".
>
> Và lí do là **bởi vì với A**, **3 col vector không cùng một
> plane**, nên luôn tìm ra được một linear combination
> giúp đi đến mọi điểm trong 3D space
>
> Trong trường hợp này ta có một **NON-SINGULAR /
> INVERTIBLE MATRIX**

<br>

<a id="node-20"></a>

<p align="center"><kbd><img src="assets/4231f1e4236c5d6b7ca270f8eae380adade8d3ea.png" width="100%"></kbd></p>

> [!NOTE]
> Còn ở một trường hợp khác, giả sử ta có matrix A với
> **3 col vector nằm trong một plane**, mà điều này xảy
> ra **khi một col vector là combination của hai col kia**
> (vì như đã biết, **hai col kia sẽ cover một plane**, nên
> **nếu col thứ 3 nằm trong plane đó thì nó sẽ là một
> linear combination của hai col 1 và col 2**.
>
> **Khi đó 3 col vector chỉ cover được 1 plane** nên**mọi điểm b nằm ngoài plane này sẽ đều không
> reachable bằng 3 col vector** -> không thể solve
> equasys với 3 vector này được

<br>

<a id="node-21"></a>

<p align="center"><kbd><img src="assets/53cdee0d463a6cc34e5b63a75e0535151863f17d.png" width="100%"></kbd></p>

> [!NOTE]
> và hình dung dù thật ra cũng khó mà hình dung được là ta **có
> một equation system trong 9-dimensional space**. Tức **col
> vector có 9 component (unit)**. Thế thì với câu hỏi này, ta cũng
> sẽ có thể **lập luận tương tự**
>
> Đó là, **nếu ta có 9 col vector linear independent**, thì **mọi
> chuyện ok**: ta **có thể reach tới mọi điểm trong không gian 9D
> này bằng (một linear combination của) 9 col vector.**
>
> Nhưng **nếu rủi thay mà col #9 là y như col #8 (hay là một
> linear combination của 8 col kia)** thì kiểu như ta lại **gặp một
> 8D plane** trong **một 9D space**.
>
> Và **mọi điểm b ở ngoài cái 8D plane đó đều không thể
> reachable.**
>
> Ở đây gs bắt đầu nhắc tới việc **col #9 không add thêm
> information gì vào system**.

<br>

<a id="node-22"></a>

<p align="center"><kbd><img src="assets/6a34fa23a0025d950685038f76ff94a020625a5f.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói về cách**tính nhân matrix A và vector b**, thì thật ra
> có **2 cách**, và gs như nãy giờ cũng thấy **thích cách làm
> theo column**.
>
> **Với góc nhìn column** thì **Ax là một linear combination
> của các col vector của A**, mà **các coefficient quy định
> bởi x**
>
> Cách thứ 2 là**làm theo row**, và cơ bản là ta sẽ tính hai
> phép tính **dot product của x** **với hai row của A**

> [!NOTE]
> Bài sau gs sẽ dùng phương pháp
> **Elimination** để **tìm solution của equasys**

<br>

