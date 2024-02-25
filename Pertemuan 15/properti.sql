-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 19 Feb 2024 pada 17.36
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `properti`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `properti`
--

CREATE TABLE `properti` (
  `id` int(11) NOT NULL,
  `kode_tempat` varchar(10) NOT NULL,
  `nomor_ktp` varchar(16) NOT NULL,
  `nomor_hp` varchar(12) NOT NULL,
  `nama_pelanggan` varchar(50) NOT NULL,
  `tanggal` date NOT NULL,
  `tanggal_mulai` date NOT NULL,
  `tanggal_selesai` date NOT NULL,
  `tarif` int(10) NOT NULL,
  `total_bayar` int(10) NOT NULL,
  `status_bayar` enum('tagihan','lunas') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `properti`
--

INSERT INTO `properti` (`id`, `kode_tempat`, `nomor_ktp`, `nomor_hp`, `nama_pelanggan`, `tanggal`, `tanggal_mulai`, `tanggal_selesai`, `tarif`, `total_bayar`, `status_bayar`) VALUES
(1, '001', '3209052505050001', '082219666171', 'Daffa', '2024-02-13', '2024-02-18', '2024-02-18', 10000000, 10000000, 'lunas'),
(2, '002', '3205050505050001', '082211335511', 'Pratama', '2024-02-15', '2024-02-25', '2024-02-25', 15000000, 15000000, 'lunas'),
(3, '003', '3202030105070001', '082211339901', 'Raditha', '2024-02-16', '2024-02-27', '2024-02-27', 15000000, 15000000, 'lunas');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `properti`
--
ALTER TABLE `properti`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode_tempat` (`kode_tempat`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `properti`
--
ALTER TABLE `properti`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
