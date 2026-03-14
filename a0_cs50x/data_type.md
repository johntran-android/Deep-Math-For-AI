# Data Type

📊 **Progress:** `8` Notes | `15` Screenshots

---
<a id="node-267"></a>

<p align="center"><kbd><img src="assets/24198edca52e07718ad6e9d199ea5ad253677adf.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ổng nói là như đã biết các ngôn ngữ ngày nay như
> Python sẽ tự biết data type của variable nhưng C hay Java thì
> cần phải define
>
> Thì với int - integer. Được represent bằng 4 bytes = 4*8 bits = 32 bit
>
> ====
>
> Integer Range -2^31 -> 2^31-1 là sao?
>
> **3 bits**: 111 = 2**2 + 2**1 + 2**0 = 4 + 2 + 1 = 7 = 8 - 1 = **2**3-1**
> **4 bits**: 1111 =2**3 + 2**2 + 2**1 + 2**0 = 8 + 4 + 2 + 1 = 15 = 16 - 1 = **2**4 - 1
> n bits**: .....**2^n - 1**
>
> Với 32 bits, **trừ 1 bit dành cho 'dấu' (dương hay âm)** thì ta **còn 31 bits**. 
>
> Thì số dương lớn nhất có thể được represent là **2**31 - 1: đó là khi bit đầu
> bằng 0 (thể hiện số dương), 31 bits tiếp theo là 1 hết.
>
> Ở giữa, khi 31 bit đều là 0 thì tất nhiên là 0**Số âm đầu tiên = -1 khi **bit đầu là 1, 31 bit tiếp theo là 0. 
>
> Do đó khi cả 31 bits tiếp theo ta thể hiện được tới số lớn nhất là 2^31 - 1.
> có nghĩa là với 31 bits đó nhỏ nhất là 0 và lớn là 2^31-1. Nhưng thay vì bắt
> đầu bởi -1 thì nay bắt đầu bởi -2 nên số lớn nhất là -2^31**

<br>

<a id="node-268"></a>

<p align="center"><kbd><img src="assets/43d4709b75150b67b4dc62e7cc0323cf8066ba33.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/43d4709b75150b67b4dc62e7cc0323cf8066ba33.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6631453fbaa32144df12e63e8bacdc8dfe93329b.png" width="100%"></kbd></p>

<br>

<a id="node-269"></a>

<p align="center"><kbd><img src="assets/8a606ecc35211b64bdef1d7115571faf4909da34.png" width="100%"></kbd></p>

> [!NOTE]
> Cái dạng **unsigned int** này nó sẽ cho phép **represent integer** ở
> **range lớn hơn bằng cách hi sinh phần negative bằng cách xài luôn cái
> bit dành cho dấu**  cộng hay trừ (tức là khi cần integer lớn hơn 2 tỉ và biết
> rằng không mang giá trị âm thì có thể dùng cái này.
>
> Và vì không support số âm nữa, nên không cần dành 1 bit cho  dấu (sign)
> nữa, nên dùng cả 32 bits cho giá trị. Thì như mới nói với 32 bits số lớn
> nhất thể hiện được sẽ là **2^32 - 1  (với 32 bits đều = 1)**

<br>

<a id="node-270"></a>

<p align="center"><kbd><img src="assets/d8400e4f828c74552229c7ec21f22d47b3695a8f.png" width="100%"></kbd></p>

> [!NOTE]
> **char data type** dùng để store một **character**. Chiếm **1 byte = 8 bits.**
>
> Với **8 bits** thì và có support số âm thì dùng 1 bit cho sign, còn lại 7 bits. Tương tự ở
> slide trước, số dương lớn nhất là 2^7-1 = 128-1 = 127 số âm nhỏ nhất là -127-1 =
> -128
>
> Và mỗi kí tự sẽ represent bằng một số theo ASCII

<br>

<a id="node-271"></a>

<p align="center"><kbd><img src="assets/a99996c42e4387cf84ee2cb6471c6c2e48df8eed.png" width="100%"></kbd></p>

> [!NOTE]
> float dùng**32 bits** để represent **real number**.  Như đã nói bên **LLM**, nó
> tổ chức theo kiểu **1 bit đầu dành cho sign**,  **8 bits tiếp dành cho exponent**,
> **23 bits tiếp theo dành cho fraction.**Và vì bị giới hạn bởi chỉ có 32 bits, trong khi phần fraction - thập phân là chuỗi
> vô hạn nên float bị vấn đề **precision - tức là không thể nào represent chính xác
> tuyệt đối.**

<br>

<a id="node-272"></a>

<p align="center"><kbd><img src="assets/2363a7de2caed2c534ed71d7c1b7503b00177dc1.png" width="100%"></kbd></p>

<br>

<a id="node-273"></a>

<p align="center"><kbd><img src="assets/85bfdb7c28b8885ca3fcb2b467a5a0fb244e810b.png" width="100%"></kbd></p>

> [!NOTE]
> Double cho phép represent real number với 64 bits từ đó
> tăng phần thập phân giúp chính xác hơn

<br>

<a id="node-274"></a>

<p align="center"><kbd><img src="assets/e64ac55f274e31a70d012012c1d2efc2ee06ffc3.png" width="100%"></kbd></p>

> [!NOTE]
> Void không hẳn là datatype, nó chỉ đơn giản là báo hiệu
> function không return cái gì hoặc không nhận argument (ví dụ
> main (void)

<br>

<a id="node-275"></a>

<p align="center"><kbd><img src="assets/f6bf2ecbd9d330340c1de1f1d78c59babc51188e.png" width="100%"></kbd></p>

<br>

<a id="node-276"></a>

<p align="center"><kbd><img src="assets/c8d6309637cac48e51b063b2ea437752e71ac41e.png" width="100%"></kbd></p>

<br>

<a id="node-277"></a>

<p align="center"><kbd><img src="assets/051d8af8bee844321387a4705c095728cf2d3f61.png" width="100%"></kbd></p>

> [!NOTE]
> Những tuần sau sẽ có structs dùng typedefs để define (gần
> gần nhưng chưa phải là class trong OOP)

<br>

<a id="node-278"></a>

<p align="center"><kbd><img src="assets/b19bfa5b7d3b4ec0c0e3c16be3ff19bc21333584.png" width="100%"></kbd></p>

> [!NOTE]
> Cách define,
> tương tự java

<br>

<a id="node-279"></a>

<p align="center"><kbd><img src="assets/b96ac3b9b7491f50d1538ddeeaeb3a1ec00dc5f9.png" width="100%"></kbd></p>

<br>

