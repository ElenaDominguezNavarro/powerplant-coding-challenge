CREATE DATABASE IF NOT EXISTS error_logs;

CREATE TABLE IF NOT EXISTS `tb_error_logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `timestamp` timestamp NOT NULL,
  `error_message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci