# Week 7: Sql

📊 **Progress:** `28` Notes | `33` Screenshots

---

<a id="node-1630"></a>
## Lab

<br>

<a id="node-1631"></a>

<p align="center"><kbd><img src="assets/01ca8c2f02ce09990d9a96ea3216a84d68a43698.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta sẽ gọi lệnh sql để lấy thông tin trả
> lời câu hỏi. Trong db này có 2 table song và
> artist.

<br>

<a id="node-1632"></a>

<p align="center"><kbd><img src="assets/a4f60f0ca3c9d34020bd35cc11e78db0c5368780.png" width="100%"></kbd></p>

<br>

<a id="node-1633"></a>

<p align="center"><kbd><img src="assets/6ff1bc43353abf1c7edb945f1444beec66f5392b.png" width="100%"></kbd></p>

> [!NOTE]
> 1.sql sql query để lấy hết name của các songs:
>
> SELECT name FROM songs;

<br>

<a id="node-1634"></a>

<p align="center"><kbd><img src="assets/5af1972ada5ca3cdeb3962732e6b935b8798ed20.png" width="100%"></kbd></p>

<br>

<a id="node-1635"></a>

<p align="center"><kbd><img src="assets/035aabc2f7e71f03ed0127c35654d02feffe6c31.png" width="100%"></kbd></p>

> [!NOTE]
> 2.sql list name của songs sort by temp từ nhỏ đến lớn
>
> SELECT name FROM songs
> ORDER BY tempo;

<br>

<a id="node-1636"></a>

<p align="center"><kbd><img src="assets/8b4506cbbd699e1daf661a57ac3ddb74a78cdea1.png" width="100%"></kbd></p>

> [!NOTE]
> 3.sql list name của songs sort by duration từ lớn đến
> nhỏ lấy 5 cái
>
> SELECT name FROM songs ORDER BY duration_ms
> DESC LIMIT 5;

<br>

<a id="node-1637"></a>

<p align="center"><kbd><img src="assets/e2379d60bd32b084bb83e1804a9b50315804773e.png" width="100%"></kbd></p>

> [!NOTE]
> 4.sql list name của songs mà các danceability, valence, energy
> lớn hơn 0.75
>
> SELECT name FROM songs WHERE danceability > 0.75 
> AND energy > 0.75 AND valence > 0.75;

<br>

<a id="node-1638"></a>

<p align="center"><kbd><img src="assets/6e2cf56f58939048712acb37f1962c2388f1bdcf.png" width="100%"></kbd></p>

> [!NOTE]
> 5.sql tính average energy của các songs
>
> SELECT AVG(energy) FROM songs;

<br>

<a id="node-1639"></a>

<p align="center"><kbd><img src="assets/4d6ebec24d72d51bcff9a4e493b26039a288034f.png" width="100%"></kbd></p>

> [!NOTE]
> 6.select cái name bài hát của ông Post Malone
>
> SELECT name FROM songs WHERE artist_id =
> (SELECT id FROM artists WHERE name = 'P ost
> Malone');

<br>

<a id="node-1640"></a>

<p align="center"><kbd><img src="assets/47e73d07d992ff4d8e9dd85dd701597231c205ea.png" width="100%"></kbd></p>

> [!NOTE]
> Tính average energy
> các song bởi Drake

<br>

<a id="node-1641"></a>

<p align="center"><kbd><img src="assets/159416c675789ab5044b08052f90754ac0f7dba3.png" width="100%"></kbd></p>

> [!NOTE]
> In tên songs có chứa '
> feat.' trong name

<br>


<a id="node-1642"></a>
## Ps 1 Movies

<br>

<a id="node-1643"></a>

<p align="center"><kbd><img src="assets/099b87bf85e70885e0263e597d9301c560e2690d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta sẽ gọi lệnh sql để lấy thông tin trả
> lời câu hỏi. Trong db này có 4 table

<br>

<a id="node-1644"></a>

<p align="center"><kbd><img src="assets/1d0eb34e6f5e642e3116576a45b0f4a45d5cf5ae.png" width="100%"></kbd></p>

<br>

<a id="node-1645"></a>

<p align="center"><kbd><img src="assets/22ada78987068ee0716ed6e329dfac10a61288d8.png" width="100%"></kbd></p>

> [!NOTE]
> Title các film release năm 2008

<br>

<a id="node-1646"></a>

<p align="center"><kbd><img src="assets/8835dd78983fd6920093e0f12b21e87583c27f84.png" width="100%"></kbd></p>

> [!NOTE]
> Năm sinh con nhỏ
> Emma Stone

<br>

<a id="node-1647"></a>

<p align="center"><kbd><img src="assets/f0fadca85c95fbe33d97c05f9328b7afb6616663.png" width="100%"></kbd></p>

> [!NOTE]
> tên movie có year >=
> 2018 sort bởi tên

<br>

<a id="node-1648"></a>

<p align="center"><kbd><img src="assets/98707ef940bc13a6906e7e4776c23b0e5cb1e796.png" width="100%"></kbd></p>

> [!NOTE]
> Đếm số film có
> rating = 10

<br>

<a id="node-1649"></a>

<p align="center"><kbd><img src="assets/6a0f442ba08b026b93ed0a4d7d2f219374fe26cd.png" width="100%"></kbd></p>

> [!NOTE]
> list tên + năm phát hành các phim Harry Potter
> (là phim có title start with "Harry Potter") sort theo year

<br>

<a id="node-1650"></a>

<p align="center"><kbd><img src="assets/7356632ea6ef199b955f417eaf7be198f9a3c4ba.png" width="100%"></kbd></p>

> [!NOTE]
> Tính average rating của các film
> phát hành năm 2012

<br>

<a id="node-1651"></a>

<p align="center"><kbd><img src="assets/b2fab5b2b4552972a320cd6402ba4a058313a1fd.png" width="100%"></kbd></p>

> [!NOTE]
> List tên diễn viên trong
> phim Toy Story

<br>

<a id="node-1652"></a>

<p align="center"><kbd><img src="assets/e32531db9c483d9e52904c683b58faf5d0d3131a.png" width="100%"></kbd></p>

> [!NOTE]
> list tên những diễn viên tham gia phim phát
> hành 2004, sort bởi năm sinh

<br>

<a id="node-1653"></a>

<p align="center"><kbd><img src="assets/1c2f23f989a5ab316d5098f42f1bcdf9340a77e3.png" width="100%"></kbd></p>

<br>

<a id="node-1654"></a>

<p align="center"><kbd><img src="assets/1425b153b21d7ee90f0219c1ba81ff124da11012.png" width="100%"></kbd></p>

> [!NOTE]
> list 5 phim rate cao nhất
> của cha này đóng

<br>

<a id="node-1655"></a>

<p align="center"><kbd><img src="assets/1f7b2e15a77cf2524b4ac644f64f1ae9784436f9.png" width="100%"></kbd></p>

> [!NOTE]
> 13 tên các người đóng chung với Kevin không tính ổng
>
> SELECT name FROM people WHERE name != 'Kevin Bacon' AND id
> IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT
> movie_id FROM stars WHERE person_id = (SELECT id FROM people
> WHERE birth = 1958 AND name = 'Kevin Bacon')));

<br>

<a id="node-1656"></a>

<p align="center"><kbd><img src="assets/bce5f6b18034098feac0c76a044928ee4b116ac2.png" width="100%"></kbd></p>

> [!NOTE]
> 12 Các phim mà hai người này đóng chung
>
> SELECT title FROM movies WHERE id IN (SELECT movie_id FROM
> stars WHERE person_id IN (SELECT id FROM people WHERE name ='
> Bradley Cooper')) AND id IN (SELECT movie_id FROM stars WHERE
> person_id IN (SELECT id FROM people WHERE name = 'Jennifer
> Lawrence'));

<br>


<a id="node-1657"></a>
## Ps 2 50ville

<br>

<a id="node-1658"></a>

<p align="center"><kbd><img src="assets/05c44b3f3e761f9833033c982d3e3847894a1e71.png" width="100%"></kbd></p>

> [!NOTE]
> Nói chung là tìm ăn
> trộm dựa vào db

<br>

<a id="node-1659"></a>

<p align="center"><kbd><img src="assets/f492a5baa23d78ed981de78fa8cb1009dc61a832.png" width="100%"></kbd></p>

<br>


<a id="node-1660"></a>
### CREATE TABLE **crime_scene_reports** (

> [!NOTE]
> CREATE TABLE **crime_scene_reports** (
>     id INTEGER,
>     year INTEGER,
>     month INTEGER,
>     day INTEGER,
>     street TEXT,
>     description TEXT,
>     PRIMARY KEY(id)
> );
> CREATE TABLE **interviews** (
>     id INTEGER,
>     name TEXT,
>     year INTEGER,
>     month INTEGER,
>     day INTEGER,
>     transcript TEXT,
>     PRIMARY KEY(id)
> );
> CREATE TABLE **atm_transactions** (
>     id INTEGER,
>     account_number INTEGER,
>     year INTEGER,
>     month INTEGER,
>     day INTEGER,
>     atm_location TEXT,
>     transaction_type TEXT,
>     amount INTEGER,
>     PRIMARY KEY(id)
> );
> CREATE TABLE **bank_accounts** (
>     account_number INTEGER,
>     person_id INTEGER,
>     creation_year INTEGER,
>     FOREIGN KEY(person_id) REFERENCES people(id)
> );
> CREATE TABLE **airports** (
>     id INTEGER,
>     abbreviation TEXT,
>     full_name TEXT,
>     city TEXT,
>     PRIMARY KEY(id)
> );
>

<br>


<a id="node-1661"></a>
#### CREATE TABLE **flights** (     id INTEGER,     origin_airport_id INTEGER,     destination_airport_id INTEGER,     year INTEGER,     month INTEGER,     day INTEGER,     hour INTEGER,     minute INTEGER,     PRIMARY KEY(id),     FOREIGN KEY(origin_airport_id) REFERENCES airports(id),     FOREIGN KEY(destination_airport_id) REFERENCES airports(id) ); CREATE TABLE **passengers** (     flight_id INTEGER,     passport_number INTEGER,     seat TEXT,     FOREIGN KEY(flight_id) REFERENCES flights(id) ); CREATE TABLE **phone_calls** (     id INTEGER,     caller TEXT,     receiver TEXT,     year INTEGER,     month INTEGER,     day INTEGER,     duration INTEGER,     PRIMARY KEY(id) ); CREATE TABLE **people** (     id INTEGER,     name TEXT,     phone_number TEXT,     passport_number INTEGER,     license_plate TEXT,     PRIMARY KEY(id) ); CREATE TABLE **bakery_security_logs** (     id INTEGER,     year INTEGER,     month INTEGER,     day INTEGER,     hour INTEGER,     minute INTEGER,     activity TEXT,     license_plate TEXT,     PRIMARY KEY(id) );

<br>

<a id="node-1662"></a>

<p align="center"><kbd><img src="assets/a5df18efb059bdcfa894861264d3e1a75c4cefaa.png" width="100%"></kbd></p>

<br>

<a id="node-1663"></a>

<p align="center"><kbd><img src="assets/78e573d5c50202642169d0e48ca32833f6fa2b20.png" width="100%"></kbd></p>

<br>


<a id="node-1664"></a>
#### -- Tìm hồ sơ vụ án có liên quan đến ‘duck’ SELECT description FROM crime_scene_reports WHERE description LIKE '%duck%'; SELECT description FROM crime_scene_reports WHERE street = 'Humphrey Street' AND day = 28 AND month = 7 AND year = 2021; -> -- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.  -- Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |  -- Xem thử có activity liên quan đến tiệm bánh này không SELECT * FROM bakery_security_logs WHERE activity LIKE '%Humphrey%';  -- Xem thử activity có gì SELECT DISTINCT(activity)  FROM bakery_security_logs;  -- Xem thử các transcript của interview có nhắc đến bakery  SELECT transcript FROM interviews WHERE transcript LIKE '%bakery%';  -> -- Sometime within **ten minutes of the theft**, I saw the thief get into a car in the**bakery parking lot** and drive away.  -- If you have **security footage** from the bakery parking lot, you might want to **look for cars that left the parking lot in that time frame**.                                                          |  -- I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,  -- I was walking by the**ATM on Leggett Street** and saw the **thief there withdrawing some money**.                                                                                                 |  -- As the thief was leaving the bakery, they called someone who **talked to them for less than a minute**. In the call,  -- I heard the thief say that they were planning to take the **earliest** **flight out of Fiftyville tomorrow.** -- The thief then asked the person on the other end of the phone to**purchase the flight ticket.**  -- I saw Richard take a bite out of his pastry at the bakery before his pastry was stolen from him.

> [!NOTE]
> Dựa vào vài thông tin ban đầu, tìm hồ
> sơ lời khai của 3 nhân chứng

<br>

<a id="node-1665"></a>

<p align="center"><kbd><img src="assets/684f0bd513ad664c0de24b3f913d40f97ef7556f.png" width="100%"></kbd></p>

> [!NOTE]
> Tìm danh sách những người thỏa mãn 4 điều kiện này
>
> -- Những người rút tiền ở ATM Legget Street ngày 28/7/2021
>
> -- Những người có tên trong các chuyến bay rời 50ville ngày 
> 29/7/2021
>
> -- Những người có gọi điện dưới 1 phút ngày 28/7/2021 
>
> -- Thêm manh mối bakery log license_place, những người có 
> biển số xe trong danh sách camera ghi lại
>
> -- tại cửa hàng bánh trước 12h ngày 28/7/2021
>
> Và xem họ gọi cho ai

<br>

<a id="node-1666"></a>

<p align="center"><kbd><img src="assets/c1026971649375021e3aeddec445c3a34ccc1481.png" width="100%"></kbd></p>

> [!NOTE]
> Thu hẹp lại mấy khứa này.
> Thử submit cặp Bruce - Robbin (search thì thấy khứa Bruce
> đi New York) thì thấy đúng

<br>


<a id="node-1667"></a>
#### SELECT id, origin_airport_id, destination_airport_id, hour, minute, day, month, year  FROM flights  WHERE id IN  (SELECT flight_id FROM passengers WHERE day = 29 AND month = 7 AND year = 2021 AND origin_airport_id = 8 AND passport_number IN  (SELECT passport_number FROM people WHERE id IN  (SELECT id FROM people                      WHERE id IN (SELECT person_id                                  FROM bank_accounts                                  WHERE account_number IN (SELECT account_number                                                      FROM atm_transactions                                                      WHERE atm_location = 'Leggett Street'                                                      AND transaction_type = 'withdraw'                                                      AND day = 28                                                      AND month = 7                                                      AND year = 2021)                     )                     AND id IN (SELECT id                                  FROM people                                  WHERE passport_number IN (SELECT passport_number                                                              FROM passengers                                                              WHERE flight_id IN (SELECT id                                                                                  FROM flights                                                                                  WHERE origin_airport_id IN (SELECT id                                                                                                              FROM airports                                                                                                              WHERE full_name = 'Fiftyville Regional Airport')                                                                                 AND day = 29                                                                                  AND month = 7                                                                                  AND year = 2021)))                     AND id IN (SELECT id                                  FROM people                                  WHERE phone_number IN (SELECT caller                                                      FROM phone_calls                                                      WHERE day = 28                                                     AND month = 7                                                     AND year = 2021                                                     AND duration <= 60))                     AND id IN (SELECT id                                  FROM people                                  WHERE license_plate IN (SELECT license_plate                                                      FROM bakery_security_logs                                                      WHERE day = 28                                                      AND month = 7                                                      AND year = 2021                                                      AND hour < 11))     ))) ORDER BY hour LIMIT 1;

> [!NOTE]
> Dựa thêm manh mối là họ sẽ dự
> định bay chuyến sớm nhất thì ta
> sẽ lấy chuyến sớm

<br>

<a id="node-1668"></a>

<p align="center"><kbd><img src="assets/cef3f5245f08407e49a0cc9feda053507a204aa6.png" width="100%"></kbd></p>

> [!NOTE]
> Ra kết quả là chuyến này, trong 3 khứa
> trên khứa nào đi chuyến này (flight id = 36)

<br>


<a id="node-1669"></a>
#### SELECT name FROM people WHERE passport_numer IN (SELECT passport_number FROM p                   error here ---^ sqlite> SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);

<br>

<a id="node-1670"></a>

<p align="center"><kbd><img src="assets/23af4cd2ff0e03bfa62ba560e274b8761385b9be.png" width="100%"></kbd></p>

> [!NOTE]
> Cả Bruce và Taylor đều
> bay chuyến này

<br>

