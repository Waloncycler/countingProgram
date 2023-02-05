""" 
Path    : apis.py.py
Function:
coding  : utf-8
Version : V1.0
Time    : 2023/2/4 9:56
Author  : Walon Cyler
Modified: 
"""
shared_definitions = \
    {
        "Expenses": {
            "type": "object",
            "properties": {
                "expense list": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/ExpenseDto"
                    }
                }
            }
        },
        "ExpenseDto": {
            "type": "object",
            "properties": {
                "item": {
                  "type": "string"
                },
                "spend": {
                    "type": "string"
                },
                "category": {
                    "type": "string"
                }
            }
        },
        "Expense": {
            "type": "object",
            "properties": {
                "id": {
                "type": "string"
                },
                "datetime": {
                "type": "string",
                "default": "00-00-00"
                },
                "item": {
                  "type": "string"
                },
                "spend": {
                    "type": "string"
                },
                "category": {
                    "type": "string"
                }
            }
        }
    }

accounting_post = {
    "definitions": shared_definitions,
    "parameters": [
        {
            "name": "消费记录",
            "in": "body",
            "type": "object",
            "required": "true",
            "schema": {
                "$ref": "#/definitions/ExpenseDto"
            }
        }
    ],
    "responses": {
        "200": {
            "description": "消费记录上传成功!",
            "schema": {
                "$ref": "#/definitions/Expense"
            }
        }
    }
}

accounting_get = {
    "definitions": shared_definitions,
    "parameters": [
        {
            "name": "花销类型",
            "in": "query",
            "type": "string",
            "description": "请选择花销类型",
            "enum": [
                "Food",
                "Social",
                "Housing",
                "Medical",
                "Others"
            ]
        }
    ],
    "responses": {
        "200": {
            "schema": {
                "$ref": "#/definitions/Expenses"
            }
        },
        "500": {
            "description": "internal server error!"
        }
    }
}