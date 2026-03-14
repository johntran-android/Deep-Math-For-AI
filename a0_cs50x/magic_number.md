# Magic Number

📊 **Progress:** `6` Notes | `7` Screenshots

---
<a id="node-302"></a>

<p align="center"><kbd><img src="assets/65e0f24e05f7e46676f22a4ec908e150f97ff051.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là có đôi khi ta cần sử dụng một hardcode
> value như chiều cao của kim tự tháp Mario gì đó,
> hoặc số lá của bộ bài. Thì thay vì để khơi khơi thì ý
> nói là **nên define dạng constant để dễ hiểu hơn cho
> người khác khi đọc code.**

<br>

<a id="node-303"></a>

<p align="center"><kbd><img src="assets/6be8f90c430469a98b17fa1fb40ea963ed3c5959.png" width="100%"></kbd></p>

<br>

<a id="node-304"></a>

<p align="center"><kbd><img src="assets/2c59ca6e3ce2deaed07650d14336b602ef6949c8.png" width="100%"></kbd></p>

> [!NOTE]
> Có thể như vầy, define local variable, hoặc thậm
> chí là global variable thì vẫn tiềm ẩn rủi ro là ai đó
> sẽ update và thay đổi value

<br>

<a id="node-305"></a>

<p align="center"><kbd><img src="assets/63b495723ebfb3ce9dd12cf000e63c32bea3c96b.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó trong C nó có vụ này #define gọi là pound
> define... kiểu như khi compile code, máy tính nó
> sẽ tìm và thay thế chỗ nào có NAME và replace
> với REPLACEMENT

<br>

<a id="node-306"></a>

<p align="center"><kbd><img src="assets/06c88760ff3aa529cb46ad4291c2814559d825e7.png" width="100%"></kbd></p>

> [!NOTE]
> bằng cách đó, chỗ nào cần dùng value vủa Pi = 3.
> 14.. thì ta chỉ cần dùng PI. Cái này cũng hơi giống
> như final variable của Java vậy

<br>

<a id="node-307"></a>

<p align="center"><kbd><img src="assets/581b64e60451a7db51e122a9e2fe63fc5ca95fde.png" width="100%"></kbd></p>

> [!NOTE]
> Và có thể define cho mọi datatype. Và theo
> convention thì dùng viết hoa

<br>

<a id="node-308"></a>

<p align="center"><kbd><img src="assets/0c44af830e6f1ff9188f6b5459735f6f59f25a91.png" width="100%"></kbd></p>

> [!NOTE]
> Với cách này, không sợ bị thay đổi giá trị của deck
> size. Ngoài ra một benefit nữa là giả sử deal với bộ
> bài có 32 lá như ở German thì chỉ cần đổi
> DECKSIZE=32.

<br>

