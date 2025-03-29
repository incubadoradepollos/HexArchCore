import json
import requests
class OpenIAAdapter():
    def __init__(self, token):
        self.token = token

    def get_text_chat_context(self, model, context, prompt):
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": context
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
            "max_tokens": 500
        }
        
        ia_response = self.get_v1_chat_completions(payload)                
        contenido_str = ia_response['choices'][0]['message']['content']
        return contenido_str
    
    def get_text_chat_context_json(self, model, context, prompt):
        content_ia = self.get_text_chat_context(model,context,prompt)
        # print(content_ia)
        contenido_str = content_ia.strip("```json").strip("```").strip()                
        return (json.loads(contenido_str))
        

    def get_text_chat(self,model,prompt):
        payload = {
                        "model": model,
                        "messages": [
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": prompt
                                    }                                    
                                ]
                            }
                        ],
                        "max_tokens": 500
                    }
        
        ia_response = self.get_v1_chat_completions(payload)        
        contenido_str = ia_response['choices'][0]['message']['content']
        return contenido_str


    def get_image_chat (self, model, image_base64, prompt): 

        payload = {
                        "model": model,
                        "messages": [
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": prompt
                                    },
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{image_base64}"
                                        }
                                    }
                                ]
                            }
                        ],
                        "max_tokens": 500
                    }
        
        ia_response = self.get_v1_chat_completions(payload)
        #print(ia_response)
        contenido_str = ia_response['choices'][0]['message']['content']


        return contenido_str
        # Eliminar los delimitadores de código (```json ... ```)
        contenido_str = contenido_str.strip("```json").strip("```").strip()

        # Convertir la cadena JSON en un diccionario de Python
        contenido_json = json.loads(contenido_str)
        return contenido_json[0]

        return [contenido_json[0]['nombre'], contenido_json[0]['descripcion']]        
    
    def get_v1_chat_completions(self, payload):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        return requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload).json()