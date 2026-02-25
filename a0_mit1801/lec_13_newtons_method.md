# Lec 13: Newton's Method

📊 **Progress:** `26` Notes | `29` Screenshots

---
<a id="node-287"></a>

<p align="center"><kbd><img src="assets/ab19ec405c057bb43f125ca8a7e6aa44b0486432.png" width="100%"></kbd></p>

> [!NOTE]
> Bài toán như vầy, các khoảng các giữa các điểm: ta, police có thể
> coi như cái cột camera đo tốc độ ví dụ vậy, và chân cột là 50, 40, 30
> Câu hỏi là dựa trên dD/dt = -80, thì ta có đang vượt quá tốc độ không
> (giới hạn là 95 ft/sec)

<br>

<a id="node-288"></a>

<p align="center"><kbd><img src="assets/c9a9c90de6d921031486c98a906b972c9b5aa3d9.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ có equation liên hệ giữa x (khoảng cách giữa ta và chân cột)
> D (khoảng cách giữa ta và police) vì tại thời điểm đang xét làm
> thành tam giác vuông (right triangle) nên ta có:
>
> x^2 + 30^2 = D^2
>
> Gs cho rằng tuy rằng ta có thể solve để có x theo D, rồi tính  đạo
> hàm, nhưng cách dễ hơn sẽ là implicit differentiation. (ý tưởng là,
> khi ta có equation ẩn chứa một function ví dụ x^2 + y^2 = c, thì ta
> thay vì solve để có dạng explicitly của function y = f(x) rồi tính đạo
> hàm của y theo x (giả sử ta cần tính), thì ta có thể implicit
> differentiation, lấy đạo hàm của equation theo x luôn, từ đó solve ra
> y'(x))
>
> Vậy lấy đạo hàm theo t của phương trình trên, vế trái trở thành
> 2x*dx/dt = 2D*dD/dt (đương nhiên là dùng chain rule)
>
> Gs lưu ý, đương nhiên ta sẽ phải để x ở dạng variable rồi mới làm
> bước lấy đạo hàm, chứ sẽ sai lầm nếu ta lại gắn giá trị tại thời điểm
> này x = 40 vào, rồi lấy đạo hàm thì sẽ sai. Lí do đương nhiên vì x là
> biến, x, và D thay đổi theo t.

<br>

<a id="node-289"></a>

<p align="center"><kbd><img src="assets/b89be17ccb55204872b582232239520701ebb221.png" width="100%"></kbd></p>

> [!NOTE]
> Sau khi đạo hàm xong, ta mới gắn giá trị x và D vào, để có
> dx/dt = -100 ft/sec, từ đó kết luận ta đang di chuyển hướng về
> với vận tốc (dx/dt chính là vận tốc) -100 ft/sec đồng nghĩa đang 
> overspeed

<br>

<a id="node-290"></a>

<p align="center"><kbd><img src="assets/123e1388a04222c7d58b3d075e883bc6444a3d3b.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ tiếp theo là cái bể nước (hình nón ngược) có bán kính top
> là 4ft, sâu 10 ft và được fill với dung lượng 2 cubic ft / min.
>
> Câu hỏi là mực nước dâng  nhanh cỡ nào khi mực nước ở mốc
> 5ft

<br>

<a id="node-291"></a>

<p align="center"><kbd><img src="assets/bc110cff18f0c1101a9812269eaac3dc5f9fd2bf.png" width="100%"></kbd></p>

> [!NOTE]
> gs cho rằng ta sẽ cần vẽ minh họa bài toán, ta sẽ thể hiện mặt
> cắt (và chỉ lấy 1/2) để thể hiện các thông số như bán kính top,
> chiều cao, chiều cao mực nước h và bán kính mực nước r
>
> Từ đó ta có equation: h/r = 10/4

<br>

<a id="node-292"></a>

<p align="center"><kbd><img src="assets/467b107360aac63daac6dd3c3a1d6969b39a8efd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/467b107360aac63daac6dd3c3a1d6969b39a8efd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/31420dcfab2b741d85ac1c07c558894d5f9cfcbe.png" width="100%"></kbd></p>

> [!NOTE]
> Và ta nhớ công thức tích thể tích bể nước V = (1/3)πr^3
>
> Và thể tích đang tăng thêm với rate là 2 cu ft / min nên ta có dV/dt = 2

<br>

<a id="node-293"></a>

<p align="center"><kbd><img src="assets/cd5e7a6c8709191602e560d021c55c6a58a41d63.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi sẽ là tìm dh/dt khi h = 5 (mực nước
> dâng nhanh ra sao khi h = 5)

<br>

<a id="node-294"></a>

<p align="center"><kbd><img src="assets/2bff23307dfa4b8237a67d0f65af7b55134c80bd.png" width="100%"></kbd></p>

> [!NOTE]
> Thế r = 2h/5 vào phương trình V và dùng implicit differentiation
> (đạo hàm hai vế theo t) ta sẽ có:
>
> Vế trái là dV/dt, và bằng 2 như vừa rồi nói vế phải đạo hàm của h^3
> theo t là 3h^2 dh/dt với các constant (1/3)*(2/5)^2

<br>

<a id="node-295"></a>

<p align="center"><kbd><img src="assets/eb628910d2012af4c84fd6300edc2ccc453eb7b3.png" width="100%"></kbd></p>

> [!NOTE]
> Rút gọn và ta có kết quả là dh/dt =
> 1/2π (ft/min) (thầy ghi sai)

<br>

<a id="node-296"></a>

<p align="center"><kbd><img src="assets/e98aee900ec924b468562568612fb54f7a499d51.png" width="100%"></kbd></p>

> [!NOTE]
> Và đây chính là ý nghĩa của Related Rate, đại khái là khi ta có các
> rate of change giữa các yếu tố liên quan, ví dụ có rate of change
> giữa thể tích và mực nước, và rate of change giữa thể tích với thời
> gian thì ta có thể tính rate of change giữa mực nước và thời gian
> (thông qua Chain Rule)

<br>

<a id="node-297"></a>

<p align="center"><kbd><img src="assets/1de644342d4d9fd0fb85387c72bca5eec87f89f6.png" width="100%"></kbd></p>

> [!NOTE]
> Bài toán tiếp theo là, ta muốn tìm vị trí của cục sắt nếu như
> hai đầu không cao bằng nhau

<br>

<a id="node-298"></a>

<p align="center"><kbd><img src="assets/f6090e48d4d21a45ce7f6ea93c0b253f14f7c1fc.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì gọi tọa độ hai đầu là (0,0) và (a,b) và toạ độ cục sắt là (x, y).
> Bài toán này gs cho là bài toán minimization, với constrain là đường
> cong này. Có nghĩa đại khái là ta cần tìm vị trí thấp nhất của cục sắt
> với ràng buộc là nó chỉ di chuyển trên đường cong này. Hay, là tìm
> điểm thấp nhất của đường cong này. Và dĩ nhiên nó sẽ phụ thuộc
> chiều dài sợi dây và hai điểm đầu

<br>

<a id="node-299"></a>

<p align="center"><kbd><img src="assets/5030d5f5a43c4270e6b41f3bc8f979fe7f336585.png" width="100%"></kbd></p>

> [!NOTE]
> Dựa vào các tọa độ, không khó để hiểu chiều dài mỗi đoạn sẽ là
> vầy (dựa vào pythagores) (chú ý x, b là các tọa độ nên phải là b-x
> chứ không phải b+x vì x âm)

<br>

<a id="node-300"></a>

<p align="center"><kbd><img src="assets/685844ab5da121260312340a8ad2f7206043c065.png" width="100%"></kbd></p>

> [!NOTE]
> Và tổng hai đoạn là chiều dài sợi dây, là fixed value (constant), gọi là
> L. Và đây là equation mô tả ràng buộc (constrain)
>
> Và quan trọng là ta cần nhận ra bài toán này ta cần tìm y nhỏ nhất
>
> Vì trong constrains equation này implicitly ngầm ẩn một function của
> y theo x. Và dễ thấy rằng tại điểm thấp nhất, tiếp tuyến với đường
> cong sẽ nằm ngang, y'(x) sẽ bằng 0, đó chính là critical point

<br>

<a id="node-301"></a>

<p align="center"><kbd><img src="assets/51acb0640c1460a7579130f02b8d6dd209ce619e.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là theo quy trình ta sẽ check critical points và sau đó là
> check các end point để xem thử critical point là maximum hay
> minimum
>
> Trong bài toán này ta có thể kết luận luôn critical point là minimum.
>
> Đương nhiên ta có thể dùng second derivative test nhưng ở đây
> làm cách đó sẽ rất phức tạp

<br>

<a id="node-302"></a>

<p align="center"><kbd><img src="assets/8b69d8ab353a540022504f2411b1964c6b15949c.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ implicit differentiation, lấy đạo hàm hai vế theo x
>
> Áp dụng chain rule, không khó để ra kết quả này
> với vế phải là dL/dx = 0 do L là constant

<br>

<a id="node-303"></a>

<p align="center"><kbd><img src="assets/d644976e173b203d49eb09c8e02721cdd1f623ec.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, ta sẽ dùng thực tế là ta đang solve equation y'
> = 0, với constrain trên, do đó ta có thể lắp y' = 0 vào

<br>

<a id="node-304"></a>

<p align="center"><kbd><img src="assets/53b7aa761b7c11055fc6f8eb3a8561ce2d2da576.png" width="100%"></kbd></p>

> [!NOTE]
> Và thật ra equation trên chính là sin(alpha) - sin(beta) = 0, và
> kết quả là alpha = beta
>
> Và gs cho rằng chỉ cần thêm một chút toán nữa là ta có thể
> tính ra y, nhưng kết quả tới đây là được rồi

<br>

<a id="node-305"></a>

<p align="center"><kbd><img src="assets/886c8e0689d0f4b9144a14d6e97f78195fe0e2b4.png" width="100%"></kbd></p>

<br>

<a id="node-306"></a>

<p align="center"><kbd><img src="assets/d44dffdf8ee920237303848611e25ac5c8b19f2f.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo ta qua Newton's method. Ví dụ ta muốn tính x sao
> cho x^2 = 5.
>
> ta có thể set f(x) = x^2 - 5 và chuyển bài toán thành giải
> phương trình f(x) = 0
>
> (thật ra chỉ là chuyển vế đổi dấu để có phương trình tương
> đương x^2 = 5 <=> x^2 - 5 = 0)

<br>

<a id="node-307"></a>

<p align="center"><kbd><img src="assets/3cce6562c8df13cf614f0cd80ba96cdccef2d920.png" width="100%"></kbd></p>

> [!NOTE]
> Gs sketch đồ thị của hàm y = x^2 - 5 là parabola này, đương nhiên nó
> cắt trục y (x=0) tại -5
>
> Và tìm solution của y = 0 đương nhiên là tìm x của điểm mà parabola
> cắt trục x (vì khi đó y = 0)
>
> Vậy thì phương pháp Newton sẽ là: ta sẽ bắt đầu với một initial guess
> (dự đoán ban đầu) về vị trí (x) của giao điểm. Ví dụ tại x0 = 2.
>
> Từ đó ta mới thiết lập phương trình của tiếp tuyến (tangent line) tại (x0,
> y(x0) = y0). Tiếp tuyến này sẽ cắt trục x, và ta sẽ tìm x của điểm đó để
> có new guess x1
>
> Quá trình sẽ lặp lại để các guess ngày càng tiến về giao điểm của
> parabola và trục x

<br>

<a id="node-308"></a>

<p align="center"><kbd><img src="assets/1eefaf65e463dbf835cc4cbfa2b16c8a86af46b6.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì phương trình tiếp tuyến đi qua x0, y0 sẽ có dạng thế này y-y0 =
> m(x-x0) với m như đã biết sẽ là đạo hàm của hàm y tại x0: y'(x0).
>
> Vậy thì để tìm new guess - giao điểm của tangent line với trục x, ta sẽ
> cho y = 0, khi đó x sẽ là new guess, tức x1
>
> 0 - y0 = m(x1 - x0)

<br>

<a id="node-309"></a>

<p align="center"><kbd><img src="assets/f5f99b36cefff128ed30da24301691d70c129933.png" width="100%"></kbd></p>

> [!NOTE]
> Để rồi ta solve ra x1 = x0 - y0 / m. Và y0 như đã biết là f(x0)
> còn m là độ dốc (slope) của hàm f tại x0: f'(x0)
>
> Vậy **x1 = x0 - f(x0)/f'(x0)
>
> Gs cho rằng đây là công thức giúp ta tính mọi căn (root)**

<br>

<a id="node-310"></a>

<p align="center"><kbd><img src="assets/1e9b3e81d7c257d59a22fe50245037ddc76b4213.png" width="100%"></kbd></p>

> [!NOTE]
> Và đây là công thức của
> Newton's Method
>
> x_n+1 = x_n - f(x_n) / f'(x_n)

<br>

<a id="node-311"></a>

<p align="center"><kbd><img src="assets/accc3358b8a5867cd0a9fd61cd40b30f0d153e1a.png" width="100%"></kbd></p>

> [!NOTE]
> Áp dụng vào, ở đây f'(x) dễ thấy là 2x, từ
> đó ta tính ra x1 = x0/2 + 5/2x0

<br>

<a id="node-312"></a>

<p align="center"><kbd><img src="assets/9bfc49c7d8b3fc09952972a7bdcae48d52a59f77.png" width="100%"></kbd></p>

> [!NOTE]
> Thế x0 = 2 (initial guess) ta có x1 = 9/4. Tiếp tục áp dụng
> x_n+1 = x_n + f(x_n) / f'(x_n) vẫn sẽ là x2 = 1/2*x1 + (5/2x1)
> = 161/72

<br>

<a id="node-313"></a>

<p align="center"><kbd><img src="assets/bbd555492e8812ca09c1c051138e7286237eefdd.png" width="100%"></kbd></p>

> [!NOTE]
> Và sau vài iteration ta đã thấy sai khác giữa
> sqrt (5) và x_n đã rất nhỏ

<br>

