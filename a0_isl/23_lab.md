# 2.3 Lab

📊 **Progress:** `14` Notes | `19` Screenshots

---

<a id="node-69"></a>
## 2.3.1 Basic Commands

<br>


<a id="node-70"></a>
### ?function name để coi help

<br>


<a id="node-71"></a>
### matrix(c(1,2,3,4), 2, 2, byrow=TRUE)

> [!NOTE]
> matrix(c(1,2,3,4), 2, 2, byrow=TRUE)
> sẽ cho ra matrix 2x2 với các giá trị từ vector 
> [1,2,3,4] và rải theo từng hàng (byrow = TRUE)

<br>


<a id="node-72"></a>
### set.seed(a number bất kì):

> [!NOTE]
> set.seed(a number bất kì): 
>
> Đại khái là nếu mình dùng đúng con số mà
> họ set.seed thì gọi random sẽ ra đúng như họ. Từ đây
> hiểu vụ setSeed trong Python.

<br>


<a id="node-73"></a>
### rnorm()

> [!NOTE]
> rnorm()
>
> rnorm(100) cho ra vector có 100 unit, lấy random theo
> normal distribution. Có thể khai thêm arg để set mean
> & stan.dev

<br>


<a id="node-74"></a>
### mean(y), var(y), sd(y) tính mean, variance (sd**2), và

> [!NOTE]
> mean(y), var(y), sd(y) tính mean, variance (sd**2), và 
> standard deviation (sd) của y

<br>


<a id="node-75"></a>
## 2.3.2 Graphics

<br>


<a id="node-76"></a>
### plot()

> [!NOTE]
> plot() 
>
> > x = rnorm(100)
> > y = rnorm(100)
> > plot(x, y)
> > plot(x, y, xlab = "this is the x-axis", ylab = "this is the y-axis", 
> main = "Plot of X vs Y", col = "red")

<br>

<a id="node-77"></a>

<p align="center"><kbd><img src="assets/8157fe5e12d822e8296c68098dfc3bb4e1d2163c.png" width="100%"></kbd></p>

  <br>


<a id="node-78"></a>
### X = \\*seq(1:10)\\* hay chỉ cần gõ

> [!NOTE]
> X = \**seq(1:10)\** hay chỉ cần gõ
> \**1:10\** cho ra 1,2,3...10

<br>


<a id="node-79"></a>
### x = seq(-pi, pi, length = 50)

> [!NOTE]
> x = seq(-pi, pi, length = 50)
> y = x
> f = outer(x, y, function(x,y) cos(y) / (1 + x^2))
> \**contour\**(x, y, f)

<br>

<a id="node-80"></a>

<p align="center"><kbd><img src="assets/aa05c690b686cd2b1f4c08ef171f8d5fb12c4b6a.png" width="100%"></kbd></p>

  <br>

<a id="node-81"></a>

<p align="center"><kbd><img src="assets/8698620862e55b2c16543848324928c253a107a1.png" width="100%"></kbd></p>

> [!NOTE]
> contour(x, y, f, nlevels = 45, add = T)

  <br>

<a id="node-82"></a>

<p align="center"><kbd><img src="assets/f49dd6ceb4875c7895f9140d5532baf3a5129531.png" width="100%"></kbd></p>

> [!NOTE]
> fa = (f - t(f)) / 2
> > contour(x, y, f, nlevels = 15)

  <br>


<a id="node-83"></a>
### image(x, y, fa) tương tự contour nhưng

> [!NOTE]
> image(x, y, fa) tương tự contour nhưng
> in ra dạng color-coded plot còn gọi là heatmap

<br>

<a id="node-84"></a>

<p align="center"><kbd><img src="assets/4887efda80cc1ea4e2eb07b0ac98e53c5d01ef8b.png" width="100%"></kbd></p>

  <br>


<a id="node-85"></a>
### persp(x, y, fa, theta = 30, phi = 20)

> [!NOTE]
> persp(x, y, fa, theta = 30, phi = 20)
> thì giúp tạo ảnh 3D

<br>

<a id="node-86"></a>

<p align="center"><kbd><img src="assets/b3e8106b2df695f0bba213feb9cb8c309e45b28f.png" width="100%"></kbd></p>

  <br>


<a id="node-87"></a>
## 2.3.3 Indexing Data

<br>

<a id="node-88"></a>

<p align="center"><kbd><img src="assets/7ee1590e261a83202e399d930a2fb9814a4859a7.png" width="100%"></kbd></p>

> [!NOTE]
> A = matrix(1:16,4,4) tạo matrix 4x4 A với các giá
> trị từ 1,2,3..16 rải thành từng cột (muốn rải theo
> hàng thì define byrow = T)
>
> Và lấy ra thì bình thường như A[i,j]
>
> Nhưng cũng có thể lấy nhiều hàng, nhiều cột,
> ở đây lấy hàng 1,2 (chú ý là nó index từ 1)
> và cột 3,4

<br>

<a id="node-89"></a>

<p align="center"><kbd><img src="assets/558601ef65ab13147ead2b8536ebc8bcb31b5a9c.png" width="100%"></kbd></p>

> [!NOTE]
> Lấy mọi hàng từ hàng 1 tới N
> (ở đây là 2), mọi cột

<br>

<a id="node-90"></a>

<p align="center"><kbd><img src="assets/14ffdf8e789f960daa12dc9f7ea55a6c33b1f58d.png" width="100%"></kbd></p>

> [!NOTE]
> Lấy mọi cột từ 1
> tới 3, mọi hàng

<br>

<a id="node-91"></a>

<p align="center"><kbd><img src="assets/b0cb9b656c22796f732d02df76542b5c5b084405.png" width="100%"></kbd></p>

> [!NOTE]
> Lấy mọi hàng trừ hai hàng 1,2 kết
> quả nó ra còn hai hàng 3,4. Cột
> thì lấy mọi cột

<br>

<a id="node-92"></a>

<p align="center"><kbd><img src="assets/f9e4e5a8a791602359d34127b25814aa46514197.png" width="100%"></kbd></p>

> [!NOTE]
> Trừ hàng 1,2 cột 3,4 còn lại 
> lấy hết như vậy kết quả nó là
> hàng 3,4 và hai cột đầu của A

<br>


<a id="node-93"></a>
## 2.3.4 Load Data

<br>


<a id="node-94"></a>
### Đầu tiên để load table Auto.data (file text) có

> [!NOTE]
> Đầu tiên để load table Auto.data (file text) có
> thể dùng read.table(file path)

<br>

<a id="node-95"></a>

<p align="center"><kbd><img src="assets/8c9ccdd8795aca09c90b77d980615908925b23c6.png" width="100%"></kbd></p>

> [!NOTE]
> Auto = read.table("~/Desktop/Learn ML/****STAT/Auto.data")
> View(Auto)
>
> Nhưng (load) với kiểu này ta sẽ tính luôn header thành 1 row

  <br>

<a id="node-96"></a>

<p align="center"><kbd><img src="assets/f9d9c4d8994a155e825ded17b0e29559a5e25fc0.png" width="100%"></kbd></p>

> [!NOTE]
> Auto = **read.table**("~/Desktop/Learn ML/****STAT/Auto.data", **header** = T, 
> **na.strings** = "?", **stringsAsFactors** = T)
>
> View(Auto)
>
> Nên có thể dùng argument **header = T (TRUE)**để cho R biết **dòng đầu là
> header.**
>
> Còn **na.strings = "?"** giúp R biết k**hi nào nó gặp kí tự này** thì nó biết đó là
> **chỗ bị miss data.**
>
> Còn **stringssAsFactors** = True sẽ cho R biết **chỗ nào là string** thì treat
> nó như factor = category hay ở trong đây gọi là **quantitative variable**

> [!NOTE]
> Tiếp theo nói về cách dễ hơn để load table vào R
> đó là dùng csv: Save table như excel file thành csv 
> và dùng **read.csv**
>
> Dùng **dim**() để xem dimension (shape) of table
>
> > dim(Auto)
> [1] 397   9
>
>
> và **names**() để in các feature (column) của table
>
> > names(Auto)
> [1] "mpg"          "cylinders"    "displacement" "horsepower"   "weight"       "acceleration" "year"        
> [8] "origin"       "name"

  <br>


<a id="node-97"></a>
## 2.3.5 Additional Graphical & Numerical Summaries

<br>


<a id="node-98"></a>
### \\*plot\\*(Auto$\\*cylinders\\*, Auto$\\*mpg\\*, col = 'red')

> [!NOTE]
> \**plot\**(Auto$\**cylinders\**, Auto$\**mpg\**, col = 'red')
>
> Để access feature của table thì dùng $
>
> Nếu gọi attach(Auto) thì R sẽ biết các
> variable (feature) của Auto và từ đó có thể 
> gọi tên feature khơi khơi
>
> attach(Auto)
> plot(cylinder, mpg, col = 'red')

<br>

<a id="node-99"></a>

<p align="center"><kbd><img src="assets/7fb9e0aa99fa976dc0ffd80c0ce629a6d6e3bd17.png" width="100%"></kbd></p>

  <br>


<a id="node-100"></a>
### hist(): In histogram

<br>

<a id="node-101"></a>

<p align="center"><kbd><img src="assets/765e028a9a7713ebcf9399d662e57b1c61bed1e7.png" width="100%"></kbd></p>

> [!NOTE]
> hist(mpg)

  <br>


<a id="node-102"></a>
### pairs(): In scatter plot

> [!NOTE]
> pairs(): In scatter plot
> với mọi cặp feature

<br>

<a id="node-103"></a>

<p align="center"><kbd><img src="assets/edc80684fb9ad5eeabe7b95e6d85485324d3e52e.png" width="100%"></kbd></p>

> [!NOTE]
> pairs(Auto, col = "blue")

  <br>

<a id="node-104"></a>

<p align="center"><kbd><img src="assets/a424514753a0d9f203c4d55c670a5e7a948e4097.png" width="100%"></kbd></p>

> [!NOTE]
> Cũng có thể chỉ in vài cặp:
>
> pairs(~ mpg + displacement + horsepower + weight +
> acceleration, data = Auto, col = "purple")

  <br>


<a id="node-105"></a>
### identify() đại khái là cho phép chọn

> [!NOTE]
> identify() đại khái là cho phép chọn
> trên plot và khi bấm escape thì nó in
> ra các variable value

<br>

<a id="node-106"></a>

<p align="center"><kbd><img src="assets/c36f581b6e4fea2e8ec62b8c6f632011594baa95.png" width="100%"></kbd></p>

> [!NOTE]
> plot(horsepower, mpg, col = 'red')
> identity(horsepower, mpg, name)
>
> Chọn vài điểm trên plot, và escape

  <br>


<a id="node-107"></a>
### summary(Auto) cho các thông số statistic

> [!NOTE]
> summary(Auto) cho các thông số statistic
> của các variable
>
> hoặc chỉ một variable nào đó
> summary(feature name)

<br>

<a id="node-108"></a>

<p align="center"><kbd><img src="assets/deb205761044fb5ed0ded0eae2d3284e9ffa1acf.png" width="100%"></kbd></p>

  <br>

