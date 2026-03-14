# Week 4 - Memory

📊 **Progress:** `129` Notes | `189` Screenshots

---
<a id="node-590"></a>

<p align="center"><kbd><img src="assets/5fdb44e34bd3ed38c228e1362e3be1e41673905f.png" width="100%"></kbd></p>

<br>

<a id="node-591"></a>

<p align="center"><kbd><img src="assets/4963660646bd9a8433b08466bfa233dac876ff00.png" width="100%"></kbd></p>

> [!NOTE]
> Image khi zoom in zoom in .... thì được cấu
> thành bởi các pixel như ta đã biết image là
> tensor dài x rộng x 3 channel (RGB)

<br>

<a id="node-592"></a>

<p align="center"><kbd><img src="assets/99051c1e624695e77a185ada7058c3e1853ffd79.png" width="100%"></kbd></p>

> [!NOTE]
> Bitmap: a map of bit
>
> D: Nếu 1 là black, 0 là white thì cái này là hình gì?
>
> A: Mặt cười :)

<br>

<a id="node-593"></a>

<p align="center"><kbd><img src="assets/80fe7cde544b0fb4f20b7d45d3cc81bd2c82c6c6.png" width="100%"></kbd></p>

<br>

<a id="node-594"></a>

<p align="center"><kbd><img src="assets/ce6ada43f1f6247e720780fe941c7e3cf99892d8.png" width="100%"></kbd></p>

<br>

<a id="node-595"></a>

<p align="center"><kbd><img src="assets/587c505a8133eb71ed4ecae827ddfcc1679f2ace.png" width="100%"></kbd></p>

<br>

<a id="node-596"></a>

<p align="center"><kbd><img src="assets/37632b635be42a366a20ee0f02d58791bff17fb1.png" width="100%"></kbd></p>

<br>

<a id="node-597"></a>

<p align="center"><kbd><img src="assets/61fc181be246191819a4e3fa731040d4f556795c.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng chưa nói gì nhiều chỉ là nói sơ qua việc các trình như
> PTS có cái color picker này, và điều chỉnh Red Blue Green
> mỗi cái từ 0- 255 để thay đổi màu. Nếu mà là 0-0-0 hết thì
> là màu trắng, red 255 blue 0 green 0 thì là màu red. Thì có
> vẻ nó có quy luật của cái color code mà mình xài quài
> #ff0000

<br>

<a id="node-598"></a>

<p align="center"><kbd><img src="assets/b94d917da3fa903bd07eba252c618ab2bb7a6e48.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b94d917da3fa903bd07eba252c618ab2bb7a6e48.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/553872a5249e48baafc92b71c63b1ab4e06847dc.png" width="100%"></kbd></p>

<br>

<a id="node-599"></a>

<p align="center"><kbd><img src="assets/3a61053cbfcc37e8c3436ac64b3ccff5a865e621.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3a61053cbfcc37e8c3436ac64b3ccff5a865e621.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/14e15c13962ff7fad1b934ba2ea6e0c1520390e2.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta sẽ xài 1 hệ khác
> không phải binary base - 2 (1,0), decimal base - 10 (1,2..9)
>
> mà là hexadecimal - base- 16. Và dùng **0 1 2..9 A B C D E F**

<br>

<a id="node-600"></a>

<p align="center"><kbd><img src="assets/628374ca3f72aa5bd19a09d44dd398266e6869ff.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/628374ca3f72aa5bd19a09d44dd398266e6869ff.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/92d75503db2f28d3f3ac507397157eb7eaeb17fd.png" width="100%"></kbd></p>

> [!NOTE]
> Thì tương tự các thể hiện
> các con số trong hệ
>
> Với base 2:
>
>  0 = 00000000 = ...............0*2^1 + 0*2^0
>  1 = 00000001 = ...............0*2^1 + 1*2^0
>  2 = 00000010 = ...............1*2^1 + 0*2^0 
>  3 = 00000011 = ...............1*2^1 + 1*2^0
>  4 = 00000100 = ..................1*2^2 + 0*2^1 + 0*2^0
> **15**= 0000**1111** = .................1*2^3 + 1*2^2 + 1*2^1 + 1*2^0
> **255** = **11111111** = 1*2^7 + 1*2^6 + 1*2^5 + 1*2^4 + 1*2^3 + 1*2^2 + 1*2^1 + 1*2^0 
> = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255
>
> Với base 10:
>
>    0 = 00000000 = ..........................0*10^1 + 0*10^0
>    1 = 00000001 =...........................0*10^1 + 1*10^0
>    2 = 00000002 =...........................0*10^1 + 2*10^0
>    3 = 00000003 =...........................0*10^1 + 3*10^0
> ...
>    9 = 00000001 =............................0*10^1 + 9*10^0
>   10=00000010 =.............................1*10^1 + 0*10^0
>   11=00000011 =.............................1*10^1 + 1*10^0
>   12=00000012 =.............................1*10^1 + 2*10^0
>   19=00000019 =.............................1*10^1 + 9*10^0
>   20=00000020 =.............................2*10^1 + 0*10^0
>   99=00000099 =.............................9*10^1 + 9*10^0
> 100=000000100 =............1*10^2 + 0*10^1 + 0*10^0
>
> Với base 16: xài hết các chữ số 0-9,mượn A, B, C, D, E, F thay cho 10,11,12,13,14,15 
>
> 0 = ................0 = .........................................................0*16^1 + 0*16^0
> 1 = ................1 = .........................................................0*16^1 + 1*16^0
> ...
> 9 = ................9 = .........................................................0*16^1 + 9*16^0
> 10 = ..............A = .........................................................0*16^1 + 10*16^0 (hay A*16^0 cũng được A = 10)
> **15** = ..............**F** = .........................................................0*16^1 + 15*16^0 (hay F*16^0 cũng được F = 15)
> 16 = ............10 = .........................................................1*16^1 + 0*16^0
> 17 = ............11 = .........................................................1*16^1 + 1*16^0
> 18 = ............12 = .........................................................1*16^1 + 2*16^0
> ...
> 25 = ............19 = .........................................................1*16^1 + 9*16^0
> 26 = ............1A = .........................................................1*16^1 + 10*16^0 (hay A*16^0 cũng được A = 10)
> 27 = ............1B = .........................................................1*16^1 + 11*16^0 (hay B*16^0 cũng được B = 11)
> 28 = ............1C = .........................................................1*16^1 + 12*16^0 (hay C*16^0 cũng được C = 12)
> 29 = ............1D = .........................................................1*16^1 + 13*16^0 (hay D*16^0 cũng được D = 13)
> 30 = ............1E = .........................................................1*16^1 + 14*16^0 (hay E*16^0 cũng được E = 14)
> 31 = ............1F = .........................................................1*16^1 + 15*16^0 (hay F*16^0 cũng được F = 15)
> 32 = ............20 = .........................................................2*16^1 + 00*16^0
> 33 = ............21 = .........................................................2*16^1 + 01*16^0
> 41 = ............29 = .........................................................2*16^1 + 09*16^0
> 42 = ............2A = .........................................................2*16^1 + 10*16^0 (hay A*16^0 cũng được A = 10)
> 43 = ............2B = .........................................................2*16^1 + 11*16^0 (hay B*16^0 cũng được B = 11)
> 44 = ............2C = .........................................................2*16^1 + 12*16^0 (hay C*16^0 cũng được C = 12)
> 45 = ............2D = .........................................................2*16^1 + 13*16^0 (hay D*16^0 cũng được D = 13)
> 46 = ............2E = .........................................................2*16^1 + 14*16^0 (hay E*16^0 cũng được E = 14)
> 47 = ............2F = .........................................................2*16^1 + 15*16^0 (hay F*16^0 cũng được F = 15)
> 48 = ............30 = .........................................................3*16^1 + 00*16^0
> ..
> **255** = ............**FF** = .........................................................15*16^1 + 15*16^0
>
> Thì ra ff thì ff là 255, nên mã ffffff có nghĩa là red = 255, green = 255, blue = 255

<br>

<a id="node-601"></a>

<p align="center"><kbd><img src="assets/92820c92166e3df7ed2e550691358a22218901da.png" width="100%"></kbd></p>

> [!NOTE]
> 0*16^1 + 2*16^0 = 2

<br>

<a id="node-602"></a>

<p align="center"><kbd><img src="assets/126b26a54ab752702897fc43feda4bb3ab95ef46.png" width="100%"></kbd></p>

> [!NOTE]
> 0*16^1 + 9*16^0 = 9

<br>

<a id="node-603"></a>

<p align="center"><kbd><img src="assets/b323ca374f0fad91f425bd4db4be24af3822c248.png" width="100%"></kbd></p>

> [!NOTE]
> 0*16^1 + A*16^0 = A = 10

<br>

<a id="node-604"></a>

<p align="center"><kbd><img src="assets/24ab3dbed450af5c2548a69d47210a279995c6a5.png" width="100%"></kbd></p>

> [!NOTE]
> 0*16^1 + B*16^0 = 11

<br>

<a id="node-605"></a>

<p align="center"><kbd><img src="assets/5a55c0925bdca702fba0df1b12a50f0939f16360.png" width="100%"></kbd></p>

> [!NOTE]
> 15

<br>

<a id="node-606"></a>

<p align="center"><kbd><img src="assets/fa692cbe8611287ee88c2a97f98644daf425436e.png" width="100%"></kbd></p>

> [!NOTE]
> D: Vậy 16 là sao? A: 10

<br>

<a id="node-607"></a>

<p align="center"><kbd><img src="assets/3c9fa008f1eba6d5974486837f18e7d920b997ad.png" width="100%"></kbd></p>

> [!NOTE]
> Correct! Đừng đọc "ten",
> mà đọc "one zero"

<br>

<a id="node-608"></a>

<p align="center"><kbd><img src="assets/25d4143b4cbee6e009bcb24fd8e75d3fd29d3ab5.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/25d4143b4cbee6e009bcb24fd8e75d3fd29d3ab5.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4eb03a49bc9a043ed4615fbfcb4de41302b89ff9.png" width="100%"></kbd></p>

> [!NOTE]
> FF = F*16^1 + F*16^0 = 15*16 + 15 =  255

<br>

<a id="node-609"></a>

<p align="center"><kbd><img src="assets/f2c84df1815a7337b3bb6294f36b72c14713e84f.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy t**ại sao lại dùng hexadecinmal**, phải làm phức tạp như 
> vậy?
>
> D: trước tiên ổng hỏi: 
> Để represent 15 trong binary cần bao nhiêu bit?
>
> A: 15 = 1*2^3 + 1*2^2 + 1*2^1 + 1*2^0 = 8 + 4 + 2 + 1 = 1111
> -> **cần 4 bit**

<br>

<a id="node-610"></a>

<p align="center"><kbd><img src="assets/f61d311450fa7d675d42a5ebdfd45bb6d7521f3f.png" width="100%"></kbd></p>

> [!NOTE]
> D: Correct, và hexadecimal là cách để thể hiện gọn hơn 
> binary
>
> Thay vì thể hiện **15** = **1111** với binary thì 
> sẽ là **F** với base-16
>
> Thay vì thể hiện **255** = **11111111** với binary thì 
> sẽ là **FF** với base-16

<br>

<a id="node-611"></a>

<p align="center"><kbd><img src="assets/789719d8220c1d2f16d4675543069c3565ac7c77.png" width="100%"></kbd></p>

> [!NOTE]
> 255 trong base-2

<br>

<a id="node-612"></a>

<p align="center"><kbd><img src="assets/1a9a239a699ee8563ee481e82159f0f4627bdd5c.png" width="100%"></kbd></p>

> [!NOTE]
> 255 trong base-16

<br>

<a id="node-613"></a>

<p align="center"><kbd><img src="assets/dd401aa35abdf7672250fcd8b199ab342ebfa624.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Vậy ở bên dưới **F là 4 bits** phải ko?
>
> D: Đúng, nó chỉ là cách để human đọc cho gọn thôi, nó vẫn
> tương đương **1111 = 4 bits**.
>
> Nên cứ **mỗi kí tự (số) của hexadecimal** là máy tính phải **chuẩn
> bị 4 bit.**
>
> **2 kí tự trong hexadecimal** phải chuẩn bị **8 bits** (để nếu nó là
> max = FF thì tương đương 11111111)

<br>

<a id="node-614"></a>

<p align="center"><kbd><img src="assets/5fa3bd1d5db6a84524a74819931e8e2845763675.png" width="100%"></kbd></p>

<br>

<a id="node-615"></a>

<p align="center"><kbd><img src="assets/8f8cc9040f3d1668f5d632d359f0e0ba5b7d869d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái tuần trước đã nói, mỗi ô này tượng trưng 1 byte = 8
> bit trong memory, và ta có thể **đánh số nó byte 0, byte 1...
> byte 1 triệu (như gigabyte) gọi nôm na là ADDRESS**

<br>

<a id="node-616"></a>

<p align="center"><kbd><img src="assets/b9a67b7b87246458cc470a2650e05d465b222ce1.png" width="100%"></kbd></p>

> [!NOTE]
> Và người ta cũng dùng
> **base-16** để đánh **index**

<br>

<a id="node-617"></a>

<p align="center"><kbd><img src="assets/38f687cdf3c389e07aeb9fbf555e1a0e11ac917a.png" width="100%"></kbd></p>

> [!NOTE]
> D: Có ai thấy có vấn đề gì nếu ta dùng
> base-16 để đánh số thứ tự như này
>
> -> Đó là **dễ bị lầm lẫn**, 10 thực ra là 16....

<br>

<a id="node-618"></a>

<p align="center"><kbd><img src="assets/6c9c4265394d6b3193becee38a058257f5af9bbc.png" width="100%"></kbd></p>

> [!NOTE]
> Nên đại khái là người ta convention là khi thể hiện ở base-16
> thì người ta ghi theo kiểu này prefix mọi digit với **0x**...
>
> Từ đó thì thấy **0x10** sẽ ko bị lầm lẫn là 10, mà sẽ hiểu đó
> cái byte kế tiếp của byte thứ **0xF** = 15, chính là 16 trong
> base-16

<br>

<a id="node-619"></a>

<p align="center"><kbd><img src="assets/267002b350c3effd269c3a0e0d23cd7ff5b58906.png" width="100%"></kbd></p>

> [!NOTE]
> một đoạn code đơn giản in giá
> trị của int variable n

<br>

<a id="node-620"></a>

<p align="center"><kbd><img src="assets/9672e4c237e472b6ac15f635d9e62af188c50332.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là **dù ta không care** máy tính nó **"bỏ" con số
> này ở đâu trong memory**
>
> nhưng ta cứ thử  hình dung rằng **đâu đó trong memory có 4 ô
> (bytes)** được gán cho variable n này và 4 byte đó có **chuỗi
> binary mang giá trị 50**
>
> D: **Tại sao lại 4 ô?**
>
> A: Vì **int** sẽ được **assign 4 bytes**, long 8 bytes

<br>

<a id="node-621"></a>

<p align="center"><kbd><img src="assets/393bd1a09428d687ec7d99f9d5a915684a2ea021.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói ví dụ rằng nó nằm ở **address** (byte index này) 
> trong memory: **0x123**
>
> Thử translate sang hexadecimal là số bao nhiêu:
>
> 123 = **1***16^2 + **2**^16^1 + **3***16^0 = 256 + 32 + 3 =**291
>
> Hay nói cách khác nó nằm ở byte thứ 291 trong memory**

<br>

<a id="node-622"></a>

<p align="center"><kbd><img src="assets/1b5f64732811d9b0c084a375b104be766ecd321e.png" width="100%"></kbd></p>

> [!NOTE]
> **& (ampersand)** sẽ trả về cho ta**address của cái variable** 
> đó trong memory.
>
> Ví dụ **0x123**
>
> Còn ***** thì đại khái là **go-there, đi vào đó, đi tới address đó**
>
> Minh hoạ sẽ hiểu

<br>

<a id="node-623"></a>

<p align="center"><kbd><img src="assets/b553a8e1216b6328a11b1b5e672ba3445ab2d92d.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng sẽ dùng print với **%p**, **&n** là như đã nói, & sẽ
> **lấy address của variable n** trong memory. Và vì nó là
> **address**, một loại datatype khác nên có **format code
> cho nó là %p,**
>
> giống như %i cho int, %s cho string

<br>

<a id="node-624"></a>

<p align="center"><kbd><img src="assets/03615f7e7970dbeeffe6419d17f93352348f2908.png" width="100%"></kbd></p>

> [!NOTE]
> **0x7ffcc784...4c** chính là **address thật của variable n**,
> vì máy tính ngày nay có **memory lớn** nên con số " địa
> chỉ" này là con số rất lớn

<br>

<a id="node-625"></a>

<p align="center"><kbd><img src="assets/1ae6db96548c109763bc22d015fbce16366d44ab.png" width="100%"></kbd></p>

> [!NOTE]
> Xong đến cái **pointers**. Chính là cái khiến C khó. Đại khái
> là nó sẽ **cho phép ta "động chạm" với memory -
> hardware của máy tính.**
> Đây là những **lớp gần gần với ở dưới** - low level
> language như **Assembly**
>
> Và từ đó có những **powerful ability** nhưng cũng đi kèm
> theo là **responsibility** vì sẽ dễ **break the program** nếu làm
> sai

<br>

<a id="node-626"></a>

<p align="center"><kbd><img src="assets/acd2757a369e3e8cdc0a555cad5be74a6a69a419.png" width="100%"></kbd></p>

> [!NOTE]
> **Pointers** có thể hiểu là **address của some
> variable in memory**

<br>

<a id="node-627"></a>

<p align="center"><kbd><img src="assets/8fb85ecb1bff55368767101fadf5aa578b1c249e.png" width="100%"></kbd></p>

> [!NOTE]
> p là **pointer**, là **address**của variable n in memory.
>
> **int** ***p** ý nói **p không phải int variable** mà là **address của 
> một int variable**trong memory.
>
> Và đương nhiên **address cũng là một con số nào đó,**ví dụ như 0#123 = 291

<br>

<a id="node-628"></a>

<p align="center"><kbd><img src="assets/5576764b027a81ca0e36d385c32011002653b05e.png" width="100%"></kbd></p>

> [!NOTE]
> Nên ổng sửa lại kiểu này
>
> Declare**p là variable** nhưng mà là **chứa address** (thể hiện cho 
> máy tính biết bằng ***p**)
>
> (khai báo **int *p;** là máy tính nó biết p là  variable chứa address 
> của một int variable rồi, nhưng chưa có gía trị.
>
> Khi assign **int *p = &n** thì máy tính nó biết: "**à, p chứa address
> của variable n"**Và vẫn dùng format **%p** để in **pointer**

<br>

<a id="node-629"></a>

<p align="center"><kbd><img src="assets/b40f9fba910a69e622d3f3eda034e69a4c2ae8e6.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Có phải **mỗi lần run chương trình này là nó sẽ dùng 
> address memory** khác  ko (ý nói là 1 address khác)
>
> D: Shortly **yes**.

<br>

<a id="node-630"></a>

<p align="center"><kbd><img src="assets/fa0169c76047a9e6276cf4ea7396d91e6330a598.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là đáng lý **hồi xưa khi tạo ra C** người ta nên
> **dùng một type ví dụ như pointer** để **chỉ variable chứa address**
>
> Nhưng**int *p** thật ra **chính là ý nghĩa này**, declare **p** là một
> **variable** và value của nó là **address đến một int variable (n)**Tóm lại:**int *p = &n**: Declare**a variable thuộc loại pointer** = chuyên **chứa
> address trong memory** của một int variable.
>
> Và khi **print("%p", p)** thì (p không có * gì), thì chỉ đơn giản là in
> value của nó ra (và vì value của nó là pointer, là address nên
> có format riêng:**%p**

<br>

<a id="node-631"></a>

<p align="center"><kbd><img src="assets/e7a3e5f6c9fa0fac7a06f68f6b038dda6dd62bce.png" width="100%"></kbd></p>

> [!NOTE]
> n là một variable loại **int** được cho 4 bytes (đang mang
> giá trị 50)
>
> thì p là một variable dạng **address**, được assign **8
> bytes**, mang giá trị là address của n **cũng là một
> number**, thể hiện cái byte thứ bao nhiêu trong bộ nhớ
> của n
>
> Ví dụ ở đây nó 8 bytes này mang giá trị  **0x123**=
> 1*16^2 + 2*16^1 + 3*16^0 = **291**
>
> **1 0010 0011** (**1*****2^8** + 0*2^7 + **1*2^5** ...+
> **1*****2^1** + 1***2^0**)  = 256 + 32 + 2 + 1 =291
>
> (và tất nhiên như đã nói base-16 chỉ để human gọn hơn
> chứ bên trong memory nó vẫn là binary)

<br>

<a id="node-632"></a>

<p align="center"><kbd><img src="assets/8b3854d1803607bf1e71cf20556e811ac8ae1308.png" width="100%"></kbd></p>

> [!NOTE]
> D: 8 ô là sao?
>
> A: Thì có nghĩa là máy tính nó cho (một var) loại address **8 bytes**
>
> D: Correct

<br>

<a id="node-633"></a>

<p align="center"><kbd><img src="assets/0daa10dba1771b9385c53a7035124c8dcef970c0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0daa10dba1771b9385c53a7035124c8dcef970c0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/46c517bf0b12da9c0c5975e5c5bd7e0b178d9c33.png" width="100%"></kbd></p>

> [!NOTE]
> Và thật ra **chẳng ai quan tâm giá trị của p là gì**, vì ngày
> nay nó thế này, ngày mai có thể nó thế khác, do đó
> người ta chỉ quan tâm à, **với p, thì nó mang address
> của n**. Thể hiện là **pointer**

<br>

<a id="node-634"></a>

<p align="center"><kbd><img src="assets/c0db1894fabfda56c00c78a670bd3c86d2b7b846.png" width="100%"></kbd></p>

> [!NOTE]
> D: Nếu tôi **mở mail box P** thì cái gì trong đó?
>
> A: giá trị của p sẽ là **address của n trong memory = 0x123**

<br>

<a id="node-635"></a>

<p align="center"><kbd><img src="assets/370b76b0bd399af099af96fc3682da16736bbf59.png" width="100%"></kbd></p>

> [!NOTE]
> Correct!

<br>

<a id="node-636"></a>

<p align="center"><kbd><img src="assets/1000254f6a2527a8ab0ad0e6dd8d3bab8573b353.png" width="100%"></kbd></p>

> [!NOTE]
> Và giá trị của p là address của n nên sẽ **giúp kiểu như
> nếu ta mò mẫm trong memory**, thì sẽ giúp **tìm được
> phần memory gắn với n nằm ở đâu**

<br>

<a id="node-637"></a>

<p align="center"><kbd><img src="assets/768e37a9fea711ef3d35882abe8a78ff66d093bd.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó tìm được valua của n là chuỗi binary 4 byte có trị giá 50

<br>

<a id="node-638"></a>

<p align="center"><kbd><img src="assets/c21fc37cc9b5b946f3f9eb9a8a6742fe57a6fc5a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c21fc37cc9b5b946f3f9eb9a8a6742fe57a6fc5a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9a8c1cc6811881941a6d3bfd838ae0c3e0cf16e9.png" width="100%"></kbd></p>

> [!NOTE]
> Nhắc lại khi ta define một **string** (bản thân là một **array các
> char**, mỗi char được một byte) thì máy tính nó tự **add 1
> byte** ở cuối cho **'\\0'**
> Nên nếu **define string s = "a" sẽ là 2 bytes (a, \\0)**, khác với define
> một char 'a' chỉ có 1 byte
>
> Và cái string này nằm ở đâu đó trong memory ta không care

<br>

<a id="node-639"></a>

<p align="center"><kbd><img src="assets/83ae4fdaec2eca15d99c01e39a5b72bb075da276.png" width="100%"></kbd></p>

<br>

<a id="node-640"></a>

<p align="center"><kbd><img src="assets/1a3948269181dce9205f5cad892b1b2adcd9a4ae.png" width="100%"></kbd></p>

<br>

<a id="node-641"></a>

<p align="center"><kbd><img src="assets/51ea86f311f3b6f8ab4ed4d16cc40b58b0f29b71.png" width="100%"></kbd></p>

> [!NOTE]
> Mỗi **char** sẽ có **một address trong memory**, thì sẽ
> có **một variable loại pointer** mang giá trị là cái
> **address của char đầu tiên ('H')**

<br>

<a id="node-642"></a>

<p align="center"><kbd><img src="assets/9fc816b83e53b367c592829700655bbfea73c918.png" width="100%"></kbd></p>

> [!NOTE]
> Thì cái pointer đó chính là **s**
>
> Vậy thật ra **string** là một **pointer**, mang **address** của **char
> đầu tiên** trong chuỗi các char
>
> Vậy khi **khởi tạo một string ví dụ "hi!"**, thì máy tính nó
> **assign 4 byte cho mỗi char** và **1 byte extra cho \\0**
> Và assign thêm **8 byte nữa để cho s** là một **pointer var** 
> mang **address của 'h'**

<br>

<a id="node-643"></a>

<p align="center"><kbd><img src="assets/f029350ce2bcf54c3c66cb767dd29b17fc914f4e.png" width="100%"></kbd></p>

<br>

<a id="node-644"></a>

<p align="center"><kbd><img src="assets/7c10dc6aeeab005849f22e889d598e2a68ba34e9.png" width="100%"></kbd></p>

<br>

<a id="node-645"></a>

<p align="center"><kbd><img src="assets/08dc1e7bb5a3955243eb9669fd2ba919694c9611.png" width="100%"></kbd></p>

> [!NOTE]
> D: Đoán thử **string** là **synonym** của cái gì?
>
> A: "**Pointer**" hả
>
> D: Correct, thật ra là một lời nói dối bấy lâu nay, **không
> có cái gì gọi là ''string'' trong C** cả mà nó thật ra là
> **pointer chỉ đến char đầu tiên trong array các char**

<br>

<a id="node-646"></a>

<p align="center"><kbd><img src="assets/65e3cb6b111977230080fde754a6d30eb6e02e21.png" width="100%"></kbd></p>

> [!NOTE]
> Bản chất nó chính là một **pointer**, một var mang giá trị là **address**
> **của char đầu tiên**
>
> int n = 50;
>
> Có nghĩa là**cho 4 bytes dành cho n**, mang giá trị là 50. 
> Trong memory nó là **chuỗi 32 số 1, số 0 sao đó mà tính ra bằng 50**
>
> **int *p = &n;**
>
> có nghĩa là **cho 8 bytes** dành cho p, để **chứa address của cái int
> variable n**, cũng là một con số ví dụ 291 (mà ở base-16 là 0x123), 
> thì 8 bytes = 64 bits này là**chuỗi số 0, 1 sao đó tính ra 291
>
> char *s = "hi!"**
>
> cho 3 + 1 = 4 bytes cho 4 char h, i, !, \\0 và sau đó **cho 8 bytes dành 
> cho s, để chứa address của cái char 'h'**

<br>

<a id="node-647"></a>

<p align="center"><kbd><img src="assets/b33aa339386f366cb0ba7fb424250def3f27be36.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với syntax như này, ta
> **define** một **struct** tên là **person**

<br>

<a id="node-648"></a>

<p align="center"><kbd><img src="assets/75732a4480430e7e5bf87b0694188e4dd9b35529.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái ổng nói là tương tự ta có thể
> **define** một là **int** tên là **integer**

<br>

<a id="node-649"></a>

<p align="center"><kbd><img src="assets/a5a04c55e63950bd7e2fbf065851abf82aec0bbc.png" width="100%"></kbd></p>

> [!NOTE]
> Và **define** một **char address** tên là **string**Do đó string chỉ giống như một cái tên để đặt cho
> một**address của char**
>
> Thì ổng nói là họ không nói cho mình biết rằng
> thật ra trong **<cs50.h>** người ta đã define một cái
> như vậy cho nên ta mới có thể dùng string s = "Hi!";

<br>

<a id="node-650"></a>

<p align="center"><kbd><img src="assets/595ea64c51f375f4e2e4afa9d2c6f752b28d2b04.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Còn các lib liên quan đến string thì sao.
>
> D: Bên trong nó **chỉ có char * (address của char)**, nói chung C 
> (under the hood không có keyword nào là string mà chỉ là char *)

<br>

<a id="node-651"></a>

<p align="center"><kbd><img src="assets/2b8b91867cbb446477f147891041fd4879dc5487.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng quay lại ví dụ với int, như hồi nãy đã hiểu khi
> define ***p = &n** thì có nghĩa là bảo máy tính: 
>
> **Cho tao 8 bytes** để ta **dành cho p** là một **variable 
> chứa address của int variable n**.
>
> Và in ra giá trị của **p** (là address) với format **%p**, thì
> nó chính là con số này **0x7ff....dc** (tương tự như khi ta
> ví dụ 0x123, nhưng thực tế máy tính nó lưu ở address này,
> nếu có thể dịch ra thì đó là **byte thứ tỉ tỉ tỉ** trong memory)

<br>

<a id="node-652"></a>

<p align="center"><kbd><img src="assets/f167918ed9e0f3871a56baf9516056b655314673.png" width="100%"></kbd></p>

<br>

<a id="node-653"></a>

<p align="center"><kbd><img src="assets/5eb05e8d2d6b7f9126bb02301e4e1b45a0b752cf.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói nếu ta in ra với **%i**, và ***p** thì ý nghĩa sẽ là:
> **ĐI VÀO / ĐI ĐẾN CÁI ADDRESS MÀ P ĐANG GIỮ XEM
> NÓ LÀ GÌ**
>
> Thì đương nhiên nó chính là **n**, ra gía trị **50**, và
> *p là n, là int nên dùng **format %i** khi in

<br>

<a id="node-654"></a>

<p align="center"><kbd><img src="assets/62277bc7333965ddb6a6cb037727fbda83402866.png" width="100%"></kbd></p>

> [!NOTE]
> Để minh họa, **bỏ quên việc include cs50.h** đi thì khi
> ta define **string s ="Hi!"** nó báo **lỗi**.
>
> Vì như đã nói, C nó **không có cái keyword nào là string cả**

<br>

<a id="node-655"></a>

<p align="center"><kbd><img src="assets/28ea0f8b31483a945c331532b02db5a21f18ba07.png" width="100%"></kbd></p>

> [!NOTE]
> D: Bây giờ thay vì include cs50 vào lại để fix thì có thể làm sao?
>
> A: Declare **char s* = "Hi!"**. Máy nó sẽ hiểu là dành **8 byte trong
> memory để chứa address của char 'H'** trong array char 'Hi!'
>
> Đầy đủ hơn như nãy đã nói là máy tính nó **tạo 4 byte để chứa 
> 4 char 'h', 'I', '!', '\\0'** trước. Sau đó nó mới**tạo 8 byte để chứa 
> address của 'h'**

<br>

<a id="node-656"></a>

<p align="center"><kbd><img src="assets/b83a6dc71e36824cd5c281dacd1621af5b360180.png" width="100%"></kbd></p>

> [!NOTE]
> Correct, và có thể **char* s** cũng đúng mà **char * s** cũng đúng
> Nhưng theo convention thì người ta để **char *s**

<br>

<a id="node-657"></a>

<p align="center"><kbd><img src="assets/f683587b1af65066954a2d20934d9f1ac60faa0d.png" width="100%"></kbd></p>

> [!NOTE]
> D: In như này nó sẽ ra ntn?
>
> A: Nó ra một dãy số bas16 như 0x.... thể hiện **address của 'H'**

<br>

<a id="node-658"></a>

<p align="center"><kbd><img src="assets/5f7b41fab14a600c91101ec1e43ae64cf9877803.png" width="100%"></kbd></p>

> [!NOTE]
> D: Correct!.
>
> D: Why?
>
> A: Vì ta đang in với **%p**, và **s là cơ bản là một pointer** (một var chuyên 
> chứa address) nên in nó ra ta sẽ có "con số" là address của 'H' trong 
> memory.
>
> Dự đoán thêm là nếu in với **(%c, *s) thì nó sẽ ra 'H'**, vì khi đó ta bảo 
> máy tính **ĐI VÀO address chứa bởi s** và in ra thì đó **chính là 'H'**

<br>

<a id="node-659"></a>

<p align="center"><kbd><img src="assets/2499f0c19dc7a2e3fd8a3e541890ad3ba0e4a4ef.png" width="100%"></kbd></p>

> [!NOTE]
> Chính xác!

<br>

<a id="node-660"></a>

<p align="center"><kbd><img src="assets/45c755718d5bb108feb8f963e4e768636784b0dc.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là khi ta chuyển thành printf("**%s**", **s**) thì kiểu
> như nó sẽ hiểu là ta muốn treats như sau: **Đi vào address
> mà s đang giữ, lần lượt in ra các char cho đến khi nào gặp
> \\0**
>
> Do đó kết quả sẽ là **HI!**

<br>

<a id="node-661"></a>

<p align="center"><kbd><img src="assets/07087bcef48de72bdea1459b93d871d83a568324.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Sao khi print ko có *s:
>
> D: Như mới nói, function printf kiểu nó nó được code để khi gặp
> **(%s, s)** nó sẽ hiểu rằng **cần phải đi vào address mà s mang**,
> sẽ **dẫn đến một vùng trong memory chứa char ('H')**. thì sau đó
> printf sẽ l**ần lượt in các char tiếp theo** (nó được thiết kế như
> vậy) **cho đến khi gặp '0\\' thì dừng.**
>
> Cho nên nếu ta in với (**%c, *s)** thì nó sẽ **chỉ in char 'H' ra thôi**

<br>

<a id="node-662"></a>

<p align="center"><kbd><img src="assets/605256de96d2508e859d166aa2e33343b5dd99a5.png" width="100%"></kbd></p>

> [!NOTE]
> D: Nó sẽ ra gì?
>
> A: 
>
> 1/%p, s là in ra **address của 'H'**
>
> 2/Với **&s[0]** và in với %p thì nó sẽ là **address của character
> đầu tiên chính là 'H'**

<br>

<a id="node-663"></a>

<p align="center"><kbd><img src="assets/e8e19ba4f441bba5c7f073d7e627a7b0dde2ce9a.png" width="100%"></kbd></p>

> [!NOTE]
> Chính xác.
>
> Cái đầu tiên như đã biết s là address của 'H' nên in ra với %p 
> là được address của 'H'.
>
> Còn cái thứ 2, vì**s nó vẫn được coi là array của char**, (dù bản
> chất nó là như address nhưng như ban đầu ta được học thì **C vẫn
> treat nó như array of char**, nên **s[0] sẽ là lấy char đầu tiên của 
> array**
>
> Sau đó dùng **ampersand &** thì lại mang ý nghĩa là**"lấy address của 
> char** đó. Thành ra **hai dòng đều in ra address của 'H'**

<br>

<a id="node-664"></a>

<p align="center"><kbd><img src="assets/0717f1d7b2d7db4be47f1bfb8b7cc7d45cc40729.png" width="100%"></kbd></p>

> [!NOTE]
> Và khi in như vầy thì có thể thấy các **address value nó kế tiếp nhau**
> confirm lại rằng khi define một string, bên trong máy tính nó sẽ
> **define các byte kế tiếp nhau**, **mỗi byte (8 bit)** mang **chuỗi số 01 sao
> cho tính ra số** mà**tra vào ascii** sẽ**tương ứng với char** theo quy ước.
>
> Và sau đó nó **cho một byte extra** mang (chuỗi **00000000**) thể hiện **'\\0'**
>
> Và cuối cùng nó **chuẩn bị 8 byte dành cho s**, **mang chuỗi 01** sao cho
> gía trị chính là **address của 'H'.**

<br>

<a id="node-665"></a>

<p align="center"><kbd><img src="assets/9405df19cfc6595a6dae5632187363102d032e4c.png" width="100%"></kbd></p>

<br>

<a id="node-666"></a>

<p align="center"><kbd><img src="assets/6d55eb4d7035357a711ee0b9c000775e0542c378.png" width="100%"></kbd></p>

> [!NOTE]
> D: In cái này ra cái gì?
>
> A: H -> I -> !

<br>

<a id="node-667"></a>

<p align="center"><kbd><img src="assets/fef57a865d007540e31bafd04d55444b1f62967a.png" width="100%"></kbd></p>

<br>

<a id="node-668"></a>

<p align="center"><kbd><img src="assets/7a081285313cf0b0b394a5525a929de88ccbb51e.png" width="100%"></kbd></p>

> [!NOTE]
> D: Nếu in **%c, s** thì ra cái gì?
>
> A: Không được, vì **s là pointer**, một là in với **%p**, hoặc **%s**
> hoặc là in với **%c** thì phải là ***s** (**đi vào** **address** chứa trong s)

<br>

<a id="node-669"></a>

<p align="center"><kbd><img src="assets/4f776167c778703fefee91e3a31d34c975688421.png" width="100%"></kbd></p>

> [!NOTE]
> Chính xác, phải in %c, *s và nó sẽ "đi vào / đi tới address 
> chứa trong s (là 'H')
>
> Và muốn**đi tới char tiếp theo**, chính là ***(s+1), *(s+2)**

<br>

<a id="node-670"></a>

<p align="center"><kbd><img src="assets/5cd814b18e9814c4fab839a80af92e1d9654f05e.png" width="100%"></kbd></p>

<br>

<a id="node-671"></a>

<p align="center"><kbd><img src="assets/3969d6aafe527d173a846d1bc956d3ec754874b5.png" width="100%"></kbd></p>

> [!NOTE]
> Và đại khái là kiểu access tới char trong string bình
> thường kiểu như **s[0], s[1]..** là **convenient**, human friendly
> syntax chứ bên trong nó chính là cái này

<br>

<a id="node-672"></a>

<p align="center"><kbd><img src="assets/2e895a372a9247877b16d6ee7ebc9fe415727f4e.png" width="100%"></kbd></p>

> [!NOTE]
> D: Và nếu bạn vọc vạch, đi đến, **đụng tới phần memory
> segment ở xa mà không được assign cho bạn** thì nó sẽ báo
> lỗi
>
> Và đây chính là cách các hacker vọc vạch, chạm tới, đi tới
> các vùng trên memory và ăn cắp password của bạn

<br>

<a id="node-673"></a>

<p align="center"><kbd><img src="assets/2b892c3cb7a79d545b048fe04ae10df89dd7dbfe.png" width="100%"></kbd></p>

> [!NOTE]
> D: Giờ in kiểu này, nó ra gì, đoán thử xem?
>
> A: Như nãy nói thực hiện lệnh printf với %s, s với s như đã nói,
> nó là một address tới char đầu tiên.
>
> Thì lệnh print được thiết kế sẽ **ĐI ĐẾN address "lưu bởi
> s"** và **in ra char đó (là 'H')** sau đó **tiếp tục**, nó **in các char kế tiếp
> cho đến khi gặp '\\0'**
>
> Vậy với cái cái kiểu s+1 cho phép đi đến pointer của char tiếp
> theo, ta sẽ đoán rằng nó sẽ tương tự như vậy, nó sẽ **in từ char
> thứ 2 là 'I' đến khi gặp '0'.**
>
> Vậy nó sẽ in ra như sau:
>
> HI! 
> I! 
> !

<br>

<a id="node-674"></a>

<p align="center"><kbd><img src="assets/98d7f2589fe86a3db57b997c9b67102b8995e462.png" width="100%"></kbd></p>

> [!NOTE]
> Correct!
>
> **s+1** cho máy tính biết là **đi đến cái byte kế tiếp**
> (Mỗi char 1 byte nhớ khong)

<br>

<a id="node-675"></a>

<p align="center"><kbd><img src="assets/49a6ad80045115413666f95b762d83e83d9896bb.png" width="100%"></kbd></p>

> [!NOTE]
> D: Tuần trước ta đã biết cách dùng function để compare 2
> string
>
> A: strcmp()
>
> D: Vậy giờ đã hiểu tại sao không thể dùng == để compare
> string chứ?
>
> A: Bởi vì **s chỉ là pointer,** và mỗi pointer**chứa address của
> char đầu tiên**. Nên **dù hai string y hệt nhau** thì**address của
> kí tự đầu tiên của chúng cũng khác nhau**.
>
> D: Correct!

<br>

<a id="node-676"></a>

<p align="center"><kbd><img src="assets/b7c97ab6a34f9028bae460585919ddcc93fa7cd3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b7c97ab6a34f9028bae460585919ddcc93fa7cd3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d4d3d3e3d850a67e68da2aa33df78d37f0f6e7cc.png" width="100%"></kbd></p>

<br>

<a id="node-677"></a>

<p align="center"><kbd><img src="assets/d3b99973369eb44c857838ca73f4474ef869a11e.png" width="100%"></kbd></p>

> [!NOTE]
> Còn function **strcmp**() nó sẽ ĐI VÀO, ĐI TỚI cái hai cái
> address lưu giữ bởi s, t. Rồi từ đó so sánh char by char ...
> cho đến khi gặp \\0. Nếu mọi char đều giống nhau thì return
> 0 -> hai string bằng nhau

<br>

<a id="node-678"></a>

<p align="center"><kbd><img src="assets/9dfda1d50fdf6dc79303679665ea1b89435fdd51.png" width="100%"></kbd></p>

> [!NOTE]
> Còn những var type khác?
>
> D: Chỉ có **string được đối xử đặc biệt** : Là pointer
> thôi, còn mấy cái khác đều là number

<br>

<a id="node-679"></a>

<p align="center"><kbd><img src="assets/65d9ba6c740445fc82364698bf67caf1a122380c.png" width="100%"></kbd></p>

> [!NOTE]
> D: Nếu như thế này thì sao?
>
> A: Vì *s có nghĩa là ĐI TỚI address "save bởi s" nó sẽ là char 'H'. 
> Nên so sánh kiểu này chính là so **hai char đầu tiên của s và t.**
> Tương đương **s[0] == t[0]**

<br>

<a id="node-680"></a>

<p align="center"><kbd><img src="assets/c48e46010ee2fd940099a9227f9a3dc0a8dc6b62.png" width="100%"></kbd></p>

> [!NOTE]
> Và ta có thể làm như thế này *s == *t &&
> *(s+1) == *(t+1)...để so sánh các char thứ
> nhất, thứ hai... với nhau.
>
> Và đó là lí do strcmp() tồn tại. nó làm cái việc này
> giúp mình.
>
> Ôn lại luôn đó là trong s sẽ "lưu" address của 
> char đầu tiên 'H', thì s+1 sẽ chỉ cái byte kế tiếp, và 
> vì khi define một string là một array các char thì máy
> tính sẽ sẽ assign các byte kế tiếp nhau cho các char
> và kết thúc cho thêm 1 byte cho '\0'.
>
> Nên s+1 sẽ là address của char thứ 2 trong string = 'i'

<br>

<a id="node-681"></a>

<p align="center"><kbd><img src="assets/4ff1b3aed656e96c6050c98b034a73a320388bb2.png" width="100%"></kbd></p>

> [!NOTE]
> D: How I can print the address IN s?
>
> A: **%p**, **s**: nó sẽ in ra cái address mà chứa trong s, 
> là cái address của char 'H'
>
> D: Correct!

<br>

<a id="node-682"></a>

<p align="center"><kbd><img src="assets/6e959231f9c2963dfd1e1dad6704017f86e3f171.png" width="100%"></kbd></p>

<br>

<a id="node-683"></a>

<p align="center"><kbd><img src="assets/f1d20f7089ade5abc63256fd0713b578c9beaa9c.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó minh chứng cho thấy **tuy hai string có content
> như nhau** nhưng **mỗi thằng nằm một nơi trong memory**,
> **address** của thằng H trong hai string **khác nhau** ...b0,
> ....f0

<br>

<a id="node-684"></a>

<p align="center"><kbd><img src="assets/d8ef6f971483119d4fc76f074bd4aec68b35f7c2.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng nói qua cái code để copy string như này.
>
> D: t[0] = toupper(t[0]) là làm gì?
>
> A: Cái này dùng function toupper của ctype.h, nó sẽ gíup convert
> thành Uppercase char.
>
> Như vậy nó sẽ uppercase char đầu tiên của string lên
>
> Giải thích thử. Việc user enter một string ví dụ "hi!" sẽ  khiến máy
> tính assign 4 bytes cho 3 char và 1 extra char '\\0' đồng thời 8 byte
> cho s chứa address của 'h' (ví dụ 0x123)
>
> String t = s; máy tính sẽ assign 8 bytes nữa cho t chứa address
> của 'h' (là 0x123)
>
> t[0] = toupper(t[0]), "bên trong" nó sẽ đi đến char đầu tiên là 'h' và
> thực hiện chuyển chuỗi binary trong đó thành một chuỗi khác có
> giá trị trong ascii tương ứng với kí tự viết hoa H
>
> Dự đoán nó sẽ in ra: cả hai đều là**Hi! vì thực chất tuy là copy
> nhưng t chỉ đang trỏ tới cùng một nội dung với s**

<br>

<a id="node-685"></a>

<p align="center"><kbd><img src="assets/49a98701d2234d915f317cdbf8bd0ae885d28731.png" width="100%"></kbd></p>

> [!NOTE]
> D: 100% Correct! Bạn chỉ đang copy address.
> Muốn copy string, bạn phải đi vào từng char
> copy nội dung của nó và tạo một array các char
> khác

<br>

<a id="node-686"></a>

<p align="center"><kbd><img src="assets/95c9142e1da926427ed994dc67d83b56b7c05dc6.png" width="100%"></kbd></p>

> [!NOTE]
> Tới đây ổng nói chỗ này có cái không ổn khi ta đang
> **assume t có ít nhất một character** trong khi **nếu user chỉ
> enter khi được hỏi** enter string thì sẽ error ta **nên check
> kiểu này**

<br>

<a id="node-687"></a>

<p align="center"><kbd><img src="assets/bc8ed81f413be016080bf22ddde15288305baf8f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bc8ed81f413be016080bf22ddde15288305baf8f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a2b9efbbb0e9a982e0b8168453c3192e0b13a59e.png" width="100%"></kbd></p>

<br>

<a id="node-688"></a>

<p align="center"><kbd><img src="assets/e53e407ed2ef6cf82c7025f39e574ba05dfe33b4.png" width="100%"></kbd></p>

> [!NOTE]
> **Malloc** = **Memory allocation**: Nó cho phép ta **request máy tính
> một số lượng bộ nhớ nào đó** 100 byte, 1GB...máy tính nó sẽ
> **tìm chỗ trống** và **trả cho ta address của cái byte đầu tiên**. 
>
> Và không như string khi máy tính tự cho thêm 1 byte chứa \\0 ở
> cuối để mà từ đó biết được điểm kết thúc thì cái này ta **phải tự 
> nhớ rằng mình đã request bao nhiêu bytes bộ nhớ.**
>
> **free** ngược lại với cái đó: gọi free với address là ta bảo máy tính 
> rằng ta đã làm xong rồi, trả lại cho mày, mày có thể xoá đi

<br>

<a id="node-689"></a>

<p align="center"><kbd><img src="assets/96f02682c63f2bdcf08054d32e88a45e2f89aebd.png" width="100%"></kbd></p>

> [!NOTE]
> Và đó cũng là những gì xảy ra khi máy tính bị treo, bị đứng.
> Đó là một program của ta liên tục malloc thêm memory mà
> không free nó bớt khiến máy tính bị out of memory

<br>

<a id="node-690"></a>

<p align="center"><kbd><img src="assets/85b9e1549039fabedaa9ab77a93aaa6e3658e369.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng làm thế này:
>
> tuỳ vào độ dài của s, ví dụ là 'hi!', strlen(s) = 3 (Chú ý, tuy trong memory nó
> có 4 byte, nhưng util function strlen() sẽ chỉ trả ta phần "content" -> = 3
>
> Khi đó, ta sẽ yêu cầu máy tính **chuẩn bị cho 4 byte:** **malloc(strlen(s) + 1)** để
> sau đó
>
> và **char *t = malloc(strlen(s) + 1)** sẽ hiểu là **chuẩn bị 4 byte** **trống**.
>
> Sau**chuẩn bị 8 byte cho t** sẽ là/**chứa address của cái char đầu tiên**, 
>
> Và như đã nói ở trước s**tring t vẫn được treat là char array** và do đó cho phép 
> dùng t[0], t[1] ,...sẽ có nghĩa là **đi đến vị trí char thứ 0, thứ 1...**
> Loop trong 0,1,2,**3 (i < strlen(s) + 1)**và**gán t[i] = s[i]**D: Tại sao lại loop trong i < strlen(s) + 1
>
> A: Vì ta sẽ cho từng byte trống (mới request) bằng từng byte của s s[0] = 'h',
> s[1] = 'i', s[2] = '!', s[3] = '\\0'

<br>

<a id="node-691"></a>

<p align="center"><kbd><img src="assets/c2ab0dfe568585504a999c2e2feca6f9e31b7ecb.png" width="100%"></kbd></p>

<br>

<a id="node-692"></a>

<p align="center"><kbd><img src="assets/04841b0922e9662f5059663a94f3fed6acfea204.png" width="100%"></kbd></p>

<br>

<a id="node-693"></a>

<p align="center"><kbd><img src="assets/d806b1aad76a7dfc9640045be546eb6266718291.png" width="100%"></kbd></p>

> [!NOTE]
> Với những thay đổi đó,
> lệnh copy đã work!

<br>

<a id="node-694"></a>

<p align="center"><kbd><img src="assets/30487ed9d388d5037fb1951ce2586933ccbe3380.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/db97a9941b93e0310351bb3f365018b131795903.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/30487ed9d388d5037fb1951ce2586933ccbe3380.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/db97a9941b93e0310351bb3f365018b131795903.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/95c41bafbccca9b0dcc8957cb5ce4d7da621b73e.png" width="100%"></kbd></p>

<br>

<a id="node-695"></a>

<p align="center"><kbd><img src="assets/c2ebd2a2bb7a205979e1a1feca12d939520825e4.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Nếu mà ta **không copy '\\0' thì sao**.
>
> D: Khi đó khi printf(t), như đã biết hàm printf sẽ **đi vào/ tới
> address của char 'h'** save trong t, in ra và **cứ thế in các
> char tiếp theo**, ..
>
> ...đến byte sau '!' như ta đã nói là không copy '\\0', nên lúc này 
> nó vẫn là empty byte thì nó sẽ in ra **con số nào đó đang ở
> trong đó**.
>
> Cứ thế cứ thể **cho đến khi nó gặp một \\0 char  đâu đó thì nó 
> mới stop**

<br>

<a id="node-696"></a>

<p align="center"><kbd><img src="assets/64e4ca02d37227fb6b40b22a0890dda603abf3b2.png" width="100%"></kbd></p>

> [!NOTE]
> D: Tại sao **call function** trong for loop như này là ko ổn? 
>
> A: Vì i < strlen(s) mỗi lần loop nó sẽ gọi **strlen(s)** - mà vốn bên 
> trong nó sẽ là một function loop trong các char của để đếm số 
> char. 
>
> Nên tính strlen(s) trước:
>
> for int i = 0,**int n = strlen(s) + 1**; i < n; i++{....}

<br>

<a id="node-697"></a>

<p align="center"><kbd><img src="assets/064f95f416149682b606095740baad0ef785641e.png" width="100%"></kbd></p>

> [!NOTE]
> Correct! Từ đó đã tự làm xong function copy string

<br>

<a id="node-698"></a>

<p align="center"><kbd><img src="assets/8e2046a6e0545acbdfaab2f0ab50b6ac80b49ed0.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng mà string.h nó có function
> **strcpy**() làm giúp việc này

<br>

<a id="node-699"></a>

<p align="center"><kbd><img src="assets/af533785d71bd5640d1c8aec3727a765c02bbd70.png" width="100%"></kbd></p>

> [!NOTE]
> NUL là một **char** '\\0' - như đã biết char được cho 1 byte,
> nên cơ bản đây chính là 1 byte mang giá trị 00000000
>
> Còn NULL là một **address**, và address có **giá trị là 0**, 
> giống như là cái byte đầu tiên, nằm trên cùng bên trái của
> memory và sẽ **không bao giờ được xài tới by convention**

<br>

<a id="node-700"></a>

<p align="center"><kbd><img src="assets/0a785aac6109ddfee2b7d44370d8eb470bdea899.png" width="100%"></kbd></p>

> [!NOTE]
> Và khi ví dụ ta nhập một đoạn **text dài thiệt dài**...và
> máy tính nó **không thể kiếm chỗ để chứa được**, thì
> nó sẽ trả về cho ta NULL
>
> Do đó **sẽ an toàn hơn khi check s == NULL** trước
> nếu nó xảy ra, **exit function với exit code = 1** báo hiệu
> có error

<br>

<a id="node-701"></a>

<p align="center"><kbd><img src="assets/8c501477e53161689b58711b5dac8346bda28bd5.png" width="100%"></kbd></p>

<br>

<a id="node-702"></a>

<p align="center"><kbd><img src="assets/c0db81203348451d6af0c9df27e1463bb63f8a20.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là khi nào ta gọi **malloc**() thì ta **phải gọi free**()
> như một good habit. (Cho dù khi kết thúc function,
> máy tính cũng sẽ free memory)
>
> Q: Free nó làm gì?
>
> D: Nó sẽ biết ta ko cần dùng đoạn memory đó nữa để
> khi có  chương trình khác request nó sẽ trả ra
>
> Và khi qua Python, nó sẽ automatically làm những việc
> này cho ta

<br>

<a id="node-703"></a>

<p align="center"><kbd><img src="assets/668030a03f845b8afa9b1709a0362bc4e642f152.png" width="100%"></kbd></p>

> [!NOTE]
> Bình thường khi cần máy tính cho **array 3 int** thì làm vầy: int x[3]
>
> Còn ở đây, **malloc (3*sizeof(int))** là ra lệnh cho máy tính **chuẩn
> bị một dải bộ nhớ dài 3 x 4 bytes** (1 int được 4 bytes) = 12 bytes.
>
> Máy tính sẽ **tìm chỗ nào còn trống** và **trả về cho mình cái 
> address của cái byte đầu tiên** và lưu trong x là một var dạng 
> address (được chuẩn bị cho 8 bytes)

<br>

<a id="node-704"></a>

<p align="center"><kbd><img src="assets/52fe5521e67b816bb1e21d77e07f6c60154207aa.png" width="100%"></kbd></p>

> [!NOTE]
> D: Có chỗ nào sai ko?
>
> A: Index từ 0 chứ, vậy phải là x[0], x[1], x[2] chứ
>
> D: Correct! Còn nữa ko (week 4 specific) ?
>
> A: Thiếu free
>
> D: Correct!

<br>

<a id="node-705"></a>

<p align="center"><kbd><img src="assets/3bd95650b91ed8148be13284e8cdf47ebba70171.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với những bug như mới kể program vẫn
> compile ok, cho thấy compile được không có nghĩa
> là không có những latent bug
>
> Thì **valgrind** là tool giúp ta detect những bug liên
> quan đến memory

<br>

<a id="node-706"></a>

<p align="center"><kbd><img src="assets/d031160ab7fdde7e501790d2b6b206ced78b28fd.png" width="100%"></kbd></p>

> [!NOTE]
> D: invalid write of size 4 là sao, có thể bug ở đâu?
>
> A: Có thể là do ta chỉ yêu cầu memory cho 3 int
> Trong khi lại assign x[3] là ở vị trí thứ 4.

<br>

<a id="node-707"></a>

<p align="center"><kbd><img src="assets/51c4f0836a0567641df6710d71e4c413e67ed0c8.png" width="100%"></kbd></p>

> [!NOTE]
> Correct!

<br>

<a id="node-708"></a>

<p align="center"><kbd><img src="assets/e06f78d962e0202e31940f5a388909fc1ca1d226.png" width="100%"></kbd></p>

> [!NOTE]
> Cái vấn đề thứ hai mà nó report là liên quan đến memory
> "loss". Thì có thể dễ hiểu là do ta kh**ông gọi free()**

<br>

<a id="node-709"></a>

<p align="center"><kbd><img src="assets/8b075d05484b619a9d62d30a700b6b4559678096.png" width="100%"></kbd></p>

> [!NOTE]
> Sửa lại, index cho đúng, và thêm **free**(x)
> Và tốt hơn nữa là **check x == NULL** thì return
> như đã biết vì **nếu máy tính nó không tìm ra được
> memory còn trống thì nó sẽ trả về cho x = NULL** là 
> address đầu tiên (=0) trong bộ nhớ

<br>

<a id="node-710"></a>

<p align="center"><kbd><img src="assets/dc2d919e65f5d2f6510008a54f71192e4a70e379.png" width="100%"></kbd></p>

> [!NOTE]
> Và run lại thì **valgrind** không
> còn report error nào nữa
>
> ..**no error detector...**
>
> ..**All heap blocks were freed...**

<br>

<a id="node-711"></a>

<p align="center"><kbd><img src="assets/ed5f06206dd4e4f40bb50569f7ed452e2d1dad3c.png" width="100%"></kbd></p>

> [!NOTE]
> Xong đến chương trình này

<br>

<a id="node-712"></a>

<p align="center"><kbd><img src="assets/f145b5f830935d251cb7996f916a94d0db691b2f.png" width="100%"></kbd></p>

> [!NOTE]
> D: Bug ở đâu?
>
> A: Khai báo int **scores[1024]** là máy tính nó đã chuẩn bị
> bộ nhớ **1024 x 4bytes** cho scores
>
> Nhưng c**hưa assign value gì cả** mà đã lấy ra trong printf
>
> Và **cũng chưa check là scores có NULL không.**
>
> D: Correct. Nếu ta ko assign value, có thể nó **chứa garbage**
> từ những chương trình khác trước đó.

<br>

<a id="node-713"></a>

<p align="center"><kbd><img src="assets/94f0d3bbf4d768a2ad6720071f6a388554692e3a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/94f0d3bbf4d768a2ad6720071f6a388554692e3a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/45911cf06a25f65f8b1356622b5655a03393c203.png" width="100%"></kbd></p>

> [!NOTE]
> Garbage đây

<br>

<a id="node-714"></a>

<p align="center"><kbd><img src="assets/d6ae0e5bc3bc97f1f76a0e1439468bbd1b491feb.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó phải initialze value

<br>

<a id="node-715"></a>

<p align="center"><kbd><img src="assets/347b39a6e92deb6a7c689e04ab56cd3d183c829e.png" width="100%"></kbd></p>

<br>

<a id="node-716"></a>

<p align="center"><kbd><img src="assets/7876951d5658cbc6444c8439f41a8b2280e7087b.png" width="100%"></kbd></p>

> [!NOTE]
> D: Có vấn đề gì?
>
> A: Chưa có memory cho y.
>
> Nè he: hai dòng đầu là declare cho máy tính biết x, y là
> var sẽ chứa address tới int. Nó sẽ cho hai chỗ trong memory
> 8 byte để chuẩn bị chứa address
>
> x = malloc(sizeof(int)) sẽ lệnh cho máy tính tìm một chỗ
> trong bộ nhớ có size của 1 int = 4 bytes và assign address
> đó cho x.
>
> *x = 42 -> máy tính sẽ gán chuỗi binary có trị giá 42 vào 4 byte
> tại address lưu bởi x.
>
> *y = 13 -> Máy tính sẽ đi đến phần memory save bởi y và gán 
> chuỗi binary có giá trị 13. Nhưng CHƯA CÓ ADDRESS ĐÓ
>
> -> Correct. Tại y sẽ là GARBAGE, một value nào đó

<br>

<a id="node-717"></a>

<p align="center"><kbd><img src="assets/69557b09d1eadfeff52e39b6db0a1d3dccc5ba37.png" width="100%"></kbd></p>

> [!NOTE]
> Sửa lại vầy thì ok, y = x đã ra lệnh cho máy tính assign cái
> address mà x đang giữ cho y.
>
> *y = 42 ra lệnh cho máy tính đi tới address của y đang giữ
> để đổi thành chuỗi binary có trị giá 42

<br>

<a id="node-718"></a>

<p align="center"><kbd><img src="assets/366b397691adb3bbba61dded971de8198590b8c0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/366b397691adb3bbba61dded971de8198590b8c0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/704ef59c27faae3d7f80991225dd9c01e1c13c70.png" width="100%"></kbd></p>

> [!NOTE]
> D: Swap water of two glass

<br>

<a id="node-719"></a>

<p align="center"><kbd><img src="assets/c7f0cf7076ba5513370103b27b8a4ee8b305945d.png" width="100%"></kbd></p>

<br>

<a id="node-720"></a>

<p align="center"><kbd><img src="assets/d026b736c56e14f5b1442d3d7a85f05f08a0d980.png" width="100%"></kbd></p>

> [!NOTE]
> D: Tại sao nó không như expected?
>
> A: Vì khi đưa vào function swap, nó đã
> copy ra thành hai int mới trong a, b
> Có nghĩa là nó tạo hai vùng mới trong memory,
> cho a và b, có chuỗi binary mang trị giá của x, và y 
> Và việc swap, chỉ diễn ra giữa a, b. 
> Còn x, y không bị thay đổi.

<br>

<a id="node-721"></a>

<p align="center"><kbd><img src="assets/1ea5999cedd3c4667fdbf81842411b20d6ad4f73.png" width="100%"></kbd></p>

> [!NOTE]
> Đúng vậy, khi nó gọi function, nó pass value vào.
> Có nghĩa là trong function, nó sẽ tạo variable khác

<br>

<a id="node-722"></a>

<p align="center"><kbd><img src="assets/dc5b92ccd9eb1387f22e830879beeaebb127b9d4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dc5b92ccd9eb1387f22e830879beeaebb127b9d4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/34e346fd331e1a5a50e55eb896c657b078387558.png" width="100%"></kbd></p>

<br>

<a id="node-723"></a>

<p align="center"><kbd><img src="assets/69f1e4ae3e31f190bc565dfcf3b2728da6ae50cd.png" width="100%"></kbd></p>

> [!NOTE]
> **Machine code,** và **globals** là vùng memory
> dành cho machine code, và globales 
>
> **heap** khi máy tính cần lấy memory
>
> **stack** vùng memory dành cho function.
>
> Thì khi stack lấy quá nhiều memory để nó đụng với 
> heap, hoặc ngược lại thì gây ra lỗi tràn bộ nhớ.
>
> Đó là lí do ta **phải check NULL khi gọi malloc()....**

<br>

<a id="node-724"></a>

<p align="center"><kbd><img src="assets/bafff8a1f47c2ad1c44f7b3f8aa07cc1947fc1d0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bafff8a1f47c2ad1c44f7b3f8aa07cc1947fc1d0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ae487756f0aba6496e35f75f0c5cb3a85217feb4.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là khi main gọi swap, vùng bộ nhớ
> dành cho swap sẽ được allocate

> [!NOTE]
> Như khi function swap đã hoàn thành,
> nó sẽ được free bởi máy tính.
>
> Nhưng như ta biết, bên các byte đó vẫn có GARBAGE

<br>

<a id="node-725"></a>

<p align="center"><kbd><img src="assets/ab7666730e4dc01911f727609e3e57e5a153238b.png" width="100%"></kbd></p>

> [!NOTE]
> Như đã nói, gọi swap(x, y), máy tính nó chỉ
> đưa VALUE vào function swap. Có nghĩa là 
> nó sẽ tạo hai var mới a, b với value bằng với
> x, y.
>
> Có nghĩa là sẽ **có hai vùng memory 4 byte dành cho a, b** 
> c**hứa chuỗi binary mang trị giá bằng 1 (của x) và 2 (của y).**
>
> Và v**iệc swap trong đó chỉ swap giá trị của a, và b**

<br>

<a id="node-726"></a>

<p align="center"><kbd><img src="assets/78b1f7d0e9ec6d8deb735a6f68a50f768f3a4171.png" width="100%"></kbd></p>

> [!NOTE]
> Còn giá trị của x, y
> không thay đổi

<br>

<a id="node-727"></a>

<p align="center"><kbd><img src="assets/235a83b8b51c79589cda1f73c85b05107bb25d26.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng sửa lại vầy CHO SWAP() TAKE ARGUMENT LÀ ADDRESS. Giải thích:
>
> Đại khái là nếu chỉ là**swap(x, y)**. Thì nó sẽ đưa vào **VALUE =**
> con số 1, 2 (là **trị giá của x, y**) và tạo ra hai var mới a, b mang trị giá này.
>
> Còn **swap(*x, *y)** là **ADDRESS** của hai vùng memory (mỗi vùng là 4 bytes,
> mang chuỗi binary có trị giá 1, 2) của x, y sẽ được  đưa vào lệnh swap.
>
> Hay nói cách khác **swap (int a, int b)** sẽ ra lệnh cho máy tính **copy giá trị từ
> hai variable** **đưa vào** và **tạo các local var** để rồi **thực hiện trên đó.**
>
> Còn **swap (int *a, int *b)** sẽ cho function nhận ADDRESS và khi gọi swap(x,
> y) nó sẽ ra lệnh cho máy tính **khi nhận variable đưa vào** (là loại ADDRESS)
> thì **ĐI TỚI ĐÓ, ĐI TỚI vùng memory mang gía trị đó** để thực hiện các thao
> tác trên đó.
>
> Khiến lúc bấy giờ, a có vai trò CHÍNH LÀ x, b CHÍNH LÀ y, Và việc swap chính
> là swap giữa x và y.

<br>

<a id="node-728"></a>

<p align="center"><kbd><img src="assets/4ae927e1219f5eb269d44794b2ec3b1a7ae8e817.png" width="100%"></kbd></p>

<br>

<a id="node-729"></a>

<p align="center"><kbd><img src="assets/c970cd78009ddf3b470fd526204bdc13c04c5cf6.png" width="100%"></kbd></p>

<br>

<a id="node-730"></a>

<p align="center"><kbd><img src="assets/08598d6171543332fa0b0b7e73c5afb9e9835329.png" width="100%"></kbd></p>

> [!NOTE]
> D: Sửa vậy rời nhưng ta sẽ cần sửa thêm gì nữa?
>
> A: Thì với swap bây giờ nhận argument là **address** 
> nên phải **swap(&x, &y)
>
> D: Correct!**

<br>

<a id="node-731"></a>

<p align="center"><kbd><img src="assets/c0b9da320e8a4d5e5ac9d8815bdc987fd00feaac.png" width="100%"></kbd></p>

<br>

<a id="node-732"></a>

<p align="center"><kbd><img src="assets/ef03edd3bd07f122ddee98073ac6b2f5b04387dc.png" width="100%"></kbd></p>

> [!NOTE]
> D: Oop! Còn 1 chỗ sai?
>
> A: Phải sửa trên chỗ **declare function** nữa void swap(int *a, int* b);

<br>

<a id="node-733"></a>

<p align="center"><kbd><img src="assets/098a16ca169f44f1d9493ef33c1aea514e2345d6.png" width="100%"></kbd></p>

> [!NOTE]
> Correct!

<br>

<a id="node-734"></a>

<p align="center"><kbd><img src="assets/8104a4400dad707bd5d14ac859f7f627a65dd0d4.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại hai cái vụ khi heap quá đụng đến
> stack và stack quá đụng đến heap thì gọi là
> heap overflow và Stack Overflow

<br>

<a id="node-735"></a>

<p align="center"><kbd><img src="assets/620c07eb2f17c0c413fff502c5287257eda4853f.png" width="100%"></kbd></p>

> [!NOTE]
> Gọi chung là
> buffer. overflow

<br>

<a id="node-736"></a>

<p align="center"><kbd><img src="assets/28d6f18874042fa244b62beee9ca28e3c9966b58.png" width="100%"></kbd></p>

<br>

<a id="node-737"></a>

<p align="center"><kbd><img src="assets/8d85af23402a3c450dec973bfa16f8581646b20d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng đang cho thấy function get_int() của cs50.h
> nó làm gì.
>
> Nó dùng một function mới gọi là **scanf**()
>
> **scanf**(**"%i", &x**); là built-in function kiểu như là nó sẽ check 
> scan - tìm - dò **tìm keyboard value**, tức là nó **theo dõi xem
> user enter cái gì**, đặc biệt là nó **cần một integer** (quy định
> bởi argument "%i")
>
> Sau đó **&x** cho nó biết khi scan được integer value user nhập
> vào rồi thì LƯU NÓ Ở ĐÂU -> ở trong **address của var x**Do đó khi print x, ta có giá trị int vừa nhập**====
>
> Ở đây ôn lại chỗ này:**Chuyện gì xảy ra khi khai báo var : int x = 1;
> Máy tính sẽ chuẩn bị một chỗ 4 bytes trong memory, 
> với một address nào đó trong memory. 4 bytes đó sẽ có chuỗi
> binary trị giá = 1. (nói luôn sẽ là 000....001)
>
> Và khi cần xem cái address đó, ta sẽ dùng &x. Và nếu mình
> Define **int *p =  &x**, thì  có nghĩa là mình **define một pointer**
> var p (chuyên chứa address), **mang trong mình address của x**

<br>

<a id="node-738"></a>

<p align="center"><kbd><img src="assets/b535322e20c3692f13bbdd84a912871a3e0f4959.png" width="100%"></kbd></p>

> [!NOTE]
> Và vì scanf("%I",..) nên nó chỉ tìm int, nên nhập
> "cat" nó sẽ reject, và nó convert thành 0. 
>
> Và trong get_int() của cs50.h sẽ handle việc sẽ reprompt lại

<br>

<a id="node-739"></a>

<p align="center"><kbd><img src="assets/03d1c4aaf37f5759c7813ac6e26e88f09be49b64.png" width="100%"></kbd></p>

> [!NOTE]
> Q: vì sao tôi ko cần **&** ở đây?
>
> A: vì **char *s** đã define **s là address/pointer** rồi
> Hay nói cách khác, **string bản chất đã là pointer 
> rồi.**

<br>

<a id="node-740"></a>

<p align="center"><kbd><img src="assets/513bea694178e8235280bdd1b193ff9d95660534.png" width="100%"></kbd></p>

> [!NOTE]
> D: Logic sai sai ở đâu?
>
> A: Cùng phân tích xem. Đầu tiên là ini s với NULL,
> Ok, coi như bảo máy tính cho 8 byte dành cho address 
> var s cho nó giá trị NULL = 0
>
> Sau đó scanf(%s, s) lệnh cho máy tính tìm /chờ nhận
> string và gán address vào s.
>
> Chỗ này có vấn đề.
>
> 1. Người ta nhập 1 chuỗi ví dụ "hi!", thì liệu rằng scanf 
> có save char đầu tiên vào s không?
>
> Còn lại thì cũng ko sai vì ngay cả khi ko có \0 thì printf
> vẫn có thể cứ đi vào address (giữ bởi s) để tới char đầu tiên
> Sau đó tiếp tục tiếp tục cho đến khi vô tình gặp một \0 ở đâu 
> đó thì nó stop.

<br>

<a id="node-741"></a>

<p align="center"><kbd><img src="assets/cf8fd4d01b502c74e186c8e8c4a4e5efaff61a9b.png" width="100%"></kbd></p>

> [!NOTE]
> Vấn đề là ta **không hề bảo máy tính chuẩn bị cho ta 
> bao nhiêu byte bộ nhớ.**
>
> Do đó cho dù scanf muốn save vào s address của 
> char đầu tiên, thì những char tiếp theo cũng không 
> có chỗ để save.
>
> Do đó câu chuyện là: 
>
> char *s -> máy tính chuẩn bị 8 bytes cho s để save address
> char *s = NULL, gán address của s bằng 0
> scanf(%s, s) -> user type in "hi!", **máy tính nó không có chỗ nào
> để lưu / chứa 3 char 'h', 'i', '!' cả**. Nên nó **không thể có address
> của 'h' mà save vào s được.**
>
> Nên s vẫn chỉ có address là NULL, in ra là 0

<br>

<a id="node-742"></a>

<p align="center"><kbd><img src="assets/1eb579f5dfbe80536be644d7f1532a81d73a6ae4.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây: **char s[4]** như **bình thường thôi** = yêu cầu máy
> tính **chuẩn bị sẵn 4 byte** để**chứa 4 char** và **scanf**() sẽ lần
> lượt **"bỏ" các char user nhập vào  vào 4 byte đó**.
>
> Nhưng nếu gõ David David ...vẫn ok là tại đang may mắn khi
> sau **4 bytes được cho ban đầu vẫn là phần memory có
> thể dùng hoặc vẫn trong giới hạn**

<br>

<a id="node-743"></a>

<p align="center"><kbd><img src="assets/9dddb8145c03713d585986fae2692a8744fc7380.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói là trong function cs50.h **get_string**() người ta
> đại khái là sẽ l**iên tục dùng malloc để yêu cầu thêm 1 byte
> khi user gõ text**

<br>

<a id="node-744"></a>

<p align="center"><kbd><img src="assets/cfa15a03a1c575d2f6334f8a32f53d3dbfae8ae2.png" width="100%"></kbd></p>

> [!NOTE]
> Giới thiệu về hai function mới giúp **mở** và**save data**vào **file** và đóng lại
>
> **FILE *file** = **fopen**("phonebook.csv", "a") giúp mở
> file, ***file** thể hiện**file là pointer**, chứa **address tới 
> FILE.**
>
> **fprintf**(file, ...) sẽ **save value vào file**
> **fclose**(file) **đóng file lại**

<br>

<a id="node-745"></a>

<p align="center"><kbd><img src="assets/49afb178f782a1c6e96a62fb4a5f3d0bd0ba5807.png" width="100%"></kbd></p>

<br>

<a id="node-746"></a>

<p align="center"><kbd><img src="assets/411ee21e94e28dfb7b196c71917aa886987c8ba5.png" width="100%"></kbd></p>

<br>

<a id="node-747"></a>

<p align="center"><kbd><img src="assets/e7112a21b27fe82533032ad4d1e01575fe2b2181.png" width="100%"></kbd></p>

> [!NOTE]
> Mở ra lại code phonebook.csv cho
> thấy file thật sự đã save info

<br>

<a id="node-748"></a>

<p align="center"><kbd><img src="assets/b7e3855b45c0a529b7d252be3cff404d100e51a0.png" width="100%"></kbd></p>

<br>

<a id="node-749"></a>

<p align="center"><kbd><img src="assets/b1a1d2fe6f096c4c8bcd4550d466078382ed33fa.png" width="100%"></kbd></p>

<br>

<a id="node-750"></a>

<p align="center"><kbd><img src="assets/19a0fbb23d0d75081aa20b0399bf176e0490989e.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói đại khái là trong PS tới ta sẽ viết code
> manipulate với image như này

<br>

