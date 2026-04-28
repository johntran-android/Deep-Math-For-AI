# 9.3 Methods Of Evaluating Interval Estimators

📊 **Progress:** `1` Notes | `1` Screenshots

---
<a id="node-812"></a>

<p align="center"><kbd><img src="assets/0eae55c98372c9356603406701388a399e437fa2.png" width="100%"></kbd></p>

> [!NOTE]
> Qua phần này ta sẽ học cách tiêu chí và phương pháp đánh giá các Interval
> Estimator. Dễ hiểu là vì một problem ta có thể có nhiều interval estimator
> nên đương nhiên là ta cần đánh giá xem cái nào tốt hơn cái nào.
>
> Thế thì với set / interval estimator, ta sẽ có hai đặc điểm quan trọng: kích
> thước và coverage probability. Và ta sẽ đương nhiên là muốn kích thước
> nhỏ nhưng độ bao phủ lớn.
>
> Vậy thì, ở đây tác giả nhắc lại cho ta rằng, coverage probability trong phần
> lớn trường hợp, thì là function của θ. Nên không thể dùng nó để so sánh
> được. Do đó ta sẽ dùng confidence coefficient. chính là infimum.
>
> Ý này dễ hiểu thôi. Nhớ lại coverage probability, của một interval estimator
> hay confidence set, là hàm theo θ, defined bởi P_θ(θ ∈ C(**X**)).
>
> Nhưng mình cũng biết, một số confidence set nếu được construct dựa trên
> pivot quantity, Q(**X**, θ) thì nó lại có distribution không phụ thuộc θ. Khi đó,
> coverage probability của confidence set này sẽ là constant theo θ. Đó là các
> case đặc biệt gs nói tới ở đây.
>
> Và ta cũng còn nhớ, định nghĩa của confidence coefficient = inf_θ P_θ(θ ∈
> C(**X**)). và nó sẽ ko còn phụ thuộc θ nữa

<br>

