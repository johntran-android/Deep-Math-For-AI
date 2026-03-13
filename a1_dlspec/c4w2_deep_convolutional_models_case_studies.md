# C4w2_deep Convolutional Models: Case Studies

📊 **Progress:** `57` Notes | `130` Screenshots

---

Discover some powerful practical tricks and methods used in deep CNNs, straight from the research papers, then apply transfer learning to your own deep CNN.
**Learning Objectives**
 • Implement the basic building blocks of ResNets in a deep neural network using Keras
 • Train a state-of-the-art neural network for image classification
 • Implement a skip connection in your network
 • Create a dataset from a directory
 • Preprocess and augment data using the Keras Sequential API
 • Adapt a pretrained model to new data and train a classifier using the Functional API and MobileNet
 • Fine-tine a classifier's final layers to improve accuracy

<a id="node-1309"></a>
## Why look at case studies?

<br>


<a id="node-1310"></a>
### 1 Case studies of effective convolutional neural networks

> [!NOTE]
> 1 Case studies of effective convolutional neural networks
>
> 2 Importance of looking at **case studies** to gain intuition and
> confidence in building effective convnets
>
> 3 **Transferability of neural network architecture** across different
> computer vision tasks
>
> 4 **Potential satisfaction in reading research papers** from the field
> of computer vision
>
> 5 Outline of the next few videos: classic networks such as
> **LeNet**-5, **AlexNet**, and **VGG**; **ResNet**, a deep 152-layer neural
> network with interesting tricks; and the **Inception** neural network
>
> 6 Benefits of learning from these examples, even for those not
> working in computer vision, as ideas are **cross-fertilizing** into
> other disciplines.

<br>

<a id="node-1311"></a>

<p align="center"><kbd><img src="assets/fa693128a883fc13ae71d36fe0f534443baec714.png" width="100%"></kbd></p>

  <br>


<a id="node-1312"></a>
## Classic Networks

<br>


<a id="node-1313"></a>
### Xem qua 1 số classic ConvNet

> [!NOTE]
> Xem qua 1 số classic ConvNet
> Nhận xét chung là nó thường có cấu trúc là 
> **Conv - Pool - Conv - Pool ...Conv - Pool- FC - FC.. -FC - Sofmax 
> Qua các layer thì nH, nW giảm, nC tăng**

<br>

<a id="node-1314"></a>

<p align="center"><kbd><img src="assets/93584e037b7617079f39aea042c6e276d21e1530.png" width="100%"></kbd></p>

> [!NOTE]
> Một số nhận xét:
> Qua các layer:
> nH, nW giảm, nC tăng
> Conv - Pool  - Conv - Pool
> **60k** params

  <br>

<a id="node-1315"></a>

<p align="center"><kbd><img src="assets/d2f01ba5f4bad74f80d4203cc7ee1fab19233a5e.png" width="100%"></kbd></p>

> [!NOTE]
> Một số nhận xét:
> Giống như LeNet như bigger
> **~60 mils** params

  <br>

<a id="node-1316"></a>

<p align="center"><kbd><img src="assets/5a893342f6a4c2036bd27b00c424a64ae4e21963.png" width="100%"></kbd></p>

> [!NOTE]
> Một số nhận xét:
> Giống như Alexnet nhưng bigger
> **~138 mils** params

  <br>


<a id="node-1317"></a>
## Resnet

<br>


<a id="node-1318"></a>
### Training **very deep** neural networks is difficult due to **vanishing** and **exploding**

> [!NOTE]
> Training **very deep** neural networks is difficult due to **vanishing** and **exploding**
> gradient problems.
>
> **Skip connections** are a solution to these problems as they **allow activations from
> one layer to be fed to another layer much deeper** in the network, allowing the
> building of **ResNets**.
>
> **ResNets** are built from **residual blocks** which consist of a main path of layers and
> a shortcut that allows information to flow directly to deeper layers.
>
> Adding these residual blocks to a plain network turns it into a ResNet and allows
> for the training of **much deeper neural networks without significant loss** in
> performance.
>
> ResNets **help with the vanishing and exploding gradient problems**, allowing the
> training of **much deeper neural networks**without **compromising performance**.

<br>

<a id="node-1319"></a>

<p align="center"><kbd><img src="assets/f2c98ffd6eacb077c896a1b164454d610dab4513.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là Residual block nó có thêm cái 
> '**Shortcut /Skip Connection**' chuyển a[l] vào step tính a[l+2]
>
> a[l+2] = g(z[l+2] + a[l])
>
> Khi vì lí do nào đó, params khiến**z[l+1] = 0** có thể do hiện tượng
> gradient exploding / vanishing thì a[l+2] sẽ bằng g(a[l]) = max(0, a[l]) (reLU) = a[l]
> từ đó đại khái là **không bị mất thông tin**

  <br>

<a id="node-1320"></a>

<p align="center"><kbd><img src="assets/0275bb9615e9634c65a8a426a39d999a2a2c7eca.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là RestNet giúp khắc phục vấn đề**nhiều layer thì
> performance giảm** do Gradient Vanishing / Exploding từ đó
> **cho phép train very deep network**

  <br>


<a id="node-1321"></a>
## Why Resnets Work

<br>


<a id="node-1322"></a>
### 1 **Residual Networks (ResNets)** work well in terms of training because they

> [!NOTE]
> 1 **Residual Networks (ResNets)** work well in terms of training because they
> can be made **deeper without decreasing performance** on the training set.
>
> 2 Making neural networks **deeper** can **hurt the ability to train them well** on
> the training set, which is a prerequisite to doing well on the holdout, test
> sets or during deployment.
>
> 3 ResNets include **residual blocks**with **shortcut connections**, making it
> easy for these extra layers to **learn the identity function**.
>
> 4 **The identity function is easy to learn**, so the addition of extra layers in the
> neural network **doesn't hurt** its ability to perform **as well as a simpler
> network without these extra layers**.
>
> 5 **Same convolutions** are often used in ResNets to **ensure** that the
> dimension of the **input**and**output**of the layers**are equal**, making it easier
> to **carry out** the **shortcut connection** and the addition of two equal
> dimension vectors.

> [!NOTE]
> Sure, here's a more detailed answer with indexed main ideas:
>  1 ResNets are deep neural networks that work well because they can be made deeper without significantly hurting performance on the training set, which is a prerequisite for good performance on the test set.
>  2 The reason ResNets can be made deeper without hurting performance is because of the use of residual blocks, which include a skip connection that allows the network to learn the identity function more easily.
>  3 Let's look at an example to see how the skip connection works in a ResNet block. Suppose we have an input X feeding into a neural network that outputs activation a[l]. We want to make the network deeper by adding two extra layers to output a[l+2]. We add a residual block with a skip connection to achieve this. If we assume all activations are greater than or equal to zero, then a[l+2] can be expressed as g(w[l+2] * a[l+1] + b[l+2] + a[l]), where g is the activation function and w[l+2] and b[l+2] are the weights and biases for the added layers.
>  4 If we use L2 regularization to shrink the weights, w[l+2], and assume b[l+2] = 0 for simplicity, then we can see that if w[l+2] = 0, the entire term w[l+2] * a[l+1] + b[l+2] disappears, leaving just a[l] as the input to the activation function. If g is the ReLU function, which outputs only non-negative numbers, then g(a[l]) = a[l]. This means that the identity function is easy for the residual block to learn, and it can easily make a[l+2] equal to a[l].
>  5 Adding two extra layers with a residual block does not significantly hurt performance because the residual block can easily learn the identity function. However, the goal is not just to avoid hurting performance but to improve it. If the added layers can learn something useful, then the network can do even better than simply learning the identity function.
>  6 In very deep plain networks without residual connections, it becomes difficult to learn even the identity function, which is why adding more layers can actually hurt performance. ResNets work because they make it easy for the extra layers to learn the identity function, and from there they have a chance of learning something useful.
>  7 Another detail worth noting is that the dimensions of z[l+2] and a[l] must be the same for the skip connection to work. This is why same convolutions are often used in ResNets to preserve the dimensions of the inputs and outputs of each layer, making it easier to carry out the skip connection and the addition of the two vectors. If the dimensions are different, an extra matrix must be added to make the dimensions match.

<br>

<a id="node-1323"></a>

<p align="center"><kbd><img src="assets/c455eefeb431149f19cfa78df9ba53f6792e0509.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nếu regularization (ví dụ vậy) bóp W, b (l+1) bằng 0 thì a[l+2] sẽ
> bằng g(a[l]) và = a[l] vì g là reLU 
>
> Có nghĩa là ..nếu gradient vanishing xảy ra, thì ..không bị làm sao cả,
>  a[l+2] chỉ đơn giản là a[l+2] quay lại bằng a[l] thay vì =0
> (ý ổng nói network rất dễ learn được identity function đại khái là 
> vậy)   
>
> Bằng 0 có nghĩa là không học được gì nữa (hiểu đại khái vậy, vì nếu
> a[l+2] = 0 thì mấy cái layer sau = 0 hết)
>
> Đo đó, với 'Skip connection' thì đầu tiên là **add thêm extra layer, hay
>  tạo very deep network sẽ không gây hại** đến model.
>
> Và từ ko gây haị thì chỉ có thể nâng lên thành improve hệ
> thống, ý nói nếu tệ nhất mà chỉ ko gây hại thì chắc chắn phải có thể
> improve rồi.
>
> Ngược lại, nếu không có Skip connection, thì việc add thêm layer rất dễ
> dẫn đến việc hệ thống bị stuck khi W bị = 0

> [!NOTE]
> Đại khái là để a[l+2] bằng size với a[l], ta nhân thêm a[l] với 1 matrix **Ws**. Ws
> có thể **trainable** hoặc **fixed value** Hoặc với ConvNet thì dùng **Same
> padding** để giữ size của input và output

  <br>

<a id="node-1324"></a>

<p align="center"><kbd><img src="assets/fe449e70323f546b101e48c7a9f47c046efa842b.png" width="100%"></kbd></p>

> [!NOTE]
> Một ví dụ 
> Conv conv conv pool, conv conv .. conv pool
> ..
>
> Sau pool (size nó giảm) thì dùng Ws để khôi phục:
> Chưa rõ lắm nhưng đại khái là vậy

  <br>

<a id="node-1325"></a>
- Sure, here's a more detailed answer with indexed main ideas:    1 **ResNets** are deep neural networks that work well because they can be made **deeper** without **significantly hurting performance** on the **training** **set**, which is a **prerequisite** for good performance on the test set.  2 The reason **ResNets** can be made deeper without hurting performance is because of the use of **residual blocks**, which include a **skip connection** that allows the network to **learn the identity function** more easily.  3 Let's look at an example to see how the skip connection works in a ResNet block. Suppose we have an input X feeding into a neural network that outputs activation **a[l]**. We want to make the network deeper by adding two extra layers to output **a[l+2]**. We add a **residual block** with a **skip connection** to achieve this. If we assume all activations are greater than or equal to zero, then a[l+2] can be expressed as **g(w[l+2] * a[l+1] + b[l+2] + a[l])**, where g is the activation function and w[l+2] and b[l+2] are the weights and biases for the added layers.  4 If we use **L2 regularization to shrink the weights**, w[l+2], and assume b[l+2] = 0 for simplicity, then we can see that if w[l+2] = 0, the **entire term w[l+2] * a[l+1] + b[l+2] disappears**, leaving just **a[l]** **as the input to the activation function**. If g is the ReLU function, which outputs only non-negative numbers, then **g(a[l]) = a[l].** This means that the **identity function** is **easy for the residual block to learn**, and it can easily make **a[l+2] equal to a[l].**  5 Adding two extra layers with a residual block **does not significantly hurt performance** because the **residual block can easily learn the identity function**. However, the goal is not just to avoid hurting performance but to improve it. **If the added layers can learn something useful**, then the **network can do even better than simply learning the identity function.**  6 In **very deep plain networks** without residual connections, it becomes **difficult to learn even the identity function**, which is why **adding more layers can actually hurt performance**. **ResNets** **work because they make it easy for the extra layers to learn the identity function**, and from there they **have a chance of learning something useful.**  7 Another detail worth noting is that the **dimensions of z[l+2] and a[l] must be the same** for the skip connection to work. This is why s**ame convolutions are often used in ResNets to preserve the dimensions of the inputs and outputs of each layer**, making it **easier to carry out the skip connection** and the addition of the two vectors. **If the dimensions are different, an extra matrix must be added to make the dimensions match.**
  <br>


<a id="node-1326"></a>
## Networks In Networks And

> [!NOTE]
> NETWORKS IN NETWORKS AND
> 1X1 CONVOLUTIONS

<br>


<a id="node-1327"></a>
### 1 Using a **one-by-one convolution** can help in designing content

> [!NOTE]
> 1 Using a **one-by-one convolution** can help in designing content
> architectures.
>
> 2 A one-by-one convolution can **multiply an image by a single number**
> or **perform a more complex operation**.
>
> 3 A one-by-one convolution takes each position in an input volume and
> applies a **fully connected neural network** to it.
>
> 4 A one-by-one convolution is sometimes called a "**network in network**"
> and has been influential in other neural network architectures.
>
> 5 One way to use a one-by-one convolution is to **shrink the number of
> channels** in an input volume.
>
> 6 A one-by-one convolution **adds nonlinearity** and **allows for learning a
> more complex function in a network**.

<br>

<a id="node-1328"></a>

<p align="center"><kbd><img src="assets/7bbfe71a60520b0b0ec7cca22ebed4cfd73aa048.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7bbfe71a60520b0b0ec7cca22ebed4cfd73aa048.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/929a5471b9abe6745def5bdf69b97ea61190e6fd.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái nó giống như apply 1 fully connected cho mỗi position của volumn (nhìn hình sẽ hiểu).

  <br>

<a id="node-1329"></a>

<p align="center"><kbd><img src="assets/1fb7109697aa5527b7360b516e74db71d63e3032.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là 1x1 Conv có thể có công dụng giúp giảm n_c, giống  cách
> như Pool giúp giảm n_h, n_w
>
> Ví dụ xài 32 cái filer 1x1x192 sẽ giúp tạo output 28x28x32
>
> Còn không (nếu không muốn giảm n_c - giữ nguyên 1x1x192) thì nó
> cũng giúp tăng hiệu quả học tập lên

  <br>


<a id="node-1330"></a>
## Inception Network Motivation

<br>

<a id="node-1331"></a>

<p align="center"><kbd><img src="assets/aa6663c9cb77ede077d5083e4a0de385e43c6936.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là khỏi phải suy nghĩ giữa chọn filter size là 1x1, hay 3x3, hay
> 5x5 rồi dùng **conv** hay **pool**, thì cứ dùng hết:
>
> 64 cái filter 1x1 ra cục xanh lá 28x28x64
> 128 cái filter 3x3 same padding -> 28x28x128
> 32 cái filter 5x5 same padding -> 28x28x32
> 32 cái max pooling -> 28x28x32
>
> Xong stack lại và để cho máy tính nó**\/tự quyết định sẽ dùng cái nào\/**

> [!NOTE]
> *Cái 1x1 ghi là 28x28x64 thì đương nhiên phải hiểu là
> **xài 64 cái filter có size 28x28x192.** Tương tự 128 cái
> filter 3x3x192 32 cái filter 5x5x192

<br>

<a id="node-1332"></a>

<p align="center"><kbd><img src="assets/a4008aacd3ef1bfc8b893131e26c40a954cc1f9e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9990b4ec5ce0f513b4f5252fafab21ea01353e01.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a4008aacd3ef1bfc8b893131e26c40a954cc1f9e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9990b4ec5ce0f513b4f5252fafab21ea01353e01.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f0defa5a474b9d605ea2af4e86da678ffc2ea041.png" width="100%"></kbd></p>

> [!NOTE]
> Tại sao lại nhân 5x5x192 đã hiểu: Mỗi lần convol là nó tính 5x5 phép
> nhân rồi cộng lại - là cho 1 lớp, có nc lớp -> 5x5xnc phép nhân

<br>

<a id="node-1333"></a>

<p align="center"><kbd><img src="assets/91fd54848e7dcd0bd7655f9761f13bacb6a02991.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là bằng cách dùng 1x1 Convolution, số phép tính cần thiết giảm đi 1/10
>
> 28x28x192 - 32 cái filter 5x5 same padding -> **28x28x32: 120m params**
> thì nếu dùng 2 bước với 1x1 filter
>
> 28x28x192 - dùng 16 cái 1x1 -> 28x28x16 - dùng 32 cái 5x5 same padding -> **28x28x32: thì chỉ có 12m params**

<br>


<a id="node-1334"></a>
## Inception Network

<br>


<a id="node-1335"></a>
### 1 The inception module takes the activation from a previous layer as input

> [!NOTE]
> 1 The inception module takes the activation from a previous layer as input
> and **outputs multiple feature maps of different sizes.**
>
> 2 The inception network is made up of a **series of inception blocks**, which
> consist of **multiple inception modules** concatenated together.
>
> 3 The inception network **repeats these inception blocks** in different positions
> in the network.
>
> 4 The inception network also includes **additional side branches**, which **use
> hidden layers to make predictions** alongside the main output layer.
>
> 5 The side branches help to **ensure that the features computed are useful
> for making predictions**.

<br>

<a id="node-1336"></a>

<p align="center"><kbd><img src="assets/67444609abf2c4af969116bfc63a04705b98014e.png" width="100%"></kbd></p>

> [!NOTE]
> Ứng dụng ý tưởng ở lecture trước, Inception module sử dụng đủ loại filter, chú ý là như đã nói, dùng 2 bước
> với 16 cái 1x1(x192) và 3x3(x16) gọi là bottle-neck layer thay vì 3x3(x192) same padding để giảm số params

  <br>

<a id="node-1337"></a>

<p align="center"><kbd><img src="assets/2278ea081c7e9bc6ea78c74106479b12a868ebfd.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái (Inception network) là nhiều Inception module
>
> Additional side branched: Dùng softmax tại các hidden layer, đại khái là
> cũng generate well predicting và giảm overfitting
>
> Term "Inception" đúng là đến từ phim Inception
>
> Cái trong hình dưới là GoogleNet

  <br>


<a id="node-1338"></a>
## Mobilenet

<br>


<a id="node-1339"></a>
### 1 Introduction to **MobileNets**, a **convolutional neural network architecture** used for

> [!NOTE]
> 1 Introduction to **MobileNets**, a **convolutional neural network architecture** used for
> computer vision that can run on devices with **low computational power**.
>
> 2 Need for **MobileNets** as other neural networks are **computationally expensive.**
>
> 3 Explanation of the **normal convolution process** used in other neural networks.
>
> 4 **Computational cost** of normal convolution determined.
>
> 5 Introduction of **depthwise separable convolution** used in **MobileNets**.
>
> 6 Explanation of how the **depthwise convolution** works.
>
> 7 Calculation of the computational cost of depthwise convolution.

<br>

<a id="node-1340"></a>

<p align="center"><kbd><img src="assets/b15644d1d6ec0a0fc8598c88c99359f123f960bc.png" width="100%"></kbd></p>

  <br>

<a id="node-1341"></a>

<p align="center"><kbd><img src="assets/40a26383deec7290c07089abf00aef1e61d81318.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là tính lại xem Convolution thông
> thường cần bao nhiêu phép tính

> [!NOTE]
> Trong Normal Conv: Mỗi lần cái filter convol để tính ra 1 số cho 1
> dimension của output, nó tính cho từng dimension của input sau
> đó nó **cộng lại cho nên kết quả là chỉ còn 1 channel, nhưng có
> nc cái filter thì thành ra cục output có nc channel**6x6x3 -  1 filter 3x3x3 -> 4x4x**1** 
> x **5 cái** filter thành ra **4x4x5**

  <br>

<a id="node-1342"></a>

<p align="center"><kbd><img src="assets/78afe9e5f022bbae31975ddc633c0fb50dc2338d.png" width="100%"></kbd></p>

> [!NOTE]
> Còn depthwise thì
> nó khác 1 chút

  <br>

<a id="node-1343"></a>

<p align="center"><kbd><img src="assets/080541d40529093c23f4dbcdfb456ba758d4eb06.png" width="100%"></kbd></p>

> [!NOTE]
> **DepthWise** đại khái là ở mỗi lần filter convol nó sẽ tính riêng từng
> dimension, và không cộng lại để 'ép' lại thành 1 channel.

  <br>

<a id="node-1344"></a>

<p align="center"><kbd><img src="assets/b1b43d9f6c1733849ca5dc6ee387261b2e30fe26.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e5b4d7ed8495a4a44395b014ce2a626240f6ec1c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b1b43d9f6c1733849ca5dc6ee387261b2e30fe26.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e5b4d7ed8495a4a44395b014ce2a626240f6ec1c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b5976e3aea5a1458c5c234b6e442f98fa1f9acbb.png" width="100%"></kbd></p>

  <br>

<a id="node-1345"></a>

<p align="center"><kbd><img src="assets/efb39219cd2679990eca1c6a661d4b9c8324c01a.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả là sau khi convol với 1 filter nó
> vẫn giữ số channel của input (chứ không
> ép lại thành 1 channel)
>
> 6x6x**3** - 1 **(chỉ một)** filter 3x3x3 -> 4x4x**3**

  <br>

<a id="node-1346"></a>

<p align="center"><kbd><img src="assets/1313e3090148b3774e26fab8381ae2c408abbc86.png" width="100%"></kbd></p>

> [!NOTE]
> Sau đó cái cục này được convol qua 5 cái
> 1x1x3 filter để thành ra **4x4x5** giống như
> output của normal convolution '

  <br>

<a id="node-1347"></a>

<p align="center"><kbd><img src="assets/ef87e00030f0829a38ffbec54b07d55048a97114.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/115f607577c6d2c77df6a9bfab0be51e42a8d707.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ef87e00030f0829a38ffbec54b07d55048a97114.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/115f607577c6d2c77df6a9bfab0be51e42a8d707.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d225263a9f602bf94604c0f75592488fb3e2e00f.png" width="100%"></kbd></p>

  <br>

<a id="node-1348"></a>

<p align="center"><kbd><img src="assets/b1b6c31439bf9965e3e1506ecc1d996c17aeecc0.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là cho thấy cùng là từ input 6x6x3 -> output 4x4x5 nhưng
> dùng **Depth-wise Separable Convolution** giúp giảm **~10x**computational expensive so với **normal convolution**

  <br>

<a id="node-1349"></a>

<p align="center"><kbd><img src="assets/bf9d3dd303945291dcd2a4315fc44b0ad63a5cad.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng nói đúng ra là phải vẽ icon thành nhiều lớp hơn 3x3xnc
> nếu nc = 8 chẳng hạn phải vẽ thành 8 lớp nhưng quy ước cứ giữ icon
> như vậy cho gọn và mình tự hiểu là được

  <br>


<a id="node-1350"></a>
## Mobilenet Architecture

<br>


<a id="node-1351"></a>
### Main ideas:  1 **MobileNet** is a neural network that uses a **depthwise**

> [!NOTE]
> Main ideas:  1 **MobileNet** is a neural network that uses a **depthwise**
> **separable** **convolutional operation** to **reduce computational cost.**
> 2 The **MobileNet v1** architecture uses a block comprising a **depthwise
> convolutional operation** and a **stack** of **13 layers** to make a
> **classification** prediction.
>
> 3 **MobileNet v2** is an **improvement** over the basic MobileNet
> architecture that **includes a residual connection** and an**expansion
> layer**before the **depthwise** convolution and the **pointwise** convolution.
>
> 4 MobileNet v2 repeats the block **17 times** and uses **pooling**,
> **fully-connected**, and **softmax layers** to make a classification prediction.
>
> 5 The MobileNet v2 **bottleneck block** **increases the size** of the
> representation within the block and **projects it back down to a smaller
> set of values**, **reducing the amount of memory** **needed** to store
> activations from layer to layer.

<br>

<a id="node-1352"></a>

<p align="center"><kbd><img src="assets/c58796de7f435e82d79c3ffdfb378e90f0fa288a.png" width="100%"></kbd></p>

  <br>

<a id="node-1353"></a>

<p align="center"><kbd><img src="assets/2c652c385140e61ded2fe3db8df4466b29a5789c.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nó expand ra để tính toán được nhiều feature hữu
> ích hơn, sau đó co lại để đáp ứng điều kiện dung lượng bộ nhớ
> hạn hẹp -> Tốt hơn MobileNet v1 mà vẫn đáp ứng bộ nhớ nhỏ
>
> Expand: nxnx3 - 18 cái filter 1x1x3 -> nxnx18
>
> Depth-wise: nxnx18 - 1 cái filter n_hxn_w x18 **depth-wise** -> nxn18
>
> (Khúc này có lẽ phải hiểu là dùng same padding để giữ size n
> và n_h, n_w ổng cũng không nói tới nhưng cũng không quan trọng)
>
> Projection: nxnx18 - 3 cái 1x1x18 -> nxn3

> [!NOTE]
> Đại khái như vậy là đủ hiểu
> MobileNet v2 rồi, muốn xem
> kĩ hơn để biết chi tiết thì đọc
> Paper của Sandler

> [!NOTE]
> Từ nxnx3 -> nxnx18 thì ta dùng 18 cái filter 1x1x3
>
> Còn từ nxnx18 về lại nxnx3 thì dùng 3 cái filter 1x1x18

  <br>


<a id="node-1354"></a>
## Efficientnet

<br>


<a id="node-1355"></a>
### 1 The benefits of using **computationally efficient neural networks** like

> [!NOTE]
> 1 The benefits of using **computationally efficient neural networks** like
> MobileNet V1 and V2.
>
> 2 The **challenge** of adapting neural networks to **different devices** with
> varying **computational resources**.
>
> 3 The concept of **EfficientNet** and how it can be used to **scale up** **or
> down** neural networks based on a **device's computational budget**.
>
> 4 The three factors that can be adjusted to scale up or down neural
> networks:**image resolution**, network **depth**, and layer **width**.
>
> 5 The importance of **finding the right trade-off between image
> resolution, network depth, and layer width** to optimize neural network
> performance for a specific device.
>
> 6 The usefulness of **open source implementations of EfficientNet** for
> adapting neural network architectures to specific devices.

<br>

<a id="node-1356"></a>

<p align="center"><kbd><img src="assets/2ce02bfae022122c40657ac012c96d54ce5c3f18.png" width="100%"></kbd></p>

> [!NOTE]
> Dùng higher resolution image

  <br>

<a id="node-1357"></a>

<p align="center"><kbd><img src="assets/530cee19a137e084534a4423c55336ff4d7df0c0.png" width="100%"></kbd></p>

> [!NOTE]
> Dùng deeper network

  <br>

<a id="node-1358"></a>

<p align="center"><kbd><img src="assets/a765c04011a99b541815d45deb9c86fd0ce7875d.png" width="100%"></kbd></p>

> [!NOTE]
> Dùng wider network

  <br>

<a id="node-1359"></a>

<p align="center"><kbd><img src="assets/ddfe3acfe8aa99855eba3b784cada6d34ce7ed84.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi là: Với cụ thể 1 giới hạn về khả năng tính toán, làm
> sao để chọn được / quyết định được r, d, w? Hay nói cách
> khác là  scale cái nào lên và giữ nguyên cái nào hoặc scale
> cùng lúc cả 3 cái lên với tỉ lệ bao nhiêu? -> **Loot at
> OpenSource implementation of EfficientNet**

  <br>

<a id="node-1360"></a>

<p align="center"><kbd><img src="assets/53a40da6667bc9ef14a46ea1f62093aba16baa97.png" width="100%"></kbd></p>

> [!NOTE]
> Build N.N for mobile devices, embedded devices

  <br>


<a id="node-1361"></a>
## Using Open-source

> [!NOTE]
> USING OPEN-SOURCE
> IMPLEMENTATION

<br>


<a id="node-1362"></a>
### 1 **Practical advice** on using neural network and **ConvNet** **architectures**

> [!NOTE]
> 1 **Practical advice** on using neural network and **ConvNet** **architectures**
>
> 2 Importance of **open-source implementations** for **replicating** neural
> networks
>
> 3 **Difficulty** of replicating neural networks without **open-source
> implementations**
>
> 4 Benefits of using **open-source implementations**, such as **faster
> implementation and transfer learning**
>
> 5 Using **GitHub** to find open-source implementations

<br>

<a id="node-1363"></a>

<p align="center"><kbd><img src="assets/87ed45a68aa57d068ed6e53aea8ad48896508d06.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nên search (GitHub) và xài cái người ta làm

  <br>


<a id="node-1364"></a>
## Transfer Learning

<br>


<a id="node-1365"></a>
### 1 **Pre-training** and**transfer learning** can help build computer vision

> [!NOTE]
> 1 **Pre-training** and**transfer learning** can help build computer vision
> applications faster.
>
> 2 Many **pre-trained models are available for download**, which have
> already been **trained on large public datasets**.
>
> 3 Using transfer learning, **pre-trained weights can be used as a starting
> point** for a new task.
>
> 4 **Frozen** **layers** in pre-trained models can be used to **extract features** that
> can be used for a new classification problem.
>
> 5 **Pre-computing features from frozen layers** can help speed up training
> with a small dataset.
>
> 6 **Fewer layers can be frozen** if there is a **larger labeled dataset** available.
>
> 7 If there is a **lot of data** available, **the whole pre-trained network can be
> used for training.**
>
> 8 There are different ways to initialize the last few layers of the network
> for the new classification problem.
>
> 9 The number of layers frozen and trained on top can be adjusted based
> on the available dataset size.

<br>

<a id="node-1366"></a>

<p align="center"><kbd><img src="assets/6fb1a00e42bedaf32914cf32b7194896f9cd110d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là:  Nếu có ít data, cứ giữ nguyên hidden layers, và train cái layer cuối
> thôi. **Precompute** đại khái là (từ feature x của mình **tính output của layer cuối
> trước với cái n.n của người ta - như 1 function**) để khi chạy G.D để training layer
> cuối của mình thì khỏi phải làm bước tính toán này (forward propagation)
>
> Nếu có nhiều data hơn thì freeze mấy layer đầu thôi, train mấy layer cuối thậm chi
> train lại hết, coi các weight đã train của họ như initialization

  <br>

<a id="node-1367"></a>

<p align="center"><kbd><img src="assets/b3b1d6196d6223de24cf5df7128a27e0ba14914c.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng nói Transfer learning hầu như là cái phải
> làm, trừ khi mình có rất rất nhiều data thì mới làm từ
> đầu

  <br>


<a id="node-1368"></a>
## Data Augmentation

<br>


<a id="node-1369"></a>
### 1 **Computer vision** task often **requires more data** to improve performance.

> [!NOTE]
> 1 **Computer vision** task often **requires more data** to improve performance.
>
> 2 **Data augmentation** is a **commonly used technique** to improve the
> performance of computer vision systems.
>
> 3 **Mirroring** and **random cropping** are frequently used data augmentation
> techniques.
>
> 4 **Color shifting** is another commonly used data augmentation technique.
>
> 5 The motivation behind color shifting is to make the learning algorithm
> more robust to changes in image color.
>
> 6 **PCA Color Augmentation** is a specific implementation of color shifting.
>
> 7 **Loading images from a hard disk using a CPU** thread is a common
> implementation of data augmentation in practice.

<br>

<a id="node-1370"></a>

<p align="center"><kbd><img src="assets/17b07d7f7a43ad5aa24ffe61fd78077010be5ed5.png" width="100%"></kbd></p>

  <br>

<a id="node-1371"></a>

<p align="center"><kbd><img src="assets/40024b159191bac301a5b39578697bef23849447.png" width="100%"></kbd></p>

  <br>

<a id="node-1372"></a>

<p align="center"><kbd><img src="assets/dcd3ca87e4cffc289b979a04d40272e0da45e2f7.png" width="100%"></kbd></p>

  <br>


<a id="node-1373"></a>
## State Of Computer Vision

<br>


<a id="node-1374"></a>
### 1 Deep learning has been successfully applied to various problems, including

> [!NOTE]
> 1 Deep learning has been successfully applied to various problems, including
> computer vision.
>
> 2 **Computer vision is a complex problem**, and **deep learning requires a large
> amount of data to achieve good performance.**
>
> 3 There is often a **trade-off** between the **amount of data available** and **the need
> for hand-engineering** in machine learning.
>
> 4 The computer vision literature has historically**relied more on
> hand-engineering**due to **limited data availability**, but with the **increase in data**
> sets, the **use of hand-engineering has decreased**.
>
> 5 **Object detection**, a subset of computer vision, has **smaller data sets** and
> therefore requires more **complex algorithms** and **specialized components.**
> 6 **Transfer learning** is a technique that can help in cases where there is **limited
> data.**
> 7 Researchers in computer vision are enthusiastic about **achieving high
> performance on standardized benchmark** data sets and competitions.

<br>

<a id="node-1375"></a>

<p align="center"><kbd><img src="assets/6621e325e8cde649dcd26b5d2629a8a4a29c8c19.png" width="100%"></kbd></p>

  <br>

<a id="node-1376"></a>

<p align="center"><kbd><img src="assets/663f5053eff50f1865a45db9fb4cc65a4998f637.png" width="100%"></kbd></p>

  <br>

<a id="node-1377"></a>

<p align="center"><kbd><img src="assets/9946b6f3937e969037ee9ca4cb09ba99e94f19a5.png" width="100%"></kbd></p>

  <br>


<a id="node-1378"></a>
## Quiz

<br>

<a id="node-1379"></a>

<p align="center"><kbd><img src="assets/fb4a048e9bd4ba1a4f092a1aa5958ae166454168.png" width="100%"></kbd></p>

<br>

<a id="node-1380"></a>

<p align="center"><kbd><img src="assets/9a3352ecf4a5451a810bc0a4597b9def063ebe51.png" width="100%"></kbd></p>

<br>

<a id="node-1381"></a>

<p align="center"><kbd><img src="assets/d76bfb23efa7157651bdd578ec439227fa210ab0.png" width="100%"></kbd></p>

<br>

<a id="node-1382"></a>

<p align="center"><kbd><img src="assets/b59fa8cfc8a1b1cf0057e2defc572ca85e62c54d.png" width="100%"></kbd></p>

> [!NOTE]
> a[l+2] = g(z[l+2] + a[l]) (a[l] bỏ trong activation
> function luôn)
>
> vì g hay dùng ReLU nên nếu z[l+2] = 0 thì a[l+2] =
> max(0, a[l]) = a[l]

<br>

<a id="node-1383"></a>

<p align="center"><kbd><img src="assets/542763356ff54137aff0235bf4969dea4229e759.png" width="100%"></kbd></p>

<br>

<a id="node-1384"></a>

<p align="center"><kbd><img src="assets/7d3c4f5af44cca116c43d8dbbc0d301527833140.png" width="100%"></kbd></p>

<br>

<a id="node-1385"></a>

<p align="center"><kbd><img src="assets/458ede98cd09f41349f6b4390dfbb9654b78a265.png" width="100%"></kbd></p>

<br>

<a id="node-1386"></a>

<p align="center"><kbd><img src="assets/5029654213e947148e97d982dfdcce58b6f42c0c.png" width="100%"></kbd></p>

<br>

<a id="node-1387"></a>

<p align="center"><kbd><img src="assets/fc7fddaa4aa3ef078312a92b1b79fad0c3307f74.png" width="100%"></kbd></p>

<br>

<a id="node-1388"></a>

<p align="center"><kbd><img src="assets/21d5d98791ebb71143a60694803cd944561c59a3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/21d5d98791ebb71143a60694803cd944561c59a3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b7f9dad35b79b6a05bbc3b8cc1512798edc5633b.png" width="100%"></kbd></p>

<br>


<a id="node-1389"></a>
## Programming Assignment: Residual Networks

<br>


<a id="node-1390"></a>
### • Implement the basic building blocks of ResNets in a deep

> [!NOTE]
> • Implement the basic building blocks of ResNets in a deep
> neural network using Keras
>
> • Put together these building blocks to implement and train a
> state-of-the-art neural network for image classification
>
> • Implement a skip connection in your network
>
> For this assignment, you'll use Keras.

<br>

<a id="node-1391"></a>
- Residual Networks
  <br>

    <a id="node-1392"></a>
    <p align="center"><kbd><img src="assets/bcb36b2e6c1abd9d4ca0b9842bfa180e31e82533.png" width="100%"></kbd></p>
    <br>

<a id="node-1393"></a>
- 1 - Packages
  <br>

    <a id="node-1394"></a>
    <p align="center"><kbd><img src="assets/213df9a4af12ea7f05b6aceaeac67debf6bb68ad.png" width="100%"></kbd></p>
    <br>

<a id="node-1395"></a>
- 2 - The Problem of Very Deep Neural Networks:  Đại khái là vấn đề Gradient Vanishing - params về 0 rất nhanh  khiến model stop learning Hoặc / Exploding - params trở nên rất lớn
  <br>

    <a id="node-1396"></a>
    <p align="center"><kbd><img src="assets/95f136e5158ac957ddcbbcc2f597dcd2618f9003.png" width="100%"></kbd></p>
    <br>

<a id="node-1397"></a>
- 3 - Building a Residual Network:  Nhắc lại rằng RestNet không những giúp giải quyết vấn đề Vanishing Gradient mà còn giúp tăng performance của network  Có hai loại block trong ResNet là **Identity** block và **Convolutional** block
  <br>

    <a id="node-1398"></a>
    <p align="center"><kbd><img src="assets/312e8ee62a1d79a48ea76671f54ca9acffb6e5b6.png" width="100%"></kbd></p>
    <br>

<a id="node-1399"></a>
- 3.1 - The Identity Block:  Đại khái là các step để tạo nên ResNet's identity block  Nói đến việc sẽ thêm 1 bước BatchNorm để tăng tốc training, chỉ cần  một dòng code với Keras.  Và trong bài này mình sẽ skip 2 layer chứ không phải 1 như trong lecture
> [!NOTE]
> Có cái vụ
> BatchNormalization
> chưa hiểu lắm

  <br>

    <a id="node-1400"></a>
    <p align="center"><kbd><img src="assets/07499e15ee55e2f2e6885230d807b5c4cb1c2e7a.png" width="100%"></kbd></p>
    <br>

    <a id="node-1401"></a>
    <p align="center"><kbd><img src="assets/d988c6c5617f27e36a4d4d226ec414787e3e7a2e.png" width="100%"></kbd></p>
    <br>

<a id="node-1402"></a>
- Exercise 1 - identity_block: Đại khái là làm theo gợi ý lần lượt khai báo các layer  Conv2D, BatchNorm, Activation (Relu),  Conv2D, BatchNorm, Activation (Relu)  Conv2D, BatchNorm, Add, Activation (Relu)  Với input thằng sau là ouput thằng trước từ đó X được update qua các layer.  Để ý thấy ở đây nó dùng keras.layer.Activation('relu') thay vì keras.layer. RELU()  như ở P.A tuần trước  Và thao tác '**Skip Connection**' được thực hiện bằng cách save X_shortcut và add  với X ở layer **Add**
  <br>

    <a id="node-1403"></a>
    <p align="center"><kbd><img src="assets/74e1f39b02bb880f29057c821305e6374819f08b.png" width="100%"></kbd></p>
    <br>

    <a id="node-1404"></a>
    <p align="center"><kbd><img src="assets/a4421f160ea60f08721c7cb4f6e80fedd93f7d66.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/a4421f160ea60f08721c7cb4f6e80fedd93f7d66.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/9f77c74cd70635bb2de1ad40369d698e6e38bfa0.png" width="100%"></kbd></p>
    <br>

    <a id="node-1405"></a>
    <p align="center"><kbd><img src="assets/c2ce8bab47a002c6b86f17f73d483597b12cdd90.png" width="100%"></kbd></p>
    <br>

<a id="node-1406"></a>
- 3.2 - The Convolutional Block:  Đại khái là cái này chỉ khác cái identity block ở chỗ nó có thêm bước dùng Conv2D để resize X_shortcut nhằm để X và X_shortcut cùng size cho bước Add, bước này đóng vai trò như \\/**Ws**\\/ trong lecture nói tới.  Nói tới đại khái là không áp dụng Activation function vì mục đích chỉ là resize thôi  Để ý thấy cho X và X_shortcut cùng size thì ở Conv2D cho layer thứ 3 và cho shortcut phải cùng số lượng filter
> [!NOTE]
> Có cái vụ Glorot uniform
> seed là không hiểu

  <br>

    <a id="node-1407"></a>
    <p align="center"><kbd><img src="assets/6ca7dd37655f87f7408db48d954f9fdc69515759.png" width="100%"></kbd></p>
    <br>

    <a id="node-1408"></a>
    <p align="center"><kbd><img src="assets/3455a626aca4272869c1c4898e5623d966659faf.png" width="100%"></kbd></p>
    <br>

<a id="node-1409"></a>
- Exercise 2 - convolutional_block  Đại khái là làm theo gợi ý lần lượt khai báo các layer  Conv2D, BatchNorm, Activation (Relu),  Conv2D, BatchNorm, Activation (Relu)  Conv2D, BatchNorm, Add, Activation (Relu)  Với input thằng sau là ouput thằng trước từ đó X được update qua các layer.  Chỉ có thêm cái Conv và Batch cho Shortcut với filter là F3
  <br>

    <a id="node-1410"></a>
    <p align="center"><kbd><img src="assets/f1b3e8b4ee7dd135f958e5cafe7ee683a0e1c046.png" width="100%"></kbd></p>
    <br>

    <a id="node-1411"></a>
    <p align="center"><kbd><img src="assets/8d4d2b2b007417ac390513366abe5e99bc03cb4b.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/8d4d2b2b007417ac390513366abe5e99bc03cb4b.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/9721f24a23668ea42639b6c8b82dcd234c875b1b.png" width="100%"></kbd></p>
    <br>

    <a id="node-1412"></a>
    <p align="center"><kbd><img src="assets/18e5387005b4efbfb517166710e4a5569fd0d4dc.png" width="100%"></kbd></p>
    <br>

<a id="node-1413"></a>
- 4 - Building Your First ResNet Model (50 layers)  Đại khái là dùng các function ở trên để tạo một network  **so deep**có 50 layers (?!) có kiến trúc như hình
  <br>

    <a id="node-1414"></a>
    <p align="center"><kbd><img src="assets/c726e3fd178494318666b5f136ac2cd49cb5e3f6.png" width="100%"></kbd></p>
    <br>

<a id="node-1415"></a>
- Exercise 3 - ResNet50  Đại khái là cũng lần lượt define từng layer theo kiến trúc của network define trong sơ đồ.  Và cuối cùng tạo model: model = Model(inputs = X_input, outputs = X)
  <br>

    <a id="node-1416"></a>
    <p align="center"><kbd><img src="assets/86da0af9966d2a964e290d1b876bb8761d990ee2.png" width="100%"></kbd></p>
    <br>

    <a id="node-1417"></a>
    <p align="center"><kbd><img src="assets/e9d411c110740cdf5f8e0964cafc2c01866db0b3.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/e9d411c110740cdf5f8e0964cafc2c01866db0b3.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/afdff13b3ea2277c7132392bde6e27d57517e1c9.png" width="100%"></kbd></p>
    <br>

    <a id="node-1418"></a>
    <p align="center"><kbd><img src="assets/a4dfb87921148a60828ab2c1be201ee77c2b9291.png" width="100%"></kbd></p>
    <br>

<a id="node-1419"></a>
- Compile và Load Data   Dùng **Adam** optimizers,  **categorical_crossentropy** loss function,  Metrics dùng **accuracy**Data là bộ**hand-sign data** bữa trước
  <br>

    <a id="node-1420"></a>
    <p align="center"><kbd><img src="assets/f231f4246151e4d035e3e5aec221ba8a38b9f02b.png" width="100%"></kbd></p>
    <br>

    <a id="node-1421"></a>
    <p align="center"><kbd><img src="assets/968384583a549be5933667097a2d2c0bb7a71f3f.png" width="100%"></kbd></p>
    <br>

<a id="node-1422"></a>
- ..và train model dùng 10 epochs, batch size = 32
  <br>

    <a id="node-1423"></a>
    <p align="center"><kbd><img src="assets/be605580ffd55a971335ab660849650e45b48b45.png" width="100%"></kbd></p>
    <br>

    <a id="node-1424"></a>
    <p align="center"><kbd><img src="assets/e6f0324629cf74b65b70d2f7878422de428aa4da.png" width="100%"></kbd></p>
    <br>

    <a id="node-1425"></a>
    <p align="center"><kbd><img src="assets/a2203b1cb5bf6abbb4ee87e82d88fb477af5b9a7.png" width="100%"></kbd></p>
    <br>

<a id="node-1426"></a>
- Submit và load pretrain model: Đại khái là ổng kêu thích thì train lại với nhiều  epoch hơn và load về cái model đã được train bằng GPU để chạy thử xem accuracy bao nhiêu.  **What you should remember**:  • Very deep "plain" networks don't work in practice because vanishing gradients make them hard to train.  • Skip connections help address the Vanishing Gradient problem. They also make it easy for a ResNet block to learn an identity function.  • There are two main types of blocks: The **identity block** and the **convolutional block**.  • Very deep Residual Networks are built by stacking these blocks together.
> [!NOTE]
> State of the art: HIện đại nhất. Ý là
> dùng cái này là hiện đại nhất rồi

  <br>

    <a id="node-1427"></a>
    <p align="center"><kbd><img src="assets/736a5e95c9129f6aca242e0d4b75a52ea3ae28af.png" width="100%"></kbd></p>
    <br>

    <a id="node-1428"></a>
    <p align="center"><kbd><img src="assets/58654772dd2ee27aedd4111f78f95fe2db393224.png" width="100%"></kbd></p>
    <br>

<a id="node-1429"></a>
- 5 - Test on Your Own Image (Optional/Ungraded)  Dùng hình tự chụp để test thử thấy hình như không đúng. Ổng có hỏi là h thử nghĩ xem tại sao ?  Có thể liên quan đến 'distribution' Hình dùng để train là trên mạng, còn đây là hình tự  chụp dẫn đến training set và production set bị khác distribution  Giải pháp là gì? Xem lại Course 3
> [!NOTE]
> Giải pháp là gì -> Xem lại course 3

  <br>

    <a id="node-1430"></a>
    <p align="center"><kbd><img src="assets/ba21b1e72c99482e48dbdd96f96df739e3531f88.png" width="100%"></kbd></p>
    <br>

    <a id="node-1431"></a>
    <p align="center"><kbd><img src="assets/167263c6702b8c4eeb14ddc967abc0de8aee3ee5.png" width="100%"></kbd></p>
    <br>

<a id="node-1432"></a>
- 6 - Bibliography  This notebook presents the ResNet algorithm from He et al. (2015).  The implementation here also took significant inspiration and follows the structure given in the GitHub repository of Francois Chollet:  • Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun - \\_Deep Residual Learning for Image Recognition (2015) \\_  • Francois Chollet's GitHub repository: \\_https://github. com/fchollet/deep-learning-models/blob/master/resnet50. py\\_
  <br>


<a id="node-1433"></a>
## Programming Assignment: Transfer Learning With Mobilenet

<br>


<a id="node-1434"></a>
### Welcome to this week's assignment, where you'll be using transfer

> [!NOTE]
> Welcome to this week's assignment, where you'll be using transfer
> learning on a pre-trained CNN to build an Alpaca/Not Alpaca
> classifier! A pre-trained model is a network that's already been trained
> on a large dataset and saved, which allows you to use it to customize
> your own model cheaply and efficiently. The one you'll be using,
> MobileNetV2, was designed to provide fast and computationally
> efficient performance. It's been pre-trained on ImageNet, a dataset
> containing over 14 million images and 1000 classes. By the end of
> this assignment, you will be able to:
>
> • \\/Create a dataset\\/ from a directory
>
> • \\/Preprocess and augment data using the Sequential API\\/
>
> • Adapt a \\/pretrained model to new data\\/ and train a classifier using
> the Functional API and \\/MobileNet\\/
>
> • Fine-tune a classifier's final layers to improve accuracy

<p align="center"><kbd><img src="assets/3b132d7ea081e502d2ee90c2ff0eeaab8cb0e4dd.png" width="100%"></kbd></p>

<br>

<a id="node-1435"></a>
- 1 - Packages
  <br>

    <a id="node-1436"></a>
    <p align="center"><kbd><img src="assets/748742d589240c2de19afc8613ca1e3256bfd5c8.png" width="100%"></kbd></p>
    <br>

<a id="node-1437"></a>
- 1.1 Create the Dataset and Split it into Training and Validation Sets  Đại khái là dùng \\/**image_dataset_from_directory**() của Keras để **load image từ  thư mục** \\/chỉ định, return một **TensorFlow Dataset**, quy định sẵn batch size, size để nó Resize image, tỉ lệ phân chia và tên các gói để phân chia.
  <br>

    <a id="node-1438"></a>
    <p align="center"><kbd><img src="assets/6bdbfeadad4fdfaec6bbe58970ffd48c2ccec370.png" width="100%"></kbd></p>
    > [!NOTE]
    > This code block is for loading image data from a directory and splitting it into training and
    > validation datasets. It uses the **image_dataset_from_directory**() function **from the
    > TensorFlow library**, which **creates a TensorFlow dataset** from image files located in a
    > directory.
    >
    > The following are the explanations of the parameters used:
    >
    > • **BATCH_SIZE**: It defines the number of images to be processed in a single batch. Here,
    > the batch size is set to 32, meaning that 32 images will be processed at a time.
    >
    > • **IMG_SIZE**: It is a tuple containing the height and width of the image. **The images will be**
    > **resized to this size** before being used in the model. Here, the image size is set to (160,
    > 160).
    >
    > • **directory**: It specifies the directory containing the image files.
    >
    > • **shuffle**: It determines whether the dataset should be shuffled before each epoch. Here, it is
    > set to True, which means the dataset will be shuffled.
    >
    > • **validation_split**: It is the fraction of the data to be used for validation. Here, 20% of the data
    > is used for validation and 80% for training.
    >
    > • **subset**: It specifies whether the dataset to be created is for training or validation. Here, the
    > training subset is used for creating the training dataset, and the validation subset is used for
    > creating the validation dataset.
    >
    > • **seed**: It is used to seed the random number generator. Here, it is set to 42 for
    > reproducibility.
    >
    > The image_dataset_from_directory() function returns a TensorFlow dataset that can be
    > used for training a machine learning model. In this code block, two datasets are created:
    > train_dataset and validation_dataset, each containing images for training and validation
    > respectively.

    <br>

    <a id="node-1439"></a>
    <p align="center"><kbd><img src="assets/8320253059273154c5f0e793e7cf6c1dbe3b6c1b.png" width="100%"></kbd></p>
    > [!NOTE]
    > Có một số hình bị sai

    <br>

<a id="node-1440"></a>
- 2 - Preprocess and Augment Training Data:  Đại khái là nói về \\/**prefetch()**\\/ data đã từng dùng ở assignment  trước để kiểu như chuẩn bị để khi chạy G.D luôn có sẵn data. Lợi hại hơn nữa là nó có thể tối ưu số lượng data chuẩn bị sẵn giùm mình luôn bằng cách để \\/buffer_size = AUTOTUNE.  Lợi hại hơn nữa là nó có thể làm cái vụ Data Augmentation nữa\\/
  <br>

    <a id="node-1441"></a>
    <p align="center"><kbd><img src="assets/0d2a652ed51bf6cf6190c35a0d02fbd12fa47077.png" width="100%"></kbd></p>
    <br>

<a id="node-1442"></a>
- Exercise 1 - data_augmenter:  Đại khái đơn giản là khởi tạo 1 Sequential và bỏ vào 2 layer: RandomFlip và RandomRotation  data_augmentation = tf.keras.Sequential() data_augmentation.add(RandomFlip('horizontal')) data_augmentation.add(RandomRotation(0.2))  Sau đó xài thử trên một image xem chơi
  <br>

    <a id="node-1443"></a>
    <p align="center"><kbd><img src="assets/167a9b5f7125192749c7f5f31bc05fcc9589a205.png" width="100%"></kbd></p>
    <br>

    <a id="node-1444"></a>
    <p align="center"><kbd><img src="assets/35f4efbd6b5ac112bf6d7789a516fe4bcb7789d2.png" width="100%"></kbd></p>
    <br>

<a id="node-1445"></a>
- **What you should remember:**  • When calling \\/image_data_set_from_directory\\/(), specify the train/val subsets and match the seeds to prevent overlap  • Use \\/prefetch\\/() to prevent memory bottlenecks when reading from disk  • Give your model more to learn from with simple data \\/augmentations\\/ like rotation and flipping.  • When using a pretrained model, it's best to \\/reuse the weights\\/ it was trained on.
  <br>

    <a id="node-1446"></a>
    <p align="center"><kbd><img src="assets/4f84a0d8fe0bd48243e41ffb6df850d7ecd0e27b.png" width="100%"></kbd></p>
    > [!NOTE]
    > Dùng lại preprocess_input???

    <br>

<a id="node-1447"></a>
- 3 - Using MobileNetV2 for Transfer Learning
  <br>

    <a id="node-1448"></a>
    <p align="center"><kbd><img src="assets/c9b12e54ffa5f155111aefa40585be8a4692a365.png" width="100%"></kbd></p>
    <br>

<a id="node-1449"></a>
- 3.1 - Inside a MobileNetV2 Convolutional Building Block
  <br>

  <a id="node-1450"></a>
  - Đại khái là nói lại về MobileNet v2 building block
    <br>

      <a id="node-1451"></a>
      <p align="center"><kbd><img src="assets/b1d65288d384ff642a0bf6ec7648a3fdcc9f1d4d.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/b1d65288d384ff642a0bf6ec7648a3fdcc9f1d4d.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/e7bc3da140871fafeffbe725a9c5b4c60963183e.png" width="100%"></kbd></p>
      > [!NOTE]
      > Đại khái là nói lại về MobileNet v2 building block

      <br>

      <a id="node-1452"></a>
      <p align="center"><kbd><img src="assets/c58796de7f435e82d79c3ffdfb378e90f0fa288a.png" width="100%"></kbd></p>
      <br>

      <a id="node-1453"></a>
      <p align="center"><kbd><img src="assets/2c652c385140e61ded2fe3db8df4466b29a5789c.png" width="100%"></kbd></p>
      > [!NOTE]
      > Đại khái là nó expand ra để tính toán được nhiều feature hữu
      > ích hơn, sau đó co lại để đáp ứng điều kiện dung lượng bộ nhớ
      > hạn hẹp -> Tốt hơn MobileNet v1 mà vẫn đáp ứng bộ nhớ nhỏ

      > [!NOTE]
      > Đại khái như vậy là đủ hiểu
      > MobileNet v2 rồi, muốn xem
      > kĩ hơn để biết chi tiết thì đọc
      > Paper của Sandler

      > [!NOTE]
      > Từ nxnx3 -> nxnx18 thì ta dùng 18 cái filter 1x1x3
      >
      > Còn từ nxnx18 về lại nxnx3 thì dùng 3 cái filter 1x1x18

      <br>

  <a id="node-1454"></a>
  - Đại khái là nó dùng lại cái MobileNet v2, \\/include_top\\/ = True tức là giữ nguyên layer cuối (Softmax), và weights đã được pretrained  Summary xem thì nhận thấy :  Đại khái là cấu trúc 1 Bottleneck layer thường sẽ như vầy  -> Expand Conv - Expand BN - Expand Relu Depthwise - Depthwise BN - Depthwise Relu Project Conv - Project BN - Add (Skip connection) ->
    <br>

      <a id="node-1455"></a>
      <p align="center"><kbd><img src="assets/31d8c70b4dd4b285ed23ae9f6957dfb30aba9bb0.png" width="100%"></kbd></p>
      > [!NOTE]
      > Đại khái là nó dùng lại cái MobileNet v2,
      > include_top = True tức là giữ nguyên layer cuối
      > (Softmax), và weights đã được pretrained

      > [!NOTE]
      > Chưa hiểu IMAGE_SHAPE = IMG_SIZE + (3,) là sao

      <br>

      <a id="node-1456"></a>
      <p align="center"><kbd><img src="assets/48e74bb4f44fd4d187dbe48db21ac1a32528c29f.png" width="100%"></kbd></p>
      > [!NOTE]
      > Đại khái là cấu trúc 1 Bottleneck layer thường sẽ như vầy
      >
      > -> Expand Conv - Expand BN - Expand Relu
      > Depthwise - Depthwise BN - Depthwise Relu
      > Project Conv - Project BN - Add (Skip connection) ->

      <br>

<a id="node-1457"></a>
- What you should remember:  MobileNetV2's unique features are:  Depthwise separable convolutions that provide lightweight feature filtering and creation Input and output bottlenecks that preserve important information on either end of the block  Depthwise separable convolutions deal with both spatial and depth (number of channels) dimensions
  <br>

<a id="node-1458"></a>
- Đại khái là Xem thử performance của cái pretrain network rao sao trên 1 batch data  Kết quả không tốt do pretrain data không có alpaca, nên việc tiếp theo là bỏ layer cuối (top layer) mà train lại layer cuối
  <br>

    <a id="node-1459"></a>
    <p align="center"><kbd><img src="assets/d27342cc92f8efa4f77f0689024d4de7bfe2cbef.png" width="100%"></kbd></p>
    > [!NOTE]
    > Đại khái là lấy 1 batch data (32 cái) ra và nói về cái format của kết
    > quả, trả về 2 con số probability cao nhất ứng với khả năng của 1
    > hình thuộc về 2 loại

    <br>

    <a id="node-1460"></a>
    <p align="center"><kbd><img src="assets/6232fed6a9fa8fee35c7baa658bdecd9a2f366d2.png" width="100%"></kbd></p>
    <br>

    <a id="node-1461"></a>
    <p align="center"><kbd><img src="assets/11e0cd937d60bfd5ecd616e4183f66acefa56445.png" width="100%"></kbd></p>
    > [!NOTE]
    > Đại khái là kết quả không tốt do pretrain data không có alpaca, nên
    > việc tiếp theo là bỏ layer cuối (top layer) mà train lại layer cuối

    <br>

<a id="node-1462"></a>
- 3.2 - Layer Freezing with the Functional API  Đại khái ta sẽ bỏ layer cuối và đóng băng (freez) cái pretrain network  đơn giản bằng cách set params \\/include_top = false và , model.trainable = false  Sau đó add 1 layer và train nó.\\/
  <br>

    <a id="node-1463"></a>
    <p align="center"><kbd><img src="assets/6666f942659efc730adec032d4da0582496d0aa8.png" width="100%"></kbd></p>
    <br>

<a id="node-1464"></a>
- Exercise 2 - alpaca_model:  Theo gợi ý lần lượt define model mới, dùng lại Pretrain model  Add thêm layer cuối với GlobalAveragePooling2D, Dropout, và Dense với 1 unit  Chỉ chưa hiểu tại sao layer cuối dùng Linear mà ko phải sigmoid
  <br>

    <a id="node-1465"></a>
    <p align="center"><kbd><img src="assets/1db90caf6ee804bdb840d50e20828ef48292db5a.png" width="100%"></kbd></p>
    > [!NOTE]
    > Tại sao lại Linear ở cuối mà ko phải Sigmoid

    <br>

    <a id="node-1466"></a>
    <p align="center"><kbd><img src="assets/fc528f3f340695ec7a041a96fbb3efc6f25dc3f9.png" width="100%"></kbd></p>
    <br>

<a id="node-1467"></a>
- Compile & train model: Adam optimizer, BinaryCrossentropy loss function, accuracy
  <br>

    <a id="node-1468"></a>
    <p align="center"><kbd><img src="assets/b92014bc600c9e110384408826cb8b61b655e26a.png" width="100%"></kbd></p>
    <br>

    <a id="node-1469"></a>
    <p align="center"><kbd><img src="assets/3a7e790004dfce313a79d93c42ff4b06ce1e3f39.png" width="100%"></kbd></p>
    <br>

    <a id="node-1470"></a>
    <p align="center"><kbd><img src="assets/acd3083f224022ef7f5549dd408fbd6ee2664927.png" width="100%"></kbd></p>
    <br>

<a id="node-1471"></a>
- 3.3 - Fine-tuning the Model:  Đại khái là gỡ băng 1 số layer cuối (bao nhiêu thì tuỳ nên phải thử) để nó train các 'high feature' với data của con alpaca, giữ nguyên các  'low feature'
  <br>

    <a id="node-1472"></a>
    <p align="center"><kbd><img src="assets/e952cb996a1f769dcb1d7d1e7c190dbffcb29b49.png" width="100%"></kbd></p>
    <br>

<a id="node-1473"></a>
- Exercise 3:  Đại khái là lấy base_model ra (model2. layers[4]) sửa lại một chút như unfreez từ layer số 120 trở đi
  <br>

    <a id="node-1474"></a>
    <p align="center"><kbd><img src="assets/a39689e0fe80dfcd90b1276df0b0aeb8df4a53e1.png" width="100%"></kbd></p>
    > [!NOTE]
    > tại sao model2.layers[4] ???

    <br>

    <a id="node-1475"></a>
    <p align="center"><kbd><img src="assets/c61e108d6e442c1aba0f13760f46df6f08b88388.png" width="100%"></kbd></p>
    > [!NOTE]
    > Tốt hơn hẳn, validation_acc: 95%

    <br>

    <a id="node-1476"></a>
    <p align="center"><kbd><img src="assets/8313c0f006b64f1294a16389103c8d52a060c16d.png" width="100%"></kbd></p>
    <br>

    <a id="node-1477"></a>
    <p align="center"><kbd><img src="assets/027b03f70ac13d41c569a1fd3a4e3d5352e41cc4.png" width="100%"></kbd></p>
    <br>

<a id="node-1478"></a>
- **What you should remember**:  • To adapt the classifier to new data: Delete the top layer, add a new classification layer, and train only on that layer  • When freezing layers, avoid keeping track of statistics (like in the batch normalization layer)  • Fine-tune the final layers of your model to capture high-level details near the end of the network and potentially improve accuracy  **Congratulations!**You've completed this assignment on transfer learning and fine-tuning. Here's a quick recap of all you just accomplished:  • Created a dataset from a directory  • Augmented data with the Sequential API  • Adapted a pretrained model to new data with the Functional API and MobileNetV2  • Fine-tuned the classifier's final layers and boosted the model's accuracy
  <br>

