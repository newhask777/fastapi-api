from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from bookings.router import router as router_bookings
from users.router import router as router_users
from hotels.router import router as router_hotels

from pages.router import router as router_pages
from images.router import router as router_images


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")


app.include_router(router_users)
app.include_router(router_bookings) 
app.include_router(router_hotels)
app.include_router(router_pages)
app.include_router(router_images)


origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", 
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)



