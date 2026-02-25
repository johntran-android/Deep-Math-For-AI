# Short

📊 **Progress:** `40` Notes | `57` Screenshots

---

<a id="node-271"></a>
## Data Type

<br>

<a id="node-272"></a>

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

<a id="node-273"></a>

<p align="center"><kbd><img src="assets/43d4709b75150b67b4dc62e7cc0323cf8066ba33.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/43d4709b75150b67b4dc62e7cc0323cf8066ba33.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6631453fbaa32144df12e63e8bacdc8dfe93329b.png" width="100%"></kbd></p>

<br>

<a id="node-274"></a>

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

<a id="node-275"></a>

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

<a id="node-276"></a>

<p align="center"><kbd><img src="assets/a99996c42e4387cf84ee2cb6471c6c2e48df8eed.png" width="100%"></kbd></p>

> [!NOTE]
> float dùng**32 bits** để represent **real number**.  Như đã nói bên **LLM**, nó
> tổ chức theo kiểu **1 bit đầu dành cho sign**,  **8 bits tiếp dành cho exponent**,
> **23 bits tiếp theo dành cho fraction.**Và vì bị giới hạn bởi chỉ có 32 bits, trong khi phần fraction - thập phân là chuỗi
> vô hạn nên float bị vấn đề **precision - tức là không thể nào represent chính xác
> tuyệt đối.**

<br>

<a id="node-277"></a>

<p align="center"><kbd><img src="assets/2363a7de2caed2c534ed71d7c1b7503b00177dc1.png" width="100%"></kbd></p>

<br>

<a id="node-278"></a>

<p align="center"><kbd><img src="assets/85bfdb7c28b8885ca3fcb2b467a5a0fb244e810b.png" width="100%"></kbd></p>

> [!NOTE]
> Double cho phép represent real number với 64 bits từ đó
> tăng phần thập phân giúp chính xác hơn

<br>

<a id="node-279"></a>

<p align="center"><kbd><img src="assets/e64ac55f274e31a70d012012c1d2efc2ee06ffc3.png" width="100%"></kbd></p>

> [!NOTE]
> Void không hẳn là datatype, nó chỉ đơn giản là báo hiệu
> function không return cái gì hoặc không nhận argument (ví dụ
> main (void)

<br>

<a id="node-280"></a>

<p align="center"><kbd><img src="assets/f6bf2ecbd9d330340c1de1f1d78c59babc51188e.png" width="100%"></kbd></p>

<br>

<a id="node-281"></a>

<p align="center"><kbd><img src="assets/c8d6309637cac48e51b063b2ea437752e71ac41e.png" width="100%"></kbd></p>

<br>

<a id="node-282"></a>

<p align="center"><kbd><img src="assets/051d8af8bee844321387a4705c095728cf2d3f61.png" width="100%"></kbd></p>

> [!NOTE]
> Những tuần sau sẽ có structs dùng typedefs để define (gần
> gần nhưng chưa phải là class trong OOP)

<br>

<a id="node-283"></a>

<p align="center"><kbd><img src="assets/b19bfa5b7d3b4ec0c0e3c16be3ff19bc21333584.png" width="100%"></kbd></p>

> [!NOTE]
> Cách define,
> tương tự java

<br>

<a id="node-284"></a>

<p align="center"><kbd><img src="assets/b96ac3b9b7491f50d1538ddeeaeb3a1ec00dc5f9.png" width="100%"></kbd></p>

<br>


<a id="node-285"></a>
## Operators

<br>


<a id="node-286"></a>
## Linux Command Line

<br>

<a id="node-287"></a>

<p align="center"><kbd><img src="assets/09cca32c4187d82ac9f9f24d0d793e129f577ca9.png" width="100%"></kbd></p>

<br>

<a id="node-288"></a>

<p align="center"><kbd><img src="assets/981289b6774a496e478f8304d48137c2ae643ff8.png" width="100%"></kbd></p>

> [!NOTE]
> ls: list current folder's items

<br>

<a id="node-289"></a>

<p align="center"><kbd><img src="assets/87a48fa58d90b21a44696638827dba8a34512fae.png" width="100%"></kbd></p>

<br>

<a id="node-290"></a>

<p align="center"><kbd><img src="assets/fdbe7b46ef7c218787977b1c33b415e2f6cdb86a.png" width="100%"></kbd></p>

> [!NOTE]
> Như đã nói, file màu xanh là
> machine code  = excutable file

<br>

<a id="node-291"></a>

<p align="center"><kbd><img src="assets/6eace858ece3284d1b00bc535703571f71f26c45.png" width="100%"></kbd></p>

> [!NOTE]
> cd: Change directory. 
> . là current directory
> .. là parent directory

<br>

<a id="node-292"></a>

<p align="center"><kbd><img src="assets/43ef1aec325bccb63498328e3d325b576ae8fdc9.png" width="100%"></kbd></p>

<br>

<a id="node-293"></a>

<p align="center"><kbd><img src="assets/07675c7c9c4eb0f7a27a03e3aeb755a50686c45a.png" width="100%"></kbd></p>

> [!NOTE]
> **cd .. :**để change directory về parent's directory
>
> **pwd = print working directory** để in ra directory path hiện tại

<br>

<a id="node-294"></a>

<p align="center"><kbd><img src="assets/ff4e62ab7e7d608c906c3c872105a29709fbd885.png" width="100%"></kbd></p>

> [!NOTE]
> muốn chuyển về ~/ luôn: cd (và nothing else)

<br>

<a id="node-295"></a>

<p align="center"><kbd><img src="assets/cabb5da59e89474b54a0aa7cf714f574c1cc1422.png" width="100%"></kbd></p>

<br>

<a id="node-296"></a>

<p align="center"><kbd><img src="assets/dd2d4b84141383455173554380084daf34c1447d.png" width="100%"></kbd></p>

<br>

<a id="node-297"></a>

<p align="center"><kbd><img src="assets/c80a5c9b9915671b1c5a183cca2d53a6eafffcd2.png" width="100%"></kbd></p>

> [!NOTE]
> ví dụ copy file **hello.txt**, paste
> với tên khác là **hi.txt**

<br>

<a id="node-298"></a>

<p align="center"><kbd><img src="assets/18dc62e0158a3b47803cd6b9a31690ee6268793b.png" width="100%"></kbd></p>

> [!NOTE]
> Trường hợp muốn copy một directory (ví dụ pset0 và
> paste với tên mới là pset3) thì nếu chỉ (đang ở
> workspace và gọi **cp pset0 pset3**) thì ổng nói Linux nó
> sẽ không hiểu mình muốn làm gì với nó.
>
> Nên phải **cp -r pset0 pset3** : Ý là bảo nó copy mọi thứ trong 
> Directory pset0 (-r có nghĩa là recursively vào trong mọi folder
> của pset0 và copy mọi thứ)

<br>

<a id="node-299"></a>

<p align="center"><kbd><img src="assets/5ec9b1e208f1774ce5399572f350a9aad2eabaa8.png" width="100%"></kbd></p>

> [!NOTE]
> rm giúp remove or
> delete file/folder.

<br>

<a id="node-300"></a>

<p align="center"><kbd><img src="assets/a9112e119db6971e3d6f0f623e3ca341c4a2e800.png" width="100%"></kbd></p>

> [!NOTE]
> rm bình thường thì nó còn
> hỏi lại có chắc không

<br>

<a id="node-301"></a>

<p align="center"><kbd><img src="assets/9ffa0d952873f83ee8531850fa81c882fa5a31d9.png" width="100%"></kbd></p>

> [!NOTE]
> **rm -f file name**
> sẽ delete ngay lập tức và
> không có cách nào undo

<br>

<a id="node-302"></a>

<p align="center"><kbd><img src="assets/f1ee05b956ce307368333053b31cebde0b2be373.png" width="100%"></kbd></p>

> [!NOTE]
> **rm -r** folder_name
>
> (again, -r có nghĩa là recursively
> - delete toàn bộ thư mục)

<br>

<a id="node-303"></a>

<p align="center"><kbd><img src="assets/5580944587e05a85e6da17cd60be674049861f9e.png" width="100%"></kbd></p>

> [!NOTE]
> và kết hợp**rm -rf**folder_name: Không có hỏi để
> confirm, nên ổng nói phải cực kì chắc chắn mới
> làm cái này, vì delete toàn bộ thư mục kiểu này là
> không có cách nào lấy lại

<br>

<a id="node-304"></a>

<p align="center"><kbd><img src="assets/db1676ce1e660872f0424c493469e40b65ea5188.png" width="100%"></kbd></p>

> [!NOTE]
> mv: move file/
> **change name**

<br>

<a id="node-305"></a>

<p align="center"><kbd><img src="assets/7f0f42e92501e6884fe6d739b6b894150ae39e37.png" width="100%"></kbd></p>

<br>

<a id="node-306"></a>

<p align="center"><kbd><img src="assets/e43b72316b8f62cff80fd85cc780842873b91ffc.png" width="100%"></kbd></p>

> [!NOTE]
> một số command line khác.

<br>


<a id="node-307"></a>
## Magic Number

<br>

<a id="node-308"></a>

<p align="center"><kbd><img src="assets/65e0f24e05f7e46676f22a4ec908e150f97ff051.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là có đôi khi ta cần sử dụng một hardcode
> value như chiều cao của kim tự tháp Mario gì đó,
> hoặc số lá của bộ bài. Thì thay vì để khơi khơi thì ý
> nói là **nên define dạng constant để dễ hiểu hơn cho
> người khác khi đọc code.**

<br>

<a id="node-309"></a>

<p align="center"><kbd><img src="assets/6be8f90c430469a98b17fa1fb40ea963ed3c5959.png" width="100%"></kbd></p>

<br>

<a id="node-310"></a>

<p align="center"><kbd><img src="assets/2c59ca6e3ce2deaed07650d14336b602ef6949c8.png" width="100%"></kbd></p>

> [!NOTE]
> Có thể như vầy, define local variable, hoặc thậm
> chí là global variable thì vẫn tiềm ẩn rủi ro là ai đó
> sẽ update và thay đổi value

<br>

<a id="node-311"></a>

<p align="center"><kbd><img src="assets/63b495723ebfb3ce9dd12cf000e63c32bea3c96b.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó trong C nó có vụ này #define gọi là pound
> define... kiểu như khi compile code, máy tính nó
> sẽ tìm và thay thế chỗ nào có NAME và replace
> với REPLACEMENT

<br>

<a id="node-312"></a>

<p align="center"><kbd><img src="assets/06c88760ff3aa529cb46ad4291c2814559d825e7.png" width="100%"></kbd></p>

> [!NOTE]
> bằng cách đó, chỗ nào cần dùng value vủa Pi = 3.
> 14.. thì ta chỉ cần dùng PI. Cái này cũng hơi giống
> như final variable của Java vậy

<br>

<a id="node-313"></a>

<p align="center"><kbd><img src="assets/581b64e60451a7db51e122a9e2fe63fc5ca95fde.png" width="100%"></kbd></p>

> [!NOTE]
> Và có thể define cho mọi datatype. Và theo
> convention thì dùng viết hoa

<br>

<a id="node-314"></a>

<p align="center"><kbd><img src="assets/0c44af830e6f1ff9188f6b5459735f6f59f25a91.png" width="100%"></kbd></p>

> [!NOTE]
> Với cách này, không sợ bị thay đổi giá trị của deck
> size. Ngoài ra một benefit nữa là giả sử deal với bộ
> bài có 32 lá như ở German thì chỉ cần đổi
> DECKSIZE=32.

<br>


<a id="node-315"></a>
## Arithmetic

> [!NOTE]
> ARITHMETIC
> OPERATORS

<br>

<a id="node-316"></a>

<p align="center"><kbd><img src="assets/03af10c3cc102540e86d4d43c755bf5033cdf7bb.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói cái **modulus operator = chia lấy phần dư**này sẽ tỏ ra hữu ích trong CS50.
>
> Ví dụ khi **lấy random number rất lớn và % cho 20**,
> thì ta sẽ **được số random từ 1-20 gì đó sẽ hữu ích
> khi cần**

<br>

<a id="node-317"></a>

<p align="center"><kbd><img src="assets/14a67cd64152788e646999c3e83d9b20727565a7.png" width="100%"></kbd></p>

> [!NOTE]
> x = x*5 có thể viết gọn là**x *= 5**
>
> x = x + 1;
> x += 1
> x++ 
> Ba cái trên y nhau

<br>

<a id="node-318"></a>

<p align="center"><kbd><img src="assets/7306cf4a2330f284e7d527d82ef24dd4bb88c25c.png" width="100%"></kbd></p>

<br>

<a id="node-319"></a>

<p align="center"><kbd><img src="assets/cf12e119129760efdb00ebd3c190d268992ac9ba.png" width="100%"></kbd></p>

> [!NOTE]
> "and" operator in C: &&

<br>

<a id="node-320"></a>

<p align="center"><kbd><img src="assets/0bdd3b566baf6263f9136bec44b4b8112d9cf527.png" width="100%"></kbd></p>

> [!NOTE]
> "or" operator in C: ||

<br>

<a id="node-321"></a>

<p align="center"><kbd><img src="assets/e66619e0c7af68f5c43edd7b55b8c26f06745458.png" width="100%"></kbd></p>

> [!NOTE]
> Này giống java

<br>

<a id="node-322"></a>

<p align="center"><kbd><img src="assets/cf42372d8b7adee27ef81388e86b5405c1f4123e.png" width="100%"></kbd></p>

> [!NOTE]
> Cơ bản không có gì

<br>

<a id="node-323"></a>

<p align="center"><kbd><img src="assets/6b2273b652d35cbe3b9ea4c3d7ff99ac5a068d69.png" width="100%"></kbd></p>

> [!NOTE]
> Cơ bản không có gì

<br>


<a id="node-324"></a>
## Loops

<br>

<a id="node-325"></a>

<p align="center"><kbd><img src="assets/a92a6018a0245b0a4ae8760f8a97b305a4451a62.png" width="100%"></kbd></p>

> [!NOTE]
> Forever loop

<br>

<a id="node-326"></a>

<p align="center"><kbd><img src="assets/ea4a298492724c06a400b8bd0dab8111e5cb6839.png" width="100%"></kbd></p>

<br>

<a id="node-327"></a>

<p align="center"><kbd><img src="assets/f9a5e2cb7cfb07de8c8174ecf01e343b4b330123.png" width="100%"></kbd></p>

> [!NOTE]
> Do while make sure code
> chạy ít nhất 1 lần

<br>

<a id="node-328"></a>

<p align="center"><kbd><img src="assets/53375c483472f149fa496652b4101a0363dde258.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/53375c483472f149fa496652b4101a0363dde258.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/312c0ff695a76106f0ff8962a1da47da30101a59.png" width="100%"></kbd></p>

> [!NOTE]
> Cơ bản không có gì

<br>

<a id="node-329"></a>

<p align="center"><kbd><img src="assets/09620064a023c6b214d3215dd7e04a81defc313b.png" width="100%"></kbd></p>

> [!NOTE]
> dùng while khi muốn repeat 1 số lần chưa biết,
> thậm chí vô hạn. Do while tương tự nhưng ít
> nhất run 1 lần. Còn for loop thì khi có 1 số nhất
> định lần muốn run

<br>


<a id="node-330"></a>
## Conditional

> [!NOTE]
> CONDITIONAL
> STATEMENTS

> [!NOTE]
> QUAY LẠI LÀM SAU

<br>

