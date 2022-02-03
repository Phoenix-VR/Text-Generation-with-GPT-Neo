from fastapi import FastAPI
from pydantic import BaseModel
from main import hello
from happytransformer import HappyGeneration, GENSettings

app = FastAPI()
happy_tc = HappyGeneration(load_path="model/")

def generate_text(prompt,min_length,max_length,temperature,no_repeat,bad_words):
    args= GENSettings(min_length,max_length,temperature=temperature,no_repeat_ngram_size=no_repeat,bad_words=bad_words)
    result = happy_tc.generate_text(prompt,args=args)
    return result

@app.post('/')
async def create_item(prompt:hello.prompt,min_length:hello.min_length,max_length:hello.max_length,temperature:hello.temperature,no_repeat:hello.no_repeat_ngram_size,bad_words:hello.bad_words):
    r = generate_text(prompt,min_length,max_length,temperature,no_repeat,bad_words)
    return {'generated_text':r}