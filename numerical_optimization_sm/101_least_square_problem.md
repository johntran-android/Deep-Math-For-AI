# 10.1 Least-square Problem

📊 **Progress:** `5` Notes | `6` Screenshots

---
<a id="node-92"></a>

<p align="center"><kbd><img src="assets/99ebd4becbb5ac08bc3289d84bfcffdec1677026.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7929b7dc55c371f313d4bb4da8d67a6173bff636.png" width="100%"></kbd></p>

> [!NOTE]
> Đầu tiên, gs giới thiệu bài toán least-square là bài toán tối ưu mà objective
> function của nó có dạng f(x) = (1/2) Σj rj(x)^2 với rj là smooth R^n → R
> function, được gọi là residual (phần dư).
>
> Đây là bài toán rất phổ biến xuất hiện ở rất nhiều lĩnh vực.
>
> Và chương này mình sẽ học các thuật toán mạnh mẽ để giải bài toán
> này

<br>

<a id="node-93"></a>

<p align="center"><kbd><img src="assets/0e5d85b02f62a91f37bf329cea6f6530dff66760.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là gs nói rằng ta sẽ thấy tại sao dạng đặc biệt của f thường sẽ khiến
> cho bài toán least-squares dễ giải hơn là bài toán unconstrained minimization
> problem chung chung.
>
> Thế thì, nhớ là trong bài toán này, objective là (1/2) Σi [ri(x)]^2, tức là tổng của
> bình phương residual ri(x). Bằng cách gom chúng lại thành vector r(x) = [r1(x),
> r2(x),....]T, thì Σi [ri(x)]^2 có thể thể hiện bởi (1/2) ||r(x)||^2, cũng là f(x) = (1/2)
> r(x)T r(x)
>
> Vậy thì, một điểm mình cần hiểu, f(x) là vector → scalar function. Nên
> derivative của f(x) đối với x là gradient vector có các phần tử là partial
> derivative ∇f(x) = (∂f/∂x1,...,∂f/∂xn)
>
> Nhưng ở đây gs nhắc đến Jacobian, thì đang nói về đạo hàm của hàm R^n
> vector → R^m vector r(x), là matrix mà hàng i của nó là vector các partial
> derivative (∂ri(x)/∂x1, ∂ri(x)/∂x2,....∂ri(x)/∂xn), dĩ nhiên, cũng chính là gradient
> vector ∇ri(x)

<br>

<a id="node-94"></a>

<p align="center"><kbd><img src="assets/e120b6799a17049110566f353c3968e2c7907cdb.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì ta có f(x) = (1/2) r(x)Tr(x) và J(x) là d/dx r(x).
>
> d/dx f(x) = (1/2) d/dx [r(x)Tr(x)]
>
> = (1/2) { d/dr(x) [r(x)Tr(x)] } . d/dx r(x) (Chain-rule)
>
> Tạm dừng chút xíu, xét hàm g(x) = xTx. Tính đạo hàm nhanh theo cách làm
> của MIT 18s096: dg(x) = (x+dx)T(x+dx)-xTx = (xT+dxT)(x+dx)-xTx =
> xTx+dxTx+xTdx+dxTdx-xTx = 2xTdx+dxTdx = 2xTdx (bỏ term bậc cao) ⇨
> ∇g(x) = 2x.
>
> Quay lại đây, dùng kết quả vừa rồi ta có:
>
> ... = (1/2) 2r(x) . J(x) = r(x) . J(x) (dấu . là kí hiệu hàm hợp)
>
> Tiếp, vì f(x), như đã nói là vector → scalar function, nên ∇f(x) dĩ nhiên là
> vector R^n, nên kết quả sẽ là J(x)Tr(x) (có shape [m,n]T[m,1] = [n,m][m,1] =
> [n,1].
>
> Nên ∇f(x) = J(x)Tr(x) là công thức 10.4 trong sách là vậy.
>
> Còn Hessian của f(x), thì cũng là d/dx ∇f(x)
>
> = d/dx [J(x)Tr(x)]
>
> Xét d/dx [J(x)Tr(x)] = d/dx [Σi [cột i của J(x)T] ri(x)]
>
> = Σi d/dx {[cột i của J(x)T] ri(x)}
>
> Xét hàm gi(x) = [cột i của J(x)T] ri(x), cũng chính là [hàng i của J(x)]T ri(x) =
> ∇ri(x) ri(x), là vector có các phần tử [∂ri(x)/∂x1 ri(x), ∂ri(x)/∂x2 ri(x), ...∂ri(x)/xn
> ri(x)]
>
> ⇨ d/dx gi(x) = d/dx [∇ri(x) ri(x)]
>
> = [d/dx ∇ri(x)] . ri(x) + ∇ri(x) . d/dx ri(x)
>
> = [∇^2ri(x)] . ri(x) + ∇ri(x) . ∇ri(x)
>
> Phân tích: gi(x) là R^n vector → R^n vector function, nên d/dx gi(x) là
> Jacobian matrix có shape [n,n].
>
> ri(x) là R^n vector → scalar function → ∇^2 ri(x) là Hessian matrix có shape
> nxn.
>
> cũng như ∇ri(x) là gradient vector, ⇨ ∇ri(x) . ∇ri(x) phải là outer product để
> có nxn matrix: ∇ri(x) ∇ri(x)T
>
> Vậy d/dx gi(x) = ∇^2ri(x) ri(x) + ∇ri(x) ∇ri(x)T
>
> Vậy d/dx [J(x)Tr(x)] = Σi d/dx {[cột i của J(x)T] ri(x)} = Σi d/dx gi(x)
>
> = Σi {∇^2ri(x) ri(x) + ∇ri(x) ∇ri(x)T}
>
> = Σi {∇^2ri(x) ri(x)} + Σi {∇ri(x) ∇ri(x)T}
>
> Term thứ 2, Σi {∇ri(x) ∇ri(x)T}, chính là tổng các rank 1 matrix, theo góc nhìn
> thứ 4 nhân hai matrix, ta có thể thấy đây là tích của hai matrix: [matrix có
> các cột là ∇ri(x)] [matrix có các hàng là ∇ri(x)] = J(x)T J(x)
>
> Vậy kết quả là Σi {∇^2ri(x) ri(x)} + J(x)TJ(x), chính là 10.5

<br>

<a id="node-95"></a>

<p align="center"><kbd><img src="assets/a994d70a4b198b78228cca1da0e857d609c74ab8.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì đại khái là vầy: Ta đã thấy rằng trong bài toán least-square, trong đó
> hàm objective là f(x) = Σi ri(x)^2 = r(x)Tr(x) với r(x) là vector → vector
> function, có Jacobian J(x) thì đạo hàm cấp 1 ∇f(x) và Hessian ∇^2f(x) có thể
> được tính bởi hai công thức 10.4 và 10.5. Và gs nói rằng, trong rất nhiều
> ứng dụng thì việc tính toán J(x) rất ít tốn kém. Từ đó, dẫn tới việc tính ra
> gradient và Hessian cũng đều không tốn kém gì mấy. Và đây là một đặc
> điểm mà ông cho rằng khiến bài toán least-square trở nên dễ chịu, và ông
> gọi nó đại khái là ta có được Hessian miễn phí.
>
> Mình hiểu thế này, trong các thuật toán tối ưu mà ta học ở đầu tới giờ, cũng
> như đã học ở Convex Optimization, giúp mình hiểu rằng: Trong các thuật
> toán tối ưu, xét về tốc độ hội tụ, thì Newton method là ngon nhất, và các
> thuật toán tối ưu đều cố gắng dùng thông tin độ cong có trong Hessian
> matrix. Có điều, vấn đề là nhiều khi tính toán Hessian rất tốn kém, thành ra
> trong các chương trước ta mới thấy các thuật toán quasi-Newton trong đó
> người ta cố gắng ước lượng Hessian để có được thông tin độ cong nhưng
> không quá tốn kém. Còn ở đây, ta có được Hessian chính xác mà không
> tốn mấy thì dĩ nhiên là quá tốt.
>
> Phải hiểu thêm là, trong đoạn này còn một ý, nói đại khái là việc tính J(x)
> rẻ, chỉ giúp tính phần J(x)TJ(x) của Hessian là rẻ thôi, còn cái term thứ hai
> thì vẫn liên quan đến Hessian của rj(x), vẫn tốn. Tuy nhiên, đại ý là vì vài lí
> do thì phần đầu mới đóng vai trò quan trọng, thành ra nói chung ta vẫn
> được lợi ích.

<br>

<a id="node-96"></a>

<p align="center"><kbd><img src="assets/922af395644376dcd64979f4e462307de1a01568.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì chương này ta sẽ bàn về các thuật toán giải bài toán least-square và
> trong đó ta sẽ thấy chúng đều cố gắng khai thác tính chất vừa nói trên.
>
> Và ta sẽ thấy những thuật toán đó đều thuộc vào hai cách tiếp cận lớn mà ta
> đã học Line Search và Trust Region. Cũng như là với mỗi cách, cũng chia ra
> là tiếp cận theo Newton và quasi-Newton method.

<br>

