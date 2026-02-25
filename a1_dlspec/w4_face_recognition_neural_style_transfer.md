# W4_face Recognition & Neural Style Transfer

📊 **Progress:** `43` Notes | `111` Screenshots

---

1ST REVIEWED: LECTURE, CHƯA PA

**Learning Objectives**
 • Differentiate between face recognition and face verification
 • Implement one-shot learning to solve a face recognition problem
 • Apply the triplet loss function to learn a network's parameters in the context of face recognition
 • Explain how to pose face recognition as a binary classification problem
 • Map face images into 128-dimensional encodings using a pretrained model
 • Perform face verification and face recognition with these encodings
 • Implement the Neural Style Transfer algorithm
 • Generate novel artistic images using Neural Style Transfer
 • Define the style cost function for Neural Style Transfer
 • Define the content cost function for Neural Style Transfer

<a id="node-1675"></a>
## Face Recognition

<br>


<a id="node-1676"></a>
### What's Face

> [!NOTE]
> WHAT'S FACE
> RECOGNITION?

<br>


<a id="node-1677"></a>
### One Shot Learning

<br>

<a id="node-1678"></a>
- 1 Face recognition requires solving the one-shot learning problem  2 Deep learning algorithms historically struggle with one-shot learning  3 One approach to address one-shot learning is to input an image, feed it to a ConvNet, and output a label using a softmax unit with multiple outputs  4 Learning a similarity function, denoted d, is a more effective approach to one-shot learning for face recognition  5 The function d takes two images and outputs the degree of difference between them  6 During recognition time, if the degree of difference is less than a threshold, the two images are predicted to be the same person  7 Learning function d allows for adding new people to the database without needing to retrain the neural network  8 Training a neural network to learn function d is discussed in the next video.
  <br>

    <a id="node-1679"></a>
    <p align="center"><kbd><img src="assets/6175d100bd55e107073ea9073dc0bc03eaa3b7eb.png" width="100%"></kbd></p>
    > Đại khái là vấn đề One-shot learning, vì
> không có nhiều data để train

    <br>

    <a id="node-1680"></a>
    <p align="center"><kbd><img src="assets/0d35ce0e36b85070748265f2deefe05aebab2b88.png" width="100%"></kbd></p>
    > Đại khái là learn được function d() tính được độ 'difference'
> giữa các images. Cùng 1 người thì ra số nhỏ

    <br>


<a id="node-1681"></a>
### Siamese Network

<br>

<a id="node-1682"></a>
- 1 The function d compares two faces and determines their similarity or difference using a Siamese network.  2 A feature vector of 128 numbers is computed by a fully connected layer to encode an input image, which represents a good representation of the image.  3 A Siamese neural network architecture runs two identical convolutional neural networks on two different inputs and then compares them.  4 \\*The Siamese neural network is trained by learning parameters that result in a function d, which tells when two pictures are of the same person.\\*  5 The objective function to make a neural network learn to determine similarity or difference between two faces is defined using the triplet loss function.
  <br>

    <a id="node-1683"></a>
    <p align="center"><kbd><img src="assets/ab586ac2f505a89a64f2ff1c10b20ff8a7bc6ee8.png" width="100%"></kbd></p>
    <br>

    <a id="node-1684"></a>
    <p align="center"><kbd><img src="assets/59aa5927a6a964552f50160d15ad6d94f5fc8f08.png" width="100%"></kbd></p>
    > Đại khái là **learn params của 1 NN sao cho** đưa hai image (x1), x(2)
> vào cho ra đầu ra f(x1), f(x2) sao cho: nếu cùng 1 người thì norm của
> hai vector nhỏ khác nhau thì norm lớn - Đó gọi là Siamese Network

    <br>


<a id="node-1685"></a>
### Triplet Loss

<br>

<a id="node-1686"></a>
- 1 Gradient descent can be used to learn the parameters of a neural network to give a good encoding for pictures of faces.  2 The triplet loss function is used to compare pairs of images and ensure that similar images have similar encodings.  3 The triplet loss function involves looking at three images at a time: an anchor image, a positive image (of the same person as the anchor), and a negative image (of a different person).  4 The goal of the triplet loss function is to have the encoding of the anchor image and the positive image be closer together than the encoding of the anchor image and the negative image, with a margin parameter to prevent trivial solutions.  5 The triplet loss function is formalized as the max of the difference between the squared norm of the anchor-positive encoding and the squared norm of the anchor-negative encoding minus a margin parameter and zero.
  <br>

    <a id="node-1687"></a>
    <p align="center"><kbd><img src="assets/387a3e0cc3570ab9c434a3cf57b43925c783b935.png" width="100%"></kbd></p>
    > Đại khái là ở đây ta định nghĩa một loss function để dùng trong
> công việc train siamese network. Bằng cách tạo ra một mệnh đề
> trong đó bắt buộc so sánh các cặp hình ảnh sao cho: **encoding
> của anchor image phải giống với encoding của positive image
> và khác với encoding của negative image.**
>
> Trong đó dùng một distance function tính bằng squared norm
> của cặp encoding của anchor - positive / anchor - negative.
>
> Và một tham số alpha để tránh máy tính nó cho kết quả zero.

    <br>

    <a id="node-1688"></a>
    <p align="center"><kbd><img src="assets/eb72aea1eab4f0a70fe03dab4faa56e14a70db41.png" width="100%"></kbd></p>
    > Đại khái là dựa vào yêu cầu ta define một hàm loss như vầy,
> rồi cost function. Cách define vầy sẽ khiến muốn minimize loss
> thì hiệu số giữa encoding của A và encoding của P phải nhỏ
> hơn nhiều hiệu số giữa encoding của A và encoding của N
>
> Yêu cầu là training set phải có nhiều picture của 1 người để từ
> đó có các cặp A-P, A-N

    <br>

    <a id="node-1689"></a>
    <p align="center"><kbd><img src="assets/a51e43491839641e21f0212b1bee306282fa2d59.png" width="100%"></kbd></p>
    > Đại khái là phải choose triplets A,P,N sao cho làm
> cho việc training khó bởi vì nếu chọn ngẫu nhiên
> thì rất dễ để có cặp A-P khác xa A-N

    <br>

    <a id="node-1690"></a>
    <p align="center"><kbd><img src="assets/91ef78e3ce9addc8b952aa8befdfd558c26d1ea9.png" width="100%"></kbd></p>
    > Tóm lại đại khái là vầy:
>
> Chuẩn bị bộ data theo kiểu cặp 3 cái A-P-N Trong đó có
> A-P là của cùng 1 người,
>
> DÙng hàm Triplet Loss để Gradient Descent để train ra
> params sao cho decoding của hai người khác nhau sẽ
> lớn hơn nhiều decoding của 2 ảnh của cùng 1 người

    <br>

    <a id="node-1691"></a>
    <p align="center"><kbd><img src="assets/839113080719b08e88eff7f111170d658a41872f.png" width="100%"></kbd></p>
    > Tóm lại đại khái là vầy:
>
> Đại khái là một số company có những bộ data rất lớn và khó mà
> tiếp cận được, nhưng một số publish model đã train đó mình có
> thể xài lại được (transfer learning)

    <br>


<a id="node-1692"></a>
### Clarification About

> [!NOTE]
> CLARIFICATION ABOUT
> UPCOMING FACE VERIFICATION...

<br>


<a id="node-1693"></a>
### Face Verification And

> [!NOTE]
> FACE VERIFICATION AND
> BINARY CLASSIFICATION

<br>

<a id="node-1694"></a>
- 1 Introduction to Face Recognition: There are different ways to learn parameters for face recognition systems, including the Triplet Loss and a straight binary classification approach.  2 Straight Binary Classification for Face Recognition: Face recognition can be posed as a binary classification problem by using a Siamese Network to compute embeddings and inputting them into a logistic regression unit to predict whether the two images are of the same person or not.  3 Computing the Logistic Regression Unit: The logistic regression unit \\*takes the differences between the encodings as features\\* and \\*trains appropriate weights on these features to predict whether the two images are of the same person or not.\\*  4 Variations on Computing the Formula: There are different variations on computing the formula for the logistic regression unit, including the \\*chi-square similarity formula\\*.  5 Training the Siamese Network: The Siamese Network is trained using pairs of similar and dissimilar images to learn to predict whether the two images are of the same person or not.  6 Pre-Computing Encodings: Pre-computing encodings can save significant computation time and works for both the binary classification approach and the Triplet Loss approach.  7 Creating a Training Set: To train a face verification or recognition system, a training set of pairs of images with target labels of one for same persons and zero for different persons is created.  8 Conclusion: With the knowledge of these techniques, one can train a face verification or recognition system that can perform one-shot learning.
  <br>

    <a id="node-1695"></a>
    <p align="center"><kbd><img src="assets/6ffa97cd7011e1ceea54ba724323181dcef49ee4.png" width="100%"></kbd></p>
    > Đại khái là vầy: Thay vì dùng phương pháp Triplet loss, ta có
> thể dùng cách 'Binary Classification'.
>
> Đại loại ra ta lấy output của Siamese network bỏ vào logistic
> regression. L. G sẽ **đại khái là train input data mà feature là
> sự giống và khác nhau của encoding của 2 bức ảnh kết quả
> bởi Siamese network để rồi train được params sao cho cùng
> người thì ra y^ = 1, khác người thì y^ = 0.**Có một vài 'biến thể' trong cách define logistic regression như
> dùng  **Absolute** value hay **Squared** value. 
>
> Ký hiệu của term f(x(i)) - f(x(j)) gọi là χ - CHI

    <br>

    <a id="node-1696"></a>
    <p align="center"><kbd><img src="assets/ce8eda4c4259894acc1a125f3e12477fd28afab0.png" width="100%"></kbd></p>
    > Các bộ training data sample là các cặp hình, cùng 1 người
> thì y = 1, khác người thì y = 0.

    <br>


<a id="node-1697"></a>
## Neural Style Transfer

<br>


<a id="node-1698"></a>
### What's Neural Style Transfer?

<br>

<a id="node-1699"></a>
- Đại khái là một ứng dụng hay ho của ConvNet là cái này, apply style của 1 image cho 1 image khác.  Cần xem thử các feature learned bởi ConvNet tại các layers khác nhau trông như thế nào
  <br>

    <a id="node-1700"></a>
    <p align="center"><kbd><img src="assets/672c8a82acf0704c1b3e52ef5896a9ff9849040c.png" width="100%"></kbd></p>
    > Đại khái là một ứng dụng hay ho của ConvNet là cái này, apply
> style của 1 image cho 1 image khác.
>
> Cần xem thử các feature learned bởi ConvNet tại các layers khác
> nhau trông như thế nào

    <br>


<a id="node-1701"></a>
### What Are Deep Convnets Learning

<br>

<a id="node-1702"></a>
- 1 The video aims to explain what the deeper layers of a ConvNet are really doing and provide visualizations that will help viewers understand the neural network's functioning better.  2 To visualize what hidden units in different layers are computing, one can find out the\\* images that maximize that unit's activation\\* by scanning through the training sets.  3 Hidden units in layer 1 usually detect relatively \\*simple features such as edges or shades of color.\\*  4 Hidden units in d\\*eeper layers\\* of the neural network see a \\*larger region of the image\\* and \\*detect more complex shapes and patterns\\*.  5 The features that second and third layers detect are \\*getting more complicated\\*.  6 The video cites a paper titled "\\*Visualizing and Understanding Convolutional Networks" by Matthew Zeiler and Rob Fergus\\* that offers more sophisticated ways of visualizing when the ConvNet is running.
  <br>

    <a id="node-1703"></a>
    <p align="center"><kbd><img src="assets/dcb5c208d414993769321806a1689adce302b693.png" width="100%"></kbd></p>
    > Đại khái là trong layer 1
>
> Với mỗi hidden layer, tìm 9 cái hình mà có unit activation lớn nhất.
>
> Lần lượt vậy với các hidden layer khác.
>
> In ra để xem nó như thế nào thì thấy càng sâu thì nó học thêm các feature /
> pattern càng  phức tạp s

    <br>

    <a id="node-1704"></a>
    <p align="center"><kbd><img src="assets/dad524a7a05153d0e9e7673f2846ab6bc18fd3a0.png" width="100%"></kbd></p>
    <br>

    <a id="node-1705"></a>
    <p align="center"><kbd><img src="assets/a8c2e0f2bcaab6c5c36d22de1144100c0001c234.png" width="100%"></kbd></p>
    <br>

    <a id="node-1706"></a>
    <p align="center"><kbd><img src="assets/291932ff6fa2c0a8ccd2beaf3f15ec2752b6e9f6.png" width="100%"></kbd></p>
    <br>

    <a id="node-1707"></a>
    <p align="center"><kbd><img src="assets/11101082b067c0b61a261d764b4e7b239bb417ff.png" width="100%"></kbd></p>
    <br>

    <a id="node-1708"></a>
    <p align="center"><kbd><img src="assets/e57a89ee6084ba86c247ab6bb3995cfeeb57e698.png" width="100%"></kbd></p>
    <br>


<a id="node-1709"></a>
### Cost Function

<br>

<a id="node-1710"></a>
- Đại khái ý tưởng là define một hàm cost function sao cho bao gồm cost function:  đ/v Content -> Làm sao cho kết quả giống với hình gốc và  đ/v Style -> Làm sao cho kết quả giống với hình style  Và nếu minimize hàm cost function này thì kết quả sẽ vừa giống hình gốc và vừa giống hình style
  <br>

    <a id="node-1711"></a>
    <p align="center"><kbd><img src="assets/96162f182c70c977d49a61fc23841538f74ecee3.png" width="100%"></kbd></p>
    > Đại khái ý tưởng là define một hàm cost function sao cho bao gồm cost
> function:
>
> đ/v Content -> Làm sao cho kết quả giống với hình gốc
>
> đ/v Style -> Làm sao cho kết quả giống với hình style
>
> Và nếu minimize hàm cost function này thì kết quả sẽ vừa giống hình
> gốc và vừa giống hình style

    <br>

    <a id="node-1712"></a>
    <p align="center"><kbd><img src="assets/63ca89e0f9729b513f1b70de48fb1fec22913ccd.png" width="100%"></kbd></p>
    <br>


<a id="node-1713"></a>
### Content Cost Function

<br>

<a id="node-1714"></a>
- 1 The neural style transfer algorithm has a cost function with a content cost component and a style cost component.  2 The content cost function measures the similarity of the hidden layer activations between a content image and a generated image.  3 A layer is chosen somewhere in between shallow and deep layers to compute the content cost.  4 A pre-trained ConvNet, such as a VGG network, can be used to measure the similarity between the activations of the content image and the generated image.  5 The content cost function is defined as the element-wise sum of squares of differences between the activations in layer l, between the images in C and G.  6 The content cost function incentivizes the algorithm to find an image G that has hidden layer activations similar to those of the content image.  7 The style cost function will be discussed next.
  <br>

    <a id="node-1715"></a>
    <p align="center"><kbd><img src="assets/e0416f16992d8515d56ddcbc66164ffabaafc028.png" width="100%"></kbd></p>
    > \/Use hidden layer l to compute content cost: \/ Đại khái là nếu L nhỏ, kiểu
> như bắt buộc cái hình mới phải giống y chang cái hình gốc, còn nếu L lớn
> thì chỉ cần giống giống một cách chung chung thôi.
>
> Vì L nhỏ thì nó ở cấp shallow feature, nên giống ở cấp này tức là phải
> giống ở những nét những feature sơ cấp -> Nên phải giống y mới được
> còn L lớn thì nó ở deep feature nên giống ở cấp này tức là giống ở mức
> pattern - Không cần y chang.

    > *a[l](C) & a[l](G):
> Unrolled into vectors

    > Use pre-trained ConvNet: Đại khái là
> nên dùng pre-trained ConvNet để dùng
> cho step này

    <br>


<a id="node-1716"></a>
### Clarification ....

<br>

  <a id="node-1717"></a>
  <p align="center"><kbd><img src="assets/2e9ce7ee9393e44fb80cc38486059299ecc9a036.png" width="100%"></kbd></p>
  <br>


<a id="node-1718"></a>
### Style Cost Function

<br>

  <a id="node-1719"></a>
  <p align="center"><kbd><img src="assets/a8be68ded43e028364a1edfab02c46ea77274e2e.png" width="100%"></kbd></p>
  > Đầu tiên phải định nghĩa 'style' là sự
> correlation giữa các channels

  <br>

  <a id="node-1720"></a>
  <p align="center"><kbd><img src="assets/19b49cbf88d96dffa9dcb78414e06b3d181d97eb.png" width="100%"></kbd></p>
  > Đại khái là dùng độ correlated giữa các layer để đánh giá xem
> style của generated image có giống style của style input image
> không
>
> Và độ correlated giữa các channel đại khái là ví dụ như là "nếu
> sọc dọc xuất hiện thì nó sẽ có xu hướng màu cam",..đại khái
> kiểu kiểu vậy sẽ "làm nên" / "tạo nên" style của image.

  <br>

  <a id="node-1721"></a>
  <p align="center"><kbd><img src="assets/4e9a3eb5325503029529a6307b98cceaa8eda734.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/b27bee59a28f3c60cd80e41cb9fa60689e8a1fee.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/4e9a3eb5325503029529a6307b98cceaa8eda734.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/b27bee59a28f3c60cd80e41cb9fa60689e8a1fee.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/fe0fa305dcfdb0a6e597a85435812bcefad22688.png" width="100%"></kbd></p>
  > Đại khái là define matrix 'Style' thể hiện style của 1 layer l còn gọi
> là Gram matrix.
>
> Và Từ đó define nên cost function đại khái à chêch lệch giữa style
> tại layer l của 2 bức hình - gốc và hình generated
>
> Có thể (/2nhnwnc) - normalization gì đó nhưng không quan trọng
> ổng nói vậy chưa hiểu lắm .

  <br>

  <a id="node-1722"></a>
  <p align="center"><kbd><img src="assets/ea1ad93dd121e588b1d180ce86b5c999f748eaca.png" width="100%"></kbd></p>
  > Đại khái mở rộng ra define cost function thể hiện chênh lệch giữa
> style của các layer l = 1 - L của hai bức hình style gốc và
> generated image;
>
> \/**Thì nếu train dc bức hình generate sao cho minimize hàm J
> này thì bức hình đó sẽ có style gần giống với bức hình gốc nhất.
>
> \/Và kết hợp với Jcontent nữa thì minimize J sẽ ra bức hình có
> content giống content của bức hình content còn style thì giống
> style của bức Styled image.**

  <br>


<a id="node-1723"></a>
### 1d & 3d Generalizations

<br>

  <a id="node-1724"></a>
  <p align="center"><kbd><img src="assets/3a527ffdf22f133df68e0cc20e838a26cf34551f.png" width="100%"></kbd></p>
  > Chắc không có gì khó hiểu chỉ có ghi chú cho nhớ lại:
>
> Filter dimension không ghi thì cũng phải hiểu là có cùng số
> dimension với input 14x14x3 thì filter cũng 5x5x3 (3 dimension)
>
> và có 16 cái filter thì out sẽ là 10x10x16

  <br>

  <a id="node-1725"></a>
  <p align="center"><kbd><img src="assets/140b2dbbfe8060b6bba4894850833192545f1a30.png" width="100%"></kbd></p>
  <br>

  <a id="node-1726"></a>
  <p align="center"><kbd><img src="assets/7c11185a5342684003e41243b87b6ec8477513b9.png" width="100%"></kbd></p>
  <br>


<a id="node-1727"></a>
### Quiz

<br>

  <a id="node-1728"></a>
  <p align="center"><kbd><img src="assets/f2a32476c0a46eed730b5ad12bb23f3fb64e1c37.png" width="100%"></kbd></p>
  <br>

  <a id="node-1729"></a>
  <p align="center"><kbd><img src="assets/b843b49a1c85818558417e8ba72f05276d806b85.png" width="100%"></kbd></p>
  > Correct. One-shot learning
> **refers to the amount of data we
> have** to solve a task.

  <br>

  <a id="node-1730"></a>
  <p align="center"><kbd><img src="assets/27070fdc2f63d5e9aeb0cb71335300b93d2fc9e2.png" width="100%"></kbd></p>
  > Correct. Although it is **necessary to have several
> pictures of the same person**, it is **not absolutely
> necessary that all the pictures only come from
> current members of the team**.

  <br>

  <a id="node-1731"></a>
  <p align="center"><kbd><img src="assets/954e9032ca7cb8462bcc3523d941e34970e427b0.png" width="100%"></kbd></p>
  <br>

  <a id="node-1732"></a>
  <p align="center"><kbd><img src="assets/9b6642cd1b268d289f85fb16f773f3b02d67a463.png" width="100%"></kbd></p>
  <br>

  <a id="node-1733"></a>
  <p align="center"><kbd><img src="assets/8d96d06ad1b0c328f86fdd8de683151d09b45be9.png" width="100%"></kbd></p>
  <br>

  <a id="node-1734"></a>
  <p align="center"><kbd><img src="assets/c6fe20f3422638f189f406f3b4dd6e2fcc01e69b.png" width="100%"></kbd></p>
  <br>

  <a id="node-1735"></a>
  <p align="center"><kbd><img src="assets/e43ef4e4c5882526ef158a47a671a57447dac060.png" width="100%"></kbd></p>
  <br>

  <a id="node-1736"></a>
  <p align="center"><kbd><img src="assets/34b6040edd1f2dee48a892aa23a463b3c2cb2b37.png" width="100%"></kbd></p>
  <br>

  <a id="node-1737"></a>
  <p align="center"><kbd><img src="assets/b92f0fc6e9d17fc06370ee6060d2ca3f2abe8e5f.png" width="100%"></kbd></p>
  <br>


<a id="node-1738"></a>
### Programming Assignment: Face Recognition

<br>

<a id="node-1739"></a>
- Welcome to the first (required) programming exercise of the final week of Course 4 in the Deep Learning Specialization. In this notebook you will build a face recognition system...one much better than the one shown in the cartoon below! :)  By the end of this assignment, you'll be able to:  • Differentiate between face recognition and face verification  • Implement one-shot learning to solve a face recognition problem  • Apply the triplet loss function to learn a network's parameters in the context of face recognition  • Explain how to pose face recognition as a binary classification problem  • Map face images into 128-dimensional encodings using a pretrained model  • Perform face verification and face recognition with these encodings 
  <p align="center"><kbd><img src="assets/1017fe332dd4648d83f682c2471b96475a6ece86.png" width="100%"></kbd></p>
  > Đại khái là ..

  <br>

  <a id="node-1740"></a>
  - Face Recognition
    <br>

      <a id="node-1741"></a>
      <p align="center"><kbd><img src="assets/5dbb74f570436f486e676a2dd6f4c9db25e8b1f6.png" width="100%"></kbd></p>
      <br>

  <a id="node-1742"></a>
  - 1 - Packages
    <br>

      <a id="node-1743"></a>
      <p align="center"><kbd><img src="assets/eff8b394d1074250826733b8981c5f8c9ea861bf.png" width="100%"></kbd></p>
      <br>

  <a id="node-1744"></a>
  - 2 - Naive Face Verification:  Đại khái là có thể so sánh độ giống của 2 bức hình (để xác định cùng 1 người theo kiểu pixel to pixel, nhưng rõ ràng sẽ rất kém vì so sánh kiểu đó không ổn, pixel nó thay đổi rất nhiều do độ sáng, góc chụp...) nên thay vì vậy phải tạo ra một hàm để encode và so sánh 2 cái encoding này
    <br>

      <a id="node-1745"></a>
      <p align="center"><kbd><img src="assets/8de35ca37d382b35dcbd4211a8dd2573cf999f85.png" width="100%"></kbd></p>
      > Đại khái là có thể so sánh độ giống của 2 bức hình (để
> xác định cùng 1 người theo kiểu pixel to pixel, nhưng rõ
> ràng sẽ rất kém vì so sánh kiểu đó không ổn, pixel nó thay đổi rất
> nhiều do độ sáng, góc chụp...) nên thay vì vậy
> phải tạo ra một hàm để encode và so sánh 2 cái encoding này

      <br>

  <a id="node-1746"></a>
  - 3 - Encoding Face Images into a 128-Dimensional Vector
    <br>

  <a id="node-1747"></a>
  - 3.1 - Using a ConvNet to Compute Encodings  Đại khái là cái cần làm là Train một cái NN để encode input  images sao cho: - Cùng một người thì distance (giữa 2 encoding) thấp - Hai người khác nhau thì distance cao.  Mà để train cái NN này thì cần nhiều data và tốn nhiều thời gian cho nên theo lẽ thường của Deep Learning là ta sẽ tìm một cái model đã pretrain để xài (train lại hoặc dùng như khởi đầu)  Và ổng đã tìm sẵn cho mình xài: \\*keras-facenet-h5/model. json\\* và cái Network Implementation dùng để train ra cái model ở trên là làm theo Inception model của ông Szegedy et al, xem trong file\\* inception_blocks_v2.py  \\*Đại khái là xem thử model (pretrained) output, input sao mình sẽ dùng nó để 'tính' / encode ra encoding, để rồi từ đó tính ra distance của 2 encoding.  Nếu distance của encoding của 2 image cùng 1 người mà nhỏ và 2 người khác nhau mà lớn thì model đó good  Đại khái là triplet loss sẽ giúp train model (phải train tiếp dựa trên pretrain model) sao cho thoả mãn tính chất trên
    <br>

      <a id="node-1748"></a>
      <p align="center"><kbd><img src="assets/5c4ed201d0f8f6521e2257c673045f81c6cb1251.png" width="100%"></kbd></p>
      > Đại khái là cái cần làm là Train một cái NN để encode input 
> images sao cho:
> - Cùng một người thì distance (giữa 2 encoding) thấp
> - Hai người khác nhau thì distance cao.
>
> Mà để train cái NN này thì cần nhiều data và tốn nhiều thời gian
> cho nên theo lẽ thường của Deep Learning là ta sẽ tìm một cái
> model đã pretrain để xài (train lại hoặc dùng như khởi đầu)
>
> Và ổng đã tìm sẵn cho mình xài: **keras-facenet-h5/model. json**
> và cái Network Implementation dùng để train ra cái model ở trên
> là làm theo Inception model của ông Szegedy et al, xem trong
> file**inception_blocks_v2.py**

      <br>

      <a id="node-1749"></a>
      <p align="center"><kbd><img src="assets/de5abbb2a247b891f693d58eb7c906804070f88e.png" width="100%"></kbd></p>
      > Đại khái là xem thử model (pretrained) output, input sao
> mình sẽ dùng nó để 'tính' / encode ra encoding, để rồi từ đó
> tính ra distance của 2 encoding.
>
> Nếu distance của encoding của 2 image cùng 1 người mà nhỏ
> và 2 người khác nhau mà lớn thì model đó good

      <br>

      <a id="node-1750"></a>
      <p align="center"><kbd><img src="assets/078687ec8a42cd804f925378b3dabd62b1b3485b.png" width="100%"></kbd></p>
      > Đại khái là triplet loss sẽ giúp train model  sao cho thoả mãn tính chất trên

      <br>

  <a id="node-1751"></a>
  - 3.2 - The Triplet Loss  Đại khái là làm chơi cho biết chứ do dùng Pretrained model nên thực tế không cần làm
    <br>

      <a id="node-1752"></a>
      <p align="center"><kbd><img src="assets/1ad088897e947ff79791a5fefe09b6d27fcd2021.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/1ad088897e947ff79791a5fefe09b6d27fcd2021.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/9bfb993abcc56cbe3628dd11824079f0392a99d5.png" width="100%"></kbd></p>
      > Đại khái là làm chơi cho biết chứ do dùng
> Pretrained model nên thực tế không cần làm

      <br>

  <a id="node-1753"></a>
  - Exercise 1 - triplet_loss
    <br>

      <a id="node-1754"></a>
      <p align="center"><kbd><img src="assets/cf8bafa7066afbe1347c8d3d0fba3a9dfab7de5f.png" width="100%"></kbd></p>
      <br>

      <a id="node-1755"></a>
      <p align="center"><kbd><img src="assets/787712dedbaa46da7b1956007416cfcacd0b7807.png" width="100%"></kbd></p>
      <br>

      <a id="node-1756"></a>
      <p align="center"><kbd><img src="assets/02f8f7b8551611eaa70a8cc4114ba6e0a9aecb75.png" width="100%"></kbd></p>
      <br>

      <a id="node-1757"></a>
      <p align="center"><kbd><img src="assets/35628f7272a132b90e0fbbb4870812c6b668d8c3.png" width="100%"></kbd></p>
      <br>

  <a id="node-1758"></a>
  - 4 - Loading the Pre-trained Model  Đại khái là load cái model (pretrained) ra xài thôi
    <br>

      <a id="node-1759"></a>
      <p align="center"><kbd><img src="assets/f34ca7554130dba432fa21714305c9d551977021.png" width="100%"></kbd></p>
      > Đại khái là load cái model (pretrained) ra xài thôi

      <br>

  <a id="node-1760"></a>
  - 5 - Applying the Model
    <br>

      <a id="node-1761"></a>
      <p align="center"><kbd><img src="assets/41206a8e3f2bf05582dc731a361be8063ffe7aae.png" width="100%"></kbd></p>
      <br>

  <a id="node-1762"></a>
  - 5.1 - Face Verification
    <br>

      <a id="node-1763"></a>
      <p align="center"><kbd><img src="assets/77470bcad7844a26b81c00683f227f29750a6007.png" width="100%"></kbd></p>
      > Đại khái là dùng cái retrained model để tạo các 'encoding'
> của các nhân viên từ ảnh của họ. 
> Tên - encoding

      <br>

      <a id="node-1764"></a>
      <p align="center"><kbd><img src="assets/3281b11872c85f1b0970782fbdda7e712529e14d.png" width="100%"></kbd></p>
      <br>

  <a id="node-1765"></a>
  - Exercise 2 - verify  Đại khái là  Lấy cái hình (chụp từ camera) (từ image path) bỏ vào tính Encoding.  Có cái tên (identity) -> Lấy cái encoding từ database ra  Tính distance giữa 2 cái encoding này bằng function distance of a & b = \\*np.linalg.norm(a-b)\\*  So với threshold để decide
    <br>

      <a id="node-1766"></a>
      <p align="center"><kbd><img src="assets/e140d59ba959a16b57a689eb4dc1acc0f65692cc.png" width="100%"></kbd></p>
      <br>

      <a id="node-1767"></a>
      <p align="center"><kbd><img src="assets/664d990025764b9949b8d6e9f6e6f39703cac65a.png" width="100%"></kbd></p>
      > Đại khái là
>
> Lấy cái hình (chụp từ camera) (từ image path) bỏ vào tính
> Encoding.
>
> Có cái tên (identity) -> Lấy cái encoding từ database ra
>
> Tính distance giữa 2 cái encoding này bằng function distance of a
> & b = **np.linalg.norm(a-b)**
>
> So với threshold để decide

      <br>

      <a id="node-1768"></a>
      <p align="center"><kbd><img src="assets/32e5f1f92bb5c96ff3baf0856c2fc0611798dd85.png" width="100%"></kbd></p>
      <br>

      <a id="node-1769"></a>
      <p align="center"><kbd><img src="assets/715d632877217e7e694b4ed227a78267bcd19349.png" width="100%"></kbd></p>
      <br>

  <a id="node-1770"></a>
  - 5.2 - Face Recognition  Đại khái là thay vì dùng cái identity (tên) để lấy ra encoding Trong database rồi so nó với encoding của bức hình chụp từ camera thì giờ ta sẽ cứ check hết distance của cam image's encoding với các encoding trong database. Cái nào nhỏ hơn threshold thì Suy ra là người đó, không có thì suy ra là người lạ.
    <br>

      <a id="node-1771"></a>
      <p align="center"><kbd><img src="assets/8011e45162a1f30014bb39335ba45fae51ac6360.png" width="100%"></kbd></p>
      > Đại khái là thay vì dùng cái identity (tên) để lấy ra encoding
> Trong database rồi so nó với encoding của bức hình chụp từ
> camera thì giờ ta sẽ cứ check hết distance của cam image's encoding
> với các encoding trong database. Cái nào nhỏ hơn threshold thì
> Suy ra là người đó, không có thì suy ra là người lạ.

      <br>

  <a id="node-1772"></a>
  - Exercise 3 - who_is_it
    <br>

      <a id="node-1773"></a>
      <p align="center"><kbd><img src="assets/68516d05d8f5610fd6fcd3bf32ed363e2334ec1d.png" width="100%"></kbd></p>
      <br>

      <a id="node-1774"></a>
      <p align="center"><kbd><img src="assets/5c978fcf3757049e37d6245509e785b1cb632182.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/5c978fcf3757049e37d6245509e785b1cb632182.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/2a3c3ba807eada6e10a38c5e4a897bc1e1c02758.png" width="100%"></kbd></p>
      <br>

      <a id="node-1775"></a>
      <p align="center"><kbd><img src="assets/a9ad05a5791b23100acf52e9371f95c2ff2d20dc.png" width="100%"></kbd></p>
      <br>

  <a id="node-1776"></a>
  - \\*Congratulations\\*! You've completed this assignment, and your face recognition system is working well! It not only lets in authorized persons, but now people don't need to carry an ID card around anymore!  You've now seen how a state-of-the-art face recognition system works, and can describe the difference between face recognition and face verification. Here's a quick recap of what you' ve accomplished:  • Posed face recognition as a binary classification problem  • Implemented one-shot learning for a face recognition problem  • Applied the triplet loss function to learn a network's parameters in the context of face recognition  • Mapped face images into 128-dimensional encodings using a pretrained model  • Performed face verification and face recognition with these encodings Great work!  \\*What you should remember\\*:  • Face verification solves an easier 1:1 matching problem; face recognition addresses a harder 1:K matching problem.  • Triplet loss is an effective loss function for training a neural network to learn an encoding of a face image.  • The same encoding can be used for verification and recognition. Measuring distances between two images' encodings allows you to determine whether they are pictures of the same person.
    <br>

    <a id="node-1777"></a>
    - Ways to improve your facial recognition model:  Although you won't implement these here, here are some ways to further improve the algorithm:  Put more images of each person (under different lighting conditions, taken on different days, etc.) into the database. Then, given a new image, compare the new face to multiple pictures of the person. This would increase accuracy.  Crop the images to contain just the face, and less of the "border" region around the face. This preprocessing removes some of the irrelevant pixels around the face, and also makes the algorithm more robust.
      <br>

  <a id="node-1778"></a>
  - 6 - References \\* \\*  1 Florian Schroff, Dmitry Kalenichenko, James Philbin (2015). \\_FaceNet: A Unified Embedding for Face Recognition and Clustering  \\_  2 Yaniv Taigman, Ming Yang, Marc'Aurelio Ranzato, Lior Wolf (2014). \\_DeepFace: Closing the gap to human-level performance in face verification\\_  3 This implementation also took a lot of inspiration from the official FaceNet github repository: \\_https://github.com/davidsandberg/facenet\\_  4 Further inspiration was found here: \\_https://machinelearningmastery. com/how-to-develop-a-face-recognition-system-using-facenet-in-keras-and-an-svm-classifier/\\_  5 And here: \\_https://github.com/nyoki-mtl/keras-facenet/blob/master/notebook/tf_to_keras. ipynb\\_
    <br>


<a id="node-1779"></a>
### Programming Assignment: Art Generation with Neural Style Transfer

<br>

<a id="node-1780"></a>
- Welcome to the final (required) programming exercise, of the final  week of Course 4 in the Deep Learning Specialization! In this notebook,  you'll use transfer learning to generate new artistic images.  \\*Upon completion of this assignment, you will be able to:\\*  • Implement the neural style transfer algorithm  • Generate novel artistic images using your algorithm  • Define the style cost function for Neural Style Transfer  • Define the content cost function for Neural Style Transfer Most of the algorithms you've studied optimize a cost function to get a set of parameter values. With Neural Style Transfer, you'll get to optimize a cost function to get pixel values. Exciting!
  <p align="center"><kbd><img src="assets/5e555086022738b7abaf5362f84e720334236096.png" width="100%"></kbd></p>
  <br>

  <a id="node-1781"></a>
  - 1 - Packages
    <br>

      <a id="node-1782"></a>
      <p align="center"><kbd><img src="assets/a6a52bc57ba721b3b670fe190d9e904e10f5e0c8.png" width="100%"></kbd></p>
      <br>

  <a id="node-1783"></a>
  - 2 - Problem Statement
    <br>

      <a id="node-1784"></a>
      <p align="center"><kbd><img src="assets/62e2abdff39f3c0e3ef918536035467cbd5da56a.png" width="100%"></kbd></p>
      <br>

  <a id="node-1785"></a>
  - 3 - Transfer Learning
    <br>

      <a id="node-1786"></a>
      <p align="center"><kbd><img src="assets/faa8387f54b802c048fdd4e363612036ac4a6fd0.png" width="100%"></kbd></p>
      > Đại khái là dùng một cái NN đã train với một kho data image khủng

      <br>

  <a id="node-1787"></a>
  - 4 - Neural Style Transfer (NST)  - First, you will build the content cost function  𝐽𝑐𝑜𝑛𝑡𝑒𝑛𝑡(𝐶,𝐺) - Second, you will build the style cost function  𝐽𝑠𝑡𝑦𝑙𝑒(𝑆,𝐺) - Finally, you'll put it all together to get 𝐽(𝐺) = 𝛼𝐽𝑐𝑜𝑛𝑡𝑒𝑛𝑡(𝐶,𝐺) + 𝛽𝐽𝑠𝑡𝑦𝑙𝑒(𝑆,𝐺)
    <br>

    <a id="node-1788"></a>
    - 4.1 - Computing the Content Cost
      <br>

      <a id="node-1789"></a>
      - 4.1.1 - Make Generated Image G Match the Content of Image C  Đại khái là bước 1 là:  Làm sao để Generated image giống với Content.  Chọn l giữa giữa để 'nó' capture cả low level và high level  features.  Ta dùng content image và generated image bỏ vào cái VGG network để forward prop để lấy ra a(C) và a(G) - Ouput của hidden layer thứ L
        <br>

          <a id="node-1790"></a>
          <p align="center"><kbd><img src="assets/dc8efc14a6c85065d63812b9e2156b3020347041.png" width="100%"></kbd></p>
          > Đại khái là bước 1 là:
>
> Làm sao để Generated image giống với Content.
>
> Chọn l giữa giữa để 'nó' capture cả low level và high level 
> features.
>
> Ta dùng content image và generated image bỏ vào cái VGG network
> để forward prop để lấy ra a(C) và a(G) - Ouput của
> hidden layer thứ L

          <br>

          <a id="node-1791"></a>
          <p align="center"><kbd><img src="assets/0874eb82f6f777e53617e6c50b7a965ec889c1f5.png" width="100%"></kbd></p>
          <br>

      <a id="node-1792"></a>
      - 4.1.2 - Content Cost Function 𝐽𝑐𝑜𝑛𝑡𝑒𝑛𝑡(𝐶,𝐺)
        <br>

          <a id="node-1793"></a>
          <p align="center"><kbd><img src="assets/854c92c84494b23f109361cb9b057d9f1651f9ec.png" width="100%"></kbd></p>
          > Đại khái là sau khi forward prop
> để có a(C) và a(G) ta bỏ vào define một 
> Cost function J_content sao cho minimize 'khoảng cách'
> giữa hai volume: ||(a(C) - a(G))|| ^2 
>
> Trong bài có nói có thể có hoặc không việc 'normalization'

          <br>

      <a id="node-1794"></a>
      - Exercise 1 - compute_content_cost  a_C = content_output[-1] a_G = generated_output[-1]      _, n_H, n_W, n_C = a_G.get_shape().as_list()      a_C_unrolled = tf.reshape(a_C, shape=[_, n_H*n_W, n_C]) a_G_unrolled = tf.reshape(a_G, shape=[_, -1, n_C])      J_content = tf.reduce_sum(         tf.square(             tf.subtract(a_C_unrolled, a_G_unrolled)         )     , axis=None)  J_content = J_content / (4*n_H*n_W*n_C)  \\*What you should remember:\\*  • The content cost takes a hidden layer activation of the neural network, and measures how different  a(𝐶) and 𝑎𝐺) are.  • When you minimize the content cost later, this will help make sure 𝐺 has similar content as 𝐶.
        <br>

          <a id="node-1795"></a>
          <p align="center"><kbd><img src="assets/ccc05dd2d50664ad128f1dff5d08f0e682cdf062.png" width="100%"></kbd></p>
          <br>

          <a id="node-1796"></a>
          <p align="center"><kbd><img src="assets/b1dadb60bc8c92837507e5edd7da78c7812bb010.png" width="100%"></kbd></p>
          <br>

          <a id="node-1797"></a>
          <p align="center"><kbd><img src="assets/0e50ea32c269202c21e79721167dffe4902a6c6b.png" width="100%"></kbd></p>
          <br>

    <a id="node-1798"></a>
    - 4.2 - Computing the Style Cost
      <br>

      <a id="node-1799"></a>
      - 4.2 - Computing the Style Cost
        <br>

          <a id="node-1800"></a>
          <p align="center"><kbd><img src="assets/b886204d898f19f59be3ea01217cc27a629f24ef.png" width="100%"></kbd></p>
          <br>

      <a id="node-1801"></a>
      - 4.2.1 - Style Matrix
        <br>

          <a id="node-1802"></a>
          <p align="center"><kbd><img src="assets/5984cbcad0155c492bef485f3eabd98d687e4520.png" width="100%"></kbd></p>
          <br>

          <a id="node-1803"></a>
          <p align="center"><kbd><img src="assets/69e71c0e2bd4af7baa729fa24da600716d3d1553.png" width="100%"></kbd></p>
          <br>

          <a id="node-1804"></a>
          <p align="center"><kbd><img src="assets/29a207e234ce7f94f8b3bfa36167657e42d3b751.png" width="100%"></kbd></p>
          <p align="center"><kbd><img src="assets/29a207e234ce7f94f8b3bfa36167657e42d3b751.png" width="100%"></kbd></p>
          <p align="center"><kbd><img src="assets/7fe8313e7ab857989666cfa6f1ae39303e1144d2.png" width="100%"></kbd></p>
          <br>

      <a id="node-1805"></a>
      - Exercise 2 - gram_matrix
        <br>

          <a id="node-1806"></a>
          <p align="center"><kbd><img src="assets/5c900060915c700396ad0568947c83d0d4ce905f.png" width="100%"></kbd></p>
          <br>

      <a id="node-1807"></a>
      - 4.2.2 - Style Cost
        <br>

          <a id="node-1808"></a>
          <p align="center"><kbd><img src="assets/af6e6c62dab31c67d6c43dd5bd4dc20b523e63a6.png" width="100%"></kbd></p>
          <br>

      <a id="node-1809"></a>
      - Exercise 3 - compute_layer_style_cost
        <br>

          <a id="node-1810"></a>
          <p align="center"><kbd><img src="assets/9856ba9518305c842f9715b864825d516754429e.png" width="100%"></kbd></p>
          <br>

          <a id="node-1811"></a>
          <p align="center"><kbd><img src="assets/029c947ed3632065c35afb8cf3c3ca629dbbcaa4.png" width="100%"></kbd></p>
          <br>

      <a id="node-1812"></a>
      - 4.2.3 Style Weights  Đại khái là tính J_style với nhiều layer thay vì chỉ một layer nào đó ở giữa giữa network architecture sẽ cho kết quả tốt hơn.  Hiểu đại khái là nếu mình "tính" J_style ảnh hưởng bởi nhiều layer thậm chí tất cả layer thì Generated image sẽ càng giống style với Styled image.  Cho mỗi layer một tham số để control ảnh hưởng nhiều hay ít.
        <br>

          <a id="node-1813"></a>
          <p align="center"><kbd><img src="assets/32c486ac89f315fa4b1a05afa1df48700d35a295.png" width="100%"></kbd></p>
          > Đại khái là tính J_style với nhiều layer thay vì chỉ một layer nào
> đó ở giữa giữa network architecture sẽ cho kết quả tốt hơn.
>
> Hiểu đại khái là nếu mình "tính" J_style ảnh hưởng bởi nhiều
> layer thậm chí tất cả layer thì Generated image sẽ càng giống
> style với Styled image.
>
> Cho mỗi layer một tham số để control ảnh hưởng nhiều hay ít.

          <br>

          <a id="node-1814"></a>
          <p align="center"><kbd><img src="assets/66f463de5cd1e4e6391578537c8b7acb8278c244.png" width="100%"></kbd></p>
          > Ở đây đại khái là chọn mấy layer này (block1_conv1, block2_conv1..)
> mỗi cái đóng góp 20%.

          <br>

      <a id="node-1815"></a>
      - Exercise 4 - compute_style_cost
        <br>

          <a id="node-1816"></a>
          <p align="center"><kbd><img src="assets/109c5c27ec4716b07e780638e3cc0f01e6991ce6.png" width="100%"></kbd></p>
          <br>

          <a id="node-1817"></a>
          <p align="center"><kbd><img src="assets/223e73e56718cf029dadbef40bde3cd32fa2189f.png" width="100%"></kbd></p>
          > Đã hiểu vì sao bỏ thằng cuối, xem minh hoạ

          <br>

      <a id="node-1818"></a>
      - How do you choose the coefficients for each layer? The deeper layers capture higher-level concepts, and the features in the deeper layers are less localized in the image relative to each other. So if you want the generated image to softly follow the style image, try choosing larger weights for deeper layers and smaller weights for the first layers. In contrast, if you want the generated image to strongly follow the style image, try choosing smaller weights for deeper layers and larger weights for the first layers.  What you should remember:  The style of an image can be represented using the Gram matrix of a hidden layer's activations.  You get even better results by combining this representation from multiple different layers.  This is in contrast to the content representation, where usually using just a single hidden layer is sufficient.  Minimizing the style cost will cause the image  𝐺   to follow the style of the image  𝑆
        <br>

      <a id="node-1819"></a>
      - 4.3 - Defining the Total Cost to Optimize
        <br>

      <a id="node-1820"></a>
      - Exercise 5 - total_cost  \\*What you should remember:\\*  • The total cost is a linear combination of the content cost 𝐽𝑐𝑜𝑛𝑡𝑒𝑛𝑡(𝐶,𝐺)  and the style cost 𝐽𝑠𝑡𝑦𝑙𝑒(𝑆,𝐺).  • 𝛼 and 𝛽 are hyperparameters that control the relative weighting between content and style.
        <br>

          <a id="node-1821"></a>
          <p align="center"><kbd><img src="assets/48da65faaed1749831d74fc1fddc1cd46f3cc0d2.png" width="100%"></kbd></p>
          <br>

  <a id="node-1822"></a>
  - 5 - Solving the Optimization Problem
    <br>

    <a id="node-1823"></a>
    - 5 - Solving the Optimization Problem
      <br>

        <a id="node-1824"></a>
        <p align="center"><kbd><img src="assets/c554c6cfc7494f9e024a1a24e32347f2097d6fbc.png" width="100%"></kbd></p>
        <br>

    <a id="node-1825"></a>
    - 5.1 Load the Content Image
      <br>

        <a id="node-1826"></a>
        <p align="center"><kbd><img src="assets/df73fbbe00dcd670ed0fc4fc668466fde9571b7b.png" width="100%"></kbd></p>
        <br>

    <a id="node-1827"></a>
    - 5.2 Load the Style Image
      <br>

        <a id="node-1828"></a>
        <p align="center"><kbd><img src="assets/6128b86b509a4829c22e7d5a6f8de6d6cdf8a4dc.png" width="100%"></kbd></p>
        <br>

    <a id="node-1829"></a>
    - 5.3 Randomly Initialize the Image to be Generated
      <br>

        <a id="node-1830"></a>
        <p align="center"><kbd><img src="assets/4322050c4cf785727a90cd26187ab13c299327d7.png" width="100%"></kbd></p>
        <br>

    <a id="node-1831"></a>
    - 5.4 - Load Pre-trained VGG19 Model
      <br>

        <a id="node-1832"></a>
        <p align="center"><kbd><img src="assets/b0506e384a2061fd2434df6eb3faec892b573e64.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/b0506e384a2061fd2434df6eb3faec892b573e64.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/20050afc9a877ef7b44dcefaca6c4a836cb18c7c.png" width="100%"></kbd></p>
        > This is a Python function that takes a pre-trained VGG model (vgg) and a
> list of layer names (layer_names) as inputs and returns a new Keras model
> that outputs the intermediate activations of the specified layers.
>
> The function first creates a list of output tensors by using a list
> comprehension to iterate over layer_names and extract the output tensor
> for each layer from the vgg model. Specifically, for each layer in
> layer_names, it gets the output tensor of that layer from the vgg model
> using vgg.get_layer(layer[0]).output. The output tensor is then added to the
> outputs list.
>
> After collecting the output tensors for all the specified layers, the function
> creates a new Keras model that takes the vgg model's input tensor as input
> and outputs a list of the intermediate activation tensors corresponding to
> the specified layers. The Model function in Keras is used to create this new
> model, and the outputs list and vgg.input tensor are passed as arguments
> to it.
>
> Finally, the function returns the **newly created Keras model**that outputs the
> intermediate activations of the specified layers.

        <br>

    <a id="node-1833"></a>
    - 5.5 - Compute Total Cost
      <br>

      <a id="node-1834"></a>
      - 5.5.1 - Compute Content Cost
        <br>

          <a id="node-1835"></a>
          <p align="center"><kbd><img src="assets/fb281841c6328f5575e0fef5e68f4830df7c8def.png" width="100%"></kbd></p>
          <br>

      <a id="node-1836"></a>
      - 5.5.2 - Compute Style Cost
        <br>

          <a id="node-1837"></a>
          <p align="center"><kbd><img src="assets/b158de9bf3c67d2252dee57e8cc146222cafc3b4.png" width="100%"></kbd></p>
          <br>

          <a id="node-1838"></a>
          <p align="center"><kbd><img src="assets/cdf68f4c015f6c3de0e9a53d5b2c5f05d8707b73.png" width="100%"></kbd></p>
          <br>

      <a id="node-1839"></a>
      - Exercise 6 - train_step
        <br>

          <a id="node-1840"></a>
          <p align="center"><kbd><img src="assets/84a65f98dee0f5d47443ff9d4f6535ec22c49f00.png" width="100%"></kbd></p>
          <br>

    <a id="node-1841"></a>
    - 5.6 - Train the Model
      <br>

        <a id="node-1842"></a>
        <p align="center"><kbd><img src="assets/4548bc6e9d53cf4f963acc6e82ca0ddc3b75524f.png" width="100%"></kbd></p>
        <br>

        <a id="node-1843"></a>
        <p align="center"><kbd><img src="assets/c4ede7c64adfb78e242899b24706782de0c61825.png" width="100%"></kbd></p>
        <br>

        <a id="node-1844"></a>
        <p align="center"><kbd><img src="assets/bf390895e2fbd17319787fd7d9127d4345c621e2.png" width="100%"></kbd></p>
        <br>

        <a id="node-1845"></a>
        <p align="center"><kbd><img src="assets/0f56226faa5d00efad804ea2bbbdecb4a5f8a9bb.png" width="100%"></kbd></p>
        <br>

    <a id="node-1846"></a>
    - \\*Conclusion:  \\*Great job on completing this assignment! You are now able to use Neural Style Transfer to generate artistic images. This is also your first time building a model in which the optimization algorithm updates the pixel values rather than the neural network's parameters. Deep learning has many different types of models and this is only one of them!  \\*What you should remember:  \\* • Neural Style Transfer is an algorithm that given a content image C and a style image S can generate an artistic image  • It uses representations (hidden layer activations) based on a pretrained ConvNet.  • The content cost function is computed using one hidden layer's activations.  • The style cost function for one layer is computed using the Gram matrix of that layer's activations. The overall style cost function is obtained using several hidden layers.  • Optimizing the total cost function results in synthesizing new images.
      <br>

    <a id="node-1847"></a>
    - 6 - Test With Your Own Image (Optional/Ungraded)
      > SẼ QUAY LẠI
> LÀM SAU

      <br>

      <a id="node-1848"></a>
      - Here are some ideas on how to tune your hyperparameters:  To select different layers to represent the style, redefine STYLE_LAYERS  To alter the number of iterations you want to run the algorithm, try changing epochs given in Section 5.6.  To alter the relative weight of content versus style, try altering alpha and beta values  Happy coding!
        <br>

    <a id="node-1849"></a>
    - 7 - References  The Neural Style Transfer algorithm was due to Gatys et al. (2015). Harish Narayanan and Github user "log0" also have highly readable write-ups this lab was inspired by. The pre-trained network used in this implementation is a VGG network, which is due to Simonyan and Zisserman (2015). Pre-trained weights were from the work of the MathConvNet team.  • Leon A. Gatys, Alexander S. Ecker, Matthias Bethge, (2015). \\_A Neural Algorithm of Artistic Style \\_  • Harish Narayanan, \\_Convolutional neural networks for artistic style transfer. \\_  • Log0, \\_TensorFlow Implementation of "A Neural Algorithm of Artistic Style". \\_  • Karen Simonyan and Andrew Zisserman (2015). \\_Very deep convolutional networks for large-scale image recognition \\_  • \\_MatConvNet.\\_
      <br>

