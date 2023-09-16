import os
import openai
from flask import Flask, request

# api_key = os.environ["api_key"]
openai.api_key = ""

app = Flask(__name__)

@app.route('/')
def index():
    html= """
    <head>
        <title>오늘 뭐 먹지?</title>
        <style>
             body{
                background-image: url('/static/food.jpg'); 
                background-size: cover;
             }
             
            .center {
               position: absolute;
               top: 50%;
               left: 50%;
               transform: translate(-50%, -50%);
	         }
          
            .transbg {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 30px;
            }
        </style>
     </head>

     <body>
         <div class="center transbg">
         <h1> 음식 레시피 추천 </h1> 
         <h5> 재료를 작성하시면  작성한 재료를 활용한 음식 레시피를 드립니다!<h5> <br/>
          <form action=/gpt ><h3>
              재료 <input type=text name=subject size=80> <h3> <br/>

             <p>칼로리
              <input type="checkbox" name=kal value="0~500">0~500
              <input type="checkbox" name=kal value="500~1000">500~1000
              <input type="checkbox" name=kal value="1000이상" checked>1000이상 
             </p> <br/>

              
              <select name=pick> 
                  <option value="1개">1개</option>
                  <option value="2개">2개</option>
                  <option value="3개">3개</option> 
              </select>
              
              <select name=style> 
                  <option value="중식">중식</option>
                  <option value="일식">일식</option>
                  <option value="양식">양식</option> 
                  <option value="한식">한식</option> 
                  <option value="랜덤">랜덤</option>   
              </select>
              <input type=submit value=선택 />
          </form>
        </div>
     </body>
    """

    return html

@app.route('/gpt')
def gpt():    
    subject = request.args.get("subject", "소세지")    
    pick  = request.args.get("pick", "1개")    
    style = request.args.get("style", "중식")  
    kal   = request.args.get("kal", "") 
    
    prompt = f"""
    당신은 요리사입니다 . 
    아래 조건과 맞는 음식레시피 {pick}를 보여주세요 .
    재료 : {subject}
    음식 종류 : {style}
    칼로리: {kal}
    """
    
    messages = []

    messages.append({"role": "user", "content": prompt})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  messages=messages)    

    res= completion.choices[0].message['content']
    print(res)   
    
    recipe_steps = res.split("\n")
    recipe_html = "<br/>".join([f"{i}. {step}" for i, step in enumerate(recipe_steps, start=1)])

    html = f"""
        <head>
            <title>오늘 뭐 먹지?</title>
            <style>
                body {{
                    background-image: url('/static/recipe.png');
                    background-size: cover;
                }}
                .recipeResult {{
                    margin: 50px auto;
                    padding: 20px;
                    width: 75%;
                    background-color: rgba(255, 255, 255, 0.8);
                }}
                .recipeResult table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                .recipeResult th, .recipeResult td {{
                    padding: 10px;
                    border: 1px solid black;
                }}
                .recipeResult th {{
                    background-color: #f2f2f2;
                }}
                .recipeResult td:last-child {{
                    white-space: pre-line;
                }}
            </style>
        </head>
    
    <body>
        <div class="recipeResult">
            <h2 style="text-align: center;">추천 음식 레시피</h2>
            <table>
                <tr>
                    <th>원하는 재료</th> 
                    <td>{subject}</td>
                </tr>
                <tr>
                    <th>음식 종류</th>
                    <td>{style}</td>
                </tr>
                <tr>
                    <th>칼로리</th>
                    <td>{kal}</td>
                </tr>
                <tr>
                    <th>레시피</th>
                    <td>{res}</td>
                </tr>
            </table>
        </div>
    </body>
    """
    
    return html
     
if __name__ == '__main__':
    app.run(debug=True)
