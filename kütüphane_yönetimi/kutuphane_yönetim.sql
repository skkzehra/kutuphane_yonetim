-- MySQL dump 10.13  Distrib 9.3.0, for macos15.2 (arm64)
--
-- Host: localhost    Database: kutuphane_yönetim
-- ------------------------------------------------------
-- Server version	9.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `kitaplar`
--

DROP TABLE IF EXISTS `kitaplar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kitaplar` (
  `kitap_id` int NOT NULL AUTO_INCREMENT,
  `ad` varchar(100) NOT NULL,
  `yazar` varchar(100) NOT NULL,
  `durum` enum('müsait','ödünç') DEFAULT 'müsait',
  PRIMARY KEY (`kitap_id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kitaplar`
--

LOCK TABLES `kitaplar` WRITE;
/*!40000 ALTER TABLE `kitaplar` DISABLE KEYS */;
INSERT INTO `kitaplar` VALUES (1,'Fikralar','also','müsait'),(2,'Fikralar','also','müsait'),(3,'deneme','deneme','ödünç'),(4,'Sefiller','Victor Hugo','müsait'),(5,'Suç ve Ceza','Fyodor Dostoyevski','ödünç'),(6,'Yüzyıllık Yalnızlık','Gabriel Garcia Marquez','müsait'),(7,'1984','George Orwell','ödünç'),(8,'Hayvan Çiftliği','George Orwell','müsait'),(9,'Küçük Prens','Antoine de Saint-Exupéry','müsait'),(10,'Simyacı','Paulo Coelho','ödünç'),(11,'Beyaz Diş','Jack London','müsait'),(12,'Martin Eden','Jack London','ödünç'),(13,'Anna Karenina','Lev Tolstoy','müsait'),(14,'Savaş ve Barış','Lev Tolstoy','ödünç'),(15,'Fahrenheit 451','Ray Bradbury','müsait'),(16,'Cesur Yeni Dünya','Aldous Huxley','ödünç'),(17,'Dava','Franz Kafka','müsait'),(18,'Dönüşüm','Franz Kafka','ödünç'),(19,'Bilinmeyen Bir Kadının Mektubu','Stefan Zweig','müsait'),(20,'Satranç','Stefan Zweig','ödünç'),(21,'Kürk Mantolu Madonna','Sabahattin Ali','müsait'),(22,'İçimizdeki Şeytan','Sabahattin Ali','ödünç'),(23,'Çalıkuşu','Reşat Nuri Güntekin','müsait'),(24,'Yaprak Dökümü','Reşat Nuri Güntekin','ödünç'),(25,'Aşk-ı Memnu','Halit Ziya Uşaklıgil','müsait'),(26,'Mai ve Siyah','Halit Ziya Uşaklıgil','ödünç'),(27,'Dokuzuncu Hariciye Koğuşu','Peyami Safa','müsait'),(28,'Yalnızız','Peyami Safa','ödünç'),(29,'Otomatik Portakal','Anthony Burgess','müsait'),(30,'Uçurtma Avcısı','Khaled Hosseini','ödünç'),(31,'Bin Muhteşem Güneş','Khaled Hosseini','müsait'),(32,'Alacakaranlık','Stephenie Meyer','ödünç'),(33,'Açlık Oyunları','Suzanne Collins','müsait'),(34,'Divergent','Veronica Roth','ödünç'),(35,'Harry Potter ve Felsefe Taşı','J.K. Rowling','müsait'),(36,'Yüzüklerin Efendisi: Yüzük Kardeşliği','J.R.R. Tolkien','ödünç'),(37,'Hobbit','J.R.R. Tolkien','müsait'),(38,'Dune','Frank Herbert','ödünç'),(39,'Zaman Makinesi','H.G. Wells','müsait'),(40,'Görünmez Adam','H.G. Wells','ödünç'),(41,'Frankenstein','Mary Shelley','müsait'),(42,'Dracula','Bram Stoker','ödünç'),(43,'Gurur ve Önyargı','Jane Austen','müsait'),(44,'Aşk ve Gurur','Jane Austen','ödünç'),(45,'Jane Eyre','Charlotte Brontë','müsait'),(46,'Uğultulu Tepeler','Emily Brontë','ödünç'),(47,'Moby Dick','Herman Melville','müsait'),(48,'Bülbülü Öldürmek','Harper Lee','ödünç'),(49,'Gazap Üzümleri','John Steinbeck','müsait'),(50,'Fareler ve İnsanlar','John Steinbeck','ödünç'),(51,'Şeker Portakalı','José Mauro de Vasconcelos','müsait'),(52,'Karamazov Kardeşler','Fyodor Dostoyevski','ödünç'),(53,'Budala','Fyodor Dostoyevski','müsait'),(54,'Yüzüklerin Efendisi: Yüzük Kardeşliği','J.R.R. Tolkien','müsait'),(55,'Yüzüklerin Efendisi: İki Kule','J.R.R. Tolkien','ödünç'),(56,'Yüzüklerin Efendisi: Kralın Dönüşü','J.R.R. Tolkien','müsait'),(57,'Harry Potter ve Felsefe Taşı','J.K. Rowling','ödünç'),(58,'Harry Potter ve Sırlar Odası','J.K. Rowling','müsait'),(59,'Harry Potter ve Azkaban Tutsağı','J.K. Rowling','müsait'),(60,'Harry Potter ve Ateş Kadehi','J.K. Rowling','ödünç'),(61,'Harry Potter ve Zümrüdüanka Yoldaşlığı','J.K. Rowling','müsait'),(62,'Harry Potter ve Melez Prens','J.K. Rowling','ödünç'),(63,'Harry Potter ve Ölüm Yadigarları','J.K. Rowling','müsait'),(64,'Otostopçunun Galaksi Rehberi','Douglas Adams','müsait'),(65,'Solgun Mavi Nokta','Carl Sagan','ödünç'),(66,'Sineklerin Tanrısı','William Golding','müsait'),(67,'1984','George Orwell','ödünç'),(68,'Hayvan Çiftliği','George Orwell','müsait'),(69,'Cesur Yeni Dünya','Aldous Huxley','müsait'),(70,'Dönüşüm','Franz Kafka','ödünç'),(71,'Suç ve Ceza','Fyodor Dostoyevski','müsait'),(72,'Gurur ve Önyargı','Jane Austen','müsait'),(73,'Küçük Prens','Antoine de Saint-Exupéry','ödünç'),(74,'Zehranın Kitabı','Zehra','ödünç'),(75,'nutuk','mustafa kemal atatürk','ödünç');
/*!40000 ALTER TABLE `kitaplar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `odunc`
--

DROP TABLE IF EXISTS `odunc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `odunc` (
  `odunc_id` int NOT NULL AUTO_INCREMENT,
  `kitap_id` int DEFAULT NULL,
  `uye_id` int DEFAULT NULL,
  `odunc_tarihi` date DEFAULT NULL,
  `iade_tarihi` date DEFAULT NULL,
  PRIMARY KEY (`odunc_id`),
  KEY `kitap_id` (`kitap_id`),
  KEY `uye_id` (`uye_id`),
  CONSTRAINT `odunc_ibfk_1` FOREIGN KEY (`kitap_id`) REFERENCES `kitaplar` (`kitap_id`),
  CONSTRAINT `odunc_ibfk_2` FOREIGN KEY (`uye_id`) REFERENCES `uyeler` (`uye_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `odunc`
--

LOCK TABLES `odunc` WRITE;
/*!40000 ALTER TABLE `odunc` DISABLE KEYS */;
INSERT INTO `odunc` VALUES (1,3,1,'2025-05-16',NULL),(2,74,1,'2025-05-16','2025-05-16'),(3,75,22,'2025-05-16',NULL),(4,74,22,'2025-05-16',NULL);
/*!40000 ALTER TABLE `odunc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uyeler`
--

DROP TABLE IF EXISTS `uyeler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uyeler` (
  `uye_id` int NOT NULL AUTO_INCREMENT,
  `ad` varchar(50) NOT NULL,
  `soyad` varchar(50) NOT NULL,
  `sifre` varchar(50) NOT NULL,
  `kimlik_no` char(11) NOT NULL,
  PRIMARY KEY (`uye_id`),
  UNIQUE KEY `kimlik_no` (`kimlik_no`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uyeler`
--

LOCK TABLES `uyeler` WRITE;
/*!40000 ALTER TABLE `uyeler` DISABLE KEYS */;
INSERT INTO `uyeler` VALUES (1,'deneme','deneme','1234','12121212223'),(2,'Ahmet','Yılmaz','12345','11111111111'),(3,'Ayşe','Demir','67890','22222222222'),(4,'Mehmet','Öztürk','abcde','33333333333'),(5,'Fatma','Kaya','fghij','44444444444'),(6,'Ali','Şahin','klmno','55555555555'),(7,'Zeynep','Çelik','pqrst','66666666666'),(8,'Mustafa','Aydın','uvwxy','77777777777'),(9,'Gamze','Güneş','z1234','88888888888'),(10,'Emre','Arslan','56789','99999999999'),(11,'Selin','Yıldız','asdfg','10101010101'),(12,'Can','Korkmaz','hjklş','12121212121'),(13,'Deniz','Aksoy','qwerty','13131313131'),(14,'Burak','Can','yuiop','14141414141'),(15,'Gizem','Erol','asdfgh','15151515151'),(16,'Hakan','Koç','jklşi','16161616161'),(17,'İrem','Demir','zxcvb','17171717171'),(18,'Kerem','Kara','nmçö','18181818181'),(19,'Leyla','Sarı','1q2w3e','19191919191'),(20,'Okan','Taş','4r5t6y','20202020202'),(21,'Pınar','Yalın','7u8i9o','21212121212'),(22,'zehra','ışık','1234','12457658896');
/*!40000 ALTER TABLE `uyeler` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-17 17:42:27
