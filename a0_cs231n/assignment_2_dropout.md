# Assignment 2 - Dropout

📊 **Progress:** `7` Notes | `18` Screenshots

---
<a id="node-881"></a>

<p align="center"><kbd><img src="assets/f4549e30caee429f555e27b7bdc3935982e45920.png" width="100%"></kbd></p>

<br>

<a id="node-882"></a>

<p align="center"><kbd><img src="assets/85963f4babd5b1a102f4360d8ecde1068647a76d.png" width="100%"></kbd></p>

> [!NOTE]
> Dropout module thực ra rất đơn giản
>
> chú ý là nếu làm theo kiểu `x*=` mask, out `=` x thì
> sẽ không pass test do x đã bị thay đổi.

<br>

<a id="node-883"></a>

<p align="center"><kbd><img src="assets/5d000669df6a5e87226c497e1d5f9a43c0148559.png" width="100%"></kbd></p>

<br>

<a id="node-884"></a>

<p align="center"><kbd><img src="assets/27b0501c2d5bec3d987e886a99083dacf38cbdf0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/27b0501c2d5bec3d987e886a99083dacf38cbdf0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b33b779a925072207a7db0911802185d8db165c4.png" width="100%"></kbd></p>

<br>

<a id="node-885"></a>

<p align="center"><kbd><img src="assets/2f9642dec5b46a65f786205dfc1db94427e148ac.png" width="100%"></kbd></p>

> [!NOTE]
> Error should be around
> `e-10` or less: Passed

> [!NOTE]
> câu hỏi là nếu ko chia cho p thì sao?

<br>

<a id="node-886"></a>

<p align="center"><kbd><img src="assets/dd3a70867fc66fb3a50c98589c3d76d918dc187f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dd3a70867fc66fb3a50c98589c3d76d918dc187f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/452957821e4fcddd652e222ecd38807eaf3a33fe.png" width="100%"></kbd></p>

> [!NOTE]
> Relative errors should be around `e-6` or less.
> Note that it's fine if for `dropout_keep_ratio=1`
> you have W2 error be on the order of `e-5.`

<br>

<a id="node-887"></a>

<p align="center"><kbd><img src="assets/04bd898f2a041d518ca13ce1fd8e384c36738f56.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/04bd898f2a041d518ca13ce1fd8e384c36738f56.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6ccc65ed43e283556d8a96ab01e026899c03fe81.png" width="100%"></kbd></p>

> [!NOTE]
> Nếu có dropout thì
> apply nó trước relu,

<br>

<a id="node-888"></a>

<p align="center"><kbd><img src="assets/7f52cc3a4d1b3e512e4ba148ae98ff8cc563a854.png" width="100%"></kbd></p>

<br>

<a id="node-889"></a>

<p align="center"><kbd><img src="assets/c57b73ee6cc2f2f18e70ad204619257ec6e4bcba.png" width="100%"></kbd></p>

> [!NOTE]
> Có thể thấy rõ với dropout giúp giảm overfit
> nên val acc tốt hơn (đương nhiên là train acc
> kém hơn)

<br>

<a id="node-890"></a>

<p align="center"><kbd><img src="assets/e92a5897beb3c526134fb35c501b83548b5edfc9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e92a5897beb3c526134fb35c501b83548b5edfc9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d0b287aefbf996d3a8cd42334aa7f052ddd17ace.png" width="100%"></kbd></p>

> [!NOTE]
> đồ thì cho thấy khi có dropout thì training performance giảm,
> nhưng validation performance thì tốt hơn cho thấy dropout đã
> khắc phục tình trạng overfit

<br>

