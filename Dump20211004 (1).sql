-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: kindly
-- ------------------------------------------------------
-- Server version	5.7.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `doadores`
--

DROP TABLE IF EXISTS `doadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doadores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `senha` varchar(100) DEFAULT NULL,
  `foto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doadores`
--

LOCK TABLES `doadores` WRITE;
/*!40000 ALTER TABLE `doadores` DISABLE KEYS */;
INSERT INTO `doadores` VALUES (1,'joao','jvsd','1234',NULL),(2,'jaozin','sla.com','123',NULL),(3,'Cassissi','cassi123','aaa',NULL),(4,'Digite seu nome completo','sla.com','123',NULL),(5,'qua','sla.com','11',NULL),(6,'aaaaaaaaaaaaaaa','aaaaaaa2','123',NULL),(7,'cassi linda','linda@sla.com','cassi123',NULL);
/*!40000 ALTER TABLE `doadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instituicoes`
--

DROP TABLE IF EXISTS `instituicoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `instituicoes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `foto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instituicoes`
--

LOCK TABLES `instituicoes` WRITE;
/*!40000 ALTER TABLE `instituicoes` DISABLE KEYS */;
INSERT INTO `instituicoes` VALUES (1,'teste','teste123@gamil.com','gNojTsfagh',NULL),(2,'aaaa','teste@gmail.com','3nWWujUa6n',NULL),(3,NULL,NULL,'ntRMo6u5Be',NULL),(4,NULL,NULL,'gLKjeNxyFx',NULL),(5,NULL,NULL,'v4GycHrFuH',NULL),(6,NULL,NULL,'ehy70qjEtI',NULL),(7,NULL,NULL,'rhJs4YIBc3',NULL);
/*!40000 ALTER TABLE `instituicoes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-04 16:43:54
