from pydantic import BaseModel
from typing import Optional


class hello(BaseModel):
    prompt: str 
    min_length: Optional['int'] = 10
    max_length: Optional['int'] = 50
    temperature: Optional['float'] = 1.0
    no_repeat_ngram_size: Optional['int'] = 0
    bad_words:Optional['str'] = None

