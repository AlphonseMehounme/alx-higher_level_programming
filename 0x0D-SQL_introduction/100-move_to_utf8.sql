-- converts hbtn_0c_0 database to UTF8
-- We use ALTER DATABASE
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
USE hbtn_0c_0;
-- ALTER TABLE first_table COLLATE = utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(255) COLLATE utf8mb4_unicode_ci;
