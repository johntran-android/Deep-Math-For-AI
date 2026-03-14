# Week 2 Array

📊 **Progress:** `101` Notes | `181` Screenshots

---
<a id="node-325"></a>

<p align="center"><kbd><img src="assets/45483b2398782f6d0b69ab74bd1a3df1494a3155.png" width="100%"></kbd></p>

<br>

<a id="node-326"></a>

<p align="center"><kbd><img src="assets/78e59eedf0b9bf4564cc5d9c985aee4f00de496b.png" width="100%"></kbd></p>

<br>

<a id="node-327"></a>

<p align="center"><kbd><img src="assets/452363af6aa757d845a1bf3068eb9b316f190620.png" width="100%"></kbd></p>

> [!NOTE]
> Nhắc lại việc **compiler** sẽ **compile** = **chuyển
> source code thành machine code.**

<br>

<a id="node-328"></a>

<p align="center"><kbd><img src="assets/c48e867754b8067fb03b96d2b0ed585c1d097231.png" width="100%"></kbd></p>

<br>

<a id="node-329"></a>

<p align="center"><kbd><img src="assets/0780401cda0e41dd497674bd0a367449652b8abc.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là cái compiler thật sự là **clang** - chỉ là tên
> của company. Bên cạnh đó có nhiều compiler khác, ví
> dụ **GCC**Và ổng tự compile thay vì gọi **make hello.c** thì gọi
> c**lang hello.c**
>
> Kết quả nó cho ra cái file tên là **a.out**
>
> Gọi **./a.out**thì nó cũng**run và in ra hello, world!**Nhưng có điều file tên a.out không thuận tiện lắm
> Khi nó chẳng nói lên nhiệm vụ của mình. Nên
> ổng nói có thể **rm a.out hello để đổi tên nhưng làm vậy
> mất công quá**

<br>

<a id="node-330"></a>

<p align="center"><kbd><img src="assets/2cb5835926d0f340c661d99590064208bef13b14.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về cái gọi là **command line argument  cho phép thay đổi
> behaviour của command line** - kiểu như thay đổi default
> setting vậy
>
> Thì với cách này, có thể compile (manually dùng Clang, và chỉ
> định tên của file output, argument  **-o** có lẽ là để chỉ **output**.

<br>

<a id="node-331"></a>

<p align="center"><kbd><img src="assets/76c861737a0b4ecaa303b1c4adb773431326a282.png" width="100%"></kbd></p>

> [!NOTE]
> Quả thật nó giúp compile ra file
> hello y như **make hello.c**

<br>

<a id="node-332"></a>

<p align="center"><kbd><img src="assets/391dcf1b5a9994765e53320039351de7ff5b4472.png" width="100%"></kbd></p>

> [!NOTE]
> Q. a.out là gì 
>
> D: Cơ bản nó là**historical name** cho
> **assembly output, ko quan trọng**

<br>

<a id="node-333"></a>

<p align="center"><kbd><img src="assets/8f631efaddac310b6ec3ed737ab43698d224f90f.png" width="100%"></kbd></p>

> [!NOTE]
> Q: -o là gì 
>
> D: là output, **chỉ định output file sẽ có tên là gì**
>
> thì ổng nói cái này là những thứ bạn phải **tự search trên mạng, đọc
> manual document..**

<br>

<a id="node-334"></a>

<p align="center"><kbd><img src="assets/3b48beae07a91c0f7a4980bacb625465cb3cd388.png" width="100%"></kbd></p>

> [!NOTE]
> Sai chỗ nào (review thôi):
>
> A: phải dùng **format code** printf("hello **%s**\\n", answer);

<br>

<a id="node-335"></a>

<p align="center"><kbd><img src="assets/446e166a04be7513b997797bbb9a7352e2c06eb3.png" width="100%"></kbd></p>

<br>

<a id="node-336"></a>

<p align="center"><kbd><img src="assets/d7c69c38a4f2b3224001fcec28c79d754a9844d4.png" width="100%"></kbd></p>

<br>

<a id="node-337"></a>

<p align="center"><kbd><img src="assets/24532a8dc89ebdd38b231bb773fca945458a179b.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây ổng giải thích là **dù với dùng include <cs50.h>**, thì nó vẫn **không đủ
> thông tin để Clang** đi**tìm trên hard drive** of the computer  **những chữ số
> 0,1 (ý là binary code) mà thực sự implement get_string() function**
>
> Và dòng include <cs50.h> này thật sự là **hint** nói với Clang rằng **ở đâu đó
> trên máy tính có function get_string()** này nhưng mày thật sự **phải dùng
> những 0, 1 machine code mà CS50 đã viết  trước đó và bake chúng trong
> your program để thật sự có thể dùng get_string function**Và ổng gọi lại lần này thêm "**-l**cs50" và ổng nói chữ l có nghĩa là **link
> mang ý nghĩa là những 0 and 1 viết bởi cs50 sẽ thật sự được link vào trong
> code**

<br>

<a id="node-338"></a>

<p align="center"><kbd><img src="assets/9a0ff60ba5aa8f211d515fc15735129f2d52a1fa.png" width="100%"></kbd></p>

> [!NOTE]
> Và không riêng gì CS50, những **lib** nào mà bạn dùng mà
> **không có đi kèm với language** trong thì đều phải dùng**-l
> như vậy**

<br>

<a id="node-339"></a>

<p align="center"><kbd><img src="assets/8e60c3151e2779f8bf5d543e738dadfb68cfdd14.png" width="100%"></kbd></p>

> [!NOTE]
> Với sự thay đổi đó
> thì nó đã work

<br>

<a id="node-340"></a>

<p align="center"><kbd><img src="assets/ac11c5c3410b7cb83289304f458dee72d81abb86.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ac11c5c3410b7cb83289304f458dee72d81abb86.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/cdcf3000fcc72c1c05ac1e8b6ce0e6620e59041f.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói là làm vậy để hiểu rằng **make giống như
> automatically mọi thứ giùm - không cần phải lo các
> command line argument
>
> Và sau này** nếu có lỗi gì thì nhiều khi không phải do make
> mà do **Clang implementation ở bên dưới** giống như ví dụ
> ở trên.

> [!NOTE]
> Q: Benefit of using Clang manually?
>
> D: Not really. Chỉ là **cho chút cảm giác control** nếu bạn
> có thể **nhớ được các argument**
>
> ===
>
> Q: Tại sao phải explain **-lcs50** mà không **-lstdio**?
>
> D: Vì **cs50** **không đi kèm với language**, còn **standard io** thì **có**
>
> ===

<br>

<a id="node-341"></a>

<p align="center"><kbd><img src="assets/9551a42127d27c4c3413885e56eb2d73be5ad191.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói compiling chứ
> **thật ra có 4 động tác**

<br>

<a id="node-342"></a>

<p align="center"><kbd><img src="assets/cad2ccf847a8ed159fef551eb336b11f27e5f0a4.png" width="100%"></kbd></p>

> [!NOTE]
> Đầu tiên là **preprocessing**. Ổng nói **bất cứ cái nào có dấu #
> (hashmask) thì đều phải được làm trước = preprocessed  =
> analyzed initially trước tiên**
>
> Tiếp đại khái là ta có thể thắc mắc **những file cs50.h hay stdio.h
> này ở đâu vì ta không thấy khi ls hay dùng GUI?**

<br>

<a id="node-343"></a>

<p align="center"><kbd><img src="assets/88c4c04d7a4b00401de0df9410096520064051d8.png" width="100%"></kbd></p>

> [!NOTE]
> Thì thật sự ở nơi mà chứa cái code space này ví dụ trên
> cloud hay trên máy tính thì nó có cái **folder /usr/include
>
> Và nếu mình gõ ls /usr/include ta sẽ thấy các file trong đó**

<br>

<a id="node-344"></a>

<p align="center"><kbd><img src="assets/f37b330eb51d7cd2c872bbb7f6d2fc686e52aaed.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ổng nói **#include** .. này giống kiểu như một **place
> holder** cho **global find and replace**. Khi clang đọc file, và
> gặp #...nó sẽ **đi vào cái file cs50** và **lấy ra các code để
> sẵn sàng sử dụng**

<br>

<a id="node-345"></a>

<p align="center"><kbd><img src="assets/5a12bb85fe8653c74140969590ae70e40b3ebfe9.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là ổng nói có thể hiểu việc include giống
> như việc **function declaration để clang nó biết là có function
> đó giống như khi ta define 1 function, thì phải declare ở trên 
> main() như tuần trước đã gặp**

<br>

<a id="node-346"></a>

<p align="center"><kbd><img src="assets/ad6e956c344ce088708a3973df04bb5cba16c9ac.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự, với **include <stdio.h>**, là **declaration**
> cho function **printf**
>
> **Ba dấu chấm** mang ý nghĩa là function này có thể
> **có nhiều argument**

> [!NOTE]
> Q: Khi include vậy nó i**nclude chỉ function được
> dùng hay mọi thứ**
>
> D: **Mọi thứ**

<br>

<a id="node-347"></a>

<p align="center"><kbd><img src="assets/5c2b813f75f4123b17decfeebc53997a942087b6.png" width="100%"></kbd></p>

<br>

<a id="node-348"></a>

<p align="center"><kbd><img src="assets/6067e4ddd0d7c1e89b7e155d91c52c96030fcf86.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là khi nó compile thì nó thành ra như thế này, là
> ngôn ngữ **Assembly** d**ù không user friendly lắm nhưng nó
> thật sự efficient**Trong đây ta có thể thấy dấu vết xuất hiện của**get_string,
> printf**

<br>

<a id="node-349"></a>

<p align="center"><kbd><img src="assets/93925e18f8511eaf5c3e4be7c7b884886f68a606.png" width="100%"></kbd></p>

> [!NOTE]
> nhìn sơ sẽ thấy nó có các arimethic
> operation như**push, move, call**, ....

<br>

<a id="node-350"></a>

<p align="center"><kbd><img src="assets/a41e36e5c7b6edd0f6e75d09a43e541ccaed6498.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng nó **vẫn chưa phải là machine
> code**. Thì bước **assembling** mới
> thật sự**tạo machine code**

<br>

<a id="node-351"></a>

<p align="center"><kbd><img src="assets/2d4ea931162db1fa77e548d9244cfafdd54e6a6b.png" width="100%"></kbd></p>

<br>

<a id="node-352"></a>

<p align="center"><kbd><img src="assets/b86b372ce38a4e19204185aeae05f68c89d69198.png" width="100%"></kbd></p>

<br>

<a id="node-353"></a>

<p align="center"><kbd><img src="assets/3ad19c1948651742a331fbce63476f354173eddc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3ad19c1948651742a331fbce63476f354173eddc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/93447686d2bd126ca0e95bad36736be7750c4a79.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là bước **linking** này sẽ**link mọi machine
> code của 3 file này với nhau thành 1**
>
> Nên gọi là c**ompile chứ thực tế có tới 4 bước trong đó**

<br>

<a id="node-354"></a>

<p align="center"><kbd><img src="assets/91ce057ed33ff6990997194542baa484ab478ca0.png" width="100%"></kbd></p>

> [!NOTE]
> Q: mấy cái file "0 và 1" này nằm ở đâu?
>
> D: Good question: Ví dụ khi dùng **VS Code Online thì
> somewhere trên server** có một **folder assign riêng cho bạn**
> chứa tất cả các file này
>
> Giống như **DropBox, Google Drive**
>
> ====
>
> Q: Có thể**thay vì include** thì **copy code trong đó bỏ vào đây
> không.**
> D: **Theo lý thuyết là được.** Thực tế phải care thứ tự abc các 
> kiểu nữa nhưng lý thuyết là được.

<br>

<a id="node-355"></a>

<p align="center"><kbd><img src="assets/f44f8387702a76c89fbbb949f521befc76e77e3d.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó ổng nói dòng include kiểu như**hint cho Slang biết
> các function sẽ như thế nào**. Còn thực tế **code nằm trong
> file cs50.c**

<br>

<a id="node-356"></a>

<p align="center"><kbd><img src="assets/fd21cfcc5d2ba66292ea5cc37e1b9754edc26c22.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Linking có happen khi compile code ko?
>
> D: **Yes**. nôm na là **compiling** sẽ **chuyển source code
> thành  Assembly code**, là language**gần gũi với server,
> window**...hơn.
>
> Sau đó**assembling sẽ chuyển assembly code thành
> machine code (binary)**
>
> Và l**inking sẽ link các binary code của các file lại.**
>
> Ổng nói thời xưa người ta **chỉ code bằng machine code** rất
> khó. Sau đó là **assembly code**, không dễ hiểu như bây giờ
> nhưng **bớt khó**, rồi **C khiến việc code gần giống tiếng
> Anh** và ngày càng **các ngôn ngữ mới build trên tầng ngôn
> ngữ cũ ví dụ Python** nằm trên C sẽ **khiến bớt khó hơn
> nữa**

<br>

<a id="node-357"></a>

<p align="center"><kbd><img src="assets/aac8fc0b7f13374bdbcc04b33c17e8dfec139ffb.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ổng nói là **dù trên lý thuyết** có thể **decompile**
> **machine code ra lại source code**. Nhưng thật ra nôm na
> là **nếu có thể mở cái iphone ra và xem xét, hiểu hết
> bên trong và làm lại** thì thật ra **sẽ dễ hơn để invent cái mới.**
>
> Có những cái gây khó ví dụ như**loop tuy có vài loại
> nhưng khi  compile nó chỉ y nhau**. Rồi **variable với tên
> này tên kia nhưng compile  xong thì nó không care**

<br>

<a id="node-358"></a>

<p align="center"><kbd><img src="assets/4d64fc0750fa707edff051dab3fa452d2b9a6cd2.png" width="100%"></kbd></p>

<br>

<a id="node-359"></a>

<p align="center"><kbd><img src="assets/f65542fe905c3e92f5e290a77665e09f88d949ed.png" width="100%"></kbd></p>

> [!NOTE]
> Đang nói về bug, nguồn gốc**cái tên là từ con bọ thật.**
> Nhưng ngoài **syntax bug** như thiếu dấu **;**
> còn có **logical bug** như ở đây yêu cầu in 3 blocks
> thì nó in 4 blocks

<br>

<a id="node-360"></a>

<p align="center"><kbd><img src="assets/49a455051ff9eb20a8d901ef240ad30d99bbfffe.png" width="100%"></kbd></p>

<br>

<a id="node-361"></a>

<p align="center"><kbd><img src="assets/9b7950b5539c690da4d693dc8ce8078bb68da711.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **printf là cái debugging tool** đầu tiên mà ta có.
> Dùng nó để **in ra các variable value** từ đó giúp ta**diagnose
> vấn đề**
> Ví dụ như trường hợp này **nhờ printf ra value của i ta có thể
> nhận thấy đang dư một vòng lặp**. Phải sửa lại <= 3 -> < 3

<br>

<a id="node-362"></a>

<p align="center"><kbd><img src="assets/2435eb2535508e30c7f466ce9f2bae0038304d21.png" width="100%"></kbd></p>

<br>

<a id="node-363"></a>

<p align="center"><kbd><img src="assets/a9145952f13667d2a70a36cab8e08d34bea1a3bc.png" width="100%"></kbd></p>

> [!NOTE]
> Công cụ thứ 2 chính là **debugger** mà các
> IDE như VS Code support. Cũng như **Android Studio**.
> Nó giúp**xem các variable** khi **chương trình đang chạy**
> bằng cách **dừng lại tại các breakpoint mà ta muốn**

<br>

<a id="node-364"></a>

<p align="center"><kbd><img src="assets/ffef1b25641231b0376e6cba005ddf7e3890bcce.png" width="100%"></kbd></p>

<br>

<a id="node-365"></a>

<p align="center"><kbd><img src="assets/97500fc2043ac7cfad4eb1389f96cd5b9e6b1360.png" width="100%"></kbd></p>

> [!NOTE]
> **Step over**là**bỏ qua**,  nó sẽ k**hông phân tích implementation
> của printf**, còn **nếu dùng nút kế tiếp thì nó sẽ step in**, **đi vào
> phân tích printf**
>
> Phân tích ở đây hiểu nôm na là chạy vào bên trong để xem
> và nó sẽ **dừng ở những dòng có tính toán**

<br>

<a id="node-366"></a>

<p align="center"><kbd><img src="assets/84c37066200d29f2ea453756a5b88abf60779997.png" width="100%"></kbd></p>

<br>

<a id="node-367"></a>

<p align="center"><kbd><img src="assets/9258795b8ca649c52bca199cf2de8bf631a9358c.png" width="100%"></kbd></p>

> [!NOTE]
> D: Tại sao phải declare **var n** tại đây
>
> A: Vì để **variable n có thể được return**, nếu để trong do {...}
> thì nó thành local var, không thể access ở ngoài
>
> D: Đúng **scope** của variable là **trong cặp dấu {}**

<br>

<a id="node-368"></a>

<p align="center"><kbd><img src="assets/f2957f4cc494d30bdcc98318db21f70e9ca77e1d.png" width="100%"></kbd></p>

<br>

<a id="node-369"></a>

<p align="center"><kbd><img src="assets/fa09e416826bc5d09bf8ed2d06534da4854aeb1f.png" width="100%"></kbd></p>

> [!NOTE]
> D: Tại sao gõ -1, -2 nó không chạy (ý là debug)
>
> A: Vì nó c**hưa ra khỏi do {} while (n < 0) trong
> function get_negative_int() được**. Nên nó **chưa xong
> function đó**

<br>

<a id="node-370"></a>

<p align="center"><kbd><img src="assets/67d1d3caa30f1d70fed29b913ee98427e209174d.png" width="100%"></kbd></p>

> [!NOTE]
> Thay vì**step over**, ổng dùng **step in** để nó chạy vào
> function **get_negative_int**()
>
> Và ổng nói **nó không dừng ở line 13,14,15,16 vì không
> có gì quan trọng ở đó.**
> Tới đây ổng hỏi **tại sao không nên click step in ở line này**?
>
> A: Vì nó sẽ chạy vào **get_int**() là function của CS50 và **mình
> assume nó correct**
>
> D: Correct

<br>

<a id="node-371"></a>

<p align="center"><kbd><img src="assets/af3d6e72c01015c2d04310b112e6c84fb035e39e.png" width="100%"></kbd></p>

> [!NOTE]
> Với việc debug giúp ta hiểu là
> đang làm sai về logic

<br>

<a id="node-372"></a>

<p align="center"><kbd><img src="assets/f7026012b99ac6173e169e5a35db7730885cd515.png" width="100%"></kbd></p>

<br>

<a id="node-373"></a>

<p align="center"><kbd><img src="assets/ec7d68727e5303266c0ee0e2e8cca02556069605.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái tool thứ 3 là nói chuyện. Khi gặp stuck, **đừng
> chỉ chăm chăm nhìn vào màn hình**. Hãy **nói ra** dù
> chỉ là với con vịt cao su **mô tả logic của mình đang
> làm** thì **rất có thể nó sẽ giúp ta nhìn ra vấn đề sai ở
> đâu**

<br>

<a id="node-374"></a>

<p align="center"><kbd><img src="assets/dfad040e5c5538ff0efcbbd2e1b9c4a1d3e839d4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b7a2ba841f5663988d978bf538d219000b8fa9e0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dfad040e5c5538ff0efcbbd2e1b9c4a1d3e839d4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b7a2ba841f5663988d978bf538d219000b8fa9e0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3b41a45d51c7453aa0245a127239f922a56c988d.png" width="100%"></kbd></p>

<br>

<a id="node-375"></a>

<p align="center"><kbd><img src="assets/020167bde75a179c62fff1672612471144428635.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng lướt sơ lại các data type và memory của
> chúng.
>
> Trong đó chỉ có string là không biết, vì nó tuỳ

<br>

<a id="node-376"></a>

<p align="center"><kbd><img src="assets/f44a94710df054200e52bd1a3ad7f3e2438e61dd.png" width="100%"></kbd></p>

<br>

<a id="node-377"></a>

<p align="center"><kbd><img src="assets/894f863ebd58d44b35d552f8f277c736cbe93990.png" width="100%"></kbd></p>

> [!NOTE]
> Đây là memory

<br>

<a id="node-378"></a>

<p align="center"><kbd><img src="assets/f25277d527a7691a3de19bd6ab130bf093f37fbb.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói đại khái ta có thể hình dung là nếu nó có
> finite storage thì có thể coi như một table các khoảng
> trống available để chứa thông tin.

<br>

<a id="node-379"></a>

<p align="center"><kbd><img src="assets/c31af4bd34d9e12284f2ecac09d98a3113b6872f.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là một char, với 1 byte nó nằm đây

<br>

<a id="node-380"></a>

<p align="center"><kbd><img src="assets/90e827357c577189c18e005de27690b05d1204a5.png" width="100%"></kbd></p>

> [!NOTE]
> 1 int, với 4 bytes nó nằm đây

<br>

<a id="node-381"></a>

<p align="center"><kbd><img src="assets/111b436768e80521a52e8f75d45351703d58cab3.png" width="100%"></kbd></p>

> [!NOTE]
> nếu là một long 8 bytes

<br>

<a id="node-382"></a>

<p align="center"><kbd><img src="assets/b4cbe6ad36e6fe1ce70b2da70b54116691b50849.png" width="100%"></kbd></p>

<br>

<a id="node-383"></a>

<p align="center"><kbd><img src="assets/2df5aad0c5caa2ed938f80afb33e930a14e1a8fa.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng viết cái code này tính average, ban đầu print ra được
> 59 khi để %i
>
> Sau đó ổng muốn check xem có phải là nó tròn 59 hay
> không, nên ổng đổi dùng %f. Compile nó báo lỗi. Vì các
> số đang tính đều là int, mà đòi print với %f nên nó lỗi.

<br>

<a id="node-384"></a>

<p align="center"><kbd><img src="assets/0496f54a9daa5177b3e1e2d9bc99a5e2cde8e302.png" width="100%"></kbd></p>

> [!NOTE]
> Thì cách giải quyết đó là **thay vì chia 3 thì chia 3.0** = đại
> khái  là **khiến phép chia trở thành chia cho một float thì kết
> quả nó sẽ là float**. Compile máy tính nó không complain
> nữa.
>
> Kết quả cho thấy là 59.3333

<br>

<a id="node-385"></a>

<p align="center"><kbd><img src="assets/8434e27a5095667481dc128d8a8e9b81bc9f5385.png" width="100%"></kbd></p>

> [!NOTE]
> Một cách khác là dùng **type casting**để bảo máy tính treat số 3 như một
> float.
>
> Thì kết quả cũng ra tương tự,

<br>

<a id="node-386"></a>

<p align="center"><kbd><img src="assets/4f801029dee3d46b47b631ff51e9ff182407945c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4f801029dee3d46b47b631ff51e9ff182407945c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d1e44de38041de861e5e930a081d638f3aac1006.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nôm na thể hiện các variable trên memory grid, 
> Tuy thực tế nó không nằm như vậy nhưng để cho đơn giản
> cứ tạm hiểu như vậy. 
>
> Thì thực tế ở dưới nó là binary value nhưng cứ tạm bỏ qua
> để hiểu là mỗi integer var score1, score2, score3 chiếm
> 4 bytes

<br>

<a id="node-387"></a>

<p align="center"><kbd><img src="assets/4845f1e9dc31f78f1500d5b4f414f5392653a226.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái ổng hỏi, dù không phải là học CS, thì đây có
> phải là best design không, dùng 3 variable để chứa 3 value
> của scores.
>
> A: (thử trả lời) Không, nên dùng **MỘT** **list** để chứa. Thay vì **3
> Variable riêng biệt
>
> D: Correct! Vì giả sử có 5 10 test scores thì lại phải add
> thêm các variable để chứa những scores đó**

<br>

<a id="node-388"></a>

<p align="center"><kbd><img src="assets/6e0df57a0a644c9db174f1ac10b609c3b096d2a8.png" width="100%"></kbd></p>

<br>

<a id="node-389"></a>

<p align="center"><kbd><img src="assets/36b8a2dc05d690a8723cf3a06f3a0a85c71cfa89.png" width="100%"></kbd></p>

> [!NOTE]
> Hãy cho tôi một variable tên là scores, dạng **array**
> có **size = 3** mà mỗi vị trí là **int**. 
>
> Tương đương, hãy cho tôi **12 (=3*4 bytes) bytes**

<br>

<a id="node-390"></a>

<p align="center"><kbd><img src="assets/66f25b6db8a4180ec5047f5f019fc27180fa9701.png" width="100%"></kbd></p>

> [!NOTE]
> Và đây là cách assign value (scores)
> vào arrays. Start index với 0

<br>

<a id="node-391"></a>

<p align="center"><kbd><img src="assets/0cde769398733e8530940dae80957791bf9c4816.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi ổng sửa code lại như vầy. Error.
>
> D: Why?
>
> A: Ông bỏ các var score1, score 2 ..đi rồi còn đâu

<br>

<a id="node-392"></a>

<p align="center"><kbd><img src="assets/0153345f6d76ef1192e741e12d5ebd64fc58ffaf.png" width="100%"></kbd></p>

> [!NOTE]
> Ok, work!

<br>

<a id="node-393"></a>

<p align="center"><kbd><img src="assets/75c25d6e9d25d2aa7d69fcb3648ad9adef806a59.png" width="100%"></kbd></p>

> [!NOTE]
> Làm cho hữu ích hơn với **entered score value**
>
> Nhưng question: Làm vậy có well design ko?
>
> A: Không, vì sẽ không được nào **nếu muốn nhiều score hơn**.
> Phải có cách nào dùng entered value cho size của scores

<br>

<a id="node-394"></a>

<p align="center"><kbd><img src="assets/379ad3c439b14dfabf5430fbfa74770115841c29.png" width="100%"></kbd></p>

> [!NOTE]
> 1 người trả lời **nên dùng loop vì có 3
> chỗ gọi get_int giống nhau**

<br>

<a id="node-395"></a>

<p align="center"><kbd><img src="assets/5b8f03372104bf50c0385e98e1de81bfdecefe17.png" width="100%"></kbd></p>

> [!NOTE]
> Correct!

<br>

<a id="node-396"></a>

<p align="center"><kbd><img src="assets/c6d66de24fed8a7597a6ca5d18ebbc7f2e197576.png" width="100%"></kbd></p>

> [!NOTE]
> ý ổng nói là ở trong memory**thay vì có 3 chỗ assign cho 3
> variable** đơn lẻ thì giờ vẫn cùng một không gian nhưng mà là
> của **1 variable**
>
> Và có thể access tới các item của nó bằng [i]
>
> The memory is **contiguous**: Contiguous =**tiếp giáp**. Ý là nó
> **không thể nằm random ở đâu đó mà vì là array  nên sẽ quy
> định các pack nằm gần nhau**, **pack to pack to pack**

<br>

<a id="node-397"></a>

<p align="center"><kbd><img src="assets/1d3edbce7a176a92d5ec1377aefaa3483ffca70c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1d3edbce7a176a92d5ec1377aefaa3483ffca70c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/eaedf4fddabd487db218b577ba81a870370a1716.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng **define một function giúp tính average nhận argument là
> array.**
>
> Cái này **hơi khác với Java: average(int[] array)** Còn ở **C lại là
> (int array[]), và array chỉ là tên của argment, có thể là number[], n[]
> .**..

<br>

<a id="node-398"></a>

<p align="center"><kbd><img src="assets/908453657913592b6ae64f97e068ffac2b7cc375.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về **magic number** mà đã học trong short video tuần
> trước. Đại khái là khi ta **HARD CODE một value nào đó**.
> Ổng nói tuy rằng nếu muốn đổi size của array lên 4 thì
> cũng không mệt gì lắm khi đổi hai chỗ nhưng vấn đề là
> khi người khác dùng lại code và họ không biết là phải
> đổi ở những chỗ nào thì rất nguy hiểm.

<br>

<a id="node-399"></a>

<p align="center"><kbd><img src="assets/383341f76fd7ca928a4954ed99d71021c7cc653c.png" width="100%"></kbd></p>

> [!NOTE]
> Dùng N **constant** để thay
> cho magic number

<br>

<a id="node-400"></a>

<p align="center"><kbd><img src="assets/02ff8638d36a9a05fea1dfa2f0301139aa034b41.png" width="100%"></kbd></p>

> [!NOTE]
> D: Nhưng ở đây sẽ không work, sai chỗ nào?
>
> A: Vì hard code kiểu này, lỡ may N define ở trên (size
> array) nhỏ hơn 3 thì nó sẽ bị lỗi ở trong average() này
> khi access array[2]
>
> D: Yes, và giả sử N bằng 5 thì average chỉ đang tính
> với 3 cái đầu tiên của array thôi
>
> ====
>
> D: Vậy phải làm sao?
>
> A: **Dùng loop**, trong length hay size của array. Để**cộng
> dồn** các value và cuối cùng chia cho size

<br>

<a id="node-401"></a>

<p align="center"><kbd><img src="assets/8f839e89441823526011f98060d04f924e7744ed.png" width="100%"></kbd></p>

<br>

<a id="node-402"></a>

<p align="center"><kbd><img src="assets/4ea6fda9d51be4d9f27d8b71fd672721d09dd6cc.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Sao phải include float average(int array[])
>
> D: (Thằng này không học bài nè) vì như tuần trước đã nói
> **C nó đọc từ trên xuống và cần phải declare như vậy cho nó
> biết có tồn tại function average()**

<br>

<a id="node-403"></a>

<p align="center"><kbd><img src="assets/5b5dcd82a9df914caab25c7f564481de1a530cd7.png" width="100%"></kbd></p>

> [!NOTE]
> Q: Có cách nào để biết size của array không?
>
> D:**Trong C thì không**, trong java, python có thể hỏi size của 
> array, còn C thì phải tự nhớ
>
> Q: Có thể có cách nào viết function để tính size của array không
>
> D: Không nốt, nếu nó là một generic array **chỉ như int không
> thể biết số item trong array được**. Điều này hơi thất vọng, nhưng
> đó là lý do tại sao các higher language như Java, Python có 
> Feature này

<br>

<a id="node-404"></a>

<p align="center"><kbd><img src="assets/c574e1e299a833f6907ab67a7f65e0dfaa801806.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c574e1e299a833f6907ab67a7f65e0dfaa801806.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7bb44aa07be81451729406cb6e13c77f3e497caf.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói tuy define N như vậy là ok, tuy nhiên **để best design**
> thì ổng không muốn vậy mà **tạo thêm một argument (length)
> của average để yêu cầu truyền array size vào**. Thì**thay vì
> dùng N ở trong function average thì dùng (length)**

<br>

<a id="node-405"></a>

<p align="center"><kbd><img src="assets/393e1031ecbb0b2b3d03f5f9e5be72e8c244af78.png" width="100%"></kbd></p>

<br>

<a id="node-406"></a>

<p align="center"><kbd><img src="assets/08f8b63236e7911714f6a4f447c66bf54f4bd918.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/479f4647ec22f6dc3ed31fd162f4bdcf6fc31b7e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ef7d0ad3fda9370d2e59f9d0eaeecefb6bf9e87f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/08f8b63236e7911714f6a4f447c66bf54f4bd918.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/479f4647ec22f6dc3ed31fd162f4bdcf6fc31b7e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ef7d0ad3fda9370d2e59f9d0eaeecefb6bf9e87f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0b45713136ff4fc167468bc4c579d70fcf93768e.png" width="100%"></kbd></p>

> [!NOTE]
> Mỗi **char** chiếm **1 byte = 8 bits** bộ nhớ. Nhớ lại, dựa
> theo quy ước **ASCII** map **một số với một char**, nên
> **thật sự nó cũng binary code** của nó (8bit) cũng chỉ là
> thể hiện một **con số.**
>
> Ví dụ bên dưới (machine code) của H là dãy **8 bits sao
> cho tính ra bằng 73**
>
> 2**7 + 2**6 + 2**5 + 2**4 + 2**3 + 2**2 + 2**1 + 2**0
>
>  128     64       32       16       8          4         2       1
>
>   0         1         0        0         1          0        0       1
>
> => 73 = **01001001** in machine code
>
> *Đừng lầm lẫn khi hồi nãy một int variable được assign
> cho giá trị 73 lại chiếm 4 bytes. **Đơn giản là int được cho
> 4 bytes** = 32 bits. Có nghĩa là **variable mang giá trị 73 đó 
> sẽ có dạng như sau:** 
>
> 00000000 00000000 00000000 **01001001**

<br>

<a id="node-407"></a>

<p align="center"><kbd><img src="assets/c508f9b671cf61dd77fc4d7ea267f678764d81cc.png" width="100%"></kbd></p>

<br>

<a id="node-408"></a>

<p align="center"><kbd><img src="assets/5efcb364d994f2c9bf3fca627763033605dce3c7.png" width="100%"></kbd></p>

<br>

<a id="node-409"></a>

<p align="center"><kbd><img src="assets/44f8e15452d3597603aa744d77d461ce5b28f863.png" width="100%"></kbd></p>

> [!NOTE]
> String này có 3 char chiếm 3 bytes

<br>

<a id="node-410"></a>

<p align="center"><kbd><img src="assets/8e39cf443afbc39a0a9a37b272abab35bff058ef.png" width="100%"></kbd></p>

> [!NOTE]
> D: Under hood string nó là cái gì?
>
> Someone: **Array of character**

<br>

<a id="node-411"></a>

<p align="center"><kbd><img src="assets/1a1f44c4fdab3eb8d4e3741a636c33ca3538ba9f.png" width="100%"></kbd></p>

> [!NOTE]
> String là một array các characters như đã biết mỗi char
> chiếm 1 bytes = 8 bits

<br>

<a id="node-412"></a>

<p align="center"><kbd><img src="assets/941e0053cb58d267f6bb238769b7b293648b11f6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/941e0053cb58d267f6bb238769b7b293648b11f6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/15d8da7a76af853ed264f3c6f9818117e90839be.png" width="100%"></kbd></p>

> [!NOTE]
> Tuy nhiên nó **tự thêm một byte** mang giá trị = 0 (0000000) ở
> cuối để **phân biệt khi nào end một string** (ý là trên
> memory các byte của các string cứ nằm kế tiếp nhau thì
> phải có  cái này để phân biệt nó ra
>
> Nên H i ! chiếm 3 bytes, tự thêm 1 bytes là 4.
>
> D a v i d chiếm 5 bytes tự thêm 1 bytes là 6
>
> Kí hiệu **\\0 để phân biệt nó với character '0' số 0**. Như ta biết 
> trong ASCII, các CHỮ SỐ cũng được map với một số nào đó.
> Cụ thể CHỮ SỐ **0, map với 48**. Có nghĩa là **nếu chuỗi 4 bytes
> có giá trị: 72 73 33 48 thì nó sẽ là "H i ! 0"**

<br>

<a id="node-413"></a>

<p align="center"><kbd><img src="assets/c4f99e6c80ac98a7c39abe12d8779c986aa15d24.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3b5f0aea258f87ab386881d2ea75f8a501d84aca.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c4f99e6c80ac98a7c39abe12d8779c986aa15d24.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3b5f0aea258f87ab386881d2ea75f8a501d84aca.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/badd44e8877b0f8c56c5edf737f9d7dbc28fd8e9.png" width="100%"></kbd></p>

> [!NOTE]
> **"\\0"** gắn với ASCII = **0**= **00000000**
> có tên riêng là kí tự NUL
>
> **"0"** (chữ số 0, trong ASCII gắn với **48**= **00110000**
>
> 00110000 = 0 + 0 + 32 + 16 + 0 + 0 + 0 + 0

<br>

<a id="node-414"></a>

<p align="center"><kbd><img src="assets/3c8db2923aa2723b9553457d5d40b393f42f63c7.png" width="100%"></kbd></p>

<br>

<a id="node-415"></a>

<p align="center"><kbd><img src="assets/1b5cb79cd7bcbbd01b1d89b6d636a8bc3502fe88.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng thử in char như vầy.
> **%c** là format cho char

<br>

<a id="node-416"></a>

<p align="center"><kbd><img src="assets/2b77246edaa28bb05ecb039b7d3cb49da317e521.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng ổng nói cũng có thể để
> **%i**, nó sẽ cho ra **số**, **key** mapping
> của char theo **ASCII**

<br>

<a id="node-417"></a>

<p align="center"><kbd><img src="assets/e8962d7663128be857ab9a2e1b2ad3a37fb67e98.png" width="100%"></kbd></p>

> [!NOTE]
> Kế tiếp ổng quay lại define string s = "Hi!" và làm như vầy
> để in các char ra.
>
> Nhận xét một điều khá hay ho là trong C (mà trong Java
> ko có)  đó là **vì bản chất string là một array chứa các char**,
> nên **chỉ cần dùng s[i] là lấy char ra.**

<br>

<a id="node-418"></a>

<p align="center"><kbd><img src="assets/bdfff2c17186e095f79ecad133f171c98560682d.png" width="100%"></kbd></p>

> [!NOTE]
> Và để minh hoạ cho việc string = array các char nhưng tự
> động thêm vào '\\0' ở cuối
>
> Ổng in với %i và với cả **s[3]** (dù string s chỉ có 3 kí tự H, I, !)
>
> Kết quả đúng là char cuối có **ASCII key = 0 gắn với NUL char**

<br>

<a id="node-419"></a>

<p align="center"><kbd><img src="assets/111e84b8b1a85adccf544b01cd1b8a3681471c35.png" width="100%"></kbd></p>

> [!NOTE]
> Q: tại sao khi define string s dù là array
> lại ko có square bracket []
>
> D: Vì string **bản thân nó là array**, nên nó **tự động 
> tạo array ở dưới**, không cần declare như int[]

<br>

<a id="node-420"></a>

<p align="center"><kbd><img src="assets/51113c29545be8b0bf745372702c24ef805470af.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/51113c29545be8b0bf745372702c24ef805470af.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4edf1774fc17ae1b067f68bd2a15eb283ec1dc9c.png" width="100%"></kbd></p>

<br>

<a id="node-421"></a>

<p align="center"><kbd><img src="assets/7372da10a300334fed32d766f81c6e465c67881a.png" width="100%"></kbd></p>

<br>

<a id="node-422"></a>

<p align="center"><kbd><img src="assets/7d8a720b3bea079b632dee3aa0a4914b53581153.png" width="100%"></kbd></p>

> [!NOTE]
> Tạo array of string, (với string là array of
> char), thì đây như là **array of array**

<br>

<a id="node-423"></a>

<p align="center"><kbd><img src="assets/11fc349ea0794f36095231b364fff261d910410b.png" width="100%"></kbd></p>

> [!NOTE]
> Và để**access char đầu tiên** trong **string
> đầu tiên** trong array:**words[0][0]**
>
> Và in ra với **%c** như hồi nãy

<br>

<a id="node-424"></a>

<p align="center"><kbd><img src="assets/62e6cc539a86247859fb384bf350a962f466f189.png" width="100%"></kbd></p>

<br>

<a id="node-425"></a>

<p align="center"><kbd><img src="assets/06eb4051ed0e761b7b95f20c4df0e80f7a0e850f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/06eb4051ed0e761b7b95f20c4df0e80f7a0e850f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5c6d2d7a723911847ac6a9f0fa6a139d75552bd8.png" width="100%"></kbd></p>

> [!NOTE]
> Trong memory nó sẽ như thế này: 
>
> **string array** chứa **2 string** 
>
> mỗi **string là một array** chứa **4 và 5 char,** mỗi char chiếm **1 byte**

<br>

<a id="node-426"></a>

<p align="center"><kbd><img src="assets/cc9e8feb6e8519f8348e4cde42fdf2d749819718.png" width="100%"></kbd></p>

> [!NOTE]
> Q: **new line character** có tốn space ko. 
>
> D: Có, nhưng nó ko thuộc string, nên printf take care

<br>

<a id="node-427"></a>

<p align="center"><kbd><img src="assets/0d52ed483c0d5fb9bfae6e235a235a3549486bba.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng dùng cách này **while loop**, trong các
> **char của string để check khi nào gặp '\\0'** để **từ đó
> đếm được số char của string.**
>
> Và ổng nói**tuy array không thể đếm length** nhưng vì
> **string là một array đặc biệt** khi có char **'\\0'** nên **có thể dùng
> để đếm length of string**

<br>

<a id="node-428"></a>

<p align="center"><kbd><img src="assets/27a2bcaa92badb843b1a73e0b4285cc8be1a106a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/27a2bcaa92badb843b1a73e0b4285cc8be1a106a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/90d36ad4f4428053487b1796559eab6eee4de0ae.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ổng nói có nhiều người đã
> giải quyết vấn đề này. Nên có một
> **thư viện hỗ trợ string**

<br>

<a id="node-429"></a>

<p align="center"><kbd><img src="assets/97399f0c2b8d693e38f1653a5afefc043cee4fb4.png" width="100%"></kbd></p>

> [!NOTE]
> D: Chưa được chỗ nào?
>
> A: Phải include <**string.h>** thì mới có **strlen()**

<br>

<a id="node-430"></a>

<p align="center"><kbd><img src="assets/4e3d2018dd4ddcd54450a4af7c06e63fb80cd81d.png" width="100%"></kbd></p>

<br>

<a id="node-431"></a>

<p align="center"><kbd><img src="assets/665924928caf2cee3fd786504bd478a42c427e6e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/665924928caf2cee3fd786504bd478a42c427e6e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e04fd371c6969e355b66fb2a36bf887b62e232c3.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự có thư
> viện hỗ trợ char

<br>

<a id="node-432"></a>

<p align="center"><kbd><img src="assets/3b45e995821f0d8a92d5da7f5d06feb46492ae81.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3b45e995821f0d8a92d5da7f5d06feb46492ae81.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/cf146cb7d0041ece14e8d7ee6ee86bc62cdaae53.png" width="100%"></kbd></p>

> [!NOTE]
> Khá hay ho
>
> loop trong các char của string
>
> và dùng**s[i] >= 'a' && s[i] <= 'z'** để check nó phải **lowercase ko**.
>
> Có nghĩa là vì **s[i] là char,** mà thực tế nó **cũng chỉ là một số** (từ
> giá trị của 8 bit theo binary tính ra giá trị theo hệ số 10 decimal
> nên char **có thể so sánh bằng <, =, >**
>
> Và vì nếu >= 'a' và <= 'z' thì đương nhiên nó là 1 trong các 
> 'a', 'b',....'z' đồng nghĩa nó là lowercase chả.
>
> Thứ hai, dựa vào bản ASCII,**key value của kí tự viết hoa luôn
> cách key value của kí tự viết thường 32 số** ví dụ **'a' = 97, 'A' = 65**
> **'b' = 98, 'B' = 66.**..
>
> Nên bằng việc **in ra s[i] - 32**, nó sẽ in ra **kí tự HOA của kí tự s[i]**
>
> Và ổng nói trong **Microsoft Word**,..thì t**hật ra bên dưới khi dùng lệnh 
> lowercase thì nó cũng làm vậy**

<br>

<a id="node-433"></a>

<p align="center"><kbd><img src="assets/e3724c9d930b5af5c078c71ca484354164ec0c29.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e3724c9d930b5af5c078c71ca484354164ec0c29.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/402bbfd4583b3c158a7cf29eedfcb61e06d489d6.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói **<ctype.h>** người ta đã **hỗ trợ các function
> làm những việc này (liên quan đến char)**
>
> Nên chỉ cần dùng **islower**() để **check lowercase**
> và **toupper**() để nó **chuyển thành upper case** (bên
> dưới vẫn chính là do the math - 32) như đã làm

> [!NOTE]
> Và hoá ra **toupper**() nó sẽ **ignore nếu
> char đã ở uppercase nên không cần
> phải check chi nữa**

> [!NOTE]
> D: Tại sao gọi **strlen**() như thế này ko ổn (well design)
>
> A: Vì **mỗi lần loop, khi nó check i**, thì nó lại gọi **strlen**()
> sẽ **tốt hơn nếu tính strlen() trước**
> D: Correct!

<br>

<a id="node-434"></a>

<p align="center"><kbd><img src="assets/3284a042dd52fbf21bec871c6b8c70596890e221.png" width="100%"></kbd></p>

> [!NOTE]
> Chính xác, và có thể làm kiểu này (chưa thấy trong java)
>
> for (int i = 0, **n = strlen(s)**; i < **n**; i++){
> }

<br>

<a id="node-435"></a>

<p align="center"><kbd><img src="assets/e8dc0467c3ea7d5259548013db5c210237d44012.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng nói như **function argument** là **những gì
> bỏ vào function**.
>
> Thì **command line argument** là những**tất cả những gì
> sau dấu $** như **make**, code, hay **-o.**...

<br>

<a id="node-436"></a>

<p align="center"><kbd><img src="assets/b710a1917b115a4d39964d04cf14022da9678bb8.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng nói theo cách thông thường **cứ phải
> run program**, **wait** for the name,**enter the name**, hit
> enter...
>
> hoặc **tưởng tượng khi các function khác cũng vậy** như
> gõ make, enter, rồi gõ tên file, enter
>
> hoặc khi chẳng directory phải gõ cd, enter, rồi gõ tên 
> folder, enter,... 
>
> nói chung là nếu mọi thứ đều như vậy thì**sẽ rất chậm**

<br>

<a id="node-437"></a>

<p align="center"><kbd><img src="assets/a304138889ddfa567f6b1cf8c40ffa0441cc588d.png" width="100%"></kbd></p>

> [!NOTE]
> nên giờ ổng đổi như vầy, cho main (void) thay bằng
> main(i**nt argc, string argv[])**
>
> Có nghĩa là giờ **main sẽ có argument.**
> **argv[]** dễ đoán là viết tắt của **argument value**sẽ là **array string
> đưa vào** sau $
>
> còn **argc** là argument count dùng để**đếm số argument value
> trong array.**
> Tương tự như ở trên đã biết trong C,**trừ string** là một array 
> of char đặc biệt **có thể có cách đếm số item trong array dựa
> vào '\\0'**, còn lại th**ì không có cách nào đếm số item trong array
> như int[].**.nên phải**tự track số lượng**

<br>

<a id="node-438"></a>

<p align="center"><kbd><img src="assets/748a79b2d3e64186bec98807e14f2c077ad14e1b.png" width="100%"></kbd></p>

> [!NOTE]
> với thay đổi này, chỉ cần gọi **./greet David** là
> nó **nhận David vào argument argv[]** và lấy ra
> bởi **argv[1]**

<br>

<a id="node-439"></a>

<p align="center"><kbd><img src="assets/479378735301c9e9b9e68a38dddd13fad104736b.png" width="100%"></kbd></p>

> [!NOTE]
> Yeah, **argv[0] là "./greet"** là cái **string đầu tiên sau dấu $**

<br>

<a id="node-440"></a>

<p align="center"><kbd><img src="assets/186aaaa3446acef85b00acb85aaa3b021cfe1119.png" width="100%"></kbd></p>

> [!NOTE]
> Và có thể dùng thêm các
> **argv[1] argv[2].....**.

<br>

<a id="node-441"></a>

<p align="center"><kbd><img src="assets/5179b7e5b37dd2660eccabe21037656a765b6aaf.png" width="100%"></kbd></p>

<br>

<a id="node-442"></a>

<p align="center"><kbd><img src="assets/18ee704325ea2dccc08fd4165259d709d4b654bc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/18ee704325ea2dccc08fd4165259d709d4b654bc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/52424cab8e18dcea86dcd575b0f3d3c27238f4fb.png" width="100%"></kbd></p>

<br>

<a id="node-443"></a>

<p align="center"><kbd><img src="assets/53c1719d9031691633f97809c1188a9002327e47.png" width="100%"></kbd></p>

<br>

<a id="node-444"></a>

<p align="center"><kbd><img src="assets/789ca732ac0e42553673846aaf544320939bbeef.png" width="100%"></kbd></p>

<br>

<a id="node-445"></a>

<p align="center"><kbd><img src="assets/f5614f9f111d8302d4c8e971ff84a651c20079cb.png" width="100%"></kbd></p>

<br>

<a id="node-446"></a>

<p align="center"><kbd><img src="assets/76c507bb107c2cdeb477eafa6856124d52d94d81.png" width="100%"></kbd></p>

> [!NOTE]
> Nói chung là một chương trình
> lâu đời tích hợp sẵn để **play với
> command line cho vui**

<br>

<a id="node-447"></a>

<p align="center"><kbd><img src="assets/139256d53d367525686e3c29846f249a03eedcb9.png" width="100%"></kbd></p>

<br>

<a id="node-448"></a>

<p align="center"><kbd><img src="assets/762911281b5d5d6a9e728aecc9001dc83642e7be.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/762911281b5d5d6a9e728aecc9001dc83642e7be.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1ed153e06e01517a0ab38d0a3f14a0727028b2c3.png" width="100%"></kbd></p>

> [!NOTE]
> Cơ bản là**return number của function
> cho biết thông tin của error**

<br>

<a id="node-449"></a>

<p align="center"><kbd><img src="assets/33b2f34851cb313ddf49e4bc0d63e0e4bbc86fb8.png" width="100%"></kbd></p>

> [!NOTE]
> **int** của **main()** là cách C design có
> nghĩa là main hidden behind**luôn
> return một int. Default là 0**

<br>

<a id="node-450"></a>

<p align="center"><kbd><img src="assets/e7326b0b64d39ed900b1dc9014966a6af654c595.png" width="100%"></kbd></p>

> [!NOTE]
> Dùng **echo $?** để xem return
> number của function vừa gọi

<br>

<a id="node-451"></a>

<p align="center"><kbd><img src="assets/71ecb15186cd2e587eb33cdbb9111c748a5138b1.png" width="100%"></kbd></p>

<br>

<a id="node-452"></a>

<p align="center"><kbd><img src="assets/fa942e837681d21eaa763bc315a7f3b2b07deffc.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là mục đích (của cái return int) là để **khi cần ta có
> thể return con số để cho biết program có work đúng hay
> không**
>
> Như ở đây, nếu không làm gì thì lúc nào  nó cũng return 0,
> dùng **echo $? để xem**

<br>

<a id="node-453"></a>

<p align="center"><kbd><img src="assets/b61b60300955a441cb9fd9d95e5304dc7e6e59ac.png" width="100%"></kbd></p>

<br>

<a id="node-454"></a>

<p align="center"><kbd><img src="assets/373eaef3767e322c5d1635c40241cb12f51466ef.png" width="100%"></kbd></p>

> [!NOTE]
> Nói qua mã hoá (encryption)
> và giải mã (decryption)

<br>

<a id="node-455"></a>

<p align="center"><kbd><img src="assets/db20faf3e9b7877052ddb2f725b88ce10208c876.png" width="100%"></kbd></p>

> [!NOTE]
> Mã hoá, **cipher** chỉ là fancy name của **algorithm**
> giúp **mã hoá** **plaintext** thành **ciphertext** (kiểu
> nhữ thông tin được mã hoá)

<br>

<a id="node-456"></a>

<p align="center"><kbd><img src="assets/228eb20671a40820357ca0a974e4d4d99cbee689.png" width="100%"></kbd></p>

<br>

<a id="node-457"></a>

<p align="center"><kbd><img src="assets/0b86bedd34d0c2b0559177e78857fd82b9b79a8f.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **để mã hoá** hay**giải mã** cần biết
> **algorithm gì**, và**key gì** ví dụ dùng Ceasar (hoán
> đổi vị trí, A -> B, B -> C...là Ceasar với key = 1
> - tức hoán đổi 1 vị trí)

<br>

<a id="node-458"></a>

<p align="center"><kbd><img src="assets/bf5284e63c44761892c42db695b0407b2127de57.png" width="100%"></kbd></p>

<br>

<a id="node-459"></a>

<p align="center"><kbd><img src="assets/97b4d05b235a772b03eacccc94224d6324a1bd3d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/65ff228abecd2570e22260b5a1f890dae1629eff.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/97b4d05b235a772b03eacccc94224d6324a1bd3d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/65ff228abecd2570e22260b5a1f890dae1629eff.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/967424e0e935f4b4f57a445670f8c460ec6c104b.png" width="100%"></kbd></p>

> [!NOTE]
> Và để giải mã ta sẽ làm ngược
> lại U lùi lại 1 thành T (TU), I -> H
> ...:THIS IS CS50

<br>

