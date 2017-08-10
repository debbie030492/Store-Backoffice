from bottle import route, run, template, static_file, get, post, delete, request
import json
import pymysql


# Connect to the database
connection = pymysql.connect(host='sql11.freesqldatabase.com',
                             user='sql11189248',
                             password='RAJh95pZfe',
                             db='sql11189248',
                             charset='utf8mb4',
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)


@get("/admin")
def admin_portal():
	return template("pages/admin.html")

#LIST CATEGORIES
@get("/categories")
def list_categories():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM category ORDER BY name ASC;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS', 'CATEGORIES':result, 'CODE':200})
    except Exception:
            return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error', 'CODE':500})

#LIST PRODUCTS
@get("/products")
def list_products():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product ORDER BY title ASC;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS', 'PRODUCTS':result, 'CODE':200})
    except Exception:
            return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error', 'CODE':500})

#LIST PRODUCTS BY CATEGORY
@get("/category/<id>/products")
def list_products_by_category(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product WHERE category={} ;".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS': 'SUCCESS', 'PRODUCTS':result, 'CODE':200})
    except Exception:
            return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error', 'CODE':500})

#GETTING PRODUCT
@get("/product/<id>")
def getting_product(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product WHERE id={};".format(id)
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS', 'PRODUCTS':result, 'CODE':200})
    except Exception:
            return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error', 'CODE':500})

#DELETING PRODUCT
@delete("/product/<id>")
def deleting_product(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM product WHERE id={0};".format(id)
            cursor.execute(sql)
            connection.commit()
            return json.dumps({'STATUS':'SUCCESS', 'CODE':201})
    except Exception:
            return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error', 'CODE':500})

#DELETING CATEGORY
@delete("/category/<id>")
def deleting_category(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM category WHERE id={0};".format(id)
            sql1 = "DELETE FROM product WHERE category={0};".format(id)
            cursor.execute(sql)
            cursor.execute(sql1)
            connection.commit()
            return json.dumps({'STATUS':'SUCCESS', 'CODE':201})
    except Exception:
            return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error', 'CODE':500})

#CREATING CATEGORY
@post('/category')
def creating_categories():
    try:
        with connection.cursor() as cursor:
            name = request.POST.get("name")
            sql = "INSERT INTO category VALUES (id, '{}')".format(name)
            cursor.execute(sql)
            connection.commit()
            return json.dumps ({'STATUS':'SUCCESS','CODE':201})
    except Exception:
        return json.dumps({'STATUS':'ERROR', 'MSG': 'Internal error', 'CODE': 500})

#CREATING/EDIT PRODUCT
@post('/product')
def creating_products():
    title = request.POST.get('title')
    description = request.POST.get('desc')
    price = request.POST.get('price')
    img_url = request.POST.get('img_url')
    category = request.POST.get('category')
    favorite = request.POST.get('favorite')
    if favorite:
        fav = True
    else:
        fav= False
    try:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) FROM product WHERE title='{}'".format(title)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result['COUNT(*)']>0:
                sql_update = "UPDATE product SET description='{0}', price={1}, img_url='{2}', category={3}, favorite={4} WHERE title='{5}'".format(description, price, img_url, category, fav, title)
                print sql_update
                cursor.execute(sql_update)
                product_id=0
                connection.commit()
            else:
                sql_add = "INSERT INTO product VALUES (id, '{0}', '{1}', {2}, '{3}', {4}, {5})".format(title, description, price, img_url, category, fav)
                cursor.execute(sql_add)
                product_id = cursor.lastrowid
                connection.commit()
        return json.dumps ({'STATUS':'SUCCESS','PRODUCT_ID':product_id, 'CODE':201})
    except Exception:
        return json.dumps({'STATUS':'ERROR', 'MSG': 'Internal error', 'CODE': 500})



@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|jpeg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


run(host='localhost', port=7000)

if __name__ == '__main__':
    main()