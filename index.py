import json
import os

FILE_SOURCE = './data_mini.json'
DIR_OUTPUT = './content'

with open(FILE_SOURCE, 'r') as content:
  posts = json.load(content)
  for post in posts:
    html = post.get('html').replace("\\/", "/").encode().decode('unicode_escape')

    # Create folders with slug name
    os.makedirs(f"{DIR_OUTPUT}/{post.get('slug')}")
    
    with open(f"{DIR_OUTPUT}/{post.get('slug')}/index.md", 'w') as file:
      file.write('---\n')
      file.write(f"title: {post.get('title')}\n")
      file.write(f"date: {post.get('created_at')}\n")
      file.write(f"description: \n")
      file.write(f"slug: {post.get('slug')}\n")
      file.write(f"feature_image: {post.get('feature_image')}\n")
      file.write('---\n\n')
      file.write(html)