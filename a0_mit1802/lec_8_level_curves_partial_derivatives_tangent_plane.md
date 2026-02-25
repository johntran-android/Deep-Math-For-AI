# Lec 8: Level Curves, Partial Derivatives, Tangent Plane

📊 **Progress:** `20` Notes | `22` Screenshots

---
<a id="node-150"></a>

<p align="center"><kbd><img src="assets/5e3254b4fd40a483b8e278b16f26307bfc43845c.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là nói về function có **hơn một variable**, ví dụ với **2
> variables** **f(x, y)** với một số ví dụ như **f=x^2+y^2,** hoặc function
> dựa vào x,y để tra cứu một thông tin nào đó.
>
> Để đơn giản ta sẽ **tập trung chủ yếu vào function có 2 hoặc 3
> variable**

<br>

<a id="node-151"></a>

<p align="center"><kbd><img src="assets/869eab10dc5c1edaba6d551d21f92adb1e49e7aa.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là để visualize function f(x,y), thì ta sẽ có một plane tạo bởi
> các điểm <x, y, z=f(x,y)>

<br>

<a id="node-152"></a>

<p align="center"><kbd><img src="assets/b2320b24611e64d9bb365ba7a38ab953cbd824b5.png" width="100%"></kbd></p>

> [!NOTE]
> ví dụ của f(x, y) = -y

<br>

<a id="node-153"></a>

<p align="center"><kbd><img src="assets/893c76e46bd8b3e79221861a74e2fe58a8319677.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ khác với function f = 1 - x^2 - y^2. Đại khái là ta có thể làm từng
> bước để **dần hiểu dạng đồ thị của f** như thế nào. Bằng cách đầu tiên
> là xét trong **yz-plane**, tức x = 0. Khi đó f = 1 - y^2, như vậy giao của
> đồ thị hàm f với yz plane là parabola.
>
> Tương tự xét trong **xz plane** thì nó là parabola**f = 1 - x^2.**
>
> Và xét trong xy plane, tức z = 0 thì ta có **x^2+y^2 = 1**, đây là phương
> trình **đường tròn unit.**

<br>

<a id="node-154"></a>

<p align="center"><kbd><img src="assets/20353b91dedc47088576b0a2f72c57a5fb82b78b.png" width="100%"></kbd></p>

> [!NOTE]
> hình ảnh bởi máy tính

<br>

<a id="node-155"></a>

<p align="center"><kbd><img src="assets/56349b3e513e488cf0b94e7f351bb36d829d1a34.png" width="100%"></kbd></p>

> [!NOTE]
> Còn đây là đồ thị của f = y^2 - x^2. có hình yên ngựa (saddle point), thì
> để ý rằng **xét trong plane yz** thì nó là **parabola ngửa lên**. Ngược lại
> trong **plane xz** thì nó là **parabola úp xuống**

<br>

<a id="node-156"></a>

<p align="center"><kbd><img src="assets/32b58ccc9c8260efd4a4c5e336979c49c89bafac.png" width="100%"></kbd></p>

> [!NOTE]
> Đây là gs nói qua **cách khác để visualize function** đó là **Contour**
> plot mà mình đã g**ặp nhiều lần trong ML class**.
>
> Nói chung là dễ hiểu khi các đường contour sẽ cho biết**giá trị của
> hàm f của mọi điểm trên đường** đó. Và nhờ vậy khi cần **xác định
> giá trị hàm f tại đâu đó**, ta có thể nhanh chóng biết được ví dụ điểm
> nào đó nằm giữa hai đường contour 1,2 thì sẽ có giá trị đâu đó ở giữa
> 1,2

<br>

<a id="node-157"></a>

<p align="center"><kbd><img src="assets/33cefb5369e43fdb568707440e2eb50ad9868cca.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta **định nghĩa chính thức của contour plot** là nó **show
> mọi điểm mà f(x, y) = fixed constant** nào đó, thường được chọn là
> tại các **regular intervals** ví dụ như 1,2,3 như ở đây.
>
> Và có thể **coi như ta cắt đồ thị hàm f bởi các plane nằm ngang**. Thì
> những đường cắt đó gọi là **LEVEL CURVE OF F**
>
> Và thể hiện hết các đường cắt đó thì ta có contour plot.

<br>

<a id="node-158"></a>

<p align="center"><kbd><img src="assets/d2206aef9c801c1004a0e128282e73d7f2d5149d.png" width="100%"></kbd></p>

> [!NOTE]
> Một **ví dụ về contour plot**. Khi ta di
> chuyển theo một đường contuour
> thì độ cao ko đổi

<br>

<a id="node-159"></a>

<p align="center"><kbd><img src="assets/d3ff67dc43b2007c2b0e94fbac4b0765484bc111.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ vẽ contour plot của function này. lần lượt cho f = 0,1,
> 2,-1,-2 thì ta có các line tạo nên contour plot

<br>

<a id="node-160"></a>

<p align="center"><kbd><img src="assets/ad45e73e137e31d225f6c5ff3c38f8a579e14049.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự là contour plot của function này. Cũng bằng cách **lần lượt
> cho f bằng các giá trị với regular interval** như 0,1,2,3 ta có các
> contour là các **phương trình đường tròn** với **bán kính khác
> nhau**.
>
> Thế thì đại ý cần chú ý là **các contour ngày càng sát nhau** khi ra xa
> thể hiện **độ dốc ngày càng lớn** (vì ta sẽ chỉ phải **đi ngày càng
> ngắn hơn** để  **tăng thêm một đơn vị của f**)
>
> Thì hình dạng 3D của nó là hình khi nãy

<br>

<a id="node-161"></a>

<p align="center"><kbd><img src="assets/e3859cf3f8ecd796f5036abf8b3402736abd16ff.png" width="100%"></kbd></p>

> [!NOTE]
> Gs cho xem contour plot của saddle point z = y^2 - x^2

<br>

<a id="node-162"></a>

<p align="center"><kbd><img src="assets/4ea4ee4727db0465528bacd52ca9f535739e4411.png" width="100%"></kbd></p>

<br>

<a id="node-163"></a>

<p align="center"><kbd><img src="assets/0b4b970e272db6010d55438cced9894d96d27d86.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là contour plot có thể cho ta câu trả lời rằng **khi x, y tăng
> lên hay giảm** (xét cái này thì giữ cái kia fix) thì function sẽ tăng
> hay giảm

<br>

<a id="node-164"></a>

<p align="center"><kbd><img src="assets/e53f5b9b4c54506539e01bb5c0975d940621767e.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì để biết **khi tăng hay giảm x, y** thì **function tăng hay
> giảm nhanh hay chậm như thế nào** (tức là độ dốc của hàm số) thì
> ta sẽ**cần derivative**
>
> gs review lại với hàm đơn biến thì **derivative** được định nghĩa là:
>
> **limit của [f(x+delta_x) - f(x)] /delta_x khi delta_x -> 0**

<br>

<a id="node-165"></a>

<p align="center"><kbd><img src="assets/33069fed401fbff7bc3eab7f85ce25e5001e6ac4.png" width="100%"></kbd></p>

> [!NOTE]
> Về mặt **hình học** thì derivative của function là function mang
> giá trị là **độ dốc của tiếp tuyến** (**tangent** line) của hàm số, nên
> **f'(x)** là giá trị của **độ dốc của tiếp tuyến tại x**
>
> **Không phải function nào cũng có derivative** tại **mọi điểm** nhưng
> trong class này ta sẽ k**hông care vấn đề differentiability**

<br>

<a id="node-166"></a>

<p align="center"><kbd><img src="assets/d5b0e20af6801183ab8ef5225fe38d12ec169783.png" width="100%"></kbd></p>

> [!NOTE]
> Ta có function ước lượng **xấp xỉ hàm số f**: f(x) ~= f(x0) + f'(x0)(x-x0) 
> và gs cho biết nếu ta có thêm các higher order term nữa thì 
> đó chính là Taylor series
>
> Sau khi học bài 9 của 1801, ta đã có thể hiểu đây chính là **LINEAR**
> **APPROXIMATION**: f(x) ~= f(x0) + f'(x0)(x-x0), xuất phát từ lập luận
> khi limit delta_x -> 0 của delta_f / delta_x = f'(x)
>
> Thì ta có thể cho rằng khi delta_x ~= 0, tức x-x0~=0, hay x~=x0
> thì delta_f / delta_x ~= f'(x0) từ đó f(x)-f(x0)~=f'(x0)(x-x0)
> <=> **f(x) ~= f(x0) + f'(x0)(x-x0)**
> Còn nếu có thể quadratic term f''(x0)(x-x0)^2/2 thì ta sẽ có 
> **QUADRATIC** **APPROXIMATION**: 
>
> f(x) ~= f(x0) + f'(x0)(x-x0) + f''(x0)(x-x0)^2/2

<br>

<a id="node-167"></a>

<p align="center"><kbd><img src="assets/b0416a665d7f1f7a18c52cef880949117f2e3d55.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là gs nói về khái niệm và kí hiệu của **partial derivative.** Đối
> với **function đa biến** thì nó **không có derivative thông thường** mà
> **chỉ có partial derivative với mỗi biến**.
>
> mang cái tên **partial**: từng phần / một phần là **bởi nó chỉ đối với một
> biến nào đó,**chứ**không phải toàn bộ**.
>
> Và định nghĩa của nó là ví dụ**partial derivative của f w.r.t x** tại **(x0, y0)**
> là **limit của  [f(x0+delta_x, y0) - f(x0, y0)] / delta_x**. Trong đó ta sẽ **treat
> y như constant**
>
> Tương tự với partial derivative của f w.r.t y
>
> **Nếu hai function này tồn tại thì f gọi là differentiable**
>
> Tuy nhiên gs nói **ta sẽ không tính bằng định nghĩa**, mà ta sẽ tính bằng
> các **phương pháp tính đạo hàm** mà ta đã biét

<br>

<a id="node-168"></a>

<p align="center"><kbd><img src="assets/74f1f1670f39fad8ec5e6c7c7e2f3ab9fd826bda.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **về mặt hình học**, ý nghĩa của partial derivative của f w.r.t x
> là:
>
> Ta sẽ**giữ y constant**, khi đó giống như ta**dùng plane y = constant** để
> **cắt** đồ thị của f(x) tại **một đường intersection màu vàng**.
>
> Và **partial derivative của f w.r.t x** chính là **FUNCTION THỂ HIỆN GIÁ
> TRỊ CỦA ĐỘ DỐC TIẾP TUYẾN CỦA ĐƯỜNG MÀU VÀNG NÀY**

<br>

<a id="node-169"></a>

<p align="center"><kbd><img src="assets/bebf1e43402a3db87ca9c4ae87ab8b05f4c975d9.png" width="100%"></kbd></p>

<br>

<a id="node-170"></a>

<p align="center"><kbd><img src="assets/b13c522e5528ad6d27bf75c014d97bafc6c8c095.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy **để tính partial derivative**, ví dụ của partial f / partial x, ta sẽ
> **coi y như constant** và **x là variable** và **tính derivative của f đối với
> x như với hàm 1 biến**
>
> Ở đây gs nói thêm **partial derivative** của f đối với x có thể được kí hiệu 
> là **f_x**

<br>

<a id="node-171"></a>

<p align="center"><kbd><img src="assets/3f865e05a126184cebd2e91666ba5d088d2c0020.png" width="100%"></kbd></p>

> [!NOTE]
> Một ví dụ

<br>

