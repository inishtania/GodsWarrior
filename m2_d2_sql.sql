USE world ;
SHOW TABLES ;

#STRING PATTERN LIKE
-- Menampilkan baris tertentu sesuai dengan pola yang dipilih
-- Pada suatu kolom

SELECT * FROM country
WHERE name = 'Indonesia';

SELECT*FROM country
WHERE name like 'Indonesia' ;

#--------------------------------------------------------------------------
#Symbol % (percent) menunjukkan teks yang bisa diawali ataupun diikuti dengan karakter 
#apapun dan jumlahnya berapapun

-- Menampilkan nama kota yang diawali oleh huruf a
USE WORLD ;
SHOW TABLES ;

SELECT name FROM city
WHERE name like 'a%';   -- Tidak case sensitif

-- Menampilkan nama kota yang diawali huruf kapital --> Menggunakan keyword binary
SELECT name FROM city
WHERE name like BINARY 'a%' ;   -- menjadi case sensitif

-- Menampilkan nama kota yang diakhiri dengan huruf a 
SELECT name FROM city
WHERE name LIKE '%a' ; 

-- Menampilkan nama kota yang mengandung huruf a ;
SELECT name FROM city
WHERE name LIKE '%a%' ; 

-- SOAL : Menampilkan nama kota yang mengandung huruf a 
-- huruf a tidak boleh diawal tidak boleh diakhir 
SELECT name FROM city
WHERE name LIKE '%a%' 
AND name NOT LIKE  'a%' 
AND NAME NOT LIKE '%a' ;

-- Menampilkan nama kota yang hanya 1 kata (Tanpa ada spasi)
SELECT name FROM city
WHERE name NOT LIKE '% %' ;  

-- Menampilkan data yang mengandung persen itu sendiri 
SELECT name FROM city 
WHERE  name LIKE '%\%%' ; #NONE result menggunakan escape character yang '\'

-- Menampilkan nama kota yang mengandung kutip 
SELECT name FROM city
WHERE name LIKE '%\'%' ;  #NONE result

SELECT*FROM country ; 
-- Menampilkan data negara dimana populasinya harus diawali dengan angka 1
-- dan diawali dengan angka 9
SELECT * FROM country
WHERE population LIKE '1%9' ; 

SELECT * FROM city 
WHERE population LIKE '1%9' ;
#--------------------------------------------------------------------------
#Symbol _ (underscore) menunjukkan jumlah karakter, dimana setiap _ bernilai 1 karakter
-- Menampilkan nama kota yang hanya memiliki 5 karakter :
SELECT name FROM city 
WHERE name LIKE '_____' ;

-- Menampilkan nama kota yang memiliki 5 karakter dan harus berawalan A 
SELECT name FROM city 
WHERE name LIKE BINARY'A____' ; 

-- Menampilkan nama kota yang minimal 5 karakter dan diawali huruf A
SELECT name FROM city 
WHERE name LIKE BINARY 'A____%' ;

-- Menampilkan nama kota yang memiliki 5 karakter huruf ketiga adalah c 
SELECT name FROM city 
WHERE name LIKE '__c__';

#SOAL - Tampilkan 5 nama kota dengan 9 karakter 
-- dimana huruf t berada di posisi ke - 4 namun 
-- tidak memiliki spasi 
-- dan tidak boleh duplicate

SELECT DISTINCT name FROM city 
WHERE name LIKE '___t_____'
AND name NOT LIKE '% %'
LIMIT 5;

#--------------------------------------------------------------------------
#BETWEEN _____ AND 
#Berguna untuk membatasi rentang nilai tertentu. 
#Nilai awal dan nilai akhir ikut ditampilkan (included)
#SYNTAX  -> SELECT nama kolom FROM nama table WHERE ..... LIKE .....  BETWEEN nilai_awal AND nilai_akhir

-- Menampilkan nama kota dan populasi dimana populasinya dalam rentang nilai 500 ribu sampai 600 ribu 
-- Pakai cara manual 
SELECT name, population FROM city
WHERE population >= 5e5 
AND population <= 6e5;

-- Pakai operator BETWEEN
SELECT name, population FROM city 
WHERE population BETWEEN 5e5 AND 6e5;

-- Keuntungan menggunakan between daripada manual adalah lebih mudah, sederhan dan lebih cepat (duration)
-- Bisa digabungkan dengan karakter _ dan %
-- Kondisi diatas ditambah ketentuan dimana kota diawali dengan huruf j ;

SELECT name, population FROM city
WHERE name LIKE 'j%' 
AND population BETWEEN 5e5 and 6e5;

#--------------------------------------------------------------------------
#GROUP BY
# Berguna untuk mengelompokkan data berdasarkan nilai unik pada suatu kolom tertentu
#GROUP BY biasanya digunakan pada fungsi agregat (SUM,MAX,MIN,COUNT,AVG)

-- Total Populasi berdasarkan setiap benua
SELECT continent, sum(population) FROM country
WHERE population
group by continent
order by sum(population);

-- Menampilkan total populasi dan rata - rata GNP tiap region 
SELECT*FROM country;

use world;
select region, sum(population), avg(GNP) from country 
WHERE population   # untuk bagian where ini bisa diskip yah gaes
GROUP BY region 
order by avg(GNP);

select * from country 
where region ='Western Europe'
order by gnp desc;

select*from city
where countrycode ='NLD'
order by population desc;
#--------------------------------------------------------------------------
#GROUP BY
#Mengurutkan data berdasarkan kolom tertentu secara ascending maupun descending
#Ascending --> ASC 
#Descending --> DESC 

-- Menampilkan data yang diurutkan nama kotanya berdasarkan abjda pertama sampai terakhir 
select*from city 
order by name ASC ; 

-- Menampilkan data yang diurutkan nama kotanya berdasarkan abjd A-Z
select*from city 
order by binary name ASC ;  -- Binary disini berfungsi untuk menampilkan A-Z

-- Menampilkan nama kota dengan 5 populasi terbanyak
select name, population from city
order by population DESC 
limit 5 ;

-- Soal : Tampilkan data tiap benua beserta rata-rata GNP dan total populasi
-- diurutkan dari benua ascending
-- kemudian diurutkan dari rata - rata GNP terbesar 
SELECT*FROM country;
SELECT Continent, avg(GNP), sum(population)  
from country
group by Continent
order by avg(GNP) DESC , continent;   #yang ini masih berantakan , maka pakai solusi dibawah yah

SELECT Continent, avg(GNP), sum(population)  
from country
group by Continent
order by BINARY Continent, avg(gnp); #Ditambahkan binary untuk memastikan A-Z
# Kalau ada 2 order by maka kolom pertama didahulukan baru kolom selanjutnya 

#---------------------------------------------------------------------------------------
#SOAL : Tampilkan total populasi setiap continent 
-- kemudian diurutkan dari populasi terkecil
-- continent diubah menjadi benua dan populasi menjadi Total Populasi
-- Tampilkan yang nilai total populasi diatas 1 milyar saja 
select continent as 'Benua' , sum(population) as 'Total Populasi' from country 
where sum(population) > 1e9   #where tidak bisa berdampingan dengan fungsi , dan sum(population) merupakan fungsi agregat
group by continent
order by sum(population) ;

# Maka gunakan having dan posisinya di bawah group by 
# Kegunaan sama dengan WHERE yakni memfilter data berdasarkan kondisi tertentu , letaknya berada di sebelah group by
# Clause WHERE berlaku untuk baris individual yang memang dicek satu per satu 
# Clause having berlaku untuk grouping beberapa baris data
# Syntax : SELECT -> FROM -> GROUP BY -> HAVING -> ORDER BY -> LIMIT 
select continent as 'Benua' , sum(population) as 'Total Populasi' from country 
group by continent
having sum(population) > 1e9
order by sum(population) ;


-- Menampilkan 3 benua dengan total populasi terkecil 
-- dengan syarat total populasi harus diatas 10 juta
-- diawali dengan huruf 0
select continent as 'Benua' , sum(population) as 'Total Populasi' from country 
group by continent
having sum(population) > 1e7
order by sum(population) ;

-- Tampilkan data rata-rata GNP dari continent ASIA dan AFRICA
SELEct continent, avg(gnp) from country 
where continent like 'asia' or continent like 'africa' 
group by continent;

#IN 
select continent as 'Benua', avg(gnp) as Rata_rata_GNP from country
where continent in ('Asia','Africa') 
group by continent;

#---------------------------------------------------------------------------------------
#BUILT IN FUNCTION
#1. Aggregate Function 
-- Function yang berguna untuk menghitung sekumpulan baris dan outputnya akan menjadi 1 baris
-- SUM,COUNT,MIN,MAX,AVG

#SUM --> Menghitung total dari kolom tertentu
#COUNT --> Menghitung jumlah baris
select count(name) from country ; #239

#MIN --> Menghitung nilai minimum pada kolom tertentu
-- Tampilkan 1 benua  yang memiliki populasi terkecil dan di negara apakah itu
SELECT continent, name, min(population) from country 
group by continent , name 
order by BINARY min(population); #fungsi binary disini optional karena ketika order by ada 3 yang 0, Africa, Asia dan Antartica, kalau gak ada binary yang muncul malah antartica
-- limit 1 ; 

#MAX menghitung nilai tertinggi pada suatu kolom
#AVG menghitung nilai rata-rata dari kolom tertentu 
SELECT AVG(lifeexpectancy) from country ; 

#------------------------------------------------------------------------------------
#2. SCALAR FUNCTION
#Yang hanya menghitung 1 baris 
#ROUND(), UCASE() untuk Uppercase, LCASE() untuk Lowercase

#ROUND -> untuk membulatkan data numerik
SELECT round(SurfaceArea,0) FROm country ;

#Ucase --> Uppercase 
SELECT ucase(continent) from country;
select*,ucase(continent) from country ; #dimana ini akan ditampilkan semua table tetapi ucase itu jadi kolom sendiri
#LENGTH() --> menampilkan jumlah karakter pada suatu kolom

SELECT length(name) from country ;