# import os
import os
# import FastAPI
from fastapi import FastAPI, responses, status, UploadFile, File
# import BaseModel from Pydantic
from pydantic import BaseModel
# Import user app from use.py
from user import user

FILEDIRS = "Files"

if not os.path.exists(FILEDIRS):
    os.makedirs(FILEDIRS)

evans = FastAPI(
    title="Evans API",
    description="Evans is learning how to build a RESTful API with FastAPI",
    version="0.0.1"
)
evans.include_router(user, prefix="/v1", tags=["users"])

class Product(BaseModel):
    name: str
    price: str

products = [
    {
        "id": 1,
        "name": "Evans 8th boxers",
        "price": "$49.99"
    },
    {
        "id": 2,
        "name": "Evans 9th boxers",
        "price": "$59.99"
    },
]


# GET, POST, DELETE, PUT, PATCH, WEBSOCKET, WEBHOOK
@evans.get("/")
async def root():
    return responses.JSONResponse({"message": "Hello Code Squad"}, status_code=status.HTTP_200_OK)

@evans.get("/products")
async def allproducts():
    return responses.JSONResponse({"data": products}, status_code=status.HTTP_200_OK)

@evans.get("/products/{product_id}")
async def get_product(product_id: int):
    try:
        data = products[product_id - 1]
        return responses.JSONResponse(data, status_code=status.HTTP_200_OK)
    except Exception as e:
        return responses.JSONResponse({"message": f"Product with {product_id} is not found", "Error": e}, status_code=status.HTTP_404_NOT_FOUND)
    
@evans.post("/products")
async def add_product(product: Product): 
    data = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }
    products.append(data)
    if data:
        return responses.JSONResponse(data, status_code=status.HTTP_200_OK)
    return responses.JSONResponse({"message": "Error in creating new product"}, status_code=status.HTTP_400_BAD_REQUEST)


@evans.put("/products/{product_id}")
async def update(product_id: int, productData: Product):
    retr = products[product_id - 1]
    if retr:
        newData = {
            "id": product_id,
            "name": productData.name,
            "price": productData.price
        }
        products[product_id - 1] = newData
        return responses.JSONResponse(newData, status_code=status.HTTP_200_OK)
    return responses.JSONResponse({"message": "Error in updating  product"}, status_code=status.HTTP_400_BAD_REQUEST)

@evans.delete("/products/{product_id}")
async def delete_product(product_id: int):
    retr = products[product_id - 1]
    if retr:
        del products[product_id - 1]
        return responses.JSONResponse({"message": "Product deleted successfully"}, status_code=status.HTTP_200_OK)
    return responses.JSONResponse({"message": "Error in deleting product"}, status_code=status.HTTP_400_BAD_REQUEST)

@evans.post("/products/upload-image")
async def upload_product_image(file: UploadFile = File(...)):
    filepath = os.path.join(FILEDIRS, file.filename)
    with open(filepath, 'wb') as buffer:
        buffer.write(await file.read())
    return responses.JSONResponse({"file-path": f"/{FILEDIRS}/{file.filename}"},status_code=status.HTTP_201_CREATED)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SwiftTrans - Reliable Transport Solutions</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100">
    <header class="bg-white shadow-md">
        <div class="container mx-auto flex justify-between items-center p-5">
            <h1 class="text-2xl font-bold text-blue-600">SwiftTrans</h1>
            <nav>
                <ul class="flex space-x-6">
                    <li><a href="#services" class="text-gray-600 hover:text-blue-600">Services</a></li>
                    <li><a href="#about" class="text-gray-600 hover:text-blue-600">About</a></li>
                    <li><a href="#contact" class="text-gray-600 hover:text-blue-600">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="text-center py-20 bg-blue-600 text-white">
        <h2 class="text-4xl font-bold">Fast, Reliable & Affordable Transport Services</h2>
        <p class="mt-4 text-lg">Experience seamless travel with our trusted transport solutions.</p>
        <a href="#contact" class="mt-6 inline-block bg-white text-blue-600 px-6 py-3 rounded-full font-semibold">Get Started</a>
    </section>

    <section id="services" class="container mx-auto py-20">
        <h3 class="text-3xl font-semibold text-center text-gray-800">Our Services</h3>
        <div class="grid md:grid-cols-3 gap-10 mt-10">
            <div class="p-6 bg-white shadow-md rounded-lg text-center">
                <h4 class="text-xl font-bold text-blue-600">City Transport</h4>
                <p class="mt-2 text-gray-600">Efficient city-wide transport solutions for individuals and businesses.</p>
            </div>
            <div class="p-6 bg-white shadow-md rounded-lg text-center">
                <h4 class="text-xl font-bold text-blue-600">Logistics & Delivery</h4>
                <p class="mt-2 text-gray-600">Timely and secure cargo and parcel delivery services.</p>
            </div>
            <div class="p-6 bg-white shadow-md rounded-lg text-center">
                <h4 class="text-xl font-bold text-blue-600">Interstate Travel</h4>
                <p class="mt-2 text-gray-600">Comfortable and affordable long-distance travel options.</p>
            </div>
        </div>
    </section>

    <section id="about" class="bg-gray-100 py-20">
        <div class="container mx-auto text-center">
            <h3 class="text-3xl font-semibold text-gray-800">About Us</h3>
            <p class="mt-6 text-gray-600 max-w-2xl mx-auto">At SwiftTrans, we are committed to providing top-quality transport services with safety, efficiency, and affordability at the core of our mission.</p>
        </div>
    </section>

    <section id="contact" class="container mx-auto py-20 text-center">
        <h3 class="text-3xl font-semibold text-gray-800">Get in Touch</h3>
        <p class="mt-4 text-gray-600">Need a ride or have inquiries? Contact us today.</p>
        <a href="mailto:info@swifttrans.com" class="mt-6 inline-block bg-blue-600 text-white px-6 py-3 rounded-full font-semibold">Email Us</a>
    </section>

    <footer class="bg-gray-800 text-white text-center py-6">
        <p>&copy; 2025 SwiftTrans. All rights reserved.</p>
    </footer>
</body>
</html>


"""

@evans.get("/page")
async def get_page():
    return responses.HTMLResponse(html)
