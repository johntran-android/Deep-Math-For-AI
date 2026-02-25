# Lec 12: Related Rates

📊 **Progress:** `24` Notes | `25` Screenshots

---
<a id="node-261"></a>

<p align="center"><kbd><img src="assets/92ed7457f3a9e309e1f52e59794475036b2ad1fa.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ tiếp tục với Max / Min. Bài toán là, cho đoạn dây chiều dài
> 1. Cắt thành 2 phần, làm thành 2 hình vuông. Câu hỏi là tìm
> diện tích lớn nhất có thể tạo ra được bởi hai hình vuông đó.

<br>

<a id="node-262"></a>

<p align="center"><kbd><img src="assets/bdec50c6c2c424c83b104cbbd6ebbfeff6bd0daf.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì gọi hai đoạn là x, và 1-x, ta sẽ thiết lập diện tích của
> hai hình vuông như sau A = (x/4)^2 + [(1-x)/4]^2

<br>

<a id="node-263"></a>

<p align="center"><kbd><img src="assets/84dc3ec5e2c396b9716cd538f3df4903606755d6.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì, solve A' = 0 ta có
> x=1/2 là critical point.

<br>

<a id="node-264"></a>

<p align="center"><kbd><img src="assets/0062a29bce848b17782af62af6b15f8365a0648b.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó thế vào ta có critical point value là 1/32. Tuy nhiên gs cho rằng
> ta chưa xong, vì như đã nói, ta còn cần phải check các endpoint cũng
> như discontinuity point
>
> (vài suy nghĩ, đương nhiên từ 1802 ta biết critical point không chắc là
> max, min thậm chí có thể là critical point nữa. Muốn biết ta sẽ phải
> check bằng second derivative test. Thì đối với hàm đơn biến ở lớp này
> chắc gs cũng sẽ nói)

<br>

<a id="node-265"></a>

<p align="center"><kbd><img src="assets/cbf8da275705af6dea781b5fc1f5938f1c30739c.png" width="100%"></kbd></p>

> [!NOTE]
> Bằng cách check thêm giá trị hàm A tại các endpoint, ta thấy:
>
> A(0+) = 1/16 và A(1-) = 1/16 cho thấy thật ra critical point có thể là
> minimum chứ không phải maximum của Area mà ta đang muốn

<br>

<a id="node-266"></a>

<p align="center"><kbd><img src="assets/310c9d8f28166c8cb8533e7931e7b46e9bb46693.png" width="100%"></kbd></p>

<br>

<a id="node-267"></a>

<p align="center"><kbd><img src="assets/cfeec27c963e67a91f5739a37850b110e8c2a1c3.png" width="100%"></kbd></p>

> [!NOTE]
> Như vậy maximum của A là 1/16, và minimum value là 1/32.
> Và gs lưu ý rằng, x=1/2 là nơi mà minimum achieved (nơi
> function đạt minimum value), nên hỏi minimum ở đâu thì trả
> lời là tại 1/2 nhưng minimum value bằng bao nhiêu thì đương
> nhiên phải là 1/16

<br>

<a id="node-268"></a>

<p align="center"><kbd><img src="assets/4141849d1ad6906f72d37e371695feb549a14990.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là, gs cho rằng câu hỏi đặt ra khi hỏi diện tích lớn nhất
> enclosed, là một trick question (tạm hiểu là câu hỏi cũng không
> dễ trả lời) và theo ông ta sẽ trả lời là 1/16, dù rằng đây đương
> nhiên là giá trị tại limit
>
> (1/16 là limit của A(x) khi x->0+ hoặc x->1-)

<br>

<a id="node-269"></a>

<p align="center"><kbd><img src="assets/88d64dd8488b5cdbed2bbc48d09607474af6d448.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ thứ hai, câu hỏi là tìm cái hộp có đáy vuông (ý là tìm kích
> thước của nó) không có nắp, sao cho diện tích bề mặt ít nhất với
> thể tích cho trước

<br>

<a id="node-270"></a>

<p align="center"><kbd><img src="assets/2f84271771369106075ac5694920e84ee0590792.png" width="100%"></kbd></p>

> [!NOTE]
> gọi x là chiều dài cạnh đáy và y là chiều cao. Thể
> tích V cho trước là x^2y và A = x^2 + 4xy
>
> Vì V fixed, nên ta có thể solve y theo x

<br>

<a id="node-271"></a>

<p align="center"><kbd><img src="assets/b831e81ba0459b00cd67733428d1ad058c46de2c.png" width="100%"></kbd></p>

> [!NOTE]
> Để có y = V / x^2 và A trở thành
> function theo x: x^2 + 4v/x

<br>

<a id="node-272"></a>

<p align="center"><kbd><img src="assets/358087b88e86e9e80d7efeeae16c2223199085bd.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó, tìm A' và giải A' = 0 ta có
> critical point là x = (2V)^1/3

<br>

<a id="node-273"></a>

<p align="center"><kbd><img src="assets/f37a897b882b6373ecce876e01d6a97d4c21f1cc.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là, ta sẽ xem range của x là gì. Thì x sẽ lớn hơn 0 (vì
> nếu bằng 0, V sẽ bằng 0) và x có thể lớn đến vô cùng.
>
> Gs cho rằng khi ta gặp bài toán mà không có giới hạn trên cụ
> thể nào thì giới hạn trên sẽ thường là infinity.

<br>

<a id="node-274"></a>

<p align="center"><kbd><img src="assets/bef4ff9cb467cc5008acb363fbbcfa042e1a0b30.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ check value của nó tại end points:
>
> A(0+), tức là limit của A(x) khi x -> 0+, bằng cách thế 0+
> vào x^2 + 4V/x thì (0+)^2 = 0, 4V/(0+) = infinity, nên kết quả
> là 0 + infinity = infinity

<br>

<a id="node-275"></a>

<p align="center"><kbd><img src="assets/9beef6eba33f59ad1ba0b3f0ebc968f27288288f.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự, A(infinity) = (inf)^2 +
> 4V/(inf) = inf + 0 = inf

<br>

<a id="node-276"></a>

<p align="center"><kbd><img src="assets/3c52e3bbf2e16b346a97651f410a5e629f1b350b.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó ta có thể kết luận critical point, x =
> (2V)^1/3 chính là minimum

<br>

<a id="node-277"></a>

<p align="center"><kbd><img src="assets/fd3ae06cbeff906838d60e9ff441ac885604743c.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói đại khái là ông cho rằng có thể dùng second derivative test để
> kiểm tra xem critical point là min hay max.
>
> Bằng cách tính A''(x), kết quả ra 2 + 8V / x^3 luôn lớn hơn 0 với mọi x 
> lớn hơn 0.
>
> Và do đó có thể kết luận function concave up (lõm hướng lên) suy ra
> critical points là minimum point

<br>

<a id="node-278"></a>

<p align="center"><kbd><img src="assets/29625eecb87e011e1dc047b0477d031db3717272.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó ta tính ra y và A khiến
> minimize diện tích hộp

<br>

<a id="node-279"></a>

<p align="center"><kbd><img src="assets/795bd31f0b77630d98bcedfa3ba99bb8b7d17641.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là, gs cho rằng ta có thể trả lời theo cách hay hơn, bằng
> cách dùng dimensionless variable: ví dụ A/V^(2/3) là tỉ lệ không còn 
> dính đến đơn vị nữa.
>
> Hay x/y cũng vậy, vậy nếu theo kết quả x, y ta có thì x/y = 2. Và đó là
> câu trả lời ý nghĩa nhất: miễn là hộp có x/y = 2 thì đó là optimal box

<br>

<a id="node-280"></a>

<p align="center"><kbd><img src="assets/0c813403d481eb3cef5ba0447314384c6b1f416d.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi của student:
>
> ? Nếu không cho mặt đáy vuông thì có giải được không? -> Được,
> nếu dùng 1802 tức là multivariate calculus. vì khi đó ta sẽ có thêm
> một variable z nữa.

<br>

<a id="node-281"></a>

<p align="center"><kbd><img src="assets/688ca629cb46657380200fd4864bbf59a6c32546.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo gs cho rằng ông sẽ giải bài toán này lại sử dùng implicit
> differentiation (vi phân hàm ẩn). Như đã biết, implicit differentiation có
> nghĩa là, ta có một equation, ẩn chứa trong đó là một function ví dụ
> trong V = x^2y, ẩn chứa (implicitly) function y = y(x) = V / x^2.
>
> Thế thì, bằng cách lấy đạo hàm equation - tức apply (d/dx) operator
> vào hai vế ta sẽ có thể solve y'.
>
> vậy từ V = x^2*y (again, chú ý y lúc này là implicit function theo x),
> ta có (d/dx) V = (d/dx) x^2*y 
>
> <=> 0 = 2xy + x^2y' (vì V là fixed, constant, nên (d/dx) V = 0, còn vế 
> phải thì theo product rule.
>
> từ đó suy ra y' = -2y/x.
>
> Tương tự (d/dx) A = 2x + 4y + 4xy'

<br>

<a id="node-282"></a>

<p align="center"><kbd><img src="assets/5670b64048ab7ba9b88365e99495c8a06b505c8c.png" width="100%"></kbd></p>

> [!NOTE]
> Và gắn y' vào dA/dx. Ta sẽ solve equation dA/dx (để
> tìm critical point như cách thông thường)

<br>

<a id="node-283"></a>

<p align="center"><kbd><img src="assets/0736292aebcfa7f05de1ad779ba555a9a5b2ba86.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả ra x/y=2 như cách hồi nãy (đương nhiên nếu apply
> vào V = x^2y thì sẽ solve ra x, y theo V giống như cách 1
> nhưng ta đã nói để kết quả ở dạng x/y=2 như vầy thì hay hơn)

<br>

<a id="node-284"></a>

<p align="center"><kbd><img src="assets/9a03a756050a61ca09ca2b3adee421bb0224ac42.png" width="100%"></kbd></p>

> [!NOTE]
> gs cho rằng cách này nhanh hơn, và cho ra kết quả nicer. Nhưng
> disadvantage của nó là nó không check dc critical point là max / min
> hay cả hai (vẫn có thể là cả hai như đã biết ở 1802, gọi là saddle
> point)
>
> Student hỏi làm sao để check. Thì gs nói trong bài toán cụ thể này
> thì ta phải check như hồi nãy ta check, đó là xem A(0+) và A(inf+)
> để ra A đều bằng infinity để kết luận critical point là min.
>
> Nhưng ông cho rằng sẽ có nhiều bài toán mà việc check này không
> cần thiết vì nó rõ ràng rồi. Khi đó cách này sẽ giúp ta làm nhanh hơn

<br>

<a id="node-285"></a>

<p align="center"><kbd><img src="assets/a2d4908b83cde7076af898c60982e1e2b8b74e23.png" width="100%"></kbd></p>

> [!NOTE]
> Mấy phút cuối gs set up bài toán về Related
> Rate. Ta sẽ tiếp tục ở bài sau

<br>

