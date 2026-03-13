# C1w1_introduction To N.n

📊 **Progress:** `4` Notes | `24` Screenshots

---

<a id="node-3"></a>
## What's A Neural Network

<br>


<a id="node-4"></a>
### The term "Deep Learning" refers to training Neural Networks, sometimes very

> [!NOTE]
> The term "Deep Learning" refers to training Neural Networks, sometimes very
> large Neural Networks.
>
> A Neural Network is a function that can be used to predict outcomes based on
> inputs, often implemented using neurons.
>
> Neurons are individual units in a Neural Network that receive input and generate
> output based on a set of weights and biases.
>
> A simple example of a Neural Network is using linear regression to predict
> housing prices based on house size.
>
> In the example, the input (house size) goes through a single neuron that applies
> a linear function and a ReLU function to generate the predicted price.
>
> A larger Neural Network can be built by stacking multiple neurons together to
> handle more complex inputs and outputs.
>
> The process of training a Neural Network involves giving it input/output pairs and
> adjusting the weights and biases of the neurons to minimize prediction error.
>
> A more complex Neural Network can be used to predict housing prices based on
> multiple features such as number of bedrooms, zip code, and walkability.

<br>

<a id="node-5"></a>

<p align="center"><kbd><img src="assets/047ede4aba8ac38a153f13d99d553569d49b65d7.png" width="100%"></kbd></p>

<br>

<a id="node-6"></a>

<p align="center"><kbd><img src="assets/0f53d0a843c2e870295868676a8370683ea47a8c.png" width="100%"></kbd></p>

<br>

<a id="node-7"></a>

<p align="center"><kbd><img src="assets/d1785f2bfc81e1e305b529ca9234c64ed0121fa4.png" width="100%"></kbd></p>

<br>


<a id="node-8"></a>
## Supervised Learning With N.n

<br>


<a id="node-9"></a>
### 1 The majority of economic value created by neural networks has been through

> [!NOTE]
> 1 The majority of economic value created by neural networks has been through
> supervised learning.
>
> 2 Various applications of neural networks include online advertising, computer
> vision, speech recognition, machine translation, and autonomous driving.
>
> 3 Different types of neural networks are useful for different applications, such as
> convolutional neural networks (CNNs) for image applications and recurrent
> neural networks (RNNs) for sequence data.
>
> 4 Standard CNN and RNN architectures are used for image and
> one-dimensional sequence data, respectively.
>
> 5 Machine learning can be applied to structured data and unstructured data.
>
> 6 Structured data refers to databases of data, while unstructured data includes
> audio, images, and text.

> [!NOTE]
> 1 What is the main focus of the discussion?
> The main focus of the discussion is the various applications of neural networks, specifically the success of supervised learning in creating economic value.
>  2 What is supervised learning?
> Supervised learning is a type of machine learning in which the algorithm is trained on labeled data, with input/output pairs. The algorithm learns to predict the output given the input, and is optimized to minimize the error between predicted and actual output.
>  3 What are some examples of successful applications of neural networks?
> Neural networks have been applied effectively to online advertising, computer vision, speech recognition, machine translation, and autonomous driving, among other applications.
>  4 How are different types of neural networks used for different applications?
> Different types of neural networks are used for different applications based on the characteristics of the data being analyzed. For example, convolutional neural networks (CNNs) are used for image applications, while recurrent neural networks (RNNs) are used for sequence data.
>  5 What is the difference between structured and unstructured data?
> Structured data refers to data that is organized in a database, with well-defined columns and meanings for each feature. Unstructured data, on the other hand, refers to data such as raw audio, images, or text, which do not have a predetermined structure.

<br>

<a id="node-10"></a>

<p align="center"><kbd><img src="assets/5e184806b919a7581abf8f355d01cd394c7330c5.png" width="100%"></kbd></p>

<br>

<a id="node-11"></a>

<p align="center"><kbd><img src="assets/49851338fe224c30ebb368bc5391468a18333a18.png" width="100%"></kbd></p>

<br>

<a id="node-12"></a>

<p align="center"><kbd><img src="assets/3de1fb15806b1c75e77d55f66dcc223654fd648c.png" width="100%"></kbd></p>

<br>


<a id="node-13"></a>
## Why Is Deep Learning Taking Off?

<br>


<a id="node-14"></a>
### Sure, here is a more detailed answer with indexed points:  1 The video discusses the reasons behind the

> [!NOTE]
> Sure, here is a more detailed answer with indexed points:  1 The video discusses the reasons behind the
> rise of deep learning, despite the fact that the basic technical ideas behind deep learning have been
> around for decades.
>
> 2 The main driver behind the rise of deep learning is the amount of data that is now available for various
> tasks, such as spam classification, ad click prediction, and self-driving cars.
>
> 3 Traditional learning algorithms like support vector machines or logistic regression show a plateau in
> performance after a certain point, as the amount of data increases.
>
> 4 However, with deep learning, the performance can continue to improve as more data is added, and the
> neural network size increases.
>
> 5 This is because deep learning algorithms can take advantage of the huge amounts of data that are now
> available, and larger neural networks can be trained to process that data.
>
> 6 In fact, today, the most reliable way to improve the performance of a neural network is to either train a
> larger network or to add more data.
>
> 7 The amount of labeled data is plotted on the x-axis in the video, where labeled data refers to the training
> examples with both input X and label Y.
>
> 8 In the regime of smaller training sets, the relative ordering of the algorithms is not well defined, and
> performance depends more on the skill of the engineer at hand-engineering features.
>
> 9 However, in the regime of very large training sets, very large M, neural networks are seen to dominate
> the other approaches.
>
> 10 The rise of deep learning has been made possible by the scale of data and the scale of computation,
> such as the ability to train large neural networks on CPUs or GPUs.
>
> 11 Additionally, there have been significant algorithmic innovations in deep learning that have made neural
> networks faster, such as the switch from sigmoid to ReLU activation functions.
>
> 12 Overall, deep learning has taken off due to the combination of scale, both in terms of data and
> computation, and significant algorithmic innovations.

<br>

<a id="node-15"></a>

<p align="center"><kbd><img src="assets/c4b78debf67c85d1776bd65c9bf8af063e82121d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là:..
>
> Những algorithm 'cũ' như SVM khi có nhiều data nó sẽ tốt hơn nhưng
>  vẫn bị giới hạn, đại khái là sẽ không biết làm gì với quá nhiều data.
>
> Còn n.n phức tạp thì càng nhiều data nó càng tốt.
>
> Muốn n.n perform tốt thì phải 1-Nhiều data, 2-Phức tạp
>
> Do 'Big data' có được từ
> digitalization, sự phát triển của
> Camera, Mobile phone,...
>
> Nếu 'Small training set' thì performance sẽ tuỳ thuộc vào
> skill của con người như 'feature engineering' nên một model
> bằng SVM làm tốt có thể vượt trội n.n. Tuy nhiên nếu ở phân khúc
> 'Big data' thì Big n.n sẽ vượt trội những algorithm khác.

<br>

<a id="node-16"></a>

<p align="center"><kbd><img src="assets/d11c63177367cf8357d5e1b0e8b98f83763465bc.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là:..
>
> Máy tính nhanh hơn giúp tăng tốc Quá trình Idea - Thử - Điều chỉnh
>
> Những algorithm mới cũng giúp quá trình 'Training' nhanh hơn
> ví dụ thay Sigmoid bằng Relu.

<br>

<a id="node-17"></a>

<p align="center"><kbd><img src="assets/2b0bbdc1bee5389a45eb0a6d2927eb51f38f269a.png" width="100%"></kbd></p>

> [!NOTE]
> Data, sự phát triển của phần cứng sẽ giúp
> Deep learning còn phát triển nữa trong những năm tới.

<br>

<a id="node-18"></a>

<p align="center"><kbd><img src="assets/89b837dc4818b737cf4cb8ea97dc488792f18476.png" width="100%"></kbd></p>

<br>


<a id="node-19"></a>
## About This Course

<br>


<a id="node-20"></a>
### The speaker gives an overview of the first course in a deep learning specialization,

> [!NOTE]
> The speaker gives an overview of the first course in a deep learning specialization,
> which comprises five courses. The first course covers the most important
> foundations of deep learning, including building and working with a deep neural
> network. The course is four weeks long, with each week covering new material and
> including 10 multiple-choice questions to check understanding. In week two, learners
> will learn about the basics of neural network programming and practice implementing
> the algorithms through a programming exercise. In week three, learners will code up
> a single hidden layer neural network, and in week four, they will build a deep neural
> network with many layers. The speaker encourages learners to take the
> multiple-choice questions seriously and to use them to check their understanding of
> the material.

<br>

<a id="node-21"></a>

<p align="center"><kbd><img src="assets/e2e0106d289d153b862daf8399dbf43325da35b5.png" width="100%"></kbd></p>

<br>

<a id="node-22"></a>

<p align="center"><kbd><img src="assets/10ce639d3a93d2824ddc5e37e0ebc885af38784e.png" width="100%"></kbd></p>

<br>


<a id="node-23"></a>
## Quiz

<br>

<a id="node-24"></a>

<p align="center"><kbd><img src="assets/96bbc6dc05891eb8a50b0c266b79b67ad24c93c0.png" width="100%"></kbd></p>

<br>

<a id="node-25"></a>

<p align="center"><kbd><img src="assets/4c19abf2411236fdefbfd525311bd4b87ff333b6.png" width="100%"></kbd></p>

<br>

<a id="node-26"></a>

<p align="center"><kbd><img src="assets/854a46c66c81c6f6287a47a34d77feb568c1c6db.png" width="100%"></kbd></p>

<br>

<a id="node-27"></a>

<p align="center"><kbd><img src="assets/2ef0f96fdae7705729a3f7e1e2dbbaab2a0520cb.png" width="100%"></kbd></p>

<br>

<a id="node-28"></a>

<p align="center"><kbd><img src="assets/85b76c884c6dc7bf0079ed2c47fd1d9d3050f14a.png" width="100%"></kbd></p>

<br>

<a id="node-29"></a>

<p align="center"><kbd><img src="assets/b07d45d5fb4099fba0a8e9702dd2c63bc7a5e52c.png" width="100%"></kbd></p>

<br>

<a id="node-30"></a>

<p align="center"><kbd><img src="assets/06af8741e6069b099c80b294977aba96933ff130.png" width="100%"></kbd></p>

<br>

<a id="node-31"></a>

<p align="center"><kbd><img src="assets/dd80916bc07cda0bd6100f0db211c9bf0f61efc2.png" width="100%"></kbd></p>

<br>

<a id="node-32"></a>

<p align="center"><kbd><img src="assets/c31108add0817f3f045018cc00e99b826f42589d.png" width="100%"></kbd></p>

<br>

<a id="node-33"></a>

<p align="center"><kbd><img src="assets/ecf0fdc25a9410c5cadf70dabd7457acbd98e3a4.png" width="100%"></kbd></p>

<br>

<a id="node-34"></a>

<p align="center"><kbd><img src="assets/cb6225514ebe143c93d6b6c7e35f981522875166.png" width="100%"></kbd></p>

<br>

<a id="node-35"></a>

<p align="center"><kbd><img src="assets/f0669181ab0316ec6fff8902e32bdc2b80f5120a.png" width="100%"></kbd></p>

<br>

