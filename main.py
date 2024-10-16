import os
import streamlit as st 
from openai import OpenAI

client = OpenAI(api_key = os.environ['OPENAI_API_KEY'])

st.title("Academy Fighter")
st.write("Welcome to Academy Fighter, a tool for solving mathematics questions.")

def question():
  system_prompt = """
  You are a helpful assistant that can answer questions about grade 6 mathematics question,
  show the solving step by step. And show the symbol instead of word like x instead of
  /times. Dont show \boxed. Make it tidy.

  replace "/" to ÷ and "x" to ×. No necessary need bracket for every question.

  The prompt will be in this format:
  Question 1: (Next line)
  (a) Q1a
  (b) Q2b
  (c) Q3c
  ...
  (one empty line)
  Question 2: (Next line)
  (a) Q2a
  (b) Q2b
  ...

  """

  response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": 
        """
1 Calculate.
  a) (1/5)/5=
  b) (6/7)/9=
  c) (7/3)/28=
  d) (39/4)/30=

2 Calculate
  a) (1/2)/(1/6)=
  b) (5/8)/(2/7)=
  c) (7/9)/(2/3)=
  d) (25/6)/(5/9)=
  e) (52/5)/(5/9)=
  f) (10/7)/(3/4)=

3 Solve these
  a) How many 1/5 are there in 2/9 ?
  b) How many 5/6 are there in 17/10 ?
  c) There are 42 parts of 1/4m in 21/2m of fabric. Is the statement true? Prove it.

4. Find the value in (x)
  a) (1/8)/x=1/6
  b) x/(9/10)=11/6
  c) (3/2)/x=2
  d) x/4=2/5

5 Calculate 
  a) what is (1/2)/3?
  b) how many 3/7 are there in 3/5?
  c) divide 64/9 by 2/3
  d) is (5/4)/(3/10) the same as (3/10)/(5/4)? Prove it"""
      }
    ],
  temperature = 0.1,
  max_tokens = 2000
)
  return response.choices[0].message.content 


def answer():
  system_prompt = """
  This is the answer for question that given just now.
  """

  response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": 
        """Answer
1)a) (1/5)/5=(1/5)*(1/5)=1/25
  b) (6/7)/9=(6/7)*(1/9)=6/63=2/21
  c) (7/3)/28=1/12
  d) (39/4)/30=13/40

2)a) (1/2)/(1/6)=(1/2)*(6/1)=6/2=3
  b) (5/8)/(2/7)=(5/8)*(7/2)=35/16
  c) (7/9)/(2/3)=7/6
  d) (25/6)/(5/9)=15/2
  e) (52/5)/(5/9)=468/25
  f) (10/7)/(3/4)=40/21

3)a) 10/9
  b) 51/25
  c) 42. Yes the statement is true

4)a) (1/8)/x=1/6   1/8=(1/6)*x   x=(1/8)/(1/6)=(1/8)*6=3/4
  b) x=33/20
  c) x=3/4
  d) 8/5

5)a) 1/6
  b) 7/5
  c) 32/3
  d) 25/6   6/25   No, they are not the same"""
      }
    ],
  temperature = 0.1,
  max_tokens = 2000
)
  return response.choices[0].message.content 

content = question()
content2 = answer()

st.write(content)