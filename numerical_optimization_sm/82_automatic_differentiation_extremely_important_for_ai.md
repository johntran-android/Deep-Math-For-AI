# 8.2 Automatic Differentiation (*extremely Important For Ai)

📊 **Progress:** `5` Notes | `8` Screenshots

---
<a id="node-54"></a>

<p align="center"><kbd><img src="assets/962f8cffadbdba68be19e7746dc7e7502483bbbf.png" width="100%"></kbd></p>

> [!NOTE]
> gs nói sơ rằng Auto Diff là tên gọi chung cho những kĩ thuật mà trong đó
> người ta dùng một "computational representation" của một function để tính ra
> giá trị analytic của đạo hàm.
>
> Mình hiểu: analytic ý là giá trị chính xác, khác với numerical hay
> approximation là giá trị tính gần đúng của đạo hàm. Nhớ lại trong cs231n
> hay cs224n, cũng đã nghe cụm từ này. Trong đó ta dùng cách tính đạo hàm
> xấp xỉ để kiểm tra (debug, xem trong quá trình xây dựng mô hình có sai sót
> gì không).
>
> Ông nói, có kĩ thuật thì làm theo lối, tạo ra code để tính đạo hàm. còn có
> cách khác thì làm theo cách đại ý giữ giá trị của các biến trung gian khi tính
> function, và quay lại dùng lại cái này để tính đạo hàm.
>
> Mình nhận ra, đây chính là BACK-PROPAGATION huyền thoại: Giữ giá trị
> các bước trung gian trong forward mode và dùng nó để tính đạo hàm trong
> backward dựa theo chain-rule.
>
> Kiến thức này luôn được nói đến trong các lớp AI, và cả MIT 18s096, nhưng
> đây là lúc mình gặp lại nó ở mức độ sâu nhất.

<br>

<a id="node-55"></a>

<p align="center"><kbd><img src="assets/f744ba42652870c79b0fa3dcae43cb76c72c1543.png" width="100%"></kbd></p>

> [!NOTE]
> Khúc đầu đại ý gs nói rằng ý tưởng của Auto Diff xuất phát từ việc người ta nhận thấy
> là dù cái hàm f có phức tạp cỡ nào thì bản chất có thể chẻ nó ra thành các phép toán
> nhỏ cơ bản. Bao gồm có các phép toán nhận hai giá trị đầu vào và làm gì đó: như
> cộng , trừ, nhân , chia, lũy thừa. Và các phép toán nhận một gía trị đầu vào và làm gì
> đó: lấy log, e^, ...
>
> Sau đó, một công cụ nữa sẽ dùng, là chain-rule trong calculus, nói rằng nếu hàm h là
> hàm theo vector y, mà y lại là hàm theo vector x thì ta sẽ có: ∇_x h(y(x)) = blah blah...
>
> Là sao?
>
> Đầu tiên, h(y) là vector → scalar function, nhận vector y, trả ra scalar h(y)
>
> y(x) lại là vector → vector function: nhận vector x, trả ra vector y(x).
>
> Nên h(y(x)) sẽ là vector → scalar function: nhận vector x, trả ra scalar h(y(x)) do đó,
> đạo hàm của h wrt x là gradient vector: ∇h(x)
>
> Ghi như trong sách để làm rõ là coi cái nào là biến thôi: ∇_x h(y(x)) vì nếu coi y là biến,
> tức tính đạo hàm của h theo y ta sẽ ghi là ∇_y h(y)
>
> Cái này thì cũng chỉ là: d/dx h(y(x)) , đạo hàm của h đối với x
>
> Theo chain rule:
>
> d/dx h(y(x)) = d/d(y) h(y) . d/dx y(x)
>
> d/d(y) h(y) chính là ∇h(y)
>
> d/dx y(x), là đạo hàm của y wrt x, vì y(x) là vector → vector nên cái này là Jacobian
> matrix J(x)
>
> Vậy ta có một operation giữa vector gradient ∇h(y) và matrix J(x), và kết quả phải cho
> ra vector (∇h(x)) nên phải thể hiện nó là: matrix J(x)T nhân vector ∇h(y) (thì mới ra
> column vector được)
>
> Phải transpose vì J có shape là (m,n), (J)T có shape (n,m) thì nhân với gradient ∇h(y)
> có shape (m,1) thì mới khớp.
>
> ⇨ ∇x_h(y(x)) = J(x)T ∇h(y)
>
> Rồi, quay lại xét ∇h(y), viết rõ ra, nó là vector các đạo hàm riêng:
>
> [∂h(y)/∂y1,...∂h(y)/∂ym]
>
> Còn J(x), là Jacobian của y wrt x, ta biết, mỗi hàng của nó, ví dụ hàng 2 là vector  đạo
> hàm riêng của y2 đối với x: [∂y2/∂x1, ∂y2/∂x2,...,∂y2/∂xn], và nó cũng là gradient của y2
> wrt x: ∇y2(x)
>
> Để rồi khi transpose, để có J(x)T, thì cột thứ 2 chính là ∇y2(x). Cột thứ i chính là ∇yi(x)
>
> Và J(x)T ∇h(y), theo MIT 1806 góc nhìn nhân matrix với vector thứ hai đã biết: Ax là
> linear combination các cột của A với hệ số là các phần tử của x.
>
> Vậy J(x)T ∇h(y) = linear combination các cột J(x)T với hệ số là components của ∇h(y):
>
> J(x)T ∇h(y) = **Σi=1:m ∂h(y)/∂yi ∇yi(x)**. Đây chính là công thức 8.25

<br>

<a id="node-56"></a>

<p align="center"><kbd><img src="assets/031370399994a483b9350d882550c83b85725c13.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/52a5d500ddf0a0a79367c79ebd9ee214a8c884ae.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1cee6b5ac9423b87ff32ee209cbaa3e862595d8c.png" width="100%"></kbd></p>

> [!NOTE]
> gs lấy một ví dụ, ta sẽ xét hàm f(x) = x1x2sin(x3) + e^(x1x2)/x3.
>
> việc tính toán bên trong hàm số này có thể được bẻ ra thành các bước nhỏ,
> có thứ tự. Đặt các biến trung gian, và thể hiện quá trình tính toán các bước
> này như một đồ thị, nơi các phép tính sẽ biểu diễn bởi  các node.
>
> Cái này gọi là computational graph.
>
> Và việc tính toán từ trái sang phải (đi từ x1,x2,x3 → x9) gọi là FORWARD
> SWEEP
>
> gs có lưu ý ta là, các phần mềm auto diff sẽ tự làm bước bẻ nhỏ hàm f
> thành các bước nhỏ này

<br>

<a id="node-57"></a>

<p align="center"><kbd><img src="assets/1e1fa9401c5dc31f5fc9519a5aae5266daede71d.png" width="100%"></kbd></p>

<br>

<a id="node-58"></a>

<p align="center"><kbd><img src="assets/627722fa024a74dffe8276dec2a7af19878bfbbb.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là, trong forward mode của auto diff, ta sẽ tính và mang theo một giá
> trị đạo hàm theo hướng p cho mội biến trung gian xi. Và ta làm việc này cùng
> lúc với việc evaluation xi.
>
> Lí do, hay mục đích của việc này thì chưa rõ lắm có thể tí nữa sẽ biết. Còn
> giờ cứ tạm hiểu vậy.
>
> Directional derivative của hàm f wrt hướng d, mình còn nhớ là như sau: Ý
> nghĩa của nó là độ dốc hàm f theo hướng d tại x
>
> Xét hàm R^n → R f(x), Xét hàm scalar → scalar g(α) = f(x + αd), thì g' (α)|α=0
> cũng là độ dốc của hàm f(x) theo hướng d tại x, chính là định nghĩa của
> directinal derivative của f(x) wrt d:
>
> lim ε → 0 [f(x + εd) - f(x)] / ε
>
> Ta sẽ xem vì sao nó là ∇f(x)Td:
>
> g'(α) = d/dα g(α) = d/dα f(x + αd)
>
> = d/d(x + αd) f(x + αd) . d/dα (x + αd) (chain rule)
>
> = ∇f(x + αd) . d
>
> (và vì g(α) là scalar → scalar, nên g'(α) phải là scalar, nên operation hợp trên
> chỉ có thể là dot product của hai vector)
>
> = ∇f(x + αd)Td.
>
> Và g'(α)|α=0 = ∇f(x)Td.
>
> \------
>
> Quay lại đây, đại khái là ta sẽ định nghĩa kí hiệu Dp_xi là directional
> derivative theo hướng p của xi
>
> Có nghĩa là sao:
>
> Tức là ta **cứ xem x1, ...x6 đều là function theo x1, x2, x3**.
>
> Ví dụ, x1, coi như là hàm x1(x1,x2,x3): Chữ x1 đầu tiên là tên hàm, x1, trong
> ngoại là argument / input. và cái hàm này = 1*x1 + 0*x2 + 0*x3.
>
> Thì như vậy, đây vẫn là hàm vector → scalar, với việc hiểu x là vector [x1, x2,
> x3], thì ta cũng ghi là x1(x) y như f(x) vậy.
>
> Rồi cũng có gradient vector ∇x1(x) (y như ∇f(x) vậy) là vector các partial
> derivative [∂x1(x)/∂x1, ∂x1(x)/∂x3, ∂x1(x)/∂x3], dĩ nhiên sẽ có giá trị là [1, 0, 0]
>
> Tương tự, x4 cứ coi như là hàm x4(x1,x2,x3) = x1*x2 + 0*x3.
>
> Và ∇x4(x) = [∂x4(x)/∂x1, ∂x4(x)/∂x3, ∂x4(x)/∂x3] 
>
> = [x2, x1, 0] (vì x4 = x1*x2 ⇨ ∂x4(x)/∂x1 = x2, ∂x4(x)/∂x2 = x1, và ∂x4(x)/∂x3 = 0)
>
> Tương tự với các ∇xi(x), i = 1,....9
>
> Và ta sẽ quan tâm đạo hàm theo hướng p của chúng
>
> Chỗ này hơi khó hiểu về kí hiệu, nhưng hãy nhìn thế này: Ta có hàm f(x), thì
> directional derivative của f wrt hướng d là ∇f(x)Td.
>
> Vậy giờ ta có hàm xi(x), ví dụ x4(x), thì directional derivative của x4 wrt p là:
>
> ∇x4(x)Tp
>
> Nên ∇x4(x)Tp = ∂x4(x)/∂x1 * p1 + ∂x4(x)/∂x3 * p2 + ∂x4(x)/∂x3 * p3
>
> = Σj=1,2,3 ∂x4(x)/∂xj * pj
>
> Tương tự, với mọi i = 1,...9
>
> ∇xi(x)Tp = Σi=1:3 ∂xi/∂xj * pj
>
> Từ đó có thể hiểu ∇x1(x)Tp = 1*p1 + 0*p2 + 0*p3  = p1
>
> tương tự ∇x2(x)Tp = p2, ∇x3(x)Tp = p3
>
> Nên ở đây mới nói "We note immediately that initial values Dpxi for the
> independent variables xi , i = 1, 2, 3" là vậy

<br>

<a id="node-59"></a>

<p align="center"><kbd><img src="assets/2aafa6c60819f0a7d865a8b0dc193b5886a166e1.png" width="100%"></kbd></p>

> [!NOTE]
> Mấu chốt chỗ này là: Khi có x4, Dpx4, x5, thì vì x7 = x4 + x5 nên ta có thể **tính x7 và Dpx7 (tức
> ∇x7(x)Tp) cùng lúc**.
>
> Là sao:
>
> Biết x4, x5 thì tính được x7 thì đương nhiên rồi: x7 = x4 + x5.
>
> Nhưng làm sao có Dpx7 (cũng là ∇x7(x)Tp)?
>
> → Dựa vào công thức 8.25: J(x)T ∇h(y) = Σi=1:m ∂h(y)/∂yi ∇yi(x).
>
> Đây nhé:
>
> Ở đây x7, trước tiên nó là hàm của x4, x5: x7(x4, x5) = x4 * x5
>
> Nên x7 là vai trò của h, [x4,x5] là trong vai y.
>
> Đạo hàm của h=x7 đối với y=[x4,x5] sẽ là gradient vector ∇h(y) = ∇x7(x4,x5)
>
> = [∂x7/∂x4, ∂x7/∂x5] = [x5, x4]
>
> Sau đó vì x4, x5 là hàm của x1, x2, x3: x4(x1,x2,x3), x5(x1,x2,x3) như note trước đã nói.
>
> Nên nếu xét y = [x4,x5] thì nó là R^3 → R^2 function y(x) = y(x1,x2,x3) = [x4(x1,x2,x3), x5(x1,x2,x3)]
>
> Và đạo hàm của y wrt x là Jacobian J(x).
>
> Có hàng 1 là ∇y1(x) = ∇x4(x)
>
> Và hàng 2 là ∇y2(x) = ∇x5(x)
>
> Vậy theo công thức trên:
>
> ∇x7 = ∂x7/∂x4 ∇x4 + ∂x7/∂x5 ∇x5 = x5 ∇x4 + x4 ∇x5
>
> Dot product hai vế với p:
>
> ∇x7Tp = (x5 ∇x4 + x4 ∇x5)Tp
>
> = x5 ∇x4Tp + x4 ∇x5Tp
>
> = x5 Dpx4 + x4 Dpx5
>
> =====
>
> Và cứ đi từ trái qua phải như vậy, mỗi lần ta sẽ tính cùng lúc một cặp (xi, Dpxi)

<br>

