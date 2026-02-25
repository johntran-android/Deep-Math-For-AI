# 2.4 Exercise

📊 **Progress:** `4` Notes | `10` Screenshots

---
<a id="node-110"></a>

<p align="center"><kbd><img src="assets/6d0ef7b29d493d5b7ab074d20317839076fb88e5.png" width="100%"></kbd></p>

<br>

<a id="node-111"></a>

<p align="center"><kbd><img src="assets/b46da589c02d9729b8938731994679da0140af52.png" width="100%"></kbd></p>

> [!NOTE]
> a. Regression, inference, n: 500, 
> p 3 - 3 features: profit, no. employees, industry
>
> b. Classification, prediction, n = 20, p = 13
>
> c. Regression, prediction, n = 12*4, p = 3

<br>

<a id="node-112"></a>

<p align="center"><kbd><img src="assets/29a816cfcf2f45e7f19183cc663504208927c9ee.png" width="100%"></kbd></p>

> [!NOTE]
> Từ less flexible -> high flexible:
>
> **Bias sẽ giảm**:
>
> **Variance sẽ tăng**
>
> **Training error** sẽ**giảm nhanh và chậm dần**:  Vì bias giảm
> và variance tăng đều khiến training error giảm.  Ban đầu
> giảm nhanh do kết hợp cả hai sự giảm error do giảm bias
> và cả variance, sau đó ảnh hưởng của giảm bias giảm
> dần nên chỉ còn ảnh hưởng của variance
>
> T**est error sẽ giảm nhưng sau đó sẽ tăng trở lại.**
> Lí do giảm bias giúp giảm test error, nhưng khi tăng variance
> khiến model bắt đầu overfit training set thì test error sẽ tăng

<br>

<a id="node-113"></a>

<p align="center"><kbd><img src="assets/0d4d1ddf0fd22494e14060f3124c399ca18e8608.png" width="100%"></kbd></p>

<br>

<a id="node-114"></a>

<p align="center"><kbd><img src="assets/5940bc510697d24cfaac4b2a12fb7ccab3a2234d.png" width="100%"></kbd></p>

<br>

<a id="node-115"></a>

<p align="center"><kbd><img src="assets/4401bdaf703f06a75c0f9b42e126fc386a031cc2.png" width="100%"></kbd></p>

> [!NOTE]
> Difference: Parametric thì có weight, nói chính xác hơn là giảm
> vấn đề từ việc tìm một function arbitrary f nào đó trở  thành một
> function có một bộ parameters, bộ params như thế nào thì tùy
> vào việc ta giả định (make assumption) về function f. Để rồi chỉ
> cần tìm bộ params thôi. Còn  non-parametric thì chưa hiểu lắm,
> nhưng đại khái là không có params mà kiểu như tìm cách mô
> hình function f bằng các observation.
>
> Advantage của params đó là: Nó có thể đơn giản hóa bài toán
> bằng cách đưa ra giả định về function f. Nếu giả định đúng, thì ta
> không cần quá nhiều training sample để train model.
>
> Nhưng disadvantage là nếu giả định sai thì f^ sẽ xa rời với thực
> tế f.

<br>

<a id="node-116"></a>

<p align="center"><kbd><img src="assets/662fa6c8cb55ed9dd0026a4c147b3ef67ae2fcb9.png" width="100%"></kbd></p>

<br>

<a id="node-117"></a>

<p align="center"><kbd><img src="assets/89d8ad30ee962002d40e875eec6bf0982188c7d4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/89d8ad30ee962002d40e875eec6bf0982188c7d4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c7c0b9ef9695d4acfd3bb13ffb3177c222a99365.png" width="100%"></kbd></p>

> [!NOTE]
> Nói rõ thêm câu d: Để match tốt với "ground truth" decision
> boundary (Bayes d.b) là non-linear thì phải có độ flexible cao
> nên K phải nhỏ (thì flexible cao)

<br>

