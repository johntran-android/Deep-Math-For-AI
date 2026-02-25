# ....a

📊 **Progress:** `5` Notes | `18` Screenshots

---

![Image](assets/18a479a3f55ccf6d0bb8bee58d9e5f073539aa94.png)
<a id="node-308"></a>

<p align="center"><kbd><img src="assets/e0a87bea03a54bfee1661270709029b6432e6b5e.png" width="100%"></kbd></p>

> [!NOTE]
> Kinh nghiệm: chỉ đưa vector vào hàm softmax này (tức, là phải
> flatten thành 1d array). Có thể quay lại tìm hiểu tại sao. 
>
> Cách suy nghĩ (ý là lý thuyết, dựa trên phần câu hỏi trước) đã đúng,
> chỉ cần đảm bảo đúng shape là được

<br>

<a id="node-309"></a>

<p align="center"><kbd><img src="assets/ffdff43eca1fd6017092b072872bcb93a5cdae6d.png" width="100%"></kbd></p>

<br>

<a id="node-310"></a>

<p align="center"><kbd><img src="assets/125847e298ac14b3f31496d06e0520cc2c5f6a6e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/125847e298ac14b3f31496d06e0520cc2c5f6a6e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/03d16cefc3897a96ad2dd203dca279601b0918e8.png" width="100%"></kbd></p>

> [!NOTE]
> chỉ cần hiểu rằng, ta xây dựng matrix U_plus (là matrix U' trong phần note trả lời lý thuyết,
> hay trong đề bài là U o,{w1,..wK}. Bằng cách "lấy ra" từ matrix U cho trước, nhờ các index
> mà id của uo đứng đầu, sau đó là K vector uw1, uw2....uwK. các index của các vector
> negative sampling sẽ được tạo bởi một sampling function nhằm đảm bảo các sampling
> word không trùng outer word (để các uw1,...uwK đều khác uo)
>
> Khi đó ta có matrix mà các cột là [uo, uw1, ..uwK], thế thì phải nhân - 1 cho các cột từ 2 trở
> đi vì U_plus là matrix [uo, -uw1, ..-uwK]
>
> Dựa theo công thức đã triển khai ở phần lý thuyết để tính dJ/dvc và dJ/dU_plus Thế thì với
> dJ/dU_plus sẽ có điểm lưu ý là, các cột của nó đương nhiên là  đạo hàm của loss đối với
> ÂM của các vector uw1, uw2...Và thứ hai là các w1,..wK có thể trùng nhau. Thành ra ta sẽ
> cần phải gộp chung lại, cho dễ hiểu thì ví dụ như sau:
>
> giả sử K = 5 và indices vector sẽ có K+1 phần tử, là [3,5,7,5,2,4]. Thì 3 chính là index của
> outer word, cột U[:,3] chính là vector uo. Các số từ 5 trở đi đương nhiên là index  của các
> sampling word. Thế thì số 5 lặp lại 2 lần, để ý cái này.
>
> Sau đó như đã nói ở trên ta sẽ tính ra dJ/dU_plus là matrix (D,K+1) = 3x6 (ví dụ D = 6) vậy,
> để có dJ/dU ta sẽ tạo matrix zeros có kích thước D,V sẵn.
>
> Sau đó, gán vector đầu tiên của dJ/dU_plus (như đã biết, nó sẽ chính là dJ/duo, uo- đang
> nói là cột có index = 3 của U) vào cột index = 3 (cột thứ 4) của dJ/dU.
>
> Rồi, cột thứ 2 và thứ 4 của dU_plus sẽ chính là ÂM của đạo hàm loss đối với cái cột có
> index = 5 matrix U. Tức là từ có index = 5 của vocab được sampling 2 lần, đồng nghĩa
> tham gia 2 lần vào quá trình tính toán, nên đạo hàm của loss đối với (ÂM CỦA) cột này của
> U sẽ  tổng hai cột thứ 2 và 4 của dU_plus (dU_plus[1] và dU_plus[3])
>
> ====
>
> Thành ra ta sẽ làm như sau đối với dJ/dU: 
>
> Sau khi khởi tạo zero matrix, ta sẽ iterate trong các index
>
> gradOutsideVecs = np.zeros((D,V)) 
>
> for i, id in enumerate(indices):
>   # Nếu id đầu tiên  tức là dJ/duo, thì gán CỘNG DỒN nó vào index tương ứng của U
>   # Nhưng từ các id tiếp theo, phải nhân cho -1 trước khi gán CỘNG DỒN  
>   gradOutsideVecs[:, id] += dU_plus[:, i] if i == 0 else -dU_plus[:,i]
>
> Để dùng vectorized, thì ta sẽ nhân -1 cho các cột dU_plus, từ cột thứ 2 trở đi 
> Sau đó dùng function  **np.add.at(gradOutsideVecs, (slice(None), indices), dU_plus)
> để có kết quả tương tự
>
> * Chú ý, cuối cùng phải transpose để dJ/dU về cũng shape với U là (V,D)**

<br>

<a id="node-311"></a>

<p align="center"><kbd><img src="assets/19b0110f7ab7a76a86b4b8f4db49c4aafd4f65a6.png" width="100%"></kbd></p>

> [!NOTE]
> đã pass test case

<br>

<a id="node-312"></a>

<p align="center"><kbd><img src="assets/cf6dfe719da790c6870b15ac8cedeeed36ba84a0.png" width="100%"></kbd></p>

<br>

<a id="node-313"></a>

<p align="center"><kbd><img src="assets/9e27f80d784b1a24e6bbc6ebf34af6e5e752bf0d.png" width="100%"></kbd></p>

<br>

<a id="node-314"></a>

<p align="center"><kbd><img src="assets/4aaf94162e2b86b0e541080d61a854d2eed952d6.png" width="100%"></kbd></p>

<br>

<a id="node-315"></a>

<p align="center"><kbd><img src="assets/59566d647a2d17303ddf3755487c45bc861ac121.png" width="100%"></kbd></p>

<br>

<a id="node-316"></a>

<p align="center"><kbd><img src="assets/e7e3be9ebc41ca03346a8021694d6c0096a083df.png" width="100%"></kbd></p>

> [!NOTE]
> Sgd đơn giản vậy thôi, take value của param bỏ vào f để tính ra loss
> và gradients, dùng gradient * lr để update cho params

<br>

<a id="node-317"></a>

<p align="center"><kbd><img src="assets/5433b1a57c0500830cfedcb4273073650be9870c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5433b1a57c0500830cfedcb4273073650be9870c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/246f77495dbc193ccbec149ba927c725ca3d7322.png" width="100%"></kbd></p>

<br>

<a id="node-318"></a>

<p align="center"><kbd><img src="assets/9abe7b02fe93d22fed12aafaa4534b4be18236b7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9abe7b02fe93d22fed12aafaa4534b4be18236b7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f867eb67ae427831e7052b01c869d1f1e02b2e43.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả cho thấy các từ gần nghĩa nằm gần nhau trong không
> gian

<br>

