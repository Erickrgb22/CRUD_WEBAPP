USE backend;
CREATE TABLE `v27225952` (
  `ID` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `CEDULA` int(32) NOT NULL,
  `APELLIDO` varchar(255) NOT NULL,
  `NOMBRE` varchar(255) NOT NULL,
  `EMAIL` varchar(255) NOT NULL,
  `CURSO` varchar(255) NOT NULL,
  `SECCION` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;
