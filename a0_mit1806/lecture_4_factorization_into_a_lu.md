# Lecture 4: Factorization Into A = Lu

📊 **Progress:** `26` Notes | `25` Screenshots

---
<a id="node-80"></a>

<p align="center"><kbd><img src="assets/44109592133793b348a9f91c590f6d68755191ab.png" width="100%"></kbd></p>

<br>

<a id="node-81"></a>

<p align="center"><kbd><img src="assets/4b538eaba4a3affe6bf8a9618e51d0ef7202a8d7.png" width="100%"></kbd></p>

> [!NOTE]
> Từ bài trước mình đã biết về **inverse của một single
> matrix A**, câu hỏi bây giờ là**inverse của một product
> AB**

<br>

<a id="node-82"></a>

<p align="center"><kbd><img src="assets/191d3a4c16abd956d3a79392395fcd7270c3ebd3.png" width="100%"></kbd></p>

> [!NOTE]
> Đáp án chính là **tích của Ainv và Binv, theo thứ tự
> ngược lại = Binv@Ainv**
>
> Chứng minh: rất dễ là hiểu là khi nhân AB và BinvAinv,
> theo bài trước đã biết ta hoàn toàn có thể di chuyển
> các dấu ngoặc để rồi ta sẽ tính BBinv trước ra bằng I.
> Sau đó AIAinv sẽ ra AAinv ra I

> [!NOTE]
> (AB)_inv = B_invA_inv

<br>

<a id="node-83"></a>

<p align="center"><kbd><img src="assets/12ed28ad090f4f0f4ed4a031159e4f94dffbf6ab.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy BinvAinv là
> inverse của AB

<br>

<a id="node-84"></a>

<p align="center"><kbd><img src="assets/ec71d4933f4d82a1a936ed5e1a80570dfc1b31c6.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi tiếp theo là inverse của A transpose là gì
>
> Gs bắt đầu với AAinv = I, transpose hai vế thì (I)T vẫn
> là I, còn (AAinv)T = AinvT AT

<br>

<a id="node-85"></a>

<p align="center"><kbd><img src="assets/d6ce52d3ee05cf74e60dd1cff6854da361bf7778.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy từ (Ainv)T (AT) = I cho thấy inverse của AT chính
> là (Ainv)T:
>
> (AT)_inv = (A_inv)T

> [!NOTE]
> (AT)_inv = (A_inv)T

<br>

<a id="node-86"></a>

<p align="center"><kbd><img src="assets/bff1a2a86127540af9eb5ea9762e206c591bcf7f.png" width="100%"></kbd></p>

<br>

<a id="node-87"></a>

<p align="center"><kbd><img src="assets/1589c68605351f773a3a15bbac9dd11232defbb7.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo, gs muốn tìm hiểu **liên hệ giữa A và U** (là matrix
> kết quả sau khi elimination), nên đặt ra ví dụ này. Câu hỏi là
> **elimination matrix E21 là gì?** (E21 như đã học, ý là matrix
> giúp nhân A để khử a21)
>
> Đã học ở bài trước: Dùng cách tiếp cận theo hàng, hàng 1
> của E21 sẽ là coeffs của linear combination giữa các hàng
> của A để ra hàng 1 của U, vậy dễ thấy: 
>
> hàng 1 của E21 sẽ là 1 **[1 0]**(để nhân với A thì giữ nguyên 
> hàng 1: **1*** A's row 1 + **0***A's row 2)**.** 
>
> hàng 2 của E21 sẽ là **[-4 1]**(để nhân với A thì sẽ "lấy hàng
> 2 trừ đi 4 lần hàng 1: **-4***A's row 1 + **1***A's row 2)
>
> Vậy E21 sẽ là **[1, 0; -4, 1]**

<br>

<a id="node-88"></a>

<p align="center"><kbd><img src="assets/adcdc08ec6849ffaf8408dc21cf84b09d4038a20.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi tiếp theo là **L là gì để nhân U ra lại A**: A = LU
>
> Theo như bài trước đã biết, **L sẽ đóng vai trò đảo ngược
> lại việc từ A biến thành U. Thế mà biến A thành U là do E:
> EA = U**. 
>
> **Nên bây giờ L đảo ngược chuyện đó nên L chính là E_inv**
>
> Ta có thể hiểu như vầy: EA = U và LU = A <=> L(EA) = A
> <=> (LE)A = A <=> LE = I từ đó suy ra **L = E_inv**
>
> Nhẩm tính theo row method để ra L là **[1 0; 4 1]**
>
> Gs cho biết **inverse của Elimination rất dễ, chỉ việc đổi
> dấu của cái coeff ở vị trí 21 lại** (để từ hàng 2 của E21 là
> [-4 1] thành [4 1] là ta sẽ có hàng 2 của E21_inv, hàng 1
> thì giữ nguyên)
>
> Có thể hiểu lí do là vì E21 sẽ khử a21 bằng cách "lấy hàng
> 2 (của A) trừ cho 4 * hàng 1 (của A) để thành hàng 2 của U". 
>
> Vậy thì để đảo ngược lại hành động này, dĩ nhiên là ta sẽ 
> "lấy hàng 2 (của U) cộng lại cho 4 * hàng 1 (của A, và cũng
> là của U vì hàng 1 giữ nguyên) thì sẽ ra lại hàng 2 của A"
>
> Quả thật nó chính là kết quả trên: 
>
> **[1, 0; -4, 1]** --(đổi dấu ở vị trí 21)--> **[1 0; 4 1]**

<br>

<a id="node-89"></a>

<p align="center"><kbd><img src="assets/d9ef7fed7000c6d4b1f91e05a4a67f14202aeadb.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 7: SOLVING AX = 0: PIVOT VARIABLES, SPECIAL SOLUTIONS](untitled.md#node-180)

> [!NOTE]
> **U** là gs viết tắt của **Upper Triangular**, tức là matrix mà
> **bên dưới đường chéo là 0 hết**, **L** là **Lower Triangular**(đường chéo là 1 hết, bên trên đường chéo là 0 hết)

<br>

<a id="node-90"></a>

<p align="center"><kbd><img src="assets/3324bf007d62cf68201373d845a166c579b2b409.png" width="100%"></kbd></p>

> [!NOTE]
> gs còn cho biết thêm**với L, đường chéo sẽ là 1**, **với U,
> đương nhiên đường chéo là các pivot**. 
>
> Và có thể**tách thêm ra** thành dạng như ở dưới trong đó
> **matrix giữa chỉ có đường chéo là các pivot.**
> Nhận xét, nhìn **có vẻ giống phép decomposition (eigen
> hoặc singular)**

<br>

<a id="node-91"></a>

<p align="center"><kbd><img src="assets/096082db8693a763b93849d2a422a7909a83ba7c.png" width="100%"></kbd></p>

> [!NOTE]
> Gs mới nói qua ví dụ dùng **matrix 3x3**. Vậy chưa cần
> biết cụ thể các matrix sẽ ntn nhưng ta biết quá trình để
> **elimination biến** A thành dạng pivot (U), ta sẽ dùng E21
> để loại coeff ở vị trí 21, sau đó là 31 và 32

<br>

<a id="node-92"></a>

<p align="center"><kbd><img src="assets/afe69ab70bc0f770e4f0bb5e5cfa7a040df25fe2.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì với matrix A 3x3 câu hỏi tương tự là matrix nào
> (khi nhân với U) sẽ **đảo ngược quá trình biến đổi từ A
> sang U**, để có lại A từ U. Hay L trong trường hợp này là gì

<br>

<a id="node-93"></a>

<p align="center"><kbd><img src="assets/cb06643467b52afdabd0743d6d11d029d917405e.png" width="100%"></kbd></p>

> [!NOTE]
> Lập luận thế này, E32 biến đổi E31E21A thành U, vậy E32inv
> sẽ biến đổi U về lại E31E21A:
>
> E32E31E21A = U 
>
> => E32inv(E32E31E21A) = (E32invE32)E31E21A = E31E21A
>
> Tiếp tục, E31inv sẽ biến đổi E31E21A về lại E21A:
>
> E31inv(E31E21A) = (E31invE31)E21A = E21A
>
> Và E21inv sẽ biến đổi E21A về lại A
>
> E21inv(E21A) = A
>
> Nên L = **E32invE31invE21inv** là matrix sẽ đảo ngược quá
> trình từ A thành U

<br>

<a id="node-94"></a>

<p align="center"><kbd><img src="assets/bc19d9245cf588f9834a3222726c3dae6cc16bb0.png" width="100%"></kbd></p>

> [!NOTE]
> Gs cho ví dụ giá trị cụ thể của các E, trong đó E31 cho
> bằng I cho gọn bớt. Thế thì ta có E = E32E21 là matrix
> khiến biến A thành U: EA=U
>
> Và L bằng E21invE32inv là matrix đảo ngược lại LU = A
>
> Để ý đã **biết cách tính E21inv** ở trên, cơ bản E21 chỉ là
> matrix mà **nếu với nhân A nó sẽ thực hiện việc lấy
> hàng 2 của A  trừ đi 2 * hàng 1 của A để thành**,
> hàng 2 của E21A
>
> (E21A) row 2 = A row 2 **- 2 * A row 1**  (1)
>
> thì E21inv sẽ đảo ngược bằng cách: **Lấy hàng 2 của E21A 
> cộng 2 * hàng 1 của E21A (cũng bằng hàng 1 của A vì E21
> không thay đổi hàng 1 so với A)** để có hàng 2 của A.
>
> (E21A) row 2 **+ 2 * (E21A) row 1** = A row 2 (2)
>
> Với (1) và (2) thì khi để ý [A row 1] và [E21A row 1] là giống
> nhau thì ta sẽ thấy rõ ràng (1) và (2) là nghịch đảo của nhau
>
> Tương tự với E32 và E32inv

<br>

<a id="node-95"></a>

<p align="center"><kbd><img src="assets/c3d48810d3abe71619ad00a8552f8f82cdae8487.png" width="100%"></kbd></p>

> [!NOTE]
> Kế tới gs đặt ra câu hỏi **how expensive**, ý là **tốn bao nhiêu operations
> tính toán** khi tăng n (matrix A kích thước [n,n]). Ví dụ n = 100.
>
> Cũng là bài toán chuyển matrix về từ A thành U như bữa giờ làm
>
> Gs **coi như một operation là một lần nhân và một lần trừ**: ví dụ [**trừ**
> hàng 2 cho [2 **nhân** hàng 1]] để khử số 0 ở đầu hàng 2

<br>

<a id="node-96"></a>

<p align="center"><kbd><img src="assets/5f4e0de3afde35c81ce3a3b819922df6f71555e4.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy bước đầu tiên là **chuyển cái cột đầu tiên thành số
> 0 hết trừ vị trí đầu tiên của hàng 1.**
>
> Câu hỏi là bước này cần bao nhiêu operations

<br>

<a id="node-97"></a>

<p align="center"><kbd><img src="assets/457796f11137e09483be53d94c395de27a560b46.png" width="100%"></kbd></p>

> [!NOTE]
> Gs đặt câu hỏi**liệu số operations có proportional với
> n theo n**2, hay n**3.**..

<br>

<a id="node-98"></a>

<p align="center"><kbd><img src="assets/f09ae1e7f33d5fcf0d29fe0b43d06eb817ee43c0.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy ở bước đầu tiên này gs **cho rằng ta sẽ tốn 100**2 operations**
>
> Chưa hiểu lắm tại sao, đại khái là gs cho rằng ta phải thay đổi 100x100
> con số (coi như thay đổi luôn hàng đầu tiên)
>
> Có thể hiểu là ở bước đầu tiên, ta sẽ muốn khử mọi phần tử không phải
> pivot của cột 1: a21, a31....Mà để khử a21 ta sẽ **trừ**row 2 cho (một
> con số nào đó **nhân** row 1). Như đã nói ta sẽ tính một phép nhân và
> một phép trừ là một operation.
>
> Thế thì việc lấy row 2 **trừ** [(something) **nhân** (row 1)] sẽ bao gồm
> 100 operation vì ta có 100 item mỗi hàng.
>
> Số operation cần thiết cũng tương tự khi khử a31, a41... và ta có
> khoảng 99 cái. Do đó số operation là **100*99** và **gs cho nó khoảng
> 100*100 luôn, là 100^2**

<br>

<a id="node-99"></a>

<p align="center"><kbd><img src="assets/3b6d0c6b654afc4d47ecf8b074503c22d46052e2.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là bước thứ hai, vấn đề cũng tương tự nhưng nhỏ
> hơn vì ta chỉ có 99 item mỗi hàng và có 98 hàng, nên số
> operation tính **gần đúng coi như có 99**2 operations**
>
> Thế thì cứ tiếp tục như vậy.
>
> Vậy ta cho rằng sẽ tốn
>
> **n**2 + (n-1)**2 +....2**2+1**2**
>
> operations

<br>

<a id="node-100"></a>

<p align="center"><kbd><img src="assets/7c96955ef4b1c1df0c818cf61f208af69388e5f2.png" width="100%"></kbd></p>

> [!NOTE]
> Gs lập luận là đây là **tổng** của **n term**, mà **bự nhất là n**2**,
> nên **nó ko thể to hơn n*n**2=n**3** được.
>
> Gs cho biết nó **sẽ cỡ n**3/3**
>
> Cái này là **tích phân từ 1 tới n của hàm x**2**.
>
> Cái này thật ra sẽ cần kiến thức của 18.01 nên mình có thể sẽ quay
> lại sau nhưng hiểu đại khái là vầy
>
> Để tính tổng 1^2 + 2^2 + ...(n-1)^2 + n^2 ta sẽ lấy tích phân từ 1 đến n
> của số hạng tổng quát. Và số hạng tổng quát là x^2. Do đó ta có:
>
> tích phân từ 0 đến n của x^2dx. và theo Fundamental  Theorem of
> Calculus Part 2, tích phân này sẽ bằng [nguyên hàm của f] n:0 = x^3/3
> | n:0 = n^3/3
>
> Vậy đây là số operations on A, tức là dành để tính cho A

> [!NOTE]
> Sẽ quay lại sau khi 18.01

<br>

<a id="node-101"></a>

<p align="center"><kbd><img src="assets/91ede3de6299ce7e6f6db5ecf16c0473e45f933a.png" width="100%"></kbd></p>

> [!NOTE]
> Còn với vector b (việc biến đổi còn có vector b bên phải
> equation Ax=b nữa nhớ ko). Sẽ **tốn n**2 operations**(gs
> không giải thích tại sao)

<br>

<a id="node-102"></a>

<p align="center"><kbd><img src="assets/47e4380aa7abaea3757b2502624d034007220d70.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, h gs nói qua việc nếu ta có tính tới row exchange,
> - nhớ lại là khi trong quá trình row elimination ta gặp
> pivot = 0 thì ta phải row exchange.
>
> Thì việc đó thực hiện bằng p**ermutation matrix**, ví dụ
> **p12 là chỉ permutation matrix giúp exchange row 1 và
> row 2.**
>
> Thế thì, gs đặt câu hỏi là**nếu ta có matrix 3x3, thì có
> mấy permutation matrix**. Là các matrix giúp exchange
> row ví dụ 1-2, 1-3, 2-3.
>
> P12 sẽ có hàng 1 là [0 1 0] vì khi nhân với A nó sẽ ra
> matrix P12A có hàng 1 là 0*a1+1*a2+0*a3=a2,
>
> và P12 có hàng 2 là [1 0 0] để P12A có hàng 2 sẽ là
> 1*a1+0*a2+0*a3=a1, tức là đã**switch hàng 1 và hàng 2
> của A rồi**
>
> (*a1,a2,a3 là ám chỉ row 1,2,3 của A)
>
> Ở trên cần nhớ lại khi **nhân row vector hàng cho
> matrix** là ta **linear combination các row của matrix**
> với c**oeff là các component của row vector**

<br>

<a id="node-103"></a>

<p align="center"><kbd><img src="assets/1872f6d0b8a1ba464aa6af3ee5b2f5322df29211.png" width="100%"></kbd></p>

> [!NOTE]
> Ngoài ra còn có các matrix này. Và đáng chú ý là **với 6
> matrix này**, **inverse hay transpose của chúng cũng
> thuộc 6 matrix này**. Ví dụ p12 (permutation matrix giúp
> exchange row 1 và 2) thì **cũng chính là nó khiến đảo
> ngược chuyện đó**, nên **P12 inv cũng chính là P12.
>
> P12 = P12_inv**

<br>

<a id="node-104"></a>

<p align="center"><kbd><img src="assets/d74fe8e7530981082543ee8f02454b3fd5997785.png" width="100%"></kbd></p>

> [!NOTE]
> Và gs cho biết **permutation matrix** có **tính chất đặc biệt** đó
> là **inverse cũng chính là transpose**: **Pinv = P.T**

<br>

