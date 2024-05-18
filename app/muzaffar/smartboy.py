# from django.db import router
from fastapi import *

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


##############################################################################################################
templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/smartboy",
    tags=["smartboy"]
)
m = FastAPI()



@router.get('/', response_class=HTMLResponse)
def _(request: Request):

    return templates.TemplateResponse(request=request, name="smartboy.html")
