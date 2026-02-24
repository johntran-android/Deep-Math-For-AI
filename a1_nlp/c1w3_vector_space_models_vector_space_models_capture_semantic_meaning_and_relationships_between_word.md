# C1W3 - VECTOR SPACE MODELS  Vector space models \\*capture semantic meaning\\* and r\\*elationships between words. \\* You'll learn how to \\*create word vectors\\* that \\*capture dependencies between words\\*,  then \\*visualize\\* \\*their relationships\\* in two dimensions using \\*PCA\\*. \\* Learning Objectives \\*  • Covariance matrices  • Dimensionality reduction  • Principal component analysis  • Cosine similarity  • Euclidean distance  • Co-occurrence matrices  • Vector representations 

📊 **Progress:** `80` Notes | `126` Screenshots

---

<a id="node-348"></a>
## Introduction

<br>


<a id="node-349"></a>
### 1 Understanding v\\*ector spaces\\* in NLP

> [!NOTE]
> 1 Understanding v\**ector spaces\** in NLP
>
> 2 Representing \**word\** \**vectors\** as numerical codes
>
> 3 Two methods for \**comparing different word vectors\**:
> \**Euclidean distance\** and\**cosine similarity\**
>
> 4 \**Plotting\** `high-dimensional` word vectors in a \**2D
> plane\**
>
> 5 \**Clustering\** \**similar words\** together in the plot

<br>


<a id="node-350"></a>
## Vector Space Models

<br>


<a id="node-351"></a>
### 1 Introduction to \\*vector space\\* models and their applications in

> [!NOTE]
> 1 Introduction to \**vector space\** models and their applications in
> \**NLP\**.
>
> 2 \**Vector space models\** can \**encode\** different \**types of information\**
> and \**capture word relationships\**.
>
> 3 Examples of how \**vector space\** models can be used in question
> \**answering\**, \**paraphrasing\**, \**summarization\**, \**information extraction\**,
> \**machine translatio\**n, and \**chat\** programming.
>
> 4 \**Representing words\** and documents \**as vectors\** using \**context\**
> and \**cooccurrence matrices\**.
>
> 5 John Firth's quote\**"You shall know a word by the company it
> keeps\**" as a fundamental concept in NLP.
>
> 6 Next video will cover \**building vector space models\** from scratch
> using \**cooccurrence matrices\**.

<br>

  <a id="node-352"></a>
  <p align="center"><kbd><img src="assets/ed201cd8a972eb17e25040c9895a1d5ed6fc6201.png" width="100%"></kbd></p>
  <br>

  <a id="node-353"></a>
  <p align="center"><kbd><img src="assets/a0be7d63f67ada91a7337520c0cdbc070ae550f6.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là **vector space** sẽ giúp giải quyết được vấn đề như
  > này một cái là **2 câu gần như giống nhau** nhưng **nghĩa
  > hoàn toàn khác xa** còn **2 câu nhìn thì khác xa** nhưng
  > n**ghĩa lại giống nhau**

  <br>

  <a id="node-354"></a>
  <p align="center"><kbd><img src="assets/2fd843c05b6152433c290aabcc83dfea86cfb718.png" width="100%"></kbd></p>
  > [!NOTE]
  > Nó cũng sẽ giúp **nắm bắt được sự liên quan
  > giữa các từ** trong câu và ứng dụng trong rất
  > nhiều lĩnh vực

  <br>

  <a id="node-355"></a>
  <p align="center"><kbd><img src="assets/f3c960126c8799e0c632d3d7eb20d2f39ba04ecc.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là represent một word sao cho **nắm bắt được tất cả
  > những thông tin context xung quanh nó** từ đó hiểu được trọn vẹn ý
  > nghĩa của từ

  <br>

  <a id="node-356"></a>
  <p align="center"><kbd><img src="assets/d2591cb5117e1484be09fa18a90417ba4bff2ea8.png" width="100%"></kbd></p>
  <br>

  <a id="node-357"></a>
  <p align="center"><kbd><img src="assets/ba2b814957529d069ea2b6f4ec6aac3b6332d5d4.png" width="100%"></kbd></p>
  <br>


<a id="node-358"></a>
## Word By Word And Word By Doc

<br>


<a id="node-359"></a>
### 1 Introduction to \\*constructing vectors\\* based on `\\*co-occurrence` matrix\\*

> [!NOTE]
> 1 Introduction to \**constructing vectors\** based on \**co-occurrence matrix\**
>
> 2 \**Different designs\** for constructing vector space models for words and
> documents
>
> 3 \**Co-occurrence\** matrix and \**vector representations\** for words in the \**corpus\**
>
> 4 \**Co-occurrence of words in documents\** and \**vector representations for
> documents in the corpus\**
>
> 5 Creating a \**vector space\** by taking representations for multiple sets of
> documents or words
>
> 6 \**Comparing\** vector representations using \**cosine similarity \**and \**Euclidean
> distance\**
>
> 7 Importance of \**similarity metrics\** in vector spaces
>
> 8 Summary of the main ideas and a teaser for the next video on \**Euclidean
> distance\** similarity metric.

<br>

  <a id="node-360"></a>
  <p align="center"><kbd><img src="assets/c2a671d92ef2b78839a231f13453dc703a539a89.png" width="100%"></kbd></p>
  <br>

  <a id="node-361"></a>
  <p align="center"><kbd><img src="assets/9343a6017d93de7e109be7ae76d6a5a7ffc5f34c.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là dựa vào nhận định ở bài trước, rằng ý nghĩa một từ có thể được
  > xác định bằng các từ hay vây quanh nó, ta có thể có cách thức đầu tiên để
  > xây dựng word vector như sau. Xét một corpus, ta sẽ thống kê xem trong
  > một phạm vi nhất định, thì có bao nhiêu lần một từ xuất hiện trong phạm vi
  > đó với một từ khác, để rồi tạo ra `co-occurrence` matrix. Và dựa vào các chỉ
  > số thống kê này, để tạo word vector. Ví dụ trong corpus gồm 2 câu như trong
  > hình, xây dựng vector cho từ "data" dựa trên số lần các từ khác xuất hiện
  > trong phạm vi gần nó
  >
  > Cho k bằng 2 thì đv từ '**data**' thì trong khoảng **K** này các từ khác **xuất
  > hiện nhiều hay ít** (mấy lần) từ đó xây dựng**vector represent** cho từ 'data'
  > ..
  >
  > Với cách tạo vector này có thể thấy n**hững từ mà có liên quan đến nhau sẽ
  > có xu hướng xuất hiện gần nhau** nhiều nên sẽ cao hơn

  <br>

  <a id="node-362"></a>
  <p align="center"><kbd><img src="assets/973c5e2665992f25352c95338b251873e6774885.png" width="100%"></kbd></p>
  > [!NOTE]
  > Còn cái này thì đại khái cũng tạo vector bằng số lần từ này **xuất
  > hiện trong 1 corpus thuộc lĩnh vực** nào đó. Như từ **data** với véctơ
  > như vậy sẽ dễ thấy nó **liên quan nhiều đến máy tính** còn **film** thì
  > **liên quan nhiều đến giải trí**

  <br>

  <a id="node-363"></a>
  <p align="center"><kbd><img src="assets/4ae56ed80ea1c022832cb31b6d28062341442f2b.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là vẽ ra như này sẽ thấy **'data' có tính economy và ML
  > còn film có tính entertainment nhiều hơn.**
  >
  > Đồng thời cũng cho thấy lĩnh vực **ML và Economy thì gần nhau
  > hơn là ML với Entertainment**
  >
  > Và để cụ thể hoá tính chất gần nhau đó thì người ta dùng thước 
  > đo **Angle** và **Distance** của các vector

  <br>

  <a id="node-364"></a>
  <p align="center"><kbd><img src="assets/22e868f11b9e0c9cad68903fc7d563a70bb22830.png" width="100%"></kbd></p>
  <br>

  <a id="node-365"></a>
  <p align="center"><kbd><img src="assets/16b952d2e548d3eb61b7f4eee0a9b2cc52932e8e.png" width="100%"></kbd></p>
  <br>

  <a id="node-366"></a>
  <p align="center"><kbd><img src="assets/46bcfdb99a732641ee3cfaf50c1cb19895ebcaa7.png" width="100%"></kbd></p>
  <br>

  <a id="node-367"></a>
  <p align="center"><kbd><img src="assets/f884a0a4c59bfebb0e34057ace55869a9bf0b1f3.png" width="100%"></kbd></p>
  <br>


<a id="node-368"></a>
## Linear Algebra In Python With Numpy

<br>


<a id="node-369"></a>
### In this lab, you will have the opportunity to remember some

> [!NOTE]
> In this lab, you will have the opportunity to remember some
> \**basic concepts \**about \**linear algebra\** and how to use them in
> \**Python\**.
>
> \**Numpy\** is one of the \**most used libraries\** in Python for \**arrays
> manipulation\**. It adds to Python a set of functions that allows
> us to \**operate on large multidimensional arrays\** with just a few
> lines. So forget about writing nested loops for adding
> matrices! With NumPy, this is as simple as adding numbers.
>
> Let us \**import\** the numpy library and assign the alias \**np\** for it.
> We will follow this convention in almost every notebook in this
> course, and you'll see this in many resources outside this
> course as well.

<br>

<a id="node-370"></a>
- import numpy as \\*np\\*  # The swiss knife of the data scientist.
  <br>

<a id="node-371"></a>
- Defining lists and numpy arrays
  <br>

  <a id="node-372"></a>
  - alist `=` [1, 2, 3, 4, 5]   # Define a python list. It looks like an np array narray `=` \\*np.array\\*([1, 2, 3, 4]) # Define a numpy array
    <p align="center"><kbd><img src="assets/9025b862fd765dfaa26b1cc582966c8c63deae2f.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/9025b862fd765dfaa26b1cc582966c8c63deae2f.png" width="100%"></kbd></p>
    <br>

<a id="node-373"></a>
- Algebraic operators on NumPy arrays vs. Python lists
  <br>

  <a id="node-374"></a>
  - One of the \\*common\\* beginner \\*mistakes\\* is to \\*mix up\\* the concepts of \\*NumPy\\* arrays and \\*Python lists\\*. Just observe the next example, where we \\*add\\* two objects of the two mentioned types.  Note that the `\\*'+'\\*` operator on NumPy arrays perform an `\\*element-wise` addition\\*, while the same operation on \\*Python\\* \\*lists\\* results in a \\*list concatenatio\\*n. Be careful while coding. Knowing this can \\*save many headaches.\\*
    <br>

    <a id="node-375"></a>
    - print(narray `\\*+\\*` narray) print(alist `\\*+\\*` alist)  [2 4 6 8] [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
      > [!NOTE]
      > Đối với Numpy array là cộng
      > vector element wise còn dv
      > Python list thì là concat

      <br>

  <a id="node-376"></a>
  - It is the same as with the \\*product\\* operator, \\**\\*. In the first case, we \\*scale\\* the vector, while in the second case, we \\*concatenate three times\\* the same list.  Be aware of the difference because, \\*within the same function\\*, \\*both\\* types of arrays can \\*appear\\*. \\*Numpy\\* arrays are designed for \\*numerical\\* and \\*matrix\\* operations, while lists are for more general purposes.
    <br>

    <a id="node-377"></a>
    - print(narray * 3) print(alist * 3)  [ 3  6  9 12] [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
      > [!NOTE]
      > Đối với Numpy array là nhân
      > vector element wise còn dv
      > Python list thì là concat 3 lần vãi thật

      <br>

<a id="node-378"></a>
- Matrix or Array of Arrays
  <br>

  <a id="node-379"></a>
  - In \\*linear algebra\\*, a \\*matrix\\* is a structure composed of \\*n rows\\* \\*by m columns\\*. That means each row must have the same number of columns. With NumPy, we have two ways to create a matrix:  `-` Creating an array of arrays using \\*np.array\\* (recommended).  `-` Creating a matrix using \\*np.matrix\\* (still available but might be removed soon). NumPy arrays or lists can be used to \\*initialize\\* a matrix, but the resulting matrix will be composed of NumPy arrays only.
    <br>

    <a id="node-380"></a>
    - npmatrix1 `=` \\*np.array\\*([narray, narray, narray]) # Matrix \\*initialized with NumPy arrays \\*npmatrix2 `=` \\*np.array\\*([alist, alist, alist]) # Matrix \\*initialized with lists\\* npmatrix3 `=` \\*np.array\\*([narray, [1, 1, 1, 1], narray]) # Matrix \\*initialized with both types \\* print(npmatrix1) print(npmatrix2) print(npmatrix3)
      <br>

        <a id="node-381"></a>
        <p align="center"><kbd><img src="assets/881d05e949d51f9ec62ae86115714043e5b872b5.png" width="100%"></kbd></p>
        <br>

      <a id="node-382"></a>
      - However, when \\*defining a matrix\\*, be sure that \\*all the rows contain the same number of elements\\*. Otherwise, the linear algebra operations could lead to unexpected results.  Analyze the following two examples:
        <br>

        <a id="node-383"></a>
        - # Example 1:  okmatrix `=` \\*np.array\\*([[1, 2], [3, 4]]) # Define a 2x2 matrix print(okmatrix) # Print okmatrix print(okmatrix * 2) # Print a scaled version of okmatrix
          <br>

            <a id="node-384"></a>
            <p align="center"><kbd><img src="assets/95cc446acb03840ba52ed2117411a19850d123c9.png" width="100%"></kbd></p>
            <br>

        <a id="node-385"></a>
        - # Example 2:  badmatrix `=` np.array([[1, 2], [3, 4], \\*[5, 6, 7]\\*]) # Define a matrix. Note the third row contains 3 elements print(badmatrix) # Print the malformed matrix print(badmatrix * 2) # It is supposed to scale the whole matrix  `->` [\\*list\\*([1, 2]) list([3, 4]) list([5, 6, 7])] [list([1, 2, 1, 2]) list([3, 4, 3, 4]) list([5, 6, 7, 5, 6, 7])]
          <br>

<a id="node-386"></a>
- Scaling and translating matrices
  <br>

  <a id="node-387"></a>
  - Now that you know how to build \\*correct NumPy arrays and matrices\\*, let us see how \\*easy\\* it is to \\*operate\\* with them in Python using the regular \\*algebraic operators\\* like `+` and `-.`  Operations can be performed \\*between arrays\\* and arrays or between \\*arrays\\* and \\*scalars\\*.
    <br>

    <a id="node-388"></a>
    - # Scale by 2 and translate 1 unit the matrix result `=` okmatrix\\* * 2\\* `+` 1 # For each element in the matrix, multiply by 2 and add 1 print(result)
      <br>

        <a id="node-389"></a>
        <p align="center"><kbd><img src="assets/903c5d946d1822f95a68d93163874e736954ab48.png" width="100%"></kbd></p>
        <br>

    <a id="node-390"></a>
    - # Add two compatible matrices result1 `=` okmatrix `\\*+\\*` okmatrix print(result1)  # Subtract two compatible matrices. This is called the difference vector result2 `=` okmatrix\\* `-\\*` okmatrix print(result2)
      <br>

        <a id="node-391"></a>
        <p align="center"><kbd><img src="assets/de98597ed7c72166014a9459a45b94ed2be85181.png" width="100%"></kbd></p>
        <br>

    <a id="node-392"></a>
    - result `=` okmatrix \\**\\* okmatrix # Multiply each element by itself print(result)
      <br>

        <a id="node-393"></a>
        <p align="center"><kbd><img src="assets/7d7f033c66d1950a3f6f8294fcaa812b02f62e3d.png" width="100%"></kbd></p>
        <br>

<a id="node-394"></a>
- Transpose a matrix
  <br>

  <a id="node-395"></a>
  - In linear algebra, the \\*transpose\\* of a matrix is an operator that \\*flips a matrix over its diagonal\\*, i.e., the transpose operator switches the row and column indices of the matrix producing another matrix. If the original matrix dimension is \\*n by m\\*, the resulting transposed matrix will be \\*m by n.\\*  \\*T\\* denotes the t\\*ranspose operation\\*s with NumPy matrices.
    <br>

    <a id="node-396"></a>
    - matrix3x2 `=` np.array([[1, 2], [3, 4], [5, 6]]) # Define a 3x2 matrix print('Original matrix 3 x 2') print(matrix3x2) print('Transposed matrix 2 x 3') print(matrix3x2.T)
      <br>

        <a id="node-397"></a>
        <p align="center"><kbd><img src="assets/2cd87dd740eb38f621cd8e42ee26a58449062a35.png" width="100%"></kbd></p>
        <br>

    <a id="node-398"></a>
    - nparray `=` np.array([1, 2, 3, 4]) # Define an array print('Original array') print(nparray) print('Transposed array') print(nparray.T)
      > [!NOTE]
      > However, note that the transpose
      > operation does not affect 1D arrays.

      <br>

        <a id="node-399"></a>
        <p align="center"><kbd><img src="assets/b076435ca8ed42b6f082fdeb131e48bbf6640c13.png" width="100%"></kbd></p>
        <br>

    <a id="node-400"></a>
    - nparray `=` np.array([[1, 2, 3, 4]]) # Define a 1 x 4 matrix. Note the 2 level of square brackets print('Original array') print(nparray) print('Transposed array') print(nparray.T)
      <br>

        <a id="node-401"></a>
        <p align="center"><kbd><img src="assets/f4b261687a6d0f5dff7c2c52dcf8b2a6fb305c76.png" width="100%"></kbd></p>
        <br>

<a id="node-402"></a>
- Get the norm of a nparray or matrix
  <br>

    <a id="node-403"></a>
    <p align="center"><kbd><img src="assets/449d3b85faab81db34debdec31e9c5cf9339026e.png" width="100%"></kbd></p>
    <br>

  <a id="node-404"></a>
  - nparray1 `=` np.array([1, 2, 3, 4]) # Define an array norm1 `=` \\*np.linalg.norm\\*(nparray1)  nparray2 `=` np.array([[1, 2], [3, 4]]) # Define a 2 x 2 matrix. Note the 2 level of square brackets norm2 `=` \\*np.linalg.norm\\*(nparray2)   print(norm1) print(norm2)  `->` 5.477225575051661 5.477225575051661
    <br>

    <a id="node-405"></a>
    - Note that without any other parameter, the norm function \\*treats the matrix as being just an array of numbers\\*. However, it is possible to get the norm \\*by rows\\* or by \\*columns\\*. The \\*axis\\* parameter controls the form of the operation:  \\* • `axis=0\\* means` get the norm of each column \\*  • `axis=1\\* means` get the norm of each row.
      <br>

      <a id="node-406"></a>
      - nparray2 `=` np.array([[1, 1], [2, 2], [3, 3]]) # Define a 3 x 2 matrix.   normByCols `=` np.linalg.norm(nparray2, `\\*axis=0\\*)` # Get the norm for each \\*column\\*. Returns 2 elements normByRows `=` np.linalg.norm(nparray2, `\\*axis=1\\*)` # get the norm for each \\*row\\*. Returns 3 elements  print(normByCols) print(normByRows)  `->` [3.74165739 3.74165739] [1.41421356 2.82842712 4.24264069] 
        <br>

<a id="node-407"></a>
- The dot product between arrays: All the flavors
  <br>

    <a id="node-408"></a>
    <p align="center"><kbd><img src="assets/a533946ff6478a299c6745941bd4ffa1aa13b05d.png" width="100%"></kbd></p>
    <br>

  <a id="node-409"></a>
  - nparray1 `=` np.array([0, 1, 2, 3]) # Define an array nparray2 `=` np.array([4, 5, 6, 7]) # Define an array  flavor1 `=` \\*np.dot\\*(nparray1, nparray2) # Recommended way print(flavor1)  flavor2 `=` \\*np.sum\\*(nparray1 * nparray2) # Ok way print(flavor2)  flavor3 `=` nparray1 \\*@\\* nparray2         # Geeks way print(flavor3)  # As you never should do:             # Noobs way flavor4 `=` 0 \\*for\\* a, b in\\* zip(nparray1, nparray2):\\*     flavor4 `+=` a * b      print(flavor4)
    <br>

      <a id="node-410"></a>
      <p align="center"><kbd><img src="assets/c8a2668cca8ccb6d262ac97ddeb3a8380695d4aa.png" width="100%"></kbd></p>
      <br>

    <a id="node-411"></a>
    - \\*We strongly recommend using np.dot, since it is the \\_only method that accepts arrays and lists without problems\\*\\_
      <br>

      <a id="node-412"></a>
      - norm1 `=` \\*np.dot\\*(np.array([1, 2]), np.array([3, 4])) # Dot product on nparrays norm2 `=` \\*np.dot\\*([1, 2], [3, 4]) # Dot product on python lists  print(norm1, `'=',` norm2 )
        <br>

          <a id="node-413"></a>
          <p align="center"><kbd><img src="assets/b9a961c11fc828a65722669ed9db43deebd6749c.png" width="100%"></kbd></p>
          <br>

          <a id="node-414"></a>
          <p align="center"><kbd><img src="assets/9a675b969affddf2abeea9cdce514f88adca5a2f.png" width="100%"></kbd></p>
          <br>

<a id="node-415"></a>
- Sums by rows or columns
  <br>

  <a id="node-416"></a>
  - Another general operation performed on matrices is the \\*sum by rows or columns\\*. Just as we did for the function norm, the \\*axis\\* parameter controls the form of the operation:  \\* • `axis=0\\* means` to sum the elements of each column together. \\*  • `axis=1\\* means` to sum the elements of each row together.
    <br>

    <a id="node-417"></a>
    - nparray2 `=` np.array([[1, `-1],` [2, `-2],` [3, `-3]])` # Define a 3 x 2 matrix.   sumByCols `=` \\*np.sum\\*(nparray2, `axis=0)` # Get the sum for each column. Returns 2 elements sumByRows `=` \\*np.sum\\*(nparray2, `axis=1)` # get the sum for each row. Returns 3 elements  print('Sum by columns: ') print(sumByCols) print('Sum by rows:') print(sumByRows)
      <br>

        <a id="node-418"></a>
        <p align="center"><kbd><img src="assets/4801948cf0b1fa7dbbf320ef9103629d4e314fe4.png" width="100%"></kbd></p>
        <br>

<a id="node-419"></a>
- Get the mean by rows or columns
  <br>

    <a id="node-420"></a>
    <p align="center"><kbd><img src="assets/2e245ad6f0a6b19eb590e881d6c989fd9c54af9a.png" width="100%"></kbd></p>
    <br>

  <a id="node-421"></a>
  - nparray2 `=` np.array([[1, `-1],` [2, `-2],` [3, `-3]])` # Define a 3 x 2 matrix. Chosen to be a matrix with 0 mean  mean `=` \\*np.mean\\*(nparray2) # Get the mean for the whole matrix meanByCols `=` \\*np.mean\\*(nparray2, `axis=\\*0\\*)` # Get the mean for each column. Returns 2 elements meanByRows `=` \\*np.mean\\*(nparray2, `axis=\\*1\\*)` # get the mean for each row. Returns 3 elements  print('Matrix mean: ') print(mean) print('Mean by columns: ') print(meanByCols) print('Mean by rows:') print(meanByRows)
    <br>

      <a id="node-422"></a>
      <p align="center"><kbd><img src="assets/3d375dc168d56a1c86ad2b54d25cf0f759c99bbc.png" width="100%"></kbd></p>
      <br>

<a id="node-423"></a>
- Center the columns of a matrix
  <br>

  <a id="node-424"></a>
  - \\*Centering the attributes\\* of a data matrix is another \\*essential preprocessing step\\*. Centering a matrix means to \\*remove the column mean to each element inside the column\\*. The mean by columns of a centered matrix is always 0.  With NumPy, this process is as simple as this:
    <br>

    <a id="node-425"></a>
    - nparray2 `=` np.array([[1, 1], [2, 2], [3, 3]]) # Define a 3 x 2 matrix.   nparrayCentered `=` nparray2 `-` \\*np.mean\\*(nparray2, `axis=\\*0\\*)` # \\*Remove the mean for each column \\* print('Original matrix') print(nparray2) print('Centered by columns matrix') print(nparrayCentered)  print('New mean by column') `print(nparrayCentered.mean(axis=0))`
      <br>

        <a id="node-426"></a>
        <p align="center"><kbd><img src="assets/04365c9aa7bb344da45ab82228b73bdb97d0165e.png" width="100%"></kbd></p>
        <br>

  <a id="node-427"></a>
  - \\*Warning\\*: This process \\*does not apply for row centering\\*. In such cases, consider \\*transposing\\* the matrix, \\*centering by columns\\*, and then \\*transpose back the result\\*.  See the example below:
    <br>

    <a id="node-428"></a>
    - nparray2 `=` np.array([[1, 3], [2, 4], [3, 5]]) # Define a 3 x 2 matrix.   nparrayCentered `=` nparray2\\*.T\\* `-` \\*np.mean\\*(nparray2, `axis=\\*1\\*)` # \\*Remove the mean for each row \\*nparrayCentered `=` nparrayCentered\\*.T\\* # \\*Transpose back \\*the result  print('Original matrix') print(nparray2) print('Centered by rows matrix') print(nparrayCentered)  print('New mean by rows') `print(nparrayCentered.mean(axis=1))`
      <br>

        <a id="node-429"></a>
        <p align="center"><kbd><img src="assets/38adac108324c9838603f21f0ae771a82fcd8df2.png" width="100%"></kbd></p>
        <br>

  <a id="node-430"></a>
  - Note that some operations can be performed using static functions like \\*np.sum\\*() or \\*np.mean\\*(), or by using the \\*inner functions of the array\\*
    <br>

    <a id="node-431"></a>
    - nparray2 `=` np.array([[1, 3], [2, 4], [3, 5]]) # Define a 3 x 2 matrix.   mean1 `=` \\*np.mean\\*(nparray2) # Static way mean2 `=` nparray2\\*.mean()\\*   # Dinamic way  print(mean1, ' `==` ', mean2)
      > [!NOTE]
      > Even if they are equivalent, we **recommend
      > the use of the static way** always.

      <br>

        <a id="node-432"></a>
        <p align="center"><kbd><img src="assets/e9254c9df75be7c3ced135517465048a30aa09ea.png" width="100%"></kbd></p>
        <br>


<a id="node-433"></a>
## Euclidean Distance

<br>


<a id="node-434"></a>
### 1 \\*Euclidean\\* \\*distance\\* is a \\*similarity metric\\* used to determine \\*how far two

> [!NOTE]
> 1 \**Euclidean\** \**distance\** is a \**similarity metric\** used to determine \**how far two
> points or vectors are from each other.\**
>
> 2 Euclidean distance can be used to calculate the \**distance between two
> document vectors\**, as well as v\**ector spaces in higher dimensions\**.
>
> 3 The formula for Euclidean distance involves finding the horizontal and
> vertical distance squared and adding them together.
>
> 4 The \**Pythagorean theorem\** is used to calculate the Euclidean distance
> between two points.
>
> 5 In \**higher dimensions\**, the Euclidean distance formula is \**the norm of the
> difference between the vectors\** being compared.
>
> 6 The implementation of Euclidean distance in Python can be done using
> the \**linag\** module from NumPy.
>
> 7 The primary takeaway of Euclidean distance is that it can be used to
> determine the \**similarity between two documents or words.\**
>
> 8 The next video will discuss \**cosine\** \**similarity\**, another popular similarity
> function.

<br>

  <a id="node-435"></a>
  <p align="center"><kbd><img src="assets/1297ba58b6f7b81e15bfaee9eef5f5ea0b7c1b06.png" width="100%"></kbd></p>
  > [!NOTE]
  > Chiều dài đoạn thẳng nối 2 vector.
  > Dễ dàng tính bằng Pythago

  <br>

  <a id="node-436"></a>
  <p align="center"><kbd><img src="assets/31a878f820b7e12a4db2c2075089ffe1f97ee560.png" width="100%"></kbd></p>
  > [!NOTE]
  > Và nó cũng chính là norm của 'hiệu 2 vector'
  >
  > the norm of the difference between the vectors
  >
  > Norm của vector là **sqrt của tổng bình phương các element** của nó
  >
  > Norm ở đây nói chọn chứ đúng phải nói rõ ra là **L2 norm**, còn đv L1 norm thì
  > (không sqrt) tổng các  absolute value các element
  >
  > Công thức chung là Ln norm `=` (a1**n `+` a2**n `+` ...)** `(1/n)`

  <br>

  <a id="node-437"></a>
  <p align="center"><kbd><img src="assets/cd70c618616f13a0489629243cff37b122c4f8df.png" width="100%"></kbd></p>
  > [!NOTE]
  > Để tính (L2) norm trong Python
  > thì dùng **np.linalg.norm**

  <br>

  <a id="node-438"></a>
  <p align="center"><kbd><img src="assets/1c38514b9289b889388ee0186b1227f4b00f429b.png" width="100%"></kbd></p>
  <br>

  <a id="node-439"></a>
  <p align="center"><kbd><img src="assets/c175e4b7ad7dbe7469380f07c121ada5653a4d52.png" width="100%"></kbd></p>
  <br>


<a id="node-440"></a>
## Cosine Similarity: Intuition

<br>


<a id="node-441"></a>
### 1 Introduction to \\*cosine similarity\\* as a \\*similarity metric\\* for comparing \\*vector

> [!NOTE]
> 1 Introduction to \**cosine similarity\** as a \**similarity metric\** for comparing \**vector
> representations.\**
>
> 2 The \**problem of using Euclidean distance\** to compare vector
> representations of documents or corpora.
>
> 3 Example of how the Euclidean distance can be \**problematic\** in comparing
> \**different sized corpora.\**
>
> 4 The use of \**cosine\** \**similarity\** as a \**better proxy\** for \**similarity between vector\**
> representations than Euclidean distance.
>
> 5 Explanation of the main \**advantage\** of cosine similarity over Euclidean
> distance.
>
> 6 The intuition behind the use of cosine similarity as a metric to compare
> the \**similarity between two vector representations.\**
>
> 7 Advantages of cosine similarity when comparing documents of \**different
> sizes.\**
>
> 8 The opportunity to learn how to calculate cosine similarity.

<br>

  <a id="node-442"></a>
  <p align="center"><kbd><img src="assets/19e645080c629b3e947fe4e7bb055800b41d6e7f.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là **vấn đề với Euclidean** là nếu **chiều dài vector khác nhau nhiều**
  > (corpus nhỏ `-` bộ từ trong 1 lĩnh vực đại khái vậy) thì **khoảng cách vector
  > không phản ánh đúng độ giống giữa 2 vector** ví dụ Foot và Agriculture do
  > chênh lệch kích thước corpus mà thành ra xa nhau hơn là Agriculture với
  > History nếu đo bằng Euclidean (d1 > d2)
  >
  > Dùng hàm **cosine** **góc giữa 2 vector càng nhỏ** thì **chúng càng giống nhau**sẽ **nắm bắt tốt hơn sự giống nhau giữa các vector (alpha < beta)**

  <br>

  <a id="node-443"></a>
  <p align="center"><kbd><img src="assets/10bcc7d1573156d29752ab963d2f2f21d37998ab.png" width="100%"></kbd></p>
  <br>


<a id="node-444"></a>
## Cosine Similarity

<br>


<a id="node-445"></a>
### 1 The video teaches how to compute the \\*dot product\\* and \\*norm

> [!NOTE]
> 1 The video teaches how to compute the \**dot product\** and \**norm
> of vectors\** to calculate the cosine similarity score.
>
> 2 The \**cosine similarity\** score measures the \**similarity of the
> directions of two vectors.\**
>
> 3 The \**cosine similarity\** takes values \**between 0 and 1\** for the
> vector spaces seen so far.
>
> 4 The \**closer the cosine similarity score is to 1\**, the \**more similar
> the vectors' directions are\**.
>
> 5 A \**cosine similarity score of 1\** indicates \**identical vectors,\** while
> a score of \**0 indicates orthogonal vectors.\**
>
> 6 \**Similar vectors\** have \**higher cosine similarity scores\**.

<br>

  <a id="node-446"></a>
  <p align="center"><kbd><img src="assets/06cdaf19cbc89296ffe11ab5afbee9ab69f8cf68.png" width="100%"></kbd></p>
  <br>

  <a id="node-447"></a>
  <p align="center"><kbd><img src="assets/4ba76391bb6be06fc860db475269d39c9715301b.png" width="100%"></kbd></p>
  > [!NOTE]
  > Ôn lại ha khái niệm
  > **norm** và **dot product**

  <br>

  <a id="node-448"></a>
  <p align="center"><kbd><img src="assets/88c87ed2fa160b7d81c446940d957cd2aae1f6d6.png" width="100%"></kbd></p>
  > [!NOTE]
  > Công thức nó vầy rảnh
  > thì chứng minh lại

  <br>

  <a id="node-449"></a>
  <p align="center"><kbd><img src="assets/2aa318c47c933570c9616c6071301c13f4fe3b25.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là rất dễ hiểu tại sao lại dùng cosine làm thước đó đơn giản vì
  > cosine giữa chúng càng lớn, 2 vector càng cùng hướng `->` mà max
  > cosine là 1 thì 2 véctơ trùng hướng luôn còn ngược lại thì cosine càng
  > nhỏ thì 2 thằng càng khác hướng nhau mà min khi hai vector vuông góc
  > gọi là **maximum dissimilar**. Nên cosine là thước đo tốt cho độ **direction
  > similarity của 2 vectors, cosine càng lớn thì 2 thằng càng giống**

  <br>

  <a id="node-450"></a>
  <p align="center"><kbd><img src="assets/c54eb308171f27d890fd6fc4d4c9e2bd3b513f0a.png" width="100%"></kbd></p>
  <br>


<a id="node-451"></a>
## Manipulating Words In Vector Sapces

<br>


<a id="node-452"></a>
### 1 Introduction: The video teaches how to \\*manipulate vectors\\* to \\*predict the capital city of a

> [!NOTE]
> 1 Introduction: The video teaches how to \**manipulate vectors\** to \**predict the capital city of a
> country.\**
>
> 2 \**Manipulating vector \**representations: \**Vector algebra\** can be used to infer\**unknown
> relationships among words.\**
>
> 3 Finding \**relationship between vectors\**: Find the \**difference between the vectors \**of two related
> entities to determine \**how many units on each dimension to move to find other related entities.\**
>
> 4 Predicting capital of Russia: Adding the vector of Russia with the previously calculated vector
> will give the vector representation of its capital.
>
> 5 Finding the \**closest representation\**: \**Compare the vector representations of all possible cities\**
> with the vector representation obtained above \**using Euclidean distances\** or \**cosine similarities\**
> to d\**etermine the most similar city\**.
>
> 6 Importance of vector space: The process \**can only be done in a vector space\** that c\**aptures
> the relative meaning of words\**.
>
> 7 \**Clustering\** of vectors: The vectors of \**words that occur in similar places in a sentence \**will be
> encoded in a \**similar\** way.
>
> 8 \**Identifying patterns:\** Take advantage of the consistency encoding to identify patterns, such as
> finding the closest words to a given word by computing cosine similarity.
>
> 9 Plotting `d-dimensional` vectors on a 2D plane: Learn how to plot vectors on a 2D plane in the
> next video.

<br>

  <a id="node-453"></a>
  <p align="center"><kbd><img src="assets/fdbd47eeebcb1f7aee99e9ed1d39b3549c8512f1.png" width="100%"></kbd></p>
  <br>

  <a id="node-454"></a>
  <p align="center"><kbd><img src="assets/bc9dc33687b58f13f6e538ee268084a5efef558d.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là nếu ta biết  WD là thủ đô USA thì **chiều của vector WD `-` USA** cho ta biết
  > **mối quan hệ của vector (encoded cho) nước và (encoded vector của) thủ đô phải
  > như thế nào**
  >
  > Từ đó nếu có encoded vector của nước khác như **Russian** thì ta sẽ **predict** được
  > en**coded vector của thủ đô của nó** dựa theo quan hệ của **WD-USA**
  >
  > Và khi chọn ra cái gần nhất `-` giống nhất (dựa trên metric cosine similarity hoặc
  > Euclidean distance) với cái predict trong số các thủ đô thì ta sẽ thấy **Moscow** là gần
  > nhất.
  >
  > Và tính sai lệch giữa predicted capital of Russia và actual (Moscow) bằng Euclidean
  > distance hoặc Cosine similarity

  <br>

  <a id="node-455"></a>
  <p align="center"><kbd><img src="assets/4f03dbd2764747fcf0972ca78821c2347c560b33.png" width="100%"></kbd></p>
  <br>

  <a id="node-456"></a>
  <p align="center"><kbd><img src="assets/3fc8e153c0c7b1e218a064e954f3d66413cd96b8.png" width="100%"></kbd></p>
  > [!NOTE]
  > Turkey (3,1) `+` (5, `-1)` `=` Predicted Capital: (8, 0)
  >
  > Actual (Ankara): (9,1)
  >
  > `->` Euclidean distance `=` norm of (predicted `-` actual) 
  >  square root of { (8-9)**2 `+` (0-1)**2 } `=` sqrt(2) `=` 1.41

  <br>

  <a id="node-457"></a>
  <p align="center"><kbd><img src="assets/84b4d0584a1f7045df6708a97c00f24dcaa86724.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là với 1 không gian vector kiểu như các từ đều được
  > encoded thì các quan hệ giữa các từ gần nhau đã biết sẽ có thể
  > cho phép ta đưa ra những dự đoán

  <br>


<a id="node-458"></a>
## Manipulating Word Embeddings

<br>


<a id="node-459"></a>
### Manipulating word embeddings

<br>

<a id="node-460"></a>
- In this week's assignment, you are going to use a `\\*pre-trained` word embedding\\* for finding word analogies and equivalence. This exercise can be used as an \\*Intrinsic Evaluation\\* for the word embedding performance. In this notebook, you will apply linear algebra operations using NumPy to find analogies between words manually. This will help you to prepare for this week's assignment.
  > [!NOTE]
  > Đại khái nói sẽ dùng 1 `pre-trained` word embedding để xem thử và từ
  > đó hiểu được ý nghĩa của việc tạo các word embedding vector trong
  > việc khắc hoạ được ý nghĩ và mối quan hệ của nó với các từ khác

  <br>

  <a id="node-461"></a>
  - import pandas as pd # Library for Dataframes  import numpy as np # Library for math functions import pickle # Python object serialization library. Not secure  `\\*word_embeddings\\*` `=` pickle.load( open( `"./data/word_embeddings_subset.p",` "rb" ) ) `len(word_embeddings)` # there should be 243 words that will be used in this assignment
    <br>

<a id="node-462"></a>
- Now that the model is loaded, we can take a look at the word representations. First, note that `\\*word_embeddings\\*` is a Agriculture. Each word is the key to the entry, and the value is its corresponding vector presentation. Remember that \\*square brackets\\* allow access to any entry if the key exists.
  <br>

  <a id="node-463"></a>
  - countryVector `=` `word_embeddings\\*['country']\\*` # Get the \\*vector representation\\* for the word '\\*country\\*' print(type(countryVector)) # Print the type of the vector. Note it is a numpy array print(countryVector) # Print the values of the vector.
    <br>

<a id="node-464"></a>
- It is important to note that we store each vector as a NumPy array. It allows us to use the linear algebra operations on it.  The vectors have a size of \\*300\\*, while the vocabulary size of Google News is around \\*3 million word\\*s!
  <br>

  <a id="node-465"></a>
  - #Get the vector for a given word: def vec(w):     return `word_embeddings[w]`
    <br>


<a id="node-466"></a>
### Operating on word

> [!NOTE]
> Operating on word
> embeddings

<br>

<a id="node-467"></a>
- Remember that \\*understanding the data\\* is one of the \\*most critical steps \\*in Data Science.\\* Word embeddings\\* are the result of \\*machine learning processe\\*s and will be part of the input for further processes. These word embedding needs to be \\*validated\\* or at least \\*understood\\* because the performance of the derived model will strongly depend on its quality.  Word embeddings are \\*multidimensional arrays\\*, usually with \\*hundreds of attributes\\* that pose a challenge for its interpretation.  In this notebook, we will \\*visually inspect\\* the \\*word embedding\\* of some words using a \\*pair of attributes\\*. Raw attributes are not the best option for the creation of such charts but will allow us to illustrate the mechanical part in Python.  In the next cell, we make a beautiful \\*plot\\* for the \\*word embeddings of some words\\*. Even if plotting the dots gives an idea of the words, the arrow representations help to visualize the vector's alignment as well.
  > [!NOTE]
  > Đại khái là word embedding vector thường có hàng trăm
  > `unit/feature/attribute/(dimension)` là kết quả của một quá trình
  > ML training (để tìm ra `/` khắc hoạ ra nghĩa, quan hệ của nó đv
  > các từ khác trong không gian từ vựng) nhưng ở đây ta sẽ dùng
  > 2 attributes để plot

  <br>

  <a id="node-468"></a>
  - import matplotlib.pyplot as plt # Import matplotlib %matplotlib inline  words `=` ['oil', 'gas', 'happy', 'sad', 'city', 'town', 'village', 'country', 'continent', 'petroleum', 'joyful']  bag2d `=` np.array([vec(word) for word in words]) # \\*Convert each word to its vector representatio\\*n  fig, ax `=` plt.subplots(figsize `=` (10, 10)) # Create custom size image  \\*col1 `=` 3 \\*# \\*Select the column\\* for the x axis col2 `=` \\*2\\* # \\*Select the column\\* for the y axis  # Print an arrow for each word for word in bag2d:     ax.arrow(0, 0, word[col1], word[col2], `head_width=0.005,` `head_length=0.005,` `fc='r',` `ec='r',` width `=` `1e-5)`       ax\\*.scatter\\*(bag2d[:, col1], bag2d[:, col2]); # Plot a dot for each word  # Add the word label over each dot in the scatter plot for I in range(0, len(words)):     ax.annotate(words[I], (bag2d[I, col1], bag2d[I, col2]))   plt.show()
    > [!NOTE]
    > Đại khái là **chọn vài từ** rồi tạo (lấy ra từ `word_embedding` dictionary) **representation
    > vectors** xong **chọn 2 attribute `/` feature** trong hàng trăm (**300) features** của nó để plot

    <br>

      <a id="node-469"></a>
      <p align="center"><kbd><img src="assets/f72dd7126eee0d06f421f62e5e7acb12e1957f62.png" width="100%"></kbd></p>
      > [!NOTE]
      > Note that **similar words** like '**village**' and '**town**' or '**petroleum**', '**oil**', and 'gas'
      > tend to point in the same direction. Also, note that**'sad' and 'happy' looks
      > close to each other; however, the vectors point in opposite directions**.
      >
      > In this chart, one can figure out the **angles** and **distances** between the
      > words. Some words are close in both kinds of distance metrics.

      > [!NOTE]
      > Nhận xét thấy các từ mà ta hiểu nghĩa gần nhau (về
      > bối cảnh như sad, happy là đều về emotion, village &
      > town) thật sự xuất hiện gần nhau trên plot.
      >
      > Nhưng hướng của chúng lại thể hiện sự tương quan về ý nghĩa
      > của từ, sad với happy đi hai hướng có góc gần với 90 thể hiện
      > chúng đối nghĩa nhau

      <br>


<a id="node-470"></a>
### Word distance

<br>

<a id="node-471"></a>
- Now \\*plot\\* the words '\\*sad\\*', '\\*happy\\*', '\\*town\\*', and '\\*village\\*'. In this same chart, \\*display the vector from 'village' to 'town'\\* and the \\*vector from 'sad' to 'happy'\\*. Let us use NumPy for these linear algebra operations.
  <br>

  <a id="node-472"></a>
  - words `=` ['sad', 'happy', 'town', 'village']  bag2d `=` np.array([vec(word) for word in words]) # Convert each word to its vector representation  fig, ax `=` plt.subplots(figsize `=` (10, 10)) # Create custom size image  col1 `=` 3 # Select the column for the x axe col2 `=` 2 # Select the column for the y axe  # Print an arrow for each word for word in bag2d:     ax.arrow(0, 0, word[col1], word[col2], `head_width=0.0005,` `head_length=0.0005,` `fc='r',` `ec='r',` width `=` `1e-5)`      # print the vector difference between village and town village `=` vec('village') town `=` vec('town') diff `=` town `-` village ax.arrow(village[col1], village[col2], diff[col1], diff[col2], `fc='b',` `ec='b',` width `=` `1e-5)`  # print the vector difference between village and town sad `=` vec('sad') happy `=` vec('happy') diff `=` happy `-` sad ax.arrow(sad[col1], sad[col2], diff[col1], diff[col2], `fc='b',` `ec='b',` width `=` `1e-5)`   ax.scatter(bag2d[:, col1], bag2d[:, col2]); # Plot a dot for each word  # Add the word label over each dot in the scatter plot for I in range(0, len(words)):     ax.annotate(words[I], (bag2d[I, col1], bag2d[I, col2]))   plt.show() 
    <br>

      <a id="node-473"></a>
      <p align="center"><kbd><img src="assets/5f41742ab89869753bedd23d7642d3b2cd8165f6.png" width="100%"></kbd></p>
      > [!NOTE]
      > Sad và happy giống như vuông góc biểu thị
      > quan hệ hoàn toàn trái ngược, vilage với
      > town có vẻ cùng hướng hơn

      <br>


<a id="node-474"></a>
### Linear algebra on

> [!NOTE]
> Linear algebra on
> word embeddings

<br>

<a id="node-475"></a>
- print(\\*np.linalg.norm\\*(vec('town'))) # Print the norm of the word town print(\\*np.linalg.norm\\*(vec('sad'))) # Print the norm of the word sad  2.3858097 2.9004838
  > [!NOTE]
  > In the lectures, we saw the analogies between words using
  > **algebra** on word embeddings. Let us see how to do it in
  > Python with Numpy.
  >
  > To start, get the norm of a word in the word embedding.

  <br>


<a id="node-476"></a>
### Predicting capitals

<br>

<a id="node-477"></a>
- Now, applying v\\*ector difference\\* and \\*addition\\*, one can create a \\*vector representation for a new word\\*. For example, we can say that the \\*vector difference between 'France' and 'Paris\\*' represents the \\*concept of Capital.\\*  One can move from the city of Madrid in the direction of the concept of Capital, and obtain something close to the corresponding country to which Madrid is the Capital.
  > [!NOTE]
  > **Hiệu hai vector France và Paris** sẽ đại diện cho **khái
  > niệm thủ đô**. Thử tìm từ nào mà hợp với Madrid để
  > tạo vector cùng chiều với vector đại diện cho khái
  > niệm thủ đô này

  <br>

  <a id="node-478"></a>
  - Capital `=` vec('France') `-` vec('Paris') Country `=` vec('Madrid') `+` capital  print(country[0:5]) # Print the first 5 values of the vector  `->[-0.02905273` `-0.2475586`   0.53952026  0.20581055 `-0.14862823]` 
    > [!NOTE]
    > Tính ra vector của từ dự
    > đoán sẽ là Spain này

    <br>

    <a id="node-479"></a>
    - Diff `=` country `-` vec('Spain') print(diff[0:10])  `[-0.06054688` `-0.06494141`  0.37643433  0.08129883 `-0.13007355` `-0.00952148`  `-0.03417969` `-0.00708008`  0.09790039 `-0.01867676]` 
      > [!NOTE]
      > We can observe that the vector 'country' that
      > we expected to be the same as the vector
      > for Spain is n**ot exactly it**.

      > [!NOTE]
      > Thì thấy nó không trùng khớp với
      > Spain (different khác 0)

      <br>

      <a id="node-480"></a>
      - # Create a dataframe out of the dictionary embedding. This facilitate the algebraic operations keys `=` `word_embeddings.keys()` data `=` [] for key in keys:     `data.append(word_embeddings[key])`  embedding `=` `pd.\\*DataFrame\\*(data=data,` `index=keys)` # Define a function to find the closest word to a vector: def `find_closest_word(v,` k `=` 1):     # Calculate the vector difference from each word to the input vector     diff `=` embedding.values `-` v      # Get the squared L2 norm of each difference vector.     # It means the squared euclidean distance from each word to the input vector     delta `=` np.sum(diff * diff, `axis=1)`     # Find the index of the minimun distance in the array     I `=` np.argmin(delta)     # Return the row name for this item     return embedding.iloc[I].name 
        > [!NOTE]
        > So, we have to **look for the closest words** in the embedding that
        > matches the candidate country. If the word embedding works as
        > expected, the most similar word must be 'Spain'. Let us define a
        > function that helps us to do it. We will store our word embedding as a
        > DataFrame, which facilitate the lookup operations based on the
        > numerical vectors.

        > [!NOTE]
        > Nên thử tìm **từ gần nhấ**t với từ này
        > trong data xem sao, ổng cho sẵn 1
        > hàm **find_closest_word**

        <br>

          <a id="node-481"></a>
          <p align="center"><kbd><img src="assets/c6912fa1ab532e3e6eaf121163c2bb3dc5e291fc.png" width="100%"></kbd></p>
          > [!NOTE]
          > Thì tuy không ra chính xác Spain
          > nhưng từ Spain là**từ 'gần nhất'** với
          > vector từ prediction này

          <br>


<a id="node-482"></a>
### Predicting other Countries

<br>

  <a id="node-483"></a>
  <p align="center"><kbd><img src="assets/b7ee30ba0c74db1e4596405d1240da3106d7630e.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là thử với các quan hệ khác tìm từ mà quan hệ của nó với
  > Madrid gần với quan hệ giữa Italy và Rome nhất sẽ ra Spain

  <br>


<a id="node-484"></a>
### Represent a sentence as a vector

<br>

  <a id="node-485"></a>
  <p align="center"><kbd><img src="assets/41c128274a9ff2c393afb5a6ed4c77b25e03643f.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là represented vector của 1
  > **sentence** là **sum của các word vector**

  <br>

  <a id="node-486"></a>
  <p align="center"><kbd><img src="assets/ab1ba798e1abbf924006c984e15bc166f5dfa0c2.png" width="100%"></kbd></p>
  <br>


<a id="node-487"></a>
## Visualization And Pca

<br>


<a id="node-488"></a>
### 1 Introduction to the \\*problem\\* of `\\*high-dimensional` vectors\\* and the

> [!NOTE]
> 1 Introduction to the \**problem\** of \**high-dimensional vectors\** and the
> need for \**dimensionality reduction\** for \**visualization\**.
>
> 2 Explanation of \**principal component analysi\**s (\**PCA\**) and how it can
> be used to \**reduce the dimension \**of \**vector representations.\**
>
> 3 Motivation for visualizing vector representations of words and using PCA
> to \**identify relationships among words\**.
>
> 4 Process of performing PCA on data to \**obtain uncorrelated features\**
> and \**projecting data to a lower dimensional space.\**
>
> 5 Importance of \**retaining as much information as possible\** during the
> dimensionality reduction process.
>
> 6 Review of the main ideas discussed, including the use of PCA for
> \**visualizing data\** and \**transforming `high-dimensional` vectors\** into\**two
> dimensions\** for \**plotting\**.

<br>

  <a id="node-489"></a>
  <p align="center"><kbd><img src="assets/668a43c509674dbc3d96183e140e75890626d270.png" width="100%"></kbd></p>
  <br>

  <a id="node-490"></a>
  <p align="center"><kbd><img src="assets/afe5849b267e3f3e022e15f4d95e2eafa9b0fbf9.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là với high dimension vector thì làm sao visualize ra mà
  > xem khi mà nó có nhiều hơn 2 feature

  <br>

  <a id="node-491"></a>
  <p align="center"><kbd><img src="assets/9cf94343daffdccbb82b17878838ca0d4e6c4a94.png" width="100%"></kbd></p>
  > [!NOTE]
  > Giải pháp như đã quá biết là dùng Principal Component Analysis để
  > giảm từ nhiều dimension xuống còn 2 hay 3 features mà giữ tối đa thông
  > tin để từ đó có thể plot trên không gian 2d hay 3d

  <br>

  <a id="node-492"></a>
  <p align="center"><kbd><img src="assets/4ecde98c813478040712758ca5fb0b173f9a0eb0.png" width="100%"></kbd></p>
  <br>

  <a id="node-493"></a>
  <p align="center"><kbd><img src="assets/71eb3625d38aef1139e864b8a72bf03de1c08813.png" width="100%"></kbd></p>
  <br>

  <a id="node-494"></a>
  <p align="center"><kbd><img src="assets/bab50ebad5083c342d3d79c05431f269416c4e90.png" width="100%"></kbd></p>
  > [!NOTE]
  > Một điểm chú ý mà có thể những bài giảng về PCA trước có nói nhưng không
  > để ý là '**uncorrelated features**', nhưng ở đây cũng chưa nói rõ tại sao hoặc là cái gì

  <br>

  <a id="node-495"></a>
  <p align="center"><kbd><img src="assets/251a682cf012b187b1505170eef6b518ce0e85c4.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/251a682cf012b187b1505170eef6b518ce0e85c4.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/abbce8ceacf48e6f87ed2c279b46de0e27894099.png" width="100%"></kbd></p>
  > [!NOTE]
  > Một số training algorithm khi learn words họ dùng cách identifying
  > neighboring words nên encoding words vector với similar POS thường
  > sẽ plot ra gần nhau
  >
  > Câu hỏi gợi mở là tại sao sad và joyful mang nghĩa trái ngược cùng gần
  > nhau? `->` Tại vì không gian ngữ cảnh của nó gần nhau cũng tính chất emotion

  <br>


<a id="node-496"></a>
## Pca Algorithm

<br>


<a id="node-497"></a>
### 1 Introduction to \\*reducing the dimension of features \\*using \\*Eigenvalues\\* and

> [!NOTE]
> 1 Introduction to \**reducing the dimension of features \**using \**Eigenvalues\** and
> \**Eigenvectors\**
>
> 2 Process for dimensionality reduction using \**PCA\**, including obtaining
> \**uncorrelated features\**, \**normalizing data\**, and performing \**singular value
> decomposition\**
>
> 3 Obtaining \**Eigenvectors\** and \**Eigenvalues\** from the \**co-variance matrix\** of
> \**normalized data\** for PCA
>
> 4 \**Projecting data onto a new vector space\** using Eigenvectors and Eigenvalue
>
> 5 Importance of organizing \**Eigenvectors\** and \**Eigenvalues\** in \**descending order\**
> to r\**etain information\**
>
> 6 Implementation of \**PCA\** in a \**programming library\** and its use in visualizing
> word representations
>
> 7 Future topic of learning about \**vector spaces\** and building a simple \**machine
> translation\** system

<br>

  <a id="node-498"></a>
  <p align="center"><kbd><img src="assets/335cfec762070862cdd5b750fa5201b2732a06d0.png" width="100%"></kbd></p>
  <br>

  <a id="node-499"></a>
  <p align="center"><kbd><img src="assets/0f4c19bd63f2c2499f45e831c2efa4b18ffc010c.png" width="100%"></kbd></p>
  > [!NOTE]
  > **Eigenvector**: the resulting vectors, also known as the **uncorrelated** **features** of
  > your data
  >
  > **Eigenvalue**: the **amount of information retained by each new feature**. You can
  > think of it as the **variance** in the eigenvector.
  >
  > Also each **eigenvalue** has a **corresponding eigenvector**. The eigenvalue tells you
  > **how much variance there is in the eigenvector.** Here are the steps required to
  > compute PCA:

  <br>

  <a id="node-500"></a>
  <p align="center"><kbd><img src="assets/308c02765774f5c0a1aba25c2929949d9d5726e4.png" width="100%"></kbd></p>
  > [!NOTE]
  > Cái này có thể mới hoặc đã học mà ko để ý là **eigenvector** là các
  > **unrelated features** còn **eigenvalue** là phần thông tin **retained** by each
  > feature

  <br>

  <a id="node-501"></a>
  <p align="center"><kbd><img src="assets/a3d7f68bd2d385e135137f9749267994f484b549.png" width="100%"></kbd></p>
  > [!NOTE]
  > Cách tính như vầy, nhưng ổng nói khỏi lo
  > có lib tính giùm hiểu là được

  <br>

  <a id="node-502"></a>
  <p align="center"><kbd><img src="assets/fd78e75eff7a5add2389344d5516316edd1a53d4.png" width="100%"></kbd></p>
  > [!NOTE]
  > Thực hiện việc project tức là tính ra bộ data mới X' (ít feature hơn X) bằng cách
  > dot product X với **matrix U lấy 2 cột đầu** **thôi** `=` 2 uncorrelated vector chứa
  > nhiều thông tin nhất  (vì đang reduce về 2D mà, nếu về 3D thì lấy 3)
  >
  > Thì tính thử percentage of **retained variance** bằng tỉ lệ của 2 thằng đầu tiên
  > trong đường chéo của matrix S (Sum `S00+S11)` và tổng các value trên đường
  > chéo (Sum `S00+S11+..Sdd)`
  >
  > Ôn lại lại, matrix **U** là **eigenvector**, sẽ có **D cột** biểu thị cho  D feature
  > (những đã chuyển thành D **uncorrelated feature**)  hay D dimension ban đầu,
  > bây giờ muốn g**iảm xuống D' < D dimension thì lấy D' cột đầu thôi** và tương
  > ứng với nó sẽ bị mất thông tin
  >
  > Again do đã học qua PCA ở ML Spec nên biết mấy cái này cũng  không khó.

  <br>

  <a id="node-503"></a>
  <p align="center"><kbd><img src="assets/93a6d41db65f68f1e2bf0ae5b7bc32005c369994.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là Eigenvector sẽ đại diện cho các
  > **uncorrelated feature**, kiểu như SVD nó sẽ phân tích
  > bộ data ban đầu với D feature (correlated) để tách
  > thành D cái uncorrelated feature

  <br>


<a id="node-504"></a>
## Another Explanation About Pca

> [!NOTE]
> Một số cái không hiểu, quay lại sau

<br>


<a id="node-505"></a>
### Another explanation about PCA

<br>

<a id="node-506"></a>
- In this lab, we are going to view another explanation about Principal Component Analysis(PCA). PCA is a \\*statistical technique\\* invented in 1901 by Karl Pearson that uses orthogonal transformations to \\*map a set of variables\\* into a set of \\*linearly uncorrelated variables\\* called \\*Principal Components.\\*  PCA is based on the \\*Singular Value Decomposition (SVD) \\*of the \\*Covariance Matrix\\* of the original dataset. The \\*Eigenvectors\\* of such decomposition are used as a \\*rotation matrix\\*. The \\*Eigenvectors are arranged in the rotation matrix in decreasing order according to its explained variance\\*. This last term is related to the \\*EigenValues\\* of the SVD.  PCA is a potent technique with applications ranging from \\*simple space transformation\\*, \\*dimensionality reduction\\*, and mixture separation from spectral information.  Follow this lab to view \\*another explanation for PCA\\*. In this case, we are going to use the concept of \\*rotation matrices\\* applied to \\*correlated random data\\*, just as illustrated in the next picture.
  > [!NOTE]
  > `\/"The` **Eigenvectors are arranged in the rotation matrix in decreasing order
  > according to its explained variance**." `\/`
  >
  > `->À` như vậy **rotation matrix** chính là **matrix U** đó mà **mỗi cột là một
  > Eigenvector** sắp theo **thứ tự giảm dần của explained variance** cũng là cái có
  > liên quan đến **Eigenvalue**
  >
  > Hiểu thêm `/` mới rằng đại khái là từ **D feature** ban đầu của **X**, phép **SVD**
  > sẽ map data thành **D unrelated new features** mỗi features được **đại diện bằng
  > 1 Eigenvector** theo thứ tự từ cái có e**xplained variance lớn nhất tới nhỏ nhất**.
  > Để từ đó muốn giảm xuống (d**imensionality reduction**) còn **K < D** feature thì
  > tính bằng cách nhân **X với K Eigenvector đầu thôi**Và PCA có nhiều ứng dụng mà ở đây sẽ **giải thích một cách khác**về PCA

  <br>

    <a id="node-507"></a>
    <p align="center"><kbd><img src="assets/fe588613ef4456b7ba954a7f09fb8f90181babb7.png" width="100%"></kbd></p>
    <br>

  <a id="node-508"></a>
  - import numpy as np                         # Linear algebra library import matplotlib.pyplot as plt            # library for visualization from \\*sklearn.decomposition\\* import \\*PCA\\*      # PCA library import pandas as pd                        # Data frame library import math                                # Library for math functions import random                              # Library for pseudo random numbers
    <br>

    <a id="node-509"></a>
    - np.random.seed(1) n `=` 1  # The amount of the correlation x `=` np.random.uniform(1,2,1000) # Generate 1000 samples from a uniform random variable y `=` x.copy() * n # Make y `=` n * x  # PCA works better if the data is centered \\*x `=` x `-` np.mean(x)\\* # \\*Center x\\*. Remove its mean \\*y `=` y `-` np.mean(y)\\* # \\*Center y\\*. Remove its mean  data `=` \\*pd.DataFrame\\*({'x': x, 'y': y}) # \\*Create a data frame with x and y\\* plt.\\*scatter\\*(data.x, data.y) # Plot the original correlated data in blue  pca `=` `\\*PCA\\*(\\*n_components=2\\*)` # \\*Instantiate a PCA\\*. Choose to get 2 output variables  # Create the\\* transformation model for this data\\*. \\*Internally\\*, it gets the \\*rotation\\*  # \\*matrix\\* and the\\* explained variance\\* pcaTr `=` pca.\\*fit\\*(data)  rotatedData `=` pcaTr.\\*transform(data)\\* # \\*Transform the data\\* base on the \\*rotation matrix\\* of pcaTr   # # \\*Create a data frame\\* with the \\*new variables\\*. We call these new variables \\*PC1\\* and \\*PC2\\* dataPCA `=` pd.DataFrame(\\*data `=` rotatedData\\*, \\*columns `=` ['PC1', 'PC2']\\*)   # Plot the transformed data in orange plt.\\*scatter\\*(\\*dataPCA.PC1\\*, \\*dataPCA.PC2\\*) plt.show()
      > [!NOTE]
      > To start, let us consider a pair of random variables x, y.
      > Consider the base case when **y `=` n * x**. The x and y
      > variables will be **perfectly correlated to each other** since
      > **y is just a scaling of x**.

      > [!NOTE]
      > Tóm tắt lại cái này, rất đơn giản
      >
      > Ổng tạo bộ dataset với x random và, y `=` 1*x
      >
      > Đầu tiên PCA để work tốt hơn thì làm động tác centerlized data X,
      > Y bằng cách trừ x cho mean x tức với mỗi dataset x(i), trừ từng
      > feature x1 `-` mu1 (mean của feature 1), x2 `-` mu2 (mean feature 2).
      > Bước này như khi normalizing thì thêm chia cho variance nữa thôi.
      >
      > Kế là tạo PCA model bằng `Scikit-Learn` với **n_compoent** là 2
      >
      > Xong dùng function fit để được pcaTr (PCA transformation) và
      > transform để ..transform X.
      >
      > Và trong cái pcaTr này sẽ có **rotation matrix** và **explained
      > variance**lưu trong**pcaTr.components_ và pcaTr.explained_variance_**
      >
      > kết quả ra rotatedData sẽ có 2 feature mới dùng pandas.
      > DataFrame để tạo lại DataFrame đặt column (feature name) là
      > PCA1, PCA2

      <br>

        <a id="node-510"></a>
        <p align="center"><kbd><img src="assets/68a1170c7c66bdf557c20b69a95f8b872f0749c8.png" width="100%"></kbd></p>
        <br>


<a id="node-511"></a>
### Understanding the

> [!NOTE]
> Understanding the
> transformation model pcaTr

<br>

<a id="node-512"></a>
- As mentioned before, a \\*PCA model\\* is composed of a \\*rotation matrix \\*and its \\*corresponding explained variance\\*. In the next module, we will explain the details of the rotation matrices.  \\*pcaTr.components_\\* has the \\*rotation matrix\\*  `\\*pcaTr.explained_variance_\\*` has the \\*explained variance\\* of each \\*principal component\\*
  <br>

  <a id="node-513"></a>
  - print('Eigenvectors or principal component: First row must be in the direction of [1, n]') print(pcaTr.\\*components_\\*)  print() print('Eigenvalues or explained variance') `print(pcaTr.\\*explained_variance_\\*)`
    <p align="center"><kbd><img src="assets/d2423f05e26ccf53092039ab9536730deecd2f8a.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/d2423f05e26ccf53092039ab9536730deecd2f8a.png" width="100%"></kbd></p>
    > [!NOTE]
    > Nó nói First row must be in direction
    > of [1, n] là sao không hiểu?

    <br>

      <a id="node-514"></a>
      <p align="center"><kbd><img src="assets/3bc5dd3785b9c599dcb939a3d7bd5e3181dc7bb1.png" width="100%"></kbd></p>
      > [!NOTE]
      > Hoàn toàn không hiểu

      <br>


<a id="node-515"></a>
### Correlated Normal

> [!NOTE]
> Correlated Normal
> Random Variables.

<br>

<a id="node-516"></a>
- Now, we will use a \\*controlled dataset\\* composed of \\*2 random variables\\* with \\*different variances\\* and with a \\*specific Covariance\\* among them. The only way I know to get such a dataset is, first, create two \\*independent Normal random variables\\* with the \\*desired variances\\* and then \\*combine\\* them using a \\*rotation matrix\\*. In this way, the new resulting variables will be a linear combination of the original random variables and thus be dependent and correlated.
  <br>

  <a id="node-517"></a>
  - import matplotlib.lines as mlines import matplotlib.transforms as mtransforms  np.random.seed(100)  std1 `=` 1     # The \\*desired standard deviation\\* of our first random variable std2 `=` 0.333 # The d\\*esired standard deviation\\* of our second random variable  x `=` np.\\*random.normal\\*(0, \\*std1\\*, 1000) # \\*Get 1000 samples from x ~ N(0, std1)\\* y `=` np.\\*random.normal\\*(0, std2, 1000)  # \\*Get 1000 samples from y ~ N(0, std2)\\* #y `=` y `+` np.random.normal(0,1,1000)*noiseLevel * np.sin(0.78)  # PCA works better if the data is centered x `=` x `-` \\*np.mean(x)\\* # \\*Center x\\*  y `=` y `-` \\*np.mean(y)\\* # \\*Center y \\* #Define a pair of dependent variables with a desired amount of covariance n `=` 1 # Magnitude of covariance.  angle `=` \\*np.arctan\\*(\\*1 `/` n)\\* # Convert the covariance to and angle print('angle: ',  angle * 180 `/` math.pi)  # Create a \\*rotation matrix\\* using the given angle \\*rotationMatrix\\* `=` np.array([[np.\\*cos(angle)\\*, np.\\*sin(angle)\\*],                  `[-np.\\*sin(angle)\\*,` np.\\*cos(angle)\\*]])   print('rotationMatrix') print(rotationMatrix)  xy `=` np.concatenate(([x] , [y]), `axis=0).T` # Create a matrix with columns x and y  # \\*Transform the data using the rotation matrix\\*. It correlates the two variables data `=` \\*np.dot(xy, rotationMatrix)\\* # Return a nD array  # Print the rotated data plt.scatter(data[:,0], data[:,1]) plt.show()
    > [!NOTE]
    > đại khái là nó đang muốn tạo
    > một bộ data randomly nhưng (distribution sao cho) với
    > standard deviation là 1 cho x và 0.333 cho y.

    <br>

      <a id="node-518"></a>
      <p align="center"><kbd><img src="assets/0786171cc802e2f5f4835cdc94885587c3dde146.png" width="100%"></kbd></p>
      🔗 **Related:** [THE ROTATION MATRIX](the_rotation_matrix.md#node-538)

      > [!NOTE]
      > Sau khi đọc Rotation Matrix có thể hiểu khúc này. Rất
      > đơn giản vì hệ số góc của y `=` x là 1 (y `=` 1*x) nên tan `=`
      > 1, từ đó tìm ra lại góc bằng bao nhiêu thôi dùng hàm
      > arctan `->` angle là 45 đó
      >
      > Rồi ổng tạo Rotation Matrix với góc beta 45 độ này theo công thức 
      > của case xoay ngược chiều kim đồng hồ

      <br>

      <a id="node-519"></a>
      <p align="center"><kbd><img src="assets/eea430ec792934b0226e0a703c8aa000f671ba68.png" width="100%"></kbd></p>
      > [!NOTE]
      > Sau khi đọc **Rotation Matrix** có thể hiểu tiếp là nhân
      > rotation matrix với vector để xoay vector qua 1 góc
      > beta ở đây là 45 (ở đây đúng hơn xoay 1000 cái
      > vector `-` xy là matrix (1000,2) được tạo thành bỏi câu
      > concate hai vector x và y đó)

      <br>

      <a id="node-520"></a>
      <p align="center"><kbd><img src="assets/46ba4e8d030df689571f1a76e95bc6d5bdf21174.png" width="100%"></kbd></p>
      <br>

    <a id="node-521"></a>
    - plt.scatter(data[:,0], data[:,1]) # Print the original data in blue  # Apply PCA. \\*In theory, the Eigenvector matrix must be the  \\*# \\*inverse of the original rotationMatrix\\*.  pca `=` `PCA(n_components=2)`  # Instantiate a PCA. Choose to get 2 output variables  # Create the transformation model for this data. Internally it gets the rotation  # matrix and the explained variance pcaTr `=` pca.\\*fit\\*(data)  # Create an array with the transformed data \\*dataPCA\\* `=` pcaTr.\\*transform\\*(data)  print('Eigenvectors or principal component: First row must be in the direction of [1, n]') print(pcaTr.components_)  print() print('Eigenvalues or explained variance') `print(pcaTr.explained_variance_)`  # Print the rotated data \\*plt.scatter(dataPCA[:,0], dataPCA[:,1])\\*  # Plot the\\* first component axe\\*. Use the \\*explained variance to scale the vector\\* plt.plot([0, rotationMatrix[0][0] * std1 * 3], [0, rotationMatrix[0][1] * std1 * 3], `'k-',` `color=\\*'red\\*')` # Plot the \\*second component axe\\*. Use the \\*explained variance to scale the vector\\* plt.plot([0, rotationMatrix[1][0] * std2 * 3], [0, rotationMatrix[1][1] * std2 * 3], `'k-',` `color='\\*green\\*')`  plt.show()
      > [!NOTE]
      > Let us print the original and the resulting transformed system using the
      > result of the PCA in the same plot alongside with the 2 Principal
      > Component vectors in red and blue

      > [!NOTE]
      > Hiểu 70%

      > [!NOTE]
      > Tới đây đã hiểu phần nào như sau
      >
      > Đaị khái là lúc đầu ổng nói cái gì muốn tạo 2 uncorrelated feature gì gì  đó thì
      > mình nên hiểu là ổng muốn tạo dataset distributed theo 2 trục vuông góc nhau
      > `-` vuông góc nhau thì chính là uncorrelated
      >
      > Rồi ổng nói gì không biết cách nào để làm vậy ngoài việc tạo riêng  2 cái rồi có
      > lẽ chính là bước ổng define x random, y random với mỗi  cái mỗi giá trị
      > standard deviation mong muốn
      >
      > Tới đây nếu plot bộ data ra trước khi 'xoay' có lẽ sẽ ra giống như màu  cam.
      >
      > Xong ổng define Rotation Matrix với góc 45 từ hệ số góc 1 trong y `=` x để xoay
      > cái dataset.
      >
      > Rồi ổng dùng PCA, apply và plot ra lại cũng như in cái Eigenvector ra cho thấy
      > kết quả là quay cái bộ data 1 góc cũng 45 độ về lại ban đầu và Eigenvector
      > (trong field **eigenvector_**của pcaTr bằng đúng giá trị của Rotation Matrix
      > làm từ góc 45.
      >
      > *Cái điểm muốn mình hiểu ở đây là
      > 1. PCA nó thực hiện phép xoay bộ data sao đó ...
      > 2. ...

      <br>

        <a id="node-522"></a>
        <p align="center"><kbd><img src="assets/2f2ed1ffca83015cc3c11452b65ab6218a26d3e0.png" width="100%"></kbd></p>
        > [!NOTE]
        > Vẽ cái data hồi nãy ra lại bằng các
        > chấm xanh cái này hiểu

        <br>

        <a id="node-523"></a>
        <p align="center"><kbd><img src="assets/c740ffaae07dad7c7bd22ba83fa45432b7a72f1a.png" width="100%"></kbd></p>
        > [!NOTE]
        > Ở đây cái câu này gợi ý Eigenvector phải là inverse của
        > Rotation Matrix, gợi ý rằng nếu apply PCA, thì nhân
        > matrix data X với Eigenvector sẽ xoay X 1 góc ngược
        > với của Rotation Matrix?

        <br>

        <a id="node-524"></a>
        <p align="center"><kbd><img src="assets/0a32467b4ada4fad2a4a1c526bb4eae0e33db62a.png" width="100%"></kbd></p>
        > [!NOTE]
        > Thì, hiện tượng ổng muốn nói là, Eigenvector đúng là
        > đóng vai trò như Rotation Matrix, nó xoay bộ data 1
        > góc bằng đúng cái góc 45 độ

        <br>

        <a id="node-525"></a>
        <p align="center"><kbd><img src="assets/b1bb600bd2f29d40ddc625cc6428f3a53e4aaa92.png" width="100%"></kbd></p>
        > [!NOTE]
        > Hiểu 70%

        > [!NOTE]
        > Nhắc lại việc đầu tiên tạo uncorrelated variables x, y `-` hiểu mơ hồ
        > rằng nó sẽ tạo các điểm phân bố ngẫu nhiên nhưng cái distribution
        > của nó ..kiểu như 2 trục vuông góc.
        >
        > Xong dùng Rotation Matrix với góc của hệ số y `=` 1*x để xoay
        >
        > Rồi nó apply PCA thì thấy PCA nó tìm ra lại đúng cái Rotation
        > Matrix này và xoay ngược trở lại vị trí cũ
        >
        > và Eigenvalue chính là bình phương 2 chỉ số standard deviation ban
        > đầu  Khi tạo x, y là 1 và 0.333 tức là Variance 1 và Variance 2
        > (Variance `=` standard deviation (sigma) **2 nhớ không)

        <br>


<a id="node-526"></a>
### PCA as a strategy for

> [!NOTE]
> PCA as a strategy for
> dimensionality reduction

<br>

<a id="node-527"></a>
- The principal components contained in the \\*rotation matrix\\*, are \\*decreasingly sorted\\* depending on its \\*explained Varianc\\*e. It usually means that \\*the first components retain most of the power\\* of the data to \\*explain the patterns\\* that generalize the data. Nevertheless, for some applications, we are interested in the patterns that explain much less Variance, for example, in novelty detection.  In the next figure, we can see the original data and its corresponding projection using dimenson axes as principal components. In other words, data comprised of a single variable.
  > [!NOTE]
  > Đoạn này hiểu nè đại khái là vì rotation matrix sắp xếp các Eigenvector
  > Theo giảm dần độ variance nên cái đầu sẽ là cái quan trọng nhất
  > Trong việc chứa đựng những thông tin pattern của data.
  >
  > Nhưng đ.v một số trường hợp ta cần check những cái less variance
  > hơn ví dụ như '**novelty detection**' `-` kiểu như anomaly detection,
  > Những thằng (data instance) ở ngoài rìa

  <br>

  <a id="node-528"></a>
  - nPoints `=` len(data)  # Plot the original data in blue plt.scatter(data[:,0], data[:,1])  #Plot the projection along the first component in orange plt.scatter(data[:,0], np.zeros(nPoints))  #Plot the projection along the second component in green plt.scatter(np.zeros(nPoints), data[:,1])  plt.show()
    <br>

      <a id="node-529"></a>
      <p align="center"><kbd><img src="assets/b35821ab2618bba9996d5067f4f7a2fc55fd14e3.png" width="100%"></kbd></p>
      > [!NOTE]
      > Hiểu, sau khi PCA thì cái feature 1 là màu cam,
      > feature 2 là màu xanh. Nếu mình giảm
      > dimension xuống chỉ có 1 trục thì nó chỉ còn cái
      > màu cam (nó chứa variance nhiều nhất)

      <br>


<a id="node-530"></a>
### PCA as a strategy to

> [!NOTE]
> PCA as a strategy to
> plot complex data

<br>

<a id="node-531"></a>
- The next chart shows a sample diagram \\*displaying a dataset of pictures of cats and dogs\\*. Raw pictures are composed of \\*hundreds or even thousands of feature\\*s. However, PCA allows us to \\*reduce that many features to only two\\*. In that \\*reduced space of uncorrelated variables\\*, we can easily separate cats and dogs.
  > [!NOTE]
  > Hiểu, đại khái là trong không gian vector mỗi từ dc
  > represented bởi hàng trăm hoặc hàng ngàn feature (tương
  > ứng là số dimension của không gian) nhưng reduce xuống
  > bằng PCA còn 2 thì plot ra dc để thấy chó với mèo nó gom
  > gom lại thành 2 group

  <br>

    <a id="node-532"></a>
    <p align="center"><kbd><img src="assets/af755300ed6e5049f5d8580a27cca4c53e302c66.png" width="100%"></kbd></p>
    <br>


<a id="node-533"></a>
## The Rotation Matrix

<br>

<a id="node-534"></a>

<p align="center"><kbd><img src="assets/c0c11aac3d6500c07bf426b39cf16cba75043841.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái qua phép tính tính lượng giác có thể hiểu được khái
> niệm **Rotation matrix** là gì `-` Đại khái là cái **matrix** mà khi **nhân
> với vector** sẽ giúp **xoay vector đó 1 góc beta** (biến thành 1
> vector mới hợp với vector cũ 1 góc beta) Có điều chưa hiểu nó
> liên quan gì với PCA ở lab trước.

<br>

<a id="node-535"></a>

<p align="center"><kbd><img src="assets/8f33a97772d7c5b93b8153c7b6798c7008862ad8.png" width="100%"></kbd></p>

> [!NOTE]
> Hiểu, cạnh góc vuông bằng
> huyền * sin đối cos kề

<br>

<a id="node-536"></a>

<p align="center"><kbd><img src="assets/20e689ba75a9b022ac9a2d3664399cdb94514c59.png" width="100%"></kbd></p>

> [!NOTE]
> Này là công thức
> lượng giác thôi.

<br>

<a id="node-537"></a>

<p align="center"><kbd><img src="assets/460f1d3f3fdd3387ded7937455a2071f66dc9f82.png" width="100%"></kbd></p>

> [!NOTE]
> Thay thế và khai triển

<br>

<a id="node-538"></a>

<p align="center"><kbd><img src="assets/fd65016bc1f2bc00a4ff24c9050094456a8be18f.png" width="100%"></kbd></p>

🔗 **Related:** [import matplotlib.lines as mlines import matplotlib.transforms as mtransforms  np.random.seed(100)  std1 = 1     # The \\*desired standard deviation\\* of our first random variable std2 = 0.333 # The d\\*esired standard deviation\\* of our second random variable  x = np.\\*random.normal\\*(0, \\*std1\\*, 1000) # \\*Get 1000 samples from x ~ N(0, std1)\\* y = np.\\*random.normal\\*(0, std2, 1000)  # \\*Get 1000 samples from y ~ N(0, std2)\\* #y = y + np.random.normal(0,1,1000)*noiseLevel * np.sin(0.78)  # PCA works better if the data is centered x = x - \\*np.mean(x)\\* # \\*Center x\\*  y = y - \\*np.mean(y)\\* # \\*Center y \\* #Define a pair of dependent variables with a desired amount of covariance n = 1 # Magnitude of covariance.  angle = \\*np.arctan\\*(\\*1 / n)\\* # Convert the covariance to and angle print('angle: ',  angle * 180 / math.pi)  # Create a \\*rotation matrix\\* using the given angle \\*rotationMatrix\\* = np.array([[np.\\*cos(angle)\\*, np.\\*sin(angle)\\*],                  [-np.\\*sin(angle)\\*, np.\\*cos(angle)\\*]])   print('rotationMatrix') print(rotationMatrix)  xy = np.concatenate(([x] , [y]), axis=0).T # Create a matrix with columns x and y  # \\*Transform the data using the rotation matrix\\*. It correlates the two variables data = \\*np.dot(xy, rotationMatrix)\\* # Return a nD array  # Print the rotated data plt.scatter(data[:,0], data[:,1]) plt.show()](another_explanation_about_pca.md#node-518)

> [!NOTE]
> Đã hiểu rotation matrix

<br>

<a id="node-539"></a>

<p align="center"><kbd><img src="assets/ede8b88a308c73b7dbb95861cd8ea6ecc032cce3.png" width="100%"></kbd></p>

<br>

<a id="node-540"></a>

<p align="center"><kbd><img src="assets/8cf306d4335e85ff742779635aba2c192fe26fe6.png" width="100%"></kbd></p>

<br>

<a id="node-541"></a>

<p align="center"><kbd><img src="assets/3b1d5da892d92fa22ba3dff8f127b511dfe29994.png" width="100%"></kbd></p>

<br>

<a id="node-542"></a>

<p align="center"><kbd><img src="assets/0d7479aef82b2fff5d0378bbec3e20f63173917f.png" width="100%"></kbd></p>

<br>


<a id="node-543"></a>
## Week Conclusion

<br>


<a id="node-544"></a>
### 1 Introduction to \\*vector spaces\\* and \\*representing words as vectors\\*

> [!NOTE]
> 1 Introduction to \**vector spaces\** and \**representing words as vectors\**
>
> 2 \**Comparing words\** using \**cosine similarity\** and \**Euclidean distance\**
>
> 3 Programming assignment: \**manipulating word vectors\** to 
> \**find countries from capital cities\**
>
> 4 \**Dimensionality reduction\** of word vectors and \**clustering similar words\**
>
> 5 Preview of next week's topic: \**machine translation\**

<br>


<a id="node-545"></a>
## Quiz

<br>

<a id="node-546"></a>

<p align="center"><kbd><img src="assets/4feabb065e68c5f7689ace54ba9a7627ac8f1d30.png" width="100%"></kbd></p>

<br>

<a id="node-547"></a>

<p align="center"><kbd><img src="assets/b13d8d577b9088bd0fabac008cafee042c0ed8aa.png" width="100%"></kbd></p>

<br>

<a id="node-548"></a>

<p align="center"><kbd><img src="assets/a98a7130263c974906d3a6b420d56106cfcb907a.png" width="100%"></kbd></p>

<br>

<a id="node-549"></a>

<p align="center"><kbd><img src="assets/d1bd201b981af809f4d11923fc9dfd81409b5e02.png" width="100%"></kbd></p>

<br>

<a id="node-550"></a>

<p align="center"><kbd><img src="assets/5e0c49f8e5962d5e174f03b2af1490dcb5a60bc2.png" width="100%"></kbd></p>

<br>

<a id="node-551"></a>

<p align="center"><kbd><img src="assets/32ad354adca16feaaaeb1c3e48dcfffc21683685.png" width="100%"></kbd></p>

<br>

<a id="node-552"></a>

<p align="center"><kbd><img src="assets/8f11c851d745519396bc8e5784824c1a1634ea9f.png" width="100%"></kbd></p>

<br>

<a id="node-553"></a>

<p align="center"><kbd><img src="assets/c9beb11d726eb3b77448baa96d41dc1487c65c9e.png" width="100%"></kbd></p>

<br>

<a id="node-554"></a>

<p align="center"><kbd><img src="assets/26a4858c8e8a7a582deb4f573a01d35972894220.png" width="100%"></kbd></p>

<br>

<a id="node-555"></a>

<p align="center"><kbd><img src="assets/3e7e33cc341998612d6e5fdd5f8aed6ce76ef1ac.png" width="100%"></kbd></p>

<br>

<a id="node-556"></a>

<p align="center"><kbd><img src="assets/3aebd4372bc79e0260e1407acfc99d7d3db3fe8c.png" width="100%"></kbd></p>

<br>


<a id="node-557"></a>
## Programming Assignment: Vector Space Models

> [!NOTE]
> Có một chỗ chưa pass unit test dù vẫn pass assignment `4/5,` quay lại sau

<br>


<a id="node-558"></a>
### Welcome to this week's programming assignment of the specialization. In

> [!NOTE]
> Welcome to this week's programming assignment of the specialization. In
> this assignment we will explore word vectors. In natural language
> processing, we \**represent each word as a vector\** consisting of numbers.
> \**The vector encodes the meaning of the word\**. These numbers (or
> weights) for each word \**are learned using various machine learning
> models\**, which we will explore in more detail later in this specialization.
> Rather than make you code the machine learning models from scratch,
> we will s\**how you how to use the\**m. \**In the real world, you can always load
> the trained word vectors, and you will almost never have to train them
> from scratch\**. In this assignment you will
>
> • \**Predict analogies between words.\**
>
> • Use \**PCA\** to\**reduce the dimensionality \**of the \**word embeddings\** and plot
> them in two dimensions.
>
> • Compare \**word embeddings\** by using a \**similarity measure\** (the\**cosine
> similarity\**).
>
> • Understand \**how these vector space models work.\**

<br>

<a id="node-559"></a>
- 1 `-` Predict the Countries from Capitals
  <br>

  <a id="node-560"></a>
  - 1.1 Importing the Data
    <br>

    <a id="node-561"></a>
    - # Run this cell to import packages. import pickle import numpy as \\*np\\* import pandas as \\*pd\\* import matplotlib.pyplot as plt import w3_unittest  from utils import `\\*get_vectors\\*`
      > [!NOTE]
      > As usual, you start by importing some essential Python
      > libraries and the load dataset. The dataset will be loaded as
      > a Pandas **DataFrame**, which is very a common method in
      > data science. Because of the large size of the data, this may
      > take a few minutes.

      <br>

      <a id="node-562"></a>
      - data `=` `pd.read_csv('./data/capitals.txt',` `delimiter='` ') data.columns `=` ['city1', 'country1', 'city2', 'country2']  # print first five elements in the DataFrame data.head(5)
        <br>

          <a id="node-563"></a>
          <p align="center"><kbd><img src="assets/ae739613120ac204f51dac259ce9e8a7a5626c45.png" width="100%"></kbd></p>
          <br>

        <a id="node-564"></a>
        - \\*To Run This Code On Your Own Machine:  \\*Note that because the \\*original google news word embedding dataset\\* is about \\*3.64 gigabytes\\*, the workspace is not able to handle the full file set. So we've downloaded the full dataset, \\*extracted a sample of the words\\* that we're going to analyze in this assignment, and saved it in a \\*pickle file\\* called `\\*word_embeddings_capitals.p\\*` If you want to download the full dataset on your own and choose your own set of word embeddings, please see the instructions and some helper code.  • Download the dataset from this \\_page\\_.  • Search in the page for `'\\*GoogleNews-vectors-negative300.bin.gz\\*'` and click the link to download.  • You'll need to \\*unzip\\* the file.  `\\*Copy-paste\\*` the code below and run it on your local machine after downloading the dataset to the same directory as the notebook.
          <br>

          <a id="node-565"></a>
          - import nltk from gensim.models import KeyedVectors   embeddings `=` `KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin',` binary `=` True) f `=` open('capitals.txt', 'r').read() `set_words` `=` `set(nltk.word_tokenize(f))` `select_words` `=` words `=` ['king', 'queen', 'oil', 'gas', 'happy', 'sad', 'city', 'town', 'village', 'country', 'continent', 'petroleum', 'joyful'] for w in `select_words:`     `set_words.add(w)`  def `get_word_embeddings(embeddings):`      `word_embeddings` `=` {}     for word in embeddings.vocab:         if word in `set_words:`             `word_embeddings[word]` `=` embeddings[word]     return `word_embeddings`   # Testing your function `word_embeddings` `=` `get_word_embeddings(embeddings)` `print(len(word_embeddings))` pickle.dump( `word_embeddings,` open( `"word_embeddings_subset.p",` "wb" ) )
            <br>

            <a id="node-566"></a>
            - `word_embeddings` `=` `pickle.load(open("./data/word_embeddings_subset.p",` "rb")) `len(word_embeddings)`  # there should be 243 words that will be used in this assignment  `->` 243
              > [!NOTE]
              > Now we will load the word embeddings as a Python
              > dictionary. As stated, these have already been obtained
              > through a machine learning algorithm.

              <br>

              <a id="node-567"></a>
              - print("dimension: {}". `format(word_embeddings['Spain'].` shape[0]))  `->dimension:` 300
                > [!NOTE]
                > Each of the word embedding is a
                > `300-dimensional` vector.

                <br>

                <a id="node-568"></a>
                - \\*Predict relationships among words  \\*Now you will write a function that will \\*use the word embeddings\\* to \\*predict relationships\\* among words.   • The function will take as \\*input\\* \\*three words.\\*   • The \\*first two are related to each other.\\*   • It will \\*predict a 4th word\\* which is \\*related to the third word\\* in a \\*similar manner as the two first words\\* are related to each other.   • As an example, "Athens is to Greece as Bangkok is to \\*__\\*"?   • You will write a program that is capable of \\*finding the fourth word.\\*   • We will give you a hint to show you how to compute this.  A similar analogy would be the following: 
                  <br>

                    <a id="node-569"></a>
                    <p align="center"><kbd><img src="assets/6b5ce1fbe620cf8e7f73f7c606930fbc13f0bd3a.png" width="100%"></kbd></p>
                    > [!NOTE]
                    > You will implement a function that can tell you the capital of a
                    > country. You should use the same methodology shown in the
                    > figure above. To do this, you'll first compute the**cosine similarity
                    > metric** or the**Euclidean distance**.

                    <br>

  <a id="node-570"></a>
  - 1.2 Cosine Similarity
    <br>

      <a id="node-571"></a>
      <p align="center"><kbd><img src="assets/40798c1ba4b6534fcbec4bf7318ecf8964f7925c.png" width="100%"></kbd></p>
      <br>

  <a id="node-572"></a>
  - Exercise 1 `-` `cosine_similarity` `(UNQ_C1)`
    <br>

      <a id="node-573"></a>
      <p align="center"><kbd><img src="assets/0cbe72ab389f8f6d177185498637757ecbf0b269.png" width="100%"></kbd></p>
      <br>

      <a id="node-574"></a>
      <p align="center"><kbd><img src="assets/ba92193fe1c6c62f936c3de34a44e68c783ae4e1.png" width="100%"></kbd></p>
      <br>

  <a id="node-575"></a>
  - 1.3 Euclidean Distance
    <br>

      <a id="node-576"></a>
      <p align="center"><kbd><img src="assets/1cef02c3df2c192fcea8f7a94b1e1f6e6a67c08e.png" width="100%"></kbd></p>
      <br>

  <a id="node-577"></a>
  - Exercise 2 `-` euclidean `(UNQ_C2)`
    <br>

      <a id="node-578"></a>
      <p align="center"><kbd><img src="assets/c595a3d3c333476a727d8079739b8f9619fe7225.png" width="100%"></kbd></p>
      <br>

      <a id="node-579"></a>
      <p align="center"><kbd><img src="assets/2e82e9db969a6708b5030d5f1ec042706689535c.png" width="100%"></kbd></p>
      <br>

  <a id="node-580"></a>
  - 1.4 Finding the Country of each Capital
    <br>

    <a id="node-581"></a>
    - Now, you will use the previous functions to compute \\*similarities between vectors\\*, and use these to find the \\*capital cities of countries\\*. You will write a function that takes in three words, and the embeddings dictionary. Your task is to find the capital cities. For example, given the following words:  • 1: Athens 2: Greece 3: Baghdad,  your task is to predict the country 4: Iraq.
      <br>

  <a id="node-582"></a>
  - Exercise 3 `-` `get_country` `(UNQ_C3)`
    <br>

    <a id="node-583"></a>
    - \\*Instructions\\*:  1 To predict the capital you might want to look at `the \\/King` `-` Man `+` Woman `=` `Queen\\/ example` above, and implement that scheme into a mathematical function, using the word embeddings and a similarity function.  2 \\*Iterate over the embeddings dictionar\\*y and compute the \\*cosine similarity score\\* between \\*your vector\\* and the \\*current word embedding\\*.  3 You should a\\*dd a check\\* to make sure that the word you return is not any of the words that you fed into your function. \\*Return the one with the highest score.\\*
      <br>

        <a id="node-584"></a>
        <p align="center"><kbd><img src="assets/903c51ad5062416227d119fc9c05dea3dfeedd0a.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/903c51ad5062416227d119fc9c05dea3dfeedd0a.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/31384a0ba66cc4f672f3ae05b57642b4390eded9.png" width="100%"></kbd></p>
        > [!NOTE]
        > Đại khái là với cái input city 1, country 1, country 2 (là tên) ta chuyển
        > nó thành embedding vector nhờ cái embedding dictionary. Sau đó,
        > dựa vào quan hệ giữa vector khái niệm Nước `-` Thủ đô với country 2
        > ta predict embedding vector của city 2. Loop trong dataset, xem thử
        > cái nào là cái gần nhất (dùng Cosine similarity) với cái predict vector

        <br>

        <a id="node-585"></a>
        <p align="center"><kbd><img src="assets/017d775f2db1885f28da386a62a4fc4f701f6db6.png" width="100%"></kbd></p>
        <br>

  <a id="node-586"></a>
  - 1.5 Model Accuracy
    <br>

      <a id="node-587"></a>
      <p align="center"><kbd><img src="assets/bcb14ce8eaaee99990a8a8c64c83bc10881dee99.png" width="100%"></kbd></p>
      <br>

  <a id="node-588"></a>
  - Exercise 4 `-` `get_accuracy` `(UNQ_C4)`
    <br>

      <a id="node-589"></a>
      <p align="center"><kbd><img src="assets/ec3f59f179cc1f77bfb5eacb841cc8a1767399f7.png" width="100%"></kbd></p>
      > [!NOTE]
      > Không có gì khó, chỉ đơn giản là loop qua các row của dataset, lấy ra
      > cái country1, city1, country2 rồi predict cái thủ đô city2: Để rồi xem nó
      > có đúng bằng cái city2 trong dataset không. Đúng thì `+1.` Xong hết chia
      > tổng số correct cho tổng số hàng để ra. Accuracy percent

      <br>

      <a id="node-590"></a>
      <p align="center"><kbd><img src="assets/1b3390eb4c5f86fccd01b1c8217f4b40898b4841.png" width="100%"></kbd></p>
      <br>

<a id="node-591"></a>
- 2 `-` Plotting the vectors using PCA
  <br>

  <a id="node-592"></a>
  - Now you will \\*explore the distance\\* between \\*word vectors\\* after \\*reducing their dimension\\*. The technique we will employ is known as \\*principal component analysis (PCA)\\*. As we saw, we are working in a `\\*300-dimensional` space\\* in this case. Although from a computational perspective we were able to perform a good job, it is\\* impossible to visualize results\\* in such high dimensional spaces.  You can think of PCA as a method that \\*projects our vectors in a space of reduced dimension\\*, while \\*keeping the maximum information\\* about the original vectors in their reduced counterparts. In this case, \\*by maximum informatio\\*n we mean that the \\*Euclidean distance between the original vectors and their projected siblings is minima\\*l. Hence vectors that were originally close in the embeddings dictionary, will produce \\*lower dimensional vectors \\*that are \\*still close to each other\\*.  You will see that when you map out the words,\\* similar words\\* will be \\*clustered\\* next to each other. For example, the words 'sad', ' happy', 'joyful' all describe emotion and are supposed to be near each other when plotted. The words: ' oil', 'gas', and ' petroleum' all describe natural resources. Words like 'city', ' village', 'town' could be seen as synonyms and describe a similar thing.
    <br>

    <a id="node-593"></a>
    - Before plotting the words, you need to first be able to \\*reduce each word vector with PCA into 2 dimensions\\* and then plot it. The steps to compute PCA are as follows:  1 \\*Mean normalize\\* the data  2 \\*Compute the covariance matrix\\* of your data `(Σ).`  3 \\*Compute the eigenvectors\\* and the\\* eigenvalues of your covariance matrix\\*  4 Multiply the \\*first K eigenvectors\\* by \\*your normalized data\\*. The transformation should look something as follows:
      <br>

        <a id="node-594"></a>
        <p align="center"><kbd><img src="assets/4ceb08c7cc50d229dd7389839cc4d503c9398144.png" width="100%"></kbd></p>
        <br>

<a id="node-595"></a>
- Exercise 5 `-` `compute_pca` `(UNQ_C5)`
  <br>

  <a id="node-596"></a>
  - \\*Instructions\\*:  Implement a program that takes in a data set where each row corresponds to a word vector.  • The \\*word vectors are of dimension 300\\*.  • Use \\*PCA\\* to change the 300 dimensions `to \\*n_components\\* dimensions.`  • The new matrix should be of dimension \\*m, `n_componentns.\\*`  • First `\\*de-mean\\*` the data  • Get the \\*eigenvalues\\* using\\* linalg.eigh\\*. Use '\\*eigh\\*' rather than '\\*eig\\*' since R is symmetric. The performance gain when using \\*eigh\\* instead of \\*eig\\* is substantial.  • \\*Sort the eigenvectors and eigenvalues by decreasing order of the eigenvalues.  \\*• Get a subset of the \\*eigenvectors\\* (choose how \\*many principle components\\* you want to use using `\\*n_components\\*).`  • Return the new transformation of the data by \\*multiplying the eigenvectors\\* with the \\*original data.\\*
    <br>

    <a id="node-597"></a>
    - Use `\\*numpy.mean(a,axis=None)\\*` which takes one required parameter. You need to specify the optional argument axis for this exercise: If you set axis `=` 0, you take the mean for each column. If you set axis `=` 1, you take the mean for each row. Remember that each row is a word vector, and the number of columns are the number of dimensions in a word vector.  Use \\*numpy.cov(m, `rowvar=True)\\*` which takes one required parameter. You need to specify the optional argument rowvar for this exercise. This calculates the covariance matrix. By default \\*rowvar\\* is True. From the documentation: "If rowvar is True (default), then each row represents a variable, with observations in the columns." In our case, each row is a word vector observation, and each column is a feature (variable).  Use \\*numpy.linalg.eigh(a, `UPLO='L')\\*`  Use\\* numpy.argsort\\* sorts the values in an array from smallest to largest, then returns the indices from this sort.  In order to reverse the order of a list, you can use: `\\*x[::-1].\\*`  To apply the sorted indices to eigenvalues, you can use this format `\\*x[indices_sorted].\\*`  When applying the sorted indices to \\*eigen\\* vectors, note that each column represents an eigenvector. In order to preserve the rows but sort on the columns, you can use this format `\\*x[:,indices_sorted]` \\* To transform the data using a subset of the most relevant principle components, take the matrix multiplication of the eigenvectors with the original data.  The data is of shape `\\*(n_observations,` `n_features).\\*`  The subset of eigenvectors are in a matrix of shape `\\*(n_features,` `n_components)\\*.`  To multiply these together, take the transposes of both the eigenvectors `\\*(n_components,` `n_features)` \\*and the data `(n_features,` `n_observations).`  The product of these two has dimensions\\* `(n_components,n_observations)\\*.` Take its transpose to get the shape `\\*(n_observations,` `n_components).\\*`
      <br>

        <a id="node-598"></a>
        <p align="center"><kbd><img src="assets/d3aa58d89d82dfe764b9caed567f3f43f8a223b4.png" width="100%"></kbd></p>
        > [!NOTE]
        > Vẫn sai chỗ nào mà pass `2/4` unit
        > test. Quay lại kiểm tra sau

        > [!NOTE]
        > Có nhiều cái mới biết:
        >
        > `-` demean,
        >
        > `-` tính covariance matrix bằng np.cov(..,rowVar),
        >
        > `-` tính Eigenvectors và Eigenvalues bởi np.linalg.
        > `eigh(cov_matrix,` `UPLO='L'` ),
        >
        > `-` sort bằng np.argsort(),

        <br>

        <a id="node-599"></a>
        <p align="center"><kbd><img src="assets/62777833eb342a5f6da98f892162920935044c70.png" width="100%"></kbd></p>
        <br>

        <a id="node-600"></a>
        <p align="center"><kbd><img src="assets/4af637a1e45f55f037a963fa546e20de2a8194dd.png" width="100%"></kbd></p>
        > [!NOTE]
        > What do you notice?
        >
        > The word vectors for gas, oil and petroleum appear related to
        > each other, because their vectors are close to each other.
        > Similarly, sad, joyful and happy all express emotions, and are
        > also near each other.

        <br>

