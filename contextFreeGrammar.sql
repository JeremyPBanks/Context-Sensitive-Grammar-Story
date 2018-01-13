-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 13, 2018 at 01:53 AM
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
(2, 'happy', 18),
(3, 'glum', 10),
(4, 'suspicious', 16),
(5, 'red', 23),
(6, 'evil', 44),
(7, 'ferocious', 21),
(8, 'blue', 19),
(9, 'slow', 19),
(10, 'fast', 15),
(11, 'old', 14),
(12, 'energetic', 20),
(13, 'unusual', 18),
(14, 'apathetic', 17),
(15, 'emotionless', 10),
(16, 'informative', 18);

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
(1, 'nearly', 20, NULL),
(2, 'happily', 25, 'manner'),
(3, 'endlessly', 26, NULL),
(4, 'quickly', 15, 'manner'),
(5, 'cheerfully', 31, 'manner'),
(6, 'truthfully', 28, 'manner'),
(7, 'there', 25, 'manner');

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
(1, 'the', 'definite', 201),
(2, 'a', 'indefinite', 229),
(3, 'an', 'indefinite', 209);

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
(1, 'and', 54),
(2, 'but', 71),
(3, 'or', 49);

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
(2, 'school', 'place', 25, 'no'),
(3, 'dude', 'person', 23, 'no'),
(4, 'vest', 'thing', 30, 'no'),
(5, 'octopus', 'thing', 32, 'no'),
(6, 'pencil', 'thing', 24, 'no'),
(7, 'hour', 'idea', 0, 'no'),
(8, 'century', 'idea', 0, 'no'),
(9, 'mile', 'idea', 0, 'no'),
(10, 'light-year', 'idea', 0, 'no'),
(11, 'home', 'place', 24, 'no'),
(12, 'classroom', 'place', 29, 'no'),
(13, 'bedroom', 'place', 23, 'no'),
(14, 'teeth', 'thing', 13, 'yes'),
(15, 'boxes', 'thing', 21, 'yes'),
(16, 'stores', 'place', 10, 'yes'),
(17, 'women', 'person', 11, 'yes'),
(18, 'theories', 'idea', 0, 'yes'),
(19, 'apocalypse', 'thing', 49, 'no'),
(20, 'golf', 'idea', 0, 'no'),
(21, 'apple', 'thing', 16, 'no'),
(22, 'apples', 'thing', 18, 'yes'),
(23, 'programmer', 'person', 6, 'no'),
(24, 'oligarchy', 'thing', 2, 'no'),
(25, 'hegemon', 'person', 3, 'no'),
(26, 'atlas', 'thing', 11, 'no'),
(27, 'citizen', 'person', 4, 'no'),
(28, 'champion', 'person', 3, 'no'),
(29, 'igloo', 'thing', 13, 'no'),
(30, 'igloos', 'thing', 19, 'yes'),
(31, 'accountants', 'person', 13, 'yes'),
(32, 'acid', 'thing', 14, 'no'),
(33, 'adolescent', 'person', 15, 'no'),
(34, 'airplane', 'thing', 11, 'no'),
(35, 'amateurs', 'person', 14, 'yes'),
(36, 'airstrip', 'place', 30, 'no'),
(37, 'airstrips', 'place', 16, 'yes'),
(38, 'ammo', 'thing', 14, 'yes'),
(39, 'uniforms', 'thing', 10, 'yes'),
(40, 'uncle', 'person', 24, 'no'),
(41, 'uncles', 'person', 12, 'yes'),
(42, 'eggs', 'thing', 10, 'yes'),
(43, 'epidemic', 'thing', 12, 'no'),
(44, 'emerald', 'thing', 21, 'no'),
(45, 'emeralds', 'thing', 21, 'yes'),
(46, 'engine', 'thing', 22, 'no'),
(47, 'field', 'place', 11, 'no'),
(48, 'man', 'person', 2, 'no'),
(49, 'bus stop', 'place', 4, 'no'),
(50, 'country', 'place', 7, 'no'),
(51, 'states', 'place', 1, 'yes'),
(52, 'office', 'place', 0, 'no'),
(53, 'rubber duck', 'thing', 0, 'no'),
(54, 'rubber ducks', 'thing', 0, 'yes');

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
(1, 'a long time ago in a galaxy far, far away...', 75, 'past'),
(2, 'back in my day,', 87, 'past'),
(3, 'in the beginning...', 75, 'past'),
(4, 'good morning,', 75, 'present'),
(5, 'it was a dark and stormy night...', 85, 'past'),
(6, 'it all started last friday...', 40, 'past'),
(7, 'as we speak,', 39, 'present');

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
(1, 'after', 30, 'time'),
(2, 'with', 29, 'agent'),
(3, 'in', 26, 'place'),
(4, 'on', 32, 'place'),
(5, 'by', 8, 'instruments'),
(6, 'into', 13, 'direction'),
(7, 'with the help of', 9, 'instruments'),
(8, 'under', 11, 'place'),
(9, 'at', 9, 'place'),
(10, 'towards', 13, 'direction'),
(11, 'to', 8, 'direction');

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
  `frequency` int(11) NOT NULL,
  `kind` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ProperNouns`
--

INSERT INTO `ProperNouns` (`id`, `word`, `type`, `frequency`, `kind`) VALUES
(1, 'jeremy banks', 'person', 99, NULL),
(2, 'chuck e cheeses', 'place', 37, NULL),
(3, 'rutgers', 'place', 38, NULL),
(4, 'space dementia', 'idea', 14, NULL),
(5, 'the legend of zelda: breath of the wild', 'thing', 17, 'title'),
(6, 'persona 5', 'thing', 18, 'title'),
(7, 'gordan freeman', 'person', 112, NULL),
(8, 'nikloa tesla', 'person', 107, NULL),
(9, 'buffalo', 'place', 29, NULL),
(10, 'new jersey', 'place', 23, NULL),
(11, 'darth vader', 'person', 100, NULL),
(12, 'ozzy osbourne', 'person', 78, NULL),
(13, 'nolan bushnell', 'person', 63, NULL),
(14, 'route 66', 'place', 6, NULL),
(15, 'virtual boy', 'thing', 2, 'product'),
(16, 'Phillies', 'thing', 2, 'group'),
(17, 'nirvana', 'thing', 3, 'group'),
(18, 'muse', 'thing', 5, 'group'),
(19, 'interstellar', 'thing', 3, 'title'),
(20, 'lg tv', 'thing', 2, 'product'),
(21, 'gtx 1080 ti', 'thing', 2, 'product'),
(22, 'harry potter and the half-blood prince', 'thing', 2, 'title'),
(23, 'bill nye', 'person', 14, NULL),
(24, 'neil degrasse tyson', 'person', 8, NULL),
(25, 'metal gear solid', 'thing', 1, 'title');

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
(2, 'snow', 'event', 13, 'present', 'place'),
(3, 'seem', 'situation', 4, 'present', NULL),
(4, 'evolve', 'change', 12, 'present', 'instruments'),
(5, 'swim', 'action', 21, 'present', 'direction'),
(6, 'swam', 'action', 28, 'past', 'direction'),
(7, 'ran', 'action', 38, 'past', 'direction'),
(8, 'evolved', 'change', 25, 'past', 'instruments'),
(9, 'participated', 'action', 23, 'past', 'time'),
(10, 'has', 'situation', 3, 'present', NULL),
(11, 'had', 'situation', 4, 'past', NULL),
(12, 'happened', 'event', 11, 'past', 'time'),
(13, 'rained', 'event', 15, 'past', 'place'),
(14, 'hailed', 'event', 18, 'past', 'place'),
(15, 'stopped', 'action', 35, 'past', 'time'),
(16, 'explored', 'action', 30, 'past', 'place'),
(17, 'was', 'situation', 4, 'past', NULL),
(18, 'shrink', 'change', 13, 'present', 'instruments'),
(19, 'grow', 'change', 11, 'present', 'instruments'),
(20, 'grew', 'change', 24, 'past', 'instruments'),
(21, 'is', 'situation', 1, 'present', NULL),
(22, 'be', 'situation', 1, 'present', NULL),
(23, 'yawned', 'action', 33, 'past', 'agent'),
(24, 'protected', 'action', 36, 'past', NULL),
(25, 'watched', 'action', 1, 'past', NULL),
(26, 'procrastinated', 'action', 1, 'past', 'time'),
(27, 'noticed', 'action', 0, 'past', NULL),
(28, 'see', 'action', 0, 'present', 'NULL'),
(29, 'mutated', 'change', 0, 'past', 'instruments');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
