# 2.4 (2) Applied

📊 **Progress:** `6` Notes | `9` Screenshots

---
<a id="node-119"></a>

<p align="center"><kbd><img src="assets/74d18c7b4f1ce6825a358d0a70a14b31b83999a7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/74d18c7b4f1ce6825a358d0a70a14b31b83999a7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e81fb2d86f9b5f7f146c956f0be6f6acb8b59c4a.png" width="100%"></kbd></p>

<br>

<a id="node-120"></a>

<p align="center"><kbd><img src="assets/c2e4b1bc1a5d499519b4cd0791c27abf6fbf0ca6.png" width="100%"></kbd></p>

> [!NOTE]
> a. Load data: 
>
> college `=` `read.csv("~/Desktop/Learn` ML/****STAT/College.csv", 
> stringsAsFactors `=` T)
> View(college)

<br>

<a id="node-121"></a>

<p align="center"><kbd><img src="assets/7873ee0cc5587be0c680e2d598d8f0cab55da192.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta sẽ delete cái cột name, vì nó không chứa số liệu
> mà nó chỉ là tên trường tuy nhiên thông tin này lại hữu ích sau
> này nên mới dùng cách này để tạo một column gọi là row.
> names column. Và R sẽ không treat cái column này như data.
>
> rownames(college) `=` college[,1]
>
> Có thể thấy cái cột mới cũng có tên trường nhưng có màu khác
>
> Sau đó ta sẽ delete cái column chứa tên trường ban đầu đi

<br>

<a id="node-122"></a>

<p align="center"><kbd><img src="assets/edabc7fc43f9bfa3c40839ce7bc67c52520247c4.png" width="100%"></kbd></p>

> [!NOTE]
> > college `=` `college[,-1]`
> > View(college)
>
> Ở đây ta chọn trong table gốc mọi hàng và mọi cột trừ cột số 1

<br>

<a id="node-123"></a>

<p align="center"><kbd><img src="assets/b946a15c09b273dd065f860ae515268071640742.png" width="100%"></kbd></p>

> [!NOTE]
> c.i Gọi summary để xem
> summary của dataset

<br>

<a id="node-124"></a>

<p align="center"><kbd><img src="assets/35688687236cc894e6a06262506afe9f4d4be6ad.png" width="100%"></kbd></p>

> [!NOTE]
> c.ii: pairs(college[, 1:10], col `=` 'blue')

<br>

<a id="node-125"></a>

<p align="center"><kbd><img src="assets/cf848978b638b83f56079c0c5d1b196552e8a530.png" width="100%"></kbd></p>

> [!NOTE]
> (c.iii) plot(college$Outstate, college$Private)

<br>

