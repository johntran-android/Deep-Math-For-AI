# PS: FILTER I + II (II chỉ có thêm Edge)

📊 **Progress:** `4` Notes | `25` Screenshots

---

Quay lại Note & Giải thích
<a id="node-900"></a>

<p align="center"><kbd><img src="assets/851b650bd10f6e0bf4ebb16553e977fc37ff6396.png" width="100%"></kbd></p>

<br>

<a id="node-901"></a>

<p align="center"><kbd><img src="assets/81aa4581b6acdb1ffcc01938ae1f7ff4c3c13cf2.png" width="100%"></kbd></p>

<br>

<a id="node-902"></a>

<p align="center"><kbd><img src="assets/957faf283bdee6aece6aee269ce50e52938c584a.png" width="100%"></kbd></p>

<br>

<a id="node-903"></a>

<p align="center"><kbd><img src="assets/9b250b3b346006e98320b54a46c55dbe6569b12b.png" width="100%"></kbd></p>

<br>

<a id="node-904"></a>

<p align="center"><kbd><img src="assets/c67884eb67b9e54ca8a6204f31c137581150e689.png" width="100%"></kbd></p>

<br>

<a id="node-905"></a>

<p align="center"><kbd><img src="assets/ea5ed3ebf0a3bfb31a279ffdd508003b4030c826.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ea5ed3ebf0a3bfb31a279ffdd508003b4030c826.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b2fa5c0594f87fcb3480c696a499ea73aeb03471.png" width="100%"></kbd></p>

<br>

<a id="node-906"></a>

<p align="center"><kbd><img src="assets/816ae2ea34c8f458a626397a4d45886203b129ab.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là mọi file đều chỉ là chuỗi 0101 binary. Hay
> Cũng là chuỗi các 8 bít `=` 1 bytes
>
> Và file format chính là cách để thế giới quy ước nhau
> file gì là như thế nào, chính là bằng các byte đầu tiên
> tạo thành header
>
> Thì đại khái ví dụ ở Lab Volume.c ta thấy file jpeg
> có phần header là 44 bytes mang giá trị thể hiện size,
> ...mà mình đã load bằng uint8_t (vì nó không có số
> âm) và sau đó là chuỗi binary mà cứ 2 bytes là một
> nốt (samples) và ta load vào một int16_t
>
> Thì ý nói là mình có thể đặt ra struct để thuận tiện hơn
> cho việc load data

<br>

<a id="node-907"></a>

<p align="center"><kbd><img src="assets/2b39f99efdfad0a9d2d41f31df372dc118d89e44.png" width="100%"></kbd></p>

<br>

<a id="node-908"></a>

<p align="center"><kbd><img src="assets/5969b87f15f134ee80595a280bd358ebbd06a1be.png" width="100%"></kbd></p>

> [!NOTE]
> Cái này thì chính là convol operation. Hai
> matrix Gx, Gy chính là là hai filter
>
> Như ta đã biết, khi nhân filter 3x3 với matrix 3x3
> của image (trên một channel `Red/Green/Blue)`
> thì nếu...

<br>

<a id="node-909"></a>

<p align="center"><kbd><img src="assets/acce868464aa6b4211a2dff465e6b92e950574b5.png" width="100%"></kbd></p>

<br>

<a id="node-910"></a>

<p align="center"><kbd><img src="assets/2512d8b89541826633356c62b9377d2ddff875d7.png" width="100%"></kbd></p>

<br>

<a id="node-911"></a>

<p align="center"><kbd><img src="assets/14253931dcb58662aef50dff43379cc444e2815c.png" width="100%"></kbd></p>

<br>

<a id="node-912"></a>

<p align="center"><kbd><img src="assets/1f07faea2fdf613c956e1c9589767849297bb2e2.png" width="100%"></kbd></p>

<br>

<a id="node-913"></a>

<p align="center"><kbd><img src="assets/eb4cf0ab302242e789bfabd882fc5fc0d68bbffe.png" width="100%"></kbd></p>

<br>

<a id="node-914"></a>

<p align="center"><kbd><img src="assets/d4434ac04ccdae3a29ef51331061cb0c82679eb8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d4434ac04ccdae3a29ef51331061cb0c82679eb8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4f7cc855f81f33e4646e03708d0525cd2e733be1.png" width="100%"></kbd></p>

<br>

<a id="node-915"></a>

<p align="center"><kbd><img src="assets/c980d91a28f1a56d35a7c97d48e112522a843b89.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c980d91a28f1a56d35a7c97d48e112522a843b89.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/98490877d9074215aac909088eb8ff332913fe79.png" width="100%"></kbd></p>

> [!NOTE]
> Tại sao dùng RGBTRIPLE newValue không
> work?
>
> Có thể là chỉ khởi tạo RGBTRIPLE newValue
> thì chỉ là  pointer, chưa có memory, giống như
> string vậy. Cần thử lại chỗ này

<br>

<a id="node-916"></a>

<p align="center"><kbd><img src="assets/a94d86086b454472ed16cefab6f081ab671b8d88.png" width="100%"></kbd></p>

<br>

<a id="node-917"></a>

<p align="center"><kbd><img src="assets/85023e7aaed9389ab7cbd39e73d7a777884e75f0.png" width="100%"></kbd></p>

<br>

<a id="node-918"></a>

<p align="center"><kbd><img src="assets/a75778d126e3e2fa1e8e953fd3395ada6d4b6a56.png" width="100%"></kbd></p>

<br>

