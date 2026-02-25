# Assignment 2 - Fully Connected Nn

📊 **Progress:** `40` Notes | `93` Screenshots

---
<a id="node-804"></a>

<p align="center"><kbd><img src="assets/75e09db17a2e4d8bc3dc24bf429271b8b61e17b2.png" width="100%"></kbd></p>

<br>

<a id="node-805"></a>

<p align="center"><kbd><img src="assets/431507fbba6621f63344889e2a6e58b2e16e28df.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/431507fbba6621f63344889e2a6e58b2e16e28df.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/61166dcddbd7774afa12603ba74442aaf5c49507.png" width="100%"></kbd></p>

> [!NOTE]
> cái  subtrac_max là tự thêm để thử nghiệm
> hiệu quả của việc có hay không trừ max
> trong hàm softmax

<br>

<a id="node-806"></a>

<p align="center"><kbd><img src="assets/09ae2a025c00d6c9f906db9d09168c63cfaa9359.png" width="100%"></kbd></p>

> [!NOTE]
> Có một chú ý quan trọng để sau này đừng sai: hidden_dims
> sẽ quy định size (còn gọi width, số unit) của hidden layer,
> đương nhiên là quy định luôn số hidden layer. Nhưng phải
> có một layer output nữa.
>
> Vậy, dựa vào input size và hidden_dims ta sẽ init các W,b của 
> hidden layer, sau đó init một W,b của output layer với số output
> là num_classes.
>
> Phần này chưa cần làm BatchNorm nên ko note về nó ở đây

<br>

<a id="node-807"></a>

<p align="center"><kbd><img src="assets/facd2d904b3d527e6569fe7afa66804460b1109b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/facd2d904b3d527e6569fe7afa66804460b1109b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2b5091eec97d64bea03d454c84f708b47c73932a.png" width="100%"></kbd></p>

> [!NOTE]
> Nếu là layer đầu thì input là X, còn sau đó input là output của layer
> trước.
>
> với mỗi hidden layer đều có qua hàm relu, layer cuối thì không 
>
> output của layer cuối chính là scores.
>
> ở đây chưa cần làm BN nên ko nói về BN ở đây

<br>

<a id="node-808"></a>

<p align="center"><kbd><img src="assets/4a4c0effee18d72ef14a90ea94a4b16c58b2fee7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4a4c0effee18d72ef14a90ea94a4b16c58b2fee7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a40f3bbce43aa9af885894bdb553d5f88a0fff3e.png" width="100%"></kbd></p>

> [!NOTE]
> backprop thì nếu là layer cuối thì không backprop qua relu,
> còn lại thì có backprop qua relu

<br>

<a id="node-809"></a>

<p align="center"><kbd><img src="assets/64b1f1df9e2a7556c78a3b5e6c66a27128656053.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/64b1f1df9e2a7556c78a3b5e6c66a27128656053.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e30b7f41155e2d78998303264aecadeaf78744b9.png" width="100%"></kbd></p>

> [!NOTE]
> kết quả cho thấy các  Ini loss (softmax) 10 class là
> -log(10) = 2.3 là ok
>
> relative error đều < e^-7 và đúng là W2 error 1e-5

<br>

<a id="node-810"></a>

<p align="center"><kbd><img src="assets/ec7d2c77974e92576beed204c7c7565fd4173b80.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/319641e81b41701ff188dee86ed37bdcbbb97f62.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ec7d2c77974e92576beed204c7c7565fd4173b80.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/319641e81b41701ff188dee86ed37bdcbbb97f62.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f6b10ff70755dd2141ec34de0b970d5dc180c82a.png" width="100%"></kbd></p>

> [!NOTE]
> tiếp theo họ kêu mình tuning lr, và weight scale sao cho
> training acc đạt 1. Ta sẽ viết một grid search để tìm. Thì
> kết qủa là lr 0.001 thì model đạt 100% training acc

<br>

<a id="node-811"></a>

<p align="center"><kbd><img src="assets/f6dba41c0bbe71e519cae979070e75dbe0c39b2d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f6dba41c0bbe71e519cae979070e75dbe0c39b2d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2fadc3f5ada91d5270b967a61791df1e5d43b533.png" width="100%"></kbd></p>

<br>

<a id="node-812"></a>

<p align="center"><kbd><img src="assets/56968469bf2348d45776a800a0c1e0aa0b4f8f61.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/56968469bf2348d45776a800a0c1e0aa0b4f8f61.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/37ba62f5f85ca6af807f42bf527edf960d88e4a0.png" width="100%"></kbd></p>

> [!NOTE]
> Sau đó làm vậy với 4 hidden layers và câu hỏi đặt ra là
> thấy cái nào nhạy cảm với weight scale hơn

<br>

<a id="node-813"></a>

<p align="center"><kbd><img src="assets/1b869f667d388f0a1365545bed217c232b375016.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/920b7d263f04f599fd923cccde6ad907f427c77e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d15fcb919262d8f263261ab1d6a6c11e630f611b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6ddb3bd7ff182f40b91078f30638f65f764f76ae.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1b869f667d388f0a1365545bed217c232b375016.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/920b7d263f04f599fd923cccde6ad907f427c77e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d15fcb919262d8f263261ab1d6a6c11e630f611b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6ddb3bd7ff182f40b91078f30638f65f764f76ae.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c44eeb938632ef158ec3666a36fc9993d7a1374f.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy trước khi trả lời câu hỏi thì nhìn vào qúa trình thử với các depth, lr,
> weight Scale khác nhau có những nhận định sau:
>
> Nhận xét: khi **3 hidden layers** (4 layer),**lr = 1e-5**, nhận thấy **khi
> weight scale ngày càng lớn thì train acc ngày càng tốt.**
>
> Điều này có thể giải thích là vì khi **weight scale** quá nhỏ,  gây hiện
> tượng **gradient vanishing**, dẫn đến quá trình **training diễn ra rất
> chậm**, vì gradient quá nhỏ, nên sau 20 epoch model học rất ít ->
> underfit. Khi tăng scale lên, dần dần khắc phục hiện tượng này, nên ở
> mức phù hợp model đạt train_acc 100% sau 20 epochs.

> [!NOTE]
> subtract_max = True, ws tăng dần thì acc tốt dần n**hưng quá 1 thì xảy
> ra hiện tượng exploding gradient.**

> [!NOTE]
> thử subtract_max = False để xem nó có cho thấy việc trừ max có tác
> dụng gì hay không thì ở đây chưa thấy khác biệt, ở đây cũng exploding
> khi wc ở mức > 1

> [!NOTE]
> biểu đồ loss cho thấy diverge do exploding gradient

> [!NOTE]
> ws phù hợp trong trường hợp này là 0. 3-1

> [!NOTE]
> ws nhỏ quá gây vanishing gradient, khiến model learn
> chậm,

<br>

<a id="node-814"></a>

<p align="center"><kbd><img src="assets/d026a0b6a68ce48e3e4117f919ab63ec159dac60.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1426b0a2cf8810a880a128d5a50443b0e16351db.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dfb878e50d4446bfe6633101f3c2cf3ac1ee3f28.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/acceb33b933f5a12c9c9b9004523c58572e1f2fa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d0a8b590f2be32957e9c579afd6ef35c084efa45.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d026a0b6a68ce48e3e4117f919ab63ec159dac60.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1426b0a2cf8810a880a128d5a50443b0e16351db.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dfb878e50d4446bfe6633101f3c2cf3ac1ee3f28.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/acceb33b933f5a12c9c9b9004523c58572e1f2fa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d0a8b590f2be32957e9c579afd6ef35c084efa45.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9ba0534e838e8e05f004add4c0699a6ce58154fb.png" width="100%"></kbd></p>

> [!NOTE]
> với **weight scale 0.1 nhỏ, gradient nhỏ model learn chậm**, In
> 30 value cuối để thấy**loss vẫn đang tiếp tục chiều hướng đi
> xuống**, thể hiện model vẫn đang **underfit**

> [!NOTE]
> với weight scale 0.6, model learn tốt, với 30 epoch cuối, cho thấy , loss đã đạt 0

> [!NOTE]
> Khi **weight scale lớn quá (2,3)**, nhận xét thấy: một là**vanishing gradient** do weight lớn
> -> underfit (hình bên trái) hoặc là bị **diverge** (loss trở nên rất lớn, hình bên phải)

> [!NOTE]
> với **weight scale quá nhỏ -> vanishing gradient
> learn chậm, thậm chí không learn**

<br>

<a id="node-815"></a>

<p align="center"><kbd><img src="assets/f73d8e901fc8ae33c52810aa8b83594e9f45273d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2024627e940fd2d71df2c2842312a362b815e778.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b9115551823a3ed51212bc2603731a364ee20def.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f73d8e901fc8ae33c52810aa8b83594e9f45273d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2024627e940fd2d71df2c2842312a362b815e778.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b9115551823a3ed51212bc2603731a364ee20def.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7cbe16f697ffc275bf3d9b3bbd55cbac325eb7ef.png" width="100%"></kbd></p>

> [!NOTE]
> có thể thấy **hiện tượng này lặp lại**với các lr khác 3e-5,
> 6e-5, 1e-4. Tất cả đều là weight scale quá nhỏ thì gây
> vanishing gradient, và cỡ >= 0.1 - 0.6 thì đạt 100%
>
> cụ thể: 
> lr 3e-5, weight scale 0.06 - 94%, 0.1 - 94%, 0.3 - 98%, 0.6 - 100%
> lr 6e-5, weight scale 0.06 - 96%, 0.1 - 100%, 0.3 - 100% 
>
> **nhưng 0.6 thì diverge (loss tăng vọt) (bên trái) hoặc bị lỗi overflow
>
> \/overflow encountered in matmul out = x.reshape(N, -1) @ w + b**\/

> [!NOTE]
> Có phải là diverge ko, **tại sao weight lớn lại gây
> diverge ?**
>
> Đúng là diverge, ta có thể hiểu **diverge** là do
> **gradient lớn** -> nên khi **update params với grad
> lớn** thì cũng**tương tự khi learning rate lớn**
> khiến "đi vọt qua bên kia"
>
> trong note nn part 2 regularization đã nhắc đến việc
> **weight lớn có thể gây hiện tượng network '
> 'explode'** bên cạnh việc nó **gây vanishing
> gradient** liên quan đến activation function lớn local
> grad ~= 0

> [!NOTE]
> hoặc như trong lecture note về weight ini cũng đã
> thấy, W lớn có thể gây **vanishing** nói gọn là**do
> local grad hàm activation**, hoặc gây**exploding
> gradient**do grad đi về bị khuếch đại do nhân với
> activation value  lớn (mà cũng bởi W lớn)

<br>

<a id="node-816"></a>

<p align="center"><kbd><img src="assets/1f86c096685f0bb86cf33c92493520b61624e7c0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1f86c096685f0bb86cf33c92493520b61624e7c0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/52a6aa973c0781db6bd6b2a398ee36c47a62ac77.png" width="100%"></kbd></p>

> [!NOTE]
> với depth 3, lr 0.0006, 0.001 có thể thấy cũng có hiện tượng trên,
> nhưng weight scale lúc này chỉ nên ở 0.01(lúc nãy là 0.1, 0.6) lên
> 0.03 là đã diverge rồi

<br>

<a id="node-817"></a>

<p align="center"><kbd><img src="assets/8d3e43e2428bece473704a96de5aad44e02a11ed.png" width="100%"></kbd></p>

> [!NOTE]
> với lr lớn hơn 0.01 thì đã trở nên quá
> lớn, weight scale bao nhiêu cũng
> diverge

<br>

<a id="node-818"></a>

<p align="center"><kbd><img src="assets/c298131609e8edfb273407f89d7155fbd29f66f8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/52048e4acd550df760519dbbceeb862382f1949d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e1128afb108a1bc1ca49cd7daa8ce5338b1141b0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dd87664d3ba39fff25659a7278ffd636810b1851.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c298131609e8edfb273407f89d7155fbd29f66f8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/52048e4acd550df760519dbbceeb862382f1949d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e1128afb108a1bc1ca49cd7daa8ce5338b1141b0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dd87664d3ba39fff25659a7278ffd636810b1851.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/22a14e5ed5cb20ac292124e7c129f053a04db7d2.png" width="100%"></kbd></p>

> [!NOTE]
> Depth = 4, lr 3e-4, ws: 0.01 - 0.03, train acc: 24% 100%

> [!NOTE]
> Depth = 4, lr 6e-4, ws: 0.01 - 0.03 - 0.06, train acc: 32% 100% 8%

> [!NOTE]
> Depth = 4, lr 1e-3, ws: 0.01 - 0.03 - 0.06, train acc: 42% 100% 8%

> [!NOTE]
> có thể thấy với depth = 4, nn **nhạy cảm** với weight scale hơn depth = 3
>
> Nguyên nhân có thể hiểu là vì nó sâu hơn, nên kiểu như tác động của việc
> scale trở nên lớn hơn (scale nhiều lần hơn)
>
> Do đó, nó nhạy cảm hơn, dễ mất ổn định hơn khi ini weight chỉ khác đi một
> chút là performance đã khác rất nhiều

> [!NOTE]
> Depth = 3, lr 3e-4, ws: 0.01 - 0.03, train acc: 90% 100%

> [!NOTE]
> Depth = 3, lr 6e-4, ws: 0.006 - 0.01, train acc: 92% 100%

<br>

<a id="node-819"></a>

<p align="center"><kbd><img src="assets/d1036d01c44075289438cd4d2f8f3360e2bd8630.png" width="100%"></kbd></p>

<br>

<a id="node-820"></a>

<p align="center"><kbd><img src="assets/2e09492c0181509e09a8eb3fbfa49819090b8e91.png" width="100%"></kbd></p>

> [!NOTE]
> kế tiếp ta sẽ làm cái SGD Momentum, trước đó xem qua
> optim.py chứa các function giúp thực hiện việc
> optimizing (dùng gradient để thay đổi parameters)
>
> Có thể thấy sgd - vanilla gradient descent, sẽ update 
> weight bằng cách trừ cho gradient * learning rate.

<br>

<a id="node-821"></a>

<p align="center"><kbd><img src="assets/06091718c60e8cf58c325a0786c1d4da3ca760ea.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/06091718c60e8cf58c325a0786c1d4da3ca760ea.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7c988266915c8c2904e465d7668fe2e52b741fb2.png" width="100%"></kbd></p>

> [!NOTE]
> nhiệm vụ là làm cái sgd_momentum update. Dựa trên
> công thức mà làm thôi, còn nguyên lý của cái này thì
> trong note đã hiểu

<br>

<a id="node-822"></a>

<p align="center"><kbd><img src="assets/7e7b2cb641bb21393c3abc94c506cfc620841a2f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7e7b2cb641bb21393c3abc94c506cfc620841a2f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b3a20e0900c28abe0d6912dd0ede0f6698ba0c7d.png" width="100%"></kbd></p>

> [!NOTE]
> Train 5 hidden layers neural net cho thấy sgd
> momentum converge nhanh hơn. Ở đây ta train
> với 4000 sample chứ ko phải 50 nên không đạt
> train acc 100% được (overfit)

<br>

<a id="node-823"></a>

<p align="center"><kbd><img src="assets/dc285dc2d2dbc89a8c2ccef3e9daf0600520b8d9.png" width="100%"></kbd></p>

> [!NOTE]
> error e-8 là ok

<br>

<a id="node-824"></a>

<p align="center"><kbd><img src="assets/22e6e323ebda500cd2420ae967421537c991d141.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo là làm
> RMSProp và Adam

<br>

<a id="node-825"></a>

<p align="center"><kbd><img src="assets/8bfbb681c12e5c9571807869da44baee10b0b6d1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8bfbb681c12e5c9571807869da44baee10b0b6d1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3f46439f2d5b9b244beccae8eb0ee3db728c365a.png" width="100%"></kbd></p>

> [!NOTE]
> cứ theo công thức mà làm thôi

<br>

<a id="node-826"></a>

<p align="center"><kbd><img src="assets/7d3510af0f24acd185ba7722c1da99bc3e251ec8.png" width="100%"></kbd></p>

> [!NOTE]
> Pass!

<br>

<a id="node-827"></a>

<p align="center"><kbd><img src="assets/13906e5671bcd3cd1c3442861fd5a4a1b5749bdb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/611b8e545ae49fa7f55f6f120d78b59b03c9e086.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/13906e5671bcd3cd1c3442861fd5a4a1b5749bdb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/611b8e545ae49fa7f55f6f120d78b59b03c9e086.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e85aad587a5b81929adaa2566a79b2f216738d8d.png" width="100%"></kbd></p>

> [!NOTE]
> cứ theo công thức mà làm thôi, chú ý t là number of iteration,
> đương nhiên là sẽ += 1 mỗi lần

<br>

<a id="node-828"></a>

<p align="center"><kbd><img src="assets/f41d0cdc77029e06220d3c2492ed516f8118c0dc.png" width="100%"></kbd></p>

> [!NOTE]
> Pass!

<br>

<a id="node-829"></a>

<p align="center"><kbd><img src="assets/9fc2d00880dc1471d596e648a8e0016f08884799.png" width="100%"></kbd></p>

<br>

<a id="node-830"></a>

<p align="center"><kbd><img src="assets/1a53816fc51b7d8ced6e968747913df1780c4d0c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1a53816fc51b7d8ced6e968747913df1780c4d0c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c3954aef5a58650fc027967a680cf654ff3298c6.png" width="100%"></kbd></p>

> [!NOTE]
> có thể thấy rõ Adam converge sớm nhất, sau đó là
> rmsprop, tệ nhất là vanilla sgd

<br>

<a id="node-831"></a>

<p align="center"><kbd><img src="assets/57b614ce46ed76c16e46aac519408e40f4b30118.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/57b614ce46ed76c16e46aac519408e40f4b30118.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7395a40be81bfd78b15a0e19c8779734738ab7e4.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi là khi John train với AdaGrad thì thấy hiện tượng parameters
> được update rất chậm, khiến learning trở nên rất lâu. Vậy tại sao lại thế
> và Adam có bị vậy không?
>
> -> Dựa vào việc hiểu nguyên lý của AdaGrad là nó cố gắng cân bằng
> việc update các param bằng cách điều chỉnh learning rate cho từng
> param thay vì dùng chung một learning rate.
>
> Bằng cách **chia lr của mỗi params** cho một giá trị **grad_square
> được cộng dồn trong quá khứ**. Với ý tưởng là nếu param A được
> update nhiều hơn param B thì learning rate cho param A sẽ nhỏ hơn
> của B.
>
> Thế thì nhược điểm của cái này là **grad_square cứ cộng dồn nên lớn
> lên mãi, sẽ khiến lr ngày càng bị bóp nhỏ lại**.
>
> RMSProp (cũng như Adam) khắc phục bằng cách dùng một **average
> weight decay**đối với grad_square giúp grad_square đại khái là không
> cứ lớn mãi dẫn đến vấn đề của AdaGrad

<br>

<a id="node-832"></a>

<p align="center"><kbd><img src="assets/1e88c5e8bdf49b787a7bf5bb460e007d33a32c79.png" width="100%"></kbd></p>

> [!NOTE]
> để train dc một FC model có val acc > 50% thì ta sẽ qua làm
> BatchNorm và Dropout trước, quay lại đây sau. Vì hai technique
> này sẽ giúp giảm overfit

<br>

