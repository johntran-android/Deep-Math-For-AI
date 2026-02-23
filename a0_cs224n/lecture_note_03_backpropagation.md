# Lecture Note - 03 Backpropagation

📊 **Progress:** `7` Notes | `25` Screenshots

---
<a id="node-264"></a>

<p align="center"><kbd><img src="assets/d59d5f13e29d769bd357a2404c75e699b40a8812.png" width="100%"></kbd></p>

> [!NOTE]
> một số điểm chính
> trong document này

<br>

<a id="node-265"></a>

<p align="center"><kbd><img src="assets/a171eb3de14c2fad8aad15798704bb2ad54b5cb0.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái nói về việc ta đã đồng ý rằng cần phải có
> những mô hình mạnh hơn, complex hơn mới deal
> được với các dataset phức tạp thì neural network là
> model có thể làm được vậy

<br>

<a id="node-266"></a>

<p align="center"><kbd><img src="assets/567f7107b7bb45b8bdbee8ff3e37d84cc36f4bed.png" width="100%"></kbd></p>

> [!NOTE]
> bộ não người phức tạp hơn nhiều, nên sẽ rất khập
> khiễng nếu so sánh tuy nhiên neural network được
> inspired bới biological neural network. Hình ảnh dưới
> cho thấy khả năng tạo decision boundary flexible giúp
> separate được hai bên

<br>

<a id="node-267"></a>

<p align="center"><kbd><img src="assets/3ab537b0394ad8dd6c9788d033d7126a2307a283.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3ab537b0394ad8dd6c9788d033d7126a2307a283.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2f0fc39ab9d846845252631182b423850768763b.png" width="100%"></kbd></p>

<br>

<a id="node-268"></a>

<p align="center"><kbd><img src="assets/5d54a0068c383b9f5c467034e949d9c320899614.png" width="100%"></kbd></p>

<br>

<a id="node-269"></a>

<p align="center"><kbd><img src="assets/fdc8af20a694fb29561d48eb7318090c697eaaad.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là dựa trên ý nghĩa của đạo hàm của hàm số là độ dốc của
> hàm số tại điểm đó, ta có thể tính toán giá trị xấp xỉ của đạo hàm bằng
> cách cho x thay đổi 1 khoảng 2 epsilon `(x-epsilon,` `x+epsilon)` và tính
> khoảng thay đổi của hàm số `f(x+eps)` `-` `f(x-eps)` và tính ra tỉ lệ. Cái này
> không thể dùng trong training vì rất tốn kém nên chỉ dùng để gradient
> check.

<br>

<a id="node-270"></a>

<p align="center"><kbd><img src="assets/a747df033d7b2af5686831fe3f13e896f278a09f.png" width="100%"></kbd></p>

<br>

<a id="node-271"></a>

<p align="center"><kbd><img src="assets/eb6215e15a6e2f99b2fb8ee8fc54f9c53cedd8d7.png" width="100%"></kbd></p>

<br>

<a id="node-272"></a>

<p align="center"><kbd><img src="assets/90af38a4e1b637e88c3662bb1b2a5d5f88942614.png" width="100%"></kbd></p>

<br>

<a id="node-273"></a>

<p align="center"><kbd><img src="assets/6fccc325f229d9b885b272eb13f4eb437bb01f76.png" width="100%"></kbd></p>

<br>

<a id="node-274"></a>

<p align="center"><kbd><img src="assets/866d0bb575b31e89682d65053d0f28d4512e814b.png" width="100%"></kbd></p>

<br>

<a id="node-275"></a>

<p align="center"><kbd><img src="assets/d1eb475dc61a18ff704fe05ce56d37667f5178ab.png" width="100%"></kbd></p>

<br>

<a id="node-276"></a>

<p align="center"><kbd><img src="assets/552af8e570ac86890f96b580147e894688a3027a.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái nói về l2 regularization `-` add thêm l2 loss term và
> cơ bản chỉ là tổng bình phương các params của weight
> matrix của mọi layer. Người ta không tính bias b vào hoặc 
> có cũng chẳng sao lí do như Andrew Ng có giải thích đó là
> có làm thì cũng không còn tác dụng.
>
> Theo Chat GPT thì bias nó chỉ là đảm bảo giúp y có giá trị
> khi feature weight `=` 0 hết, nó không ảnh hưởng đến việc 
> gây model overfit `-` cái mà chỉ là do các feature weight gây ra

<br>

<a id="node-277"></a>

<p align="center"><kbd><img src="assets/4bbca41aaff9ba445f82b0c48aa8ab96d5eb310d.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là như đã biết dropout ở DLSpec, nhưng ở đây nhắc
> nhớ lại rằng nó giúp như ta train một bộ nhiều simple neural
> network để rồi khi dự đoán (test với dropout không áp dụng) thì
> như ta xài ensemble method `-` lấy số đông kết quả của một bộ
> nhiều cái neural net

<br>

<a id="node-278"></a>

<p align="center"><kbd><img src="assets/8914541ffa2ce66b7592f23d908fc4570cfda59a.png" width="100%"></kbd></p>

<br>

<a id="node-279"></a>

<p align="center"><kbd><img src="assets/fad0883d85b0db45edb755a37e0be5bf4913472f.png" width="100%"></kbd></p>

<br>

<a id="node-280"></a>

<p align="center"><kbd><img src="assets/cf7c3fb1df7e31a097af82fa94efc1e09a56ac66.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là thông qua SVD, ta có U là matrix mà mỗi column là
> eigenvector của X'. Từ đó UX' thì ta có các feature mới (các cột
> của matrix UX') kiểu như là linear combination của các feature cũ
> nhưng có tính chất uncorrelated

<br>

<a id="node-281"></a>

<p align="center"><kbd><img src="assets/16b74f99c5347c2b0ca7cff80decdd10977f4292.png" width="100%"></kbd></p>

<br>

<a id="node-282"></a>

<p align="center"><kbd><img src="assets/68832f55aaac8245b6f0342d13ef62e3f4a389d2.png" width="100%"></kbd></p>

<br>

<a id="node-283"></a>

<p align="center"><kbd><img src="assets/245324700ef891d57816e8b8c7e2bfbe2b2e58b1.png" width="100%"></kbd></p>

<br>

<a id="node-284"></a>

<p align="center"><kbd><img src="assets/ab4aecd46b9c2b3261c7d498f31fec473a19b865.png" width="100%"></kbd></p>

<br>

<a id="node-285"></a>

<p align="center"><kbd><img src="assets/7d656f97b5d547f1299cf2fbcbbd83ad3af179a7.png" width="100%"></kbd></p>

<br>

<a id="node-286"></a>

<p align="center"><kbd><img src="assets/1d021113cf6c6d80d1f67a1129a497625ddca96c.png" width="100%"></kbd></p>

<br>

