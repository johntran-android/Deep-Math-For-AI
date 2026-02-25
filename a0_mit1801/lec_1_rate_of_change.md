# Lec 1: Rate Of Change

📊 **Progress:** `25` Notes | `27` Screenshots

---
<a id="node-3"></a>

<p align="center"><kbd><img src="assets/0961414ea779a70961a23f77597631a59fdf76c2.png" width="100%"></kbd></p>

> [!NOTE]
> về khía cạnh hình học, bài toán là tìm đường tiếp tuyến
> với function y = f(x) tại P. Thì gs vẽ đường này và cho
> rằng bằng cách nào đó ông đã làm xong. Nhưng vấn đề
> là làm sao để tìm nó analytically để máy tính cũng có
> thể làm được

<br>

<a id="node-4"></a>

<p align="center"><kbd><img src="assets/ff4b9132e25404cea047825558855d2cc74aa396.png" width="100%"></kbd></p>

> [!NOTE]
> Dựa vào kiến thức highschool, phương trình đường tiếp tuyến tại
> P (x0, y0) sẽ có dạng như vầy. Ta sẽ cần tìm P và độ dốc (slope)
> m, và slope độ dốc của đường thẳng tại P (x0, y0) được gọi là
> derivative f'(x0)

<br>

<a id="node-5"></a>

<p align="center"><kbd><img src="assets/4a5425c9d438ce9f3c08bd1ac0c01f871d7946ae.png" width="100%"></kbd></p>

> [!NOTE]
> Ta có định nghĩa f'(x0) là derivative của hàm f tại x(0)
> chính là độ dốc của đường tiếp tuyến với hàm f(x) tại P (x0, y0)

<br>

<a id="node-6"></a>

<p align="center"><kbd><img src="assets/3b681733d739aadacd1c8cb21615d6a8b9d2e99e.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì gs đặt vấn đề là, làm sao để biết một line như đường màu
> cam không phải là tangent. Ông cho rằng không phải vì nó cắt f tại 2
> điểm P, Q mà nói nó không phải tangent, bởi lẽ function có thể wiggly.

<br>

<a id="node-7"></a>

<p align="center"><kbd><img src="assets/cf8a02ff4870e9ca01e16fc88476ad212acfd4c7.png" width="100%"></kbd></p>

> [!NOTE]
> và thực tế tangent line chính là đường
> secant line khi Q -> P với P cố định

<br>

<a id="node-8"></a>

<p align="center"><kbd><img src="assets/37fecb318236670fb3b748ab6fe3bab801e82302.png" width="100%"></kbd></p>

> [!NOTE]
> tiếp theo gs vẽ lại secant line, gọi delta_x (xQ - xP) là khoảng
> thay đổi của x, delta_f= f(Q) - f(P) là khoảng thay đổi của f
>
> thì độ dốc của tangent theo định nghĩa (gs cho rằng lim có thể áp
> dụng cho cả line và độ dốc) sẽ là limit của delta_f / delta_x khi
> delta_x nhỏ vô cùng

<br>

<a id="node-9"></a>

<p align="center"><kbd><img src="assets/fe9b1d1811037bf61ece3ed6b24e6c9031cc0dae.png" width="100%"></kbd></p>

> [!NOTE]
> và ta với việc thay delta_x = f(x0+delta_x) - f(x0) ta có định
> nghĩa chính thức của derivative of f tại x0: f'(x0)

<br>

<a id="node-10"></a>

<p align="center"><kbd><img src="assets/6b7f73f27a29e8d7db33071358f921539c417c25.png" width="100%"></kbd></p>

🔗 **Related:** [LEC 3: DERIVATIVES](untitled.md#node-59)

> [!NOTE]
> và biểu thức cần tìm limit có tên gọi là
> **DIFFERENCE QUOTIENT**

<br>

<a id="node-11"></a>

<p align="center"><kbd><img src="assets/702bf6c0758ec69e988cfe6c5ffceddcb9772b96.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ áp dụng để tìm derivative của f(x) = 1/x. Ông cho rằng ta
> sẽ chọn 1 điểm x0. Và kết quả là ta sẽ tìm được tangent line
> của hyperbolla này

<br>

<a id="node-12"></a>

<p align="center"><kbd><img src="assets/64924f5324f767b869ffaf93aa72207d20a48228.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì ta sẽ thiết lập delta_f/delta_x
> như vầy. Và thu gọn nó lại

<br>

<a id="node-13"></a>

<p align="center"><kbd><img src="assets/209164558bfe1127540bb112f6af9f8dbcdeea77.png" width="100%"></kbd></p>

> [!NOTE]
> Mục đích là khử đi delta_x ở tử và mẫu thoát khỏi dạng 0/0 (khi
> delta_x -> 0)
>
> Kết quả cuối cùng, là -1/(x0 + delta_x)x0. Và để có lim khi delta_x
> -> 0  chỉ việc thế delta_x = 0, Ta có **-1/x0^2**Dễ thấy đây cũng chính là công thức tính đạo hàm của hàm 1/x
> Thì ở đây chính là ta tìm lại công thức của nó theo định nghĩa đạo
> hàm

<br>

<a id="node-14"></a>

<p align="center"><kbd><img src="assets/453115ee4368675a9a33c0adf976c241db87a457.png" width="100%"></kbd></p>

> [!NOTE]
> nhận xét là tangent của hàm 1/x chúi xuống vì slope âm. Và khi x0 ->
> vô cùng, tức là điểm tiếp tuyến càng xa thì độ dốc càng nhỏ lại
>
> ý nói cái mà ta tìm ra phù hợp với hình ảnh của tangent của hyperbol

<br>

<a id="node-15"></a>

<p align="center"><kbd><img src="assets/d89f7562dcb8aa5600151a315ae56e13dba8f786.png" width="100%"></kbd></p>

> [!NOTE]
> gs giải thích khi tìm limit của biểu thức này khi delta_x -> 0, điều
> ta làm thật sự chỉ là bỏ 0 vào delta_x thôi

<br>

<a id="node-16"></a>

<p align="center"><kbd><img src="assets/4a68861c34eb8bf0cad4008047a41ebf74ac3520.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4a68861c34eb8bf0cad4008047a41ebf74ac3520.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/500ca18943c5f759d536b95289af7edbbb101558.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp ta sẽ thử giải bài toán này: tìm diện tích của hình tạo bởi
> tangent của f(x) = 1/x và 2 trục. Nó là vấn đề calculus vì nó có dính
> đến tangent.

<br>

<a id="node-17"></a>

<p align="center"><kbd><img src="assets/d0eedec36395542a487b58a04bb0cdfd101c49d4.png" width="100%"></kbd></p>

> [!NOTE]
> Gọi x0,y0 là điểm tiếp xúc
>
> Thế thì rõ ràng ta cần tìm base và height thể hiện bằng 2 điểm
> line cắt 2 trục
>
> Thế thì ta đã có phương trình đường tangent với độ dốc đã NHỜ
> CALCULUS MÀ TÍNH ĐƯỢC = -1/x^2.
>
> Gs gọi nó là yếu tố duy nhất của calculus trong bài toán này

<br>

<a id="node-18"></a>

<p align="center"><kbd><img src="assets/64263ff56f3c3f7540840f78e2d8f14d6711b71b.png" width="100%"></kbd></p>

> [!NOTE]
> Và để tìm hai giao điểm của tangent line với 2 trục ta cho y = 0 để
> tìm điểm thứ nhất, và x = 0 để tìm điểm thứ 2.
>
> Từ đó ta có height và base của tam giác

<br>

<a id="node-19"></a>

<p align="center"><kbd><img src="assets/f299481561ac1f8b7887fed4f822d2db7bab492a.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái gs có thể làm nhanh hơn bằng cách
> dùng tính đối xứng của x và y

<br>

<a id="node-20"></a>

<p align="center"><kbd><img src="assets/1683c43979afbe463d5c268486f20809f8c5c1a8.png" width="100%"></kbd></p>

> [!NOTE]
> và từ base và  height ta tính ra area của tam giác và vì y0 = 1/x0,
> diện tích không còn phụ thuộc x0, y0 nữa ( = 2)

<br>

<a id="node-21"></a>

<p align="center"><kbd><img src="assets/3b927c498906231db79fc1018364496406f1c567.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói thêm một số notation: đó là derivative có thể dùng **f'(x)**, và đó
> là notation của **Newton**. Hoặc **df/dx** là **Leibniz**

> [!NOTE]
> NOTATION CỦA DERIVATIVE:
>
> NEWTON: f'
>
> LEIBNIZ: df/dx, hoặc (d/dx) f

<br>

<a id="node-22"></a>

<p align="center"><kbd><img src="assets/907998fc8b8e372bcdaf746b4263ac1318210389.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ 2. tìm derivative của f(x) = x^n.
>
> Thế thì ta cũng sẽ thiết lập biểu thức delta_f / delta_x Nhưng gs cho
> rằng ta không còn cần dùng notation x0 nữa. Mà chỉ cần biết x là fixed
> - là điểm cần tìm derivative và delta x là khoảng thay đổi của x từ đó

<br>

<a id="node-23"></a>

<p align="center"><kbd><img src="assets/c8dbce3d86800031702cf49caff36feb7cd16cbc.png" width="100%"></kbd></p>

<br>

<a id="node-24"></a>

<p align="center"><kbd><img src="assets/c4ac86d53a67f24969c740e0f0b62feb197f0106.png" width="100%"></kbd></p>

> [!NOTE]
> Gs cho rằng ta sẽ vận dụng Binomial theorem (nhị thức newton) để
> triển khai
>
> (x+delta_x)^n = x^n + x^(n-1)*delta_x + O(delta_x^2)
>
> Có nghĩa là binomial theorem,sẽ giúp ta triển (x+y)^n thành một tổng
> các biểu thức của x và y.
>
> Thế thì với x+delta_x ta**chỉ cần hai cái đầu** và gọi tất cả các term
> mà dính tới bậc cao hơn 1 của delta_x là O(delta_x^2)
>
> Đương nhiên ta hiểu rằng là m vậy là vì trong bài toán này ta sẽ tìm lim
> của nó khi  delta_x -> 0 thì O(detal_x^2) ~= 0

<br>

<a id="node-25"></a>

<p align="center"><kbd><img src="assets/b6627bbf36c6295c623d0f6e143c5cd386c93607.png" width="100%"></kbd></p>

> [!NOTE]
> và triển khai như trước ,thế delta_f = f(x+delta_x) - f(x) và rút gọn
> ta có n*x^(n-1) + O(delta_x)

<br>

<a id="node-26"></a>

<p align="center"><kbd><img src="assets/abc2697940e14bd19133be94c34a8d178592394b.png" width="100%"></kbd></p>

> [!NOTE]
> và khi tìm limit khi delta_x -> 0 Thì
> O(delta_x) = 0 và chỉ còn n*x^(n-1)

<br>

<a id="node-27"></a>

<p align="center"><kbd><img src="assets/9904b172b29947ad3466c762084f0863b5373087.png" width="100%"></kbd></p>

> [!NOTE]
> và ta sẽ có thể áp dụng
> nó như thế này

<br>

