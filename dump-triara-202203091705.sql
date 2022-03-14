-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: triara
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.22-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Admins');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(13,1,13),(14,1,14),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,1,52);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add reporte fallas',7,'add_reportefallas'),(26,'Can change reporte fallas',7,'change_reportefallas'),(27,'Can delete reporte fallas',7,'delete_reportefallas'),(28,'Can view reporte fallas',7,'view_reportefallas'),(29,'Can add vendor',8,'add_vendor'),(30,'Can change vendor',8,'change_vendor'),(31,'Can delete vendor',8,'delete_vendor'),(32,'Can view vendor',8,'view_vendor'),(33,'Can add cambio hw',9,'add_cambiohw'),(34,'Can change cambio hw',9,'change_cambiohw'),(35,'Can delete cambio hw',9,'delete_cambiohw'),(36,'Can view cambio hw',9,'view_cambiohw'),(37,'Can add ambiente',10,'add_ambiente'),(38,'Can change ambiente',10,'change_ambiente'),(39,'Can delete ambiente',10,'delete_ambiente'),(40,'Can view ambiente',10,'view_ambiente'),(41,'Can add tipo falla',11,'add_tipofalla'),(42,'Can change tipo falla',11,'change_tipofalla'),(43,'Can delete tipo falla',11,'delete_tipofalla'),(44,'Can view tipo falla',11,'view_tipofalla'),(45,'Can add componente',12,'add_componente'),(46,'Can change componente',12,'change_componente'),(47,'Can delete componente',12,'delete_componente'),(48,'Can view componente',12,'view_componente'),(49,'Can add cierre falla',13,'add_cierrefalla'),(50,'Can change cierre falla',13,'change_cierrefalla'),(51,'Can delete cierre falla',13,'delete_cierrefalla'),(52,'Can view cierre falla',13,'view_cierrefalla'),(53,'Can add categoria',11,'add_categoria'),(54,'Can change categoria',11,'change_categoria'),(55,'Can delete categoria',11,'delete_categoria'),(56,'Can view categoria',11,'view_categoria');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$MF8383mxwndmz2ozFYwYNY$3YIPCa77yNxyknwlopM7iUZVImPl/ZTvh/v4PJCEc7g=','2022-03-07 18:18:51.207526',1,'birkoff','Manuel','Meneses','manuel.meneses@triara.com',1,1,'2022-02-08 18:05:19.000000'),(2,'pbkdf2_sha256$320000$bF1sxcLC4cNUpvfigAGA4P$7hi+2URhNaMe02PhFprXYtEQO7pECM+5TiTHqtjFhJk=','2022-02-15 21:05:18.000000',0,'angel.lozano','Angel','Lozano','jesus.lozano@triara.com',1,1,'2022-02-15 21:04:13.000000'),(3,'pbkdf2_sha256$320000$UA8lF0rS2e0hK47eEy0CQm$576EZpdhDfNs/Fb+xbmZSoPVXXLqWOAiVL1QP1JBimQ=',NULL,0,'hector.ortiz','Héctor','Ortíz','',1,1,'2022-02-16 01:35:09.000000'),(4,'pbkdf2_sha256$320000$FXrDBoPIdMfxgP250HfwuW$d4EWGXuwFJ2lIUAP19WR6N2I06oZ+yRID59ixtmXeeM=',NULL,0,'luis.ramirez','Luis','Ramírez','',1,1,'2022-02-16 01:35:23.000000'),(5,'pbkdf2_sha256$320000$9LhKWOltKrxaqW4MKbcSlR$+pSiODyTZUp1cf9bMda4CaBQaQMKb3903WEmvf8XODk=',NULL,0,'rodolfo.mena','Rodolfo','Mena','',1,1,'2022-02-16 01:35:31.000000'),(6,'pbkdf2_sha256$260000$HDnO79dQycFFDE7y2mxnzU$zfm2wNLMJVdjnymEYeXCmfSsU/Ht4YS9jjjbacTTvac=','2022-02-23 18:11:49.876588',0,'erik.arroyo','Erik','Arroyo','',1,1,'2022-02-16 01:36:19.000000'),(7,'pbkdf2_sha256$320000$6emC7cMvSBR2E2eJOIli33$ijxNopnilSqHfww60PwBLmMLJwc57zxRB8K9enQn+JM=',NULL,0,'diego.montoya','Diego','Montoya','',1,1,'2022-02-16 01:36:26.000000'),(8,'pbkdf2_sha256$320000$7DgVpLmVhjtYMq8aqnjhnH$+xEj1qojDaJMaCnOC0SfbxYR7C31KHg++8SyMHj+MEc=',NULL,0,'jorge.ramirez','Jorge','Ramírez','',1,1,'2022-02-16 01:36:34.000000'),(9,'pbkdf2_sha256$320000$lYMtfFHPQYao9L3C4RHvvY$2VVq/FyMrIUVEgXjq7r7mdF5oX302/rz5kQnn+AK9hA=',NULL,0,'miguel.pinzon','Miguel','Pinzón','',1,1,'2022-02-16 01:36:44.000000'),(10,'pbkdf2_sha256$320000$D7v0NesTHlfNllKOCKJjF0$yeBAe569LOb7tIsVG+ShRwkqvdf8ZJ8zUZHH5TR+roA=',NULL,0,'esdras.orizaba','Esdras','Orizaba','',1,1,'2022-02-16 01:37:10.000000'),(11,'pbkdf2_sha256$260000$UsF5zKua9l9MTOqeKNch9I$IX0OzsbXIy/nJu5O+9fyipXGeWIXYzKKgifpSvuYwRg=','2022-02-23 23:04:22.789829',0,'manuel.meneses','Manuel','Meneses','manuel.meneses@triara.com',1,1,'2022-02-16 01:37:21.000000'),(12,'pbkdf2_sha256$320000$cyLJSAYzy956B3UlzBRGmQ$49cs/R1OM5q4sEvPVPfXiH4ydbM7QKam3+7Xu7hGUrE=',NULL,0,'tonatiuh.mata','Tonatiuh','Mata','',1,1,'2022-02-16 01:37:31.000000'),(13,'pbkdf2_sha256$320000$Fc0Z6e90gLNAFKTBabitmK$R0hhZ0ruT2nWKppHl/fABbO8hCatiJBpSWg4okW6w9M=',NULL,0,'rene.alcalde','Rene','Alcalde','',1,1,'2022-02-16 01:37:47.000000'),(14,'pbkdf2_sha256$260000$C0iVyqcpl474vdj8HfozY6$W9C2nVg7K8GZiYY0CQ4EwJWBr/UfCvU2qlWusiMCWUk=',NULL,0,'cynthia.gutierrez','Cynthia','Gutiérrez Vargas','cynthia.gutierrez@triara.com',1,1,'2022-02-23 18:16:39.000000'),(15,'pbkdf2_sha256$260000$3NGe7UqrhcLGeztWV0lX2G$pgziwnnWWcGvPuk3rKyXBFh5ALswa/SqGTr0U+KS4Wc=','2022-02-23 18:24:31.000000',0,'luis.garcia','Luis','García','luis.garciag@triara.com',1,1,'2022-02-23 18:17:41.000000'),(16,'pbkdf2_sha256$260000$JhppHy16rDdBcAUa9ygn65$Mpo2525QkoVAhcli83Orh4LGkWVKQrSzhTmln4IyD04=',NULL,0,'patricio.silva','','','',0,1,'2022-02-23 23:45:16.235776'),(17,'pbkdf2_sha256$260000$w6jcQD53aIfHwt1U8vegdo$PWtFtvVvpAm5JFUaO+bMIDPhnmEuqGo5BMLkAO+LQzo=',NULL,0,'ricardo.lopez','','','',0,1,'2022-02-23 23:45:46.435834');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,14,1),(2,15,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=155 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-02-08 18:06:39.954481','1','birkoff',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),(2,'2022-02-14 18:56:12.236670','1','Dell',1,'[{\"added\": {}}]',8,1),(3,'2022-02-14 18:58:04.020967','2','HPE',1,'[{\"added\": {}}]',8,1),(4,'2022-02-14 18:58:07.386880','3','Cisco',1,'[{\"added\": {}}]',8,1),(5,'2022-02-14 18:58:10.740310','4','VMware',1,'[{\"added\": {}}]',8,1),(6,'2022-02-14 18:59:00.053982','1','AMX USA',1,'[{\"added\": {}}]',10,1),(7,'2022-02-14 18:59:07.367350','2','AMX ECU',1,'[{\"added\": {}}]',10,1),(8,'2022-02-14 18:59:23.219675','3','NPV',1,'[{\"added\": {}}]',10,1),(9,'2022-02-14 18:59:26.137230','4','NPE',1,'[{\"added\": {}}]',10,1),(10,'2022-02-14 18:59:49.435635','5','OACI',1,'[{\"added\": {}}]',10,1),(11,'2022-02-14 18:59:58.933165','1','Si',1,'[{\"added\": {}}]',9,1),(12,'2022-02-14 19:00:01.603986','2','No',1,'[{\"added\": {}}]',9,1),(13,'2022-02-14 19:00:04.879949','3','Pendiente',1,'[{\"added\": {}}]',9,1),(14,'2022-02-14 19:45:33.019172','2','reporteFallas object (2)',3,'',7,1),(15,'2022-02-14 19:45:33.081250','1','reporteFallas object (1)',3,'',7,1),(16,'2022-02-14 19:50:00.960850','4','reporteFallas object (4)',3,'',7,1),(17,'2022-02-14 19:50:01.032646','3','reporteFallas object (3)',3,'',7,1),(18,'2022-02-15 21:04:14.046009','2','cgutierrez',1,'[{\"added\": {}}]',4,1),(19,'2022-02-15 21:05:02.653843','2','cgutierrez',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\"]}}]',4,1),(20,'2022-02-15 22:11:24.660089','5','Huawei',1,'[{\"added\": {}}]',8,1),(21,'2022-02-15 22:11:27.970265','6','RedHat',1,'[{\"added\": {}}]',8,1),(22,'2022-02-15 22:11:50.821602','6','GMM',1,'[{\"added\": {}}]',10,1),(23,'2022-02-15 22:11:55.910886','7','AMX ARG',1,'[{\"added\": {}}]',10,1),(24,'2022-02-15 22:12:02.014428','8','GBMV',1,'[{\"added\": {}}]',10,1),(25,'2022-02-15 22:12:08.343298','9','AMX COL',1,'[{\"added\": {}}]',10,1),(26,'2022-02-15 22:17:39.457244','2','Hardware',1,'[{\"added\": {}}]',11,1),(27,'2022-02-15 22:17:43.606746','3','Software',1,'[{\"added\": {}}]',11,1),(28,'2022-02-15 22:18:01.534310','4','Pendiente',1,'[{\"added\": {}}]',11,1),(29,'2022-02-16 01:25:42.064640','63','reporteFallas object (63)',3,'',7,1),(30,'2022-02-16 01:25:42.179589','62','reporteFallas object (62)',3,'',7,1),(31,'2022-02-16 01:25:42.359124','61','reporteFallas object (61)',3,'',7,1),(32,'2022-02-16 01:25:42.414557','60','reporteFallas object (60)',3,'',7,1),(33,'2022-02-16 01:25:42.459723','59','reporteFallas object (59)',3,'',7,1),(34,'2022-02-16 01:25:42.492339','58','reporteFallas object (58)',3,'',7,1),(35,'2022-02-16 01:25:42.526165','57','reporteFallas object (57)',3,'',7,1),(36,'2022-02-16 01:25:42.558731','56','reporteFallas object (56)',3,'',7,1),(37,'2022-02-16 01:25:42.592643','55','reporteFallas object (55)',3,'',7,1),(38,'2022-02-16 01:25:42.625765','54','reporteFallas object (54)',3,'',7,1),(39,'2022-02-16 01:25:42.659254','53','reporteFallas object (53)',3,'',7,1),(40,'2022-02-16 01:25:42.692395','52','reporteFallas object (52)',3,'',7,1),(41,'2022-02-16 01:25:42.759196','51','reporteFallas object (51)',3,'',7,1),(42,'2022-02-16 01:25:42.802017','50','reporteFallas object (50)',3,'',7,1),(43,'2022-02-16 01:25:42.880047','49','reporteFallas object (49)',3,'',7,1),(44,'2022-02-16 01:25:42.925700','48','reporteFallas object (48)',3,'',7,1),(45,'2022-02-16 01:25:42.959430','47','reporteFallas object (47)',3,'',7,1),(46,'2022-02-16 01:25:42.992638','46','reporteFallas object (46)',3,'',7,1),(47,'2022-02-16 01:25:43.025716','45','reporteFallas object (45)',3,'',7,1),(48,'2022-02-16 01:25:43.059340','44','reporteFallas object (44)',3,'',7,1),(49,'2022-02-16 01:25:43.091023','43','reporteFallas object (43)',3,'',7,1),(50,'2022-02-16 01:25:43.113913','42','reporteFallas object (42)',3,'',7,1),(51,'2022-02-16 01:25:43.135140','41','reporteFallas object (41)',3,'',7,1),(52,'2022-02-16 01:25:43.157906','40','reporteFallas object (40)',3,'',7,1),(53,'2022-02-16 01:25:43.191138','39','reporteFallas object (39)',3,'',7,1),(54,'2022-02-16 01:25:43.314024','38','reporteFallas object (38)',3,'',7,1),(55,'2022-02-16 01:25:43.357604','37','reporteFallas object (37)',3,'',7,1),(56,'2022-02-16 01:25:43.391580','36','reporteFallas object (36)',3,'',7,1),(57,'2022-02-16 01:25:43.425949','35','reporteFallas object (35)',3,'',7,1),(58,'2022-02-16 01:25:43.460019','34','reporteFallas object (34)',3,'',7,1),(59,'2022-02-16 01:25:43.492839','33','reporteFallas object (33)',3,'',7,1),(60,'2022-02-16 01:25:43.510889','32','reporteFallas object (32)',3,'',7,1),(61,'2022-02-16 01:25:43.537169','31','reporteFallas object (31)',3,'',7,1),(62,'2022-02-16 01:25:43.554616','30','reporteFallas object (30)',3,'',7,1),(63,'2022-02-16 01:25:43.581132','29','reporteFallas object (29)',3,'',7,1),(64,'2022-02-16 01:25:43.621552','28','reporteFallas object (28)',3,'',7,1),(65,'2022-02-16 01:25:43.659090','27','reporteFallas object (27)',3,'',7,1),(66,'2022-02-16 01:25:43.677694','26','reporteFallas object (26)',3,'',7,1),(67,'2022-02-16 01:25:43.702904','25','reporteFallas object (25)',3,'',7,1),(68,'2022-02-16 01:25:43.722591','24','reporteFallas object (24)',3,'',7,1),(69,'2022-02-16 01:25:43.767503','23','reporteFallas object (23)',3,'',7,1),(70,'2022-02-16 01:25:43.791584','22','reporteFallas object (22)',3,'',7,1),(71,'2022-02-16 01:25:43.811924','21','reporteFallas object (21)',3,'',7,1),(72,'2022-02-16 01:25:43.846991','20','reporteFallas object (20)',3,'',7,1),(73,'2022-02-16 01:25:43.936577','19','reporteFallas object (19)',3,'',7,1),(74,'2022-02-16 01:25:44.025739','18','reporteFallas object (18)',3,'',7,1),(75,'2022-02-16 01:25:44.101846','17','reporteFallas object (17)',3,'',7,1),(76,'2022-02-16 01:25:44.147084','16','reporteFallas object (16)',3,'',7,1),(77,'2022-02-16 01:25:44.179917','15','reporteFallas object (15)',3,'',7,1),(78,'2022-02-16 01:25:44.213748','14','reporteFallas object (14)',3,'',7,1),(79,'2022-02-16 01:25:44.247640','13','reporteFallas object (13)',3,'',7,1),(80,'2022-02-16 01:25:44.281979','12','reporteFallas object (12)',3,'',7,1),(81,'2022-02-16 01:25:44.313111','11','reporteFallas object (11)',3,'',7,1),(82,'2022-02-16 01:25:44.346949','10','reporteFallas object (10)',3,'',7,1),(83,'2022-02-16 01:25:44.379863','9','reporteFallas object (9)',3,'',7,1),(84,'2022-02-16 01:25:44.414310','8','reporteFallas object (8)',3,'',7,1),(85,'2022-02-16 01:25:44.447462','7','reporteFallas object (7)',3,'',7,1),(86,'2022-02-16 01:25:44.480816','6','reporteFallas object (6)',3,'',7,1),(87,'2022-02-16 01:25:44.513155','5','reporteFallas object (5)',3,'',7,1),(88,'2022-02-16 01:25:44.536316','4','reporteFallas object (4)',3,'',7,1),(89,'2022-02-16 01:25:44.569053','3','reporteFallas object (3)',3,'',7,1),(90,'2022-02-16 01:25:44.615310','2','reporteFallas object (2)',3,'',7,1),(91,'2022-02-16 01:25:44.648227','1','reporteFallas object (1)',3,'',7,1),(92,'2022-02-16 01:34:43.970946','2','angel.lozano',2,'[{\"changed\": {\"fields\": [\"Username\", \"First name\", \"Last name\", \"Email address\"]}}]',4,1),(93,'2022-02-16 01:35:09.952984','3','hector.ortiz',1,'[{\"added\": {}}]',4,1),(94,'2022-02-16 01:35:23.865699','4','luis.ramirez',1,'[{\"added\": {}}]',4,1),(95,'2022-02-16 01:35:31.694194','5','rodolfo.mena',1,'[{\"added\": {}}]',4,1),(96,'2022-02-16 01:36:20.033355','6','erik.arroyo',1,'[{\"added\": {}}]',4,1),(97,'2022-02-16 01:36:27.121858','7','diego.montoya',1,'[{\"added\": {}}]',4,1),(98,'2022-02-16 01:36:34.923770','8','jorge.ramirez',1,'[{\"added\": {}}]',4,1),(99,'2022-02-16 01:36:44.434280','9','miguel.pinzon',1,'[{\"added\": {}}]',4,1),(100,'2022-02-16 01:37:10.638811','10','esdras.orizaba',1,'[{\"added\": {}}]',4,1),(101,'2022-02-16 01:37:21.935657','11','manuel.meneses',1,'[{\"added\": {}}]',4,1),(102,'2022-02-16 01:37:31.694627','12','tonatiuh.mata',1,'[{\"added\": {}}]',4,1),(103,'2022-02-16 01:37:47.603441','13','rene.alcalde',1,'[{\"added\": {}}]',4,1),(104,'2022-02-16 04:31:30.494929','4','VMWare',2,'[{\"changed\": {\"fields\": [\"Falla\"]}}]',11,1),(105,'2022-02-16 05:38:46.975508','12','tonatiuh.mata',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(106,'2022-02-17 18:50:51.480685','4','VMWare',3,'',11,1),(107,'2022-02-18 01:38:37.260956','1','Fabric Connect',1,'[{\"added\": {}}]',12,1),(108,'2022-02-18 01:39:02.086227','2','ESX 7.1.0',1,'[{\"added\": {}}]',12,1),(109,'2022-02-23 18:10:59.572438','7','diego.montoya',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(110,'2022-02-23 18:11:11.093482','6','erik.arroyo',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(111,'2022-02-23 18:12:19.495219','10','esdras.orizaba',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(112,'2022-02-23 18:12:47.204484','3','hector.ortiz',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(113,'2022-02-23 18:13:03.297602','8','jorge.ramirez',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(114,'2022-02-23 18:13:19.959085','4','luis.ramirez',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(115,'2022-02-23 18:15:13.706917','11','manuel.meneses',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\", \"Superuser status\"]}}]',4,1),(116,'2022-02-23 18:15:27.022481','9','miguel.pinzon',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(117,'2022-02-23 18:15:34.801719','11','manuel.meneses',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(118,'2022-02-23 18:15:49.880473','13','rene.alcalde',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(119,'2022-02-23 18:16:02.354488','5','rodolfo.mena',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(120,'2022-02-23 18:16:15.480465','12','tonatiuh.mata',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),(121,'2022-02-23 18:16:39.311087','14','cynthia.hernandez',1,'[{\"added\": {}}]',4,1),(122,'2022-02-23 18:17:21.024377','14','cynthia.gutierrez',2,'[{\"changed\": {\"fields\": [\"Username\", \"First name\", \"Last name\", \"Email address\", \"Staff status\"]}}]',4,1),(123,'2022-02-23 18:17:42.047930','15','luis.garcia',1,'[{\"added\": {}}]',4,1),(124,'2022-02-23 18:21:09.821729','15','luis.garcia',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Staff status\", \"Superuser status\"]}}]',4,1),(125,'2022-02-23 18:21:31.788132','11','manuel.meneses',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]',4,1),(126,'2022-02-23 18:22:31.399235','15','luis.garcia',2,'[{\"changed\": {\"fields\": [\"Superuser status\"]}}]',4,1),(127,'2022-02-23 18:25:27.033306','1','Admins',1,'[{\"added\": {}}]',3,1),(128,'2022-02-23 18:25:42.220712','14','cynthia.gutierrez',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(129,'2022-02-23 18:25:54.496230','15','luis.garcia',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(130,'2022-02-23 18:26:32.093681','1','Admins',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(131,'2022-02-23 18:26:38.249136','1','Admins',2,'[]',3,1),(132,'2022-02-23 18:27:55.518638','1','Admins',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(133,'2022-02-23 23:33:31.103863','7','SuSE',1,'[{\"added\": {}}]',8,1),(134,'2022-02-23 23:33:55.832351','8','SMTP2GO',1,'[{\"added\": {}}]',8,1),(135,'2022-02-23 23:34:39.807584','8','SMTP2GO',3,'',8,1),(136,'2022-02-23 23:34:55.401135','9','Microsoft',1,'[{\"added\": {}}]',8,1),(137,'2022-02-23 23:35:38.011205','10','Lenovo',1,'[{\"added\": {}}]',8,1),(138,'2022-02-23 23:45:16.449619','16','patricio.silva',1,'[{\"added\": {}}]',4,1),(139,'2022-02-23 23:45:46.819519','17','ricardo.lopez',1,'[{\"added\": {}}]',4,1),(140,'2022-03-01 02:58:56.684123','10','AMX BR',1,'[{\"added\": {}}]',10,1),(141,'2022-03-01 02:59:04.371326','11','AMX CH',1,'[{\"added\": {}}]',10,1),(142,'2022-03-01 02:59:12.851911','12','AMX DOM',1,'[{\"added\": {}}]',10,1),(143,'2022-03-01 02:59:20.567512','13','AMX GUAT',1,'[{\"added\": {}}]',10,1),(144,'2022-03-01 02:59:27.351781','14','AMX PERU',1,'[{\"added\": {}}]',10,1),(145,'2022-03-01 02:59:32.267645','15','AMX PTO RICO',1,'[{\"added\": {}}]',10,1),(146,'2022-03-01 02:59:46.226278','16','CENAM',1,'[{\"added\": {}}]',10,1),(147,'2022-03-01 03:03:53.892500','17','CONDUMEX',1,'[{\"added\": {}}]',10,1),(148,'2022-03-02 03:51:17.616892','3','Disk',1,'[{\"added\": {}}]',12,1),(149,'2022-03-02 03:54:33.775188','11','Cisco',1,'[{\"added\": {}}]',8,1),(150,'2022-03-02 03:58:44.173158','12','Dell',1,'[{\"added\": {}}]',8,1),(151,'2022-03-02 03:58:52.415937','13','Huawei',1,'[{\"added\": {}}]',8,1),(152,'2022-03-02 03:59:03.771481','14','HPE',1,'[{\"added\": {}}]',8,1),(153,'2022-03-02 03:59:13.640231','15','Lenovo',1,'[{\"added\": {}}]',8,1),(154,'2022-03-07 20:12:58.470179','181','RHUI',2,'[{\"changed\": {\"fields\": [\"Componente\"]}}]',12,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'reportInfra','ambiente'),(9,'reportInfra','cambiohw'),(11,'reportInfra','categoria'),(13,'reportInfra','cierrefalla'),(12,'reportInfra','componente'),(7,'reportInfra','reportefallas'),(8,'reportInfra','vendor'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-02-08 18:04:30.837846'),(2,'auth','0001_initial','2022-02-08 18:04:35.382335'),(3,'admin','0001_initial','2022-02-08 18:04:36.664737'),(4,'admin','0002_logentry_remove_auto_add','2022-02-08 18:04:36.696156'),(5,'admin','0003_logentry_add_action_flag_choices','2022-02-08 18:04:36.733529'),(6,'contenttypes','0002_remove_content_type_name','2022-02-08 18:04:37.287167'),(7,'auth','0002_alter_permission_name_max_length','2022-02-08 18:04:38.169535'),(8,'auth','0003_alter_user_email_max_length','2022-02-08 18:04:38.273323'),(9,'auth','0004_alter_user_username_opts','2022-02-08 18:04:38.318989'),(10,'auth','0005_alter_user_last_login_null','2022-02-08 18:04:38.944683'),(11,'auth','0006_require_contenttypes_0002','2022-02-08 18:04:38.969780'),(12,'auth','0007_alter_validators_add_error_messages','2022-02-08 18:04:39.028607'),(13,'auth','0008_alter_user_username_max_length','2022-02-08 18:04:39.082760'),(14,'auth','0009_alter_user_last_name_max_length','2022-02-08 18:04:39.166960'),(15,'auth','0010_alter_group_name_max_length','2022-02-08 18:04:39.226336'),(16,'auth','0011_update_proxy_permissions','2022-02-08 18:04:39.266414'),(17,'auth','0012_alter_user_first_name_max_length','2022-02-08 18:04:39.316576'),(18,'sessions','0001_initial','2022-02-08 18:04:39.515928'),(19,'reportInfra','0001_initial','2022-02-08 18:50:57.357100'),(20,'reportInfra','0002_alter_reportefallas_cambiohw_and_more','2022-02-14 19:01:19.305314'),(21,'reportInfra','0003_alter_reportefallas_fecha','2022-02-14 22:22:06.616333'),(22,'reportInfra','0004_alter_reportefallas_fecha_alter_reportefallas_motivo','2022-02-15 21:35:02.918263'),(23,'reportInfra','0005_tipofalla_alter_reportefallas_cambiohw_and_more','2022-02-15 22:15:02.362802'),(24,'reportInfra','0006_alter_reportefallas_motivo_and_more','2022-02-15 22:53:32.539047'),(25,'reportInfra','0007_alter_reportefallas_descripcion','2022-02-16 02:14:59.536901'),(26,'reportInfra','0008_alter_ambiente_options_alter_cambiohw_options_and_more','2022-02-16 04:34:45.150115'),(27,'reportInfra','0009_alter_reportefallas_fecha','2022-02-16 04:50:18.079284'),(28,'reportInfra','0010_remove_reportefallas_motivo_componente_and_more','2022-02-17 00:06:44.684054'),(29,'reportInfra','0011_cierrefalla','2022-02-23 18:03:19.996452'),(30,'reportInfra','0012_remove_cierrefalla_idfalla','2022-02-23 20:41:20.348287'),(31,'reportInfra','0013_auto_20220228_1957','2022-03-01 01:57:43.714417'),(32,'reportInfra','0014_auto_20220228_2007','2022-03-01 02:07:24.049586'),(33,'reportInfra','0015_vendor_idcategoria','2022-03-01 03:10:13.587678'),(34,'reportInfra','0016_cierrefalla_idfalla','2022-03-03 01:05:53.752322'),(35,'reportInfra','0017_rename_idfalla_cierrefalla_idfalla','2022-03-03 01:06:53.303723');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1v1h9yhg0sx92nzeguh2xi0gwpqj4nk6','.eJxVjEEOwiAQRe_C2pCCTMu4dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKtxTl0KUG2zkBmjEyWfZ8JUSIna5wMPWEEZxEABAeP3tozgulYuqjeH_LjN8A:1nRHwZ:rjiVFY75tFqvTlk1QDFfoOrHs7LBL73GJ1nauqfh7No','2022-03-21 18:18:51.389487'),('hokjzqqhhqdwi2e7gnqc92nfwwj7e5ep','.eJxVjEEOwiAQRe_C2pCCTMu4dN8zkIEZpGpoUtqV8e7apAvd_vfef6lA21rC1mQJE6uLMur0u0VKD6k74DvV26zTXNdlinpX9EGbHmeW5_Vw_w4KtfKtxTl0KUG2zkBmjEyWfZ8JUSIna5wMPWEEZxEABAeP3tozgulYuqjeH_LjN8A:1nN0mn:1KzNbbSNTDxA0XYn-WTpGIrfKZo2cucS_jr9wXFlH58','2022-03-09 23:11:05.803189');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reportinfra_ambiente`
--

DROP TABLE IF EXISTS `reportinfra_ambiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportinfra_ambiente` (
  `idAmbiente` int(11) NOT NULL AUTO_INCREMENT,
  `NombreAmbiente` varchar(100) NOT NULL,
  PRIMARY KEY (`idAmbiente`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reportinfra_ambiente`
--

LOCK TABLES `reportinfra_ambiente` WRITE;
/*!40000 ALTER TABLE `reportinfra_ambiente` DISABLE KEYS */;
INSERT INTO `reportinfra_ambiente` VALUES (1,'AMX USA'),(2,'AMX ECU'),(3,'NPV'),(4,'NPE'),(5,'OACI'),(6,'GMM'),(7,'AMX ARG'),(8,'GBMV'),(9,'AMX COL'),(10,'AMX BR'),(11,'AMX CH'),(12,'AMX DOM'),(13,'AMX GUAT'),(14,'AMX PERU'),(15,'AMX PTO RICO'),(16,'CENAM'),(17,'CONDUMEX');
/*!40000 ALTER TABLE `reportinfra_ambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reportinfra_cambiohw`
--

DROP TABLE IF EXISTS `reportinfra_cambiohw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportinfra_cambiohw` (
  `idHW` int(11) NOT NULL AUTO_INCREMENT,
  `NombreHW` varchar(100) NOT NULL,
  PRIMARY KEY (`idHW`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reportinfra_cambiohw`
--

LOCK TABLES `reportinfra_cambiohw` WRITE;
/*!40000 ALTER TABLE `reportinfra_cambiohw` DISABLE KEYS */;
INSERT INTO `reportinfra_cambiohw` VALUES (1,'Si'),(2,'No'),(3,'Pendiente');
/*!40000 ALTER TABLE `reportinfra_cambiohw` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reportinfra_categoria`
--

DROP TABLE IF EXISTS `reportinfra_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportinfra_categoria` (
  `idTipo` int(11) NOT NULL AUTO_INCREMENT,
  `Categoria` varchar(100) NOT NULL,
  PRIMARY KEY (`idTipo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reportinfra_categoria`
--

LOCK TABLES `reportinfra_categoria` WRITE;
/*!40000 ALTER TABLE `reportinfra_categoria` DISABLE KEYS */;
INSERT INTO `reportinfra_categoria` VALUES (2,'Hardware'),(3,'Software');
/*!40000 ALTER TABLE `reportinfra_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reportinfra_cierrefalla`
--

DROP TABLE IF EXISTS `reportinfra_cierrefalla`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportinfra_cierrefalla` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ComentarioCierre` longtext DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `idFalla` longtext DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reportinfra_cierrefalla`
--

LOCK TABLES `reportinfra_cierrefalla` WRITE;
/*!40000 ALTER TABLE `reportinfra_cierrefalla` DISABLE KEYS */;
INSERT INTO `reportinfra_cierrefalla` VALUES (1,'asdasdas','2022-03-03 01:54:14.343253','1075381229'),(2,'Hola, espero que funcione!!!!','2022-03-03 02:20:38.999260','1076278953'),(3,'Pues un link down','2022-03-03 02:22:38.315443','1081335416'),(4,'asdasdsa','2022-03-03 02:23:25.213372','Test'),(5,'asdasdas','2022-03-03 02:23:44.537330','Test'),(6,'asdasdasdas','2022-03-03 02:24:12.864220','Test'),(7,'asdasdas','2022-03-03 02:24:56.004297','Test'),(8,'sadasdas','2022-03-03 02:25:27.612233','Test'),(9,'sdsdasdas','2022-03-03 02:25:39.493016','1081335416'),(10,'asdasdsadas','2022-03-03 02:25:50.524429','1083007408'),(11,'sadasdsadas','2022-03-03 02:28:00.936452','1081190553'),(12,'ssaddasdasdas','2022-03-03 02:28:14.426838','21285682912'),(13,'asdasdas','2022-03-03 02:28:59.563337','21278998911'),(14,'asdasdas','2022-03-03 02:29:14.207236','1080717754'),(15,'asdadsada','2022-03-03 02:32:32.963800','1081335416'),(16,'asdadasas','2022-03-03 02:32:59.145805','1081335416'),(17,'asdasdsadsa','2022-03-03 02:33:16.895098','1081190039'),(18,'asdsadsad','2022-03-03 02:33:31.857916','1080725620'),(19,'asdasdas','2022-03-03 03:53:27.567611','1080717754'),(20,'asdsadsdas','2022-03-03 03:55:56.953510','Test'),(21,'TEst 1518522','2022-03-03 03:56:16.492868','Test'),(22,'asdasdsa','2022-03-03 04:05:28.928715','v950440'),(23,'asdasdsadas','2022-03-03 04:05:31.910278','v950440'),(24,'Ya por fin cerro este pedo','2022-03-03 04:12:01.817297','1076278953'),(25,'Se ejecutaron los comandos que me envio Dell','2022-03-07 17:22:35.656763','1086223591'),(26,'Ahora me piden que actualice el FW iDRAC','2022-03-07 17:23:21.681108','1086223591'),(27,'Se finaliza con el caso con la solución que envió Dell\r\nCerrar SR','2022-03-07 17:24:02.730702','1086223591');
/*!40000 ALTER TABLE `reportinfra_cierrefalla` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reportinfra_componente`
--

DROP TABLE IF EXISTS `reportinfra_componente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportinfra_componente` (
  `idComponente` int(11) NOT NULL AUTO_INCREMENT,
  `Componente` varchar(100) NOT NULL,
  `idVendor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`idComponente`),
  KEY `reportInfra_componen_idVendor_id_1cae764b_fk_reportInf` (`idVendor_id`),
  CONSTRAINT `reportInfra_componen_idVendor_id_1cae764b_fk_reportInf` FOREIGN KEY (`idVendor_id`) REFERENCES `reportinfra_vendor` (`idVendor`)
) ENGINE=InnoDB AUTO_INCREMENT=192 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reportinfra_componente`
--

LOCK TABLES `reportinfra_componente` WRITE;
/*!40000 ALTER TABLE `reportinfra_componente` DISABLE KEYS */;
INSERT INTO `reportinfra_componente` VALUES (1,'FW',11),(2,'BIOS',11),(3,'iDRAC',11),(4,'iLO',11),(5,'Drivers',11),(6,'iBMC',11),(7,'CIMC',11),(8,'iOS',11),(9,'FW',12),(10,'BIOS',12),(11,'iDRAC',12),(12,'iLO',12),(13,'Drivers',12),(14,'iBMC',12),(15,'CIMC',12),(16,'iOS',12),(17,'FW',13),(18,'BIOS',13),(19,'iDRAC',13),(20,'iLO',13),(21,'Drivers',13),(22,'iBMC',13),(23,'CIMC',13),(24,'iOS',13),(25,'FW',14),(26,'BIOS',14),(27,'iDRAC',14),(28,'iLO',14),(29,'Drivers',14),(30,'iBMC',14),(31,'CIMC',14),(32,'iOS',14),(33,'FW',15),(34,'BIOS',15),(35,'iDRAC',15),(36,'iLO',15),(37,'Drivers',15),(38,'iBMC',15),(39,'CIMC',15),(40,'iOS',15),(41,'Disk',1),(42,'Flash Disk',1),(43,'Smart Array Battery',1),(44,'Flex Fabric',1),(45,'DIMM',1),(46,'CPU',1),(47,'Micro SD',1),(48,'Usb Controller',1),(49,'Network Adapter',1),(50,'Motherboard',1),(51,'Satadom',1),(52,'Switches',1),(53,'Backplane',1),(54,'Cables SAS',1),(55,'Full node',1),(56,'Power Supply',1),(57,'IO Module',1),(58,'Chassis',1),(59,'Transceiver',1),(60,'Server',1),(61,'Cabling',1),(62,'Cabinet/Rack',1),(63,'Fan',1),(64,'Disk',2),(65,'Flash Disk',2),(66,'Smart Array Battery',2),(67,'Flex Fabric',2),(68,'DIMM',2),(69,'CPU',2),(70,'Micro SD',2),(71,'Usb Controller',2),(72,'Network Adapter',2),(73,'Motherboard',2),(74,'Satadom',2),(75,'Switches',2),(76,'Backplane',2),(77,'Cables SAS',2),(78,'Full node',2),(79,'Power Supply',2),(80,'IO Module',2),(81,'Chassis',2),(82,'Transceiver',2),(83,'Server',2),(84,'Cabling',2),(85,'Cabinet/Rack',2),(86,'Fan',2),(87,'Disk',3),(88,'Flash Disk',3),(89,'Smart Array Battery',3),(90,'Flex Fabric',3),(91,'DIMM',3),(92,'CPU',3),(93,'Micro SD',3),(94,'Usb Controller',3),(95,'Network Adapter',3),(96,'Motherboard',3),(97,'Satadom',3),(98,'Switches',3),(99,'Backplane',3),(100,'Cables SAS',3),(101,'Full node',3),(102,'Power Supply',3),(103,'IO Module',3),(104,'Chassis',3),(105,'Transceiver',3),(106,'Server',3),(107,'Cabling',3),(108,'Cabinet/Rack',3),(109,'Fan',3),(110,'Disk',5),(111,'Flash Disk',5),(112,'Smart Array Battery',5),(113,'Flex Fabric',5),(114,'DIMM',5),(115,'CPU',5),(116,'Micro SD',5),(117,'Usb Controller',5),(118,'Network Adapter',5),(119,'Motherboard',5),(120,'Satadom',5),(121,'Switches',5),(122,'Backplane',5),(123,'Cables SAS',5),(124,'Full node',5),(125,'Power Supply',5),(126,'IO Module',5),(127,'Chassis',5),(128,'Transceiver',5),(129,'Server',5),(130,'Cabling',5),(131,'Cabinet/Rack',5),(132,'Fan',5),(133,'Disk',10),(134,'Flash Disk',10),(135,'Smart Array Battery',10),(136,'Flex Fabric',10),(137,'DIMM',10),(138,'CPU',10),(139,'Micro SD',10),(140,'Usb Controller',10),(141,'Network Adapter',10),(142,'Motherboard',10),(143,'Satadom',10),(144,'Switches',10),(145,'Backplane',10),(146,'Cables SAS',10),(147,'Full node',10),(148,'Power Supply',10),(149,'IO Module',10),(150,'Chassis',10),(151,'Transceiver',10),(152,'Server',10),(153,'Cabling',10),(154,'Cabinet/Rack',10),(155,'Fan',10),(156,'ESXi',4),(157,'vCenter Server',4),(158,'NSX-T',4),(159,'NSX-V',4),(160,'vSAN',4),(161,'Cloud Director',4),(162,'vRealize Orchestrator',4),(163,'vRealize Operations ',4),(164,'Tenant App',4),(165,'vRealize Log Insight ',4),(166,'vRealize Network Insight ',4),(167,'Identity Manager',4),(168,'Central Point Of Management (CPoM) ',4),(169,'vRealize Suite Lifecycle Manager ',4),(170,'SDDC Manager',4),(171,'Bitnami ',4),(172,'App Launchpad',4),(173,'Terraform Provider ',4),(174,'Harbor',4),(175,'Container Service Extension (CSE)',4),(176,'Tanzu',4),(177,'Cloud Availability (VCDA)',4),(178,'AVI Networks',4),(179,'WorskSpace One Access',4),(180,'HCX',4),(181,'RHUI',6),(182,'CDS',6),(183,'OS',6),(184,'KMS',9),(185,'Active Directory',9),(186,'SQL Server',9),(187,'DNS',9),(188,'DHCP',9),(189,'SO',9),(190,'RMT',7),(191,'SO',7);
/*!40000 ALTER TABLE `reportinfra_componente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reportinfra_reportefallas`
--

DROP TABLE IF EXISTS `reportinfra_reportefallas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportinfra_reportefallas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `SR` varchar(150) NOT NULL,
  `descripcion` longtext DEFAULT NULL,
  `Fecha` varchar(50) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL DEFAULT current_timestamp(6),
  `Ambiente_id` int(11) DEFAULT NULL,
  `CambioHW_id` int(11) DEFAULT NULL,
  `Usuario_id` int(11) NOT NULL DEFAULT 1,
  `Vendor_id` int(11) DEFAULT NULL,
  `Componente_id` int(11) DEFAULT NULL,
  `Categoria_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reportInfra_reportef_Ambiente_id_0ee6548a_fk_reportInf` (`Ambiente_id`),
  KEY `reportInfra_reportef_CambioHW_id_45a47e0b_fk_reportInf` (`CambioHW_id`),
  KEY `reportInfra_reportefallas_Usuario_id_760f1bae_fk_auth_user_id` (`Usuario_id`),
  KEY `reportInfra_reportef_Vendor_id_ade2015a_fk_reportInf` (`Vendor_id`),
  KEY `reportInfra_reportef_Componente_id_c91aab4b_fk_reportInf` (`Componente_id`),
  KEY `reportInfra_reportef_Categoria_id_d3b145e7_fk_reportInf` (`Categoria_id`),
  CONSTRAINT `reportInfra_reportef_Ambiente_id_0ee6548a_fk_reportInf` FOREIGN KEY (`Ambiente_id`) REFERENCES `reportinfra_ambiente` (`idAmbiente`),
  CONSTRAINT `reportInfra_reportef_CambioHW_id_45a47e0b_fk_reportInf` FOREIGN KEY (`CambioHW_id`) REFERENCES `reportinfra_cambiohw` (`idHW`),
  CONSTRAINT `reportInfra_reportef_Categoria_id_d3b145e7_fk_reportInf` FOREIGN KEY (`Categoria_id`) REFERENCES `reportinfra_categoria` (`idTipo`),
  CONSTRAINT `reportInfra_reportef_Componente_id_c91aab4b_fk_reportInf` FOREIGN KEY (`Componente_id`) REFERENCES `reportinfra_componente` (`idComponente`),
  CONSTRAINT `reportInfra_reportef_Vendor_id_ade2015a_fk_reportInf` FOREIGN KEY (`Vendor_id`) REFERENCES `reportinfra_vendor` (`idVendor`),
  CONSTRAINT `reportInfra_reportefallas_Usuario_id_760f1bae_fk_auth_user_id` FOREIGN KEY (`Usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reportinfra_reportefallas`
--

LOCK TABLES `reportinfra_reportefallas` WRITE;
/*!40000 ALTER TABLE `reportinfra_reportefallas` DISABLE KEYS */;
INSERT INTO `reportinfra_reportefallas` VALUES (1,'125514376 ','ESXi usdfw01m-esx04 - Servidor no arranca, se quedaba ciclado. ','26/10/2021','2022-02-23 14:47:32.434636',1,2,2,2,2,NULL),(2,'21252103208','6 VMs presentan problemas a nivel aplicativo, a nivel vmware con el siguiente mensaje: The vmware the virtual machine\'s guest operating system has crashed.','30/08/2021','2022-02-23 14:47:32.435797',2,2,3,1,2,NULL),(3,'v950440 ','Se presentan fallas en el host ESXSRVE43, por lo cual se requiere actualizar a una version mas reciente. EL host se encuentra trabajando ahora de forma normal','17/08/2021','2022-02-23 14:47:32.436807',2,1,3,2,2,NULL),(4,'21246578508','Error al cargar el portal de Tenant App y usar la API, se obtiene el siguiente error Failed to get license status','09/08/2021','2022-02-23 14:47:32.531001',3,2,4,1,2,NULL),(5,'692141034','Error de equipo mcp-pp01-cl08-esx003, se quedo pasmado y fabricante determina daño en motherboard, se realiza cambio de la misma','09/10/2021','2022-02-23 14:47:32.531288',4,1,3,3,2,NULL),(6,'21253775409','Latencia en algunas VM, una de ellas un controlador de NSX que provocó desconexión temporal de los host','02/09/2021','2022-02-23 14:47:32.531491',3,2,4,1,2,NULL),(7,'21255850909','Resolución de vulnerabilidad CVE-2021-22021 en VMware vRealize Log Insight versión 4.8.0','09/09/2021','2022-02-23 14:47:32.531667',3,2,4,1,2,NULL),(8,'21256644709','En el vCenter Server No es posible iniciar el servicio VMware vSphere Profile-Driven Storage','13/09/2021','2022-02-23 14:47:32.531837',4,2,4,1,2,NULL),(9,'21258189509','No es posible configurar el Lookup Service en vCAV on premises 3.5.2','17/09/2021','2022-02-23 14:47:32.531995',4,2,4,1,2,NULL),(10,'21258939209','Error al tratar de conectar vCenter 6.0 con vCAV. 3.5.2 ','21/09/2021','2022-02-23 14:47:32.532150',4,2,4,1,2,NULL),(11,'21259049009','The vCenter lookup service appears to have a registration for an older vCenter that no longer exists','21/09/2021','2022-02-23 14:47:32.532304',4,2,4,1,2,NULL),(12,'21262207409','Se requiere actualizar vcloud director y los componentes que forman parte de la solución','04/10/2021','2022-02-23 14:47:32.532458',3,2,5,1,2,NULL),(13,'21255005709','Esxi host not responding, se revisó via consola y no responde (anexo pantalla). vSphere HA detected a possible host failure of this host error 9/7/2021 9:11:23 PM mcp-pp01-cl08-esx003.cloudtelmex.local','09/08/2021','2022-02-23 14:47:32.532613',4,2,5,1,2,NULL),(14,'5358558963','Reemplazo Hardware equipos OACI','14/09/2021','2022-02-23 14:47:32.532824',4,1,5,4,2,NULL),(15,'5358558777','Reemplazo Hardware equipos OACI','14/09/2021','2022-02-23 14:47:32.533060',4,1,5,4,2,NULL),(16,'125514376','Revisión servidor PSOD y no arranca el SO, se cicla en la carga de memoria, bios y dispositivos PCI','26/10/2021','2022-02-23 14:47:32.533227',1,2,4,2,2,NULL),(17,'125638917','ESXi usmia01m-esx06 - The memory health monitor feature has detected a degradation in the DIMM installed in DIMM_B5.','27/10/2021','2022-02-23 14:47:32.533382',1,2,2,2,2,NULL),(18,'16759274','Disco de capacidad de VSAN dañado','13/10/2021','2022-02-23 14:47:32.533537',4,1,4,5,2,NULL),(19,'21270536410','Validacion compatibilidad de Tenant App 8.6','27/10/2021','2022-02-23 14:47:32.533687',3,2,4,1,2,NULL),(20,'16893818','IT | Hardware validation after unexpected restart ','05/11/2021','2022-02-23 14:47:32.533857',4,2,6,5,2,NULL),(21,'5360179281','Error array smart servidor HP mcp-pp01-cl24-esx015','19/11/2021','2022-02-23 14:47:32.534019',4,2,7,4,2,NULL),(22,'5360160940','Error tarjeta de red servidor HP mcp-pp01-cl23-esx-002','17/11/2021','2022-02-23 14:47:32.534172',4,2,7,4,2,NULL),(23,'1075381229','Alarmas por saturacion de almacenamiento en switches ARBUE01-SWMGT-01,02,03,04,05,06 de AMX Argentina (SYS_STAT_LOW_DISK_SPACE: Warning! Configuration directory has 25.0%% free. Please delete unnecessary files from home directory)','11/11/2021','2022-02-23 14:47:32.534342',5,2,8,2,2,NULL),(24,'1076278953','Alarmas de desconexion PSU Switches Dell AMX Argentina (%EQM_PSU_OFF: Power supply unit power off or removed PSU 1, %EQM_FANTRAY_NOT_PRESENT: Fan tray absent fantray 4 is not present)','19/11/2021','2022-02-23 14:47:32.534503',5,2,8,2,2,NULL),(25,'21278998911','Validarción de mitigación de vulnerabilidades','18/11/2021','2022-02-23 14:47:32.534658',4,2,4,1,2,NULL),(26,'21280963411','Problema de replicación con vCAV onpremises','23/11/2021','2022-02-23 14:47:32.534812',4,2,4,1,2,NULL),(27,'2127951061','Error \"cpu12:40373347)WARNING: LinuxThread: 424: python: Error cloning thread: -28 (bad0081)\"','18/11/2021','2022-02-23 14:47:32.534977',5,3,7,1,2,NULL),(28,'21276485911','NSX-V Edge DNS not resolving','09/11/2021','2022-02-23 14:47:32.535159',3,3,9,1,2,NULL),(29,'17043918','Upgrade to latest vimware version. Huawei 2288H V5','01/12/2021','2022-02-23 14:47:32.535353',3,3,10,5,2,NULL),(30,'17068596','El host mxap-npvtp16.cloudmty.local is DOWN! ','12/06/2021','2022-02-23 14:47:32.535524',3,1,11,5,2,NULL),(31,'5360576273','Falla en NIC Network Adapter Link Down (Slot 1, Port 1) (Slot 1, Port 2)','12/06/2021','2022-02-23 14:47:32.535713',4,1,11,4,2,NULL),(32,'5360668903','Falla en Power Supply en servidor mcp-pp01-cl20-esx002','12/09/2021','2022-02-23 14:47:32.535884',4,1,11,4,2,NULL),(33,'21283879912','Error en Work Flow \"Creación nueva IP Publica\"','12/03/2021','2022-02-23 14:47:32.536083',5,2,12,1,2,NULL),(34,'5360697064','Falla en NIC Network Adapter Link Down (Slot 1, Port 1) (Slot 1, Port 2)','10/12/2021','2022-02-23 14:47:32.536264',4,2,11,4,2,NULL),(35,'21285682912','Alarma: Error al descargar el complemento. Asegúrese de que pueda accederse a la URL y que la huella digital registrada sea correcta. java.io.IOException: Server returned HTTP response code: 401 for URL: https://ARBUE01M-VCS001.arg.clarocloud.info:443/ui/plugins/h4va.zip ','10/12/2021','2022-02-23 14:47:32.536462',5,2,8,1,2,NULL),(36,'21288337012','error: AFFINITY_RULE_CREATE','17/12/2021','2022-02-23 14:47:32.536663',1,2,3,1,2,NULL),(37,'21290519312','Alto consumo de memoria ram en cluster de vRealize LogInsight NPE','23/12/2021','2022-02-23 14:47:32.536856',3,2,8,1,2,NULL),(38,'21291134312','No se pudo realizar la operación porque el objeto se encuentra en un estado no válido. La tarea vCenter Server (moref: task-597633) ha fallado en vCenter Server \'MXAP-NPV-VCSR01.cloudmty.local\'','28/12/2021','2022-02-23 14:47:32.537037',3,2,6,1,2,NULL),(39,'22291887301','Adapter instance has no data receiving status: ADAPTER_INSTANCE = ADAPTER_INSTANCE','01/04/2022','2022-02-23 14:47:32.537236',1,2,6,1,2,NULL),(40,'v979485 ','S3, Bursatec, S.A. de C.V., DIMM DIMM_R1 on','01/04/2022','2022-02-23 14:47:32.537417',6,1,6,3,2,NULL),(41,'21291502312','NSX Manager','30/12/2021','2022-02-23 14:47:32.537614',3,2,7,1,2,NULL),(42,'5361210187','Fallo Disco Duro mcp-pp01-cl24-esx006','01/06/2022','2022-02-23 14:47:32.537792',4,1,7,4,2,NULL),(43,'v980191','S3, Bursatec, S.A. de C.V., DIMM DIMM_B1 y B2','01/09/2022','2022-02-23 14:47:32.537986',6,2,7,3,2,NULL),(44,'17190108','mcp-pp01-cl25-esx003 - Fallo de host estatus \"Not responding\", error de disco bootbank','29/12/2021','2022-02-23 14:47:32.538164',4,2,8,5,2,NULL),(45,'692810763','Falla de host estatus de server \"Not responding\" con las siguientes alertas: fc VIF 2152 on server 1 / 2 of switch B down, reason: None, ether VIF 10004 on server 1 / 2 of switch B down, reason: Error disabled','01/02/2022','2022-02-23 14:47:32.538365',4,2,8,3,2,NULL),(46,'22295902701','Consulta para la renovacion de certificados vCloud Director 9.7 NPE','17/01/2022','2022-02-23 14:47:32.538547',3,2,8,1,2,NULL),(47,'1080717754','Link Down en NIC 1 Puerto 1','05/01/2021','2022-02-23 14:47:32.538795',1,3,11,2,2,NULL),(48,'1080720898','Link Down en NIC 1 Puerto 2','05/01/2021','2022-02-23 14:47:32.538977',1,3,11,2,2,NULL),(49,'1080725620','Link Down en NIC 1 Puerto 2','05/01/2021','2022-02-23 14:47:32.539166',1,3,11,2,2,NULL),(50,'1081335416','Link Down en NIC 2 Puerto 1','11/01/2022','2022-02-23 14:47:32.539341',1,1,11,2,2,NULL),(51,'1081338470','Link Down en NIC 1 Puerto 1','11/01/2022','2022-02-23 14:47:32.539534',1,2,11,2,2,NULL),(52,'22298724401','Falla deploy de celda vCloud Director en STG NPE','25/01/2022','2022-02-23 14:47:32.539711',3,2,5,1,2,NULL),(53,'639884618','Cambio de Fabric Interconnect','16/01/2022','2022-02-23 14:47:32.539908',4,1,11,3,2,NULL),(54,'22826595','Solicitud de vinculacion de cuenta con ID de AMX','26/01/2022','2022-02-23 14:47:32.540090',7,2,7,2,2,NULL),(55,'639885088','Cambio de IO Module','18/01/2022','2022-02-23 14:47:32.540285',4,1,11,3,1,NULL),(56,'17261221','Cambio de HDD por fallo y freeze de host mcp-pp01-cl25-esx026','13/01/2022','2022-02-23 14:47:32.540461',4,1,11,5,2,NULL),(57,'v982091','Fuente de poder alertada','22/01/2022','2022-02-23 14:47:32.540644',4,1,11,2,1,NULL),(58,'1081190039','Cerrado, Problemas en memoria de los equipos ARBUE01P-ESX05 y ARBUE01P-ESX09. Se resolvió con un reinicio de ambos equipos','07/01/2022','2022-02-23 14:47:32.540838',5,2,13,2,2,NULL),(59,'1081190553','Cerrado, se realizó el cambio de Disco en el equipo ARBUE01P-ESX37','01/07/2022','2022-02-23 14:47:32.541019',5,1,13,2,2,NULL),(60,'5361608550','Cerrado, Se detectarón problemas de red en el equipo: mcp-pp01-cl21-esx009, se resolvió con un reinicío del equipo','24/01/2022','2022-02-23 14:47:32.541202',4,2,13,4,2,NULL),(61,'1083007408','USMIA01P-ESX03 - Problem with memory in slot DIMM Socket B3 - Falla en la memoria ','27/01/2022','2022-02-23 14:47:32.541363',1,2,2,2,2,NULL),(62,'22299859401','mxap-npvtp11 - Virtual ethernet card Network adapter 1 is not supported. - Falla al hacer vMotion o Modo mtto (no funcionaba la migracion)','28/01/2022','2022-02-23 14:47:32.541547',3,2,2,1,2,NULL),(63,'22292946101','Revisión falla migración y replicación VCDA AMX','01/06/2022','2022-02-23 14:47:32.541707',1,2,12,1,2,NULL),(64,'22298606501','Fallo en sincronización de templates suscrito a un catalógo.','25/01/2022','2022-02-23 14:47:32.541889',1,2,4,1,2,NULL),(65,'22299780601','No levanta el contenedor tenant-app-ui en Tenant App ','28/01/2022','2022-02-23 14:47:32.542084',3,2,4,1,2,NULL),(66,'3128782','Disable vulnerable ciphers RHUI','19/01/2022','2022-02-23 14:47:32.542244',3,2,4,6,2,NULL),(67,'22300440702','Como deshabilitar la sincronización de la base de datos al nodo secundario para realizar el upgrade de vrealize orchestrator from 7.5 to 7.6','30/01/2022','2022-02-23 14:47:32.542427',3,2,5,1,2,NULL),(68,'1083422311','CPU2 Temp: Temperature is above critical threshold: >75','02/02/2022','2022-02-23 14:47:32.542589',8,2,3,2,2,NULL),(69,'22301455702','error: AFFINITY_RULE_CREATE','03/02/2022','2022-02-23 14:47:32.542772',1,2,3,1,2,NULL),(70,'22294783101','No se elimina Organización en VCD','12/01/2022','2022-02-23 14:47:32.542927',1,2,12,1,2,NULL),(71,'5361820403','Fallo Disco Duro mcp-pp01-cl24-esx002 (en proceso)','09/02/2022','2022-02-23 14:47:32.543115',4,1,3,4,2,NULL),(72,'134614945','Falla de equipo despues de un renicio, el equipo no entra a S.O. se queda en pantalla de arranque: MXAP-NPVTP24, MXAP-NPVTP54, MXAP-NPVTP55, MXAP-NPVTP59, MXAP-NPVTP27','13/02/2022','2022-02-23 14:47:32.543269',3,3,3,2,2,NULL),(73,'Test Manuel','test','23/02/2022','2022-03-02 01:37:24.024314',17,1,11,3,1,2),(74,'Test','TEst\r\n1518522','15/02/2022','2022-03-02 17:09:34.048517',16,2,11,6,181,3),(75,'1086223591','Link down / BR-LP-SP-LEAF-ZV07B\r\nNSX-T Management service has failed / critical / liagent / ManagementService / Application / Configuration','04/03/2022','2022-03-07 17:20:45.044467',10,3,11,1,52,2);
/*!40000 ALTER TABLE `reportinfra_reportefallas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reportinfra_vendor`
--

DROP TABLE IF EXISTS `reportinfra_vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportinfra_vendor` (
  `idVendor` int(11) NOT NULL AUTO_INCREMENT,
  `NombreVendor` varchar(100) NOT NULL,
  `idCategoria_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`idVendor`),
  KEY `reportInfra_vendor_idCategoria_id_81764085_fk_reportInf` (`idCategoria_id`),
  CONSTRAINT `reportInfra_vendor_idCategoria_id_81764085_fk_reportInf` FOREIGN KEY (`idCategoria_id`) REFERENCES `reportinfra_categoria` (`idTipo`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reportinfra_vendor`
--

LOCK TABLES `reportinfra_vendor` WRITE;
/*!40000 ALTER TABLE `reportinfra_vendor` DISABLE KEYS */;
INSERT INTO `reportinfra_vendor` VALUES (1,'Dell',2),(2,'HPE',2),(3,'Cisco',2),(4,'VMware',3),(5,'Huawei',2),(6,'RedHat',3),(7,'SuSE',3),(9,'Microsoft',3),(10,'Lenovo',2),(11,'Cisco',3),(12,'Dell',3),(13,'Huawei',3),(14,'HPE',3),(15,'Lenovo',3);
/*!40000 ALTER TABLE `reportinfra_vendor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'triara'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-09 17:05:15
