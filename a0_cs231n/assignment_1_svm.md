# Assignment 1 SVM

📊 **Progress:** `14` Notes | `25` Screenshots

---
<a id="node-272"></a>

<p align="center"><kbd><img src="assets/553a694248d060156454f7818c9f8e4bd6d51872.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta sẽ làm phiên bản fully vectorized khi công thức tính
> loss function với SVM, cũng như là analytic gradient. Rồi check
> (gradient check) với numerical gradient. Tune learning rate và
> regularization. Optimize với SGD

<br>

<a id="node-273"></a>

<p align="center"><kbd><img src="assets/01392dfbda04972f9512fd9d7fcc929d1f539e3b.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ dụng utils function người ta chuẩn bị
> sẵn để load CIFAR10 dataset

<br>

<a id="node-274"></a>

<p align="center"><kbd><img src="assets/916da903384d5f9c012f1e5e571dcbba22c0d8d8.png" width="100%"></kbd></p>

> [!NOTE]
> Nhờ utils function load dataset CIFAR10 từ thư mục, nó đã có sẵn
> training + testing dataset. Trong function đó đã thực hiện động tác
> reshape để training tensor sẽ có shape là 50.000 x 32 x 32 x 3

<br>

<a id="node-275"></a>

<p align="center"><kbd><img src="assets/1d808179e6602403f3dfbf817cbc72c3db6c38fb.png" width="100%"></kbd></p>

<br>

<a id="node-276"></a>

<p align="center"><kbd><img src="assets/c544831c03bfeb0b839de7b7e95652ce2d8568e1.png" width="100%"></kbd></p>

> [!NOTE]
> In vài data sample ra xem thử

<br>

<a id="node-277"></a>

<p align="center"><kbd><img src="assets/3fc7fa55caaf97a3ab4be2fb2cf4cdde42b874f1.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với 50000 cái hình trong training, người ta
> dành 1000 cái cuói làm validatiaon sét. Rồi lại lấy trong
> 49000 cái của training sét, random 500 cái dùng làm dev
> sét.
>
> Rồi trong 10000 cái của tét sét gốc thì ta chỉ lấy 1000 cái
> đầu thôi

<br>

<a id="node-278"></a>

<p align="center"><kbd><img src="assets/528b3eac4db76351e866dd6686adc92f894893e7.png" width="100%"></kbd></p>

> [!NOTE]
> Cơ bản là flatten các image đang là 32,32,3 thành
> vector có 32x32x3 dimensions

<br>

<a id="node-279"></a>

<p align="center"><kbd><img src="assets/c6b849c0a468445d80c298348250b9d300b1b5b3.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là lúc này X_train có shape là 49000,3072 để normalization,
> họ tính mean của từng feature, đương nhiên là theo từng cột của
> matrix, nên axis sẽ là 0. Sau đó trừ mọi giá trị của tensor X cho
> mean.
>
> Còn bước hai đó là bias trick, cơ bản là tạo vector cột toàn số 1 có
> shape là 49000x1 rồi dùng numpy's hstack. = horizontal stack để
> stack lại,

<br>

<a id="node-280"></a>

<p align="center"><kbd><img src="assets/91bb851d5b181e45f554f2fc0ae7297435bff114.png" width="100%"></kbd></p>

<br>

<a id="node-281"></a>

<p align="center"><kbd><img src="assets/b63b88702195a74c9fe418af80a6452b5b9d9435.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là hoàn thành
> function tính svm loss

<br>

<a id="node-282"></a>

<p align="center"><kbd><img src="assets/03726d2ee57c120318e18f6c5a43776939e1da2a.png" width="100%"></kbd></p>

<br>

<a id="node-283"></a>

<p align="center"><kbd><img src="assets/e38652ab9d8a14e0bc9b7eab285f84f413901d36.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e38652ab9d8a14e0bc9b7eab285f84f413901d36.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0b582135e39be6c42aea85e1ee348d1037c48aab.png" width="100%"></kbd></p>

<br>

<a id="node-284"></a>

<p align="center"><kbd><img src="assets/47a9caf948faa0e47e7ef7fe40335ead6bdf6afb.png" width="100%"></kbd></p>

> [!NOTE]
> Tại sao lại "cộng dồn" khi tính đạo hàm của L w.r.t W với
> loss là trên 1 batch các data sample lại là tổng (đúng hơn là
> trung bình) các đạo hàm của loss trên từng data sample w.
> r.t W. Vì đạo hàm của tổng là tổng đạo hàm vậy thôi

<br>


<a id="node-285"></a>
## Inline Question 1

> [!NOTE]
> Inline Question 1
>
> It is possible that once in a while a dimension in the gradcheck will not match exactly. What could
> such a discrepancy be caused by? Is it a reason for concern? What is a simple example in one
> dimension where a gradient check could fail? How would change the margin affect of the frequency
> of this happening? Hint: the SVM loss function is not strictly speaking differentiable
>
> Y𝑜𝑢𝑟𝐴𝑛𝑠𝑤𝑒𝑟:  fill this in.

> [!NOTE]
> Quay lại sau

<br>

<a id="node-286"></a>

<p align="center"><kbd><img src="assets/ad082898f11616aac2b744d6bf4eac372ce37333.png" width="100%"></kbd></p>

<br>

<a id="node-287"></a>

<p align="center"><kbd><img src="assets/4ce3c00a96cab7d88b4c8d14d9df5f8535eb3300.png" width="100%"></kbd></p>

> [!NOTE]
> Correct! Viết hàm tính loss SVM vectorized
>
> Chú ý phải có regularizer (ban đầu mình quên cộng), còn
> cơ bản cách làm là đúng khi so với cách làm của solution
> tham khảo.
>
> Nhìn hơi khác ở chỗ là trong cách làm tham khảo,  họ
> reshape vector y_hat_true (mà mình gọi là correct_scores)
> bằng cái syntax: [:, np.newaxis] còn mình reshape bằng
> function reshape: .reshape(N,-1)
>
> Sau đó thì cũng lấy S (họ đặt là Y_hat) trừ đi y_hat_true và
> cộng delta.
>
> Một chỗ khác nữa, đó là mình bỏ bớt delta thừa bằng cách
> trừ margins vector cho 1 còn họ thì dùng cách - 1 thật ra
> cũng y chang.

<br>

<a id="node-288"></a>

<p align="center"><kbd><img src="assets/ae5d9314d0cdb0c9136ac699433a0237e2bc525d.png" width="100%"></kbd></p>

<br>

<a id="node-289"></a>

<p align="center"><kbd><img src="assets/273987ce0e98d6d5b78105fc4642deb3fd1032b9.png" width="100%"></kbd></p>

<br>

<a id="node-290"></a>

<p align="center"><kbd><img src="assets/5626178baf5200aa08b3859cef1559881b024885.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5626178baf5200aa08b3859cef1559881b024885.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b79a286423b9f53a6ff69293fe0fb55ab00da8ec.png" width="100%"></kbd></p>

> [!NOTE]
> Giảm xuống còn 1 vòng lặp nhưng chú ý là phải có
> dL_regularizer/dW nếu Loss có regularizer loss term

<br>

<a id="node-291"></a>

<p align="center"><kbd><img src="assets/bbd41868ae00dfe2158f997c99b1e33a5c8c405b.png" width="100%"></kbd></p>

> [!NOTE]
> Qua các bước tính ra margin, và khử đi vị
> trí tương ứng với correct class, tạm gọi là matrix I

<br>

<a id="node-292"></a>

<p align="center"><kbd><img src="assets/436cd6f04577d9147beb0e0775d39808620167ee.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là X (transposed) matmul với I thì
> kết qủa matrix (shape DxC) thì nó chính là
> tổng dW "đối với / tính trên các incorrect class

<br>

<a id="node-293"></a>

<p align="center"><kbd><img src="assets/4837737b9e84b6cfc974a45f4d5218972d52121b.png" width="100%"></kbd></p>

<br>

