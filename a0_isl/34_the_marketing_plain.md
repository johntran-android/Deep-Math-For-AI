# 3.4 The Marketing Plain

📊 **Progress:** `0` Notes | `0` Screenshots

---

<a id="node-266"></a>
## 1. Có Quan Hệ Nào Giữa Sale Và Advertising Budget Không?

<br>


<a id="node-267"></a>
### Thì đại khái là bằng cách \\*fit một multi regression model\\* với target

> [!NOTE]
> Thì đại khái là bằng cách \**fit một multi regression model\** với target
> value là sales, predictors là TV, radio, news paper (budget) thì ta có
> thể xây dựng và kiểm tra xem null hypothesis `(beta_Tv` `=` `beta_Radio`
> `=` `beta_News)` có đúng không.
>
> Và bằng cách tính `F-statistic` và nhận xét chỉ số này lớn hơn 1 xa
> bảng 3.6 cho \**F-stat `=` 560 > 1\** và đồng thời (dù không cho biết
> \**p-value\** gắn với `F-stat` ở trên là bao nhiêu nhưng cho biết nó "
> \**essentially zero\**" nên ta có thể kết luận rằng có bằng chứng rõ
> rằng `Null-hypothesis` không đúng, hay nói cách khác phải có tồn tại
> quan hệ giữa sale và advertising (nói chung)

<br>


<a id="node-268"></a>
## 2. Quan Hệ Mạnh Cỡ Nào

<br>


<a id="node-269"></a>
### Đại khái là thông qua RSE và R^2. RSE `=` 1.69 cho thấy sai sót

> [!NOTE]
> Đại khái là thông qua RSE và R^2. RSE `=` 1.69 cho thấy sai sót
> chiếm 12% (chia RSE cho mean của responce `-` sale) và R^2 `=` 89%
> cho thấy model đã explain được `~-` 90% variability của response
> (sale)

<br>


<a id="node-270"></a>
## 3. Kênh Nào Tác Động Đến Sale

<br>


<a id="node-271"></a>
### Bằng cách xem sét các coefficient và `p-value` gắn với `t-statistic` của

> [!NOTE]
> Bằng cách xem sét các coefficient và `p-value` gắn với `t-statistic` của
> mỗi cái, cho thấy chỉ có của Tv và Radios là nhỏ đủ để khẳng định
> có tác động đến sale còn của News thì không

<br>


<a id="node-272"></a>
## 4. Tác Động Của Mỗi Kênh Đến Sale Mạnh Cỡ Nào

<br>


<a id="node-273"></a>
## 5. How Accuracy Predicting Future Sales?

<br>


<a id="node-274"></a>
## 6.is The Relationship Linear?

<br>


<a id="node-275"></a>
## 7. Is There Synergy Among

> [!NOTE]
> 7. IS THERE SYNERGY AMONG
> THE ADVERTISING MEDIA?

<br>

