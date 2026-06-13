# 10.1 Least-square Problem

📊 **Progress:** `3` Notes | `4` Screenshots

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

