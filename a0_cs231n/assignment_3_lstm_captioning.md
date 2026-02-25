# Assignment 3 - Lstm Captioning

📊 **Progress:** `13` Notes | `51` Screenshots

---
<a id="node-1253"></a>

<p align="center"><kbd><img src="assets/25f25bd0d9891605f2591b7b9eecafce36c02eaf.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/25f25bd0d9891605f2591b7b9eecafce36c02eaf.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a9eb5b62adf91e8176e7f82df1d61aeac1a9bae8.png" width="100%"></kbd></p>

> [!NOTE]
> ở đây lại không bị cái vụ lỗi import như ở RNN captioning, cũng như
> trong notebook đó ta cũng sẽ dùng COCO dataset

<br>

<a id="node-1254"></a>

<p align="center"><kbd><img src="assets/c5d86b6c4f2a6e9984a91f7785f8ac9fc7ac56a0.png" width="100%"></kbd></p>

> [!NOTE]
> mô tả lại cách "làm" LSTM, như đã biết, nhưng chú ý là ở đây trong cs231n,
> khác với DLSpec hay NLPSpec, ta sẽ "gộp" các matrix W (cho các gate) thành
> matrix lớn, để rồi khi tính, cơ bản là ta tính một lượt từ xt, ht-1, ra luôn 4 vector
> dưới dạng một vector a dài 4H, sau đó cắt ra và apply các function sigmoid /
> tanh khác nhau để có các gate vector.
>
> Sau đó thì tính ct, ht thì biết rồi.

<br>

<a id="node-1255"></a>

<p align="center"><kbd><img src="assets/90efb332c1c0e97b6bd0f94365951f18115fefb1.png" width="100%"></kbd></p>

<br>

<a id="node-1256"></a>

<p align="center"><kbd><img src="assets/efe5ef82229b0c9dee148ed1fa42da393b8677bf.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/efe5ef82229b0c9dee148ed1fa42da393b8677bf.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1d3768f18d6428f719b7dffb5d0b6b3b9b805816.png" width="100%"></kbd></p>

> [!NOTE]
> forward tương đối đơn giản, theo mô tả đã rất rõ
> không cần phải note gì nhiều

<br>

<a id="node-1257"></a>

<p align="center"><kbd><img src="assets/b965cacb1ece1751812cc5aeff0e86a9b12e74ab.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fb908a611df29524049fab12dfc82eecf49c3ac4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5f042f5816e3234f9013e0b46920d3aae5c91092.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/061e1fd29955e8557efa894416ef0d13580c10aa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/027b6edb55df8a7aaf345bb66481f2600f5c299f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/34025e63a4c5f361b8c1d7a19912879a0e446343.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9512dc78b627b6fb8773bc461c34a9e48c800e85.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/648f30261cc1fb29c0928b46373fb88bf4f04a2e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b965cacb1ece1751812cc5aeff0e86a9b12e74ab.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fb908a611df29524049fab12dfc82eecf49c3ac4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5f042f5816e3234f9013e0b46920d3aae5c91092.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/061e1fd29955e8557efa894416ef0d13580c10aa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/027b6edb55df8a7aaf345bb66481f2600f5c299f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/34025e63a4c5f361b8c1d7a19912879a0e446343.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9512dc78b627b6fb8773bc461c34a9e48c800e85.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/648f30261cc1fb29c0928b46373fb88bf4f04a2e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/11f322313ad34dc68ab3d13bd35ac4d294e7c4b3.png" width="100%"></kbd></p>

> [!NOTE]
> dnext_c input chỉ là 1 nhánh, ct có tham gia tính ht,nên phải có 
> gradient của nhánh đó nữa.
>
> dnext_c += dnext_h * cache['o'] * (1-np.tanh(cache['next_c'])**2) 
>
> dprev_c = dnext_c * cache['f']

> [!NOTE]
> df = dnext_c * cache['prev_c']   # (N,H)*(N,H) = (N,H)

> [!NOTE]
> di = dnext_c * cache['g']  # (N,H)*(N,H) = (N,H)

> [!NOTE]
> dg = dnext_c * cache['I']  # (N,H)*(N,H) = (N,H)

> [!NOTE]
> do = dnext_h * np.tanh(cache[' next_c']) #(N,H)*(N,H)

<br>

<a id="node-1258"></a>

<p align="center"><kbd><img src="assets/6f63750a822c5bbdd48eeb2737e649e0c7c242f6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6f63750a822c5bbdd48eeb2737e649e0c7c242f6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7769dc44e519ca4bf109fc032c4f4a330e22f8b8.png" width="100%"></kbd></p>

> [!NOTE]
> You should see errors on the
> order of e-7 or less.

<br>

<a id="node-1259"></a>

<p align="center"><kbd><img src="assets/9b9f8c63cc8796711718410961755ad0b8773601.png" width="100%"></kbd></p>

<br>

<a id="node-1260"></a>

<p align="center"><kbd><img src="assets/8209e1b9a15d0559e33559fa07f1b9cc8039ed68.png" width="100%"></kbd></p>

> [!NOTE]
> You should see an error on
> the order of e-7 or less

<br>

<a id="node-1261"></a>

<p align="center"><kbd><img src="assets/81dcc5c6f6daf75a7ffb93ebc9ce96b58144eec9.png" width="100%"></kbd></p>

> [!NOTE]
> Hoàn toàn tương tự cái rnn_backward()

<br>

<a id="node-1262"></a>

<p align="center"><kbd><img src="assets/2cd69f9904a51efc1a6bd0c25d3344efaac07a53.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2cd69f9904a51efc1a6bd0c25d3344efaac07a53.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4c6986302b6ca8f1574f52cdb7194250d362995f.png" width="100%"></kbd></p>

<br>

<a id="node-1263"></a>

<p align="center"><kbd><img src="assets/1e78df196745134514a631776282ec6dd0ad6d0b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1e78df196745134514a631776282ec6dd0ad6d0b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/73f9ce97898dbb34532224392075f6d77436ef97.png" width="100%"></kbd></p>

<br>

<a id="node-1264"></a>

<p align="center"><kbd><img src="assets/41ec0615cbf0099fb9558784361bc1ca15adfc45.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/41ec0615cbf0099fb9558784361bc1ca15adfc45.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a78496e912c5c76844c1649bb4106b91d8c4e4e8.png" width="100%"></kbd></p>

> [!NOTE]
> Update thêm case lstm

<br>

<a id="node-1265"></a>

<p align="center"><kbd><img src="assets/da6056f226f1123bd84e9d4cbe9457fcb25f1aee.png" width="100%"></kbd></p>

> [!NOTE]
> update thêm case của
> lstm cho sample()

<br>

<a id="node-1266"></a>

<p align="center"><kbd><img src="assets/534251266806e8c07400efb7a9666f12e1952b8a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/534251266806e8c07400efb7a9666f12e1952b8a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8469ffe7fc9405bf78bc546042fecbe8faf78782.png" width="100%"></kbd></p>

<br>

<a id="node-1267"></a>

<p align="center"><kbd><img src="assets/7b03c422479e7ba61b9783f8f66e29d961b26638.png" width="100%"></kbd></p>

<br>

<a id="node-1268"></a>

<p align="center"><kbd><img src="assets/263aa026d8920e1163ecae8c29db995ce0182920.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ab7f85cc4412e01fc5881b5538d223774153e7f3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/263aa026d8920e1163ecae8c29db995ce0182920.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ab7f85cc4412e01fc5881b5538d223774153e7f3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4827199345866d5226a6b871375204548dc107e7.png" width="100%"></kbd></p>

<br>

<a id="node-1269"></a>

<p align="center"><kbd><img src="assets/9f949a9388beb8bbc0e8a9358b98b326c56a8c7d.png" width="100%"></kbd></p>

<br>

