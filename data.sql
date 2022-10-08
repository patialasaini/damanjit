/*
 Navicat Premium Data Transfer

 Source Server         : my
 Source Server Type    : MySQL
 Source Server Version : 80030
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80030
 File Encoding         : 65001

 Date: 08/10/2022 17:02:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for data
-- ----------------------------
DROP TABLE IF EXISTS `data`;
CREATE TABLE `data`  (
  `strikePrice` int NULL DEFAULT NULL,
  `expiryDate` tinytext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `underlying` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `identifier` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `openInterest` double NULL DEFAULT NULL,
  `changeinOpenInterest` double NULL DEFAULT NULL,
  `pchangeinOpenInterest` int NULL DEFAULT NULL,
  `totalTradedVolume` double NULL DEFAULT NULL,
  `impliedVolatility` double NULL DEFAULT NULL,
  `lastPrice` double NULL DEFAULT NULL,
  `change` double NULL DEFAULT NULL,
  `pChange` int NULL DEFAULT NULL,
  `totalBuyQuantity` int NULL DEFAULT NULL,
  `totalSellQuantity` int NULL DEFAULT NULL,
  `bidQty` double NULL DEFAULT NULL,
  `bidprice` int NULL DEFAULT NULL,
  `askQty` double NULL DEFAULT NULL,
  `askPrice` double NULL DEFAULT NULL,
  `underlyingValue` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `InstrumentTye` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `Time stemp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
