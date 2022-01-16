/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : py_system

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 14/01/2022 21:48:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for feacture_ifo
-- ----------------------------
DROP TABLE IF EXISTS `feacture_ifo`;
CREATE TABLE `feacture_ifo`  (
  `id` int NOT NULL,
  `name` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `feacture` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of feacture_ifo
-- ----------------------------
INSERT INTO `feacture_ifo` VALUES (1, '张三', '13asd');
INSERT INTO `feacture_ifo` VALUES (2, '李四', 'adssa');
INSERT INTO `feacture_ifo` VALUES (3, 'adsdc', '达到');
INSERT INTO `feacture_ifo` VALUES (4, 'ffsdfw', '发送');
INSERT INTO `feacture_ifo` VALUES (7, '路人乙', '阿达');
INSERT INTO `feacture_ifo` VALUES (8, 'ads', '萨顶顶');

SET FOREIGN_KEY_CHECKS = 1;
