# Ghi Chú Tay Cho Lab + Problem Set - Week 4 - Memory

📊 **Progress:** `46` Notes | `93` Screenshots

---

<a id="node-1491"></a>
## Lab 1 Smiley

<br>

<a id="node-1492"></a>

<p align="center"><kbd><img src="assets/d5bbf62ae49f8d8a9771a9e5b09434ea821b38cd.png" width="100%"></kbd></p>

<br>

<a id="node-1493"></a>

<p align="center"><kbd><img src="assets/a393ac9e1a27c04e17e0c3c525e6cc2a59be25f1.png" width="100%"></kbd></p>

<br>

<a id="node-1494"></a>

<p align="center"><kbd><img src="assets/03604c35edbf0da8c4d29df5813e716e8f0a9c98.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là trong picture, mỗi pixel "có" 3 bytes:
> 1 bytes cho value của Red, 1 bytes cho value 
> của Green, 1 bytes cho value của Blue.
>
> Với 1 bytes, thì như ta đã biết nó có thể thể hiện
> từ 0 (00000000 hay 0x00 trong base-16) tới 
> 255 (11111111 hay 0xff)
>
> Và như vậy combo mấy màu này có thể cover mọi
> màu

<br>

<a id="node-1495"></a>

<p align="center"><kbd><img src="assets/50dfda789be13c94dfb1a0d6de86ddedda75cb57.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là trong lib bmp.h có define một struct: 
> typedef struct {
> ...3 variable thuộc "loại" BYTE = 8-bit integer.
> } RGBTRIPLE
>
> Ở đây nhớ lại int trong C được "cho" 4 bytes tức là
> 32 bits. Còn BYTE là integer 8-bit. Thì mình hiểu 
> nôm na là int cần để chứa số nguyên, nên cần 32 bit
> (mà còn không đủ, khi muốn thể hiện số lớn hơn 2 tỷ
> phải cần đến long = 8 bytes = 64 bits)
>
> Còn BYTE có thể chỉ cần 8 bit để thể hiện một dải giá
> trị có max chỉ 255 là đủ.
>
> ====
>
> Rồi một số điều mới biết đó là image nó có metadata
> hay còn gọi là headers. 
>
> Và với một pixel thuộc "loại" RGBTRIPLE ở trên thì
> có thể access các colors của nó (các variable của nó
> thuộc loại BYTE như mới nói) bằng .rgbtBlue, rgbtRed,
> .rgbtGreen. Cái này thì ko có gì khó hiểu, struct - nó chưa phải
> object nhưng cũng gần gần với object

<br>

<a id="node-1496"></a>

<p align="center"><kbd><img src="assets/57e6bd4ae5901aaf82bce658cc648a88302ba1dd.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là mình sẽ "làm" function **colorize()** này.
> Để làm sao có thể nhận một 2D array các giá trị pixel của
> Image và chuyển đổi các màu đen thành màu mong muốn
>
> Ở dưới chỉ cách compile và chạy thử function, nó sẽ 
> nhận file image gốc cần chỉnh sửa smiley.bmp và xuất ra
> image (outfile.bmp)

<br>


<a id="node-1497"></a>
### Thought Question

> [!NOTE]
> Thought Question
>
> How do you think you **represent a black pixel**
> when using a**24-bit color BMP file**?
>
> Is this the same or different when mixing paints
> to repesent various colors?

> [!NOTE]
> 1. A: Hình như là chuỗi số 0 hết tức là 
>
> 00000000 (Red), 00000000 (Green) 00000000 (Blue)
>
> Hay 0x00 Red, 0x00 Green, 0x00 Blue 
>
> Hay #000000
>
> Hay nói cách khác cả ba BYTE var rgbtRed, Green, Blue 
> của RGBTRIPLE đều = 0
>
> 2. A: Chưa hiểu câu hỏi.

<br>

<a id="node-1498"></a>

<p align="center"><kbd><img src="assets/592842b55764ef6dd9a2988ba74d96b09f04f020.png" width="100%"></kbd></p>

> [!NOTE]
> Loop trong các pixel là các RGBTRIPLE struct
>
> Check có phải nó là black pixel không: nếu cả 3 variable: 
> rgbtRed/Green/Blue (loại BYTE là 8-bit integer) đều bằng 
> 0 thì nó là Black
>
> Thì khi đó assign lại cái màu khác (bằng cách đổi giá trị 
> khác (từ 0-255))

<br>

<a id="node-1499"></a>

<p align="center"><kbd><img src="assets/fefa19a80d21dc0d992ea5f91f85e00035bf489b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fefa19a80d21dc0d992ea5f91f85e00035bf489b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3e1326b4caca8fe68ec630f3e54129e69510d4eb.png" width="100%"></kbd></p>

<br>

<a id="node-1500"></a>

<p align="center"><kbd><img src="assets/a05f9b01d2c7073ed750088ca962cc8288be8a7d.png" width="100%"></kbd></p>

<br>


<a id="node-1501"></a>
## Lab 2: Volume

<br>

<a id="node-1502"></a>

<p align="center"><kbd><img src="assets/64793699c0a84965f0c476528827b0b2d7a018d9.png" width="100%"></kbd></p>

> [!NOTE]
> Đổi volume của audio file

<br>

<a id="node-1503"></a>

<p align="center"><kbd><img src="assets/69c579067d3599ef215bf744a50a509b282605a1.png" width="100%"></kbd></p>

<br>

<a id="node-1504"></a>

<p align="center"><kbd><img src="assets/3367012d6496fb66140e8c2641729bda128db6fc.png" width="100%"></kbd></p>

<br>

<a id="node-1505"></a>

<p align="center"><kbd><img src="assets/2ade8505fc169db75c7073fa1a86680c73d123e4.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là cái thư viện stdint.h nó có declare sẵn một
> số loại (type) ví dụ như uint8_t, và int16_t.
>
> Unsigned (có chữ u phía trước như uint8_t) có nghĩa là
> nó dành hết 8 bits để chứa value. Và như vậy chỉ thể hiện
> số dương thôi. Do đó max của nó là 8 số 1: 11111111 = 255
>
> Nhưng Signed, ví dụ int8_t thì nó phải dành 1 bit đầu cho 
> "dấu (sign)" với 0 là số dương, 1 là âm. Thành ra chỉ còn 7 bit
> cho giá trị. Nên số dương lớn nhất chỉ còn + 127, và số âm 
> nhỏ nhất là -128.
>
> Tại sao: 
>
> Max: 0 (sign = số dương) còn lại 7 bit cho 7 số 1 hết thì ta có:
> 1*2^6 + 1*2^5 + 1*2^4 + 1*2^3 + 1*2^2 + 1*2^1 + 1*2^0
> = 64 + 32 + 16 + 8 + 4 + 2 + 1 = 127
> Min: 1 (sign = số âm) còn lại 7 bit cũng số 1 hết thì 
> 1 000000 sẽ là -1
> 1 000001 sẽ là -2
> ...
> 1 1111111 sẽ là -128
>
> ====
>
> Do đó với định nghĩa của WAV file trong đó 44 byte đầu tiên
> dành cho header thì ta có thể cho rằng nó chỉ số dương nên
> Ta có thể **"TREAT CÁC BYTE ĐÓ NHƯ uint8_t value"**Còn chuỗi samples mỗi sample là 2 bytes mang gía trị
> của âm thanh thì ta sẽ **TREAT CÁC BỘ 2 BYTES NÀY
> NHƯ int16_t value**

<br>

<a id="node-1506"></a>

<p align="center"><kbd><img src="assets/4ebd5bcc25b7cec2e050c5998e764ac8de3febff.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là function sẽ nhận 3 argument (nếu check
> phải check argc _argument count = 4) vì như đã biết
> cái tên function là 1 argument rồi
>
> Thì ta sẽ mở file gốc ra, mở file đích ra.
>
> Loop trong đó, hay đọc các byte trong đó
>
> Nôm na là 44 byte đầu tiên là header thì giữ nguyên
> chỉ ghi (write) y xỳ vào file đích
>
> Còn các 16 bits sample tiếp theo, thì nhân giá trị với
> Factor trước khi ghi vào file đích.
>
> Nôm na là vậy

<br>

<a id="node-1507"></a>

<p align="center"><kbd><img src="assets/4f0043636c00104d1edaef5be257809fecc0fb77.png" width="100%"></kbd></p>

<br>

<a id="node-1508"></a>

<p align="center"><kbd><img src="assets/37a55b8d53ae612adf3981bead7e2b257c224f73.png" width="100%"></kbd></p>

<br>

<a id="node-1509"></a>

<p align="center"><kbd><img src="assets/875d381a20a13c6d82ecec2031abf924d6ecfd3e.png" width="100%"></kbd></p>

> [!NOTE]
> các 2-bytes samples đơn giản chỉ là một con số,
> ví lí do gì đó mà sample được cho 2 bytes = 16 bits để thể hiện 
> giá trị. Có nghĩa là max của nó là 2^17 - 1 = 131071
> (Ở đây cứ nhớ vầy: ví dụ 8 bit thì max là 2^7+2^6.. 2^0 thì chính
> là bằng 2^8-1= 256-1 = 255. Nên tương tự nếu có 16 bit thì mã
> sẽ là 2^17-1 = 131071)
>
> Và việc nhân con số này lên sẽ tạo hiệu quả là  làm nhân (scale) 
> volume lên (cái này cứ biết vậy thôi)

<br>

<a id="node-1510"></a>

<p align="center"><kbd><img src="assets/72a7c7052909a45769fe6f4590f5a8ae5f5b9406.png" width="100%"></kbd></p>

> [!NOTE]
> Function sẽ nhận 3
> command-line argument

<br>

<a id="node-1511"></a>

<p align="center"><kbd><img src="assets/20e115ff7130ae578d3828c4ecb70d37d8951212.png" width="100%"></kbd></p>

<br>

<a id="node-1512"></a>

<p align="center"><kbd><img src="assets/51c277543c00535736251bb15bf7dadb6c48cfae.png" width="100%"></kbd></p>

<br>

<a id="node-1513"></a>

<p align="center"><kbd><img src="assets/6dfdf396dc84e6bbcce6fe05f1eaf325b6d50fd6.png" width="100%"></kbd></p>

> [!NOTE]
> Đọc doc

<br>

<a id="node-1514"></a>

<p align="center"><kbd><img src="assets/2c479ef99d4d2c8e04182f58724ab9a058400a9e.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói khi copy header thì vì đã biết luôn có 44
> bytes của header nên chỉ việc read từ file gốc 44
> bytes đầu và write vào file đích thôi
>
> Còn đọc sample và nhân với factor rồi ghi vào
> file đích thì cần loop cho đến khi hết

<br>

<a id="node-1515"></a>

<p align="center"><kbd><img src="assets/a7cb8c86c005dbb5db3da65c7f1375bad59e24f4.png" width="100%"></kbd></p>

> [!NOTE]
> Còn lại thì tự làm hết với các chú ý rút ra như sau:
>
> 1. Để hiểu function fread, nhận argument đầu tiên là một **pointer**:
>
> Ví dụ trong doc của họ:
>
> char c;  -> Tạo một vùng memory 1 byte cho c.
>
> fread(**&c**...) hoặc tạo**int *p = &c**; fread(**p**,....) cũng sẽ đúng -> Read file và **load thông
> tin vào vùng memory có ADDRESS là &c (hay p)**
>
> Tương tự như vậy: **uint8_t header[44];** -> **Tạo vùng memory rộng 44 bytes** cho
> header
>
> for loop..: fread(&header[i], 1, 1, input):  -> Có nghĩa là **read file và load data vào
> vùng memory mà  ADDRESS là &header[i]**====
>
> 2. Cũng có thể làm gọn, không cần phải "đọc 1 byte rồi bỏ vào array rồi ghi vào
> file output 1byte". Vì fread cho phép **đọc nhiều byte**, quy định bởi arg size (thứ 2) 
>
> Nên làm theo solution của họ thì như sau:
>
> fread(**header**, **HEADER_SIZE**, 1, input); 
>
> fwrite(**header**, **HEADER_SIZE**, 1, output);
>
> Thì cơ bản là bảo máy tính **đọc và load data 44 byte** vào **vùng memory tại
> header** và sau đó là **ghi vào output data** tại vùng memory của header.
>
> Chú ý là **header ở đây thì không cần dùng &header**.
>
> Có thể lí giải là vì **bản thân header là array thì** **nó cũng là pointer** (tới các
> int16_t) rồi.
>
> Cũng như trong bài giảng có chỗ khi dùng s - string thì không cần & vì **bản thân
> nó là pointer rồi**

<br>

<a id="node-1516"></a>

<p align="center"><kbd><img src="assets/50694c41918741038514869944dfe7373a377dc9.png" width="100%"></kbd></p>

> [!NOTE]
> Sai một chỗ khiến code work đúng khi factor 2.0,
> 3.0 nhưng không khi factor 0.5: Đó là nhầm lẫn
> **int16_t** thì lại ghi là **uint16_t**. Phải search google
> mới phát hiện.

<br>

<a id="node-1517"></a>

<p align="center"><kbd><img src="assets/b6ed8bb96efc6998336cff74de2a614d2bf87da3.png" width="100%"></kbd></p>

<br>


<a id="node-1518"></a>
## Ps : Recover

<br>

<a id="node-1519"></a>

<p align="center"><kbd><img src="assets/a4d45a6843df7451677e6c7a543f63986f2e3a88.png" width="100%"></kbd></p>

<br>

<a id="node-1520"></a>

<p align="center"><kbd><img src="assets/83e305b09907a0f6fd2ec92468286a98b6fe2f71.png" width="100%"></kbd></p>

> [!NOTE]
> "r" = read mode

<br>

<a id="node-1521"></a>

<p align="center"><kbd><img src="assets/500781d3baae2c060d7fbdcbc213e08a2381392e.png" width="100%"></kbd></p>

<br>

<a id="node-1522"></a>

<p align="center"><kbd><img src="assets/12c4d1bfc9ad784defec836e3ee6225cd34d77e4.png" width="100%"></kbd></p>

<br>

<a id="node-1523"></a>

<p align="center"><kbd><img src="assets/a7793bccb448fdac8b0a858653af1efca968799f.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ **đọc file theo từng chunk 512 bytes** và check
> pattern bằng cách **check 4 bytes đầu tiên**
>
> Khi check thấy trong một cục đó có pattern của  một jpeg
> file (bằng cách check 4 byte đầu tiên)
>
> Tại sao chỉ **check 4 byte đầu tiên**: Là bởi ổng nói nó - là
> cái cơ chế FAT của máy ảnh
>  - sẽ ghi data theo kiểu giả sử l**ưu hết 1 image rồi mà
> vẫn dư** thì nó**vẫn qua chunk 512 bytes tiếp theo** để
> ghi image mới. Và phần dư của cái chunk gọi là **slack space**

<br>


<a id="node-1524"></a>
### Fortunately, digital cameras tend to store photographs contiguously on

> [!NOTE]
> Fortunately, digital cameras tend to store photographs contiguously on
> memory cards, whereby each photo is stored immediately after the previously
> taken photo. Accordingly, the start of a JPEG usually demarks the end of
> another.
>
> **However**, digital cameras often initialize cards with a FAT file system
> whose**“block size” is 512 bytes (B)**. The implication is that these cameras
> only write to those cards in units of 512 B. A photo that’s 1 MB (i.e., 1,048,576
> B) thus takes up 1048576 ÷ 512 = 2048 “blocks” on a memory card. But so
> does a photo that’s, say, one byte smaller (i.e., 1,048,575 B)! The **wasted
> space** on disk is called “**slack space**.” Forensic investigators often look at
> slack space for remnants of suspicious data.
>
> The implication of all these details is that you, the investigator, can probably
> write a program that **iterates over a copy of my memory card**, **looking for
> JPEGs’ signatures**.
>
> Each time you **find a signature**, you can **open a new file** **for writing**
> and start **filling that file with bytes from my memory card**, closing that file
> only**once you encounter another signature**.
>
> Moreover, **rather than** read my memory card’s **bytes one at a time**, you can
> **read 512 of them at a time** into a buffer for efficiency’s sake. Thanks to FAT,
> you can trust that JPEGs’ signatures will be “block-aligned.” That is, you need
> **only look for those signatures in a block’s first four bytes.**

<br>


<a id="node-1525"></a>
#### Realize, of course, that JPEGs can span contiguous blocks. Otherwise, no JPEG could be larger than 512 B. But the **last byte of a JPEG might not fall at the very end of a block.**  Recall the possibility of**slack space**. But not to worry. Because this memory card was **brand-new**when I started snapping photos, odds are it’d been**“zeroed”**(i.e., filled with 0s) by the manufacturer, in which case any slack space will be filled with 0s. It’s okay if those trailing 0s end up in the JPEGs you recover; they should still be viewable.

> [!NOTE]
> Đại khái là ổng nói**một cái jpeg sẽ trải qua nhiều  block (512
> bytes)**. Và cái **byte cuối cùng của jpeg khả năng cao là không
> nằm ngay chóc cái byte  cuối cùng của block** (cái này thì dễ
> hiểu rồi)
>
> Và cũng như đã nói ở đoạn trước đó là phần dư (Chưa hết 1
> block mà đã hết jpeg) gọi là slack-space.
>
> Thì ổng nói là vì cái thẻ mới nên khả năng cao là chưa xài,
> nên cái phần dư đó chỉ có số 0, tức là còn mới tinh, chưa
> từng chứa dữ liệu gì.
>
> Như đã học, ổng nói vậy vì nếu mà cái thẻ xài rồi, khả năng
> khi ghi đến giả sử byte thứ 400 trong block thì kết thúc  data
> của jpec thì 112 cái byte còn lại có thể cũng có GARBAGE là
> data của chương trình nào đó lưu vào nhưng chưa xoá.
>
> Thì từ đây có thể cho ta cái hiểu rằng, cứ ghi hết data của mỗi
> block vào file dù cho block cuối data jpec của jpeg kết thúc trước
> byte cuối. Vì phần data trong slack sapce không ảnh hưởng gì

<br>


<a id="node-1526"></a>
#### Now, I only have **one memory card**, but there are a lot of you! And so I’ve gone ahead and created a “forensic image” of the card, **storing its contents, byte after byte**, in a file called card. raw.   So that you don’t waste time **iterating over millions of 0s** unnecessarily, I’ve only imaged the **first few megabytes** of the memory card. But you should ultimately find that the image contains 50 JPEGs.

<p align="center"><kbd><img src="assets/f374421fec6c07dcf31041e857fb8f0e3a9c4ed2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f374421fec6c07dcf31041e857fb8f0e3a9c4ed2.png" width="100%"></kbd></p>

> [!NOTE]
> Cuối cùng đại ý là ổng đảm bảo cái các jpegs chỉ nằm ở những
> megabytes đầu tiên của memory thôi chứ không phải nằm ở đâu
> đó xa xôi tuốt luốt để mà phải iterate cả triệu con số 0 (tức là các
> byte trống không có data) 
>
> Và dù vậy vẫn có 50 cái hình

<br>

<a id="node-1527"></a>

<p align="center"><kbd><img src="assets/15e111a6d2eb767883f500ee0b838d7ac469001c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/15e111a6d2eb767883f500ee0b838d7ac469001c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8088c1ee165a9907d85d33ee012e53fd702031b3.png" width="100%"></kbd></p>

<br>

<a id="node-1528"></a>

<p align="center"><kbd><img src="assets/a18826093f7b0776a83f702dcaddc490f5370142.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a18826093f7b0776a83f702dcaddc490f5370142.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2f1189f8245fd9afadbac19bb9595d75b7fd52ad.png" width="100%"></kbd></p>

> [!NOTE]
> "002.jpg" = 7 char -> Cần 8 bytes
>
> Đại khái là cách để open card.raw để bắt đầu đọc data.
>
> Dùng sprintf để "đặt tên" có nói rõ ở sau.Và không cần
> recover tên gốc của image mà chỉ cần đặt tên theo số 
> thứ tự là được
>
> Để check thử cái file mình recover có đúng không thì 
> chỉ việc bấm mở ra để xem, nếu là cái hình thì đúng
>
> Ở dưới là cách xoá file

<br>

<a id="node-1529"></a>

<p align="center"><kbd><img src="assets/ad6e3409cbffd1aacf60fde7bf6b73c324210d33.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây họ có hint cho việc tạo một new type dạng uint8_t
> chưa hiểu để làm gì.
>
> https://man.cs50.io/3/fread
> Còn việc đọc file bằng fread có hướng dẫn ở sau, đại khái
> Buffer sẽ là cái pointer, ta sẽ đọc từng element , mỗi element
> có BLOCK_SIZE = 512 bytes, raw file là cái file sau khi dùng
> fopen để mở file.
>
> Thì như họ cũng có nói (ở sau) cách để detect xem việc đọc
> và ghi file có thể kết thúc hay chưa. Thì ở đây chính là như vậy:
> Ta sẽ while cho đến khi nào lệnh fread trả về không bằng 512 bytes 
> nữa thì dừng (mà ở đây ổng nói thêm là nó sẽ trả về 0) bởi file
> raw được tạo Theo kiểu có đúng some numebr of 512 bytes block.

<br>

<a id="node-1530"></a>

<p align="center"><kbd><img src="assets/0b33741619f7a4e1007fbaad3ebe1e96e5e22476.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ lần lượt đọc từng chuck 512 bytes và detect
> xem 4 bytes đầu có  pattern của một jpeg ko

<br>

<a id="node-1531"></a>

<p align="center"><kbd><img src="assets/b364919bf382985102fa5b998db2341614992bf8.png" width="100%"></kbd></p>

> [!NOTE]
> Và khi xác định là có, thì:
>
> Nếu chưa thì tạo file và bắt đầu ghi
> data từ file này vào file đó
>
> Nếu đang ghi thì kết thúc tạo file mới và bắt đầu ghi

<br>

<a id="node-1532"></a>

<p align="center"><kbd><img src="assets/1b40f76326f8b9dbca469b0debec52a116ce2fad.png" width="100%"></kbd></p>

<br>

<a id="node-1533"></a>

<p align="center"><kbd><img src="assets/c2a20d82af9ab7a5fc00f9b605633a45b32d8281.png" width="100%"></kbd></p>

> [!NOTE]
> Đây là khi đang ghi thì phát hiện pattern ->
> Đóng file đang ghi và ghi file mới

<br>

<a id="node-1534"></a>

<p align="center"><kbd><img src="assets/89c33d4dbee430e907642f897ba3b69d9957060e.png" width="100%"></kbd></p>

<br>

<a id="node-1535"></a>

<p align="center"><kbd><img src="assets/e4730f2f180d217520f06d59f0df734dc8dc3211.png" width="100%"></kbd></p>

> [!NOTE]
> Size: **số bytes của mỗi element** mà mình đang cố gắng
> đọc từ file
>
> number: Số element mà mình muốn đọc cùng lúc  (all at
> once) Cái này nhiều khả năng là 1 thôi.
>
> và inptr: FILE mà mình sẽ đọc data từ đó
>
> Và có**chú ý là ta sẽ cần đọc file** từ memory card theo các
> **chunk 512 bytes** thì có nghĩa là như vậy ta sẽ **set size =
> 512 (mỗi element là 512 bytes)**

<br>

<a id="node-1536"></a>

<p align="center"><kbd><img src="assets/0d28ea4dd5fa0ce6ebc2f775fb09a3313ddca83c.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là mình sẽ đọc data thành từng **chunk 512 bytes.**
> Vì ta kiểu như làm sao có một cái array để chứa 512 bytes đó
>
> Thì từ đó mới check thử xem có phải là JPEG ko bằng cách
> check **4 byte đầu tiên**. (Với mỗi byte, kiểu như tính ra xem
> base-16 value của nó là bao nhiêu)
>
> Và so với quy luật
>
> ====
>
> 0xff = 255 Vậy cái byte thứ nhất phải là có chuỗi binary là 
> 11111111 hay tính ra phải là 255
>
> Nhớ lại 1 byte = 8 bit. Thì câu hỏi là đọc giá trị của 1 byte như
> thế nào? 
>
> A: Có thể là từ address tới 1 byte ví dụ p. Ta sẽ **int n = *p;** 
> để đi tới đó, và xem value của nó. thì check giá trị của nó 
> xem có bằng 255 không

<br>

<a id="node-1537"></a>

<p align="center"><kbd><img src="assets/9461475f4d450079c14ebc7817413a8bc68fa9c8.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là đối với cái byte thứ 4, thay vì so 16 lần
> với 16 cái pattern thì dùng cách **bit-wise arithmetic** như
> thế này. Nôm na là nó "**cắt đi bớt và so phần đầu thôi"**"Just look at the first four bits of this 8-bits, và set 4 bits 
> còn lại thành 0" (ví dụ 1234 5678 thì ) thành 1234 0000.
>
> Để rồi chỉ cần so kết qủa sau khi cắt với 0xe0. Phần này
> hiểu ý chính là vậy
>
> 0xe0 = e*16 + 0 = 14*16 + 0 = 224
> 0xe1 = e*16 + 1 = 14*16 + 1 = 225
> ....
> 0xef = e*16 + f = 14*16 + 15 = 239
>
> 0xe0 = 224: **1110** 0000 = 2^7 + 2^6 + 2^5 + ...0
> 0xe1 = 225: **1110** 0001 = 2^7 + 2^6 + 2^5 + ...2^0
> 0xe2 = 226: **1110** 0010 = 2^7 + 2^6 + 2^5 + ...2^1
> ..
> 0xef = 239:  **1110** 1111 = 2^7 + 2^6 + 2^5 + ...0

<br>

<a id="node-1538"></a>

<p align="center"><kbd><img src="assets/4f6b71720e7ae10ddb4bee7ed70af8a2bd6d2c4e.png" width="100%"></kbd></p>

> [!NOTE]
> Khi đã "tìm thấy một pattern cho thấy đó là
> jpeg thì ta sẽ **tạo một file mới** và **write data vào**
>
> Và **cần đặt tên file** để biết ta **đang ghi file jpeg thứ mấy**
> thì có thể dùng function **sprintf** là in vào một string
>
> Như này có nghĩa là in vào var string filename, một 
> content có dạng 3 digit.jpg (quy định bởi %03i), và số
> là giá trị digit -> filename sẽ là **002.jpg**

<br>

<a id="node-1539"></a>

<p align="center"><kbd><img src="assets/46ed8efccabfa181b13a7a72d48781c99300ffaf.png" width="100%"></kbd></p>

> [!NOTE]
> Phải make sure có **đủ memory = có đủ character**
> để fully **represent this entire file name**

<br>

<a id="node-1540"></a>

<p align="center"><kbd><img src="assets/9a8f060eb1cb66b80197cdd726daaa2638e4f27b.png" width="100%"></kbd></p>

> [!NOTE]
> Khi đó ta sẽ dùng FILE *img. = fopen(filename, "w") để
> mở file có tên filename mới đặt, ở mode "write" ("w")
> để có thể bắt đầu "write" file

<br>

<a id="node-1541"></a>

<p align="center"><kbd><img src="assets/03bba5982b965a87afecc59555b5fdd9c4eac407.png" width="100%"></kbd></p>

> [!NOTE]
> Để ghi data vào file:
>
> data: pointer to bytes (hay address của cái bytes) mà ta
> muốn ghi vào file
>
> size: Là số bytes trong mỗi element mà mình muốn write to
> the file, để coi lại element là gì
>
> number: Số element that you're going to write to the file
>
> outptr: FILE mà mình muốn ghi vào, chính là cái file mới mở
> ra ở trước.

<br>

<a id="node-1542"></a>

<p align="center"><kbd><img src="assets/924b6b476f6718acb97f8d715674a7d2c15dcc1a.png" width="100%"></kbd></p>

> [!NOTE]
> Và ta sẽ cứ tiếp tục detect và ghi file JPEG cho
> đến khi detect end of the file (file gốc trong bộ nhớ)

<br>

<a id="node-1543"></a>

<p align="center"><kbd><img src="assets/e128cbe4e463278d66a108da263b9df93bb909a3.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ tôi muốn đọc 255 elements = 255 bytes (À element là
> bytes) thì ý ổng nói là máy tính nó sẽ trả về từng cục 255
> bytes. Thì khi đến sắp hết file thì nó không còn trả đủ 255
> bytes nữa thì đó chính là dấu hiệu hết file
>
> Có thể chưa rõ chỗ này cụ thể là gì nhưng đại khái là  vậy
> để **check khi nào thì kết thúc**

<br>

<a id="node-1544"></a>

<p align="center"><kbd><img src="assets/6d65966b43ed7983ba2bde8a92d34db60909efd4.png" width="100%"></kbd></p>

<br>

<a id="node-1545"></a>

<p align="center"><kbd><img src="assets/3929362d4ee282564256f71f234b6967f132e5cb.png" width="100%"></kbd></p>

<br>

<a id="node-1546"></a>

<p align="center"><kbd><img src="assets/983b8bc6235b407b3b674a78c71da60c6691514e.png" width="100%"></kbd></p>

> [!NOTE]
> QUay lại thử lại với BYTE buffer[512]

> [!NOTE]
> uint8_t buffer[512]: Tạo array chứa 512 uint8_t. 
>
> Thì khi gọi lệnh này máy tính sẽ tìm 512 byte (uint8_t là 8 bit
> chứa số dương) và return về buffer cái address của cái byte
> đầu tiên
>
> Khi gọi fread(buffer, 1, 512, file), máy tính sẽ đọc file, theo từng
> bộ 512 element mỗi element là 1 byte. Và load vào memory 
> có address là buffer từ byte đầu đến byte 512 chuẩn bị sẵn

<br>

<a id="node-1547"></a>

<p align="center"><kbd><img src="assets/c2e796302e877aa5ccdc0a3334547f958299f121.png" width="100%"></kbd></p>

> [!NOTE]
> read từng cụm 512 bộ (element) mỗi bộ 1
> bytes để bỏ vào buffer là array chứa 512
> uint8_t
>
> Nó hơi khác với vụ đọc 1 bộ (element), có
> 44 bytes ở bài toán volume.

<br>

<a id="node-1548"></a>

<p align="center"><kbd><img src="assets/8cd49c74c3457ce45064d6c2816f408f3480fba3.png" width="100%"></kbd></p>

> [!NOTE]
> Xong hết nhớ đóng cả file
> input (file) và img
>
> Gọi malloc thì phải free cái filename

<br>

<a id="node-1549"></a>

<p align="center"><kbd><img src="assets/bc057642a3889013dd9119004b14b3b31bdf6744.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại làm cái vụ trim sau. Tạm thời
> có thể check byte[3] kiểu này

<br>


<a id="node-1550"></a>
## Ps: Reverse

<br>

<a id="node-1551"></a>

<p align="center"><kbd><img src="assets/bb6517e9690e2ce73ab652d87277ae8d88389247.png" width="100%"></kbd></p>

<br>

<a id="node-1552"></a>

<p align="center"><kbd><img src="assets/36d22b3076a8561798575664442bf0d7966554c4.png" width="100%"></kbd></p>

> [!NOTE]
> Yeah, header nếu chỉ define là WAVHEADER header
>
> Thì máy tính cơ bản chỉ là tạo 1 **pointer** (8 bytes)
> cho header nhưng chưa có vùng memory nào để
> chứa 44 bytes của WAVHEADER cả.
>
> Phải malloc(44)
>
> Và khi gọi check_format phải *header vì để pass vào
> VALUE / là vùng 44 bytes chứa thông tin header, 
> bằng cách ĐI VÀO ADDRESS mà header đang giữ
> chứ bản thân header chỉ là một pointer variable được 
> cho 8 byte để mang giá trị của cái ADDRESS thôi

<br>

<a id="node-1553"></a>

<p align="center"><kbd><img src="assets/a06a96d89408426f8ba31b916088459f5e3f08e5.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a06a96d89408426f8ba31b916088459f5e3f08e5.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7aaa4bd6df3ab76975f83ef104266ed9c43a6394.png" width="100%"></kbd></p>

> [!NOTE]
> Đã check cách 2, vẫn đúng:
>
> Nếu mình define kiểu header là array như  này: 
>
> WAVHEADER header[1]
>
> Thì ngay lập tức máy tính sẽ tạo vùng 44 byte (vì WAVHEADER 
> struct cần size 44 byte) và assign **ADDRESS** của byte đầu cho 
> header, khi đó khỏi cần malloc. 
>
> Khi đó pass vào check_format sẽ đơn giản là header[0]
> vì header[0] đã **CHỈ TỚI** giá trị của vùng memory 44 byte
> chứa WAVHEADER

<br>

<a id="node-1554"></a>

<p align="center"><kbd><img src="assets/b3dfc4eac7eac06a21e4d329cb3079e8edc7983e.png" width="100%"></kbd></p>

<br>

<a id="node-1555"></a>

<p align="center"><kbd><img src="assets/2cff47c7e1efa5f08b6c45bbd1328eea055219f2.png" width="100%"></kbd></p>

<br>

<a id="node-1556"></a>

<p align="center"><kbd><img src="assets/eca442f8b9fb089e15e9ca71fcbfcd856c837c59.png" width="100%"></kbd></p>

> [!NOTE]
> BYTE buffer[block] -> máy tính tạo vùng memory 4 (block)
> bytes  và assign address byte đầu cho buffer.
>
> fread(buffer,...) sẽ load data vào vùng 4 byte này với address
> của byte đầu là chứa trong buffer bởi. Nhắc lại không thừa
> buffer sẽ là pointer var được cho 8 bytes bộ nhớ.
>
> ====
>
> Việc fread(buffer, 1, block, ..) hay fread(buffer, block, 1...) cũng
> như nhau.
>
> ====
>
> Chỉ chú ý 1 chỗ là khi chuyển pointer về cuối file input thì
> phải lùi về 1 block cho lần read & write đầu tiên.
>
> ====
>
> Còn các function fseek cũng dễ hiểu, chỉ là giúp move pointer
> của file tới vị trí nào đó đọc doc là hiểu
>
> ftell thì giúp tell cái vị trí pointer hiện tại. 
>
> Thì ban đầu nó = 0, tức con trỏ ở byte thứ 0 (byte đầu tiên)
> mỗi khi lệnh fread( ..,size in bytes of element, no.element,...)
> thì pointer nó move đi (size of element* no.element), ví dụ
> từ 0, fread(..,1,4,..) thì nó nghĩa là nó read 4 byte, vậy sau
> khi read, pointer sẽ ở byte thứ 0 + 4 = 5

<br>


<a id="node-1557"></a>
## Practice (không Bắt Buộc)

<br>


<a id="node-1558"></a>
### Bottom Up

> [!NOTE]
> LÀM SAU

<br>


<a id="node-1559"></a>
### License

> [!NOTE]
> LÀM SAU

<br>


<a id="node-1560"></a>
## PS: FILTER I + II (II chỉ có thêm Edge)

> [!NOTE]
> Quay lại sau để Note & Giải thích

<br>

<a id="node-1561"></a>

<p align="center"><kbd><img src="assets/851b650bd10f6e0bf4ebb16553e977fc37ff6396.png" width="100%"></kbd></p>

<br>

<a id="node-1562"></a>

<p align="center"><kbd><img src="assets/81aa4581b6acdb1ffcc01938ae1f7ff4c3c13cf2.png" width="100%"></kbd></p>

<br>

<a id="node-1563"></a>

<p align="center"><kbd><img src="assets/957faf283bdee6aece6aee269ce50e52938c584a.png" width="100%"></kbd></p>

<br>

<a id="node-1564"></a>

<p align="center"><kbd><img src="assets/9b250b3b346006e98320b54a46c55dbe6569b12b.png" width="100%"></kbd></p>

<br>

<a id="node-1565"></a>

<p align="center"><kbd><img src="assets/c67884eb67b9e54ca8a6204f31c137581150e689.png" width="100%"></kbd></p>

<br>

<a id="node-1566"></a>

<p align="center"><kbd><img src="assets/ea5ed3ebf0a3bfb31a279ffdd508003b4030c826.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ea5ed3ebf0a3bfb31a279ffdd508003b4030c826.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b2fa5c0594f87fcb3480c696a499ea73aeb03471.png" width="100%"></kbd></p>

<br>

<a id="node-1567"></a>

<p align="center"><kbd><img src="assets/816ae2ea34c8f458a626397a4d45886203b129ab.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là mọi file đều chỉ là chuỗi 0101 binary. Hay
> Cũng là chuỗi các 8 bít = 1 bytes
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

<a id="node-1568"></a>

<p align="center"><kbd><img src="assets/2b39f99efdfad0a9d2d41f31df372dc118d89e44.png" width="100%"></kbd></p>

<br>

<a id="node-1569"></a>

<p align="center"><kbd><img src="assets/5969b87f15f134ee80595a280bd358ebbd06a1be.png" width="100%"></kbd></p>

> [!NOTE]
> Cái này thì chính là convol operation. Hai
> matrix Gx, Gy chính là là hai filter
>
> Như ta đã biết, khi nhân filter 3x3 với matrix 3x3
> của image (trên một channel Red/Green/Blue)
> thì nếu...

<br>

<a id="node-1570"></a>

<p align="center"><kbd><img src="assets/acce868464aa6b4211a2dff465e6b92e950574b5.png" width="100%"></kbd></p>

<br>

<a id="node-1571"></a>

<p align="center"><kbd><img src="assets/2512d8b89541826633356c62b9377d2ddff875d7.png" width="100%"></kbd></p>

<br>

<a id="node-1572"></a>

<p align="center"><kbd><img src="assets/14253931dcb58662aef50dff43379cc444e2815c.png" width="100%"></kbd></p>

<br>

<a id="node-1573"></a>

<p align="center"><kbd><img src="assets/1f07faea2fdf613c956e1c9589767849297bb2e2.png" width="100%"></kbd></p>

<br>

<a id="node-1574"></a>

<p align="center"><kbd><img src="assets/eb4cf0ab302242e789bfabd882fc5fc0d68bbffe.png" width="100%"></kbd></p>

<br>

<a id="node-1575"></a>

<p align="center"><kbd><img src="assets/d4434ac04ccdae3a29ef51331061cb0c82679eb8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d4434ac04ccdae3a29ef51331061cb0c82679eb8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4f7cc855f81f33e4646e03708d0525cd2e733be1.png" width="100%"></kbd></p>

<br>

<a id="node-1576"></a>

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

<a id="node-1577"></a>

<p align="center"><kbd><img src="assets/a94d86086b454472ed16cefab6f081ab671b8d88.png" width="100%"></kbd></p>

<br>

<a id="node-1578"></a>

<p align="center"><kbd><img src="assets/85023e7aaed9389ab7cbd39e73d7a777884e75f0.png" width="100%"></kbd></p>

<br>

<a id="node-1579"></a>

<p align="center"><kbd><img src="assets/a75778d126e3e2fa1e8e953fd3395ada6d4b6a56.png" width="100%"></kbd></p>

<br>

