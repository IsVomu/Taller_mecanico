-- =====================================================
-- Respaldo de Base de Datos - Taller Mecánico San José
-- INACAP - Hito 3
-- =====================================================

CREATE DATABASE IF NOT EXISTS bd_taller_mecanico;
USE bd_taller_mecanico;

-- -----------------------------------------------------
-- Tabla Padre: Tipo de Repuesto
-- -----------------------------------------------------
CREATE TABLE `apps_tiporepuesto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- -----------------------------------------------------
-- Tabla Hijo: Repuesto (Con Relación 1:N)
-- -----------------------------------------------------
CREATE TABLE `apps_repuesto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `disponible` tinyint(1) NOT NULL,
  `categoria_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `apps_repuesto_categoria_id_660ea7d6_fk_apps_tiporepuesto_id` (`categoria_id`),
  CONSTRAINT `apps_repuesto_categoria_id_660ea7d6_fk_apps_tiporepuesto_id` 
    FOREIGN KEY (`categoria_id`) REFERENCES `apps_tiporepuesto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;