CREATE TABLE category (
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(50));

INSERT INTO category (name) VALUES ("France");
INSERT INTO category (name) VALUES ("Switzerland");
INSERT INTO category (name) VALUES ("Spain");

CREATE TABLE product (
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    title VARCHAR(100),
    description TEXT,
    price FLOAT,
    img_url VARCHAR(100),
    category INTEGER,
    favorite BOOLEAN);

INSERT INTO product (title, description, price, img_url, category, favorite)
	VALUES ( 
		"Le 1947 ***", 
		"Le 1947 derives its name from the most prestigious vintage of Château Cheval Blanc and provides the perfect stage for the striking culinary art of chef Yannick Alléno.",
		"350.00",
        "/images/le_1947.jpg",
        1,
        TRUE);

INSERT INTO product (title, description, price, img_url, category, favorite)
	VALUES (
		"Flocons de Sel ***", 
		"An intimate atmosphere, elegance down to the finest detail, the art of authentic mountain life honed to perfection: our gastronomic restaurant located at the heights of Megève offers diners a unique setting.",
		"300.00",
        "/images/flocons_de_sel.jpg",
        1,
        FALSE);

INSERT INTO product (title, description, price, img_url, category, favorite)
	VALUES (
		"Plaza Athénée ***", 
		"Alain Ducasse tells a personal and radical story, continuing the work he began twenty-five years ago. Healthier and more natural, more respectful of the Planet, it delivers a free and nearly instinctive interpretation of Haute Cuisine, revealing the produces’ original flavour, from the noble to the humble, all exceptional.",
		"300.00",
        "/images/plaza_athenee.jpg",
        1,
        FALSE);

INSERT INTO product (title, description, price, img_url, category, favorite)
	VALUES (
		"Restaurant de l'Hôtel de Ville ***", 
		"An exceptional setting to savor the moment. The Restaurant de l'Hotel de Ville de Crissier in Switzerland features Chef Franck Giovannini's signature cuisine.",
		"400.00",
        "/images/hotel_de_ville.jpg",
        2,
        TRUE);

INSERT INTO product (title, description, price, img_url, category, favorite)
	VALUES (
		"Schloss Schauenstein ***", 
		"Schauenstein Schloss Restaurant Hotel – a historical castle which features Andreas Caminada’s award-winning restaurant. Everybody does their best to provide an unforgettable experience.",
		"350.00",
        "/images/schloss.jpg",
        2,
        FALSE);

INSERT INTO product (title, description, price, img_url, category, favorite)
	VALUES (
		"Cheval Blanc ***", 
		"Our Chef de Cuisine Peter Knogl awaits you in the Cheval Blanc with a symphony of aromas, colours and harmonious tastes. Ingeniously prepared from the best nature has to offer us.",
		"350.00",
        "/images/cheval_blanc.jpg",
        2,
        FALSE);

INSERT INTO product (title, description, price, img_url, category, favorite)
	VALUES (
		"El Celler de Can Roca ***", 
		"El Celler de Can Roca is a restaurant in Girona, Catalonia, Spain which was opened in 1986 by the Roca brothers, Joan, Josep and Jordi.",
		"300.00",
        "/images/el_celler.jpg",
        3,
        TRUE);

INSERT INTO product (title, description, price, img_url, category, favorite)
	VALUES (
		"Lasarte ***", 
		"Lasarte is much more than chef Martín Berasategui’s gastronomic vision for Barcelona. It is a spiritual project with the very best team of professionals at its forefront that strives to delight its diners with every aroma and flavour.",
		"250.00",
        "/images/lasarte.jpg",
        3,
        FALSE);

INSERT INTO product (title, description, price, img_url, category, favorite)
	VALUES (
		"DiverXo ***", 
		"With food served on ‘canvasses’, and sauces painted on to dishes, the phrase ‘works of art’ certainly comes to mind when describing Spanish fusion restaurant DiverXo. With young Madrid-born chef David Muñoz at the pass it’s no surprise that hearty Iberian traditions meet the fragrant flavours of China and Japan.",
		"250.00",
        "/images/diver_xo.jpg",
        3,
        FALSE);

SELECT * FROM product;
SELECT * FROM category;




