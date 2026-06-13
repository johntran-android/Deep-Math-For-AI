# 2.3 Gaussian Distribution

📊 **Progress:** `2` Notes | `4` Screenshots

---
<a id="node-205"></a>

<p align="center"><kbd><img src="assets/2656ed6afa45bb14b906417a3953011818e62c23.png" width="100%"></kbd></p>

> [!NOTE]
> Phần này ta sẽ nói về Gaussian (hay Normal distribution), là distribution khá
> quan quen thuộc sau khi học xong Stat110 và Casella. Công thức của case
> đơn biến hay đa biến thì mình cũng đã đều bíết rồi. Đặc biệt trong chap 1
> mình đã derive lại công thức Normal đa biến để hiểu công thức 2.43 rồi.
>
> Thế thì gs nói đây là distribution hay dùng, và nó xuất hiện trong nhiều bối
> cảnh. Ví dụ như trong chap 1 mình đã thấy nó chính là **distribution có
> entropy lớn nhất**.

<br>

<a id="node-206"></a>

<p align="center"><kbd><img src="assets/e3b90f424ad27ff3fce28ed3dfd1ab508f7c28b6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f3db0f9094505b969dca90fd4db8f11f7017169a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c9bc5a3f2529ba9f754d13311151d5541d41ee9f.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là gs Bishop nói một trường hợp nữa mà ta thấy sự xuất hiện của
> Normal đó là, Central Limit Theorem, còn nhớ trong Stat110 và Casella,
> theorem này nói rằng, xét một random sample size n X1,X2,...Xn ~ distribution
> có mean μ và variance σ^2 thì sample mean  Xbar sẽ converge in distribution
> về một normal(μ, σ^2/n).
>
> Và hình ảnh minh họa cho thấy, X1, ..Xn là uniform, và người ta plot giá trị của
> sample mean Xbar.
>
> Hiểu như sau. Ban đầu ta sẽ chỉ in Xbar của sample size N=1: tức là lấy
> random sample size N = 1 nhiều lần, mỗi lần tính ra Xbar, và plot ra, khi đó có
> thể thấy distribution của Xbar cũng chỉ là uniform.
>
> Nhưng ta làm vậy với N lớn dần thì sẽ thấy distribution của Xbar dần dần có
> dạng của normal.

<br>

