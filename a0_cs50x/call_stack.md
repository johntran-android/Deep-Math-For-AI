# Call Stack

📊 **Progress:** `3` Notes | `11` Screenshots

---
<a id="node-753"></a>

<p align="center"><kbd><img src="assets/c1af31e3d4f09329608eb5df904e49ab622df245.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là khi một function được gọi, máy tính nó sẽ
> set một vùng memory dành cho function đó. Được gọi
> là **stack frame hay function frame**
>
> Và khi nhiều function được gọi (cái này gọi cái kia) thì
> mỗi function đều có stack frame.

<br>

<a id="node-754"></a>

<p align="center"><kbd><img src="assets/c5f39f51d7a769698a32bcddda65fc75d809f95b.png" width="100%"></kbd></p>

> [!NOTE]
> Và các frame này được xếp trong một stack. Cái frame
> nào được gọi mới nhất thì nằm trên cùng.
>
> Một khi có function khác được gọi thì nó được push lên
> top.
>
> Và một khi nó hoàn tất, nó sẽ popped off, đẩy thằng nằm
> dưới lên

<br>

<a id="node-755"></a>

<p align="center"><kbd><img src="assets/eec3e51d41328639e054059f3934c58b47da1cfa.png" width="100%"></kbd></p>

<br>

<a id="node-756"></a>

<p align="center"><kbd><img src="assets/3fcddf4826bb709b129f8fb64e44c02141807ffa.png" width="100%"></kbd></p>

<br>

<a id="node-757"></a>

<p align="center"><kbd><img src="assets/891e2460bbf3419af8b6860a4fc91a8dd3b9f388.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là minh hoạ một function tính factorization (giai thừa) là
> dạng recursive function.
>
> Main gọi printf, main pause, printf lên top
>
> Prinf gọi fact(5), printf pause, fact(5) lên top
>
> fact(5) gọi nhánh else, gọi fact(4). fact(5) pause fact(4) lên top
>
> fact(4) check ifelse -> else, gọi fact(3), fact(4) pause, fact(3) lên top
>
> ...
>
> fact(2) check, gọi fact(1), fact(2) pause, fact(1) lên top
>
> fact(1) chạy và return 1, finished, pop off, fact(2) lên top
>
> fact(2) chạy return 1*2, finished, pop off, fact(3) lên top
>
> ....

<br>

<a id="node-758"></a>

<p align="center"><kbd><img src="assets/f7441da988ef0a2466e9aac73bf672a156292a76.png" width="100%"></kbd></p>

<br>

<a id="node-759"></a>

<p align="center"><kbd><img src="assets/5fa28dcb768fe1758c1282f8832421c6c2b54897.png" width="100%"></kbd></p>

<br>

<a id="node-760"></a>

<p align="center"><kbd><img src="assets/772fa337710430297b206cb174c8410f8a8c65fd.png" width="100%"></kbd></p>

<br>

<a id="node-761"></a>

<p align="center"><kbd><img src="assets/c4d506f2e49aac17d75de1c2aa4a1c9865652ee1.png" width="100%"></kbd></p>

<br>

<a id="node-762"></a>

<p align="center"><kbd><img src="assets/458113ce9d2cfd9598db11499f29da0adfe5330b.png" width="100%"></kbd></p>

<br>

<a id="node-763"></a>

<p align="center"><kbd><img src="assets/c496aa8a25928bf6918ce7fe0596caaffc1f7211.png" width="100%"></kbd></p>

<br>

