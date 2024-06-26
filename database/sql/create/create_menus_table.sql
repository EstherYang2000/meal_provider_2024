CREATE TABLE menus (
    menu_id VARCHAR(50) PRIMARY KEY,
    restaurant_id VARCHAR(50) NOT NULL,
    menu_name VARCHAR(255) NOT NULL,
    menu_description TEXT,
    active_from TIMESTAMPTZ,
    active_to TIMESTAMPTZ,
    created_time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);
