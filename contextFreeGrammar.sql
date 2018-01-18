-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 18, 2018 at 06:07 PM
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
(1, 'sad', 23),
(2, 'happy', 19),
(3, 'glum', 10),
(4, 'suspicious', 17),
(5, 'red', 23),
(6, 'evil', 44),
(7, 'ferocious', 22),
(8, 'blue', 22),
(9, 'slow', 20),
(10, 'fast', 15),
(11, 'old', 16),
(12, 'energetic', 21),
(13, 'unusual', 20),
(14, 'apathetic', 17),
(15, 'emotionless', 11),
(16, 'informative', 20);

-- --------------------------------------------------------

--
-- Table structure for table `Adverb`
--

CREATE TABLE `Adverb` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `frequency` int(11) NOT NULL,
  `type` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Adverb`
--

INSERT INTO `Adverb` (`id`, `word`, `frequency`, `type`) VALUES
(1, 'nearly', 25, 'degree'),
(2, 'happily', 28, 'manner'),
(3, 'endlessly', 32, 'frequency'),
(4, 'quickly', 17, 'manner'),
(5, 'cheerfully', 35, 'manner'),
(6, 'truthfully', 35, 'manner'),
(7, 'there', 26, 'place'),
(8, 'never', 4, 'time'),
(9, 'recently', 2, 'time'),
(10, 'everywhere', 2, 'place'),
(11, 'above', 2, 'place'),
(12, 'loudly', 2, 'manner'),
(13, 'almost', 2, 'degree'),
(14, 'hardly', 3, 'degree'),
(15, 'normally', 1, 'frequency'),
(16, 'sometimes', 0, 'frequency');

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
(1, 'the', 'definite', 214),
(2, 'a', 'indefinite', 246),
(3, 'an', 'indefinite', 220);

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
(1, 'and', 62),
(2, 'but', 73),
(3, 'or', 54),
(4, 'yet', 0);

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
(1, 'ouch', 129),
(2, 'yikes', 127),
(3, 'thank goodness', 125),
(4, 'oh crap', 102),
(5, 'boom', 123),
(6, 'c-c-c-combo breaker', 116),
(7, 'yay', 109);

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
(1, 'girl', 'person', 12, 'no'),
(2, 'school', 'place', 27, 'no'),
(3, 'dude', 'person', 25, 'no'),
(4, 'vest', 'thing', 30, 'no'),
(5, 'octopus', 'thing', 32, 'no'),
(6, 'pencil', 'thing', 26, 'no'),
(7, 'hour', 'idea', 2, 'no'),
(8, 'century', 'idea', 1, 'no'),
(9, 'mile', 'idea', 1, 'no'),
(10, 'light-year', 'idea', 0, 'no'),
(11, 'home', 'place', 26, 'no'),
(12, 'classroom', 'place', 30, 'no'),
(13, 'bedroom', 'place', 25, 'no'),
(14, 'teeth', 'thing', 13, 'yes'),
(15, 'boxes', 'thing', 21, 'yes'),
(16, 'stores', 'place', 10, 'yes'),
(17, 'women', 'person', 11, 'yes'),
(18, 'theories', 'idea', 0, 'yes'),
(19, 'apocalypse', 'thing', 49, 'no'),
(20, 'golf', 'idea', 0, 'no'),
(21, 'apple', 'thing', 17, 'no'),
(22, 'apples', 'thing', 18, 'yes'),
(23, 'programmer', 'person', 6, 'no'),
(24, 'oligarchy', 'thing', 3, 'no'),
(25, 'hegemon', 'person', 4, 'no'),
(26, 'atlas', 'thing', 11, 'no'),
(27, 'citizen', 'person', 6, 'no'),
(28, 'champion', 'person', 5, 'no'),
(29, 'igloo', 'thing', 13, 'no'),
(30, 'igloos', 'thing', 19, 'yes'),
(31, 'accountants', 'person', 14, 'yes'),
(32, 'acid', 'thing', 14, 'no'),
(33, 'adolescent', 'person', 16, 'no'),
(34, 'airplane', 'thing', 11, 'no'),
(35, 'amateurs', 'person', 15, 'yes'),
(36, 'airstrip', 'place', 31, 'no'),
(37, 'airstrips', 'place', 17, 'yes'),
(38, 'ammo', 'thing', 14, 'yes'),
(39, 'uniforms', 'thing', 10, 'yes'),
(40, 'uncle', 'person', 25, 'no'),
(41, 'uncles', 'person', 12, 'yes'),
(42, 'eggs', 'thing', 10, 'yes'),
(43, 'epidemic', 'thing', 13, 'no'),
(44, 'emerald', 'thing', 21, 'no'),
(45, 'emeralds', 'thing', 22, 'yes'),
(46, 'engine', 'thing', 24, 'no'),
(47, 'field', 'place', 11, 'no'),
(48, 'man', 'person', 2, 'no'),
(49, 'bus stop', 'place', 5, 'no'),
(50, 'country', 'place', 9, 'no'),
(51, 'states', 'place', 2, 'yes'),
(52, 'office', 'place', 1, 'no'),
(53, 'rubber duck', 'thing', 0, 'no'),
(54, 'rubber ducks', 'thing', 0, 'yes'),
(55, 'eon', 'idea', 0, 'no'),
(56, 'eons', 'idea', 0, 'yes');

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
(1, 'a long time ago in a galaxy far, far away...', 80, 'past'),
(2, 'back in my day,', 96, 'past'),
(3, 'in the beginning...', 82, 'past'),
(4, 'good morning,', 81, 'present'),
(5, 'it was a dark and stormy night...', 97, 'past'),
(6, 'it all started last friday...', 46, 'past'),
(7, 'as we speak,', 44, 'present');

-- --------------------------------------------------------

--
-- Table structure for table `Prepositions`
--

CREATE TABLE `Prepositions` (
  `id` int(11) NOT NULL,
  `word` varchar(50) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Prepositions`
--

INSERT INTO `Prepositions` (`id`, `word`, `frequency`, `type`) VALUES
(1, 'after', 36, 'time'),
(2, 'with', 32, 'agent'),
(3, 'in', 37, 'place'),
(4, 'on', 37, 'place'),
(5, 'by', 11, 'instruments'),
(6, 'into', 17, 'direction'),
(7, 'with the help of', 13, 'instruments'),
(8, 'under', 14, 'place'),
(9, 'at', 15, 'place'),
(10, 'towards', 17, 'direction'),
(11, 'to', 12, 'direction');

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
(1, 'you', 'subjective', 6),
(2, 'mine', 'possessive', 0),
(3, 'myself', 'reflexive', 4),
(4, 'me', 'objective', 0);

-- --------------------------------------------------------

--
-- Table structure for table `ProperNouns`
--

CREATE TABLE `ProperNouns` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `frequency` int(11) NOT NULL,
  `kind` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ProperNouns`
--

INSERT INTO `ProperNouns` (`id`, `word`, `type`, `frequency`, `kind`) VALUES
(1, 'jeremy banks', 'person', 106, NULL),
(2, 'chuck e cheeses', 'place', 44, NULL),
(3, 'rutgers', 'place', 42, NULL),
(4, 'space dementia', 'idea', 20, NULL),
(5, 'the legend of zelda: breath of the wild', 'thing', 18, 'title'),
(6, 'persona 5', 'thing', 19, 'title'),
(7, 'gordan freeman', 'person', 120, NULL),
(8, 'nikloa tesla', 'person', 115, NULL),
(9, 'buffalo', 'place', 33, NULL),
(10, 'new jersey', 'place', 26, NULL),
(11, 'darth vader', 'person', 107, NULL),
(12, 'ozzy osbourne', 'person', 86, NULL),
(13, 'nolan bushnell', 'person', 68, NULL),
(14, 'route 66', 'place', 12, NULL),
(15, 'virtual boy', 'thing', 5, 'product'),
(16, 'Phillies', 'thing', 4, 'group'),
(17, 'nirvana', 'thing', 5, 'group'),
(18, 'muse', 'thing', 6, 'group'),
(19, 'interstellar', 'thing', 6, 'title'),
(20, 'lg tv', 'thing', 4, 'product'),
(21, 'gtx 1080 ti', 'thing', 2, 'product'),
(22, 'harry potter and the half-blood prince', 'thing', 3, 'title'),
(23, 'bill nye', 'person', 24, NULL),
(24, 'neil degrasse tyson', 'person', 18, NULL),
(25, 'metal gear solid', 'thing', 2, 'title');

-- --------------------------------------------------------

--
-- Table structure for table `Verbs`
--

CREATE TABLE `Verbs` (
  `id` int(11) NOT NULL,
  `word` varchar(255) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `frequency` int(11) NOT NULL,
  `tense` varchar(50) DEFAULT NULL,
  `kind` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Verbs`
--

INSERT INTO `Verbs` (`id`, `word`, `type`, `frequency`, `tense`, `kind`) VALUES
(1, 'jump', 'action', 25, 'present', 'direction'),
(2, 'snow', 'event', 14, 'present', 'place'),
(3, 'seem', 'situation', 4, 'present', NULL),
(4, 'evolve', 'change', 16, 'present', 'instruments'),
(5, 'swim', 'action', 23, 'present', 'direction'),
(6, 'swam', 'action', 32, 'past', 'direction'),
(7, 'ran', 'action', 42, 'past', 'direction'),
(8, 'evolved', 'change', 30, 'past', 'instruments'),
(9, 'participated', 'action', 25, 'past', 'time'),
(10, 'has', 'situation', 3, 'present', NULL),
(11, 'had', 'situation', 4, 'past', NULL),
(12, 'happened', 'event', 11, 'past', 'time'),
(13, 'rained', 'event', 19, 'past', 'place'),
(14, 'hailed', 'event', 21, 'past', 'place'),
(15, 'stopped', 'action', 35, 'past', 'time'),
(16, 'explored', 'action', 36, 'past', 'place'),
(17, 'was', 'situation', 4, 'past', NULL),
(18, 'shrink', 'change', 14, 'present', 'instruments'),
(19, 'grow', 'change', 11, 'present', 'instruments'),
(20, 'grew', 'change', 30, 'past', 'instruments'),
(21, 'is', 'situation', 1, 'present', NULL),
(22, 'be', 'situation', 1, 'present', NULL),
(23, 'yawned', 'action', 34, 'past', 'agent'),
(24, 'protected', 'action', 38, 'past', NULL),
(25, 'watched', 'action', 3, 'past', NULL),
(26, 'procrastinated', 'action', 3, 'past', 'time'),
(27, 'noticed', 'action', 3, 'past', NULL),
(28, 'see', 'action', 2, 'present', 'NULL'),
(29, 'mutated', 'change', 1, 'past', 'instruments'),
(30, 'kick', 'action', 3, 'present', 'direction');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `Adverb`
--
ALTER TABLE `Adverb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `Articles`
--
ALTER TABLE `Articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `Conjunction`
--
ALTER TABLE `Conjunction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `Exclamation`
--
ALTER TABLE `Exclamation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `Nouns`
--
ALTER TABLE `Nouns`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;
--
-- AUTO_INCREMENT for table `OpeningPhrases`
--
ALTER TABLE `OpeningPhrases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `Prepositions`
--
ALTER TABLE `Prepositions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `Pronoun`
--
ALTER TABLE `Pronoun`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `ProperNouns`
--
ALTER TABLE `ProperNouns`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `Verbs`
--
ALTER TABLE `Verbs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
