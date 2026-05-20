# Chap 10 Asymtotic Evaluation

📊 **Progress:** `3` Notes | `3` Screenshots

---

<a id="node-848"></a>
## 10.1 Point Estimation

<br>

<a id="node-849"></a>

<p align="center"><kbd><img src="assets/eed3dc9dc2d7bb4ca79c376e49e19bf28ce745b7.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là bữa giờ ta xét các hành vi của các quy trình suy luận trong
> bối cảnh là finite-sample, tức là mẫu có số lượng hữu hạn. Chapter
> này sẽ xem xét tính asymptotic -  tính chất mô tả hành vi của quy trình
> khi kích thước mẫu tăng lên infinite.
>
> Ta sẽ đánh giá tính chất này của cả 3 quy trình suy luận chính: point
> estimation, hypothesis testing và interval estimation. Đặc biệt tập
> trung vào các phương pháp liên quan đến maximum likelihood

<br>

<a id="node-850"></a>

<p align="center"><kbd><img src="assets/578b5873903a6d43f4a0103016bcaa888bf9e3c9.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là, gs nói sơ về giá trị của cái này là nó khiến việc tính toán trở nên
> đơn giản hóa khi ta cho phép số lượng mẫu tăng lên indefinite.
>
> Có những cách đánh giá trở nên bất khả thi khi xét trong bối cảnh
> finite-sample nhưng trở nên khả thi khi xét trong bối cảnh infinte bao gồm
> các technique nổi tiếng như bootstrap và M-estimation.

<br>

<a id="node-851"></a>

<p align="center"><kbd><img src="assets/ffb6bcb7d331819d71c5853ef4d216ad2a52d8c5.png" width="100%"></kbd></p>

> [!NOTE]
> Xét vấn đề đánh giá tiệm cận với phương pháp suy luận thuộc loại point 
> estimation. Đầu tiên nói về tính chất nhất quán (consistency)
>
> Thì đại ý là, cái này nó nền tảng đến nỗi nếu một estimator mà inconstent
> thì có thể phải đặt câu hỏi là có đáng để dùng không.
>
> Thế thì đầu tiên, gs nói trong bối cảnh đánh giá tiệm cận, thật ta ta nên
> hiểu là ta sẽ  **XÉT MỘT CHUỖI CÁC ESTIMATOR**, **CHỨ KHÔNG PHẢI
> LÀ MỘT CÁI DÙ CHO KHI NÓI THÌ TA NÓI "CONSISTENT ESTIMATOR**"
>  trông có vẻ như là tính chất của một estimator đơn lẻ.
>
> Tức là hình dung, với sample X1,X2,...Xn thì kiểu như ta dùng cùng một
> quy trình inference để xây dựng một chuỗi các point estimator với kích
> thước mẫu tăng dần. W1(X1), W2(X1,X2),....Wn(X1,...Xn)
>
> ví dụ, lấy Xbar đi (nó là point estimator cho population mean như đã biết)
>
> thì ta có Xbar1(X1) = X1, Xbar2(X1,X2) = (X1+X2)/2, Xbar_n(X1,..Xn)
> = (Σi=1:n Xi) / n
>
> Mình ghi Xbar1(X1) là hoàn toàn hợp lệ, vì gs Casella trong mấy chương
> trước đã nói, Xbar, hay S^2 thật ra chỉ là ghi cho gọn, ghi rõ phải là Xbar(**X**)
> hay S^2(**X**) để thể hiện nó là function của sample **X**

<br>

