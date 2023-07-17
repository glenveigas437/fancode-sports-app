-- MySQL dump 10.13  Distrib 8.0.33, for macos13 (arm64)
--
-- Host: localhost    Database: fancode_sports_db
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('a45caa39628e');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matches`
--

DROP TABLE IF EXISTS `matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matches` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `tourId` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `format` varchar(50) NOT NULL,
  `startTime` timestamp NOT NULL,
  `endTime` timestamp NOT NULL,
  `recUpdatedAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `tourId` (`tourId`),
  CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`tourId`) REFERENCES `tour` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matches`
--

LOCK TABLES `matches` WRITE;
/*!40000 ALTER TABLE `matches` DISABLE KEYS */;
INSERT INTO `matches` VALUES (1,'GT vs RCB',1,1,'T20','2023-04-09 12:30:00','2023-04-09 17:30:00','2023-07-17 08:26:13','2023-07-17 08:26:13'),(2,'CSK vs MI',1,0,'T20','2023-04-10 12:30:00','2021-04-10 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08'),(3,'LSG vs KXIP',1,0,'T20','2023-04-11 12:30:00','2023-04-11 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08'),(4,'RR vs SRH',1,0,'T20','2023-04-12 12:30:00','2023-04-12 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08'),(5,'BLR vs BEN',2,0,'soccer','2023-04-29 12:30:00','2023-04-29 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08'),(6,'ATK vs MCFC',2,0,'soccer','2023-04-21 12:30:00','2023-04-21 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08'),(7,'KER vs JFC',2,0,'soccer','2023-04-22 12:30:00','2023-04-22 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08'),(8,'IND vs WI',3,0,'ODI','2023-06-10 04:30:00','2023-06-10 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08'),(9,'IND vs WI',3,0,'ODI','2023-06-12 04:30:00','2023-06-12 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08'),(10,'IND vs WI',3,0,'ODI','2023-06-14 04:30:00','2023-06-14 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08'),(11,'KER vs JFC',4,0,'soccer','2022-04-09 12:30:00','2022-04-09 17:30:00','2023-07-17 08:32:08','2023-07-17 08:32:08');
/*!40000 ALTER TABLE `matches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `sportId` int NOT NULL,
  `tourId` int NOT NULL,
  `matchId` int NOT NULL,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `sportId` (`sportId`),
  KEY `tourId` (`tourId`),
  KEY `matchId` (`matchId`),
  CONSTRAINT `news_ibfk_1` FOREIGN KEY (`sportId`) REFERENCES `sport` (`id`),
  CONSTRAINT `news_ibfk_2` FOREIGN KEY (`tourId`) REFERENCES `tour` (`id`),
  CONSTRAINT `news_ibfk_3` FOREIGN KEY (`matchId`) REFERENCES `matches` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (1,'Titans beat Challengers','Gujarat Titans clinched victory by six wickets in their final IPL 2023 league game and also knocked out Royal Challengers Bangalore, at the M Chinnaswamy Stadium in Bengaluru.',1,1,1,'2023-07-17 08:28:00'),(2,'Gaikwad-Conway Partnership','Top knocks from Ruturaj Gaikwad and Devon Conway guided Chennai Super Kings (CSK) to a six-wicket win over Mumbai Indians (MI) in their Indian Premier League (IPL) match at Chennai on Saturday.',1,1,2,'2023-07-16 06:59:00'),(3,'Punjab Kings fall short','Marcus Stoinis and Kyle Mayers put on a power-hitting masterclass as Lucknow Super Giants slayed Punjab Kings by 56 runs.',1,1,3,'2023-07-16 07:01:50'),(4,'Samad smashes a six after no-ball','After Sandeep Sharma overstepped of what was supposed to be the last ball of the innings, Abdul Samad smacked a six down the ground to seal a four-wicket win.',1,1,4,'2023-07-16 07:03:22'),(5,'Mumbai City seal playoff spot','Mumbai City beat ATK Mohun Bagan 1-0 to become the first side to confirm a playoff spot this season.',2,2,6,'2023-07-16 07:05:09'),(6,'East Bengal triumph over Bengaluru','East Bengal FC played against Bengaluru FC in 2 matches this season. Currently, East Bengal FC rank 10th.',2,2,5,'2023-07-16 07:07:37');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sport`
--

DROP TABLE IF EXISTS `sport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sport` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `recUpdatedAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sport`
--

LOCK TABLES `sport` WRITE;
/*!40000 ALTER TABLE `sport` DISABLE KEYS */;
INSERT INTO `sport` VALUES (1,'Cricket',1,'2023-07-16 18:11:08','2023-07-16 18:11:08'),(2,'Football',1,'2023-07-16 18:11:08','2023-07-16 18:11:08');
/*!40000 ALTER TABLE `sport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tour`
--

DROP TABLE IF EXISTS `tour`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tour` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `sportId` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `startTime` timestamp NOT NULL,
  `endTime` timestamp NOT NULL,
  `recUpdatedAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `sportId` (`sportId`),
  CONSTRAINT `tour_ibfk_1` FOREIGN KEY (`sportId`) REFERENCES `sport` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tour`
--

LOCK TABLES `tour` WRITE;
/*!40000 ALTER TABLE `tour` DISABLE KEYS */;
INSERT INTO `tour` VALUES (1,'Indian Premier League, 2023',1,1,'2023-04-08 18:30:00','2023-05-29 18:30:00','2023-07-17 08:24:35','2023-07-17 08:24:35'),(2,'India Super League, 2023',2,1,'2023-04-20 18:30:00','2023-06-19 18:30:00','2023-07-17 08:29:53','2023-07-17 08:29:53'),(3,'India Tour of West Indies, 2023',1,1,'2023-06-09 18:30:00','2023-06-28 18:30:00','2023-07-17 08:29:53','2023-07-17 08:29:53'),(4,'English Premier League, 2022',2,1,'2022-04-08 18:30:00','2022-05-29 18:30:00','2023-07-17 08:29:53','2023-07-17 08:29:53');
/*!40000 ALTER TABLE `tour` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-17 15:19:26
