instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS category;',
    'DROP TABLE IF EXISTS news;',
    'DROP TABLE IF EXISTS user;',
    'SET FOREIGN_KEY_CHECKS=',
    """
        CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            name VARCHAR(100)
        )
    """,
    """
        CREATE TABLE news (
            id_news INT PRIMARY KEY AUTO_INCREMENT,
            id_category INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            title TEXT NOT NULL,
            paragraph1 TEXT NOT NULL,
            paragraph2 TEXT,
            paragraph3 TEXT,
            paragraph4 TEXT,
            paragraph5 TEXT,
            paragraph6 TEXT,
            link_img VARCHAR(100) NOT NULL,
            created_by INT NOT NULL,
            status INT NOT NULL
        )
    """,
    """
        CREATE TABLE category (
            id_category INT PRIMARY KEY AUTO_INCREMENT,
            description VARCHAR(50),
            created_by INT NOT NULL,
            status INT NOT NULL
        )
    """
]