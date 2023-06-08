-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: desafio7
-- ------------------------------------------------------
-- Server version	8.0.32

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


CREATE DATABASE desafio7;
USE desafio7;

--
-- Table structure for table `articulo`
--

DROP TABLE IF EXISTS `articulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `articulo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `titulo` varchar(100) DEFAULT NULL,
  `resumen` varchar(255) DEFAULT NULL,
  `contenido` text,
  `fecha_publicacion` date DEFAULT (curdate()),
  `estado` tinyint(1) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `articulo_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `categoria_articulo`
--

DROP TABLE IF EXISTS `categoria_articulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria_articulo` (
  `id_articulo` int NOT NULL,
  `id_categoria` int NOT NULL,
  KEY `id_articulo` (`id_articulo`),
  KEY `id_categoria` (`id_categoria`),
  CONSTRAINT `categoria_articulo_ibfk_1` FOREIGN KEY (`id_articulo`) REFERENCES `articulo` (`id`),
  CONSTRAINT `categoria_articulo_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `comentario`
--

DROP TABLE IF EXISTS `comentario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comentario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_articulo` int NOT NULL,
  `id_usuario` int NOT NULL,
  `contenido` text,
  `fecha_hora` datetime DEFAULT (now()),
  `estado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_articulo` (`id_articulo`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `comentario_ibfk_1` FOREIGN KEY (`id_articulo`) REFERENCES `articulo` (`id`),
  CONSTRAINT `comentario_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `contrasenia` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT (false),
  `fecha_creacion` datetime NOT NULL DEFAULT (now()),
  `avatar` varchar(255) DEFAULT NULL,
  `es_publico` tinyint(1) NOT NULL DEFAULT (false),
  `es_colaborador` tinyint(1) NOT NULL DEFAULT (false),
  `es_admin` tinyint(1) NOT NULL DEFAULT (false),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-04 21:35:30


--
-- consultas
--

--
-- Agregar el comando necesario que introduzca en la tabla usuario, 1 usuario con rol de admin, 4 con rol de colaborador y 5 con rol de público
--
INSERT INTO usuario
(
nombre,
apellido,
telefono,
username,
email,
contrasenia,
es_publico,
es_colaborador,
es_admin)
VALUES
("lionel", "messi", "123456789", "lionelmessi", "lionel@messi", "lionelmessi", false, false, true),
("joel", "chavez","123456789", "joelchavez", "joel@chavez", "joelchavez", false, true, false),
("cristiano", "ronaldo", "123456789", "cristianoronaldo", "cristiano@ronaldo", "cristianoronaldo", false, true, false),
("neymar", "jr", "123456789", "neymarjr", "neymar@jr", "neymarjr", false, true, false),
("kylian", "mbappe", "123456789", "kylianmbappe", "kylian@mbappe", "kylianmbappe", false, true, false),
("paulo", "dybala", "123456789", "pauldybala", "paulo@dybala", "pauldybala", true, false, false),
("angel", "di maria", "123456789", "angoldimaria", "angel@di maria", "angoldimaria", true, false, false),
("jordi", "alba", "123456789", "jordialba", "jordi@alba", "jordialba", true, false, false),
("rodrigo", "de paul", "123456789", "rodpaul", "rodrigo@de_paul", "rodpaul", true, false, false),
("diego", "mradona", "123456789", "dgmradona", "diego@mradona", "dgmradona", true, false, false),
("lukita", "modric", "123456789", "lukimodric", "lukita@modric", "lukimodric", true, false, false);

--
-- Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios agregado con rol de colaborador.
--
UPDATE usuario SET es_colaborador=false, es_admin=true WHERE es_colaborador=true LIMIT 1;

--
-- Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con estado TRUE y uno con estado FALSE.
--
INSERT INTO articulo
(
id_usuario,
titulo,
resumen,
contenido,
estado
)
VALUES
(12, "articulo 1", "resumen 1", "contenido 1", true),
(13, "articulo 2", "resumen 2", "contenido 2", true),
(14, "articulo 3", "resumen 3", "contenido 3", true),
(15, "articulo 4", "resumen 4", "contenido 4", false);

--
-- Agregar el comando necesario para eliminar el artículo que tenga estado FALSE.
--
DELETE FROM articulo WHERE estado=false;

--
-- Agregar el comando necesario que introduzca 3 comentarios al primer artículo agregado y 2 comentarios al segundo artículo.
--
INSERT INTO comentario
(
id_articulo,
id_usuario,
contenido
)
VALUES
(5, 12, "comentario 1"),
(5, 13, "comentario 2"),
(5, 14, "comentario 2"),
(6, 15, "comentario 2"),
(6, 15, "comentario 2");

--
-- Agregar el comando necesario para listar todos los artículos que tengan comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho comentario, agrupados por artículos.
--
SELECT articulo.titulo, articulo.fecha_publicacion, usuario.nombre, comentario.fecha_hora
FROM articulo
INNER JOIN usuario ON articulo.id_usuario=usuario.id
INNER JOIN comentario ON articulo.id=comentario.id_articulo;

# integrantes
# Pablo, Acevedo
# Matías Gastón, Serial Trachta
# Lugo Mauro, Rodrigo
# Julio R, Escanciano Gonzalez
# Facundo, Vicedo
# Gabriel, Leiva
# Joel, Chavez
# Maximiliano Imanol, Aguer
# Cristian J, Salto
# Fabricio, Herrera