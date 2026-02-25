# Day 3

📊 **Progress:** `22` Notes | `41` Screenshots

---
<a id="node-89"></a>

<p align="center"><kbd><img src="assets/00bad9336352e8ccb2f099d58acb26c8fa109f58.png" width="100%"></kbd></p>

<br>

<a id="node-90"></a>

<p align="center"><kbd><img src="assets/e0a7b2f0271580e32739852c60a75321adcb7ed6.png" width="100%"></kbd></p>

<br>

<a id="node-91"></a>

<p align="center"><kbd><img src="assets/a10a47633950cf19e6c7fd7a899578f5e54676b9.png" width="100%"></kbd></p>

<br>

<a id="node-92"></a>

<p align="center"><kbd><img src="assets/9c2ee0ea62e38b4f165d60749c19a7fbfd1b2dbb.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói về khi ta bấm icon green flag, ta đã trigger an
> event. Và nó trigger function màu xanh define để print "
> Hello, world!". Message đó là input, hay argument,
> parameters của function

<br>

<a id="node-93"></a>

<p align="center"><kbd><img src="assets/293b3a2fe0dacec4faffd7937267207193d02706.png" width="100%"></kbd></p>

<br>

<a id="node-94"></a>

<p align="center"><kbd><img src="assets/6c764132e59ae63f0661b9fbe6214f1e4fd01b96.png" width="100%"></kbd></p>

> [!NOTE]
> **Input** là **'Hello, world'** là **argument/parameter** của function
>
> **Algorithm** là những gì Scratch **xử lý bên dưới khi thực hiện
> function say() này**
> Output trong trường hợp này gọi là**'side effect'** - **something
> mình thấy, nghe ...**

<br>

<a id="node-95"></a>

<p align="center"><kbd><img src="assets/d06a5b70be6928cbdf064bbc89c47a0ae6f52d7f.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng làm vậy, để giới thiệu khái niệm **'return value'** của
> function. Tuy nhiên ổng hỏi tại sao khi run nó chỉ in ra 'David'
> - là cái tên được nhập sau câu hỏi.
>
> -> Rõ ràng ở trình của mình ta hiểu bởi 'hello,' vẫn được  in
> nhưng đã bị thay bởi 'David' tức thì nên ta không thấy

<br>

<a id="node-96"></a>

<p align="center"><kbd><img src="assets/c9e6224b1d02feccd0182a2a9014eb62fcc77234.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng khắc phục bằng cái này,
> nhưng rõ ràng rất stupid khi say '
> Hello'...rồi 2 giây sau 'David'

<br>

<a id="node-97"></a>

<p align="center"><kbd><img src="assets/b0c1782d9c6f7a6dc8a9ff87766eee09bff388c2.png" width="100%"></kbd></p>

<br>

<a id="node-98"></a>

<p align="center"><kbd><img src="assets/5fb12ce04f89eae8b9d0afd0e0056b079755f4b1.png" width="100%"></kbd></p>

<br>

<a id="node-99"></a>

<p align="center"><kbd><img src="assets/4cff199f57b776147b8802a2dd0ee65c7b096fa6.png" width="100%"></kbd></p>

> [!NOTE]
> Xịn xò hơn, dùng text to
> speech để say "hello, David"

<br>

<a id="node-100"></a>

<p align="center"><kbd><img src="assets/988116333839056728eab0d21bac3cd5ec78db88.png" width="100%"></kbd></p>

<br>

<a id="node-101"></a>

<p align="center"><kbd><img src="assets/74ca8eee30626d450508701ee60d6bc3b173ce0e.png" width="100%"></kbd></p>

<br>

<a id="node-102"></a>

<p align="center"><kbd><img src="assets/2203178e7aedde8fd2585b1dfc5d3fef7f37f54e.png" width="100%"></kbd></p>

> [!NOTE]
> Ý ổng là sắp nói về cách để dùng **loop**. Với yêu cầu **cho
> con mèo kêu 3 lần**, cách nhau chút xíu thì như vầy là đúng.
> Nhưng về**design thì nó không phải là tốt nhất.**Vì giả sử
> muốn đổi thời gian đợi thành 2 giây ta phải sửa từng cái....từ
> đó mất thời gian và sinh ra bug

<br>

<a id="node-103"></a>

<p align="center"><kbd><img src="assets/305d2b251a1885d6e5057f87ba06a94b9d543f9d.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi là nên làm thế nào cho tốt hơn? ->
> Tự trả lời: Theo mình có lẽ là dùng for loop,
> số lần loop là số lần mèo kêu nhận từ argument,
> Trong loop gọi function mèo kêu và wait'

<br>

<a id="node-104"></a>

<p align="center"><kbd><img src="assets/8eba130de7ca6544b390c489fbe03e6f2831f959.png" width="100%"></kbd></p>

> [!NOTE]
> Với for loop (repeat block) như thế này, ta đã
> improve code khi bây giờ nếu muốn thay đổi số lần
> mèo kêu, ..ta chỉ change 1 chỗ

<br>

<a id="node-105"></a>

<p align="center"><kbd><img src="assets/e56bcf9d5463daffb1b00b7db1cf817b9a2926dc.png" width="100%"></kbd></p>

<br>

<a id="node-106"></a>

<p align="center"><kbd><img src="assets/49ebe9ae301513e4c8a997c438acdc99712d6347.png" width="100%"></kbd></p>

<br>

<a id="node-107"></a>

<p align="center"><kbd><img src="assets/64b6b89f19d29637b76e6290d694257a991d3a96.png" width="100%"></kbd></p>

<br>

<a id="node-108"></a>

<p align="center"><kbd><img src="assets/19cbfd83c4f33db3710a399b52efc90c7c1d8cf5.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với việc **define function 'meow'** của mình
> (**custom function**) ta có thể có đoạn code **more readable,**
> Và giả sử cần thay đổi gì ta **chỉ thay đổi trong function
> meow thôi** chứ k**hông cần thay đổi nhiều nơi có sử dụng
> hành động mèo kêu này**

<br>

<a id="node-109"></a>

<p align="center"><kbd><img src="assets/44d6c8ac8ac6d1d4e733fa6ed5bed6f6ced1cee9.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là sửa lại function meow chút xíu sao
> cho có thêm input (argument) , đặt là n, và add
> label cho argument là 'times'

<br>

<a id="node-110"></a>

<p align="center"><kbd><img src="assets/3f635520f218095e60df6fbb17080212cc434d4e.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng move cái loop vào trong
> function meow luôn, sử dụng argument times
> -n của meow làm số lần repeat.

<br>

<a id="node-111"></a>

<p align="center"><kbd><img src="assets/79a341d3c44801d3ba936548b62ddac4009d2ecc.png" width="100%"></kbd></p>

> [!NOTE]
> Với việc đó, đoạn code ta
> much more readable :Click
> green flag, meo 3 times

<br>

<a id="node-112"></a>

<p align="center"><kbd><img src="assets/29827b069e9529357e1375feb344b6d4ad0484ff.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng muốn khi ổng move con chuột tới hình con mèo
> thì nó kêu. Nhưng đoạn code này không work, tại
> sao?
>
> -> Rõ ràng là khi ông click, nó đã run cái conditional ở
> dưới và lúc này con chuột đương nhiên đang ở  cái
> green flag nên condition fail nên nó không gọi đoạn
> code bên trong. Tới đây thì nó đã 'xong'
>
> Nên khi ổng rê tới cái hình con mèo thì còn gì nữa
> đâu mà khóc với sầu.
>
> Muốn làm như ổng nói thì phải có cái gọi là **event listener**

<br>

<a id="node-113"></a>

<p align="center"><kbd><img src="assets/c8d00ce198fc02f52a2870b1d80aa1b37767ab66.png" width="100%"></kbd></p>

> [!NOTE]
> Một cách ở làm ở đây là dùng
> forever loop - nó sẽ liên tục
> check cái condition này

<br>

<a id="node-114"></a>

<p align="center"><kbd><img src="assets/ec42eef17f996444db209de40e7b4f8e9a05d9c5.png" width="100%"></kbd></p>

> [!NOTE]
> Xong ổng dùng cái 'when video motion' của video
> add-on gì đó để detect event camera phát hiện motion
> lớn hơn mức nào đó (argument) thì phát tiếng mèo kêu

<br>

<a id="node-115"></a>

<p align="center"><kbd><img src="assets/d2232907266da2fd01ae7fa1f18f5d7d8e769d68.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d2232907266da2fd01ae7fa1f18f5d7d8e769d68.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1d54c5600af461255f52a5a579ca77865346c585.png" width="100%"></kbd></p>

> [!NOTE]
> Ý là với Scratch ta có thể build game, app như game này.
> Nhớ lại hồi xưa mình cũng đã từng làm cả một cái app học
> tiếng Anh với nhiều tính năng với App Inventor - một cái
> tương tự như Scratch này.

<br>

<a id="node-116"></a>

<p align="center"><kbd><img src="assets/d6482e4c571d239ecb75f25828dd90d977f3f492.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d6482e4c571d239ecb75f25828dd90d977f3f492.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e6aa5f9337e9a9b7543490dc3354ba6efa34a19f.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp ổng nói về cái game do ổng viết hồi xưa, trong đó
> rác rời xuống và mình phải kéo nó vào thùng rác. Hình
> như còn có vụ nội dung bài hát sẽ báo trước số lượng
> rác xắp rơi xuống nữa

<br>

<a id="node-117"></a>

<p align="center"><kbd><img src="assets/703f6d99fec11f19a86e9f50477daa98f5ae2f60.png" width="100%"></kbd></p>

<br>

<a id="node-118"></a>

<p align="center"><kbd><img src="assets/b4150b26fe83769521e48f39e3b9add25eeec273.png" width="100%"></kbd></p>

> [!NOTE]
> Ý ổng nói đến một ý quan trọng đó là: Kiểu như **ở high level**, khi ta
> **rê chuột tới cái thùng rác người ta thấy nó 'Mở ra'**, nhưng **thực
> tế 'ở dưới code'** chỉ là **thay đổi cái hình của cái sprite thành hình
> khác.**Và nếu làm siêng hơn, cho nó thay đổi thành nhiều hình liên tục
> thay vì chỉ có 2 hình thì nó sẽ tạo hiệu ứng thị giác là cái thùng mở
> nắp

<br>

<a id="node-119"></a>

<p align="center"><kbd><img src="assets/8ba54da7cd666a74c433025f75f76367847e877b.png" width="100%"></kbd></p>

> [!NOTE]
> Theo mô típ Input -> Algorithm -> Output

<br>

<a id="node-120"></a>

<p align="center"><kbd><img src="assets/793bc0ee1a1c4dbdadddab6e5093f990edd789b0.png" width="100%"></kbd></p>

<br>

<a id="node-121"></a>

<p align="center"><kbd><img src="assets/d414033da27aad417dcaeb7af511e21d55cab3e6.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng hỏi là làm sao để cái này nó
> di chuyển theo key: Trả lời, có cái
> forever loop listen to key

<br>

<a id="node-122"></a>

<p align="center"><kbd><img src="assets/563cda53e4e1722c5bfaa5cc7ab4bf75ed4701c1.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây ổng hỏi Y nó làm gì: Nhìn biết liền, khi click green flag,
> về giữa, quay 90 độ rồi với forever loop, nó sẽ move 1 step có
> vẻ như là nó sẽ di chuyển 1 ở phương direction tức sau khi
> quay 90 độ là phương ngang, nếu đụng bức tường thì nó quay
> 180 độ. Có nghĩa là chữ Y (là 1 sprite) sẽ chạy qua chạy lại
> giữa 2 bức tường.

<br>

<a id="node-123"></a>

<p align="center"><kbd><img src="assets/8455943ca2bb5cadea30d3608174dd3a753040c7.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp hỏi cái này làm gì: Thì dễ thấy khi click cái cờ thì
> cái MIT (đây là code của cái MIT sprite) được assign một
> random position, sau đó với forever loop, nó hướng tới
> cái Harvard sprite và move 1 step. Tức là nó luôn dí theo cái
> Harvard sprite

<br>

<a id="node-124"></a>

<p align="center"><kbd><img src="assets/f355536264edc0f58742c84827f366f41d54dc20.png" width="100%"></kbd></p>

<br>

<a id="node-125"></a>

<p align="center"><kbd><img src="assets/c71bc21490160674aa82743ba81c3399b4bc4f69.png" width="100%"></kbd></p>

<br>

