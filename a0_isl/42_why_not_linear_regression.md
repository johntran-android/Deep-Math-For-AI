# 4.2 Why Not Linear Regression?

📊 **Progress:** `0` Notes | `2` Screenshots

---

<a id="node-297"></a>
## Why?

<br>


<a id="node-298"></a>
### Đại khái lí do đầu tiên là việc chuyển categories thành

> [!NOTE]
> Đại khái lí do đầu tiên là việc chuyển categories thành
> number để dùng cho việc train mô hình linear
> regression đã vô tình gán thứ tự cho các categories vốn
> chẳng có thứ tự gì, khi đó mỗi kiểu gán sẽ cho ra một
> mô hình khác nhau, từ đó đưa ra những dự đoán khác
> nhau cho một sample.
>
> Trừ khi các categories có thể nằm theo thứ tự và
> khoảng cách giữa chúng được phép cho rằng như nhau
> thì xài linear regression được (ví dụ Easy, Medium,
> Hard)

<br>


<a id="node-299"></a>
### Còn nếu có 2 class, và ta gán hai class là 1 và 0 thì thật

> [!NOTE]
> Còn nếu có 2 class, và ta gán hai class là 1 và 0 thì thật
> ra vẫn không hoàn toàn vô lý nếu dùng linear regression.
> Vì thứ nhất khi ta không gặp phải vấn đề thứ tự của các
> class id thay đổi kết quả dự đoán. Thứ hai là giá trị
> prediction number (tức beta1*x+beta0) có thể mang ý
> nghĩa là giá trị xác suất thô (crude probability), nói vậy là
> bởi những giá trị này cũng tuân theo thứ tự tương ứng
> với xác suất (như số tính ra nhỏ thì đúng là xác suất nhỏ,
> số tính ra lớn thì đúng ứng với xác suất lớn)
>
> Tuy nhiên, bị vấn đề là giá trị này có thể ra âm, có thể ra
> lớn hơn 1, nên không hoàn toàn có thể kiến giải theo xác
> suất được.

<p align="center"><kbd><img src="assets/d4bdf90f3cb782a53a4e815a77e537d9e64a2a0b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d4bdf90f3cb782a53a4e815a77e537d9e64a2a0b.png" width="100%"></kbd></p>

<br>


<a id="node-300"></a>
### Tóm lại là có hai lí do không thể áp dụng l.r cho bài toán

> [!NOTE]
> Tóm lại là có hai lí do không thể áp dụng l.r cho bài toán
> classification. 1 là nếu có 2 classes thì việc tính
> y^=X*beta rồi coi nó như Pr(Y=1|X) không thỏa đáng vì
> nó có thể ra giá trị âm hoặc lớn hơn 1.
>
> Còn nếu có nhiều hơn 2 classes thì không có cách nào
> convert class label thành numerical giúp dùng cho bài
> toán linear regression vì nó tạo ra sai lệch trong quan hệ
> giữa các thứ tự.

<br>

