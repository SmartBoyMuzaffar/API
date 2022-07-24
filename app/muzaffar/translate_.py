# from django.db import router
from ..database import get_db
from googletrans import Translator
from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.orm import Session
from .. import models

from ..import schemas as sm
##############################################################################################################





router = APIRouter(
    prefix="/Translator",
    tags=["Translator"]
)
m = FastAPI()












trans = Translator()
# id_ = 0


########################################################################################################

# @m.get('/Translator')
@router.get('')
def _():



    return {
        "->" :"You can translate here something! Enter /Enlish page for translate to english anything! Enter /Uzbek page for translate to Uzbek anything!"
    }




# @m.get('/Translator/English/{text}')
@router.get('/English/{text}')
def _(text, db: Session=Depends(get_db)):

    # global id_


    result = trans.translate(text, dest='en').text
        
    # id_ += 1
     
    word = models.trans_(entered=text, translated=result)

    db.add(word)
    db.commit()
    db.refresh(word) 

    return result
    
    
    
    # data = db.query(models.User).filter(models.trans_.entered==text)


    # if not data:
        
    #     # self.text = text
         
    #     result = trans.translate(text, dest='en').text
        
    #     # id_ += 1
         
    #     word = models.trans_(entered=text, translated=result)

    #     db.add(word)
    #     db.commit()
    #     db.refresh(word)

    #     return result

    # else:

    #     return data





# @m.get('/Translator/Uzbek/{text}')
@router.get('/Uzbek/{text}')
def _(text, db: Session=Depends(get_db)):


    # global id_


    result = trans.translate(text, dest='uz').text
        
    # id_ += 1
     
    word = models.trans_(entered=text, translated=result)

    db.add(word)
    db.commit()
    db.refresh(word)

    return result
    


    

    # data = db.query(models.trans_).filter(models.trans_.entered==text).first()


    # if not data:
        
    #     # self.text = text
         
    #     result = trans.translate(text, dest='uz').text
        
    #     # id_ += 1
         
    #     word = models.trans_(entered=text, translated=result)

    #     db.add(word)
    #     db.commit()
    #     db.refresh(word)

    #     return result

    # else:

    #     return data


#####################################################################################################
