from typing import Any
import httpx

async def make_nws_request(url: str) -> dict[str,Any] | None : 
    """ Make a request ti the NWS API with proper error handling"""

    headers = {
        "user-Agent" : "weather-app/1.0",
        "Accept" : "application/geo+json"
    }

    async with httpx.AsyncClient() as client : 

        try : 
            response = await client.get(url , headers=headers , timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception : 
            return None
        

def format_alert(feature : dict) -> str : 
    """Format an alert feature into a readable string"""

    props = feature["properties"]

    return f"""
        Event: {props.get('event', 'Unknown')}
        Area: {props.get('areaDesc', 'Unknown')}
        Severity: {props.get('severity', 'Unknown')}
        Description: {props.get('description', 'No description available')}
        Instructions: {props.get('instruction', 'No specific instructions provided')}
        """



def format_search(docs) : 
    hasil = []
    props = [doc for doc in docs]

    for prop in props : 
      hasil.append(  f"""
        title : {prop.metadata['title']},
        source : {prop.metadata['source']},
        dontent : {prop.page_content}
        
        """)
      
    return "\n---\n".join(hasil)

