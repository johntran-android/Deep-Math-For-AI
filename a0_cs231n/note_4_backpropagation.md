# Note #4 Backpropagation

📊 **Progress:** `9` Notes | `13` Screenshots

---
<a id="node-361"></a>

<p align="center"><kbd><img src="assets/fe8955c2c494e0ead2454724102448944700d6a2.png" width="100%"></kbd></p>

<br>

<a id="node-362"></a>

<p align="center"><kbd><img src="assets/625c20b1df206256ac44c6469982c4dbc35bb0cf.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói về ý nghĩa của đạo hàm là tỉ lệ của khoảng thay
> đổi của hàm f trên khoảng thay đổi vô cùng nhỏ (infinitesimally)
> của x.
>
> Và kí hiệu df/dx không phải ý chia df cho dx mà là kí hiệu chỉ việc
> tính ra đạo hàm của hàm f w.r.t (đối với) x và nó cũng là một hàm
> số

<br>

<a id="node-363"></a>

<p align="center"><kbd><img src="assets/24da9df4cd8337413f4f31253cc90860620234d3.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là chính vì ý nghĩa đạo hàm như vậy nên có thể hiểu nó như
> **sự nhạy cảm** của function f (khi x thay đổi tác động đến f thay đổi
> nhiều hay ít ra sao)
>
> Tiếp theo như đã biết khi f là function của**hai  variable x, y** hay của
> một variable nhưng dưới dạng  **vector [x, y]** thì đạo hàm của f đối với
> input là **vector  các partial derivative.**
>
> Nói qua ý nghĩa của đạo hàm của hàm**f = x + y**đối với x, hay y đều
> bằng **1**. Vì rõ ràng với hàm sum như này thì **x thay đổi bao nhiêu thì f
> thay đổi bấy nhiêu**, thành ra **tỉ lệ  của hai khoảng thay đổi là 1.**
>
> Còn với hàm **max** (x, y) thì rõ ràng là vì **nếu y nhỏ hơn x**, thì**hàm f chỉ
> được tính bởi x**, do đó c**hỉ có x tác động lên f**, còn y thì không nên y
> có thay đổi (nhỏ) bao nhiêu thì f vẫn vậy nên đạo hàm của f đối với y
> là 0, và **với x là 1 (vì khi đó như hàm  f = x)**

<br>

<a id="node-364"></a>

<p align="center"><kbd><img src="assets/385c2a66486e5e4cf3ed4706590525a674d2cf88.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là mô phỏng một cách đơn giản quá trình forward
> prop với việc tính q từ xây và f từ q, z và backprop với việc
> tính df/dx, df/dy, df/dz thông qua chain rule với df/dq
>
> Các công thức tính gradient thì như đã biết ở phần trên

<br>

<a id="node-365"></a>

<p align="center"><kbd><img src="assets/a62fec2c6fffab2015fbb94878ce97f6b16d0d0e.png" width="100%"></kbd></p>

> [!NOTE]
> từ sau sẽ viết tắt
> dfdx là dx thôi

<br>

<a id="node-366"></a>

<p align="center"><kbd><img src="assets/397dc4671f956a04950f4381a6ab01b6fc72cb5d.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là backprop sẽ như cách các gate giao tiếp với nhau để kiểu
> như node sau báo cho node trước biết: à, mà mà tăng 1 khoảng chút
> xíu thì hệ quả f cuối sẽ tăng hay giảm khoảng như vậy. Từ đó cả đám
> sẽ dựa vào đó mà thay đổi sao đó để đạt mục đích chung

<br>

<a id="node-367"></a>

<p align="center"><kbd><img src="assets/33e83b3a40f4aed28f79591c1940f6e01e98ee3e.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là cái khái niệm **gate (hay node)** ở trên về cơ bản có thể là bất
> kì một function nào mà **differentiable** nào. Và ta**có thể
> nhóm các gate lại (hay node)** thành một node bự hơn hoặc
> **chia nhỏ ra** để thuận tiện
>
> Cung cấp thêm một số công thức tính đạo hàm của các function
> với vụ **unary gate** ý nói các function f = x + c hay a*x là hàm đơn biến
> vì c với a là constant **nên chỉ có 1 nhánh input**

<br>

<a id="node-368"></a>

<p align="center"><kbd><img src="assets/ea92061e534ff4c80a576ef7eaec8ff924825ac7.png" width="100%"></kbd></p>

> [!NOTE]
> ví dụ này đã triển
> khai ở bài trước

<br>

<a id="node-369"></a>

<p align="center"><kbd><img src="assets/10cd2bf0d046d5021fb831d4430cb2f720dcbed0.png" width="100%"></kbd></p>

> [!NOTE]
> nói về đạo hàm của hàm sigmoid, và khi tính
> toán có thể coi sigmoid là 1 gate (gồm các gate
> nhỏ hơn) để khi backprop thì dùng công thức
> này để tính local gradient

<br>

<a id="node-370"></a>

<p align="center"><kbd><img src="assets/0fbc5763508b44320a65515f99363e5e890a309b.png" width="100%"></kbd></p>

> [!NOTE]
> Theo computational graph thì khi backprop, tại z (hay ở dưới là dot) input
> của sigmoid (= weighted sum của x và w) ta có df/dz là (1-f)*f. và local
> gradient tại node z = vector x.dot product với vector w, dz/dw sẽ là vector x,
> thành ra df/dw là ddot*x.
>
> Thì nhờ dùng local gradient của sigmoid tức là coi sigmoid là 1 node nên 
> việc tính toán gọn hơn

<br>

<a id="node-371"></a>

<p align="center"><kbd><img src="assets/49b7ea645cc07eeaa41dfd6624eab3e5ab13044e.png" width="100%"></kbd></p>

<br>

<a id="node-372"></a>

<p align="center"><kbd><img src="assets/08594e0a04ce7e428d5d605360a2059c193bf90b.png" width="100%"></kbd></p>

<br>

<a id="node-373"></a>

<p align="center"><kbd><img src="assets/1caf8d968148ef221e704a07530882107b943b1c.png" width="100%"></kbd></p>

<br>

