# Lec 9: Max-min Problems, Least Squares

📊 **Progress:** `23` Notes | `33` Screenshots

---
<a id="node-173"></a>

<p align="center"><kbd><img src="assets/583c1fe674a38bfc4c37627e30b7920c2712b551.png" width="100%"></kbd></p>

🔗 **Related:** [Như vậy ta hiểu là trong 1801 implicit differentiation là ta apply d/dx vào hai vế, mà ý nghĩa CHÍNH LÀ LẤY ĐẠO HÀM THEO X HAI VẾ.   y = f(x) => (d/dx) y = (d/dx) f(x) <=> \\*dy/dx = f'(x)\\*  Còn 18.02 thì implicit differentiation thể hiện bằng cách  LẤY VI PHÂN HAI VẾ  y = f(x) <=> \\*dy = f'(x) dx\\*  Và chúng cùng bản chất, chẳng qua cách thể hiện theo vi phân  sẽ chuẩn bị cho ta bước qua khái niệm VI PHÂN TOÀN PHẦN (TOTAL DIFFERENTIAL)](untitled.md#node-230)

> [!NOTE]
> Tiếp bài trước về **partial derivative**, ta quay lại với **approximation
> formula** (linear approximation)
>
> Câu hỏi là với**function 2 biến x, y** thì công thức sẽ ntn:
>
> Câu trả lời là nếu **x ~> x + ∆x**,**y ~> y + ∆y** thì z = f(x, y) sẽ
> thay đổi một khoảng xấp xỉ  **f_x*∆x + f_y*∆y** với f_x, f_y là 
> partial derivative
>
> Tức là linear approximation đối với bivariate function f(x, y) là:
>
> **∆f ~= f_x*∆x + f_y*∆y** 
>
> So sánh với hàm một biến: 
>
> **∆f ~= f'*∆x** (hay f(x) - f(x0) ~= f'(x0)(x-x0) 
>
> <=> **f(x) ~= f(x0) + f'(x)(x-x0)**
>
> Và intuition là: khi **x thay đổi delta_x** nó khiến f**unction f thay đổi** một
> khoảng bằng **delta_x** **nhân** với**rate of change f_x**: **f_x*delta_x**
>
> khi**y thay đổi delta_y** nó khiến function **thay đổi một khoảng delta_y**
> **nhân** với **rate of change f_y**: **f_y*delta_y**.
>
> Thế thì khi thay đổi cả x, y ta **xấp xỉ** khoảng thay đổi của f bằng **tổng
> hai khoảng thay đổi** do y và do x

<br>

<a id="node-174"></a>

<p align="center"><kbd><img src="assets/c7a3bd4b959e0bb63632760481c5de601e51573b.png" width="100%"></kbd></p>

> [!NOTE]
> Review lại **một chút ý nghĩa của partial derivative** của f w.r.t x:
>
> Đó là ta sẽ **giữ y = y0 fixed**, để rồi điều này **giống như ta sẽ cắt đồ
> thị hàm f với plane song song với xz plane**, khi đó ta có
> **intersection** là đồ thị của **hàm số f(x, y0)**.
>
> Thì hàm số mang giá trị là **độ dốc của f(x, y0)** chính là **derivative
> của f(x, y0)**, và nó chính là **partial derivative của f đối với x:
> f_x()**

<br>

<a id="node-175"></a>

<p align="center"><kbd><img src="assets/822f56caa416de7f856449123d66a210632bacd4.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì, tiếp theo ta sẽ justify (**biện minh**) cho c**ông thức
> approximation**  vừa rồi.
>
> Ta sẽ đã biết**f_x, f_y** là**slope của 2 đường tiếp tuyến**

<br>

<a id="node-176"></a>

<p align="center"><kbd><img src="assets/19d5398c546c569418553469fc13595c476543fb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/19d5398c546c569418553469fc13595c476543fb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/202f7689e0ccef46d74e85d40ab79cc561f2b058.png" width="100%"></kbd></p>

> [!NOTE]
> thế thì đại khái là **nếu ta có f_x(x0, y0) = a** ta có **đường tiếp tuyến** nằm t**rong mặt phẳng
> song song với xz,** **cắt trục y tại** **y0** và có **độ dốc tại x0 là a**, và phương trình của nó là **z -
> z0 = a(x - x0)** mang ý nghĩa là khi x thay đổi từ x0 -> x, z thay đổi từ z0 -> z với rate
> (z-z0)/(x-x0) = a
>
> Tương tự với **tiếp tuyến thứ hai**, **độ dốc tại (x0,y0) là b**, nó nằm **trong mặt phẳng song 
> song với yz**, **cắt x tại x0**và có phương trình:
>
> x = x0; z - z0 = b(y - y0)

<br>

<a id="node-177"></a>

<p align="center"><kbd><img src="assets/a4419267d7a67c1fdbc05d9c9ed619bb2ee2dd14.png" width="100%"></kbd></p>

> [!NOTE]
> thế thì **L1, L2 đều là tiếp tuyến của đồ thị hàm z = f(x,y)**. Chúng
> **TẠO THÀNH MỘT PLANE** plane **z = z0 + a(x-x0) + b(y-y0)**
>
> Thì đây là phương trình mặt phẳng với x*constant + y*constant +
> constant và nếu giữ y, thay đổi x ta có phương trình của tangent line
> thứ 1 (ý là cho y = y0 ko đổi thì phương trình trở thành z = z0 + a(x -
> x0)) và ngược lại, giữ x thay đổi y thì ta có phương trình tangent line
> thứ 2
>
> Gs nói rằng **để có phương trình này** ta có thể **dùng cách khác** liên
> quan đến việc dùng **cross product** và **normal vecto**r, ta cũng sẽ ra
> equation này.

<br>

<a id="node-178"></a>

<p align="center"><kbd><img src="assets/ff3887e790a122ef9561a26b27419ded8586f083.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì gs cho biết **ý nghĩa** của **linear approximation đối với hàm
> hai biến** chính là **nói rằng** **đồ thị hàm số f (tất nhiên chỉ xét trong
> một khoảng x~=x0) có thể coi như trùng với tangent plane**.
>
> Nếu ta **di chuyển trên tangent plane** thì **delta_z = linear function
> của delta_x và delta_y (fx*delta_x + fy*delta_y)**.
>
> Nhưng vì **thực tế** đồ thị của f **chỉ là gần bằng tangent plane** nên
> ta dùng dấu**xấp xỉ ~=**

<br>

<a id="node-179"></a>

<p align="center"><kbd><img src="assets/cc93458952a0667c79f49742dd906e1e8c4637a7.png" width="100%"></kbd></p>

<br>

<a id="node-180"></a>

<p align="center"><kbd><img src="assets/3732710335e9684d1af66234032119987b6b66e9.png" width="100%"></kbd></p>

<br>

<a id="node-181"></a>

<p align="center"><kbd><img src="assets/57d5b8f29df05cdcbbfed8edd7db0b8b3eed3830.png" width="100%"></kbd></p>

> [!NOTE]
> Ứng dụng của partial derivative là **optimization**
> problem **tìm min max của function f(x,y)**

<br>

<a id="node-182"></a>

<p align="center"><kbd><img src="assets/ad9d0b95aab7e3569b180c143cab7fccfc8b7d14.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ad9d0b95aab7e3569b180c143cab7fccfc8b7d14.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6438ebec92f74fbf75daa112d7138203984dfb13.png" width="100%"></kbd></p>

> [!NOTE]
> thế thì gs nói rằng tại l**ocal min hoặc max thì cả fx
> và fy đều bằng 0.**
>
> Và ta khi đó **tangent plane sẽ nằm ngang (song
> song với xy plane)**

<br>

<a id="node-183"></a>

<p align="center"><kbd><img src="assets/5453b317b6f5ad67f04888097cd01bd45484cd81.png" width="100%"></kbd></p>

> [!NOTE]
> và ta có cái tên cho điểm mà tại đó mọi partial derivative đều bằng 0:
> **CRITICAL POINT (cực trị)**.
>
> Gs cho biết nó **chưa thỏa điều kiện đủ** để xác định là **max hoặc
> min** vì **có những điểm khác mà mọi partial derivative cũng bằng
> 0**

<br>

<a id="node-184"></a>

<p align="center"><kbd><img src="assets/c2f68b21cd758e827fb2eafdda04a3812c3e0bb1.png" width="100%"></kbd></p>

> [!NOTE]
> nói nó **chưa đủ để kết luận** min hay max là vì s**addle point
> cũng có mọi partial derivative bằng 0**. Nhưng tùy ta đi hướng nào
> (thay đổi x hay y) thì function sẽ tăng lên hay giảm xuống
>
> Bài sau ta sẽ xác định maximum hay saddle point bằng cách dùng
> đạo hàm cấp 2 (**second** **partial** **derivative**)

<br>

<a id="node-185"></a>

<p align="center"><kbd><img src="assets/0faab1a80c39f154cc2c2cf510c2337892b2e7f3.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì có**3 khả năng như vậy**, như vừa nói **bữa sau** ta sẽ dùng
> **đạo hàm cấp hai để xác định**. Còn ở đây ta sẽ dùng phương pháp
> **COMPLETING THE SQUARE**

<br>

<a id="node-186"></a>

<p align="center"><kbd><img src="assets/676d9c22d79d29815855dba05cd60f74af3e17c7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/676d9c22d79d29815855dba05cd60f74af3e17c7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e101fc4e3fc7d71a77d2bcb8d155d8f5ee2f4333.png" width="100%"></kbd></p>

> [!NOTE]
> Bằng cách**đưa f về tổng các bình phương**, thì **ta xác định f sẽ >= -1**
>
> và nó **bằng -1 khi y = 0**, và x-y = -1 ->**x = -1**. Do đó đây là **minimum**

<br>

<a id="node-187"></a>

<p align="center"><kbd><img src="assets/d58e55d76589ad27daadee1b047fe865b30d84e4.png" width="100%"></kbd></p>

> [!NOTE]
> gs nói qua **bài toán Least Square**, như đã biết là trong bài toán này ta 
> sẽ muốn **tìm line y = ax + b** **fit tốt nhất** với các data point **(xj, yj)**

<br>

<a id="node-188"></a>

<p align="center"><kbd><img src="assets/5e7b758ac9be55f8f266de7a55ed5c33e572c0f4.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là gs giải thích về việc **để có best line**, thì ta **phải định nghĩa
> best là như thế nào**. Thế thì c**ó nhiều kiểu định nghĩa**, để rồi mỗi
> cái sẽ cho ra một best line khác nhau.
>
> Nhưng một **giải pháp là dùng sum bình phương của các error**.
> Gs cho rằng cái này được **sử dụng phổ biến** vì thứ nhất nó c**ho ra
> kết quả best line** là đường đi khá tốt, **sát với data points**.
>
> Và thứ hai là nó **khiến bài toán trở nên đơn giản**, dễ giải.

<br>

<a id="node-189"></a>

<p align="center"><kbd><img src="assets/be535b6f601847f75108c88522d4ea7c0227a751.png" width="100%"></kbd></p>

> [!NOTE]
> như đã nói bài toán **Least Square**, ta sẽ tìm cách **minimize** D =
> **Tổng bình phương của residual** (difference giữa "predicted value"
> ax_i + b và y_i)

<br>

<a id="node-190"></a>

<p align="center"><kbd><img src="assets/51a46f18fee100ff8d6fb3d027b3f5d481209296.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì đầu tiên ta sẽ đi tìm**CRITICAL POINT**, bằng cách **solve
> các equation**: **Partial derivative của D w.r.t a và b bằng 0**.
>
> Việc **tính partial derivative** khá **đơn giản**. Với việc dùng
> **chain rule**

<br>

<a id="node-191"></a>

<p align="center"><kbd><img src="assets/8cd1a66d58c231497c736f7dece62d36e0179cde.png" width="100%"></kbd></p>

> [!NOTE]
> **Simplify** một chút ta có như vầy, gs lưu ý rằng ta có thể
> thấy đây **vẫn là các linear equation of a, b**

<br>

<a id="node-192"></a>

<p align="center"><kbd><img src="assets/cc3d3be54176bc872fd2d0513f3b9d617d706584.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo, nôm na là ta **có thể phân phối dấu tổng** (cơ bản
> chỉ là **sắp xếp lại các term**). Và bài toán **hoàn toàn chỉ là
> giải hệ hai phương trình tuyến tính**

<br>

<a id="node-193"></a>

<p align="center"><kbd><img src="assets/4565f3bd6590d2202b79018d1c304fa101ff8d17.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/32179e3be2b0c512dcccf0b32c9c7ebb60d129d2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4565f3bd6590d2202b79018d1c304fa101ff8d17.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/32179e3be2b0c512dcccf0b32c9c7ebb60d129d2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c5406a42a706873e6408b8a6f3300b48f95d5cdb.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, đại khái gs cho một ví dụ khác, trong đó data points
> không có vẻ gì là có quy luật tuyến tính

> [!NOTE]
> Nhưng khi dùng giá trị **log** của y, thì nó có thể thấy là tuân
> theo linear pattern

> [!NOTE]
> và sự thật pattern của
> nó là exponential

<br>

<a id="node-194"></a>

<p align="center"><kbd><img src="assets/c135c81238ac2d8245fd02c5173c8852e7015e50.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì **true pattern** có dạng **y = c*e^ax**, để **tìm c và a** giúp
> tạo được đường **fit tốt nhất với data** này thì rất **khó**. Nhưng **chỉ
> cần lấy ln hai vế**. Ta sẽ có  thể thấy **bài toán trở thành least
> square**ln(c*e^ax) = ln(c) + ln(e^ax) = ln(c) + ax ln(e) = ln(c) + ax

<br>

<a id="node-195"></a>

<p align="center"><kbd><img src="assets/1441701cfeb5696554efac21e7f32f7b5793ec49.png" width="100%"></kbd></p>

> [!NOTE]
> Hay để fit được quadratic pattern thì cũng hoàn toàn dùng least
> square để solve a, b, c bình thường. Và ta sẽ vẫn có hệ 3 phương 
> trình TUYẾN TÍNH đối với a, b, c

<br>

