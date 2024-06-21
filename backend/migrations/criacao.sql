-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema public
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema public
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `public` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `public` ;

-- -----------------------------------------------------
-- Table `public`.`curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `public`.`curso` (
  `id` VARCHAR(36) NOT NULL,
  `nome_curso` VARCHAR(50) NOT NULL,
  `descricao` TEXT NULL DEFAULT NULL,
  `duracao` INT NULL DEFAULT NULL,
  `curso_relacionado` VARCHAR(150) NULL DEFAULT NULL,
  `status_curso` CHAR(30) NULL DEFAULT NULL,
  `quantidade_max_alunos` INT NULL DEFAULT NULL,
  `data_inclusao` DATETIME(6) NULL DEFAULT NULL,
  `data_modificacao` DATETIME(6) NULL DEFAULT NULL,
  `professor_ra` VARCHAR(8) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `public`.`aulas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `public`.`aulas` (
  `id` VARCHAR(36) NOT NULL,
  `nome_aula` VARCHAR(100) NOT NULL,
  `descricao_aula` TEXT NULL DEFAULT NULL,
  `conteudo_aula` TEXT NULL DEFAULT NULL,
  `duracao_aula` INT NOT NULL,
  `id_curso` VARCHAR(36) NOT NULL,
  `data_inclusao` DATETIME(6) NULL DEFAULT NULL,
  `data_modificacao` DATETIME(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_curso` (`id_curso` ASC) VISIBLE,
  CONSTRAINT `aulas_ibfk_1`
    FOREIGN KEY (`id_curso`)
    REFERENCES `public`.`curso` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `public`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `public`.`usuarios` (
  `ra` VARCHAR(20) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(100) NOT NULL,
  `tipoAcesso` VARCHAR(20) NOT NULL,
  `dataNascimento` DATE NOT NULL,
  `sexo` CHAR(1) NOT NULL,
  `data_inclusao` DATETIME(6) NULL DEFAULT NULL,
  `data_modificacao` DATETIME(6) NULL DEFAULT NULL,
  PRIMARY KEY (`ra`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `public`.`faltas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `public`.`faltas` (
  `id` VARCHAR(36) NOT NULL,
  `id_aula` VARCHAR(36) NOT NULL,
  `usuario_ra` VARCHAR(8) NOT NULL,
  `data_falta` DATE NOT NULL,
  `justificada` TINYINT(1) NOT NULL DEFAULT '0',
  `data_inclusao` DATETIME(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_faltas_aula` (`id_aula` ASC) VISIBLE,
  INDEX `fk_faltas_usuario` (`usuario_ra` ASC) VISIBLE,
  CONSTRAINT `fk_faltas_aula`
    FOREIGN KEY (`id_aula`)
    REFERENCES `public`.`aulas` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_faltas_usuario`
    FOREIGN KEY (`usuario_ra`)
    REFERENCES `public`.`usuarios` (`ra`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `public`.`notas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `public`.`notas` (
  `id` VARCHAR(36) NOT NULL,
  `curso_id` VARCHAR(36) NOT NULL,
  `usuario_ra` VARCHAR(8) NOT NULL,
  `nota` DECIMAL(5,2) NULL DEFAULT NULL,
  `data_lancamento` DATE NULL DEFAULT NULL,
  `data_inclusao` DATETIME(6) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_notas_curso` (`curso_id` ASC) VISIBLE,
  INDEX `fk_notas_usuario` (`usuario_ra` ASC) VISIBLE,
  CONSTRAINT `fk_notas_curso`
    FOREIGN KEY (`curso_id`)
    REFERENCES `public`.`curso` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_notas_usuario`
    FOREIGN KEY (`usuario_ra`)
    REFERENCES `public`.`usuarios` (`ra`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `public`.`usuarios_curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `public`.`usuarios_curso` (
  `curso_id` VARCHAR(36) NOT NULL,
  `usuario_ra` VARCHAR(8) NOT NULL,
  `data_inclusao` DATETIME(6) NULL DEFAULT NULL,
  PRIMARY KEY (`curso_id`, `usuario_ra`),
  INDEX `usuario_ra` (`usuario_ra` ASC) VISIBLE,
  CONSTRAINT `usuarios_curso_ibfk_1`
    FOREIGN KEY (`curso_id`)
    REFERENCES `public`.`curso` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `usuarios_curso_ibfk_2`
    FOREIGN KEY (`usuario_ra`)
    REFERENCES `public`.`usuarios` (`ra`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
