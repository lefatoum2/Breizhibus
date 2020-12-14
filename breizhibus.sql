-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 14, 2020 at 09:42 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `breizhibus`
--

-- --------------------------------------------------------

--
-- Table structure for table `arrets`
--

CREATE TABLE `arrets` (
  `ID_ARRET` int(11) NOT NULL,
  `NOM` varchar(20) NOT NULL,
  `ADRESSE` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets`
--

INSERT INTO `arrets` (`ID_ARRET`, `NOM`, `ADRESSE`) VALUES
(1, 'kORRIGAN', '1 IMPASSE DU KORRIGAN'),
(2, 'MORGANA', '2 PLACE MORGANA'),
(3, 'L\'ANKOU', '3 PLACE DE LA MORGUE'),
(4, 'YS', '4 RUE DE L\'ILE D\'YS'),
(5, 'VIVIANE', '5 AVENUE DE VIVIANE'),
(6, 'GUENOLE', '6 RUE SAINT GUENOLE');

-- --------------------------------------------------------

--
-- Table structure for table `arrets_lignes`
--

CREATE TABLE `arrets_lignes` (
  `ID_LIGNE` int(11) NOT NULL,
  `ID_ARRET` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets_lignes`
--

INSERT INTO `arrets_lignes` (`ID_LIGNE`, `ID_ARRET`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 2),
(2, 4),
(2, 6),
(3, 4),
(3, 5),
(3, 6),
(3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

CREATE TABLE `bus` (
  `ID_BUS` int(11) NOT NULL,
  `NUMERO` varchar(4) NOT NULL,
  `IMMATRICULATION` varchar(7) NOT NULL,
  `NOMBRE_PLACE` int(11) NOT NULL,
  `ID_LIGNE` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`ID_BUS`, `NUMERO`, `IMMATRICULATION`, `NOMBRE_PLACE`, `ID_LIGNE`) VALUES
(1, 'BB01', 'CA123DO', 20, 1),
(2, 'BB02', 'NO123EL', 30, 2),
(3, 'BB03', 'JE123UX', 20, 3),
(4, 'BB04', 'RE123PA', 30, 1),
(7, '464', 'BB5646', 23, 3),
(8, 'B789', 'PJHG6', 25, 2);

-- --------------------------------------------------------

--
-- Table structure for table `lignes`
--

CREATE TABLE `lignes` (
  `ID_LIGNE` int(11) NOT NULL,
  `NOM` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lignes`
--

INSERT INTO `lignes` (`ID_LIGNE`, `NOM`) VALUES
(1, 'ROUGE'),
(2, 'VERT'),
(3, 'BLEU');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arrets`
--
ALTER TABLE `arrets`
  ADD PRIMARY KEY (`ID_ARRET`);

--
-- Indexes for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD KEY `ID_ARRET` (`ID_ARRET`),
  ADD KEY `ID_LIGNE` (`ID_LIGNE`);

--
-- Indexes for table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`ID_BUS`),
  ADD KEY `ID_LIGNE` (`ID_LIGNE`);

--
-- Indexes for table `lignes`
--
ALTER TABLE `lignes`
  ADD PRIMARY KEY (`ID_LIGNE`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arrets`
--
ALTER TABLE `arrets`
  MODIFY `ID_ARRET` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `bus`
--
ALTER TABLE `bus`
  MODIFY `ID_BUS` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `lignes`
--
ALTER TABLE `lignes`
  MODIFY `ID_LIGNE` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD CONSTRAINT `arrets_lignes_ibfk_1` FOREIGN KEY (`ID_ARRET`) REFERENCES `arrets` (`ID_ARRET`),
  ADD CONSTRAINT `arrets_lignes_ibfk_2` FOREIGN KEY (`ID_LIGNE`) REFERENCES `lignes` (`ID_LIGNE`);

--
-- Constraints for table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `bus_ibfk_1` FOREIGN KEY (`ID_LIGNE`) REFERENCES `lignes` (`ID_LIGNE`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
