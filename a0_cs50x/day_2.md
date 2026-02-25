# Day 2

📊 **Progress:** `42` Notes | `54` Screenshots

---
<a id="node-34"></a>

<p align="center"><kbd><img src="assets/557625a1065e611741167e091e8ca72ff4af450f.png" width="100%"></kbd></p>

> [!NOTE]
> Nên đôi khi thấy lỗi khi load emoji đơn giản là
> do phone chưa update để nhận font mới nhất

<br>

<a id="node-35"></a>

<p align="center"><kbd><img src="assets/be2b5db293d5d78fcebf0b260e9c047110f937c2.png" width="100%"></kbd></p>

<br>

<a id="node-36"></a>

<p align="center"><kbd><img src="assets/055f82a332f89a8064cbc39cc0956686b39eaa71.png" width="100%"></kbd></p>

> [!NOTE]
> Ý là các công ty hiện nay cho phép tuỳ
> chỉnh color của icon (skin tone...)

<br>

<a id="node-37"></a>

<p align="center"><kbd><img src="assets/e64b2dc256bedf843710040b43537cef6c927112.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi là **làm sao các company cho
> phép tuỳ chỉnh màu sắc của các emoji với
> các skin tone khác nhau?**

<br>

<a id="node-38"></a>

<p align="center"><kbd><img src="assets/da650d6e4600034be737a7b03c84aed1f94fdb4a.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói có thể ta**làm mỗi icon với
> một skin tone cụ thể một mã hoá binary
> riêng biệt**. 5 cái skin tone thì thành ra 5
> cái chuỗi binary khác nhau. Nhưng rõ
> ràng làm vậy **không hiệu quả lắm** khi
> các icon **chỉ khác nhau chút xíu ở skin
> tone** mà **phải sử dụng nhiều bit hơn**

<br>

<a id="node-39"></a>

<p align="center"><kbd><img src="assets/5782d400c13620be8a3981e2d52492750f3e956d.png" width="100%"></kbd></p>

> [!NOTE]
> 1 bà nói về RGB

<br>

<a id="node-40"></a>

<p align="center"><kbd><img src="assets/47a3bcf536f4e92df5f0bb823d22bb50f3ae3f54.png" width="100%"></kbd></p>

<br>

<a id="node-41"></a>

<p align="center"><kbd><img src="assets/8b6931f57117220cf984ee5dc35e6cf66ce577a2.png" width="100%"></kbd></p>

> [!NOTE]
> Một ý kiến khác là store 1 copy
> của emoji và store nhiều variants
> của colors khác nhau

<br>

<a id="node-42"></a>

<p align="center"><kbd><img src="assets/2e006b0e1f40f257117f16028970512eead39a9a.png" width="100%"></kbd></p>

> [!NOTE]
> Một ý kiến khác cho rằng
> 'filter' là giải pháp

<br>

<a id="node-43"></a>

<p align="center"><kbd><img src="assets/847d746b4836a1bed4c402295a59ac30b474d9b2.png" width="100%"></kbd></p>

> [!NOTE]
> Một ý kiến nữa là 5 skin tone
> là 5 font khác nhau

<br>

<a id="node-44"></a>

<p align="center"><kbd><img src="assets/4cf69d83e87674b80280122a403dbf44a6a65dff.png" width="100%"></kbd></p>

> [!NOTE]
> Bite đầu tiên để represent cấu trúc của emoji - tức là
> chuỗi binary represent emoji với màu default - vàng
> (sau khi chuyển sang decimal, tra cứu bảng
> unicode)

<br>

<a id="node-45"></a>

<p align="center"><kbd><img src="assets/174442b0bf8d1c6d111b8acc2ce1ffb7534ab140.png" width="100%"></kbd></p>

> [!NOTE]
> Và sau đó là **byte thứ 2** - "a certain pattern of bit" thứ hai
> sẽ là kiểu như quy ước (human standardize) để represent
> các different shades of skin tones

<br>

<a id="node-46"></a>

<p align="center"><kbd><img src="assets/cbb8068c4517aeeae93318800fa95fa40843480c.png" width="100%"></kbd></p>

> [!NOTE]
> Thì như vậy**chỉ dùng x2 số bit cần thiết** thay vì phải **x5**
> cho**5 cái different pattern cho 5 cái emoji với skin tone
> khác nhau**

<br>

<a id="node-47"></a>

<p align="center"><kbd><img src="assets/2a32e53a287766da179a53a5bf3812d0e3c51bab.png" width="100%"></kbd></p>

<br>

<a id="node-48"></a>

<p align="center"><kbd><img src="assets/3dc998fba21abd0964b7ac833854ac0644ea28c5.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là người ta chỉ tạo binary bits cho mỗi cái hình trong emoji này, rồi
> combine lại để thành emoji hoàn chỉnh. Với cách này, người ta **ko cần phải
> define cụ thể từng cái emoji** (với 2 man yêu nhau, 2 woman yêu nhau, rồi tùm
> lùm các case cụ thể mà không thể nào 'làm trước' được)...mà chỉ việc**ghép
> các ...tạm gọi là các emoji đơn lẻ - tất nhiên là ở dạng binary - lại**

<br>

<a id="node-49"></a>

<p align="center"><kbd><img src="assets/9b39d596f663cedab4467b4ee2a4403e699c0c5b.png" width="100%"></kbd></p>

<br>

<a id="node-50"></a>

<p align="center"><kbd><img src="assets/05a14b9eb1d1643da074d017ae5c38cde4ddef89.png" width="100%"></kbd></p>

> [!NOTE]
> Tới đây ổng nói vì **người ta không tính trước** (ví
> dụ như ASCII - chỉ chứa American centric
> character để rồi sau này phải tạo ra Unicode) nên
> mới có khái niệm **version**

<br>

<a id="node-51"></a>

<p align="center"><kbd><img src="assets/966d6ba0be378a16760043365743b6aa90a128f7.png" width="100%"></kbd></p>

> [!NOTE]
> Qua tuần sau khi học về C, ta sẽ biết với vai trò là developer ta
> phải cho máy tính biết cái gì là text cái gì là number ...Đó chính là
> **data type**Và sau này với các language như Python, nó sẽ tự dựa vào
> context mà biết được data type phù hợp, rất tiện lợi cho human

<br>

<a id="node-52"></a>

<p align="center"><kbd><img src="assets/a02c45be29d6671b3f499d6060b1a4475e599bc6.png" width="100%"></kbd></p>

<br>

<a id="node-53"></a>

<p align="center"><kbd><img src="assets/9825c7209ed61659a645d24754b6d385383b2ee0.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây ổng nói nếu là messenger nó sẽ hiểu 72
> 73 33 là hi! thì với Photoshop chẳng hạn nó sẽ
> hiểu là 3 giá trị của R,G,B.

<br>

<a id="node-54"></a>

<p align="center"><kbd><img src="assets/c8d4ae2cef0a4562c580dce7edf460bddc243096.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây tự nhiên hiểu tại sao giá trị của pixel có
> range từ 0 -**255**: 255 chính là các **số có thể được
> represented bởi 1 byte = 8 bit.**

<br>

<a id="node-55"></a>

<p align="center"><kbd><img src="assets/584855e7eb4eaf5ecab46005342677b79d624843.png" width="100%"></kbd></p>

> [!NOTE]
> Thì 72 73 33 chính
> là cái màu này

<br>

<a id="node-56"></a>

<p align="center"><kbd><img src="assets/6229bde4659f6741ec424628c4854f8384970e32.png" width="100%"></kbd></p>

> [!NOTE]
> Và như vậy **mỗi pixel** sẽ được represent bởi **3 bytes:** 1
> byte = 8 bit cho Red, 1 byte = 8 bit cho Green, 1 byte = 8 bit
> cho Blue

<br>

<a id="node-57"></a>

<p align="center"><kbd><img src="assets/6b2c9a75f798e8dff609bcc6894e69c0c5a7d4d7.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy video thì sao ?

<br>

<a id="node-58"></a>

<p align="center"><kbd><img src="assets/ac740143ead3839c3f51665ae86ea95fb459cf65.png" width="100%"></kbd></p>

> [!NOTE]
> Cơ bản là các image thay đổi liên tục
> thôi: 24 images / second

<br>

<a id="node-59"></a>

<p align="center"><kbd><img src="assets/1a96210829eb78fe2fdd21cdd7817cf6415c99a3.png" width="100%"></kbd></p>

<br>

<a id="node-60"></a>

<p align="center"><kbd><img src="assets/234ae4cbb8d92b717309f615118c86250ae495c7.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là người ta represent number là **chỉ số Hezt - tần số cao độ
> (nốt cao hay nốt trầm)**. Có thể **dùng thêm byte khác** represent
> **cường độ (to hay nhỏ)**. Có thể **dùng thêm byte nữa** represent ..kiểu
> như **thời gian bấm 1 nốt nhạc lâu hay nhanh**...Từ đó ra các định
> dạng **MIDI, mp3**...tất cả **đều là các cách represent khác nhau của
> âm thanh.**

<br>

<a id="node-61"></a>

<p align="center"><kbd><img src="assets/eae267e3df7d3c9c86526ddecf74e92c42bc7eec.png" width="100%"></kbd></p>

> [!NOTE]
> Ý ổng là vì dụ như ta đi xe hơi ta không quan tâm
> máy nó chạy hay cấu tạo ra sao, ta chỉ quan tâm đi
> từ A-B. Đó gọi là abstraction

<br>

<a id="node-62"></a>

<p align="center"><kbd><img src="assets/0bca821538d8f30f395a95641405e108369f1065.png" width="100%"></kbd></p>

> [!NOTE]
> Vì như vậy sẽ rất chậm khi phải care mọi
> thứ behide , ta chỉ think và operate ở
> high level of abstraction

<br>

<a id="node-63"></a>

<p align="center"><kbd><img src="assets/9bd99631e3ec7db6f047a263bc535b7b0ce13ea9.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy cho đến nay, có gì trong blackbox này (ý là để
> rồi giúp ta với **input** là **binary** và **output cho ra text,
> số, image, video, music....)**

<br>

<a id="node-64"></a>

<p align="center"><kbd><img src="assets/f02cace2a25feb8b6769b33687fd0c83aa9ceaad.png" width="100%"></kbd></p>

<br>

<a id="node-65"></a>

<p align="center"><kbd><img src="assets/0d7817b496767e854dc75fb83b24eb521eaca0b2.png" width="100%"></kbd></p>

<br>

<a id="node-66"></a>

<p align="center"><kbd><img src="assets/8ba84add6256ac6a3ad218f4895c1b6e403507e4.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng lấy ví dụ, search trong phone book app,
> **"HI"**, lập tức **autocomplete** suggest các name
> start với HI. Câu hỏi là **nó hoạt động như thế
> nào?**

<br>

<a id="node-67"></a>

<p align="center"><kbd><img src="assets/7f6da265ba7de762b3f23a12ad55ccf22986d71f.png" width="100%"></kbd></p>

> [!NOTE]
> Thì một cách là**loop từ đầu đến cuối, thằng nào có tên
> bắt đầu với H, A thì 'lấy'**. Nhưng rõ ràng làm vậy không
> ổn, sẽ **rất chậm** khi list name lớn

<br>

<a id="node-68"></a>

<p align="center"><kbd><img src="assets/aca336b7f692c9b389d90bfdc1939efc95e1d20b.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ổng nói, ví dụ ổng tìm ông có tên là Harvard trong
> cuốn name record này, bằng cách lật từng trang từ đầu
> đến cuối. Thì nó vẫn là algorithm đúng vì một lúc nào đó
> ổng sẽ tìm thấy tên ổng cần. Dù việc này rất chậm
> nhưng vẫn đúng.

<br>

<a id="node-69"></a>

<p align="center"><kbd><img src="assets/a04b6047e7e3a1b334d774b27e8ead3899b47202.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi ổng giả sử lật 2 trang một, thì rõ
> ràng algorithm này sai, vì ổng có thể
> skip cái tên ổng cần.

<br>

<a id="node-70"></a>

<p align="center"><kbd><img src="assets/946851a9b5469bbb76e6b437fa80e539429ee0b7.png" width="100%"></kbd></p>

> [!NOTE]
> Thì trong thực tế we **human** sẽ làm là **lật bừa ra xem
> thử trúng chữ gì** ví dụ **M**. Từ đó **xác định được cái
> tên John Harvard cần tìm nằm ở phần bên nào.**Với việc xác định vì H nó trước chữ M nên suy ra nó
> nằm ở phần đầu,  từ đó ổng xé bỏ phần sau chỉ giữ lại
> phần đầu

<br>

<a id="node-71"></a>

<p align="center"><kbd><img src="assets/12d1377853fefffb18e7c7f2b93d83ec4dec999c.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi tiếp tục như vậy
> again and again,...

<br>

<a id="node-72"></a>

<p align="center"><kbd><img src="assets/6478d376d7c0b17dbbf883167ad742daf161cb9b.png" width="100%"></kbd></p>

> [!NOTE]
> Cuối cùng ổng come up with 1 page cần tìm.

<br>

<a id="node-73"></a>

<p align="center"><kbd><img src="assets/9d6143409d7ca6508a38a0ebb4579034d6cbe4ed.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về thể hiện đồ thị giữa số lần phải thực hiện
> (ví dụ lật trang để tìm tên trong phone book) và số
> lương tên trong phone book
>
> Ví dụ phải tìm cái tên thứ n trong phone book có
>  có n cái tên (size of problem = n)

<br>

<a id="node-74"></a>

<p align="center"><kbd><img src="assets/b0ad87ed9a3ea942a0ef4aeae934c4b6a07acee7.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ở đây, ổng nói nếu làm theo cách cũ (lật từng
> trang) thì số lần phải thực hiện (phép tính) là n (ví dụ
> có n cái tên trong phone book và cần tìm cái tên thứ
> n)
>
> Nếu làm theo cách lật 1 lúc 2 trang như cách sau, thì
> số lần  phải thực hiện chỉ còn n/2 (tuy nhiên như đã
> biết algorithm này không đúng)

<br>

<a id="node-75"></a>

<p align="center"><kbd><img src="assets/cf14b723be8f400b5f6c29cb9850414f37096cdb.png" width="100%"></kbd></p>

> [!NOTE]
> Thì ý là với một algorithm mà "**chia nửa rồi xé"** rất
> hiệu quả thể hiện trên biểu đồ màu vàng log2(m).
>
> Cho thấy **dù số lượng name trong phone có tăng
> nhiều thì số phép tính phải làm không tăng bao nhiêu.**Bởi vì dù **số lượng cái tên có x2**thì cũng **chỉ tốn
> thêm 1 lần chia**

<br>

<a id="node-76"></a>

<p align="center"><kbd><img src="assets/a769d7c9ab923ef5844c81f64061d38231916c0f.png" width="100%"></kbd></p>

> [!NOTE]
> Nếu database nhỏ thì không nói làm gì, có thể cứ search từ
> trên xuống mà tìm như cách 1. Nhưng nếu database cỡ
> Google thì algorithm rất quan trọng.

<br>

<a id="node-77"></a>

<p align="center"><kbd><img src="assets/ff1193d978f09e45fc75bb35ede6e2cca172b3ac.png" width="100%"></kbd></p>

<br>

<a id="node-78"></a>

<p align="center"><kbd><img src="assets/219d305bdd4a4ca658997dc654546d51a8d7ebf6.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là mô tả cách làm
> bằng human language

<br>

<a id="node-79"></a>

<p align="center"><kbd><img src="assets/19e6072b5575ec21d5cd0469959cc8c7cd00fa25.png" width="100%"></kbd></p>

> [!NOTE]
> Verb in pseudocode (màu vàng) = **function**

<br>

<a id="node-80"></a>

<p align="center"><kbd><img src="assets/6f88b45c337929942fd597b1e1da1607cfae6ac5.png" width="100%"></kbd></p>

> [!NOTE]
> Condition

<br>

<a id="node-81"></a>

<p align="center"><kbd><img src="assets/694cbbd0202fe2c90ca80a3936af37e83cb0bed3.png" width="100%"></kbd></p>

> [!NOTE]
> Boolean expression

<br>

<a id="node-82"></a>

<p align="center"><kbd><img src="assets/a56b745748fcd48e78627669e6930a9dad86b8bd.png" width="100%"></kbd></p>

> [!NOTE]
> Loop

<br>

<a id="node-83"></a>

<p align="center"><kbd><img src="assets/a195156eb827299d962fec126e8a47f0c4b56800.png" width="100%"></kbd></p>

> [!NOTE]
> Ý ổng nói the key để nó không chạy quài và mắc kẹt là
> bởi 1 là nó sẽ tìm được cái tên cần tìm hai là không có
> và nó reach keyword "Quit"

<br>

<a id="node-84"></a>

<p align="center"><kbd><img src="assets/3aeff98ccb5be1b89923fa5450c9683c3b429516.png" width="100%"></kbd></p>

<br>

<a id="node-85"></a>

<p align="center"><kbd><img src="assets/39400f1ccb158ebe6f3a2b54e949e6c9c012a363.png" width="100%"></kbd></p>

> [!NOTE]
> Hello world!

<br>

<a id="node-86"></a>

<p align="center"><kbd><img src="assets/9c8707f83298fd6f6bd2dcd48b3b8f5a41c5575f.png" width="100%"></kbd></p>

<br>

<a id="node-87"></a>

<p align="center"><kbd><img src="assets/44a8a8c42fe2219f667bdb58036bacf2099bb635.png" width="100%"></kbd></p>

<br>

