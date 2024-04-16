from fastapi import HTTPException
import traceback

async def output_json_creator(tuple_keys, tuple_values):
    try:
        output_json = [{tuple_keys[i]: tuple_value[i] for i in range(len(tuple_keys))} for tuple_value in tuple_values]
        return output_json

    except Exception as e:
        print('ERROR FOUND')
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
