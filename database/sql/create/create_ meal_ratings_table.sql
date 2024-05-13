CREATE TABLE meal_ratings (
    rating_id SERIAL PRIMARY KEY,
    menu_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT,
    comment TEXT,
    rating_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (menu_id) REFERENCES Menus(menu_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
)PARTITION BY RANGE (rating_date);