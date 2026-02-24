# Ps 1 Movies

📊 **Progress:** `12` Notes | `14` Screenshots

---
<a id="node-1393"></a>

<p align="center"><kbd><img src="assets/099b87bf85e70885e0263e597d9301c560e2690d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta sẽ gọi lệnh sql để lấy thông tin trả
> lời câu hỏi. Trong db này có 4 table

<br>

<a id="node-1394"></a>

<p align="center"><kbd><img src="assets/1d0eb34e6f5e642e3116576a45b0f4a45d5cf5ae.png" width="100%"></kbd></p>

<br>

<a id="node-1395"></a>

<p align="center"><kbd><img src="assets/22ada78987068ee0716ed6e329dfac10a61288d8.png" width="100%"></kbd></p>

> [!NOTE]
> Title các film release năm 2008

<br>

<a id="node-1396"></a>

<p align="center"><kbd><img src="assets/8835dd78983fd6920093e0f12b21e87583c27f84.png" width="100%"></kbd></p>

> [!NOTE]
> Năm sinh con nhỏ
> Emma Stone

<br>

<a id="node-1397"></a>

<p align="center"><kbd><img src="assets/f0fadca85c95fbe33d97c05f9328b7afb6616663.png" width="100%"></kbd></p>

> [!NOTE]
> tên movie có year `>=`
> 2018 sort bởi tên

<br>

<a id="node-1398"></a>

<p align="center"><kbd><img src="assets/98707ef940bc13a6906e7e4776c23b0e5cb1e796.png" width="100%"></kbd></p>

> [!NOTE]
> Đếm số film có
> rating `=` 10

<br>

<a id="node-1399"></a>

<p align="center"><kbd><img src="assets/6a0f442ba08b026b93ed0a4d7d2f219374fe26cd.png" width="100%"></kbd></p>

> [!NOTE]
> list tên `+` năm phát hành các phim Harry Potter
> (là phim có title start with "Harry Potter") sort theo year

<br>

<a id="node-1400"></a>

<p align="center"><kbd><img src="assets/7356632ea6ef199b955f417eaf7be198f9a3c4ba.png" width="100%"></kbd></p>

> [!NOTE]
> Tính average rating của các film
> phát hành năm 2012

<br>

<a id="node-1401"></a>

<p align="center"><kbd><img src="assets/b2fab5b2b4552972a320cd6402ba4a058313a1fd.png" width="100%"></kbd></p>

> [!NOTE]
> List tên diễn viên trong
> phim Toy Story

<br>

<a id="node-1402"></a>

<p align="center"><kbd><img src="assets/e32531db9c483d9e52904c683b58faf5d0d3131a.png" width="100%"></kbd></p>

> [!NOTE]
> list tên những diễn viên tham gia phim phát
> hành 2004, sort bởi năm sinh

<br>

<a id="node-1403"></a>

<p align="center"><kbd><img src="assets/1c2f23f989a5ab316d5098f42f1bcdf9340a77e3.png" width="100%"></kbd></p>

<br>

<a id="node-1404"></a>

<p align="center"><kbd><img src="assets/1425b153b21d7ee90f0219c1ba81ff124da11012.png" width="100%"></kbd></p>

> [!NOTE]
> list 5 phim rate cao nhất
> của cha này đóng

<br>

<a id="node-1405"></a>

<p align="center"><kbd><img src="assets/1f7b2e15a77cf2524b4ac644f64f1ae9784436f9.png" width="100%"></kbd></p>

> [!NOTE]
> 13 tên các người đóng chung với Kevin không tính ổng
>
> SELECT name FROM people WHERE name `!=` 'Kevin Bacon' AND id
> IN (SELECT `person_id` FROM stars WHERE `movie_id` IN (SELECT
> `movie_id` FROM stars WHERE `person_id` `=` (SELECT id FROM people
> WHERE birth `=` 1958 AND name `=` 'Kevin Bacon')));

<br>

<a id="node-1406"></a>

<p align="center"><kbd><img src="assets/bce5f6b18034098feac0c76a044928ee4b116ac2.png" width="100%"></kbd></p>

> [!NOTE]
> 12 Các phim mà hai người này đóng chung
>
> SELECT title FROM movies WHERE id IN (SELECT `movie_id` FROM
> stars WHERE `person_id` IN (SELECT id FROM people WHERE name `='`
> Bradley Cooper')) AND id IN (SELECT `movie_id` FROM stars WHERE
> `person_id` IN (SELECT id FROM people WHERE name `=` 'Jennifer
> Lawrence'));

<br>

