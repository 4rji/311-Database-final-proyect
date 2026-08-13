CREATE USER IF NOT EXISTS 'havi_user'@'localhost' IDENTIFIED BY 'havi_pass';
ALTER USER 'havi_user'@'localhost' IDENTIFIED BY 'havi_pass';
GRANT SELECT ON Havi.* TO 'havi_user'@'localhost';
FLUSH PRIVILEGES;
