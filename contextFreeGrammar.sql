-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 02, 2018 at 12:59 AM
-- Server version: 5.7.20-0ubuntu0.17.04.1
-- PHP Version: 7.0.22-0ubuntu0.17.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `contextFreeGrammar`
--

-- --------------------------------------------------------

--
-- Table structure for table `Adjective`
--

CREATE TABLE `Adjective` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `frequency` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Adjective`
--

INSERT INTO `Adjective` (`id`, `word`, `frequency`) VALUES
(1, 'sad', 15),
(2, 'happy', 15),
(3, 'glum', 5),
(4, 'suspicious', 9),
(5, 'red', 20),
(6, 'evil', 12),
(7, 'ferocious', 13),
(8, 'blue', 15),
(9, 'slow', 13),
(10, 'fast', 9);

-- --------------------------------------------------------

--
-- Table structure for table `Adverb`
--

CREATE TABLE `Adverb` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `frequency` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Adverb`
--

INSERT INTO `Adverb` (`id`, `word`, `frequency`) VALUES
(1, 'nearly', 9),
(2, 'happily', 11),
(3, 'endlessly', 11),
(4, 'quickly', 9),
(5, 'cheerfully', 15),
(6, 'truthfully', 15),
(7, 'there', 11);

-- --------------------------------------------------------

--
-- Table structure for table `Articles`
--

CREATE TABLE `Articles` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `type` varchar(25) DEFAULT NULL,
  `frequency` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Articles`
--

INSERT INTO `Articles` (`id`, `word`, `type`, `frequency`) VALUES
(1, 'the', 'definite', 103),
(2, 'a', 'indefinite', 131),
(3, 'an', 'indefinite', 124);

-- --------------------------------------------------------

--
-- Table structure for table `Conjunction`
--

CREATE TABLE `Conjunction` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `frequency` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Conjunction`
--

INSERT INTO `Conjunction` (`id`, `word`, `frequency`) VALUES
(1, 'and', 25),
(2, 'but', 28),
(3, 'or', 22);

-- --------------------------------------------------------

--
-- Table structure for table `Exclamation`
--

CREATE TABLE `Exclamation` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `frequency` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Exclamation`
--

INSERT INTO `Exclamation` (`id`, `word`, `frequency`) VALUES
(1, 'ouch', 125),
(2, 'yikes', 123),
(3, 'thank goodness', 117),
(4, 'oh crap', 99),
(5, 'boom', 120),
(6, 'c-c-c-combo breaker', 116),
(7, 'yay', 107);

-- --------------------------------------------------------

--
-- Table structure for table `Nouns`
--

CREATE TABLE `Nouns` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `frequency` int(11) NOT NULL,
  `isPlural` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Nouns`
--

INSERT INTO `Nouns` (`id`, `word`, `type`, `frequency`, `isPlural`) VALUES
(1, 'girl', 'person', 10, 'no'),
(2, 'school', 'place', 12, 'no'),
(3, 'dude', 'person', 10, 'no'),
(4, 'vest', 'thing', 17, 'no'),
(5, 'octopus', 'thing', 7, 'yes'),
(6, 'pencil', 'thing', 12, 'no'),
(7, 'hour', 'idea', 0, 'no'),
(8, 'century', 'idea', 0, 'no'),
(9, 'mile', 'idea', 0, 'no'),
(10, 'light-year', 'idea', 0, 'no'),
(11, 'home', 'place', 9, 'no'),
(12, 'classroom', 'place', 19, 'no'),
(13, 'bedroom', 'place', 9, 'no'),
(14, 'teeth', 'thing', 8, 'yes'),
(15, 'boxes', 'thing', 12, 'yes'),
(16, 'stores', 'place', 4, 'yes'),
(17, 'women', 'person', 8, 'yes'),
(18, 'theories', 'idea', 0, 'yes'),
(19, 'apocalypse', 'thing', 10, 'no'),
(20, 'golf', 'idea', 0, 'no');

-- --------------------------------------------------------

--
-- Table structure for table `OpeningPhrases`
--

CREATE TABLE `OpeningPhrases` (
  `id` int(11) NOT NULL,
  `phrase` varchar(500) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `tense` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `OpeningPhrases`
--

INSERT INTO `OpeningPhrases` (`id`, `phrase`, `frequency`, `tense`) VALUES
(1, 'a long time ago in a galaxy far, far away...', 44, 'past'),
(2, 'back in my day,', 52, 'past'),
(3, 'in the beginning...', 45, 'past'),
(4, 'good morning,', 46, 'present'),
(5, 'it was a dark and stormy night...', 51, 'past'),
(6, 'it all started last friday...', 8, 'past'),
(7, 'as we speak,', 9, 'present');

-- --------------------------------------------------------

--
-- Table structure for table `Prepositions`
--

CREATE TABLE `Prepositions` (
  `id` int(11) NOT NULL,
  `word` varchar(50) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Prepositions`
--

INSERT INTO `Prepositions` (`id`, `word`, `frequency`) VALUES
(1, 'after', 13),
(2, 'with', 11),
(3, 'in', 9),
(4, 'on', 14);

-- --------------------------------------------------------

--
-- Table structure for table `Pronoun`
--

CREATE TABLE `Pronoun` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `frequency` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Pronoun`
--

INSERT INTO `Pronoun` (`id`, `word`, `type`, `frequency`) VALUES
(1, 'you', 'subjective', 0),
(2, 'mine', 'possessive', 0),
(3, 'myself', 'reflexive', 0),
(4, 'me', 'objective', 0);

-- --------------------------------------------------------

--
-- Table structure for table `ProperNouns`
--

CREATE TABLE `ProperNouns` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `frequency` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ProperNouns`
--

INSERT INTO `ProperNouns` (`id`, `word`, `type`, `frequency`) VALUES
(1, 'jeremy banks', 'person', 54),
(2, 'chuck e cheeses', 'place', 14),
(3, 'rutgers', 'place', 18),
(4, 'space dementia', 'idea', 0),
(5, 'the legend of zelda: breath of the wild', 'thing', 9),
(6, 'persona 5', 'thing', 10),
(7, 'gordan freeman', 'person', 59),
(8, 'nikloa tesla', 'person', 62),
(9, 'buffalo', 'place', 16),
(10, 'new jersey', 'place', 10),
(11, 'darth vader', 'person', 60),
(12, 'ozzy osbourne', 'person', 40),
(13, 'nolan bushnell', 'person', 21);

-- --------------------------------------------------------

--
-- Table structure for table `Verbs`
--

CREATE TABLE `Verbs` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `frequency` int(11) NOT NULL,
  `tense` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Verbs`
--

INSERT INTO `Verbs` (`id`, `word`, `type`, `frequency`, `tense`) VALUES
(1, 'jump', 'action', 3, 'present'),
(2, 'snow', 'event', 0, 'present'),
(3, 'seem', 'situation', 4, 'present'),
(4, 'evolve', 'change', 4, 'present'),
(5, 'swim', 'action', 7, 'present'),
(6, 'swam', 'action', 9, 'past'),
(7, 'ran', 'action', 17, 'past'),
(8, 'evolved', 'change', 7, 'past'),
(9, 'participated', 'action', 8, 'past'),
(10, 'has', 'situation', 3, 'present'),
(11, 'had', 'situation', 3, 'past'),
(12, 'happened', 'event', 0, 'past'),
(13, 'rained', 'event', 0, 'past'),
(14, 'hailed', 'event', 0, 'past'),
(15, 'stopped', 'action', 8, 'past'),
(16, 'explored', 'action', 6, 'past'),
(17, 'was', 'situation', 4, 'past'),
(18, 'shrink', 'change', 2, 'present'),
(19, 'grow', 'change', 0, 'present'),
(20, 'grew', 'change', 4, 'past'),
(21, 'is', 'situation', 1, 'present'),
(22, 'be', 'situation', 1, 'present'),
(23, 'yawned', 'action', 14, 'past'),
(24, 'protected', 'action', 16, 'past');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Adjective`
--
ALTER TABLE `Adjective`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Adverb`
--
ALTER TABLE `Adverb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Articles`
--
ALTER TABLE `Articles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Conjunction`
--
ALTER TABLE `Conjunction`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Exclamation`
--
ALTER TABLE `Exclamation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Nouns`
--
ALTER TABLE `Nouns`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `OpeningPhrases`
--
ALTER TABLE `OpeningPhrases`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Prepositions`
--
ALTER TABLE `Prepositions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Pronoun`
--
ALTER TABLE `Pronoun`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ProperNouns`
--
ALTER TABLE `ProperNouns`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Verbs`
--
ALTER TABLE `Verbs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Adjective`
--
ALTER TABLE `Adjective`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `Adverb`
--
ALTER TABLE `Adverb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `Articles`
--
ALTER TABLE `Articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `Conjunction`
--
ALTER TABLE `Conjunction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `Exclamation`
--
ALTER TABLE `Exclamation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `Nouns`
--
ALTER TABLE `Nouns`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `OpeningPhrases`
--
ALTER TABLE `OpeningPhrases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `Prepositions`
--
ALTER TABLE `Prepositions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `Pronoun`
--
ALTER TABLE `Pronoun`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `ProperNouns`
--
ALTER TABLE `ProperNouns`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `Verbs`
--
ALTER TABLE `Verbs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
